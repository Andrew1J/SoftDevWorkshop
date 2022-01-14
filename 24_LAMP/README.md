# how-to :: PROVISION A DIGITAL OCEAN DROPLET AND INSTALL UBUNTU 20.04.3 AND APACHE2.
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 30 minutes - 1 hour

### Prerequisites:
- A Digital Ocean account with a payment method
- You are breathing


## Instructions
### Set up a Droplet
#### We will be using SSH keys because password authentication is less secure. 
1. If you do not have SSH keys create one by typing 
    ```
    ssh key-gen
    ```
    and copying the contents of the key 
    ```
    cat /Users/your_username/.ssh/id_rsa.pub
    ```
2. In https://cloud.digitalocean.com/account/security, click Add SSH Key and copy and paste the contents of your ssh key into it. 
3. Log in to your Digital Ocean account and from the control panel, click Create -> Droplets. We will be using Ubuntu 20.04 with the Basic Plan and Regular Intel with SSD which should cost $5/month. 
4. Create your droplet!!!

### Initial Server Setup With Ubuntu 20.04
1. Connect to the as the root user (you can find the server ip in the droplets page of your Digital Ocean dashboard)
   ```
   ssh root@your_server_ip
   ```
3. Once you are logged in as root, we will add a new account to log into instead of root. (replace your_username with your username)
   ```
   adduser your_username
   ```
4. Grant your account with admin privileges
   ```
   usermod -aG sudo your_username
   ```
   Now you can use sudo on your new account!
5. Set up a basic firewall to make sure only connections to certain services are allowed.
   ```
   ufw allow OpenSSH
   ```
   ```
   ufw enable
   ```
   You can see that SSH connections are allowed by typing
   ```
   ufw status
   ```
   ```Output
   Status: active

   To                         Action      From
   --                         ------      ----
   OpenSSH                    ALLOW       Anywhere
   OpenSSH (v6)               ALLOW       Anywhere (v6)
   ```
   Currently the firewall is only allowing SSH connections!
6. You will need a copy of your local public key to use the new account
   ```
   rsync --archive --chown=your_username:your_username ~/.ssh /home/your_username
   ```
7. You should be able to log into the new user account by typing
   ```
   ssh your_username@your_server_ip
   ```
You should be good to go to install the apache web server! 

### Install the Apache Web Server on Ubuntu 20.04
1. Install the Apache2 package.
   ```
   sudo apt update
   ```
   ```
   sudo apt install apache2
   ```
2. Adjust firewall to allow access to the default web ports
   ```
   sudo ufw allow 'Apache'
   ```
   Verify the change by typing
   ```
   sudo ufw status
   ```
   ```
   Output
   Status: active
   To                         Action      From
   --                         ------      ----
   OpenSSH                    ALLOW       Anywhere                  
   Apache                     ALLOW       Anywhere                
   OpenSSH (v6)               ALLOW       Anywhere (v6)             
   Apache (v6)                ALLOW       Anywhere (v6)    
   ```
3. Check with the systemd init system to make sure the service is running by typing:
   ```
   sudo systemctl status apache2
   ```
   ```
   Output
    ● apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2020-04-23 22:36:30 UTC; 20h ago
       Docs: https://httpd.apache.org/docs/2.4/
    Main PID: 29435 (apache2)
      Tasks: 55 (limit: 1137)
     Memory: 8.0M
     CGroup: /system.slice/apache2.service
             ├─29435 /usr/sbin/apache2 -k start
             ├─29437 /usr/sbin/apache2 -k start
             └─29438 /usr/sbin/apache2 -k start
   ```
Go to http://your_server_ip, you should see the default Ubuntu 20.04 Apache web page with a red "It Works!" page. 

### Resources
* https://docs.digitalocean.com/tutorials/recommended-droplet-setup/
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
---

Accurate as of (last update): 2022-01-11

#### Contributors:  
Andrew Juang, pd2

_Note: the two spaces after each name are important! ( <--burn after reading)  _
