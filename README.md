# Platform Engineer Coding Evaluation

## 📁 Folder Structure

platform-engineer-evaluation/
├── 1_kubernetes_mastery/
│ ├── 1.1_gpu_pod.yaml # GPU-optimized PodSpec
│ └── 1.2_frontend_deployment_networkpolicy.yaml # Secure frontend stack
├── 2_observability/
│ ├── 2.1_otel_instrumentation.py # OpenTelemetry tracing
│ └── 2.2_slo_alerts.yaml # Production SLO alerts
├── 3_airflow/
│ ├── 3.1_etl_dag.py # Resilient ETL pipeline
│ └── 3.2_debugging_guide.md # Task skipping debug guide
├── 4_scripting/
│ ├── 4.1_k8s_validator.py # Kubernetes manifest validator
│ └── 4.2_crashloop_triage.sh # CrashLoopBackOff diagnostics
└── README.md # This file

![image](https://github.com/user-attachments/assets/5551a7a4-1ae9-4137-a9cf-eaeda9a85581)



## 🚀 Quick Start

### 1. Kubernetes Mastery
```bash
# Deploy GPU pod
kubectl apply -f 1_kubernetes_mastery/1.1_gpu_pod.yaml

# Deploy frontend with NetworkPolicy
kubectl apply -f 1_kubernetes_mastery/1.2_frontend_deployment_networkpolicy.yaml


****2. Observability****

bash
# Install OpenTelemetry dependencies
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp

# Run tracing script (requires local OTEL Collector)
python 2_observability/2.1_otel_instrumentation.py

# Deploy SLO alerts to Prometheus
kubectl apply -f 2_observability/2.2_slo_alerts.yaml


3. Airflow

bash
# Copy DAG to Airflow's dags folder
cp 3_airflow/3.1_etl_dag.py ${AIRFLOW_HOME}/dags/

# Debugging guide doesn't require execution
cat 3_airflow/3.2_debugging_guide.md


4. Scripting

bash
# Validate Kubernetes manifests
python 4_scripting/4.1_k8s_validator.py /path/to/manifests/

# Troubleshoot crashing pods (requires kubectl and jq)
chmod +x 4_scripting/4.2_crashloop_triage.sh
./4_scripting/4.2_crashloop_triage.sh


🔍 Detailed Documentation


1. Kubernetes Solutions
File	Purpose	Key Features
1.1_gpu_pod.yaml	GPU workload scheduling	- Node affinity
- Resource limits
- Tolerations
1.2_frontend...yaml	Secure frontend stack	- TLS Ingress
- NetworkPolicy
- Rolling updates

2. Observability
File	Purpose	Dependencies
2.1_otel_instrumentation.py	Distributed tracing	OTEL Collector
2.2_slo_alerts.yaml	Reliability monitoring	Prometheus

3. Airflow
File	Purpose	Best Practices Implemented
3.1_etl_dag.py	Data pipeline	- Task groups
- Exponential backoff
- S3 upload
3.2_debugging...md	Troubleshooting guide	Trigger rules, depends_on_past

4. Scripting Tools
File	Purpose	Output Example
4.1_k8s_validator.py	Manifest validation	JSON error report
4.2_crashloop...sh	Pod diagnostics	Structured logs


🛠️ Technical Requirements

Kubernetes 1.20+

Python 3.8+ (for scripts)

Airflow 2.4+ (for DAGs)

kubectl (configured)

jq (for bash script)
