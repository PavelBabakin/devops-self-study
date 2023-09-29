# Task 16: Harden SSH access (disable root login, use key-based authentication).

SSH (Secure Shell) is a protocol widely used for secure remote access to systems. While it offers encrypted communication, its security can be further enhanced. In this guide, we'll focus on two critical steps to harden SSH access: disabling root login and implementing key-based authentication.

**1. Disabling Root Login**:

- **Why It's Important**:
The root user has unrestricted access to the system. By disabling root login via SSH, we add an extra layer of security, making it harder for unauthorized users to gain control.
- **How to Disable**:
    1. Edit the SSH configuration file: **`sudo nano /etc/ssh/sshd_config`**
    2. Find the line that says **`PermitRootLogin`** and modify it to: **`PermitRootLogin no`**
    3. Save and close the file.
    4. Restart the SSH service: **`sudo systemctl restart sshd`**

**2. Key-Based Authentication**:

- **Understanding Key-Based Authentication**:
Instead of using passwords, which can be brute-forced, key-based authentication uses a pair of cryptographic keys: a private key (kept secret) and a public key (shared with the server).
- **Setting Up Key-Based Authentication**:
    1. Generate a key pair: **`ssh-keygen`**
    2. By default, this will create a private key (**`~/.ssh/id_rsa`**) and a public key (**`~/.ssh/id_rsa.pub`**).
    3. Copy the public key to the server: **`ssh-copy-id username@server_ip`**
    4. Once the key is copied, edit the SSH configuration file on the server (**`/etc/ssh/sshd_config`**) and ensure **`PasswordAuthentication`** is set to **`no`**.
    5. Restart the SSH service.

**Tips**:

- Always backup configuration files before making changes.
- Regularly update your SSH keys and consider using passphrase protection for added security.
- Monitor SSH logs (**`/var/log/auth.log`** or **`/var/log/secure`**) for any suspicious activity.

**Conclusion**:
Hardening SSH access is a crucial step in system security. By disabling root logins and implementing key-based authentication, we significantly reduce the risk of unauthorized access. As with all security measures, regular reviews, updates, and monitoring are essential to maintain a fortified system.