
# risk_prediction.py - Risk Prediction and Prioritization Module for ML-GRC Suite

import json
import logging
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
def load_config(config_path="config.json"):
    with open(config_path, "r") as config_file:
        return json.load(config_file)

# Load historical incident data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

# Train risk prediction model
def train_model(data, target_column, features, model_params):
    try:
        X = data[features]
        y = data[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestRegressor(**model_params)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        logger.info(f"Model trained successfully. MSE: {mse}, R2: {r2}.")
        return model, predictions, y_test
    except Exception as e:
        logger.error(f"Error training model: {e}")
        raise

# Generate risk prioritization output
def generate_risk_prioritization(data, model, features, output_path):
    try:
        data["predicted_risk"] = model.predict(data[features])
        data_sorted = data.sort_values(by="predicted_risk", ascending=False)
        data_sorted.to_json(output_path, orient="records", indent=4)
        logger.info(f"Risk prioritization saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error generating risk prioritization: {e}")
        raise

# Main function
if __name__ == "__main__":
    # Load config
    config = load_config()

    # Risk prediction settings
    data_path = config["risk_prediction"]["data"]["historical_incidents_file"]
    target_column = config["risk_prediction"]["data"]["target_column"]
    features = config["risk_prediction"]["data"]["features"]
    model_params = config["risk_prediction"]["model"]["hyperparameters"]
    output_path = config["risk_prediction"]["output"]["risk_prioritization_file"]

    # Load data and train model
    data = load_data(data_path)
    model, predictions, y_test = train_model(data, target_column, features, model_params)

    # Generate risk prioritization output
    generate_risk_prioritization(data, model, features, output_path)
