**********************************************************************
Converting Virtualbox images to OpenStack
**********************************************************************

In this tutorial we explain how to convert a Virtual Box image to kvm
format and then register it on OpenStack.

Prerequisites
-------------

There is two main prerequisites for your images to work with OpenStack

Disable SELinux (Only for RedHat-based Linux like CentOS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the file /etc/selinux/config and set the SELINUX option to disabled::

    SELINUX=disabled

Configuring the image network interface (eth0) for DHCP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Ubuntu, you edit the file /etc/network/interfaces and configure eth0
to::

    auto eth0
    iface eth0 inet dhcp

In CentOS, you edit the file /etc/sysconfig/network-scripts/ifcfg-eth0
and make sure it contains::

    DEVICE=eth0
    BOOTPROTO=dhcp
    ONBOOT=yes

Configure the image to allow OpenStack to inject the ssh key 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Ubuntu (it may not be needed for Ubuntu, but it is recomended)

.. code:: rteindent2

    $ sudo apt-get install cloud-init curl

-  CentOS. Edit the file /etc/rc.local

.. code:: rteindent2

    route del -net 169.254.0.0 netmask 255.255.0.0 dev eth0
    # load pci hotplug for dynamic disk attach in KVM (for EBS)
    depmod -a
    modprobe acpiphp

    # simple attempt to get the user ssh key using the meta-data service
    mkdir -p /root/.ssh
    echo >> /root/.ssh/authorized_keys
    curl -m 10 -s http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key | grep 'ssh-rsa' >> /root/.ssh/authorized_keys
    echo "AUTHORIZED_KEYS:"
    echo "************************"
    cat /root/.ssh/authorized_keys
    echo "************************"

Configure udev persistent rules (only CentOS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the file /etc/udev/rules.d/70-persistent-net.rules, delete
everything and add::

    ACTION=="add",SUBSYSTEM=="net", IMPORT{program}="/lib/udev/rename_device"
    SUBSYSTEM=="net", RUN+="/etc/sysconfig/network-scripts/net.hotplug"

Convert your virtual box image to raw format
--------------------------------------------

::

    VBoxManage clonehd /path/to/imagefile/vboximage.vdi /path/to/rawimage.img --format raw

Make sure that you specify the full path. Otherwise, you may experience
errors and the new image will be placed in  ~/.VirtualBox/HardDisks/

Convert the image to qcow2 format (optional)
--------------------------------------------

This step is optional, but it is recommended if your image as a
considerable size because the qcow2 format will compress your image.
Nevertheless, it will takes a while to finish this command. As example
my 8GB image took a couple of hours to get ready and was compressed to
less than 6 GB::

    qemu-img convert -f raw rawimage.img -O qcow2 qcow2image.img

Test your image
---------------

If you are in a computer with graphical interface, the easiest way to
test it is by executing the following command. This command will open a
window and you will see if your image boots correctly::

    kvm -hda rawimage.img -m 1024

or::

    kvm -hda qcow2image.img -m 1024

From now on, we refer only to the rawimage.img, but it works in the same
way with the qcow2image.img.

Transfer your Image to India
----------------------------

::

    $ scp rawimage.img <username>@india.futuregrid.org:/N/u/<username>/

Log into India
--------------

::

    $ ssh <username>@india.futuregrid.org

::

Upload your image to OpenStack
------------------------------

First, we need to load the euca2ools module that contains the command
line interface to interact with OpenStack. Then we need to load our own
credentials that are typically in a novarc file. Finally you update and
register the image. Although, we are going to briefly explain these
steps here, this is part of the OpenStack tutorial that can be found
in \ `https://portal.futuregrid.org/tutorials/openstack <https://portal.futuregrid.org/tutorials/openstack>`__::

    $ module load euca2ools
    $ source ~/novarc

Upload the image::

    $ euca-bundle-image -i rawimage.img 

    Checking image
    Encrypting image
    Splitting image...
    Part: rawimage.img.part.00
    Part: rawimage.img.part.01
    Part: rawimage.img.part.02
    .....
    Generating manifest /tmp/rawimage.img.manifest.xml

At the end you get a manifest file that you use in the next step. You
also need to specify a bucket name (option -b). We can use our username
(jdiazz in my case), but it can be any other string::

    $ euca-upload-image -m /tmp/rawimage.img.manifest.xml -b jdiazz

    Checking bucket: jdiaz
    Uploading manifest file
    Uploading part: rawimage.img.part.00
    Uploading part: rawimage.img.part.01
    Uploading part: rawimage.img.part.02
    .....
    Uploaded image as jdiazz/rawimage.img.manifest.xml

Finally we register the image::

    $ euca-register jdiazz/rawimage.img.manifest.xml

    IMAGE ami-00000058

From this last command we get the ami-ID that identifies the image in
OpenStack (marked in yellow). You will need this to start instances.

Checking Status Image
---------------------

You cannot run instances until your image is in available status. You
can check the status of your image with the euca-describe-images
command. This command can take some time to respond because the system
will be busy processing your image::

    $ euca-describe-images ami-00000058

Test Image in OpenStack
-----------------------

For this step we recomend to go to the OpenStack tutorial where we
explain how to create a key-pair and run an instance with our image.
Please
see \ `https://portal.futuregrid.org/using-openstack-futuregrid#key\_management <https://portal.futuregrid.org/using-openstack-futuregrid#key_management>`__

Running the instance can be something like this::

    $ euca-run-instances -k jdiaznova ami-00000058 -t m1.large

where jdiaznova is the key name of my openstack key pairs. This key will
allow us to ssh into the image. Please refer to the OpenStack tutorial
for more information.

Troubleshooting
---------------

One problem of this way of using our images is that we cannot use
euca-get-console-output command to debug the boot process of the images.
Therefore it makes more complicated solving runtime problems. However,
if your image boots properly when doing the "Test your Image" section,
it should work also on OpenStack and the only problem could be wrong
configuration of network interface or SELinux enabled.

Notes:
------

This tutorial has been tested with Ubuntu 12 and CentOS 6 using
OpenStack Essex. 

`‹ One-click Twister K-means on Eucalyptus
FutureGrid </tutorials/one-click-twister-k-means-eucalyptus-futuregrid>`__
`up </tutorials>`__ `Virtual Appliances › </community/appliances>`__
