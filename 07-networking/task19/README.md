# Task 19: Harden your SSH configuration: disable root login, change the default port, and set up fail2ban for intrusion prevention.

SSH (Secure Shell) is a widely used protocol for secure communication between systems. While it is secure by design, additional hardening practices enhance its security further, safeguarding your system against potential threats. In this guide, we will explore how to harden your SSH configuration by disabling root login, changing the default port, and setting up fail2ban for intrusion prevention.

**Prerequisites**

- A Linux machine with SSH installed
- Basic understanding of terminal commands
- Root or sudo access to the server

**Step 1: Disabling Root Login**

1. **Edit SSH Configuration**:
    
    ```bash
    sudo nano /etc/ssh/sshd_config
    ```
    
2. **Disable Root Login**:
Find and modify the following line to disable root login via SSH:
    
    ```perl
    PermitRootLogin no
    ```
    
3. **Restart SSH Service**:
    
    ```bash
    sudo systemctl restart ssh
    ```
    

**Step 2: Changing the Default SSH Port**

1. **Edit SSH Configuration**:
    
    ```bash
    sudo nano /etc/ssh/sshd_config
    ```
    
2. **Change SSH Port**:
Find and modify the following line to change the default SSH port (default is 22):Replace **`[desired_port_number]`** with your chosen port number.
    
    ```bash
    Port [desired_port_number]
    ```
    
3. **Restart SSH Service**:
    
    ```bash
    sudo systemctl restart ssh
    ```
    

**Step 3: Installing and Configuring fail2ban**

1. **Install fail2ban**:
    
    ```bash
    sudo apt install fail2ban
    ```
    
2. **Start and Enable fail2ban**:
    
    ```bash
    sudo systemctl start fail2ban
    sudo systemctl enable fail2ban
    ```
    
3. **Create a Custom Configuration File**:
    
    ```bash
    sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
    ```
    
4. **Configure fail2ban**:
Edit the **`jail.local`** file and configure it according to your needs. For SSH hardening, ensure the **`[sshd]`** section is configured appropriately.
    
    ```bash
    sudo nano /etc/fail2ban/jail.local
    ```
    
5. **Restart fail2ban**:
    
    ```bash
    sudo systemctl restart fail2ban
    ```
    

**Step 4: Monitoring and Managing fail2ban**

- **View Banned IPs**:
    
    ```bash
    sudo fail2ban-client status sshd
    ```
    
- **Unban an IP**:Replace **`[IP_Address]`** with the IP address you wish to unban.
    
    ```bash
    sudo fail2ban-client set sshd unbanip [IP_Address]
    ```
    

**Conclusion**

Hardening your SSH configuration is a crucial step in securing your server against unauthorized access and potential attacks. By disabling root login, changing the default SSH port, and implementing fail2ban, you add multiple layers of security that significantly enhance your system’s resilience against cyber threats.

In the forthcoming articles, we will explore more about secure server management, advanced SSH usage, and additional security practices to safeguard your systems. Stay tuned to continue enhancing your skills in secure communications and server management!