# Task 24: Explore LXC's security features, such as AppArmor profiles and seccomp policies.

Security is paramount in containerized environments, and LXC (Linux Containers) provides robust security features, such as AppArmor profiles and seccomp policies, to safeguard containers against potential threats. In this guide, we will explore these security features and understand how to implement them in LXC.

---

### Prerequisites

- LXC installed and configured on your machine.
- Basic understanding of Linux security concepts.

---

### AppArmor Profiles in LXC

AppArmor (Application Armor) is a Linux Security Module (LSM) that protects applications by enforcing security profiles. In LXC, AppArmor profiles restrict what containers can do, enhancing security.

### **1. Default AppArmor Profile**

LXC applies a default AppArmor profile to containers, restricting certain actions like mount operations.

### **2. Custom AppArmor Profiles**

You can create custom AppArmor profiles tailored to specific containers, defining permitted and restricted actions.

### **3. Applying AppArmor Profiles**

Custom AppArmor profiles can be applied to containers via the LXC configuration file.

---

### Seccomp Policies in LXC

Seccomp (secure computing mode) restricts the system calls a process can make, providing an additional layer of security.

### **1. Default Seccomp Policy**

LXC includes a default seccomp policy that restricts certain system calls, such as rebooting the host machine.

### **2. Custom Seccomp Policies**

You can define custom seccomp policies to allow or deny specific system calls based on your security requirements.

### **3. Implementing Seccomp Policies**

Seccomp policies are applied to containers via the LXC configuration file, ensuring that the defined system call rules are enforced.

---

### Step 1: Exploring the Default AppArmor Profile

Explore the default AppArmor profile applied to LXC containers.

```
cat /etc/apparmor.d/lxc/lxc-default
```

---

### Step 2: Creating a Custom AppArmor Profile

Create and define a custom AppArmor profile tailored to specific container requirements.

```
sudo nano /etc/apparmor.d/lxc-containers/my_custom_profile
```

Example entry to deny mount operations:

```
deny mount,
```

---

### Step 3: Applying a Custom AppArmor Profile to a Container

Edit the LXC configuration file of the container to apply the custom AppArmor profile.

```
sudo nano /var/lib/lxc/[container_name]/config
```

Add the following line:

```
lxc.apparmor.profile = /etc/apparmor.d/lxc-containers/my_custom_profile
```

---

### Step 4: Crafting a Custom Seccomp Policy

Create and define a custom seccomp policy to control system calls.

```
sudo nano /var/lib/lxc/[container_name]/seccomp_policy
```

Example entry to deny the **`reboot`** system call:

```
2
denylist
[all]
reboot
```

---

### Step 5: Enforcing a Custom Seccomp Policy on a Container

Edit the LXC configuration file of the container to enforce the custom seccomp policy.

```
sudo nano /var/lib/lxc/[container_name]/config
```

Add the following line:

```
lxc.seccomp.profile = /var/lib/lxc/[container_name]/seccomp_policy
```

---

### Conclusion

LXC’s security features, including AppArmor profiles and seccomp policies, provide a robust mechanism to safeguard containers against potential threats and unauthorized actions. By understanding and implementing these security features, you ensure that your LXC containers operate securely, adhering to defined security policies and best practices.

---

### Next Steps

- **Advanced Security**: Explore additional LXC security features and best practices.
- **Container Auditing**: Investigate auditing tools and practices for LXC containers.
- **Network Security**: Explore network security practices for LXC containers.

---

### Further Reading

- **[LXC - Linux Containers](https://linuxcontainers.org/)**
- **[AppArmor Wiki](https://gitlab.com/apparmor/apparmor/-/wikis/home)**
- **[Seccomp - man7.org](https://man7.org/linux/man-pages/man2/seccomp.2.html)**