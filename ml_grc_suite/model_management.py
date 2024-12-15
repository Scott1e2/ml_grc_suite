
# model_management.py - Advanced Model Management for ML-GRC Suite

import os
import joblib
import logging
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Save model with versioning
def save_model_with_version(model, model_name, version, directory="./models"):
    try:
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, f"{model_name}_v{version}.joblib")
        joblib.dump(model, file_path)
        logger.info(f"Model saved successfully to {file_path}.")
        return file_path
    except Exception as e:
        logger.error(f"Error saving model: {e}")
        raise

# Load a specific model version
def load_model_by_version(model_name, version, directory="./models"):
    try:
        file_path = os.path.join(directory, f"{model_name}_v{version}.joblib")
        model = joblib.load(file_path)
        logger.info(f"Model loaded successfully from {file_path}.")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise

# Automated retraining pipeline
def retrain_model(data, target_column, features, model_class, model_params, test_size=0.2):
    try:
        X = data[features]
        y = data[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        model = model_class(**model_params)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        if hasattr(model, "predict_proba"):
            score = accuracy_score(y_test, predictions)
            metric = "Accuracy"
        else:
            score = mean_squared_error(y_test, predictions)
            metric = "MSE"

        logger.info(f"Retrained model performance: {metric} = {score}.")
        return model, score
    except Exception as e:
        logger.error(f"Error retraining model: {e}")
        raise
