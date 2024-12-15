
# third_party_risk.py - Third-Party Risk Assessment for ML-GRC Suite

import json
import pandas as pd
import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
def load_config(config_path="config.json"):
    with open(config_path, "r") as config_file:
        return json.load(config_file)

# Load vendor data
def load_vendor_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Vendor data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        logger.error(f"Error loading vendor data: {e}")
        raise

# Train risk assessment model
def train_risk_model(data, target_column, features):
    try:
        X = data[features]
        y = data[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logger.info(f"Model trained successfully. Accuracy: {accuracy:.2f}.")
        logger.info(classification_report(y_test, predictions))
        return model
    except Exception as e:
        logger.error(f"Error training risk assessment model: {e}")
        raise

# Generate risk scores for vendors
def generate_vendor_risk_scores(data, model, features, output_path):
    try:
        data["risk_score"] = model.predict_proba(data[features])[:, 1]
        data_sorted = data.sort_values(by="risk_score", ascending=False)
        data_sorted.to_json(output_path, orient="records", indent=4)
        logger.info(f"Vendor risk scores saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error generating vendor risk scores: {e}")
        raise

# Main function
if __name__ == "__main__":
    # Load config
    config = load_config()

    # Third-party risk assessment settings
    vendor_data_path = config["third_party_risk"]["vendor_data_file"]
    output_path = config["third_party_risk"]["output_risk_scores_file"]
    target_column = "risk_label"
    features = ["vendor_size", "incident_history", "compliance_score"]

    # Load data and train model
    vendor_data = load_vendor_data(vendor_data_path)
    risk_model = train_risk_model(vendor_data, target_column, features)

    # Generate vendor risk scores
    generate_vendor_risk_scores(vendor_data, risk_model, features, output_path)
