# Task 6: Write a basic playbook to install a web server (e.g., Nginx) on all hosts.

Embarking on the journey of automating your infrastructure with Ansible brings forth the power of playbooks. Playbooks allow you to define a series of tasks to be executed on remote servers, offering a reproducible and auditable configuration management approach. In this guide, we'll walk through creating a basic Ansible playbook to install the Nginx web server on all hosts in your inventory.

---

**Step 1: Understanding Ansible Playbooks**

### **What is an Ansible Playbook?**

- **Definition:** A YAML file defining tasks, handlers, and more in a structured format.
- **Purpose:** Automate tasks in a repeatable, scalable manner.
- **Components:** Plays, Tasks, Variables, Handlers, and more.

---

**Step 2: Setting Up Your Ansible Environment**

Ensure your Ansible environment is set up, and your inventory is configured with the target hosts.

### **Example Inventory:**

```
[web_servers]
server1.example.com
server2.example.com
```

---

**Step 3: Crafting the Nginx Installation Playbook**

### **Basic Playbook Structure:**

```yaml
---
- name: Install Nginx on Web Servers
  hosts: web_servers
  become: yes
  tasks:
    - name: Ensure Nginx is installed
      apt:
        name: nginx
        state: present
```

### **Playbook Breakdown:**

- **name:** Descriptive name of the play.
- **hosts:** Target hosts group from the inventory.
- **become:** Elevate privileges (use sudo).
- **tasks:** List of tasks to be executed.
- **apt:** Module to manage apt-packages.
- **name: nginx:** Target package to manage.
- **state: present:** Ensure the package is installed.

---

**Step 4: Running the Playbook**

Execute the playbook using the **`ansible-playbook`** command.

```
ansible-playbook install_nginx.yml
```

### **Expected Output:**

```
PLAY [Install Nginx on Web Servers] ********************************************

TASK [Ensure Nginx is installed] ************************************************
changed: [server1.example.com]
changed: [server2.example.com]

PLAY RECAP *********************************************************************
server1.example.com        : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
server2.example.com        : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

---

**Step 5: Validating the Installation**

Ensure Nginx is installed and running on the target hosts.

```
ansible web_servers -m shell -a "systemctl status nginx" -b
```

---

**Step 6: Exploring Further**

- **Adding More Tasks:** Expand the playbook to configure Nginx, deploy websites, or secure the server.
- **Using Variables:** Make the playbook dynamic by utilizing variables for package names, versions, or file paths.
- **Implementing Handlers:** Use handlers to manage service states (start, restart) when configurations change.

---

**Conclusion**

Creating an Ansible playbook to install Nginx provides a glimpse into the world of automated configuration management. This basic playbook can be the foundation upon which you build more complex configurations, manage your web servers, and eventually, control your entire infrastructure.

In the upcoming articles, we will explore more advanced Ansible concepts, diving into variables, templates, and roles, to further enhance your automation capabilities.