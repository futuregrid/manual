.. _s-eucalyptus:

**********************************************************************
Eucalyptus
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

Eucalyptus is a software platform that implements
`IaaS-style <http://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_Service_.28IaaS.29>`__
cloud computing. Eucalyptus provides an Amazon Web Services
(`AWS <http://aws.amazon.com/>`__) compliant EC2 based web service
interface for interacting with the Cloud service. Additionally,
Eucalyptus provides services such as the AWS Compliant Walrus and a user
interface for managing users and images. The aim of this tutorial is to
give users an introduction of how to interact with Eucalyptus using the
Eucalyptus EC2 Interface
(`Euca2ools <https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#shared/euca2ools_section.html>`__). Complete 
documentation can be found at the `Eucalyptus
Website <https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#shared/index.html>`__. A detailed
user guide is available
`here <https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#shared/user_section.html>`__.

As of May 1, 2014, FutureGrid is using `Eucalyptus version 3.4
<https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#shared/index.html>`__
on sierra.futuregrid.org. This version of Eucalyptus requires
`euca2ools 3.0.2
<https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#shared/euca2ools_section.html>`__.
After logging in to sierra, make sure to load the euca2ools module::

    $ module load euca2ools

before using Eucalyptus. `euca2ools 3.0.2
<https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#shared/euca2ools_section.html>`__
is part of Eucalyptus installation packages for CentOS 6 and RHEL 6
described `here
<https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#install-guide/installing_euca_release.html>`__

Source code installation for other platforms is available `here
<http://downloads.eucalyptus.com/software/euca2ools/3.0/source/euca2ools-3.0.2.tar.gz>`__



Account Setup
--------------------

Eucalyptus 3.4 accounts are provisioned for all FutureGrid users with a
valid portal account and project affiliation. There is no need to apply
for Eucalyptus accounts separately.

Obtaining Credentials

-  Credentials files are created by default and placed in your home
   directory under *.futuregrid* folder on sierra.  There are separate
   credentials for each FutureGrid project. For instance, if you are
   part of FutureGrid project numbers 100 and 200, there will be two
   folders (fg100 and fg200) in *.futuregrid/eucalyptus*. Each project
   folder contains a corresponding credentials zip file. So
   fg100:username and fg200:username in Eucalyptus are two different
   identities, but they are tied to the same FutureGrid user.

-  Find your credential zip file in 
   $HOME/.futuregrid/eucalyptus/fgNNN::

       $ cd $HOME/.futuregrid/eucalyptus/fgNNN
       $ unzip euca34-{cluster}-fgNNN-{username}.zip  

-  Apply the eucarc file::

       $ source eucarc

