# Task 22: Set up a VPC with custom subnets.

Virtual Private Cloud (VPC) in Google Cloud Platform provides a private network space, where users can provision Google Cloud resources, such as VM instances and databases. It allows users to define their own IP address space, create subnets, and configure route tables and network gateways. In this guide, we will explore how to set up a VPC with custom subnets, providing a hands-on approach to managing network resources in GCP.

**Step 1: Navigating to VPC Network**

- **Access GCP Console**: Log into the [Google Cloud Console](https://console.cloud.google.com/).
- **Navigate to VPC Network**: From the navigation menu on the left, click on “VPC Network”.

**Step 2: Creating a VPC**

- **Create VPC**: Click on “Create VPC”.
- **Configure the VPC**: Define the name and description for your VPC.
- **Subnets**: Define custom subnets by specifying the name, region, and IP address range.
- **Firewall Rules**: Optionally, configure firewall rules to control the traffic within the VPC.
- **Create**: Click on “Create” to deploy the VPC.

**Step 3: Verifying the VPC and Subnets**

- **Navigate to the VPC**: Click on the name of the VPC you created.
- **Verify Subnets**: Ensure that the subnets are created as per the configurations defined.
- **Firewall Rules**: Verify the firewall rules and ensure they are configured as per your requirements.

**Step 4: Deploying Resources in the VPC**

- **Create VM Instance**: Navigate to “Compute Engine” -> “VM instances” and click on “Create Instance”.
- **Configure VM**: Define the name, region, and machine type. Under “Networking”, select the VPC and subnet where the VM should be deployed.
- **Deploy**: Click on “Create” to deploy the VM instance.

**Step 5: Testing Network Connectivity**

- **SSH into VM**: Click on the “SSH” button next to your VM instance to connect to it using a secure shell.
- **Ping Test**: Optionally, create another VM in a different subnet and perform a ping test to verify the connectivity between VMs across subnets.

**Conclusion**

Setting up a VPC with custom subnets in Google Cloud Platform provides a foundational understanding of managing network resources and architecting network in the cloud. From creating a VPC to deploying resources within it, GCP offers a robust and scalable platform for handling various network configurations and requirements. As we continue to explore GCP, our subsequent guides will delve into more advanced networking practices and scenarios with VPC. Stay tuned for more hands-on tasks and insights!