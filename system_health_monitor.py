import psutil
import datetime
import time

# -----------------------------
# Configuration
# -----------------------------

# CPU Thresholds
CPU_WARNING = 70
CPU_CRITICAL = 90

# Memory Thresholds
MEM_WARNING = 75
MEM_CRITICAL = 90

# Disk Thresholds
DISK_WARNING = 80
DISK_CRITICAL = 95

# Monitoring Settings
CHECK_INTERVAL = 5  # seconds

# Log File
LOG_FILE = "system_logs.txt"

# Escalation Settings
ESCALATION_LIMIT = 3

# -----------------------------
# Metric Evaluation
# -----------------------------

def evaluate_metric(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "HEALTHY"

# -----------------------------
# Logging Function
# -----------------------------

def log_to_file(message):
    with open(LOG_FILE, "a") as file:
        file.write(message + "\n")

# -----------------------------
# Monitoring Engine
# -----------------------------

critical_counter = 0

def monitor_system():
    global critical_counter

    # Collect Metrics
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Evaluate Metrics
    cpu_status = evaluate_metric(cpu, CPU_WARNING, CPU_CRITICAL)
    mem_status = evaluate_metric(memory, MEM_WARNING, MEM_CRITICAL)
    disk_status = evaluate_metric(disk, DISK_WARNING, DISK_CRITICAL)

    # Determine Overall Health
    if "CRITICAL" in [cpu_status, mem_status, disk_status]:
        overall_status = "SYSTEM CRITICAL"
        critical_counter += 1
    elif "WARNING" in [cpu_status, mem_status, disk_status]:
        overall_status = "SYSTEM WARNING"
        critical_counter = 0
    else:
        overall_status = "SYSTEM HEALTHY"
        critical_counter = 0

    # Create Log Message
    log_message = (
        f"{timestamp} | "
        f"CPU: {cpu}% ({cpu_status}) | "
        f"Memory: {memory}% ({mem_status}) | "
        f"Disk: {disk}% ({disk_status}) | "
        f"Overall: {overall_status}"
    )

    print(log_message)
    log_to_file(log_message)

    # Escalation Logic
    if critical_counter >= ESCALATION_LIMIT:
        alert_message = f"{timestamp} 🚨 ESCALATION ALERT: System critical for {ESCALATION_LIMIT} consecutive checks!"
        print(alert_message)
        log_to_file(alert_message)

    print("-" * 80)

# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    print("Starting System Health Monitor...")
    print("=" * 80)

    while True:
        monitor_system()
        time.sleep(CHECK_INTERVAL)
