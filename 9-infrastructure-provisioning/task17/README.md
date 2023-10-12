# Task 17: Write a basic Terraform configuration to provision a GCP Compute Engine instance.

Terraform allows you to define, provision, and manage infrastructure in a predictable and declarative manner. In this guide, we will create a basic Terraform configuration to provision a Google Cloud Platform (GCP) Compute Engine instance, providing a practical example of Infrastructure as Code (IaC) in action.

---

**Step 1: Setting Up GCP Credentials**

1. **Create a GCP Project:** Navigate to the [GCP Console](https://console.cloud.google.com/) and create a new project.
2. **Enable Compute Engine API:** Enable the Compute Engine API for your project.
3. **Service Account:** Create a service account and download the JSON key file.
4. **Set Environment Variable:** Export the path to your service account key as an environment variable:
    
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="path-to-your-service-account-key.json"
    ```
    

---

**Step 2: Writing the Terraform Configuration**

### **File: `main.tf`**

```
provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
}

resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "f1-micro"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral IP
    }
  }
}
```

### **Explanation:**

- **Provider Block:** Specifies the provider (GCP) and project details.
- **Resource Block:** Defines the resource type and configuration.

---

**Step 3: Initializing and Applying the Configuration**

1. **Initialize Terraform:**
    
    ```bash
    terraform init
    ```
    
    This command initializes your directory, installs the Google provider plugin, and sets up the backend.
    
2. **Apply Configuration:**
    
    ```bash
    terraform apply
    ```
    
    Review the plan and type **`yes`** to provision the GCP Compute Engine instance.
    

---

**Step 4: Validating the Deployment**

- Navigate to the [GCP Compute Engine Dashboard](https://console.cloud.google.com/compute/instances) and validate that the instance is running.
- Note the external IP and try accessing the instance, e.g., via SSH.

---

**Step 5: Destroying the Infrastructure**

When you no longer need the infrastructure, use Terraform to destroy it and prevent further charges:

```bash
terraform destroy
```

Review and confirm the destruction plan by typing **`yes`**.

---

**Conclusion**

In this guide, we walked through a basic example of using Terraform to define and provision a GCP Compute Engine instance. This practical example illustrates the simplicity and power of Infrastructure as Code, enabling you to manage infrastructure with ease and reliability.

In subsequent articles, we will explore more advanced Terraform topics, such as state management, modular configurations, and managing dependencies between resources. Stay tuned as we continue to explore the world of Terraform and Infrastructure as Code!