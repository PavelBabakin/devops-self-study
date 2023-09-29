import os
import sys

def gather_system_info():
    # OS type
    os_type = os.name
    print(f"OS Type: {os_type}")

    # Platform details
    platform = sys.platform
    print(f"Platform: {platform}")

    # Disk Usage
    disk_usage = os.statvfs('/')
    total_space = disk_usage.f_blocks * disk_usage.f_frsize
    free_space = disk_usage.f_bfree * disk_usage.f_frsize
    used_space = total_space - free_space
    print(f"Total Disk Space: {total_space / (1024*1024):.2f} MB")
    print(f"Used Disk Space: {used_space / (1024*1024):.2f} MB")
    print(f"Free Disk Space: {free_space / (1024*1024):.2f} MB")

    # Environment Variables
    env_vars = os.environ
    print("\nEnvironment Variables:")
    for key, value in env_vars.items():
        print(f"{key}: {value}")

def main():
    gather_system_info()

if __name__ == "__main__":
    main()