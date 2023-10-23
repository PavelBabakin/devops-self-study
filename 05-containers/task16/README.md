# Task 16: Familiarize yourself with basic LXC commands like lxc-list, lxc-info, and lxc-stop.

Linux Containers (LXC) offer a lightweight virtualization method to run multiple containers on a host machine. To manage these containers effectively, LXC provides a suite of commands. In this article, we will delve into some basic LXC commands, namely **`lxc-list`**, **`lxc-info`**, and **`lxc-stop`**, to help you navigate through your LXC environment.

---

### 1. **Listing Containers: `lxc-list`**

### **Purpose**

- **Viewing Active Containers**: Lists all active containers on the host machine.

### **Usage**

```
lxc-list
```

### **Example**

```
$ lxc-list
RUNNING
- my_ubuntu_container
STOPPED
- my_stopped_container
```

### **Key Points**

- Displays containers categorized by their state (RUNNING, STOPPED, etc.).

---

### 2. **Fetching Container Information: `lxc-info`**

### **Purpose**

- **Retrieving Container Details**: Provides detailed information about a specific container.

### **Usage**

```
lxc-info -n [container_name]
```

### **Example**

```
$ lxc-info -n my_ubuntu_container
Name:           my_ubuntu_container
State:          RUNNING
PID:            12345
IP:             10.0.3.123
CPU use:        12.34 seconds
BlkIO use:      1.23 MiB
Memory use:     123.45 MiB
KMem use:       12.34 MiB
```

### **Key Points**

- Displays various metrics and information such as state, PID, IP address, and resource usage.

---

### 3. **Stopping Containers: `lxc-stop`**

### **Purpose**

- **Halting Containers**: Gracefully stops a running container.

### **Usage**

```
lxc-stop -n [container_name]
```

### **Example**

```
$ lxc-stop -n my_ubuntu_container
```

### **Key Points**

- Ensures the container is stopped gracefully, preserving data and maintaining the filesystem integrity.

---

### Additional Basic Commands

- **Starting a Container**: **`lxc-start -n [container_name]`**
- **Attaching to a Container**: **`lxc-attach -n [container_name]`**
- **Destroying a Container**: **`lxc-destroy -n [container_name]`**

---

### Conclusion

Understanding and utilizing basic LXC commands is fundamental in managing your LXC environment effectively. The commands **`lxc-list`**, **`lxc-info`**, and **`lxc-stop`** provide essential functionalities to view, retrieve information, and manage the state of your containers, respectively. As you continue to explore LXC, these commands will be pivotal in managing and interacting with your containers.

---

### Next Steps

- **Advanced LXC Commands**: Explore more advanced LXC commands for networking, snapshotting, and cloning.
- **LXC Networking**: Dive into networking within LXC, exploring bridges, NAT, and port forwarding.
- **Container Configuration**: Learn about configuring containers for specific use cases and resource limits.

---

### Further Reading

- **[LXC Command Line Interface](https://linuxcontainers.org/lxc/manpages/)**
- **[LXC Getting Started Guide](https://linuxcontainers.org/lxc/getting-started/)**
- **[LXC on Ubuntu](https://ubuntu.com/server/docs/containers-lxc)**