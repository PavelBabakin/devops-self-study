# Task 23: Use LXC templates to create containers with pre-defined software and configurations.

LXC (Linux Containers) templates are powerful tools that allow users to create containers with pre-defined software and configurations, ensuring consistency and saving time during deployment. In this guide, we will explore how to utilize LXC templates to create containers that meet specific requirements right from the start.

---

### Prerequisites

- LXC installed and configured on your machine.
- Basic understanding of shell scripting and package management.

---

### Understanding LXC Templates

LXC templates are shell scripts designed to automate the creation of containers, including installing software and applying configurations. They are typically located in **`/usr/share/lxc/templates/`** and can be used directly or customized as per requirements.

---

### Step 1: Exploring Available Templates

List the available LXC templates on your system.

```
ls /usr/share/lxc/templates/
```

Common templates include:

- **`lxc-download`**: Downloads pre-built images from the LXC image repository.
- **`lxc-ubuntu`**: Creates Ubuntu containers.
- **`lxc-debian`**: Creates Debian containers.
- **`lxc-centos`**: Creates CentOS containers.

---

### Step 2: Using a Pre-existing Template

Create a container using one of the available templates.

```
sudo lxc-create -t [template_name] -n [container_name]
```

Example:

```
sudo lxc-create -t ubuntu -n my_ubuntu_container
```

---

### Step 3: Customizing a Template

### **a. Copy an Existing Template**

Create a copy of an existing template to customize.

```
sudo cp /usr/share/lxc/templates/lxc-ubuntu /usr/share/lxc/templates/lxc-mytemplate
```

### **b. Edit the Custom Template**

Modify the template script according to your requirements, such as installing specific software or applying configurations.

```
sudo nano /usr/share/lxc/templates/lxc-mytemplate
```

Example addition to install NGINX:

```
# Install NGINX
chroot $rootfs apt-get install -y nginx
```

### **c. Set Permissions**

Ensure the custom template is executable.

```
sudo chmod +x /usr/share/lxc/templates/lxc-mytemplate
```

---

### Step 4: Creating a Container Using the Custom Template

Use the custom template to create a new container.

```
sudo lxc-create -t mytemplate -n my_custom_container
```

---

### Step 5: Verifying the Configuration

Start the container and verify that the pre-defined software and configurations are applied.

```
sudo lxc-start -n my_custom_container
sudo lxc-attach -n my_custom_container -- systemctl status nginx
```

---

### Conclusion

LXC templates offer a streamlined approach to container deployment, enabling the creation of containers with specific software and configurations right from the outset. By utilizing and customizing LXC templates, you ensure consistency across deployments and save valuable time during container creation and configuration.

---

### Next Steps

- **Advanced Scripting**: Explore advanced scripting within LXC templates to automate complex setup and configuration tasks.
- **Container Management**: Dive into managing and orchestrating multiple containers.
- **Security**: Explore securing your LXC containers and ensuring safe deployments.

---

### Further Reading

- **[LXC - Linux Containers](https://linuxcontainers.org/)**
- **[LXC Templates](https://linuxcontainers.org/lxc/manpages/man1/lxc-create.1.html)**
- **[LXC GitHub Repository (Templates)](https://github.com/lxc/lxc/tree/master/templates)**