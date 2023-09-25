import psutil

def monitor_resources():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        print(f"WARNING: CPU usage is at {cpu_usage}%!")

    # Get memory usage
    memory_info = psutil.virtual_memory()
    if memory_info.percent > 80:
        print(f"WARNING: Memory usage is at {memory_info.percent}%!")

def main():
    while True:
        monitor_resources()

if __name__ == "__main__":
    main()