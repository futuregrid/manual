.. _s-eucalyptus:

===================================================
Eucalyptus
===================================================

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
(`Euca2ools <https://launchpad.net/euca2ools>`__). A more detailed
documentation can be found in the `Eucalyptus
Website <http://www.eucalyptus.com/eucalyptus-cloud/iaas>`__. A detailed
user guide is also available
`here <http://www.eucalyptus.com/sites/all/modules/pubdlcnt/pubdlcnt.php?file=/sites/all/files/docs/latest/ug.pdf&nid=296>`__.


As of May 15, 2012, FutureGrid is using `Eucalyptus version
3.1 <http://www.eucalyptus.com/eucalyptus-cloud/iaas/features>`__ which
requires `euca2ools
2.1.2 <http://www.eucalyptus.com/download/euca2ools>`__ and python > 2.4
(available by modules on india). Make sure to load the
euca2ools module::

    $ module load euca2ools

before using Eucalyptus. `euca2ools
2.1.2 <http://www.eucalyptus.com/download/euca2ools>`__ is part of
Eucalyptus Enterprise package. However, the source is available
`here <http://bazaar.launchpad.net/~eucalyptus-maintainers/euca2ools/euca2ools-main/revision/>`__.


Account Creation
--------------------

Eucalyptus 3.1 accounts are provisioned for all FutureGrid users with a
valid portal account and project affiliation. There is no need to apply
for Eucalyptus accounts separately.

Obtaining Credentials

-  Credentials files are created by default and placed in your home
   directory under *.futuregrid* folder on india.  There are separate
   credentials for each FutureGrid project. For instance, if you are
   part of FutureGrid project numbers 100 and 200, there will be two
   folders (fg100 and fg200) in *.futuregrid/eucalyptus*. Each project
   folder contains a corresponding credentials zip file. So
   fg100:username and fg200:username in Eucalyptus are two different
   identities, but they are tied to the same FutureGrid user.

   *NOTICE:* Due to an compatibility problem introduced during the
   upgrade to the Eucalyptus 3.1 system, accessing the GUI dashboard of
   Eucalyptus on india is temporarily unavailable. However, your credential
   will be in place so you can execute the steps of this tutorial using euca2ools.

-  Find your credential zip file in cd
   $HOME/.futuregrid/eucalyptus/fgprojectnumber::

           $ unzip euca3-{username}-{cluster}-fgprojectnumber.zip  

-  Apply the eucarc file::

       source eucarc

