
# real_time_api.py - REST API for ML-GRC Suite

from flask import Flask, jsonify, request
import subprocess
import os
import json

app = Flask(__name__)

# Paths to module outputs
OUTPUT_DIR = "./output"

# Utility to load JSON data
def load_json_data(file_name):
    file_path = os.path.join(OUTPUT_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {"error": f"{file_name} not found."}

# API endpoint to trigger modules
@app.route("/run-module", methods=["POST"])
def run_module():
    module_name = request.json.get("module")
    module_scripts = {
        "risk_prediction": "../modules/risk_prediction.py",
        "compliance_automation": "../modules/compliance_automation.py",
        "control_monitoring": "../modules/control_monitoring.py",
        "third_party_risk": "../modules/third_party_risk.py",
        "audit_optimization": "../modules/audit_optimization.py",
    }
    script_path = module_scripts.get(module_name)
    if script_path:
        subprocess.run(["python", script_path])
        return jsonify({"status": "success", "message": f"{module_name} module executed."})
    else:
        return jsonify({"status": "error", "message": "Invalid module name."}), 400

# API endpoint to fetch module outputs
@app.route("/get-output/<module>", methods=["GET"])
def get_output(module):
    output_files = {
        "risk_prediction": "risk_prioritization.json",
        "compliance_automation": "compliance_mappings.json",
        "control_monitoring": "control_anomalies.json",
        "third_party_risk": "third_party_risk_scores.json",
        "audit_optimization": "audit_optimized.json",
    }
    file_name = output_files.get(module)
    if file_name:
        data = load_json_data(file_name)
        return jsonify(data)
    else:
        return jsonify({"status": "error", "message": "Invalid module name."}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5001)
