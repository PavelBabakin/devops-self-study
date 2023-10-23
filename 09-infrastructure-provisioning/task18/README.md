# Task 18: Initialize, plan, and apply your Terraform configuration.

Terraform, a widely used Infrastructure as Code (IaC) tool, allows developers and operators to define and manage infrastructure using a declarative language. The typical workflow in Terraform involves several commands, each serving a specific purpose in the process of deploying and managing resources. In this guide, we will delve into the fundamental Terraform commands: **`init`**, **`plan`**, and **`apply`**, and understand their role in the Terraform workflow.

---

**Step 1: Terraform Initialize (`terraform init`)**

### **Purpose:**

- Initialize the working directory containing Terraform configuration files.
- Download the provider plugins specified in the configuration.
- Prepare the backend for state management.

### **Usage:**

Navigate to the directory containing your **`.tf`** files and run:

```bash
terraform init
```

### **Key Points:**

- **Provider Plugins:** Terraform downloads the necessary provider plugins.
- **Backend Initialization:** Prepares the backend for storing the state file.
- **Module Download:** If using modules, Terraform fetches them.

---

**Step 2: Terraform Plan (`terraform plan`)**

### **Purpose:**

- Generate an execution plan detailing what actions Terraform will take to apply the configuration.
- Enable reviewing the changes before applying them.

### **Usage:**

```bash
terraform plan
```

### **Key Points:**

- **Resource Actions:** Displays the actions (create, update, destroy) for each resource.
- **Safety:** Allows reviewing changes before making them.
- **Output:** Can be saved to be used by **`terraform apply`** for certainty in changes.

---

**Step 3: Terraform Apply (`terraform apply`)**

### **Purpose:**

- Apply the changes required to reach the desired state defined in the configuration.
- Provision the defined infrastructure.

### **Usage:**

```bash
terraform apply
```

### **Key Points:**

- **Execution Plan:** Displays the execution plan and seeks approval before proceeding.
- **Resource Creation:** Provisions the resources as per the configuration.
- **State Update:** Updates the state file post successful deployment.

---

**Example Workflow: Deploying a GCP Compute Engine Instance**

1. **Write Configuration:** Create a **`.tf`** file with the desired infrastructure code.
2. **Initialize Terraform:**
    
    ```bash
    terraform init
    ```
    
    Validate that Terraform is initialized without errors.
    
3. **Generate and Review Plan:**
    
    ```bash
    terraform plan
    ```
    
    Review the actions that Terraform will perform.
    
4. **Apply Changes:**
    
    ```bash
    terraform apply
    ```
    
    Confirm the actions and observe Terraform provisioning the resources.
    

---

**Conclusion**

Understanding the Terraform workflow and the purpose of each command (**`init`**, **`plan`**, and **`apply`**) is fundamental to effectively using Terraform for IaC. This structured approach ensures that you can review, validate, and control the changes to your infrastructure in a predictable manner.

In the upcoming articles, we will explore more advanced Terraform concepts, such as state management, variable interpolation, and working with modules, to further enhance your IaC practices. Stay tuned and embark on this insightful journey into the depths of Terraform and IaC!