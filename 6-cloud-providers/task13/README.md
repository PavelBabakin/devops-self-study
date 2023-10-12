# Task 13: Set up a Virtual Network (VNet) with multiple subnets.

Microsoft Azure Virtual Network (VNet) is a fundamental building block for your private network in Azure. VNet enables many types of Azure resources, such as Azure Virtual Machines (VM), to securely communicate with each other, the internet, and on-premises networks. In this guide, we will explore how to set up a VNet and configure multiple subnets to organize and manage resources in a segmented manner.

**Step 1: Creating a Virtual Network**

- **Navigate to Virtual Networks**: From the Azure Portal, click on “Create a resource”, and select “Virtual network”.
- **Basics**: Configure the basic settings, including subscription, resource group, name, and region.
- **IP Address Space**: Define the IP address space that will be used by the VNet.
- **Subnet**: Define the first subnet for your VNet.
- **Security**: Configure DDoS protection and firewall settings.
- **Review + Create**: Review your configurations and click “Create” to deploy the VNet.

**Step 2: Adding Additional Subnets**

- **Navigate to the VNet**: Once created, go to the VNet you just created.
- **Subnets**: Click on “Subnets” in the left navigation.
- **Add Subnet**: Click on “+ Subnet”, assign a name, and define the address range.
- **Create**: Click “Add” to create the additional subnet.

**Step 3: Configuring Network Security Group (NSG) Rules**

- **Navigate to NSGs**: From the Azure Portal, click on “Create a resource”, and select “Network security group”.
- **Basics**: Configure the basic settings, including name, subscription, and resource group.
- **Inbound/Outbound Rules**: Define rules to control inbound and outbound traffic to network interfaces (NIC), VMs, and subnets.
- **Associate to Subnet**: Under “Subnets”, associate the NSG to the desired subnet in your VNet.

**Step 4: Deploying Resources in Subnets**

- **Create Resources**: Deploy resources like VMs, ensuring to select the desired VNet and subnet during configuration.
- **Verify Connectivity**: Ensure resources within the VNet can communicate with each other and validate connectivity based on NSG rules.

**Step 5: Connecting to Resources**

- **Public IP**: Optionally, assign a public IP to resources to enable communication from the internet.
- **RDP/SSH**: Use Remote Desktop Protocol (for Windows) or Secure Shell (for Linux) to connect to VMs deployed within the VNet.

**Conclusion**

Setting up a Virtual Network with multiple subnets in Azure provides a structured and secure environment to deploy and manage resources. By segmenting resources into subnets and controlling traffic with NSG rules, you can build scalable and secure applications in Azure. As we continue to explore Azure, our subsequent guides will delve into more advanced networking and security concepts, ensuring you build a comprehensive skillset in cloud computing. Stay tuned for more hands-on tasks and insights!