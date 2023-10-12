# Task 13: Use your role in a playbook and deploy it to the hosts.

After crafting an Ansible role, the next logical step is to implement it within a playbook and deploy the configured services to your hosts. This article will guide you through the process of utilizing the previously created database role within a playbook and orchestrating its deployment across your server infrastructure.

---

**Step 1: Preparing Your Environment**

### **A. Inventory File:**

Ensure your inventory file is set up with the appropriate host groups and host addresses.

### **B. SSH Access:**

Verify that Ansible can access the target hosts via SSH using key-based authentication.

### **C. Role Availability:**

Ensure the role you intend to use is available in the **`roles`** directory of your Ansible project.

---

**Step 2: Crafting the Playbook**

### **A. Defining Hosts and Roles:**

Specify the target hosts and roles to be applied within the playbook.

### **B. Example Playbook:**

```yaml
---
- name: Deploy PostgreSQL to Database Servers
  hosts: db_servers
  become: yes
  roles:
    - role: my_database_role
```

### **Explanation:**

- **name:** Descriptive name for the playbook.
- **hosts:** Target host group from the inventory file.
- **become: yes:** Elevate privileges to become the superuser.
- **roles:** List of roles to be applied to the target hosts.

---

**Step 3: Running the Playbook**

### **A. Deploying the Role:**

Use the **`ansible-playbook`** command to run the playbook and deploy the role to your hosts.

### **B. Example Command:**

```bash
ansible-playbook -i inventory.ini deploy_database.yml
```

### **Explanation:**

- **i inventory.ini:** Specifies the inventory file.
- **deploy_database.yml:** The playbook file that utilizes the database role.

---

**Step 4: Verifying the Deployment**

### **A. SSH into Hosts:**

SSH into the target hosts to verify the deployment and configuration of the service.

### **B. Checking Service Status:**

Use system commands to check the status of the deployed service.

```bash
systemctl status postgresql
```

### **C. Validating Configurations:**

Ensure that any configurations managed by the role are applied correctly.

---

**Step 5: Managing Role Versions**

### **A. Updating Roles:**

Modify the role as per updated requirements and redeploy using the playbook.

### **B. Role Versioning:**

Consider using a version control system like Git to manage different versions of your roles.

### **C. Reusability:**

Remember that roles can be reused across different playbooks and projects, enhancing your automation efficiency.

---

**Conclusion**

Implementing Ansible roles within playbooks and deploying them to manage host configurations is a powerful and efficient approach to IT automation. By encapsulating specific tasks, handlers, and templates within roles, you ensure that your automation workflows are modular, reusable, and easy to manage.

In subsequent articles, we will delve deeper into advanced Ansible functionalities and explore various scenarios to enhance your automation capabilities.