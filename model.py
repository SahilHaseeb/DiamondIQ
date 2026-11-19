
# DIAMOND PRICE PREDICTION
# DATA PREPROCESSING

import pandas as pd
import numpy as np
import joblib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor


#  1: Load Cleaned Dataset

df = pd.read_csv("data/processed/diamonds_cleaned.csv")


#  2: Select Input Features (X)

X = df[
    [
        "carat",
        "cut",
        "color",
        "clarity",
        "depth",
        "table",
        "x",
        "y",
        "z",
        "volume"
    ]
]


#  3: Select Target Variable (y)

y = df["price"]


#  4: Identify Numerical and Categorical Features

numerical_features = [
    "carat",
    "depth",
    "table",
    "x",
    "y",
    "z",
    "volume"
]

categorical_features = [
    "cut",
    "color",
    "clarity"
]


#  5: Encode Categorical Features

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


#  6: Split Dataset into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


#  7: Apply Preprocessing

X_train_processed = preprocessor.fit_transform(X_train)

X_test_processed = preprocessor.transform(X_test)


#  8: Display Results


print("\nOriginal Dataset Shape:", df.shape)

print("\nTraining Data Shape:", X_train_processed.shape)

print("\nTesting Data Shape:", X_test_processed.shape)

print("\nTraining Target Shape:", y_train.shape)

print("\nTesting Target Shape:", y_test.shape)



#  9: LINEAR REGRESSION MODEL

print("LINEAR REGRESSION MODEL TRAINING")

#  Create model
linear_model = LinearRegression()

#  Train model
linear_model.fit(X_train_processed, y_train)

print("\nLinear Regression Model Trained Successfully!")

#  Make predictions
y_pred = linear_model.predict(X_test_processed)

#  Evaluate model
mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

#  Display results
print("\nMODEL PERFORMANCE")

print("MAE:", round(mae, 2))

print("MSE:", round(mse, 2))

print("RMSE:", round(rmse, 2))

print("R2 Score:", round(r2, 4))

print("\nLinear Regression Completed!")



#  10: DECISION TREE REGRESSOR

print("DECISION TREE MODEL TRAINING")

#  Create model
decision_tree_model = DecisionTreeRegressor(
    random_state=42
)

#  Train model
decision_tree_model.fit(X_train_processed, y_train)


#  Make predictions
dt_predictions = decision_tree_model.predict(X_test_processed)

#  Evaluate model
dt_mae = mean_absolute_error(y_test, dt_predictions)

dt_mse = mean_squared_error(y_test, dt_predictions)

dt_rmse = np.sqrt(dt_mse)

dt_r2 = r2_score(y_test, dt_predictions)

#  Display results
print("\nDECISION TREE PERFORMANCE")

print("MAE:", round(dt_mae, 2))
print("MSE:", round(dt_mse, 2))
print("RMSE:", round(dt_rmse, 2))
print("R2 Score:", round(dt_r2, 4))

print("\nDecision Tree Completed!")



#  11: RANDOM FOREST REGRESSOR


print("RANDOM FOREST MODEL TRAINING")

# Create model
random_forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train model
random_forest_model.fit(X_train_processed, y_train)

print("\nRandom Forest Model Trained Successfully!")

# Make predictions
rf_predictions = random_forest_model.predict(X_test_processed)

# Evaluate model
rf_mae = mean_absolute_error(y_test, rf_predictions)

rf_mse = mean_squared_error(y_test, rf_predictions)

rf_rmse = np.sqrt(rf_mse)

rf_r2 = r2_score(y_test, rf_predictions)

# Display results
print("\nRANDOM FOREST PERFORMANCE")

print("MAE:", round(rf_mae, 2))
print("MSE:", round(rf_mse, 2))
print("RMSE:", round(rf_rmse, 2))
print("R2 Score:", round(rf_r2, 4))

print("\nRandom Forest Completed!")




# STEP 12: GRADIENT BOOSTING REGRESSOR

print("GRADIENT BOOSTING MODEL TRAINING")


#  Create model
gradient_model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

#  Train model
gradient_model.fit(X_train_processed, y_train)


#  Make predictions
gb_predictions = gradient_model.predict(X_test_processed)

# Evaluate model
gb_mae = mean_absolute_error(y_test, gb_predictions)

gb_mse = mean_squared_error(y_test, gb_predictions)

gb_rmse = np.sqrt(gb_mse)

gb_r2 = r2_score(y_test, gb_predictions)

#  Display results
print("\nGRADIENT BOOSTING PERFORMANCE")

print("MAE:", round(gb_mae, 2))
print("MSE:", round(gb_mse, 2))
print("RMSE:", round(gb_rmse, 2))
print("R2 Score:", round(gb_r2, 4))

print("\nGradient Boosting Completed!")



# STEP 13: FEATURE IMPORTANCE ANALYSIS


print("FEATURE IMPORTANCE ANALYSIS")

# Get feature names after One-Hot Encoding
feature_names = preprocessor.get_feature_names_out()

# Get Random Forest feature importance
importance_values = random_forest_model.feature_importances_

# Create DataFrame
importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance_values
})

# Sort features by importance
importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

# Display results
print("\nFeature Importance Ranking:")
print(importance_df.to_string(index=False))

