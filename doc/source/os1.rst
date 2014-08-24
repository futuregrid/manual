**********************************************************************
 Running an OpenStack Appliance on FutureGrid
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:
      
      

Background
~~~~~~~~~~

This tutorial guides you through the steps of deploying and using an OpenStack virtual environment which can be used for development, testing, education and training activities. 

This tutorial uses Nimbus to create a private, single-node OpenStack environment within a virtual machine instance on FutureGrid - essentially using a form of "nested" virtualization to run a single-node OpenStack cloud within a Nimbus instance. 

OpenStack is a recently open sourced, IaaS cloud computing platform founded by Rackspace Hosting and NASA and widely used in industry. It includes three components:Compute(Nova),Object Storage (Swift) and Image Service (Glance). In this tutorial we only use Nova.
Running OpenStack as an appliance (i.e. via a virtual machine) gives users a sandboxed environment to explore OpenStack and to freely modify its configuration without affecting other users.

The OpenStack appliance is a KVM-based Nimbus virtual machine. Nimbus is installed on several FutureGrid clusters, however only the Alamo cluster is KVM-based and therefore supports the appliance.

The hands-on steps in this tutorial will show you the basic steps necessary to 1) instantiate the OpenStack appliance on FutureGrid using Nimbus and KVM-base virtualization, 2) log in interactively to the appliance, 3) configure the OpenStack environment, 4) instantiate a virtual machine instance within the appliance using OpenStack and QEMU-based virtualization, and 5) log in interactively to the OpenStack instance

 

 

Prerequisites
~~~~~~~~~~~~~

It is assumed the user is familiar with launching virtual machines with Nimbus, specifically how to setup and use the Nimbus cloud client and credentials. If not refer to this FutureGrid Nimbus tutorial.

Getting Started
~~~~~~~~~~~~~~~

Lauch the appliance VM::

[user@node nimbus-cloud-client-019]$ bin/cloud-client.sh --conf conf/alamo.conf --run  
--name openstack-ubuntu-10.10-amd64.img.gz --hours 2 
Launching workspace.  
Workspace Factory Service: 
https://nimbus.futuregrid.tacc.utexas.edu:8443/wsrf/services/WorkspaceFactoryService  
Creating workspace "vm-007"... done.   
IP address: 129.114.32.101 
Hostname: vm-101.alamo.futuregrid.org 
Start time: Fri Jun 24 15:47:38 EDT 2011 
Shutdown time: Fri Jun 24 17:47:38 EDT 2011 
Termination time: Fri Jun 24 17:49:38 EDT 2011  
Waiting for updates.   
"vm-007" reached target state: Running  Running: 'vm-007'  


Log in as root::

[user@node nimbus-cloud-client-019]$ ssh root@129.114.32.101 
Linux virtual-machine 2.6.35-22-generic #33-Ubuntu SMP Sun Sep 19 20:32:27 UTC 2010  x86_64 GNU/Linux 
Ubuntu 10.10  

Welcome to Ubuntu! 
* Documentation: https://help.ubuntu.com/  

ew release 'natty' available. 
Run 'do-release-upgrade' to upgrade to it.   

