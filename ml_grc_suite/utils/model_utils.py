
# model_utils.py - Model Management Utility for ML-GRC Suite

import joblib
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score

def evaluate_classification_model(y_true, y_pred):
    """Evaluate a classification model."""
    accuracy = accuracy_score(y_true, y_pred)
    report = {"accuracy": accuracy}
    return report

def evaluate_regression_model(y_true, y_pred):
    """Evaluate a regression model."""
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    report = {"mean_squared_error": mse, "r2_score": r2}
    return report

def save_model(model, file_path):
    """Save a trained model to disk."""
    try:
        joblib.dump(model, file_path)
        print(f"Model saved successfully to {file_path}.")
    except Exception as e:
        raise Exception(f"Error saving model: {e}")

def load_model(file_path):
    """Load a saved model from disk."""
    try:
        model = joblib.load(file_path)
        print(f"Model loaded successfully from {file_path}.")
        return model
    except Exception as e:
        raise Exception(f"Error loading model: {e}")
