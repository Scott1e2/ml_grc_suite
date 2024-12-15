
# pipeline_orchestration.py - Pipeline Orchestration for ML-GRC Suite

from prefect import Flow, task
import subprocess

# Task to run risk prediction module
@task
def run_risk_prediction():
    subprocess.run(["python", "../modules/risk_prediction.py"])

# Task to run compliance automation module
@task
def run_compliance_automation():
    subprocess.run(["python", "../modules/compliance_automation.py"])

# Task to run control monitoring module
@task
def run_control_monitoring():
    subprocess.run(["python", "../modules/control_monitoring.py"])

# Task to run third-party risk assessment module
@task
def run_third_party_risk():
    subprocess.run(["python", "../modules/third_party_risk.py"])

# Task to run audit optimization module
@task
def run_audit_optimization():
    subprocess.run(["python", "../modules/audit_optimization.py"])

# Orchestrate all tasks
with Flow("ML-GRC Suite Orchestration") as flow:
    risk_prediction = run_risk_prediction()
    compliance_automation = run_compliance_automation()
    control_monitoring = run_control_monitoring()
    third_party_risk = run_third_party_risk()
    audit_optimization = run_audit_optimization()

# Entry point to execute the flow
if __name__ == "__main__":
    flow.run()
