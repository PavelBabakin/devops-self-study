# Task 8: Use variables in your playbook to make it more dynamic (e.g., setting the server name).

Variables in Ansible playbooks empower you to manage configurations dynamically, enhancing reusability and maintainability. By parameterizing configurations, you can adapt your automation to various environments and use cases without rewriting tasks. In this guide, we'll explore how to utilize variables in your Ansible playbook to dynamically set the server name in the Nginx configuration.

---

**Step 1: Understanding Ansible Variables**

### **What are Ansible Variables?**

- **Definition:** Parameters that alter the behavior of tasks and templates.
- **Usage:** Variables can be defined in playbooks, roles, and inventory, or passed via the command line.
- **Syntax:** Variables are enclosed within double curly braces **`{{ variable_name }}`**.

---

**Step 2: Defining Variables in Your Playbook**

### **Example Variable Definition:**

```yaml
---
- name: Install and Configure Nginx
  hosts: web_servers
  become: yes
  vars:
    server_name: "www.example.com"
  tasks:
    - name: Ensure Nginx is installed
      apt:
        name: nginx
        state: present
```

### **Key Points:**

- **vars:** Section where variables are defined.
- **server_name:** Variable name followed by its value.

---

**Step 3: Utilizing Variables in Tasks and Templates**

### **A. Using Variables in Tasks:**

Variables can be used within tasks to dynamically set values.

### **B. Using Variables in Templates:**

Jinja2 templates allow you to generate configuration files dynamically using variables.

### Example Jinja2 Template (**`nginx_conf.j2`**):

```
server {
    listen 80;
    server_name {{ server_name }};

    location / {
        return 200 'Welcome to {{ server_name }}';
    }
}
```

---

**Step 4: Integrating Templates and Variables in Your Playbook**

### **Example Playbook with Template and Variable:**

```yaml
---
- name: Install and Configure Nginx
  hosts: web_servers
  become: yes
  vars:
    server_name: "www.example.com"
  tasks:
    - name: Ensure Nginx is installed
      apt:
        name: nginx
        state: present

    - name: Deploy Nginx Configuration
      template:
        src: nginx_conf.j2
        dest: /etc/nginx/sites-available/default
      notify: Restart Nginx

  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted
```

### **Explanation:**

- **template:** Module to manage file templates.
- **src:** Source Jinja2 template file.
- **dest:** Destination path on the target host.
- **notify:** Trigger a handler when the task makes changes.

---

**Step 5: Running the Playbook and Verifying the Configuration**

### **A. Running the Playbook:**

```
ansible-playbook configure_nginx.yml
```

### **B. Verifying the Configuration:**

Ensure that the Nginx configuration is applied correctly and the service is running with the new settings.

```
ansible web_servers -m shell -a "curl localhost" -b
```

---

**Conclusion**

Incorporating variables into your Ansible playbooks enhances their flexibility and reusability across diverse environments and scenarios. By parameterizing configurations and utilizing Jinja2 templates, you can manage complex configurations in a structured and maintainable manner.

In the upcoming articles, we will delve deeper into more advanced Ansible concepts, further expanding your automation toolkit and capabilities.