-  If you want to add Eucalyptus environment variables to your .bashrc
   then, do this: (if you are planning to switch between different cloud
   platforms, it is probably better to use source::

           $ cat eucarc >> $HOME/.bashrc
           $ source .bashrc



Resources Overview
----------------------

Eucalyptus is available to FutureGrid Users on the India
cluster. As we will see later, when we instantiate a Virtual Machine
(VM) we must select the type of VM Image that we are going to
use. The VM Image types available are:

India::

    AVAILABILITYZONE    euca3india    149.165.146.135 arn:euca:eucalyptus:euca3india:cluster:euca3indiaCC/
    AVAILABILITYZONE    |- vm types    free / max   cpu   ram  disk
    AVAILABILITYZONE    |- m1.small    0189 / 0192   1    512     5
    AVAILABILITYZONE    |- c1.medium    0170 / 0171   1   2048     7
    AVAILABILITYZONE    |- m1.large    0091 / 0094   2   5120    10
    AVAILABILITYZONE    |- m1.xlarge    0073 / 0075   2   6000    15
    AVAILABILITYZONE    |- c1.xlarge    0044 / 0047   4   9216    20


Testing Your Setup
----------------------

Use euca-describe-availability-zones to test the setup::

        $ ssh portalname@india.futuregrid.org
        Last login: Fri May 11 06:39:02 2012 from 129-79-49-230.dhcp-bl.indiana.edu

        Welcome to India.FutureGrid.Org

        torque/2.5.5 version 2.5.5 loaded
        moab version 5.4.0 loaded 
      
        
::
        
        $ module load euca2ools
        euca2ools version 2.1.2 loaded

::

        $ euca-version
        euca2ools 2.1.2 (Limbo)

::

        $ source .futuregrid/eucalyptus/fgprojectnumber/eucarc
        $ euca-describe-availability-zones
        AVAILABILITYZONE  euca3india  149.165.146.135 arn:euca:eucalyptus:euca3india:cluster:euca3indiaCC/

Available Images

List the existing images using euca-describe-images::

        $ euca-describe-images 

        IMAGE    emi-8E1C3B69    euca-centos-2012/euca-centos-2012.1.14-x86_64.img.manifest.xml    available    public    
        IMAGE    emi-D21D3F6C    euca3/ubuntu-natty.img.manifest.xml    available    public    
        IMAGE    emi-1A413C95    centos/centos.5-3.x86-64.img.manifest.xml    available    public    
        IMAGE    eki-9F293A6A    kernel/vmlinuz-2.6.27.21-0.1-xen.manifest.xml    available    public    
        IMAGE    emi-0FA13B83    inca/centos5inca3128800784.img.manifest.xml    available    public    
        IMAGE    emi-A9D33917    ubuntu/ubuntu.9-04.x86-64.img.manifest.xml    available    public    
        IMAGE    eri-D1513DBA    ramdisk/initrd-2.6.27.21-0.1-xen.manifest.xml    available    public    
        IMAGE    eki-919E3C9A    kernel/vmlinuz-2.6.27.21-0.1-xen.manifest.xml    available    public    
        IMAGE    eri-55FE3F76    ramdisk/initrd.img-2.6.32-5-amd64.manifest.xml    available    public    
        IMAGE    eri-9DCC3A6B    ramdisk/initrd-2.6.27.21-0.1-xen.manifest.xml    available    public    
        ...
        
This command may take quite a bit of time as there are currently many images available. On sierra, we observed more than 40 seconds before the command returned.
 

Image Deployment
--------------------

Before deploying a VM, you need to create at least one key pair. This
key pair will be injected into the VM, allowing you to SSH into the
instance. This is done using the euca-add-keypair command::

        $ euca-add-keypair $USER-key   > $USER-key.pem


Fix the permissions on the generated private key::

        $ chmod 0600 $USER-key.pem 

When executing the euca-add-keypair command you will however run into
problems. To see if you have done this, please cat the key with::

    $ cat $USER-key.pem

If you see a message that starts with::

    -----BEGIN RSA PRIVATE KEY-----

things should be fine. However, if you see::

    CreateKeyPairType: Keypair already exists: gvonlasz-key: Could not execute JDBC batch update

You have created the key multiple times and you may encounter
problems later on. The best thing to do is to check if your key is
already  in the keypair list. This can 
such as::

        $ euca-describe-keypairs

If it is, you probably have uploaded it already. If you need to create
a new key however, you can delete the old one by 

        $ euca-delete-keypair $USER-key

After that you naturally need to create a new one as described above.

Now you can start a VM using one of the pre-existing images.  We have uploaded an ubuntu image for you that you can find out more
about with::

   $ euca-describe-images | fgrep futuregrid\/precise

It will show you an id starting with the prefix "emi-"::

    IMAGE	emi-63F93D41	futuregrid/precise-server-cloudimg-amd64.img.manifest.xml	...

we use this id in the next step. Use the
euca-run-instances command to start the VM::

        $ euca-run-instances -k $USER-key -n 1 -t c1.medium emi-63F93D41

        RESERVATION     r-4E730969      $USER-key    $USER-key-default
        INSTANCE        i-4FC40839      emi-63F93D41    0.0.0.0 0.0.0.0 pending userkey   2010-07-20T20:35:47.015Z   eki-743D3CFA   eri-4E163AA8

The euca-describe-instances command can be used to check the status
of the request. The following image was assigned an ip address and is
starting up, as demonstrated by the "pending" status::

        $ euca-describe-instances 

        RESERVATION     r-4E730969      $USER-key    default
        INSTANCE        i-4FC40839      emi-63F93D41    149.165.146.153 10.0.2.194      pending         userkey         0       
                  m1.small        2010-07-20T20:35:47.015Z        india   eki-743D3CFA    eri-4E163AA8

Once started, the status will change to "running"::

        $ euca-describe-instances

        RESERVATION     r-4E730969      $USER-key    default
        INSTANCE        i-4FC40839      emi-63F93D41    149.165.146.153 10.0.2.194      running         userkey         0       
                  m1.small        2010-07-20T20:35:47.015Z        india   eki-743D3CFA    eri-4E163AA8

If you need to delete a deployed VM, you can use the
euca-terminate-instances command::

           $ euca-terminate-instances i-4FC40839

Logging Into the VM
-----------------------

Create rules to allow access to the VM over ssh and to allow ping

    $ euca-authorize -P tcp -p 22 -s 0.0.0.0/0   default
    $ euca-authorize -P icmp -t -1:-1 -s 0.0.0.0/0 default

The ssh private key that was generated earlier can now be used to
login to the VM::

        $ssh -i userkey.pem root@149.165.146.153

        # uname -a

         Linux localhost 2.6.27.21-0.1-xen #1 SMP   2009-03-31 14:50:44 +0200 x86_64 x86_64 x86_64 GNU/Linux

VM Network Info
-------------------

The VM itself is visible from outside using the VM public IP. The
internal network will show the VM private IP address::

        # /sbin/ifconfig

        eth0    Link encap:Ethernet  HWaddr D0:0D:33:14:06:40  
                inet addr:10.0.2.194  Bcast:10.0.2.255  Mask:255.255.255.192

Image Management
--------------------

We will use the example ubuntu 10 image to test uploading images.
Download the gzipped tar ball::

        $ wget http://cloud-images.ubuntu.com/releases/precise/release/ubuntu-12.04-server-cloudimg-amd64.tar.gz

Uncompress and untar the archive::

        $ tar zxf ubuntu-12.04-server-cloudimg-amd64.tar.gz

Bundle the image with a kernel and a ramdisk using the
euca-bundle-image command. In this example, we will use the xen
kernel already registered. euca-describe-images returns the kernel
and ramdisk IDs that we need::

        $ euca-bundle-image -i   precise-server-cloudimg-amd64.img --kernel eki-78EF12D2 --ramdisk   eri-5BB61255

        Checking image
        Tarring image
        Encrypting image
        Splitting image...
        Part:   precise-server-cloudimg-amd64.img.part.0
        Part:   precise-server-cloudimg-amd64.img.part.1
        Part:   precise-server-cloudimg-amd64.img.part.2
        Part:   precise-server-cloudimg-amd64.img.part.3
        Part:   precise-server-cloudimg-amd64.img.part.4
        Part:   precise-server-cloudimg-amd64.img.part.5
        Part:   precise-server-cloudimg-amd64.img.part.6
        Part:   precise-server-cloudimg-amd64.img.part.7
        Part:   precise-server-cloudimg-amd64.img.part.8
        Part:   precise-server-cloudimg-amd64.img.part.9
        Part:   precise-server-cloudimg-amd64.img.part.10
        Part:   precise-server-cloudimg-amd64.img.part.11
        Part:   precise-server-cloudimg-amd64.img.part.12
        Part:   precise-server-cloudimg-amd64.img.part.13
        Part:   precise-server-cloudimg-amd64.img.part.14
        Part:   precise-server-cloudimg-amd64.img.part.15
        Part:   precise-server-cloudimg-amd64.img.part.16
        Generating manifest   /tmp/precise-server-cloudimg-amd64.img.manifest.xml

Use the generated manifest file to upload the image to Walrus::

        $ euca-upload-bundle -b ubuntu-image-bucket   -m /tmp/precise-server-cloudimg-amd64.img.manifest.xml

        Checking bucket:   ubuntu-image-bucket
        Creating bucket:   ubuntu-image-bucket
        Uploading manifest   file
        Uploading part:   precise-server-cloudimg-amd64.img.part.0
        Uploading part:   precise-server-cloudimg-amd64.img.part.1
        Uploading part:   precise-server-cloudimg-amd64.img.part.2
        Uploading part:   precise-server-cloudimg-amd64.img.part.3
        Uploading part:   precise-server-cloudimg-amd64.img.part.4
        Uploading part:   precise-server-cloudimg-amd64.img.part.5
        Uploading part:   precise-server-cloudimg-amd64.img.part.6
        Uploading part:   precise-server-cloudimg-amd64.img.part.7
        Uploading part:   precise-server-cloudimg-amd64.img.part.8
        Uploading part:   precise-server-cloudimg-amd64.img.part.9
        Uploading part:   precise-server-cloudimg-amd64.img.part.10
        Uploading part:   precise-server-cloudimg-amd64.img.part.11
        Uploading part:   precise-server-cloudimg-amd64.img.part.12
        Uploading part:   precise-server-cloudimg-amd64.img.part.13
        Uploading part:   precise-server-cloudimg-amd64.img.part.14
        Uploading part:   precise-server-cloudimg-amd64.img.part.15
        Uploading part:   precise-server-cloudimg-amd64.img.part.16
        Uploaded image as   ubuntu-image-bucket/precise-server-cloudimg-amd64.img.manifest.xml

Register the uploaded image::

        $ euca-register   ubuntu-image-bucket/precise-server-cloudimg-amd64.img.manifest.xml

        IMAGE   emi-FFC3154F

The returned image ID can now be used to start instances with
euca-run-instances as described earlier. euca-describe-images also
shows the new image now::

        $ euca-describe-images 

        IMAGE emi-FFC3154F   ubuntu-image-bucket/precise-server-cloudimg-amd64.img.manifest.xml $USER-key available public   x86_64 machine eri-5BB61255 eki-78EF12D2 
        IMAGE emi-0B951139   centos53/centos.5-3.x86-64.img.manifest.xml           admin  available public   x86_64 machine 
          ...

You can also delete your images::

    $ euca-deregister emi-FFC3154F

Status of Deployments
---------------------

At times you may ask if the Eucalyptus systems on FutureGrid are
operational. You can find this out by visiting 

a) The :portal:`Outage page <metrics/html/results/realtime.html#total-count-of-running-vm-instances-updated-every-5-seconds>`
b) The `Real Time Status monitor <http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid>`__
c) Our `Runtime History <http://inca.futuregrid.org:8080/inca/jsp/report.jsp?xml=cloudReport.xml>`__

