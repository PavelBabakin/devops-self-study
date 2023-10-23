# Task 20: Launch a Compute Engine instance and SSH into it.

Google Compute Engine delivers virtual machines (VMs) running in Google's innovative data centers and worldwide fiber network. It allows users to easily run large-scale workloads with the benefits of robust performance, flexibility, and cost-effectiveness. In this guide, we will walk through the steps to launch a Compute Engine instance and SSH into it, providing a hands-on approach to managing VMs in Google Cloud Platform (GCP).

**Step 1: Navigating to Compute Engine**

- **Access GCP Console**: Log into the [Google Cloud Console](https://console.cloud.google.com/).
- **Navigate to Compute Engine**: From the navigation menu on the left, click on “Compute Engine” and then “VM instances”.

**Step 2: Launching a VM Instance**

- **Create Instance**: Click on “Create Instance”.
- **Configure the VM**: Define the name, region, machine type, and boot disk for your VM. Customize the settings according to your use case.
- **Firewall**: Optionally, allow HTTP/HTTPS traffic if your application requires it.
- **Create**: Click on “Create” to deploy the VM instance.

**Step 3: SSH into the VM Instance**

- **SSH Options**: Once the VM is deployed, click on the “SSH” dropdown next to your VM instance.
- **Open in Browser Window**: Select “Open in browser window” to SSH into the VM using a browser-based terminal.
- **Using gcloud**: Alternatively, you can use the **`gcloud`** CLI to SSH into the VM:
    
    ```bash
    gcloud compute ssh [INSTANCE_NAME] --zone=[ZONE]
    ```
    
- **Using SSH Client**: Or use an SSH client with the provided external IP and SSH keys.

**Step 4: Managing the VM Instance**

- **Execute Commands**: Once SSH’ed into the VM, you can execute commands, install software, and manage workloads.
- **Transfer Files**: Use **`scp`** or **`gcloud compute scp`** to transfer files between your local machine and the VM.
- **Monitor**: Navigate to the “Monitoring” tab in the VM instance details to view usage charts and logs.

**Step 5: Cleaning Up**

- **Stop the VM**: If you wish to preserve the VM for future use but avoid continuous billing, stop the VM.
- **Delete the VM**: To permanently delete the VM and associated resources, click on “Delete”.

**Conclusion**

Launching a Compute Engine instance and SSH’ing into it provides a foundational understanding of managing VMs in Google Cloud. From deploying VMs to executing commands, Compute Engine offers a scalable and flexible environment for running your applications and workloads. As we continue to explore GCP, our subsequent guides will delve into more advanced functionalities and management practices with Compute Engine. Stay tuned for more hands-on tasks and insights!