# Plot top 15 features
plt.figure(figsize=(12, 7))

sns.barplot(
    data=importance_df.head(15),
    x="Importance",
    y="Feature"
)

plt.title("Top 15 Important Features for Diamond Price Prediction")
plt.xlabel("Importance Score")
plt.ylabel("Features")

plt.tight_layout()

plt.savefig("graphs/16_feature_importance.png")

plt.show()

print("\nFeature Importance Analysis Completed!")




# GRAPH number 17: ACTUAL VS PREDICTED PRICE

# Create graphs folder if  does not exist
os.makedirs("graphs", exist_ok=True)

# Create graph
plt.figure(figsize=(8, 6))

sns.scatterplot(
    x=y_test,
    y=rf_predictions,
    alpha=0.4
)

# Perfect prediction reference line
min_value = min(y_test.min(), rf_predictions.min())
max_value = max(y_test.max(), rf_predictions.max())

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    "r--",
    label="Perfect Prediction"
)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Diamond Prices - Random Forest")
plt.legend()
plt.tight_layout()

# Save graph
plt.savefig("graphs/17_actual_vs_predicted.png")

plt.show()



# GRAPH 18: RESIDUAL / ERROR PLOT

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

os.makedirs("graphs", exist_ok=True)

# Calculate prediction errors
residuals = y_test - rf_predictions

plt.figure(figsize=(8, 6))

sns.scatterplot(
    x=rf_predictions,
    y=residuals,
    alpha=0.4
)

# Zero error reference line
plt.axhline(y=0, color="red", linestyle="--")

plt.xlabel("Predicted Price")
plt.ylabel("Residual Error")
plt.title("Residual Plot - Random Forest")

plt.tight_layout()
plt.savefig("graphs/18_residual_plot.png")
plt.show()


# GRAPH 19: MODEL COMPARISON

# Calculate RMSE for all models
linear_rmse = np.sqrt(mean_squared_error(y_test, y_pred))
dt_rmse = np.sqrt(mean_squared_error(y_test, dt_predictions))
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_predictions))
gb_rmse = np.sqrt(mean_squared_error(y_test, gb_predictions))

# Create comparison DataFrame
comparison = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting"
    ],

    "MAE": [
        mean_absolute_error(y_test, y_pred),
        mean_absolute_error(y_test, dt_predictions),
        mean_absolute_error(y_test, rf_predictions),
        mean_absolute_error(y_test, gb_predictions)
    ],

    "RMSE": [
        linear_rmse,
        dt_rmse,
        rf_rmse,
        gb_rmse
    ],

    "R2 Score": [
        r2_score(y_test, y_pred),
        r2_score(y_test, dt_predictions),
        r2_score(y_test, rf_predictions),
        r2_score(y_test, gb_predictions)
    ]
})

print(comparison.round(4).to_string(index=False))


# MAE Comparison
plt.figure(figsize=(9, 6))

sns.barplot(
    data=comparison,
    x="Model",
    y="MAE"
)

plt.title("Model Comparison - MAE")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("graphs/19a_model_comparison_mae.png")
plt.show()


# RMSE Comparison
plt.figure(figsize=(9, 6))

sns.barplot(
    data=comparison,
    x="Model",
    y="RMSE"
)

plt.title("Model Comparison - RMSE")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("graphs/19b_model_comparison_rmse.png")
plt.show()


# R2 Comparison
plt.figure(figsize=(9, 6))

sns.barplot(
    data=comparison,
    x="Model",
    y="R2 Score"
)

plt.title("Model Comparison - R2 Score")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("graphs/19c_model_comparison_r2.png")
plt.show()


# GRAPH 20: OVERFITTING CHECK

# Predict training data
rf_train_predictions = random_forest_model.predict(
    X_train_processed
)

# Calculate training and testing R2
train_r2 = r2_score(y_train, rf_train_predictions)
test_r2 = r2_score(y_test, rf_predictions)

print(f"Training R2 Score: {train_r2:.4f}")
print(f"Testing R2 Score:  {test_r2:.4f}")

print(f"R2 Difference:     {train_r2 - test_r2:.4f}")


# Create comparison DataFrame
overfitting_data = pd.DataFrame({
    "Dataset": ["Training Data", "Testing Data"],
    "R2 Score": [train_r2, test_r2]
})

# Draw graph
plt.figure(figsize=(8, 6))

sns.barplot(
    data=overfitting_data,
    x="Dataset",
    y="R2 Score"
)

plt.ylim(0, 1.05)
plt.title("Random Forest - Overfitting Check")
plt.ylabel("R2 Score")

plt.tight_layout()
plt.savefig("graphs/20_overfitting_check.png")
plt.show()


print("\nAll graphs generated successfully!")




#  SAVE athe BEST MODEL


# Create models folder
os.makedirs("models", exist_ok=True)

# Save trained Random Forest model
joblib.dump(
    random_forest_model,
    "models/random_forest_model.pkl" #Trained model jo diamond ki price predict karega
)

# Save fitted preprocessing pipeline
joblib.dump(
    preprocessor,
    "models/preprocessor.pkl" #User ke input ko training wale format mein convert karega
)
print("Random Forest model saved!")
print("Preprocessing pipeline saved !")
print("Both files are stored in the models folder.")





