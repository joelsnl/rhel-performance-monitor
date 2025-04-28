import psutil
import time
import logging

# Configure logging
logging.basicConfig(
    filename='performance.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Thresholds (customize if needed)
CPU_THRESHOLD = 85  # %
MEMORY_THRESHOLD = 85  # %
DISK_THRESHOLD = 90  # %

def check_performance():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    logging.info(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

    if cpu > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory}%")
    if disk > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk}%")

if __name__ == "__main__":
    while True:
        check_performance()
        time.sleep(30)
