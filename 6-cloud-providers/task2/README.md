# Task 2: Launch an EC2 instance and SSH into it.

After successfully setting up your AWS account and familiarizing yourself with the management console, it's time to delve deeper into one of AWS's core services - Amazon Elastic Compute Cloud (EC2). EC2 allows users to run virtual servers on-demand, providing scalable compute capacity. In this guide, we will walk through launching an EC2 instance and connecting to it using SSH.

**Step 1: Launching an EC2 Instance**

- **Navigate to EC2**: From the AWS Management Console, click on “Services” and select “EC2”.
- **Launch Instance**: Click on the “Launch Instance” button to initiate the setup.
- **Choose an Amazon Machine Image (AMI)**: Select an AMI, which is a template that contains the software configuration (like operating system, application server, and applications) required to launch your instance.
- **Choose an Instance Type**: Select the hardware configuration for your instance. For general-purpose tasks, you might select a type within the “t” series.
- **Configure Instance**: Adjust settings like the number of instances and network configurations.
- **Add Storage**: Attach storage to your instance, considering your application’s requirements.
- **Tag Instance**: Assign a tag to your instance, which involves creating a Key-Value pair to help identify and manage the instance.
- **Configure Security Group**: Define the security group, which acts as a virtual firewall, controlling the traffic for one or more instances.
- **Review and Launch**: Review your instance configurations and click “Launch”.
- **Key Pair**: Choose an existing key pair or create a new one. Download and securely store the .pem file, which will be used to SSH into the instance.

**Step 2: SSH into Your EC2 Instance**

- **Retrieve Public DNS**: From the EC2 dashboard, select your instance and retrieve the Public DNS (IPv4) from the description.
- **Open Terminal**: On your local machine, open the terminal (or command prompt/PowerShell for Windows users).
- **Locate PEM File**: Navigate to the directory where your .pem file is stored.
- **Connect via SSH**: Use the following command, replacing **`[your-key-pair].pem`** with your .pem file name and **`[your-instance-public-dns]`** with your instance’s Public DNS:
    
    ```bash
    ssh -i "[your-key-pair].pem" ec2-user@[your-instance-public-dns]
    ```
    
- **Explore**: Once connected, you have access to your instance via the command line. Explore and manage your instance as per your requirements.

**Conclusion**

Successfully launching an EC2 instance and establishing an SSH connection marks a significant step in your AWS journey. You've not only created a virtual server but also interacted with it, providing a foundation for hosting applications, databases, and more in the future. In our upcoming guides, we will explore further into AWS services, ensuring you build a robust understanding and skillset in cloud computing. Stay tuned!