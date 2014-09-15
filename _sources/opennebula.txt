OpenNebula 2.0 Tutorial
=======================

This document is aimed to be a guide to start using OpenNebula 2.0.
Therefore, if you need more information about any particular OpenNebula
aspect that it is not addressed here, please refer to the official
documentation located in
(`http://www.opennebula.org/documentation:documentation <http://www.opennebula.org/documentation:documentation>`__)

If you are a user that is only interested in test OpenNebula with some
pre-configured VM, you can use this guide
(`http://www.opennebula.org/documentation:rel2.0:vmg <http://www.opennebula.org/documentation:rel2.0:vmg>`__).

ALL users have to add the following lines to their $HOME/.bashrc or
$HOME/.profile file.

::

    export PATH=$PATH:$ONE_LOCATION/bin
    export ONE_AUTH=$HOME/.one/one_ssh

Create a VM Image Contextualized for OpenNebula
===============================================

In this section we are going to explain how to create a KVM image and
how to contextualize for OpenNebula.

Create VM Image Using KVM
-------------------------

This process is generic and it is not related with OpenNebula directly.
Therefore, this image can be deploy in any machine with KVM and could be
used to create a VM image for any IaaS framework. The first step is
install KVM.

Ubuntu

::

    sudo apt-get install qemu kvm

    sudo apt-get install libvirt-bin

RHEL or CentOS

::

    sudo yum install kvm virt-manager

Be sure that the virtualization features of your machine are enabled in
the BIOS. If they are, you should be able to load the KVM
modules        

::

    sudo modprobe kvm-intel
    or
    sudo modprobe kvm-amd        

Now, we need to download the ISO that we are going to install in the VM,
in this case Ubuntu iso. You can do it from
`http://ubuntu-releases.cs.umn.edu/10.10/ubuntu-10.10-server-amd64.iso. <http://ubuntu-releases.cs.umn.edu/10.10/ubuntu-10.10-server-amd64.iso>`__

Every VM need a disk to be used as a virtual hard drive (1GB is enough
for Ubuntu server). Thus, to create this we use the next command:

::

    qemu-img create machine_name.img -f raw 1G

After this, we are prepared to boot the VM and install the OS.

::

    kvm -m 512 -cdrom /home/user/ubuntu-10.10-server-amd64.iso -boot d machine_name.img

This command will start the VM and you can install the OS as in a normal
PC. When you install the OS in the VM you can boot it using this
command:

::

    kvm -no-acpi -m 512 machine_name.img

 

Contextualize VM
----------------

There are two contextualization mechanisms available in OpenNebula: the
automatic IP assignment, and a more generic way to give any file and
configuration parameters. You can use any of them individually, or both.
Nevertheless, we need to prepare the VM image to use this mechanism
(`http://www.opennebula.org/documentation:rel2.0:cong <http://www.opennebula.org/documentation:rel2.0:cong>`__).  

 

First, download the vmcontext.sh  file in your machine. This file depend
of your linux distribution.

::

    http://dev.opennebula.org/projects/opennebula/repository/show/share/scripts

In this address you can find the vmcontext for each supported
distribution.
CentOS

::

    wget http://dev.opennebula.org/projects/opennebula/repository/revisions/master/raw/share/scripts/centos-5/net-vmcontext/vmcontext -O vmcontext.sh

Ubuntu

::

    wget http://dev.opennebula.org/projects/opennebula/repository/revisions/master/raw/share/scripts/ubuntu/net-vmcontext/vmcontext -O vmcontext.sh

Copy this file to the VM. To do that you can configure a network
interface in the VM and send the file using ssh. For example if your
machine has the private IP 192.168.1.1, you could assign to the VM the
192.168.1.2. So, execute this command in the VM:

::

    sudo ifconfig eht0 192.168.1.2

From your machine execute this command to send the file to your VM:

::

    scp vmcontext.sh 192.168.1.2:/home/user

In the VM copy the file to the /etc/init.d directory:

