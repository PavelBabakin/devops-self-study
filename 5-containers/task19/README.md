# Task 19: Snapshot an LXC container and restore it to a previous state.

Snapshots in LXC (Linux Containers) provide a mechanism to capture the state of a container at a specific point in time. This can be invaluable for testing, debugging, and rollback scenarios. In this article, we will explore how to create a snapshot of an LXC container and restore it to a previous state.

---

### Prerequisites

- LXC installed and configured on your machine.
- An existing LXC container to snapshot.

---

### Step 1: Creating a Snapshot

### **Syntax**

```
lxc-snapshot -n [container_name]
```

### **Example**

Assuming we have a container named **`my_ubuntu_container`** that we wish to snapshot.

```
lxc-snapshot -n my_ubuntu_container
```

### **Key Points**

- Snapshots will be stored in a subdirectory related to the container, typically located at **`/var/lib/lxc/[container_name]/snaps/`**.

---

### Step 2: Listing Available Snapshots

### **Syntax**

```
lxc-snapshot -n [container_name] -L
```

### **Example**

```
lxc-snapshot -n my_ubuntu_container -L
```

### **Key Points**

- This command will display a list of all snapshots available for the specified container.

---

### Step 3: Restoring a Snapshot

### **Syntax**

```
lxc-snapshot -n [container_name] -r [snapshot_name]
```

### **Example**

Assuming we have a snapshot named **`snap0`** for **`my_ubuntu_container`** that we wish to restore.

```
lxc-snapshot -n my_ubuntu_container -r snap0
```

### **Key Points**

- Ensure the container is stopped before attempting to restore a snapshot.
- **`r [snapshot_name]`**: Specifies the snapshot to restore.

---

### Step 4: Deleting a Snapshot

### **Syntax**

```
lxc-snapshot -n [container_name] -d [snapshot_name]
```

### **Example**

```
lxc-snapshot -n my_ubuntu_container -d snap0
```

### **Key Points**

- **`d [snapshot_name]`**: Specifies the snapshot to delete.

---

### Conclusion

LXC snapshots are a potent tool for managing container states, allowing you to capture, restore, and even rollback containers to previous states. This functionality is crucial for maintaining stable and recoverable environments, especially in testing and development scenarios where changes may introduce instability or undesired behaviors.

---

### Next Steps

- **Advanced Snapshot Management**: Explore managing snapshots with additional metadata and comments.
- **Automation**: Investigate automating snapshot creation and management using scripts or orchestration tools.
- **Container Cloning**: Dive deeper into cloning containers from snapshots for testing and scaling.

---

### Further Reading

- **[LXC - Linux Containers](https://linuxcontainers.org/)**
- **[LXC Snapshot Documentation](https://linuxcontainers.org/lxc/manpages/man1/lxc-snapshot.1.html)**
- **[LXC Container Management](https://linuxcontainers.org/lxc/manpages/)**