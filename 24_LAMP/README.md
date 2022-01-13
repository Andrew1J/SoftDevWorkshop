# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 30 minutes

### Prerequisites:
- A Digital Ocean account with a payment method
- You are breathing


### Instructions
#### Set up a Droplet
##### We will be using SSH keys because password authentication is less secure. 
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

1. Step blah blah blah, and/or...
1. Step, with `inline code`, and/or...
1. Step, with
    ```
    generic code block or terminal command
    ```
   and/or...
    ```javascript
    var foo = "this that JS tho";
    ```
   and/or...
    ```python
    print("this that Python tho")
    ```
   and/or...
1. Step, with [hyperlink](https://xkcd.com)s...


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