::

    sudo cp vmcontext.sh /etc/init.d
    sudo chmod +x /etc/init.d/vmcontext.sh

Configure init.d to execute the script during the VM startup
Centos

::

    sudo chkconfig --add vmcontext.sh

Ubuntu

::

    ln /etc/init.d/vmcontext.sh /etc/rc2.d/S01vmcontext.sh

Add at the end of this file (this may not be needed):

::

    ifup -a

or

::

    /etc/init.d/networking restart  #(in ubuntu)
    /etc/init.d/network restart     #(in centos)

Remove the udev persistent files (ubuntu only)

::

    sudo rm -f /etc/udev/rules.d/z25_persistent-net.rules

    sudo rm -f /etc/udev/rules.d/z45_persistent-net-generator.rules

 

With all these steps we have configured the automatic IP assignment in
the VM. Now, we need to enable the generic contextualization by copying
these lines to /etc/rc.local.

::

    mount -t iso9660 /dev/sr0 /mnt  #(in ubuntu)
    mount -t iso9660 /dev/hdc /mnt  #(in centos. Actually this depend on the initrd that you uses. If you use the one provided by Ubuntu then you use the previous line instead of this one)

    if [ -f /mnt/context.sh ]; then

          . /mnt/init.sh

    fi

    umount /mnt

    exit 0

 

The file init.sh is different for each distribution and you can find
them in the `OpenNebula
repository <http://dev.opennebula.org/projects/opennebula/repository/revisions/master/show/share/scripts>`__.
You do not need to include it in the VM because it is included
automatically by OpenNebula when you require it in the VM template.

 

Managing Virtual Machines
=========================

`(http://www.opennebula.org/documentation:rel2.0:vm\_guide) <http://www.opennebula.org/documentation:rel2.0:vm_guide>`__

A Virtual Machine within the OpenNebula system consists of:

-  A capacity in terms memory and CPU
-  A set of NICs attached to one or more virtual networks
-  A set of **disk images**.
-  A state file (optional) or **recovery file**, that contains the
   memory image of a running VM plus some hypervisor specific
   information.

The above items, plus some additional VM attributes like the OS kernel
and context information to be used inside the VM, are specified in a
**`VM
template <http://www.opennebula.org/documentation:rel2.0:template>`__**
file.

Each VM in OpenNebula is identified by an unique number, the ``<VID>``.
Also, the user can assign it a name in the `VM
template <http://www.opennebula.org/documentation:rel2.0:template>`__,
the default name for each VM is ``one-<VID>``.

Virtual Machine Template
------------------------

OpenNebula templates are designed to be hypervisor-agnostic, but there
are still some peculiarities to be taken into account, and mandatory
attributes change depending on the target hypervisor. Hypervisor
specific information for this attributes can be found in the drivers
configuration guides:

-  `Xen Adaptor <http://www.opennebula.org/documentation:rel2.0:xeng>`__
-  `KVM Adaptor <http://www.opennebula.org/documentation:rel2.0:kvmg>`__
-  `VMware
   Adaptor <http://www.opennebula.org/documentation:rel2.0:vmwareg>`__

OpenNebula has been designed to be easily extended, so any attribute
name can be defined for later use in any OpenNebula module. There are
some pre-defined attributes, though.

Please check the `Virtual Machine definition
file <http://www.opennebula.org/documentation:rel2.0:template>`__
reference for details on all the sections.

A basic VM template to be run using KVM could be this:
 

::

    #---------------------------------------
    # VM definition example
    #---------------------------------------

    NAME = "ttylinux"

    CPU    = 0.5
    MEMORY = 64

    # --- disks ---

    DISK = [
      source   = "/srv/cloud/images/ttylinux/ttylinux.img",
      target   = "hda",
      readonly = "no" ]

    # --- 1 NIC ---

    NIC = [ NETWORK="Red LAN"]

    FEATURES=[ acpi="no" ]

    # --- VNC server ---

    GRAPHICS = [
      type    = "vnc",
      listen  = "127.0.0.1"]

