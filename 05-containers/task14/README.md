# Task 14: Install LXC on your machine.

Linux Containers (LXC) provide lightweight, secure virtualization by isolating processes in their own environment without the overhead of a full virtual machine. In this article, we will guide you through the process of installing LXC on your machine, marking the first step in exploring containerization with LXC.

---

### Prerequisites

- A Linux distribution installed on your machine.
- Sudo or root access to the machine.

---

### Step 1: Updating the Package List

Ensure your system’s package list is updated to retrieve the latest software.

```
sudo apt-get update
sudo apt-get upgrade
```

---

### Step 2: Installing LXC

Install LXC using the package manager of your Linux distribution.

For Ubuntu/Debian-based systems:

```
sudo apt-get install lxc
```

For Red Hat/CentOS systems:

```
shellCopy code
sudo yum install lxc

```

For Fedora systems:

```
sudo dnf install lxc
```

---

### Step 3: Verifying LXC Installation

Post-installation, verify that LXC is installed correctly.

```
lxc-checkconfig
```

This command will display a list of kernel subsystems and whether they are enabled on your system.

---

### Step 4: Starting the LXC Service

Ensure the LXC service is running.

```
sudo systemctl start lxc
sudo systemctl enable lxc
```

---

### Step 5: Creating Your First Container

Create your first LXC container using a template. Here, we are using the Ubuntu template.

```
sudo lxc-create -t ubuntu -n my_first_container
```

Explanation:

- **`t ubuntu`**: Specifies the template to use (Ubuntu in this case).
- **`n my_first_container`**: Names the container **`my_first_container`**.

---

### Step 6: Starting and Accessing the Container

Start the container and access its shell.

```
sudo lxc-start -n my_first_container
sudo lxc-attach -n my_first_container
```

---

### Step 7: Stopping and Destroying the Container

When done, you can stop and destroy the container.

```
sudo lxc-stop -n my_first_container
sudo lxc-destroy -n my_first_container
```

---

### Conclusion

Congratulations! You have successfully installed LXC on your machine and created your first container. This marks your first step into the world of LXC, opening avenues to explore container management, networking, storage, and more with LXC.

---

### Next Steps

- **LXC Networking**: Explore networking concepts in LXC, such as bridging, NAT, and port forwarding.
- **Persistent Storage**: Learn about managing persistent storage in LXC containers.
- **Container Management**: Dive deeper into managing LXC containers, including configuration, cloning, and snapshotting.

---

### Further Reading

- **[Official LXC Documentation](https://linuxcontainers.org/lxc/getting-started/)**
- **[LXC Man Page](https://man7.org/linux/man-pages/man7/lxc.7.html)**
- **[LXC GitHub Repository](https://github.com/lxc/lxc)**