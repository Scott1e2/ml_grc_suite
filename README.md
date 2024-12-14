# ML-GRC Suite
ML enhancement to GRC tooling sets


## Overview

The ML-GRC Suite is a unified platform designed to enhance Governance, Risk, and Compliance (GRC) functions using machine learning. The suite consists of modular tools for risk prediction, compliance automation, continuous control monitoring, third-party risk assessment, and audit evidence optimization.

### Key Features
1. **Risk Prediction and Prioritization**: Analyzes historical incidents to predict and prioritize risks.
2. **Compliance Automation**: Maps regulatory requirements to internal policies using NLP.
3. **Continuous Control Monitoring**: Detects control drift and anomalies in real-time.
4. **Third-Party Risk Assessment**: Scores vendors based on security posture and compliance history.
5. **Audit Evidence Optimization**: Clusters and organizes audit evidence for efficient reviews.

### Enhancements
- **Dashboard Integration**: A web-based interface to visualize results from all modules.
- **Pipeline Orchestration**: Automated workflow execution using Prefect.
- **Real-Time API**: RESTful API to integrate suite functionalities into external systems.
- **Data Encryption**: Secure sensitive outputs with encryption.
- **Advanced Model Management**: Includes model versioning and automated retraining.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repository/ml-grc-suite.git
    cd ml-grc-suite
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Generate Encryption Key** (if not already done):
    ```bash
    python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())" > encryption.key
    ```

## Usage

### Module Execution
Modules can be executed individually or as part of the pipeline orchestration.

#### Run Modules Individually
```bash
python modules/risk_prediction.py
python modules/compliance_automation.py
python modules/control_monitoring.py
python modules/third_party_risk.py
python modules/audit_optimization.py
```

#### Run All Modules via Orchestration
```bash
python pipeline_orchestration.py
```

#### Access the Dashboard
Run the dashboard server:
```bash
python dashboard/app.py
```
Open `http://localhost:5000` in a web browser.

#### Use the REST API
Run the API server:
```bash
python real_time_api.py
```
Interact with endpoints, such as:
- **Run a Module**:
    ```
    POST /run-module
    JSON Body: {"module": "risk_prediction"}
    ```
- **Get Module Output**:
    ```
    GET /get-output/risk_prediction
    ```

### Data Structure

#### Input Files
- `data/historical_incidents.csv`: Historical incidents for risk prediction.
- `data/regulatory_texts/`: Regulatory documents for compliance automation.
- `data/vendor_assessments.csv`: Vendor details for third-party risk assessment.
- `data/audit_evidence/`: Audit evidence files for optimization.

#### Output Files
- `output/risk_prioritization.json`: Risk prediction results.
- `output/compliance_mappings.json`: Compliance mapping outputs.
- `output/control_anomalies.json`: Control monitoring anomalies.
- `output/third_party_risk_scores.json`: Vendor risk scores.
- `output/audit_optimized.json`: Optimized audit evidence.

#### Models
- `models/`: Stores versioned models (e.g., `risk_model_v1.joblib`).

## Support
For issues or suggestions, open an issue on the GitHub repository.

## License
This project is licensed under the MIT License.