In the previous template KVM will asume that the image is RAW. If you
have a image with the qcow2 format, you have to add the following to the
DISK description:       

::

    driver = "qcow2"     

Assuming we have a VM template called "ttylinux.one" describing a
virtual machine. Then, we can allocate the VM in OpenNebula issuing a:

.. code:: xterm

    $ onevm create ttylinux.one

afterwards, the VM can be listed with the ``list`` option:

.. code:: xterm

    $ onevm list
       ID     USER     NAME STAT CPU     MEM        HOSTNAME        TIME
       45   oneadmin ttylinux runn   0     64M     192.168.1.5 00 05:19:31

Managing the Image Repository
=============================

The Image Repository system allows OpenNebula administrators and users
to set up images, which can be operative systems or data, to be used in
Virtual Machines easily. These images can be used by several Virtual
Machines simultaneously, and also shared with other users.

Create an OS Image
~~~~~~~~~~~~~~~~~~

This is what a sample template looks like:

.. code:: xterm

    $ cat ubuntu.one.img
    NAME          = "Ubuntu Desktop"
    PATH          = /home/cloud/images/ubuntu-desktop/disk.0
    PUBLIC        = YES
    DESCRIPTION   = "Ubuntu 10.04 desktop for students."

To submit the template, you have to issue the command

.. code:: xterm

    $ oneimage register ubuntu_img.one  

You can use the ``oneimage list`` command to check the available images
in the repository.

.. code:: xterm

    $ oneimage list
      ID     USER                 NAME TYPE              REGTIME PUB PER STAT  #VMS
       1   carlos       Ubuntu Desktop   OS   Jul 11, 2010 15:17 Yes  No  rdy     0

There other commands to manage the images sotored in the Image
Repository:

-  Use the ``oneimage publish`` and ``oneimage unpublish`` commands to
   make your images public for every user to use in their virtual
   machines, or private.
-  Use the ``oneimage persistent`` and ``oneimage nonpersistent``
   commands to make your images persistent (they are not cloned, but
   rather used from the original image) or not. A persistent image
   cannot be published.

Using an Image Stored in the Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The only difference with the previous VM template is that now, you only
need to specify the name of the image that you want to use in the DISK
section.

.. code:: code

    CPU    = 1
    MEMORY = 512

    DISK = [ image     = "Ubuntu Desktop" ]

    NIC    = [ NETWORK = "Public network" ]
    NIC    = [ NETWORK = "Private network" ]

    # FEATURES=[ acpi="no" ]

    GRAPHICS = [ 
      type    = "vnc",              
      listen  = "1.2.3.4",
      port    = "5902"  ]

Assuming that the template containing the previous information is called
template.one, you can deploy the VM using the command:

.. code:: xterm

    onevm create template.one

Save Changes
~~~~~~~~~~~~

Once the VM is deployed you can save the changes made to any disk as a
new image. To do so, use the ``onevm saveas`` command. This command
takes three or four arguments: The VM name (or ID), the disk\_id to
save, the name of the new image to register, and optionally the image
type.

To know the DISK\_ID of the disk you want to save, just take a look at
the ``onevm show`` output for your VM.

The DISK\_IDs are assigned in the same order the disks were defined in
the `VM
template <http://www.opennebula.org/documentation:rel2.0:template>`__.

.. code:: xterm

    $ onevm saveas one-5 0 "Ubuntu with Apache and MySQL"

This will register a new image called “Ubuntu with Apache and MySQL”,
that will be ready as soon as the VM is shut down.

The disks can be saved even if they were defined from a local disk file
(see the `VM
template <http://www.opennebula.org/documentation:rel2.0:template>`__
reference guide for more information on the different kinds of disks).

 

Managing Physical Hosts and Clusters
====================================

(`http://www.opennebula.org/documentation:rel2.0:cluster\_guide <http://www.opennebula.org/documentation:rel2.0:cluster_guide>`__)

In order to use your existing physical nodes, you have to add them to
the system as OpenNebula hosts. You need the following information:

