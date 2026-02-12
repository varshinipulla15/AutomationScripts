import psutil
import json
from datetime import datetime

def collect_metrics():
    metrics = {
        "timestamp" : str(datetime.now()),
        "cpu_percentage" : psutil.cpu_percent(interval=1),
        "memory_percentage" : psutil.virtual_memory().percent,
        "disk_percentage" : psutil.disk_usage("/").percent
    }
    return metrics

def savefile_into_json(metrics, filename="metrics.json"):
    with open(filename, "w") as f:
        json.dump(metrics, f, indent=4)

if __name__ == "__main__":
    metrics = collect_metrics()
    savefile_into_json(metrics)
    print (f"{metrics}")