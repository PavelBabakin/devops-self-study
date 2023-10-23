# Task 16: Install Terraform and understand its CLI commands.

Terraform, developed by HashiCorp, is an open-source Infrastructure as Code (IaC) tool that allows you to define and provide data center infrastructure using a declarative configuration language. In this guide, we will walk through the steps to install Terraform and explore its Command Line Interface (CLI) commands to manage and manipulate infrastructure resources.

---

**Step 1: Installing Terraform**

### **For Windows, macOS, and Linux:**

1. **Download Terraform:** Visit the [Terraform Downloads](https://www.terraform.io/downloads.html) page and download the appropriate version for your operating system.
2. **Extract the Binary:**
    - **Windows:** Extract the zip file and place the **`terraform`** binary in a known path.
    - **macOS/Linux:** Use **`unzip`** or **`tar`** to extract the binary and move it to a directory in your **`PATH`** (e.g., **`/usr/local/bin`**).
3. **Verify Installation:** Open a terminal or command prompt and verify the installation by running:
    
    ```bash
    terraform -v
    ```
    
    This should display the Terraform version.
    

---

**Step 2: Understanding Terraform CLI Commands**

### **Core Commands:**

- **`terraform init`**
    - **Purpose:** Initializes the Terraform working directory.
    - **Usage:**
        
        ```bash
        terraform init
        ```
        
- **`terraform plan`**
    - **Purpose:** Generates an execution plan, showing what actions Terraform will take to apply the configuration.
    - **Usage:**
        
        ```bash
        terraform plan
        ```
        
- **`terraform apply`**
    - **Purpose:** Applies the changes required to reach the desired state defined in the configuration.
    - **Usage:**
        
        ```bash
        terraform apply
        ```
        
- **`terraform destroy`**
    - **Purpose:** Removes all resources defined by the configuration.
    - **Usage:**
        
        ```bash
        terraform destroy
        ```
        

### **Additional Commands:**

- **`terraform validate`**
    - Validates the configuration files for syntax.
- **`terraform output`**
    - Displays outputs from the state file.
- **`terraform fmt`**
    - Re-formats configuration files to a standard style.
- **`terraform state`**
    - Advanced command for inspecting and modifying the state file.

---

**Step 3: Basic Workflow with Terraform CLI**

1. **Write Configuration:** Create a **`.tf`** file defining the infrastructure resources.
2. **Initialize Directory:** Run **`terraform init`** to initialize the working directory.
3. **Plan Changes:** Use **`terraform plan`** to see the planned actions.
4. **Apply Changes:** Execute **`terraform apply`** to apply the desired changes.
5. **Destroy Resources:** Optionally, use **`terraform destroy`** to remove deployed resources.

---

**Conclusion**

Terraform provides a robust and user-friendly interface to manage infrastructure across multiple cloud providers. Understanding the core CLI commands and their usage is fundamental to efficiently utilizing Terraform for IaC practices.

In the upcoming articles, we will delve deeper into writing Terraform configurations, managing state, and implementing advanced IaC practices with Terraform. Join us on this journey to explore and master the capabilities of Terraform in managing and orchestrating cloud infrastructure!