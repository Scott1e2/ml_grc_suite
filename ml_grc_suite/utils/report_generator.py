
# report_generator.py - Standardized Reporting Utility for ML-GRC Suite

import json

def generate_json_report(data, output_file):
    """Generate a JSON report."""
    try:
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
        print(f"JSON report saved successfully to {output_file}.")
    except Exception as e:
        raise Exception(f"Error generating JSON report: {e}")

def generate_text_report(data, output_file):
    """Generate a plain text report."""
    try:
        with open(output_file, "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
        print(f"Text report saved successfully to {output_file}.")
    except Exception as e:
        raise Exception(f"Error generating text report: {e}")
