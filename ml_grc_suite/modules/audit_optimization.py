
# audit_optimization.py - Audit Evidence Optimization for ML-GRC Suite

import json
import os
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
def load_config(config_path="config.json"):
    with open(config_path, "r") as config_file:
        return json.load(config_file)

# Load audit evidence from the specified folder
def load_audit_evidence(folder_path):
    evidence = {}
    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                evidence[file_name] = file.read()
        logger.info(f"Loaded {len(evidence)} audit evidence files from {folder_path}.")
    except Exception as e:
        logger.error(f"Error loading audit evidence: {e}")
        raise
    return evidence

# Optimize audit evidence using clustering
def optimize_audit_evidence(evidence, num_clusters=3):
    try:
        evidence_names = list(evidence.keys())
        evidence_texts = list(evidence.values())

        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(evidence_texts)

        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        clusters = kmeans.fit_predict(tfidf_matrix)

        optimized_evidence = {f"Cluster {i}": [] for i in range(num_clusters)}
        for idx, cluster in enumerate(clusters):
            optimized_evidence[f"Cluster {cluster}"].append(evidence_names[idx])

        logger.info("Audit evidence optimized successfully.")
        return optimized_evidence
    except Exception as e:
        logger.error(f"Error optimizing audit evidence: {e}")
        raise

# Save optimized audit evidence to a JSON file
def save_optimized_evidence(optimized_evidence, output_file):
    try:
        with open(output_file, "w") as file:
            json.dump(optimized_evidence, file, indent=4)
        logger.info(f"Optimized audit evidence saved to {output_file}.")
    except Exception as e:
        logger.error(f"Error saving optimized evidence: {e}")
        raise

# Main function
if __name__ == "__main__":
    # Load config
    config = load_config()

    # Audit optimization settings
    evidence_folder = config["audit_optimization"]["evidence_folder"]
    output_file = config["audit_optimization"]["output_optimized_evidence_file"]

    # Load and optimize audit evidence
    evidence = load_audit_evidence(evidence_folder)
    optimized_evidence = optimize_audit_evidence(evidence, num_clusters=3)
    save_optimized_evidence(optimized_evidence, output_file)
