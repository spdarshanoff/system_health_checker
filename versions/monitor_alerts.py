import psutil
import datetime
import time

# -----------------------------
# Threshold Configuration
# -----------------------------
CPU_WARNING = 70
CPU_CRITICAL = 90

MEM_WARNING = 75
MEM_CRITICAL = 90

DISK_WARNING = 80
DISK_CRITICAL = 95

CHECK_INTERVAL = 5
LOG_FILE = "system_logs.txt"

critical_counter = 0


def evaluate_metric(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "HEALTHY"


def log_to_file(message):
    with open(LOG_FILE, "a") as file:
        file.write(message + "\n")


def get_system_metrics():
    global critical_counter

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu_status = evaluate_metric(cpu, CPU_WARNING, CPU_CRITICAL)
    mem_status = evaluate_metric(memory, MEM_WARNING, MEM_CRITICAL)
    disk_status = evaluate_metric(disk, DISK_WARNING, DISK_CRITICAL)

    # Overall System Health Logic
    if "CRITICAL" in [cpu_status, mem_status, disk_status]:
        overall_status = "SYSTEM CRITICAL"
        critical_counter += 1
    else:
        overall_status = "SYSTEM HEALTHY"
        critical_counter = 0

    log_message = (
        f"{timestamp} | CPU: {cpu}% ({cpu_status}) | "
        f"Memory: {memory}% ({mem_status}) | "
        f"Disk: {disk}% ({disk_status}) | "
        f"Overall: {overall_status}"
    )

    print(log_message)

    # Escalation Logic
    if critical_counter >= 3:
        alert_message = f"{timestamp} 🚨 ESCALATION ALERT: System critical for 3 consecutive checks!"
        print(alert_message)
        log_to_file(alert_message)

    print("-" * 80)
    log_to_file(log_message)


while True:
    get_system_metrics()
    time.sleep(CHECK_INTERVAL)
