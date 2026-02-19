## System Health Checker – Python IT Monitoring Tool

## Overview
The System Health Checker is a real-time infrastructure monitoring tool built using Python.  
It continuously monitors CPU, memory, and disk utilization, applies configurable threshold logic, and generates health classifications with escalation alerts to simulate production-level IT operations monitoring workflows.

This project is designed to reflect real-world Cloud Support and NOC (Network Operations Center) monitoring practices.

---

## Key Features

### Real-Time Resource Monitoring
- CPU usage monitoring
- Memory utilization tracking
- Disk usage analysis
- Timestamped system checks

### Configurable Threshold-Based Alerting
- Warning and Critical thresholds for each metric
- Dynamic health evaluation (HEALTHY / WARNING / CRITICAL)

### System Health Classification
- Overall system status derived from individual metric states
- Production-style health rollup logic

### Continuous Monitoring Engine
- Periodic polling mechanism
- Configurable monitoring interval
- Simulates real infrastructure monitoring agents

### Structured Logging System
- Timestamped log entries
- Health status logging
- Persistent log file storage for historical tracking

### Escalation Logic
- Tracks consecutive critical states
- Triggers escalation alert after multiple failures
- Reduces false positives using failure tracking logic

---

## Technologies Used

- Python
- psutil (system resource monitoring library)
- Git & GitHub (version control)

---

## Project Structure

```
monitor.py
monitor_threshold.py
monitor_logging.py
monitor_alerts.py
continuous_monitoring.py
system_logs.txt
```

---

## How It Works

1. The system collects CPU, memory, and disk metrics using the `psutil` library.
2. Each metric is evaluated against predefined thresholds.
3. Status is classified as:
   - HEALTHY
   - WARNING
   - CRITICAL
4. Overall system health is determined.
5. Results are printed and logged.
6. Escalation logic triggers alerts after repeated critical states.

---

## Use Case

This project simulates:

- Cloud infrastructure monitoring
- NOC alerting workflows
- Threshold-based production monitoring
- Basic IT operations health tracking

It reflects core monitoring logic used in tools like Nagios, Zabbix, and CloudWatch agents.

---

## Future Improvements

- Store logs in MySQL database
- Web-based monitoring dashboard
- Email alert integration
- Uptime percentage calculation
- Deployment on cloud VM

---

## Author

Developed as part of infrastructure monitoring practice and cloud engineering preparation.

