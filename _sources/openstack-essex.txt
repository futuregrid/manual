
Using OpenStack on FutureGrid
=============================

NOTE: 
======

-  **This tutorial contains material that is customized for the
   particular user. The best way to view this tutorial is to  ask for a
   FutureGrid portal account and to log into the portal. You will also
   need to be in a valid FG project to execute the directions.**

Summary
=======

We currently have twenty nodes in the FG India cluster dedicated to the
`Essex <http://www.openstack.org/software/essex/>`__ release of
`OpenStack <http://www.openstack.org>`__, a collection of open-source
technology that provides scalable, open-source cloud computing software.
OpenStack consists of a series of `interrelated
projects <http://www.openstack.org/software/>`__ that deliver various
components for a cloud infrastructure solution. This tutorial provides
an overview of OpenStack Nova installation on FutureGrid, as well as
steps for deploying virtual machines.

Getting Started
===============

Be sure you have a valid portal account
(`https://portal.futuregrid.org) <https://portal.futuregrid.org>`__ and
are part of a valid FG project. If you're not part of any project, you
can either create a new one (it will need approval) or join an existing
one with the permission of the Lead.

Once the previous requirements are fulfilled, your OpenStack account is
automatically created.

Log into India
==============

+-------------------------------------------------------------------------------------------------------------------------+
 Tip: to login into FutureGrid \ `see this page <https://portal.futuregrid.org/accessing-futuregrid-resources-ssh>`__   |
+-------------------------------------------------------------------------------------------------------------------------+

The first step is to ssh into india.futuregrid.org using your FG
username:

::

    $ ssh gvonlasz@india.futuregrid.org

If this command fails,
contact \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__. 
It likely means one of the following:

#. Your account is not yet set up.

#. You provided no public key, or a corrupted public key.

#. The private key you are using does not match the public key you
   registered with FutureGrid.

Account and Credentials
=======================

As noted above, OpenStack credentials and configuration files are
automatically created for all valid users, and are placed in your home
directory on the India system under the ***.futuregrid/openstack***
folder. The file name is called
***openstack-essex-<username>-india.zip***. The credential .zip file
contains the user keys and novarc file. The novarc file contains the
necessary environment variables.

Unzip the credential file:

::

    $ unzip ~/.futuregrid/openstack/openstack-essex-gvonlasz-india.zip -d ~/openstack

Load Environment variables:

::

    $ source ~/openstack/novarc

**Note:** As both Eucalyptus and OpenStack use the same EC2
environmental variables (i.e. EC2\_URL, EC2\_ACCESS), using novarc will
overwrite previous Eucalyptus credentials. If you have the eucarc file
in your home directory, doing a *source eucarc* will bring back those
variables and overwrite the OpenStack ones. In this way, you can go back
and forth with OpenStack and Eucalyptus.

Euca2ools (EC2 client tools)
============================

OpenStack services can be controlled using an EC2 interface (only
available for GNU/Linux platforms). In this tutorial, we are going to
use the \ `Euca2ools <http://www.eucalyptus.com/download/euca2ools>`__
client installed in India.

::

    $ module load euca2ools

Testing Your Setup
==================

Use euca-describe-availability-zones to test the setup:

::

    $ euca-describe-availability-zones 

    AVAILABILITYZONE    india   available

List of Common Images
=====================

Following are the current images uploaded in essex:

::

    $ euca-describe-images |grep common

    IMAGE   ami-000000b4   common/precise-server-cloudimg-amd64.img.manifest.xml   available   private   x86_64   machine   aki-000000b3   instance-store

VM Types
========

The following types of VM are available:

$ nova flavor-list

| +----+-------------+-----------+------+-----------+------+-------+-------------+-----------+-------------+
|  \| ID \| Name        \| Memory\_MB \| Disk \| Ephemeral \| Swap \|
VCPUs \| RXTX\_Factor \| Is\_Public \| extra\_specs \|
| 
+----+-------------+-----------+------+-----------+------+-------+-------------+-----------+-------------+
|  \| 1  \| m1.tiny     \| 512       \| 0    \| 0         \|      \|
1     \| 1.0         \| N/A       \| {}          \|
|  \| 2  \| m1.small    \| 2048      \| 10   \| 20        \|      \|
1     \| 1.0         \| N/A       \| {}          \|
|  \| 3  \| m1.medium   \| 4096      \| 10   \| 40        \|      \|
2     \| 1.0         \| N/A       \| {}          \|
|  \| 4  \| m1.large    \| 8192      \| 10   \| 80        \|      \|
4     \| 1.0         \| N/A       \| {}          \|
|  \| 5  \| m1.xlarge   \| 16384     \| 10   \| 160       \|      \|
8     \| 1.0         \| N/A       \| {}          \|
|  \| 6  \| m1.special1 \| 16384     \| 50   \| 1500      \|      \|
8     \| 1.0         \| N/A       \| {}          \|
| 
+----+-------------+-----------+------+-----------+------+-------+-------------+-----------+-------------+

Key Management
==============

Before you instantiate a VM, you need to create at least one key pair.
This key pair will be injected into the VM, allowing you to SSH into the
instance. This is done using the *euca-add-keypair* command:

::

    $ euca-add-keypair gvonlaszkey1 > gvonlaszkey1.pem

**Important Tip: **\ In case you execute this command twice this will
naturally not work in case the key is already added and imported. You
can check this by doing a cat on the .pem file and make sure that there
is a key in ther and not an error! If there is an error, you can either
delete the key and add it again, or you can create a new key name and
use that. Also if you have used that key before and you overwrote it you
will not have access to your images anymore. so be careful and before
issuing the above command think about what you do.

Fix the permissions on the generated private key:

::

    $ chmod 0600 gvonlaszkey1.pem

Note: Instead of creating a new keypair, you can import a public key
created with a third-party tool using *euca-import-keypair*. For
instance, if you have your ssh public key in india, you can do the
following:

::

    $ euca-import-keypair -f .ssh/id_rsa.pub gvonlaszkey2

You can add multiple keys, and here's the command to check the list of
your keys:

::

    $ chmod 0600 keyname.pem
    euca-describe-keypairs
    KEYPAIR    key1    53:e3:01:c1:70:df:94:ef:59:93:1a:3f:c0:10:a5:34
    KEYPAIR    key2    07:a5:da:30:b4:55:16:eb:35:54:a2:5a:56:68:f6:cb

::

Key pair verification
---------------------

Please verify that you do not have any error in the key file.

Image Instantiation
===================

At this point, you can start a VM using one of the pre-existing images.
You need the ami-id of the image you want to start. This was listed in
the output of the *euca-describe-images* command you saw earlier. Use
the *euca-run-instances* command to start the VM (use the key name you
specified before).

::

    $ euca-run-instances -k gvonlaszkey -n 1 ami-000000b4

    RESERVATION r-gbs9hpmm 461884eef90047fbb4eb9ec92f22a1e3 default
    INSTANCE i-00000a27 ami-000000b4 server-2599 server-2599 pending gvonlaszkey 0 m1.small 2012-07-31T14:54:40.000Z unknown zone

The output shows the id of your VM, which in this case is i-00000a27.

This id will be useful to do operations with your VM. You can also see
the status of your VM, which is pending now. You need to wait until the
VM is in running status to be able to log into the VM.

Better Server Names
===================

Unfortunately, the default use of the euca commands uses the name
server-<number> to identify a started instance. This is often not
desirable, as many users have similar names and it will be difficult to
find your own images when lots of users start images. To fix this, you
van however use the nova commands and say

$ nova rename Server-2599 <yourusername>-001

Monitoring Instances
====================

You can monitor the status of the instances by using the
*euca-describe-instances* command. The public IP is highligthed in
yellow; each VM should have one:

::

    $ euca-describe-instances

::

    RESERVATION r-xfj0nag8 461884eef90047fbb4eb9ec92f22a1e3 default
    INSTANCE i-0000090e ami-00000016 149.165.158.157 server-2318 running clegoues 0 m1.medium 2012-07-24T19:39:21.000Z india aki-00000014 ari-00000015

    RESERVATION r-8mwsq0n0 461884eef90047fbb4eb9ec92f22a1e3 default
    INSTANCE i-000008f2 ami-000000b4 149.165.158.130 server-2290 running clegoues 0 m1.medium 2012-07-24T02:19:38.000Z india aki-00000014 ari-00000015
    INSTANCE i-000008f3 ami-000000b4 149.165.158.149 server-2291 running clegoues 1 m1.medium 2012-07-24T02:19:38.000Z india aki-00000014 ari-00000015
    INSTANCE i-000008f4 ami-000000b4 149.165.158.156 server-2292 running clegoues 2 m1.medium 2012-07-24T02:19:39.000Z india aki-00000014 ari-00000015

    RESERVATION r-p90m3pno 461884eef90047fbb4eb9ec92f22a1e3 default
    INSTANCE i-000007e2 ami-000000b4 149.165.158.158 server-2018 running jiaazeng 0 m1.medium 2012-07-15T20:56:16.000Z india aki-00000026 
    INSTANCE i-000007e3 ami-000000b4 149.165.158.159 server-2019 running jiaazeng 1 m1.medium 2012-07-15T20:56:17.000Z india aki-00000026
    ...

You can monitor or restrict the output simply by checking the status of
your VM:

::

    $ euca-describe-instances i-00000a27

    RESERVATION r-zvtbbj8j default
    INSTANCE i-00000a27 ami-000000b4 server-1854 server-1854 pending gvonlaszkey 0 m1.small 2012-07-09T15:49:46.000Z  unknown zone aki-0000000e ari-0000000f

This VM does not have public IP yet. Getting the public IP may take some
time, but it is needed to be able to connect to the VM:

::

    $ euca-describe-instances i-00000a27

    RESERVATION r-zvtbbj8j default
    INSTANCE i-00000a27 ami-000000b4 149.165.158.175 server-1854 running gvonlaszkey 0 m1.small 2012-07-09T15:49:46.000Z  unknown zone aki-0000000e ari-0000000f

Log into your VM
================

The ssh private key that was generated earlier can now be used to log in
to the VM. You also need to indicate the public IP associated with your
VM (use the key name you have specified before).

::

    $ ssh -i gvonlaszkey.pem ubuntu@149.165.158.175

    $ ssh ubuntu@149.165.158.175 (for imported keys) 

Note: For some ubuntu images, log in with the user *ubuntu,* then
*sudo*.

Exit from the VM to continue with the tutorial.

::

    # exit

Making a snapshot with nova client
----------------------------------

You can make a snapshot of your instance:

::

    $ nova image-create <instance name> <snapshot name>
    $ euca-describe-images

Your snapshot will be listed at the end of the output, and it will be
available in 5 to 10 minutes. There's a bug that snapshots are created
as "snapshot" whatever you name it. So please remember the image ID.

Nova Volumes (Not available)
============================

Nova-volume provides persistent block storage compatible with Amazon’s
Elastic Block Store. The storage in the instances is non-persistent and
gets lost when the instance is terminated. Therefore, we need persistent
volumes to keep data generated during instance lifetime after the
instance is terminated. Volumes are accessed via iSCSI, although they
will appear as a new device in your VM.

List available Volumes
----------------------

You can see the available volumes by using the *euca-describe-volumes*
command:

::

    $  euca-describe-volumes

    VOLUME  vol-00000027  100  india  in-use  2012-06-06T21:39:47.000Z
               ATTACHMENT  vol-00000027  i-0000070f  /dev/vdc  attached 
    VOLUME  vol-00000028  50  india  available  2012-06-06T21:44:30.000Z
    VOLUME  vol-0000002a  30  india  available  2012-06-06T21:45:37.000Z

Create a Volume
---------------

Create a 1 GB volume in the India zone:

::

    $  euca-create-volume -s 1 -z india

    VOLUME  vol-00000031  1  india  creating  2012-07-10T15:15:47.244Z

Attach Volume
-------------

A volume can only be attached to one instance. Once the volume is
attached to a VM, *euca-describe-volumes* will show its status as
“attached”. 

Attach a volume to a running instance:

::

    $  euca-attach-volume -i i-00000a27 -d /dev/vdc vol-0000031

After this command is executed, an additional SCSI disk is created in
the instance. Although we specified the device, it may differ if that
device already exists (look into */dev* or */var/log/syslog* to find the
new device).

Using the new Disk
------------------

Log into the VM again (use the key name you specified before):

::

    $ ssh -i gvonlaszkey.pem ubuntu@149.165.158.175

Format the disk (skip this step if you want to reuse data stored):

::

    # mkfs /dev/vdc

Mount the disk:

::

    # mount /dev/vdc /mnt

You now have the new disk mounted in your system. In this way, you can
use it as a normal directory to store information. However, the
information stored there will be kept after you terminate the VM.

Exit from the VM to continue with the tutorial:

::

    # exit

Detach Volumes
--------------

Volumes are automatically detached when the instance is terminated.

To detach a volume:

::

    $  euca-detach-volume vol-00000031 

If you detach the volume while the instance is running, and with disk
mounted, it loses access to the disk. Thus, you need to make sure that
you umount (umount /mnt) the disk before you detach the volume. If you
terminate the instance, the volume is automatically detached.

Volume Snapshots
================

Snapshots are useful to create backups or replicate volumes in different
zones.

Create Snapshot
---------------

::

    $  euca-create-snapshot -d 'Testing snapshot' vol-00000027

    SNAPSHOT    snap-00000001    vol-00000027    creating    2012-07-16T14:22:21.728Z    0%    Testing snapshot

List Snapshot
-------------

::

    $  euca-describe-snapshots

    SNAPSHOT    snap-00000001    vol-00000027    available    2012-07-16T14:22:21.000Z    100%

Create Volume from Snapshot (not yet functional in OpenStack Essex)
-------------------------------------------------------------------

The snapshot must be in available status (100% completed). The new
volume can be bigger if desired, and you can also create this volume in
a different zone (*-z* option).

To create a 2 GB volume from snapshot:

::

    $  euca-create-volume -s 2 --snapshot snap-00000001 -z india

    VOLUME    vol-00000032    2    snap-00000001    india    creating    2012-07-16T14:47:07.916Z

Image Registration
==================

We will use an CentOS 5 image to test the image registration:

::

    $ wget i120/test-image/centos5.tgz

Uncompress and untar the archive:

::

    $ tar xvfz centos5.tgz

Bundle the image with a kernel and a ramdisk using the
*euca-bundle-image* command. In this example, we will use the KVM kernel
already registered. *euca-describe-images* returns the kernel and
ramdisk IDs that we need.

::

    $ euca-bundle-image -i centos5.img --kernel aki-0000000e --ramdisk ari-0000000f

::

    Checking image
    Encrypting image
    Splitting image...
    Part: centos5.img.part.00
    ...
    Part: centos5.img.part.35
    Generating manifest /tmp/centos5.img.manifest.xml

Use the generated manifest file to upload the image. You need to specify
a bucket name; it can be anything you want:

::

    $ euca-upload-bundle -b gvonlasz-bucket -m /tmp/centos5.img.manifest.xml

    Checking bucket: gvonlasz-bucket
    Creating bucket: gvonlasz-bucket
    Uploading manifest file
    Uploading part: centos5.img.part.00
    ...
    Uploading part: centos5.img.part.35

    Uploaded image as gvonlasz-bucket/centos5.img.manifest.xml

Register the upload image:

::

    $ euca-register gvonlasz-bucket/centos5.img.manifest.xml

    IMAGE  ami-00000033

The returned image ID can now be used to start instances
with\ *euca-run-instances* as described earlier. However, you cannot run
instances until the image is in available status. You can check the
status using \ *euca-describe-images*:

::

    $ euca-describe-instances ami00000033 IMAGE ami-00000033 gvonlasz-bucket/centos5.img.manifest.xml available private x86_64 machine aki-0000000e ari-0000000f instance-store

Delete your images
==================

::

    $ euca-deregister ami-00000033

Terminate your VMs
==================

::

    $ euca-terminate-instances i-00000a27

Limitations
===========

Our current installation has the following limitations. We are working
on finding a fix:

#. Instances cannot ping their own IP address from within the instance
   (it is pingable and reachable from the outside). The private IP
   (which can be found via ifconfig) is pingable.

   ubuntu@server-837:~$ ifconfig
    eth0      Link encap:Ethernet  HWaddr fa:16:3e:00:e5:2a 
              inet addr:10.1.2.16  Bcast:10.1.2.255 
   Mask:255.255.255.0
              inet6 addr: fe80::f816:3eff:fe00:e52a/64 Scope:Link
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:199 errors:0 dropped:0 overruns:0 frame:0
              TX packets:188 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000
              RX bytes:32213 (32.2 KB)  TX bytes:21676 (21.6 KB)

   lo        Link encap:Local Loopback 
              inet addr:127.0.0.1  Mask:255.0.0.0
              inet6 addr: ::1/128 Scope:Host
              UP LOOPBACK RUNNING  MTU:16436  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:0
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

#. In Essex, each instance gets an internal DNS name.
   *euca-describe-instance* will show this name along with the public IP
   addresses. If you are building a cluster and need to communicate
   among all the nodes in the cluster, you will need to do so with these
   names or the private IP addresses:

   ubuntu@server-837:~$ ping server-716
    PING server-716.novalocal (10.1.2.10) 56(84) bytes of data.
    64 bytes from server-716.novalocal (10.1.2.10): icmp\_req=1 ttl=64
   time=5.06 ms
    ^C
    --- server-716.novalocal ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 5.062/5.062/5.062/0.000 ms
    ubuntu@server-837:~$ ping server-837
    PING server-837.novalocal (127.0.1.1) 56(84) bytes of data.
    64 bytes from server-837.novalocal (127.0.1.1): icmp\_req=1 ttl=64
   time=0.032 ms
    64 bytes from server-837.novalocal (127.0.1.1): icmp\_req=2 ttl=64
   time=0.018 ms

Troubleshooting:
================

Console output will provide you more details about the VM:

::

    $ euca-get-console-output <instanceId>

For any other issue, please submit a ticket.