-  If you want to add Eucalyptus environment variables to your .bashrc
   then, do this: (if you are planning to switch between different cloud
   platforms, it is probably better to use source::

           $ cat eucarc >> $HOME/.bashrc
           $ source $HOME/.bashrc



Resources Overview
----------------------

Eucalyptus is available to FutureGrid Users on the Sierra
cluster. As we will see later, when we instantiate a Virtual Machine
(VM) we must select the type of VM Image that we are going to
use. The VM Image types available are:

Sierra::

    INSTANCETYPE    Name         CPUs  Memory (MB)  Disk (GB)  Used / Total  Used %
    INSTANCETYPE    m1.small        1          256          5     1 /    24      4%
    INSTANCETYPE    t1.micro        1          256          5     1 /    24      4%
    INSTANCETYPE    m1.medium       1          512         10     1 /    12      8%
    INSTANCETYPE    c1.medium       2          512         10     1 /    12      8%
    INSTANCETYPE    m1.large        2          512         10     1 /    12      8%
    INSTANCETYPE    m1.xlarge       2         1024         10     1 /    12      8%
    INSTANCETYPE    c1.xlarge       2         2048         10     1 /    12      8%
    INSTANCETYPE    m2.xlarge       2         2048         10     1 /    12      8%


Testing Your Setup
----------------------

Use ``euca-describe-availability-zones`` to test the setup::

        $ ssh portalname@sierra.futuregrid.org
        Last login: Fri May 11 06:39:02 2012 from 129-79-49-230.dhcp-bl.indiana.edu

        Welcome to sierra.futuregrid.org

        torque/2.4.8 version 2.4.8 loaded
        moab version 5.4.0 loaded 
      
        
::
        
        $ module load euca2ools
        euca2ools version 3.0.2 loaded

::

        (euca2ools) $ euca-version
        euca2ools 3.0.2 (Sparta)

::

        (euca2ools) $ source .futuregrid/eucalyptus/fgNNN/eucarc
        (euca2ools) $ euca-describe-availability-zones
        AVAILABILITYZONE        euca34sierra    198.202.120.44 arn:euca:eucalyptus:euca34sierra:cluster:cc-s38/

Available Images
----------------------------------------------------------------------

List the existing images using ``euca-describe-images``. Remember you
must use the ``--all`` option to see public images that you don't
own::

        (euca2ools) $ euca-describe-images --all

        IMAGE   eki-19543879    fg-kernel/vmlinuz-3.13.0-29-generic.manifest.xml ...
        IMAGE   eki-7EA73854    fg-kernel/vmlinuz-2.6.32-431.17.1.el6.x86_64.manifest.xml ...
        IMAGE   emi-763C3C2D    fg-image/20140618-euca-centos-6_5.manifest.xml ...
        IMAGE   emi-F7473A3B    fg-image/20140616-euca-ubuntu-14_04.manifest.xml ...
        IMAGE   eri-13F63599    fg-ramdisk/initrd.img-3.13.0-29-generic.manifest.xml ...
        IMAGE   eri-1E5C3571    fg-ramdisk/initramfs-2.6.32-431.17.1.el6.x86_64.img.manifest.xml ...
        ...
        
Note, if you omit the --all option you will only see your images (not
other images, even if they are public). This differs from the behavior
of previous versions.
 
Currently the following machine images have been known to work

* emi-763C3C2D

  * OS: CentOS release 6.5
  * Flavors: m1.small
  * username: cloud-user

* emi-F7473A3B

  * OS: Ubuntu 14.04 LTS
  * Flavors: m1.small
  * username: ubuntu

Out of consideration for other users, please use the smallest "flavor" that meets your needs. Resources are limited.


Image Deployment
--------------------

Before running a VM instance, you need to create at least one key
pair. This key pair will be injected into the VM, allowing you to SSH
into the instance. This is done using the ``euca-add-keypair`` command::

    $ euca-add-keypair $USER-key   > $USER-key.pem

Fix the permissions on the generated private key::

    $ chmod 0600 $USER-key.pem 

When executing the ``euca-add-keypair`` command you may run into problems
if you reuse a key name.  To see if you have done this, please cat the
key with::

    $ cat $USER-key.pem

If you see a message that starts with::

    -----BEGIN RSA PRIVATE KEY-----

things should be fine. However, if you see::

    CreateKeyPairType: Keypair already exists: gvonlasz-key: Could not execute JDBC batch update

You have already created a keypair with that name in your project.
You can check if your key is already in the keypair list::

    $ euca-describe-keypairs

This will list all the keypairs in your project. If you need to create
a new key, you can delete the old one by::

    $ euca-delete-keypair $USER-key

After that you can create a new one as described above.

Now you can start a VM using one of the pre-existing images.  We have
provided images based on CentOS 6.5 and Ubuntu 14.04. You can find
these images with::

   $ euca-describe-images --all | fgrep fg-image

It will show you an id starting with the prefix "emi-".::

    IMAGE   emi-763C3C2D    fg-image/20140618-euca-centos-6_5.manifest.xml  663263781684    available       public  x86_64  machine eki-7EA73854       eri-1E5C3571            instance-store  paravirtualized
    IMAGE   emi-F7473A3B    fg-image/20140616-euca-ubuntu-14_04.manifest.xml        663263781684    available       public  x86_64  machine eki-19543879       eri-13F63599            instance-store  paravirtualized

Note that the image name is formatted with the date and linux
distribution name (centos or ubuntu) and version.  As we are
continually updating images as security updates are released, the
details in the examples here may differ from what you see.

We use the emi id in the next step. Use the ``euca-run-instances`` command
to start the VM::

    $ euca-run-instances -k $USER-key -n 1 -t m1.small emi-763C3C2D
    RESERVATION     r-F8BD3F92   597941386389    default
    INSTANCE        i-B2EF473E   emi-763C3C2D    0.0.0.0 0.0.0.0 pending $USER-key   0   m1.small   2014-06-23T18:53:09.216Z   euca34sierra   eki-7EA73854   eri-1E5C3571   monitoring-disabled   0.0.0.0 0.0.0.0   instance-store   paravirtualized

      
The initial state of the machine instance will be "pending" while it
is being provisioned and starting up. The ``euca-describe-instances``
command can be used to check the status of the request. The following
image was assigned an ip address and is starting up, as demonstrated
by the "pending" status::

  $ euca-describe-instances 

    RESERVATION     r-F8BD3F92   597941386389    default
    INSTANCE        i-B2EF473E   emi-763C3C2D    198.202.120.101 10.128.74.140   pending $USER-test-key   0   m1.small  2014-06-23T18:53:09.216Z euca34sierra    eki-7EA73854    eri-1E5C3571   monitoring-disabled  198.202.120.101 10.128.74.140   instance-store   paravirtualized

Once started, the status will change to "running"::

    $ euca-describe-instances

    RESERVATION     r-F8BD3F92   597941386389    default
    INSTANCE        i-B2EF473E   emi-763C3C2D    198.202.120.101 10.128.74.140   running $USER-test-key   0   m1.small  2014-06-23T18:53:09.216Z euca34sierra    eki-7EA73854    eri-1E5C3571   monitoring-disabled  198.202.120.101 10.128.74.140   instance-store   paravirtualized

If you need to delete a deployed VM, you can use the
``euca-terminate-instances`` command with the instance id::

           $ euca-terminate-instances i-B2EF473E


Logging Into the VM
-----------------------

The ssh private key that was generated earlier can now be used to
login to the VM. We are using the CentOS image so we log in as the
user ``cloud-user``::

    $ ssh -i $USER-key.pem cloud-user@10.128.74.140
    [cloud-user@ip-10-128-74-140 ~]$

Note, if you are using the Ubuntu 14.04 image, you will need to use
the username ``ubuntu`` instead of ``cloud-user``.

If you see a message something like::

    Warning: Identity file $USER-key.pem not accessible: No such file or directory.

this likely means that you are in a directory other than where your
key file is saved. Change to the directory containing your key file,
or use a fully-qualified path in the ``-i`` argument

    [cloud-user@ip-10-128-74-140 ~]$ uname -a
    Linux ip-10-128-74-140 2.6.32-431.17.1.el6.x86_64 #1 SMP Wed May 7 23:32:49 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux


Shutting down the VM
-----------------------
When you are finished with your instance, terminate it to release resources for other users::

    $ euca-terminate-instances i-B2EF473E

You may continue to see your instance in a "terminated" state in the
output of ``euca-describe-instances`` for a period of time after you
terminate it. This is normal.


VM Network Info
-------------------

Note that each VM instance has a public IP address (starting with
``198.202``) and a private IP address (starting with ``10.128``). If
you need to access your VM from outside the sierra login node, you
will need to use the public IP address. These IP addresses are listed
in the output of the ``euca-describe-instances`` command.

On the VM, the network will show only the VM private IP address::

    [cloud-user@ip-10-128-74-140 ~]$ ip addr show eth0
    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
        link/ether d0:0d:b2:ef:47:3e brd ff:ff:ff:ff:ff:ff
        inet 10.128.74.140/27 brd 10.128.74.159 scope global eth0
        inet6 fe80::d20d:b2ff:feef:473e/64 scope link 
           valid_lft forever preferred_lft forever


Image Management
--------------------

Please take care to only install images that you create yourself or
obtain from trustworthy sources. You are responsible for the images
you use on FutureGrid resources. Any instances that are detetermined
to contain malware, or to be spamming, or attacking other systems on
the network, etc. will be terminated without notice and deleted.

Eucalyptus provides several "starter" images in their github
repository. We will use one of these to demonstrate basic image
management. For more image management information see the `Image Tasks
section of the Eucalyptus documentation
<https://www.eucalyptus.com/docs/eucalyptus/3.4/index.html#image-guide/img_task_intro.html>`__

We will use the first image on the list (as of 25-Jun-2014 this is
CentOS 6.4. We have found that some of the Ubuntu images at this site
do not work, as of this date).

The following steps are executed on the sierra login node. Be sure you
have run ``module load euca2ools`` and ``source eucarc`` before
proceeding.

First download the image archive::

  $ wget http://emis.eucalyptus.com/starter-emis/euca-centos6.4-ec2user-2013.07.12-x86_64.tzg

Uncompress it::

  $ tar xzf euca-centos6.4-ec2user-2013.07.12-x86_64.tgz

We can see that this archive includes kernel, ramdisk, and root partiton images::

  $ tree euca-centos6.4-ec2user-2013.07.12-x86_64
  euca-centos6.4-ec2user-2013.07.12-x86_64
  |-- euca-centos6.4-ec2user-2013.07.12-x86_64.img
  `-- kvm-kernel
      |-- initramfs-2.6.32-358.11.1.el6.x86_64.img
      `-- vmlinuz-2.6.32-358.11.1.el6.x86_64

Eucalyptus restricts kernel image registration to administrators, so
we will use existing FutureGrid CentoOS kernel and ramdisk images with
the downloaded root partition image.

We will need to bundle the image, kernel and ramdisk, upload the
bundle, and register it. When uploading the bundle, you must specify a
Walrus bucket with the ``-b`` argument to ``euca-upload-bundle``. The
buckets fg-image, fg-ramdisk, and fg-kernel are reserved for
FutureGrid administrative use. We suggest using your Portal username
or project as a bucket name.

First we will find our kernel and ramdisk images::

  $ euca-describe-images --all | grep fg-kernel
  IMAGE   eki-19543879    fg-kernel/vmlinuz-3.13.0-29-generic.manifest.xml        663263781684    available       public  x86_64  kernel    instance-store
  IMAGE   eki-7EA73854    fg-kernel/vmlinuz-2.6.32-431.17.1.el6.x86_64.manifest.xml       663263781684    available       public  x86_64  kernel    instance-store

  $ euca-describe-images --all | grep fg-ramdisk
  IMAGE   eri-13F63599    fg-ramdisk/initrd.img-3.13.0-29-generic.manifest.xml    663263781684    available       public  x86_64  ramdisk   instance-store
  IMAGE   eri-1E5C3571    fg-ramdisk/initramfs-2.6.32-431.17.1.el6.x86_64.img.manifest.xml        663263781684    available       public  x86_64     ramdisk    instance-store

We'll use the 2.6.32 kernel and ramdisk which matches what was in the image archive we downloaded.::

  $ euca-bundle-image -i euca-centos6.4-ec2user-2013.07.12-x86_64.img --kernel eki-7EA73854 --ramdisk eri-1E5C3571 --arch x86_64
  Wrote manifest /var/tmp/bundle-XiJgSu/euca-centos6.4-ec2user-2013.07.12-x86_64.img.manifest.xml

Use the generated xml manifest to upload the bundle. Remember to use
your own username or project as bucket name (``-b`` argument)::

  $ euca-upload-bundle -b fg82 -m /var/tmp/bundle-XiJgSu/euca-centos6.4-ec2user-2013.07.12-x86_64.img.manifest.xml
  Uploaded fg82/euca-centos6.4-ec2user-2013.07.12-x86_64.img.manifest.xml

Finally, register the image::

  $ euca-register fg82/euca-centos6.4-ec2user-2013.07.12-x86_64.img.manifest.xml -a x86_64 -n centos-6_4-image
  IMAGE   emi-BFC33B29

The returned image ID can now be used to start instances with ``euca-run-instances`` as described earlier.  ``euca-describe-images`` shows this as a private image now::

  $ euca-describe-images
  ...
  IMAGE   emi-BFC33B29    fg82/euca-centos6.4-ec2user-2013.07.12-x86_64.img.manifest.xml  597941386389    available       private x86_64  machine    eki-7EA73854    eri-1E5C3571            instance-store  paravirtualized

To remove an image, first deregister it, then delete the bundle. The
argument value to use for ``-p`` is the prefix of the image manifest
name (everything before the .manifest.xml suffix)::

  $ euca-deregister emi-BFC33B29

  $ euca-delete-bundle -b fg82 -p euca-centos6.4-ec2user-2013.07.12-x86_64.img

  

Status of Deployments
---------------------

At times you may ask if the Eucalyptus systems on FutureGrid are
operational. You can find this out by visiting 

a) The :portal:`Outage page <metrics/html/results/realtime.html#total-count-of-running-vm-instances-updated-every-5-seconds>`
b) The `Real Time Status monitor <http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid>`__
c) Our `Runtime History <http://inca.futuregrid.org:8080/inca/jsp/report.jsp?xml=cloudReport.xml>`__

