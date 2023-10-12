# Task 11: Launch a virtual machine (VM) and RDP/SSH into it.

Virtual Machines (VMs) in Azure offer the ability to deploy a wide range of computing solutions in an agile way. With Azure VMs, you can deploy virtualized Windows or Linux servers within minutes, scaling your resources according to your needs. In this guide, we will explore how to launch a VM in Azure and connect to it using Remote Desktop Protocol (RDP) and Secure Shell (SSH).

**Step 1: Creating a Virtual Machine**

- **Navigate to VMs**: From the Azure Portal, click on “Create a resource”, and select “Virtual Machine”.
- **Basics**: Configure the basic settings for the VM, including subscription, resource group, VM name, region, availability options, image, and size.
- **Administrator Account**: Set up an administrator account by providing a username and either a password or SSH public key.
- **Inbound Port Rules**: Choose which ports to allow - select RDP (3389) for Windows VMs and SSH (22) for Linux VMs.
- **Disks**: Choose the type of OS disk and optionally add additional data disks.
- **Networking**: Configure the virtual network, subnet, public IP, and NIC.
- **Management**: Configure monitoring, auto-shutdown, and backup settings.
- **Review + Create**: Review your configurations and click “Create” to deploy the VM.

**Step 2: Connecting to the VM**

- **Windows VM (RDP)**
    - **Download RDP File**: Once the VM is deployed, go to the VM’s overview page, click on “Connect”, select “RDP”, and download the RDP file.
    - **Remote Desktop Connection**: Open the RDP file using a Remote Desktop client, enter the username and password you configured, and connect to the VM.
- **Linux VM (SSH)**
    - **SSH Command**: Navigate to the VM’s overview page, click on “Connect”, select “SSH”, and copy the SSH command.
    - **Terminal**: Open a terminal, paste the SSH command, and connect to the VM using the credentials or SSH key you configured.

**Step 3: Managing and Monitoring the VM**

- **Stop/Start**: You can stop or start the VM from the overview page to manage costs and availability.
- **Metrics**: Navigate to “Metrics” to monitor the performance and health of the VM.
- **Disks**: Visit the “Disks” section to manage and add additional storage.
- **Networking**: Manage network interfaces, IP addresses, and network security group rules in the “Networking” section.

**Conclusion**

Launching a VM and connecting to it via RDP/SSH in Azure provides a flexible and scalable environment to host your applications and services. With a wide array of available configurations and sizes, Azure VMs cater to various computing needs, from small-scale applications to large enterprise solutions. As we continue to explore Azure, our subsequent guides will delve into more functionalities and services, ensuring you build a comprehensive skillset in cloud computing. Stay tuned for more hands-on tasks and insights!