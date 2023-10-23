# Task 15: Create your first LXC container and access its shell.

Having installed LXC on your machine, the next exciting step is to create your first LXC container and interact with it. In this article, we will guide you through the process of creating an LXC container and accessing its shell, providing a hands-on experience with LXC.

---

### Step 1: Creating an LXC Container

LXC provides various templates to create containers. Here, we will create an Ubuntu container.

```
sudo lxc-create -t ubuntu -n my_ubuntu_container
```

- **`t ubuntu`**: Specifies the Ubuntu template.
- **`n my_ubuntu_container`**: Names the container **`my_ubuntu_container`**.

---

### Step 2: Starting the LXC Container

Once created, start the container using the following command:

```
sudo lxc-start -n my_ubuntu_container
```

---

### Step 3: Accessing the Container’s Shell

To interact with the container, access its shell using the following command:

```
sudo lxc-attach -n my_ubuntu_container
```

You should now be inside the container, interacting with its shell. You can execute commands, install packages, and explore the container environment.

---

### Step 4: Managing the LXC Container

### **a. Stopping the Container**

To stop the container, use the following command:

```
sudo lxc-stop -n my_ubuntu_container
```

### **b. Restarting the Container**

To restart the container, use the following command:

```
sudo lxc-restart -n my_ubuntu_container
```

### **c. Destroying the Container**

If you wish to delete the container, use the following command:

```
sudo lxc-destroy -n my_ubuntu_container
```

**Note**: Ensure you have stopped the container before destroying it.

---

### Conclusion

Creating and interacting with an LXC container provides a practical understanding of containerization at a lightweight and flexible level. You have successfully created, accessed, and managed an LXC container, laying a foundation to explore more advanced LXC features and management practices.

---

### Next Steps

- **LXC Networking**: Explore how to set up networking for LXC containers.
- **Persistent Storage**: Learn how to manage storage and data within LXC containers.
- **Container Configuration**: Dive into configuring LXC containers for specific use cases.

---

### Further Reading

- **[LXC - Linux Containers](https://linuxcontainers.org/)**
- **[LXC Container Management](https://linuxcontainers.org/lxc/manpages/)**
- **[Ubuntu LXC](https://ubuntu.com/server/docs/containers-lxc)**