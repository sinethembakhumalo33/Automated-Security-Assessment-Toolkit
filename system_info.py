import platform
import socket
import os
import psutil


def get_system_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    os_name = platform.system()
    version = platform.version()
    cpu = platform.processor()
    ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    user = os.getlogin()

    return {
        "Hostname": hostname,
        "IP Address": ip,
        "Operating System": os_name,
        "Version": version,
        "CPU": cpu,
        "RAM (GB)": ram,
        "Current User": user
    }


if __name__ == "__main__":
    info = get_system_info()

    print("System Information")
    print("-" * 30)

    for key, value in info.items():
        print(f"{key}: {value}")