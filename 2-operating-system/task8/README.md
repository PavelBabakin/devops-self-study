# Task 8: Add, modify, and delete users and groups on each system.

In the realm of system administration, managing users and groups is a fundamental task. Whether it's granting permissions, ensuring security, or simply organizing users, understanding how to effectively manage user accounts and groups is essential. In this guide, we'll explore how to add, modify, and delete users and groups on Ubuntu/Debian, FreeBSD, and RHEL derivatives.

**1. Ubuntu/Debian & RHEL Derivatives**:

- **Adding Users**:
    
    ```bash
    sudo useradd [username]
    sudo passwd [username]
    ```
    
- **Modifying Users**:
    - Change username: **`sudo usermod -l [new_username] [old_username]`**
    - Change home directory: **`sudo usermod -d /path/to/new/home [username]`**
- **Deleting Users**:
    
    ```bash
    sudo userdel [username]
    ```
    
- **Adding Groups**:
    
    ```bash
    sudo groupadd [groupname]
    ```
    
- **Modifying Groups**:
    - Rename group: **`sudo groupmod -n [new_groupname] [old_groupname]`**
- **Deleting Groups**:
    
    ```bash
    sudo groupdel [groupname]
    ```
    

**2. FreeBSD**:

- **Adding Users**:
    
    ```bash
    sudo adduser
    ```
    
    (This will initiate an interactive user creation process.)
    
- **Modifying Users**:
    
    ```bash
    sudo pw usermod [username] -n [new_username] -d /path/to/new/home
    ```
    
- **Deleting Users**:
    
    ```bash
    sudo pw userdel [username]
    ```
    
- **Adding Groups**:
    
    ```bash
    sudo pw groupadd [groupname]
    ```
    
- **Modifying Groups**:
    
    ```bash
    sudo pw groupmod [old_groupname] -n [new_groupname]
    ```
    
- **Deleting Groups**:
    
    ```bash
    sudo pw groupdel [groupname]
    ```
    

**Tips**:

- Always backup system files like **`/etc/passwd`**, **`/etc/shadow`**, and **`/etc/group`** before making changes.
- Be cautious when deleting users or groups to avoid unintentionally removing critical system accounts.
- Use the **`id`** command to view user and group IDs.

**Conclusion**:
Managing users and groups is a core responsibility in system administration. Whether you're working with Ubuntu/Debian, FreeBSD, or a RHEL derivative, this guide provides a step-by-step approach to effectively handle user and group operations. As always, practice makes perfect. Regularly working with these commands will ensure you're well-equipped to manage any user or group-related task.