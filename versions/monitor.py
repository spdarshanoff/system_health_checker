import psutil
import datetime
def get_system_metrics():
    cpu = psutil.cpu_percent(interval=10)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.datetime.now()

    print("Time:", timestamp)
    print("CPU Usage:", cpu, "%")
    print("Memory Usage:", memory, "%")
    print("Disk Usage:", disk, "%")
    print("-" * 40)

get_system_metrics()
