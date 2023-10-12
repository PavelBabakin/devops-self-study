# Task 7: Run the playbook and verify the installation on the hosts.

Executing an Ansible playbook and verifying its impact is a crucial step in infrastructure automation. After crafting a playbook to install Nginx, it's imperative to run it and ensure that the installation is successful across all targeted hosts. This article will guide you through running your Ansible playbook and verifying the Nginx installation on your servers.

---

**Step 1: Executing the Playbook**

### **Running the Playbook:**

Utilize the **`ansible-playbook`** command to initiate the playbook execution.

```
ansible-playbook install_nginx.yml
```

### **Understanding the Output:**

- **PLAY:** Indicates the start of the play and shows the name.
- **TASK:** Displays the tasks being executed and their status.
- **PLAY RECAP:** Provides a summary, indicating the success or failure of the tasks on each host.

---

**Step 2: Verifying the Installation**

### **A. Checking the Nginx Service Status:**

Use Ansible ad-hoc commands to check the Nginx service status on all hosts.

```
ansible web_servers -m shell -a "systemctl status nginx" -b
```

### **B. Validating Nginx Response:**

Ensure Nginx is responding to HTTP requests on the default port (80).

```
ansible web_servers -m shell -a "curl localhost"
```

### **C. Accessing the Nginx Welcome Page:**

You can also manually verify by navigating to the server's IP or domain in a web browser. You should see the Nginx welcome page.

---

**Step 3: Troubleshooting Common Issues**

### **A. Task Failures:**

- **SSH Issues:** Ensure SSH keys are configured correctly.
- **Privilege Escalation:** Ensure **`become`** is used for tasks requiring superuser privileges.

### **B. Nginx Service Not Running:**

- **Firewall Rules:** Ensure no firewall rules are blocking Nginx.
- **Configuration Errors:** Check Nginx configurations for syntax errors.

---

**Step 4: Making Adjustments and Re-running the Playbook**

### **A. Making Changes:**

If you need to make adjustments or add additional configurations, modify the playbook accordingly.

### **B. Idempotency of Playbooks:**

Ansible playbooks are idempotent, meaning you can run them multiple times without affecting the final state.

---

**Step 5: Documenting and Version Controlling Your Playbooks**

### **A. Documentation:**

Ensure to document your playbooks, including comments within the YAML file explaining complex tasks.

### **B. Version Control:**

Utilize a version control system (e.g., Git) to manage changes and maintain a history of your playbooks.

---

**Conclusion**

Successfully running and verifying an Ansible playbook is a rewarding step in infrastructure automation. Ensuring that your playbooks execute flawlessly and achieve the desired state on your hosts is crucial for maintaining a stable and secure environment. As you progress in your Ansible journey, you'll encounter more complex scenarios, and developing a systematic approach to running and verifying your playbooks will be invaluable.

In the subsequent articles, we will delve deeper into more advanced Ansible topics, enhancing your automation skills and infrastructure management capabilities.