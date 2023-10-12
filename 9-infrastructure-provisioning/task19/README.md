# Task 19: Use Terraform modules to organize and reuse infrastructure code.

Terraform modules encapsulate distinct logical components of infrastructure, promoting reusability and maintainability of Infrastructure as Code (IaC). In this guide, we will explore how to use Terraform modules to organize and reuse infrastructure code, enhancing the modularity and efficiency of your IaC practices.

---

**Step 1: Understanding Terraform Modules**

### **What is a Terraform Module?**

- A container for multiple resources that are used together.
- Can be used to encapsulate and parameterize infrastructure code, making it reusable and manageable.

### **Key Components:**

- **Inputs:** Parameters to customize the module for different use cases.
- **Outputs:** Expose attributes of the module’s resources.
- **Resources:** Infrastructure objects defined within the module.

---

**Step 2: Creating a Basic Terraform Module**

### **Example: A Module for a GCP Compute Engine Instance**

### Directory Structure:

```
my-gcp-instance-module/
│
├── main.tf
├── variables.tf
└── outputs.tf
```

### main.tf

```
resource "google_compute_instance" "instance" {
  name         = var.name
  machine_type = var.machine_type
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = var.image
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }
}
```

### variables.tf

```
variable "name" {
  type        = string
  description = "Name of the instance"
}

variable "machine_type" {
  type        = string
  description = "Machine type of the instance"
  default     = "f1-micro"
}

variable "zone" {
  type        = string
  description = "Zone of the instance"
  default     = "us-central1-a"
}

variable "image" {
  type        = string
  description = "Boot disk image"
  default     = "debian-cloud/debian-9"
}
```

### outputs.tf

```
output "instance_ip" {
  value       = google_compute_instance.instance.network_interface[0].access_config[0].nat_ip
  description = "Public IP of the instance"
}
```

---

**Step 3: Utilizing the Module**

### **Example Usage in a Terraform Configuration**

### Directory Structure:

```
my-gcp-deployment/
│
├── main.tf
└── variables.tf
```

### main.tf

```
module "gcp_instance" {
  source      = "./my-gcp-instance-module"
  name        = var.instance_name
  machine_type = var.machine_type
}

output "deployed_instance_ip" {
  value = module.gcp_instance.instance_ip
}
```

### variables.tf

```
variable "instance_name" {
  type    = string
  default = "my-instance"
}

variable "machine_type" {
  type    = string
  default = "f1-micro"
}
```

---

**Step 4: Initializing and Applying the Configuration**

1. **Initialize Terraform:**
    
    ```bash
    terraform init
    ```
    
2. **Apply Configuration:**
    
    ```bash
    terraform apply
    ```
    
    Review and approve the execution plan.
    

---

**Conclusion**

Terraform modules enable you to encapsulate, reuse, and manage infrastructure code effectively, promoting a modular and scalable IaC approach. By understanding and implementing modules, you can enhance the maintainability and reusability of your Terraform configurations, streamlining your infrastructure management practices.

In the upcoming articles, we will delve deeper into advanced Terraform topics, exploring practices like state management, collaboration, and handling dependencies with Terraform. Join us as we continue to explore the expansive world of Terraform and Infrastructure as Code!