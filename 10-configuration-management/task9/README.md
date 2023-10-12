# Task 9: Gather facts about your hosts and use them in your playbook (e.g., based on OS type).

Ansible facts, gathered via the setup module, provide a wealth of information about target hosts, enabling you to tailor configurations based on specific host attributes. This article will guide you through leveraging Ansible facts to dynamically manage configurations, focusing on adapting tasks based on the operating system type of the target hosts.

---

**Step 1: Understanding Ansible Facts**

### **What are Ansible Facts?**

- **Definition:** Data related to the system, retrieved by the setup module during playbook execution.
- **Access:** Utilize facts within playbooks, templates, and expressions using variable syntax **`{{ ansible_facts['fact_name'] }}`**.

### **Viewing Available Facts:**

Retrieve and display facts for a host using the following ad-hoc command:

```
ansible [target_host] -m setup
```

---

**Step 2: Utilizing Facts in Your Playbook**

### **A. Accessing Facts:**

Use facts within tasks and templates by referencing the fact name.

### **B. Conditional Execution:**

Employ facts to conditionally execute tasks based on host attributes.

---

**Step 3: Example Use Case - Adapting Tasks Based on OS Type**

### **A. Gathering Facts:**

Ensure facts are gathered at the beginning of the playbook.

### **B. Conditional Tasks:**

Implement tasks conditionally based on the OS type.

### Example Playbook:

```yaml
---
- name: Install Web Server Based on OS Type
  hosts: all
  become: yes
  tasks:
    - name: Install Apache (for Debian-based systems)
      apt:
        name: apache2
        state: present
      when: ansible_facts['os_family'] == "Debian"

    - name: Install httpd (for RedHat-based systems)
      yum:
        name: httpd
        state: present
      when: ansible_facts['os_family'] == "RedHat"
```

### **Explanation:**

- **when:** Directive to specify the condition for executing a task.
- **ansible_facts['os_family']:** Fact indicating the OS family (e.g., Debian, RedHat).

---

**Step 4: Running and Verifying the Playbook**

### **A. Executing the Playbook:**

Run the playbook and observe how tasks are executed conditionally based on the OS type.

```
ansible-playbook install_web_server.yml
```

### **B. Verifying the Installation:**

Check the installation of the web server on the target hosts.

```
ansible all -m shell -a "systemctl status apache2 || systemctl status httpd" -b
```

---

**Step 5: Advanced Usage of Facts**

### **A. Creating Dynamic Configurations:**

Utilize facts within Jinja2 templates to generate dynamic configurations based on host attributes.

### **B. Fact Caching:**

Consider enabling fact caching to optimize playbook runs by avoiding gathering facts repeatedly.

---

**Conclusion**

Ansible facts empower you to create intelligent, adaptive automation workflows that cater to the specificities of each target host. By harnessing the rich data provided by facts, you can ensure that your configurations are not only consistent but also optimized for the particularities of each system.

In the following articles, we will explore more advanced Ansible topics, further enhancing your configuration management and automation capabilities.