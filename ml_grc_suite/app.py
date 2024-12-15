
# app.py - Dashboard for ML-GRC Suite

from flask import Flask, render_template, jsonify
import os
import json

app = Flask(__name__)

# Configuration paths
OUTPUT_DIR = "../output"

# Utility to load JSON data
def load_json_data(file_name):
    file_path = os.path.join(OUTPUT_DIR, file_name)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {"error": f"{file_name} not found."}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/risk-prioritization")
def risk_prioritization():
    data = load_json_data("risk_prioritization.json")
    return jsonify(data)

@app.route("/compliance-mappings")
def compliance_mappings():
    data = load_json_data("compliance_mappings.json")
    return jsonify(data)

@app.route("/control-anomalies")
def control_anomalies():
    data = load_json_data("control_anomalies.json")
    return jsonify(data)

@app.route("/third-party-risk")
def third_party_risk():
    data = load_json_data("third_party_risk_scores.json")
    return jsonify(data)

@app.route("/audit-optimization")
def audit_optimization():
    data = load_json_data("audit_optimized.json")
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
