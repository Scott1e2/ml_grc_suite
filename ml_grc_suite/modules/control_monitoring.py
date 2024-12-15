
# control_monitoring.py - Continuous Control Monitoring for ML-GRC Suite

import json
import logging
import numpy as np
from sklearn.ensemble import IsolationForest

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
def load_config(config_path="config.json"):
    with open(config_path, "r") as config_file:
        return json.load(config_file)

# Simulate control effectiveness data
def generate_control_data(num_records=100):
    np.random.seed(42)
    # Simulate normal effectiveness scores (80-100% effectiveness)
    normal_data = np.random.uniform(0.8, 1.0, size=(num_records, 1))
    # Introduce anomalies (10-40% effectiveness)
    anomaly_data = np.random.uniform(0.1, 0.4, size=(5, 1))
    return np.vstack((normal_data, anomaly_data))

# Train anomaly detection model
def train_anomaly_model(data, contamination=0.05):
    try:
        model = IsolationForest(contamination=contamination, random_state=42)
        model.fit(data)
        predictions = model.predict(data)
        anomalies = np.where(predictions == -1)[0]
        logger.info(f"Anomaly detection model trained. {len(anomalies)} anomalies detected.")
        return model, anomalies
    except Exception as e:
        logger.error(f"Error training anomaly detection model: {e}")
        raise

# Save anomaly detection results
def save_anomaly_results(data, anomalies, output_path):
    try:
        results = [{"record": int(i), "effectiveness": float(data[i][0])} for i in anomalies]
        with open(output_path, "w") as file:
            json.dump(results, file, indent=4)
        logger.info(f"Anomaly detection results saved to {output_path}.")
    except Exception as e:
        logger.error(f"Error saving anomaly results: {e}")
        raise

# Main function
if __name__ == "__main__":
    # Load config
    config = load_config()

    # Continuous control monitoring settings
    drift_threshold = config["control_monitoring"]["drift_detection_threshold"]
    output_file = "./output/control_anomalies.json"

    # Generate data and train model
    control_data = generate_control_data()
    model, anomalies = train_anomaly_model(control_data, contamination=1-drift_threshold)
    save_anomaly_results(control_data, anomalies, output_file)
