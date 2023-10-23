# Task 6: Set up HTTPS on your web server using Let's Encrypt to obtain a free SSL/TLS certificate.

In an era where cybersecurity is paramount, securing web traffic through HTTPS (HyperText Transfer Protocol Secure) has become indispensable. HTTPS encrypts data in transit, safeguarding it from eavesdroppers and man-in-the-middle attacks. Let's Encrypt provides free SSL/TLS certificates and an automated process to set up HTTPS. In this guide, we will explore how to secure a web server with HTTPS using Let's Encrypt.

**Prerequisites**

- A domain name pointing to your web server
- Nginx or Apache web server installed
- Root or sudo access to the server
- Basic understanding of terminal commands

**Step 1: Installing Certbot**

1. **Update System Repositories**:
    
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
    
2. **Install Certbot**:
    - For Nginx:
        
        ```bash
        sudo apt install certbot python3-certbot-nginx
        ```
        
    - For Apache:
        
        ```bash
        sudo apt install certbot python3-certbot-apache
        ```
        

**Step 2: Obtaining a Let's Encrypt SSL/TLS Certificate**

1. **Generate Certificate**:
    - For Nginx:
        
        ```bash
        sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
        ```
        
    - For Apache:
        
        ```bash
        sudo certbot --apache -d yourdomain.com -d www.yourdomain.com
        ```
        
    
    Replace **`yourdomain.com`** with your actual domain name.
    
2. **Follow Prompts**: Answer the questions prompted by Certbot, providing an email address and agreeing to the terms of service.
3. **HTTPS Configuration**: Certbot will automatically configure HTTPS for your server.

**Step 3: Verifying HTTPS Implementation**

- Navigate to **`https://yourdomain.com`** and observe the padlock icon in the address bar, indicating a secure connection.

**Step 4: Automating Certificate Renewal**

- Let's Encrypt certificates are valid for 90 days. Set up automatic renewal by editing the crontab.
    
    ```bash
    sudo crontab -e
    ```
    
- Add the following line to automate renewal and reload the web server to apply the new certificate:Replace **`nginx`** with **`apache2`** if using Apache.
    
    ```bash
    0 3 * * * /usr/bin/certbot renew --quiet && systemctl reload nginx
    ```
    

**Conclusion**

Congratulations! You have successfully secured your web server with HTTPS using a free SSL/TLS certificate from Let's Encrypt. Implementing HTTPS is vital in protecting data integrity and confidentiality, ensuring secure communication between users and your server.

In the next articles, we will explore further into redirecting HTTP traffic to HTTPS and delve deeper into SSL/TLS and DNS. Stay tuned to continue fortifying your knowledge in managing secure and efficient web servers!