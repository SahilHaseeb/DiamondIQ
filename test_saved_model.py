
# TEST SAVED MODel

# Ye test  verify karega
# Saved Random Forest model properly load ho raha hai.
# Saved preprocessing pipeline properly load ho rahi hai.
# New diamond input transform ho raha hai.
#  Model us diamond ki price predict kar raha hai.

import joblib
import pandas as pd

# Load saved model
model = joblib.load("models/random_forest_model.pkl")

# Load saved preprocessing pipeline
preprocessor = joblib.load("models/preprocessor.pkl")

print("Model loaded successfully!")
print("Preprocessor loaded successfully!")

# Create sample diamond input
sample_diamond = pd.DataFrame([{
    "carat": 1.0,
    "cut": "Ideal",
    "color": "E",
    "clarity": "SI1",
    "depth": 61.5,
    "table": 55.0,
    "x": 6.4,
    "y": 6.4,
    "z": 3.9,
    "volume": 6.4 * 6.4 * 3.9
}])

# Transform input using saved preprocessor
processed_input = preprocessor.transform(sample_diamond)

# Predict diamond price
predicted_price = model.predict(processed_input)

print(f"Predicted Diamond Price: ${predicted_price[0]:,.2f}")


# Sample Diamond — Predicted Price
# $5,410.41