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
We should be good to go to install the apache web server! 

### Install the Apache Web Server on Ubuntu 20.04


### Resources
* https://docs.digitalocean.com/tutorials/recommended-droplet-setup/
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04

(please verify ; some of these are old links)

---

Accurate as of (last update): 2022-01-11

#### Contributors:  
Clyde "Thluffy" Sinclair  
Topher Mykolyk, pd0  

_Note: the two spaces after each name are important! ( <--burn after reading)  _