-  *Hostname* of the cluster node or IP
-  *Information Driver* to be used to monitor the host, e.g. ``im_kvm``.
-  *Storage Driver* to clone, delete, move or copy images into the host,
   e.g. ``tm_nfs``.
-  *Virtualization Driver* to boot, stop, resume or migrate VMs in the
   host, e.g. ``vmm_kvm``.

|:!:| Before adding a host check that you can ssh to it without being
prompt for a password

Managing Hosts
--------------

Hosts can be added to the system anytime with the ``onehost`` command.
You can add the cluster nodes to be used by OpenNebula.

This is two example of adding a KVM host.

.. code:: xterm

    $ onehost create host01 im_kvm vmm_kvm tm_nfs

    $ onehost create 192.168.1.5 im_kvm vmm_kvm tm_nfs

This is an example of adding a XEN host.

.. code:: xterm

    $ onehost create host02 im_xen vmm_xen tm_nfs

Note that in the two previous examples we are using tm\_nfs. This means
that OpenNebula is configured to share the VM directory or to use SSH
with no share directory. Other option is the use of LVM. More
information about the diferent storage system supported can be found in
`http://www.opennebula.org/documentation:rel2.0:sm <http://www.opennebula.org/documentation:rel2.0:sm>`__

The status of the cluster can be checked with the ``onehost list``
command:

.. code:: xterm

    $ onehost list
      ID NAME                      CLUSTER                   RVM   TCPU   FCPU   ACPU    TMEM    FMEM STAT
       0 host01                    default                     2    100     90     90  523264  205824   on
       2 host02                    default                     0    100     99     99  523264  264192  off
       3 192.168.1.5               default                     1    400    400    350    7.7G    7.5G   on

And specific information about a host with ``show``:

.. code:: xterm

    $ onehost show 3
    HOST 3 INFORMATION                                                              
    ID                    : 3                   
    NAME                  : 192.168.1.5         
    CLUSTER               : default             
    STATE                 : MONITORED           
    IM_MAD                : im_kvm              
    VM_MAD                : vmm_kvm             
    TM_MAD                : tm_nfs              

    HOST SHARES                                                                     
    MAX MEM               : 8043848             
    USED MEM (REAL)       : 821384              
    USED MEM (ALLOCATED)  : 65536               
    MAX CPU               : 400                 
    USED CPU (REAL)       : 0                   
    USED CPU (ALLOCATED)  : 50                  
    RUNNING VMS           : 1                   

    MONITORING INFORMATION                                                          
    ARCH=x86_64
    CPUSPEED=2000
    FREECPU=400.0
    FREEMEMORY=7819560
    HOSTNAME=fg-gravel5.futuregrid.iu.edu
    HYPERVISOR=kvm
    MODELNAME=Intel(R) Core(TM)2 Quad CPU Q9550 @ 2.83GHz
    NETRX=144207042
    NETTX=23584321
    TOTALCPU=400
    TOTALMEMORY=8043848
    USEDCPU=0.0
    USEDMEMORY=821384

If you want not to use a given host you can temporarily disable it:

 

.. code:: xterm

    $ onehost disable host01

A disabled host should be listed with ``STAT off`` by ``onehost list``.
You can also remove a host permanently with:

 

.. code:: xterm

    $ onehost delete host01

 

|:!:| Detailed information of the ``onehost`` utility can be found `in
the Command Line
Reference <http://www.opennebula.org/documentation:rel2.0:cli#onehost>`__

 

If you use the ``onecluster list`` command you will see that the
“default” cluster is created automatically.

.. code:: xterm

    $ onecluster list
      ID     NAME
       0  default

    $ onehost list
      ID NAME                      CLUSTER                   RVM   TCPU   FCPU   ACPU    TMEM    FMEM STAT
       0 ursa                      default                     0      0      0    100       0       0   on
       1 ursa01                    default                     0      0      0    100       0       0   on
       2 ursa02                    default                     0      0      0    100       0       0   on
       3 ursa03                    default                     0      0      0    100       0       0   on
       4 ursa04                    default                     0      0      0    100       0       0   on