The programs included with the Ubuntu system are free software; the exact distribution terms for each program are described in the individual files in /usr/share/doc/*/copyright.  

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by applicable law.  
 

Launching the VM Hosting OpenStack

On the Alamo cluster, the list of images will show the OpenStack appliance image:
[user@node ~]$ cd nimbus-cloud-client-019 [user@node nimbus-cloud-client-019]$ bin/cloud-client.sh --conf conf/alamo.conf --list  ...  [Image] 'openstack-ubuntu-10.10-amd64.img.gz' Read only Modified: Jun 29 2011 @ 10:50 Size: 900046867 bytes (~858 MB)  ... 
 

Using OpenStack

Once logged in, there is a text file in /root/ named openstack.txt that describes how to create a project and instantianate OpenStack Compute instances. The following elaborates on the contents of that text file.
First create an Nova user named "testadmin":

root@virtual-machine:~# nova-manage user admin testadmin export EC2_ACCESS_KEY=fcb33f63-742f-469f-b7e1-ef49c6f24d5f export EC2_SECRET_KEY=e6b85615-dcf5-40ef-b340-c8ddb7f7b90c 
Create a project named "testproj" administered by the user just created:
root@virtual-machine:~# nova-manage project create testproj
testadmin
Generate the file nova.zip that holds the credentials for the newly created project:
root@virtual-machine:~# nova-manage project zipfile testproj
testadmin
The credentials include environments variables that are to be sourced:
root@virtual-machine:~# unzip nova.zip Archive: nova.zip extracting: novarc  extracting: pk.pem  extracting: cert.pem  extracting: cacert.pem  root@virtual-machine:~# .
novarc
Generate the keypair that will be used for ssh logins into Compute instances:
root@virtual-machine:~# euca-add-keypair testkey >testkey.pem  root@virtual-machine:~# chmod 600 testkey.pem 
Allow ICMP (for ping) and ssh into Compute instances:
root@virtual-machine:~# euca-authorize default -P icmp -t -1:-1 GROUP default PERMISSION default ALLOWS icmp -1 -1 root@virtual-machine:~# euca-authorize default -P tcp -p 22 -s 0.0.0.0/0 GROUP default PERMISSION default ALLOWS tcp 22 22 FROM CIDR 0.0.0.0/0

Lauch an OpenStack Compute Instance

Download and install an image that is to be used for Compute instances:
root@virtual-machine:~# wget http://smoser.brickies.net/ubuntu/ttylinux-uec/ttylinux-uec-amd64-12.1_2.6.35-22_1.tar.gz --2011-06-24 16:05:07-- http://smoser.brickies.net/ubuntu/ttylinux-uec/ttylinux-uec-amd64-12.1_2.6.35-22_1.tar.gz Resolving smoser.brickies.net... 69.163.204.191 Connecting to smoser.brickies.net|69.163.204.191|:80... connected. HTTP request sent, awaiting response... 200 OK Length: 24346106 (23M) [application/x-tar] Saving to: `ttylinux-uec-amd64-12.1_2.6.35-22_1.tar.gz'  100%[=>] 24,346,106 1.21M/s in 21s 2011-06-24 16:05:28 (1.11 MB/s) - `ttylinux-uec-amd64-12.1_2.6.35-22_1.tar.gz' saved [24346106/24346106] root@virtual-machine:~# uec-publish-tarball ttylinux-uec-amd64-12.1_2.6.35-22_1.tar.gz ttylinux Fri Jun 24 16:05:47 EDT 2011: 
extracting image

 

kernel : ttylinux-uec-amd64-12.1_2.6.35-22_1-vmlinuz ramdisk: ttylinux-uec-amd64-12.1_2.6.35-22_1-initrd image : ttylinux-uec-amd64-12.1_2.6.35-22_1.img Fri Jun 24 16:05:47 EDT 2011:
bundle/upload kernel

 

Fri Jun 24 16:05:48 EDT 2011:
bundle/upload ramdisk

 

Fri Jun 24 16:05:49 EDT 2011:
bundle/upload image

 

Fri Jun 24 16:05:58 EDT 2011:
done

 

emi="ami-50e0e75b"; eri="ari-29563e11"; eki="aki-107fa561"; Note that this last line is a series of environment variables, source them before proceeding:
root@virtual-machine:~# emi="ami-50e0e75b"; eri="ari-29563e11"; eki="aki-107fa561" 
Now launch an OpenStack Compute instance:
root@virtual-machine:~# euca-run-instances $emi -k testkey -t m1.tiny RESERVATION r-9x69bs30 testproj default INSTANCE i-00000001 ami-50e0e75b scheduling  testkey (testproj, None) 0 m1.tiny 2011-06-24T20:26:49Z unknown zone 
Use euca-describe-instances to determine the status of the newly created instance:
root@virtual-machine:~# euca-describe-instances RESERVATION r-9x69bs30 testproj default INSTANCE i-00000001 ami-50e0e75b 10.0.0.3 10.0.0.3  running testkey (testproj, virtual-machine) 0m1.tiny 2011-06-24T20:26:49Z nova 
When it is running, log in to the instance:
root@virtual-machine:~# ssh -i testkey.pem root@10.0.0.3 The authenticity of host '10.0.0.3 (10.0.0.3)' can't be established. RSA key fingerprint is 95:e8:b7:74:30:da:42:a3:2d:94:03:73:32:08:7c:11. Are you sure you want to continue connecting (yes/no)? yes Warning: Permanently added '10.0.0.3' (RSA) to the list of known hosts.  Chop wood, carry water.  #  
You are now logged into the Compute instance.
