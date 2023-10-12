# Task 4: Set up a VPC with a public and private subnet.

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch Amazon Web Services (AWS) resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS. In this guide, we will walk through the process of setting up a VPC and creating both public and private subnets within it.

**Step 1: Creating Your VPC**

- **Navigate to VPC**: From the AWS Management Console, click on “Services” and select “VPC”.
- **Your VPCs**: Click on “Your VPCs” in the left navigation pane.
- **Create VPC**: Click on the “Create VPC” button.
- **Name and CIDR Block**: Assign a name to your VPC and specify a CIDR block (e.g., 10.0.0.0/16).
- **Tenancy**: Choose “Default” tenancy and click “Create”.

**Step 2: Creating a Public Subnet**

- **Subnets**: In the VPC dashboard, click on “Subnets”.
- **Create Subnet**: Click on the “Create subnet” button.
- **VPC, Name, and CIDR Block**: Select the VPC you created, assign a name, and specify a CIDR block for the subnet (e.g., 10.0.1.0/24).
- **Availability Zone**: Select an availability zone and ensure “Auto-assign IPv4 public IP” is enabled to make it a public subnet.
- **Create**: Click on the “Create” button.

**Step 3: Creating a Private Subnet**

- **Create Subnet**: Click on the “Create subnet” button again.
- **VPC, Name, and CIDR Block**: Select the VPC, assign a different name, and specify a different CIDR block (e.g., 10.0.2.0/24).
- **Availability Zone**: Select an availability zone (preferably different from the public subnet) and ensure “Auto-assign IPv4 public IP” is disabled to make it a private subnet.
- **Create**: Click on the “Create” button.

**Step 4: Configuring Route Tables**

- **Route Tables**: In the VPC dashboard, click on “Route Tables”.
- **Create Route Table**: Click on the “Create route table” button.
- **Name and VPC**: Assign a name and select your VPC.
- **Create**: Click on the “Create” button.
- **Edit Subnet Associations**: Select your new route table, click on the “Subnet Associations” tab, and associate your public subnet.
- **Routes**: In the “Routes” tab, add a route to allow traffic to the internet via an Internet Gateway (which you may need to create).

**Conclusion**

Successfully setting up a VPC with both public and private subnets lays a solid foundation for deploying applications in a secure and scalable environment. This configuration allows you to manage accessibility, ensuring public-facing components are reachable, while maintaining the privacy of backend systems. As we continue to explore AWS, our upcoming guides will delve into more functionalities and services, ensuring you build a comprehensive skillset in cloud computing. Stay tuned and happy learning!