You may want to isolate your physical hosts running virtual machines
containing important services for you business, from the virtual
machines running a development version of your software. The OpenNebula
administrator can do so with these commands:

 

.. code:: xterm

    $ onecluster create testing
    $ onecluster create production

    $ onecluster addhost ursa01 production
    $ onecluster addhost ursa03 testing
    $ onecluster addhost ursa04 testing

    $ onehost list
      ID NAME                      CLUSTER                   RVM   TCPU   FCPU   ACPU    TMEM    FMEM STAT
       0 ursa                      default                     0      0      0    100       0       0   on
       1 ursa01                    production                  0      0      0    100       0       0   on
       2 ursa02                    default                     0      0      0    100       0       0   on
       3 ursa03                    testing                     0      0      0    100       0       0   on
       4 ursa04                    testing                     0      0      0    100       0       0   on

From this point, the newly created machines can use this cluster names
as a `placement
requirement <http://www.opennebula.org/documentation:rel2.0:template#placement_section>`__:

 

.. code:: xterm

    REQUIREMENTS = "CLUSTER = \"testing\""

Once your development cycle is finished, this “testing” and “production”
clusters may not be useful any more. Let's delete the testing cluster.

 

.. code:: xterm

    $ onecluster delete testing
    $ onehost list
      ID NAME                      CLUSTER                   RVM   TCPU   FCPU   ACPU    TMEM    FMEM STAT
       0 ursa                      default                     0      0      0    100       0       0   on
       1 ursa01                    production                  0      0      0    100       0       0   on
       2 ursa02                    default                     0      0      0    100       0       0   on
       3 ursa03                    default                     0      0      0    100       0       0   on
       4 ursa04                    default                     0      0      0    100       0       0   on

As you can see, the hosts assigned to the “testing” cluster have been
moved to the “default” one.

|:!:| Detailed information of the ``onecluster`` utility can be found in
the `Command Line
Reference <http://www.opennebula.org/documentation:rel2.0:cli#onecluster>`__

 

 

Managing Virtual Networks
=========================

`( <http://www.opennebula.org/documentation:rel2.0:vgg>`__\ `http://www.opennebula.org/documentation:rel2.0:vgg <http://www.opennebula.org/documentation:rel2.0:vgg>`__)

A cluster node is connected to one or more networks that are available
to the virtual machines through the corresponding bridges. To set up a
virtual networks you just need to know the name of the bridge to bind
the virtual machines to.

Defining a Virtual Network
--------------------------

OpenNebula allows for the creation of Virtual Networks by mapping them
on top of the physical ones. All Virtual Networks are going to share a
default value for the MAC preffix, set in the ``oned.conf`` file.

There are two types of Virtual Networks in OpenNebula:

#. **Fixed**, defines a fixed set of IP-MAC pair addresses
#. **Ranged**, defines a class network.

|:!:| Virtual Networks created by ``oneadmin`` can be used by every
other user.

 

Fixed Virtual Network
~~~~~~~~~~~~~~~~~~~~~

For example to create a Fixed Virtual Network, called ``Public`` with
the set of public IPs to be used by the VMs, just create a file with the
following contents:

.. code:: code

    NAME = "Public"
    TYPE = FIXED

    #We have to bind this network to ''virbr1'' for Internet Access
    BRIDGE = vbr1

    LEASES = [IP=130.10.0.1, MAC=50:20:20:20:20:20]
    LEASES = [IP=130.10.0.2, MAC=50:20:20:20:20:21]
    LEASES = [IP=130.10.0.3]
    LEASES = [IP=130.10.0.4]

where **LEASES**: Definition of the IP-MAC pairs. If an IP is defined,
and there is no associated MAC, OpenNebula will generate it using the
following rule: ``MAC = MAC_PREFFIX:IP``. So, for example, from IP
10.0.0.1 and MAC\_PREFFIX 00:16, we get 00:16:0a:00:00:01. Defining only
a MAC address with no associated IP is not allowed.

 

