# Task 17: Decrypt and use the encrypted data during playbook execution.

In the realm of automation, safeguarding sensitive data is paramount. Ansible Vault offers a robust solution for encrypting and protecting such data within your playbooks and roles. However, at some point, you'll need to access this encrypted information during playbook execution. In this article, we will explore the process of decrypting Ansible Vault and utilizing the sensitive data within your automation tasks.

---

**Step 1: Why Decrypt Ansible Vault?**

### **A. Use Cases:**

- Retrieving encrypted passwords.
- Accessing API keys.
- Decrypting configuration files.

### **B. Prerequisites:**

- You have an encrypted Ansible Vault file (e.g., **`secret_data.yml`**).

---

**Step 2: Decrypting Ansible Vault**

### **A. Decrypting Manually:**

Use the **`ansible-vault decrypt`** command to decrypt an Ansible Vault file.

```bash
ansible-vault decrypt secret_data.yml
```

### **B. Decrypting Prompted by Playbook:**

When running a playbook that uses an encrypted Vault file, Ansible will prompt you for the Vault password.

```bash
ansible-playbook -i inventory.ini my_playbook.yml --ask-vault-pass
```

### **C. Using a Vault Password File:**

Alternatively, use the **`--vault-password-file`** option to specify a file containing the Vault password.

```bash
ansible-playbook -i inventory.ini my_playbook.yml --vault-password-file vault_pass.txt
```

### **D. Editing Decrypted Files:**

After decryption, you can edit the file as needed using any text editor.

```bash
vim secret_data.yml
```

---

**Step 3: Using Decrypted Data in Playbooks**

### **A. Referencing Decrypted Vault Data:**

In your playbook, reference the decrypted Vault data as variables.

```yaml
- name: Deploy Application
  hosts: app_servers
  become: yes
  tasks:
    - name: Ensure API Key is present
      set_fact:
        my_api_key: "{{ vault_api_key }}"
      when: my_api_key is undefined
```

### **B. Running Playbooks:**

When running a playbook that uses decrypted Vault data, Ansible will access the decrypted information without additional prompts.

```bash
ansible-playbook -i inventory.ini my_playbook.yml
```

---

**Step 4: Handling Decrypted Data Securely**

### **A. Best Practices:**

- Keep decrypted data files secure.
- Limit access to decrypted data to authorized personnel.
- Avoid storing decrypted data in version control.

---

**Conclusion**

Decrypting Ansible Vault and utilizing encrypted data within your playbooks is essential for managing sensitive information securely. Whether you need to access passwords, API keys, or configuration files, Ansible Vault ensures that your automation processes remain efficient and your sensitive data remains protected.

In future articles, we will explore advanced Ansible topics and real-world use cases to further elevate your automation skills.