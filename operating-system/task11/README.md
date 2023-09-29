# Task 11: Set up and manage storage using tools like fdisk, lsblk, and df.

Managing storage is a fundamental task for system administrators. Whether it's partitioning a new drive, checking available space, or understanding block devices, having the right tools at your disposal is crucial. In this guide, we'll delve into three essential utilities: **`fdisk`**, **`lsblk`**, and **`df`**.

**1. `fdisk`: Disk Partitioning Tool**:

- **Understanding `fdisk`**:
**`fdisk`** is a command-line utility used to create and manipulate disk partitions on Linux.
- **Basic `fdisk` Commands**:
    - View partition table: **`sudo fdisk -l`**
    - Create a new partition table: **`sudo fdisk /dev/sdX`** (Replace X with the appropriate drive letter.)
- **Using `fdisk`**:
Once inside the **`fdisk`** interface:
    - **`p`**: Display the partition table.
    - **`n`**: Create a new partition.
    - **`d`**: Delete a partition.
    - **`w`**: Write changes and exit.

**2. `lsblk`: List Block Devices**:

- **Understanding `lsblk`**:
**`lsblk`** lists information about all available block devices, making it easier to identify drives, partitions, and their relationships.
- **Using `lsblk`**:
    - Basic usage: **`lsblk`**
    - View more detailed information: **`lsblk -f`**

**3. `df`: Disk Space Usage Tool**:

- **Understanding `df`**:
**`df`** displays the amount of disk space used and available on the mounted filesystems.
- **Using `df`**:
    - Basic usage: **`df`**
    - Display in human-readable format: **`df -h`**
    - Show inodes usage instead of block usage: **`df -i`**

**Tips**:

- Always backup important data before making changes to disk partitions.
- Regularly monitor disk space to ensure the system operates efficiently.
- Use **`man`** (e.g., **`man fdisk`**) to access the manual pages for these tools for more detailed information and options.

**Conclusion**:
Effective storage management is essential for maintaining system health, optimizing performance, and ensuring data safety. Tools like **`fdisk`**, **`lsblk`**, and **`df`** provide administrators with the capabilities to handle storage tasks confidently. As with all technical skills, hands-on practice and continuous exploration are the keys to mastery.