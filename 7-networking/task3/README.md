# Task 3: Secure your FTP connection by setting up an SFTP server (Secure FTP over SSH).

Security is paramount in managing file transfers, especially when dealing with sensitive data. SFTP (Secure File Transfer Protocol) provides a secure method of transferring files by leveraging SSH (Secure Shell) to encrypt the data being transmitted. In this guide, we will explore the steps to set up an SFTP server, ensuring secure file transfers and enhancing the security posture of our FTP server.

**Prerequisites**

- An FTP server set up and running
- SSH enabled on your server
- Basic knowledge of Linux terminal commands

**Step 1: Enabling SSH on Your Server**

1. **Install OpenSSH Server**: If not already installed, install the OpenSSH server package.
    
    ```bash
    sudo apt update
    sudo apt install openssh-server
    ```
    
2. **Start and Enable SSH**: Ensure SSH is running and enabled to start at boot.
    
    ```bash
    sudo systemctl start ssh
    sudo systemctl enable ssh
    ```
    

**Step 2: Configuring SFTP**

1. **Backup SSH Configuration**: It’s prudent to backup configuration files before making changes.
    
    ```bash
    sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.orig
    ```
    
2. **Edit SSH Configuration**: Open the SSH daemon configuration file for editing.
    
    ```bash
    sudo nano /etc/ssh/sshd_config
    ```
    
    - Ensure SSH is using a different port (other than the default 22) for enhanced security:
        
        ```
        Port [Your-Preferred-Port-Number]
        ```
        
    - Enable SFTP by ensuring the following line is present:
        
        ```
        Subsystem sftp /usr/lib/openssh/sftp-server
        ```
        
    - Save and exit the text editor.
3. **Restart SSH**: Apply the changes by restarting the SSH service.
    
    ```bash
    sudo systemctl restart ssh
    ```
    

**Step 3: Connecting via SFTP**

1. **Using the Terminal**: You can connect to the SFTP server directly from the terminal.
    
    ```bash
    sftp -P [Your-SSH-Port] [username]@[your-server-ip]
    ```
    
    Replace **`[Your-SSH-Port]`**, **`[username]`**, and **`[your-server-ip]`** with your SSH port number, username, and server IP address, respectively.
    
2. **Using FileZilla**:
    - Open FileZilla and enter the following details:
        - **Host**: sftp://[your-server-ip]
        - **Username**: Your FTP user
        - **Password**: Your FTP password
        - **Port**: [Your-SSH-Port]
    - Click “Quickconnect” to establish a secure SFTP connection.

**Step 4: Managing Files Securely**

- Navigate and manage files as you would with FTP, with the assurance that data transmission is encrypted and secure.

**Conclusion**

Securing your file transfers with SFTP is a vital step in safeguarding data integrity and confidentiality during transmission. By leveraging SSH, SFTP ensures that your files are securely transferred, mitigating the risks of data interception.

In the next segment, we will explore further into HTTP/HTTPS, diving into setting up web servers and understanding the HTTP request/response cycle. Stay tuned to continue enhancing your DevOps expertise!