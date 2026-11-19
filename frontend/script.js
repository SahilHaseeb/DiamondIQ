
// Get the prediction form and result elements
const predictionForm = document.getElementById("prediction-form");
const resultBox = document.getElementById("result");
const predictedPrice = document.getElementById("predicted-price");
const resultMessage = document.getElementById("result-message");

// =========================================
// PREDICTION HISTORY FUNCTION
// =========================================

async function loadHistory() {

    const historyTableBody = document.getElementById("history-table-body");
    const totalPredictions = document.getElementById("total-predictions");
    const averagePrice = document.getElementById("average-price");
    const historyMessage = document.getElementById("history-message");

    try {

        // Request prediction history from Flask
        const response = await fetch("/history");

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Could not load history.");
        }

        // Update statistics
        totalPredictions.textContent = data.total_predictions;

        averagePrice.textContent =
            "$" + Number(data.average_price).toLocaleString("en-US", {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });

        // Clear old table rows
        historyTableBody.replaceChildren();

        // Check if history is empty
        if (data.predictions.length === 0) {

            const row = document.createElement("tr");
            const cell = document.createElement("td");

            cell.colSpan = 7;
            cell.textContent = "No predictions found yet.";

            row.appendChild(cell);
            historyTableBody.appendChild(row);

            historyMessage.textContent = "Make your first diamond prediction!";

            return;
        }

        // Display predictions in the table
        data.predictions.forEach(prediction => {

            const row = document.createElement("tr");

            const values = [
                prediction.id,
                prediction.carat,
                prediction.cut,
                prediction.color,
                prediction.clarity,
                "$" + Number(prediction.predicted_price).toLocaleString("en-US", {
                    minimumFractionDigits: 2,
                    maximumFractionDigits: 2
                }),
                prediction.created_at
            ];

            values.forEach(value => {

                const cell = document.createElement("td");

                cell.textContent = value;

                row.appendChild(cell);

            });

            historyTableBody.appendChild(row);

        });

        historyMessage.textContent =
            "Showing your saved diamond predictions.";

    } catch (error) {

        historyMessage.textContent =
            error.message || "Unable to load prediction history.";

    }
}


// =========================================
// PREDICTION FORM
// =========================================

// Run this code when the user submits the form
predictionForm.addEventListener("submit", async function (event) {

    // Prevent the page from refreshing
    event.preventDefault();

    // Read values from the form
    const diamondData = {
        carat: Number(document.getElementById("carat").value),
        cut: document.getElementById("cut").value,
        color: document.getElementById("color").value,
        clarity: document.getElementById("clarity").value,
        depth: Number(document.getElementById("depth").value),
        table: Number(document.getElementById("table").value),
        x: Number(document.getElementById("x").value),
        y: Number(document.getElementById("y").value),
        z: Number(document.getElementById("z").value)
    };

    // Check numeric values
    const numericValues = [
        diamondData.carat,
        diamondData.depth,
        diamondData.table,
        diamondData.x,
        diamondData.y,
        diamondData.z
    ];

    if (numericValues.some(value => !Number.isFinite(value) || value <= 0)) {
        resultBox.style.display = "block";
        resultMessage.textContent = "Please enter valid positive numbers in all numeric fields.";
        predictedPrice.textContent = "";
        return;
    }

    // Show loading message
    resultBox.style.display = "block";
    predictedPrice.textContent = "Calculating...";
    resultMessage.textContent = "Please wait while we predict your diamond's price.";

    try {

        // Send diamond data to Flask backend
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(diamondData)
        });

        // Convert response into JSON
        const result = await response.json();

        // Check for backend errors
        if (!response.ok) {
            throw new Error(result.error || "Prediction failed.");
        }

        // Display predicted price
        predictedPrice.textContent =
            "$" + Number(result.predicted_price).toLocaleString("en-US", {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });

        resultMessage.textContent =
            "Your diamond's estimated price is ready!";

        // Refresh prediction history after successful prediction
        await loadHistory();

    } catch (error) {

        // Display error message
        predictedPrice.textContent = "Prediction unavailable";
        resultMessage.textContent =
            error.message || "Could not connect to the prediction server.";

    }

    // Scroll to the result
    resultBox.scrollIntoView({
        behavior: "smooth",
        block: "center"
    });

});


// =========================================
// LOAD HISTORY WHEN WEBSITE OPENS
// =========================================

loadHistory();
