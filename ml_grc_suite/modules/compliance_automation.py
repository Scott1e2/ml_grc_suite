
# compliance_automation.py - Compliance Automation Module for ML-GRC Suite

import json
import os
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load configuration
def load_config(config_path="config.json"):
    with open(config_path, "r") as config_file:
        return json.load(config_file)

# Load regulatory texts from the specified folder
def load_regulatory_texts(folder_path):
    documents = {}
    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                documents[file_name] = file.read()
        logger.info(f"Loaded {len(documents)} regulatory documents from {folder_path}.")
    except Exception as e:
        logger.error(f"Error loading regulatory texts: {e}")
        raise
    return documents

# Generate compliance mappings
def generate_compliance_mappings(documents):
    try:
        tfidf_vectorizer = TfidfVectorizer()
        document_names = list(documents.keys())
        document_texts = list(documents.values())
        
        tfidf_matrix = tfidf_vectorizer.fit_transform(document_texts)
        similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

        mappings = {}
        for i, doc_name in enumerate(document_names):
            similar_docs = {
                document_names[j]: float(similarity_matrix[i, j])
                for j in range(len(document_names))
                if i != j and similarity_matrix[i, j] > 0.5
            }
            mappings[doc_name] = similar_docs

        logger.info("Compliance mappings generated successfully.")
        return mappings
    except Exception as e:
        logger.error(f"Error generating compliance mappings: {e}")
        raise

# Save compliance mappings to a JSON file
def save_compliance_mappings(mappings, output_file):
    try:
        with open(output_file, "w") as file:
            json.dump(mappings, file, indent=4)
        logger.info(f"Compliance mappings saved to {output_file}.")
    except Exception as e:
        logger.error(f"Error saving compliance mappings: {e}")
        raise

# Main function
if __name__ == "__main__":
    # Load config
    config = load_config()

    # Compliance automation settings
    regulatory_texts_folder = config["compliance_automation"]["regulatory_texts_folder"]
    output_file = config["compliance_automation"]["output_mappings_file"]

    # Load regulatory texts and generate mappings
    documents = load_regulatory_texts(regulatory_texts_folder)
    mappings = generate_compliance_mappings(documents)
    save_compliance_mappings(mappings, output_file)
