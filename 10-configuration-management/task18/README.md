# Task 18: Set up a dynamic inventory script to fetch hosts from a cloud provider (e.g., AWS EC2 instances).

In the world of automation, managing inventory manually can be a cumbersome and error-prone task. Ansible offers a powerful solution through dynamic inventories, allowing you to automatically fetch and configure hosts from various sources, including cloud providers. In this article, we will explore the setup of a dynamic inventory script to effortlessly fetch hosts from a cloud provider like AWS EC2 instances.

---

**Step 1: What is a Dynamic Inventory?**

### **A. Definition:**

- **Dynamic Inventory:** A feature in Ansible that allows you to automatically discover and configure hosts from various sources.

### **B. Use Cases:**

- Automating host configuration from cloud providers.
- Updating inventory lists from external databases.
- Adapting to ever-changing infrastructure.

---

**Step 2: Setting Up Dynamic Inventory for AWS EC2**

### **A. Prerequisites:**

- You have an AWS account with EC2 instances.
- AWS CLI is installed and configured on your machine.

### **B. Ansible AWS Dynamic Inventory Script:**

Ansible provides a built-in AWS dynamic inventory script that you can use. Ensure it's available on your system:

```bash
curl -o /path/to/aws_ec2.py https://raw.githubusercontent.com/ansible/ansible/stable-2.10/contrib/inventory/aws_ec2.py
chmod +x /path/to/aws_ec2.py
```

### **C. Configuration:**

Edit your **`ansible.cfg`** file to specify the path to the dynamic inventory script:

```
[defaults]
inventory = /path/to/aws_ec2.py
```

---

**Step 3: AWS Configuration and Permissions**

### **A. IAM Role:**

Ensure that the EC2 instances have an IAM role with appropriate permissions for AWS API access.

### **B. AWS CLI Configuration:**

Ensure that your AWS CLI is configured with the appropriate credentials and region:

```bash
aws configure
```

---

**Step 4: Testing Dynamic Inventory**

### **A. Listing Hosts:**

You can now list the hosts discovered by the dynamic inventory script:

```bash
/path/to/aws_ec2.py --list
```

### **B. Testing in Ansible:**

Use Ansible commands to target hosts fetched by the dynamic inventory:

```bash
ansible -i /path/to/aws_ec2.py tag_Name_my_ec2_instance -m ping
```

---

**Step 5: Customizing Dynamic Inventory**

### **A. Grouping Hosts:**

You can use EC2 tags to group hosts logically in your dynamic inventory.

### **B. Custom Scripting:**

You can also create custom dynamic inventory scripts tailored to your specific needs.

---

**Conclusion**

Automating host configuration using dynamic inventory from cloud providers like AWS EC2 instances simplifies the management of your infrastructure. It enables you to adapt quickly to changes, reduces manual effort, and ensures that your automation tasks are always working with up-to-date information.

In future articles, we will delve into advanced Ansible concepts and explore real-world use cases to further enhance your automation expertise.