Ranged Virtual Network
~~~~~~~~~~~~~~~~~~~~~~

The following is an example of a Ranged Virtual Network template:

.. code:: code

    NAME = "Red LAN"
    TYPE = RANGED

    # This vnet can be only used by the owner user
    PUBLIC = NO

    #Now we'll use the cluster private network (physical)
    BRIDGE = vbr0

    NETWORK_SIZE    = C
    NETWORK_ADDRESS = 192.168.0.0

where:

-  **NETWORK\_ADDRESS**: Base network address to generate IP addresses.
-  **NETWORK\_SIZE**: Number of hosts that can be connected using this
   network. It can be defined either using a number or a network class
   (B or C).

Adding and Deleting Virtual Networks
------------------------------------

Once a template for a VN has been defined, the ``onevnet`` command can
be used to create it.

To create the previous networks put their definitions in two different
files, ``public.net`` and ``red.net``, respectively. Then, execute:

.. code:: xterm

    $ onevnet -v create public.net
    $ onevnet -v create red.net

Also, ``onevnet`` can be used to query OpenNebula about available VNs:

.. code:: xterm

    $ onevnet list
      ID USER     NAME              TYPE BRIDGE P #LEASES
       2 oneadmin Public           Fixed   vbr1 Y       0
       3 oneadmin Red LAN         Ranged   vbr0 N       0

with ``USER`` the owner of the network and ``#LEASES`` the number of
IP-MACs assigned to a VM from this network.

We can see the details of a particular VN:

::

    $onevnet show 0

    VIRTUAL NETWORK 0 INFORMATION                                                   
    ID:       : 0                   
    UID:      : 0                   
    PUBLIC    : N                   

    VIRTUAL NETWORK TEMPLATE                                                        
    BRIDGE=br1
    LEASES=[ IP=192.168.1.7 ]
    LEASES=[ IP=192.168.1.8 ]
    LEASES=[ IP=192.168.1.9 ]
    LEASES=[ IP=192.168.1.10 ]
    NAME=Small LAN
    TYPE=FIXED

    LEASES INFORMATION                                                              
    LEASE=[ IP=192.168.1.7, MAC=02:00:c0:a8:01:07, USED=1, VID=54 ]
    LEASE=[ IP=192.168.1.8, MAC=02:00:c0:a8:01:08, USED=1, VID=45 ]
    LEASE=[ IP=192.168.1.9, MAC=02:00:c0:a8:01:09, USED=0, VID=-1 ]
    LEASE=[ IP=192.168.1.10, MAC=02:00:c0:a8:01:0a, USED=0, VID=-1 ]

To delete a virtual network just use ``onevnet delete``. For example to
delete the previous networks:

.. code:: xterm

    $onevnet delete 2
    $onevnet delete 'Red LAN'

|:!:| Check the ``onevnet`` command help or `reference
guide <http://www.opennebula.org/documentation:rel2.0:cli#onevnet>`__
for more options to list the virtual networks.

Using the Leases Within the Virtual Machine
-------------------------------------------

Hypervisors can attach a specific MAC address to a virtual network
interface, but Virtual Machines need to obtain an IP address. There are
a variety of ways to achieve this within OpenNebula:

-  Obtain the IP from the MAC address, using the default MAC assignment
   schema (**PREFERRED**)

-  Use the ``CONTEXT`` attribute, check the `Contextualization
   Guide <http://www.opennebula.org/documentation:rel2.0:cong>`__

Configuring the Virtual Machine to Use the Leases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please visit the `contextualization
guide <http://www.opennebula.org/documentation:rel2.0:cong>`__ to learn
how to configure your Virtual Machines.

Accounting
==========

(`http://opennebula.org/documentation:rel2.0:accounting <http://opennebula.org/documentation:rel2.0:accounting>`__)

Physical Resources
------------------

Usage of a physical resource can be obtained for a given user or a given
virtual machine. Accounting reports always show aggregated information,
considering possible migration of a virtual machine to between physical
resources.

