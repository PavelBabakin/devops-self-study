# Task 13: Configure IP addresses, netmasks, and gateways for static and DHCP setups.

In the digital age, ensuring seamless connectivity is paramount. A foundational step in this process is the correct configuration of IP addresses, netmasks, and gateways. Whether you're setting up a static IP or relying on DHCP, understanding these configurations is essential. In this guide, we'll delve into configuring IP addresses, netmasks, and gateways for both static and DHCP setups.

**1. Understanding IP Configuration**:

- **IP Address**: A unique identifier for a device on a network.
- **Netmask**: Determines the range of IP addresses in a subnet.
- **Gateway**: The device (usually a router) that connects a local network to other networks.

**2. DHCP Setup**:

- **Understanding DHCP**:
DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses and other network configuration information to devices.
- **Configuring DHCP**:
    - **Ubuntu/Debian & RHEL Derivatives**:
    Edit the network configuration file (e.g., **`/etc/network/interfaces`** or **`/etc/sysconfig/network-scripts/ifcfg-eth0`**) and set the method to DHCP.
    - **FreeBSD**:
    Edit **`/etc/rc.conf`** and add:
        
        ```bash
        ifconfig_[interface]="DHCP"
        ```
        
        Replace **`[interface]`** with the appropriate network interface name.
        

**3. Static IP Setup**:

- **Configuring Static IP**:
    - **Ubuntu/Debian**:
    Edit **`/etc/network/interfaces`**:
        
        ```bash
        iface [interface] inet static
        address [your_ip]
        netmask [your_netmask]
        gateway [your_gateway]
        ```
        
    - **RHEL Derivatives**:
    Edit the appropriate file in **`/etc/sysconfig/network-scripts/`** (e.g., **`ifcfg-eth0`**):
        
        ```bash
        BOOTPROTO=static
        IPADDR=[your_ip]
        NETMASK=[your_netmask]
        GATEWAY=[your_gateway]
        ```
        
    - **FreeBSD**:
    Edit **`/etc/rc.conf`**:
        
        ```bash
        ifconfig_[interface]="inet [your_ip] netmask [your_netmask]"
        defaultrouter="[your_gateway]"
        ```
        

**4. Applying Changes**:

After making the necessary configurations, restart the network service to apply the changes:

```bash
sudo systemctl restart networking (Ubuntu/Debian)
sudo systemctl restart network (RHEL Derivatives)
sudo service netif restart && sudo service routing restart (FreeBSD)
```

**Conclusion**:
Configuring IP addresses, netmasks, and gateways is a foundational skill for anyone managing networks or systems. Whether you're setting up a static configuration or leveraging the automation of DHCP, understanding these setups ensures seamless connectivity and optimal network performance. As with all technical areas, hands-on practice and continuous exploration are key to mastery.