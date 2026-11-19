
# Import required libraries
import os
import sqlite3
import joblib
import pandas as pd

from flask import Flask, request, jsonify, send_from_directory

from database import initialize_database, DATABASE_PATH


# Get the main project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Define folder paths
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
MODEL_DIR = os.path.join(BASE_DIR, "models")


# Load saved Machine Learning model
model = joblib.load(
    os.path.join(MODEL_DIR, "random_forest_model.pkl")
)


# Load saved data preprocessor
preprocessor = joblib.load(
    os.path.join(MODEL_DIR, "preprocessor.pkl")
)


# Create Flask application
app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,
    static_url_path=""
)


# Initialize SQLite database
initialize_database()


# Function to save prediction in database
def save_prediction(data, predicted_price):

    connection = sqlite3.connect(DATABASE_PATH)

    try:
        connection.execute("""
            INSERT INTO predictions (
                carat, cut, color, clarity,
                depth, table_value, x, y, z,
                predicted_price
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["carat"],
            data["cut"],
            data["color"],
            data["clarity"],
            data["depth"],
            data["table"],
            data["x"],
            data["y"],
            data["z"],
            predicted_price
        ))

        connection.commit()

    finally:
        connection.close()


# Open the frontend homepage
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Receive diamond details from JavaScript
        data = request.get_json()

        if not isinstance(data, dict):
            return jsonify({"error": "Invalid input data."}), 400

        # Define allowed categorical values
        allowed_cut = ["Fair", "Good", "Very Good", "Premium", "Ideal"]

        allowed_color = ["D", "E", "F", "G", "H", "I", "J"]

        allowed_clarity = [
            "I1", "SI2", "SI1", "VS2",
            "VS1", "VVS2", "VVS1", "IF"
        ]

        # Read numeric values
        numeric_fields = [
            "carat", "depth", "table", "x", "y", "z"
        ]

        values = {}

        for field in numeric_fields:

            value = float(data[field])

            if not pd.notna(value) or value <= 0:
                return jsonify({
                    "error": f"Invalid value for {field}."
                }), 400

            values[field] = value

        # Validate categorical values
        cut = data.get("cut")
        color = data.get("color")
        clarity = data.get("clarity")

        if cut not in allowed_cut:
            return jsonify({"error": "Invalid cut value."}), 400

        if color not in allowed_color:
            return jsonify({"error": "Invalid color value."}), 400

        if clarity not in allowed_clarity:
            return jsonify({"error": "Invalid clarity value."}), 400

        # Calculate diamond volume
        volume = values["x"] * values["y"] * values["z"]

        # Prepare input in the same feature structure used for training
        input_data = pd.DataFrame([{
            "carat": values["carat"],
            "cut": cut,
            "color": color,
            "clarity": clarity,
            "depth": values["depth"],
            "table": values["table"],
            "x": values["x"],
            "y": values["y"],
            "z": values["z"],
            "volume": volume
        }])

        # Transform input data
        transformed_data = preprocessor.transform(input_data)

        # Predict diamond price
        prediction = model.predict(transformed_data)

        predicted_price = round(float(prediction[0]), 2)

        # Save prediction in SQLite database
        save_prediction(
            {
                **values,
                "cut": cut,
                "color": color,
                "clarity": clarity
            },
            predicted_price
        )

        # Return prediction to JavaScript
        return jsonify({
            "predicted_price": predicted_price,
            "message": "Prediction saved successfully."
        })

    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Please provide all diamond details correctly."
        }), 400

    except Exception as error:
        print("Prediction Error:", error)

        return jsonify({
            "error": "Something went wrong while predicting the price."
        }), 500



# =========================================
# PREDICTION HISTORY API
# =========================================

@app.route("/history", methods=["GET"])
def history():

    try:

        # Connect to SQLite database
        connection = sqlite3.connect(DATABASE_PATH)

        # Get all predictions (newest first)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                carat,
                cut,
                color,
                clarity,
                depth,
                table_value,
                x,
                y,
                z,
                predicted_price,
                created_at
            FROM predictions
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()

        # Close database connection
        connection.close()

        # Calculate total predictions
        total_predictions = len(rows)

        # Calculate average predicted price
        average_price = (
            sum(row[10] for row in rows) / total_predictions
            if total_predictions > 0 else 0
        )

        # Convert database records into JSON-friendly data
        predictions = []

        for row in rows:

            predictions.append({
                "id": row[0],
                "carat": row[1],
                "cut": row[2],
                "color": row[3],
                "clarity": row[4],
                "depth": row[5],
                "table_value": row[6],
                "x": row[7],
                "y": row[8],
                "z": row[9],
                "predicted_price": row[10],
                "created_at": row[11]
            })

        # Send history to JavaScript
        return jsonify({
            "predictions": predictions,
            "total_predictions": total_predictions,
            "average_price": round(average_price, 2)
        })

    except Exception as error:

        print("History Error:", error)

        return jsonify({
            "error": "Could not load prediction history."
        }), 500


# Run Flask development server
if __name__ == "__main__":
    app.run(debug=True)