``oneacct host`` - prints accounting information for the physical
resources

Obtaining the accounting information for user john

.. code:: xterm

    $ oneacct host -u john
        HOST       XFR      RUNN  VMS
         sun  00:00:05  00:18:40    2
       rigil  00:00:05  00:00:02    1
     schedar  00:00:02 198:17:53    1

The columns are:

-  XFR: Total transfer time. It includes cloning VM disk images in the
   target resource and transfer back of modified images when applicable
-  RUNN: Total running time. It includes boot, running and saving times
-  VMS: Total number of virtual machines

Obtaining accounting information for host

.. code:: xterm

    $ oneacct host -r rigil
        USER       XFR      RUNN  VMS
       admin  00:00:05  00:00:02    1
        hugo  00:00:02 194:25:30    1

  Virtual Resources
-------------------

Accounting information for Virtual Machines can be obtained for a given
user or a given virtual machine.

The current version of the virtual resources reports does not consider
possible migration of a virtual machine to between physical resources.

``oneacct vm`` - prints accounting information for virtual machines

Obtaining the accounting information for a given VM

.. code:: xterm

    $ oneacct vm 2
        HOST       XFR      RUNN
         sun  00:00:01  00:00:21
     schedar  00:00:02 198:17:53

The columns are:

-  HOST: where the VM has been executed
-  XFR: Total transfer time in that host
-  RUNN: Total running time in the host

Obtaining the accounting information for a given host

.. code:: xterm

    $ oneacct vm -r rigil
    VMID     NAME       XFR      RUNN
       5      xee         2 194:25:30
       6      phi         5  00:00:02

Obtaining the accounting information for a given user

.. code:: xterm

    $ oneacct vm -u carroll
    VMID     NAME       XFR      RUNN    HOSTS
       3 Ubuntu-9  00:00:01  00:02:54        3
       4 Ubuntu-9  00:00:00  00:00:10        2

In this last example columns show aggregated transfer and running times.

 

User Management
===============

