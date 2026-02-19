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

CHECK_INTERVAL = 5  # seconds


def evaluate_metric(value, warning, critical):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    else:
        return "HEALTHY"


def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.datetime.now()

    cpu_status = evaluate_metric(cpu, CPU_WARNING, CPU_CRITICAL)
    mem_status = evaluate_metric(memory, MEM_WARNING, MEM_CRITICAL)
    disk_status = evaluate_metric(disk, DISK_WARNING, DISK_CRITICAL)

    # Overall System Health Logic
    if "CRITICAL" in [cpu_status, mem_status, disk_status]:
        overall_status = "SYSTEM CRITICAL"
    elif "WARNING" in [cpu_status, mem_status, disk_status]:
        overall_status = "SYSTEM WARNING"
    else:
        overall_status = "SYSTEM HEALTHY"

    print("Time:", timestamp)
    print(f"CPU: {cpu}% → {cpu_status}")
    print(f"Memory: {memory}% → {mem_status}")
    print(f"Disk: {disk}% → {disk_status}")
    print("Overall:", overall_status)
    print("-" * 50)


# -----------------------------
# Continuous Monitoring Loop
# -----------------------------
while True:
    get_system_metrics()
    time.sleep(CHECK_INTERVAL)