(`http://www.opennebula.org/documentation:rel2.0:users) <http://www.opennebula.org/documentation:rel2.0:users>`__

Adding New Users
----------------

Current Authentication/Authorization module (from now on auth module)
has support for user/password and rsa private/public key authentication
and also user quota support. Here, we are going to talk about the SSH
module and how to add users using SSH keys. More information can be
found in the official documentation:
`http://www.opennebula.org/documentation:rel2.0:users <http://www.opennebula.org/documentation:rel2.0:users>`__

Public Key Extraction (Done by Users)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a user compatible with ``ssh`` option for authentication the
administrator needs to add the user's public key into the database. The
file with public key generated by ``ssh-keygen``
(``$HOME/.ssh/id_rsa.pub``) is written in a format readable by
``openssl`` so the public key should be extracted by the user and sent
to the administrator. The way to extract it is the following:

.. code:: code

    $ oneauth key
    Enter PEM pass phrase:
    MIIBCAKCAQEApUO+JISjSf02rFVtDr1yar/34EoUoVETx0n+RqWNav+5wi+gHiPp3e03AfEkXzjDYi8F
    voS4a4456f1OUQlQddfyPECn59OeX8Zu4DH3gp1VUuDeeE8WJWyAzdK5hg6F+RdyP1pT26mnyunZB8Xd
    bll8seoIAQiOS6tlVfA8FrtwLGmdEETfttS9ukyGxw5vdTplse/fcam+r9AXBR06zjc77x+DbRFbXcgI
    1XIdpVrjCFL0fdN53L0aU7kTE9VNEXRxK8sPv1Nfx+FQWpX/HtH8ICs5WREsZGmXPAO/IkrSpMVg5taS
    jie9JAQOMesjFIwgTWBUh6cNXuYsQ/5wIwIBIw

The string the user has to send to the administrator to create the user
is written to the console.

User Creation (done by the administrator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the user sends the rsa public key the administration needs to
create a new account in OpenNebula system. This is done in a similar way
as standard user/password users but using the public key provided by the
user and adding a parameter to the command so the password (in this case
the public key) is stored as is in the database. Here is the command to
create a user called ``test`` with the previously extracted public key:

.. code:: code

    $ oneuser create -n test "MIIBCAKCAQEApUO+JISjSf02rFVtDr1yar/34EoUoVETx0n+RqWNav+5wi+gHiPp3e03AfEkXzjDYi8F
    voS4a4456f1OUQlQddfyPECn59OeX8Zu4DH3gp1VUuDeeE8WJWyAzdK5hg6F+RdyP1pT26mnyunZB8Xd
    bll8seoIAQiOS6tlVfA8FrtwLGmdEETfttS9ukyGxw5vdTplse/fcam+r9AXBR06zjc77x+DbRFbXcgI
    1XIdpVrjCFL0fdN53L0aU7kTE9VNEXRxK8sPv1Nfx+FQWpX/HtH8ICs5WREsZGmXPAO/IkrSpMVg5taS
    jie9JAQOMesjFIwgTWBUh6cNXuYsQ/5wIwIBIw"

After this the administrator can check that the user is in the system:

.. code:: code

    $ oneuser list
      ID USER            PASSWORD                                          
       0 oneadmin        5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8          
       1 test            MIIBCAKCAQEApUO+JISjSf02rFVtDr1yar/34EoUoVETx0n+Rq

User Login (Done by Users)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Before performing any action in OpenNebula system the user needs to
login. To do this we must issue this command:

.. code:: code

    $ oneauth login test
    Enter PEM pass phrase:
    export ONE_AUTH=/home/test/.one/one_ssh

The command on success will print the command needed to execute so
OpenNebula knows where to find the login file generated.

.. code:: code

    $ export ONE_AUTH=/home/test/.one/one_ssh

This line can also be added by the user to $HOME/.profile or
$HOME/.bashrc so it is not needed to be executed every new system login.

By default the login file will be valid for one hour. This expire time
can be changed adding another parameter with the number of seconds you
want the login to be valid. For example to create a 2 hours valid login
you can issue this command:

.. code:: code

    $ oneauth login test 7200
    Enter PEM pass phrase:
    export ONE_AUTH=/home/test/.one/one_ssh

 

Quota
-----

When quota module is enabled it checks for user resource consumption
before letting a VM to created in OpenNebula system. You have to take
into account that all resources for VMs listed by ``onevm list`` for a
user are counted as used. Administrator user has unlimited quota.

Quotas Database Security (Done by the Administrator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default user quota database is an *sqlite* database located at
``$ONE_LOCATION/var/auth.db``. This database on creation does not have
secure permissions and the administrator may change its permission and
maybe its location. To change its location you can use a full path to
the database in the auth module configuration file:

.. code:: code

    :database: sqlite:///somewhere/in/your/hdd/auth.db
    ...

You may also change its permissions to ``0600`` so the unix user that
runs OpenNebula daemons is the only with read/write access permissions.

Default Quotas (Done by the Administrator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default quotas for all users are configured as previously stated in
*Configuring and Enabling Auth Module*. This is the first configuration
you will have to do if you enable quota system as any user without
explicit quotas can only use that amount of resources.

Explicit User Quotas (Done by the Administrator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting special quotas for a user can be done using ``oneauth`` command.
If you have secured the database only unix user that runs OpenNebula
will be able to update them. The steps to change permissions for a user
are as follows:

-  Find the user id for the user we want to change limits. We are
   searching for user ``test``:

.. code:: code

    $ oneuser list
      ID USER            PASSWORD                                          
       0 oneadmin        5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8          
       1 test            MIIBCAKCAQEApUO+JISjSf02rFVtDr1yar/34EoUoVETx0n+Rq

-  The user id for ``test`` is 1. Now we use
   ``oneauth quota set <user id> <cpu> <memory>`` to change user limits:

.. code:: code

    $ oneauth quota set 1 20 10000000

 
