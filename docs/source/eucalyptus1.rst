Using with Eucalyptus
---------------------

In order to use the tool with Eucalyptus, the following envs must be
set:

-  export
   CLOUDINITD\_IAAS\_URL='http://149.165.146.135:8773/services/Eucalyptus'
-  export CLOUDINITD\_IAAS\_ACCESS\_KEY=<your access key>
-  export CLOUDINITD\_IAAS\_SECRET\_KEY=<your access secret>
-  export CLOUDINITD\_IAAS\_IMAGE='emi-5F4F1B49'
    

You may have trouble registering your keys.� This is due to Eucalyptus
not yet supporting the latest version of the EC2 API.� To circumvent
this, create a key pair named 'futuregrid', and set the env
*CLOUDINITD\_IAAS\_SSHKEYNAME*\ to 'futuregrid'.� Then, set the env
*CLOUDINITD\_IAAS\_SSHKEY* to point to the private key associated with
that key name.

What Happens
============

This script uses the program cloudinit.d
(`http://www.nimbusproject.org/doc/cloudinitd/latest/) <http://www.nimbusproject.org/doc/cloudinitd/latest/>`__.�
This is a Nimbus Platform multi-cloud tool for running cloud
applications.� In this case, it runs a very simple 1 VM application.� It
can launch any debian-based VM and install sshfs on it.� Then it runs
sshfs inside of the VM to remotely mount your FutureGrid home directory.

FutureGrid Tutorial NM2 - Nimbus One-Click Cluster Guide
========================================================

�

**Summary:**

This tutorial demonstrates using the Nimbus cloud client to create
auto-configured clusters of virtual machines on Nimbus.

�

**Prerequisites:**

Java 1.5+ and a working Nimbus cloud client.

�

**Hands-On Tutorial**:

This tutorial is maintained at the Nimbus website. See�\ `One Click
Clusters <http://www.nimbusproject.org/docs/current/clouds/clusters.html>`__.

�

**Reference Material:**

`Nimbus Documentation <http://www.nimbusproject.org/docs/>`__

�

**Authors:**

Tim Freeman, Kate Keahey, David LaBissoniere, John Bresnahan

University of Chicago

Using Eucalyptus on FutureGrid
==============================

Presentation about this document:
`fg-tutorial-eucalyptus.ppt <http://futuregrid.svn.sourceforge.net/viewvc/futuregrid/presentations/software/fg-tutorial-eucalyptus.ppt>`__

**Summary**
-----------

Eucalyptus is a software platform that implements
`IaaS-style <http://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_Service_.28IaaS.29>`__
cloud computing. Eucalyptus provides an Amazon Web Services
(`AWS <http://aws.amazon.com/>`__) complaint EC2-based web service
interface for interacting with the Cloud service. Additionally,
Eucalyptus provides services such as the AWS Complaint Walrus and a user
interface for managing users and images. The aim of this tutorial is to
give users an introduction of how to interact with Eucalyptus using the
Eucalyptus EC2 Interface
(`Euca2ools <https://launchpad.net/euca2ools>`__). More detailed
documentation can be found in the `Eucalyptus
Website <http://www.eucalyptus.com/eucalyptus-cloud/iaas>`__. A detailed
user guide is also available
`here <http://www.eucalyptus.com/sites/all/modules/pubdlcnt/pubdlcnt.php?file=/sites/all/files/docs/latest/ug.pdf&nid=296>`__.

**Requirements**
----------------

Users get access to the Eucalyptus features using the Eucalyptus EC2
Interface, which is only available for GNU/Linux platforms. Therefore,
users will require a machine with a GNU/Linux installed on it.
�

Eucalyptus 3
''''''''''''

As of May 15, 2012, FutureGrid is using `Eucalyptus version
3 <http://www.eucalyptus.com/eucalyptus-cloud/iaas/features>`__ which
requires `euca2ools
2.0.2 <http://www.eucalyptus.com/download/euca2ools>`__ and python > 2.4
(available by modules in india and sierra). Make sure to load **"module
load euca2ools/2.0.2"** before using Eucalyptus. `euca2ools
2.0.2 <http://www.eucalyptus.com/download/euca2ools>`__ is part of
Eucalyptus Enterprise package. However, the source is available
`here <http://bazaar.launchpad.net/~eucalyptus-maintainers/euca2ools/euca2ools-main/revision/>`__.
�

**Account Creation**
--------------------

Eucalyptus 3 is now integrated with our LDAP. Each account is created by
default for all FutureGrid users with valid portal account and project
affiliation. There is no need to apply for accounts.

**Obtaining Credentials**

-  Credentials files are created by default and placed in a user's home
   directory under *.futuregrid* folder in india and sierra. To leverage
   LDAP group, we created separate credentials for each FutureGrid
   project. For instance, if you are part of FutureGrid project number
   100 and 200, there will be two folders (**fg100** and **fg200**) in
   *.futuregrid/eucalyptus*. Each project folder contains corresponding
   credentials zip files. So fg100:username and fg200:username in
   Eucalyptus, however, two different identities are tied to the same
   LDAP user. A user can also download the credential file from the
   Eucalyptus dashboard in
   `india <https://eucalyptus.india.futuregrid.org:8443>`__ and
   `sierra <https://eucalyptus.sierra.futuregrid.org:8443>`__. To log in
   to the dashboard, use your FutureGrid project number (in the format
   of *fgnumber)*\ as "Account" and your portal user name as "User".
   Then use the FutureGrid portal password. (If you download the file
   from the dashboard, by default the system will name the file
   *euca2-{username}-x509*). We are using a slightly different naming
   scheme. The credential file will be found under the menu tab
   *username@fgnumber�*.)

NOTICE: Due to an incompatibility problem introduced during the
upgrade to the Eucalyptus 3.1 system, accessing the dashboard of
Eucalyptus on india is tempararily unavailable. However, your credential
will be in place so you can execute the later steps of this manual.
On Sierra, the access is still available so you could download the
credential zip file. Make sure to put it to Sierra first and then set up
the environment as the following steps.
Please be reminded that the credential for one cluster should/could
not be used in another.
�

|image88|

-  Find your credential zip file in cd
   $HOME/.futuregrid/eucalyptus/fgprojectnumber :

       ::

           $ unzip euca3-{username}-{cluster}-fgprojectnumber.zip  

-  Apply the eucarc file:

   ::

       source eucarc

-  If you want to add Eucalyptus environment variables to your .bashrc
   then, do this: (if you are planning to switch between different cloud
   platforms, it is probably better to use source. 

       ::

           $ cat eucarc >> $HOME/.bashrc

       ::

           $ source .bashrc

**Install Euca2tools**

    Older versions of euca2ools are not compatible with Eucalyptus 3.
    `euca2ools 2.0.2 <http://www.eucalyptus.com/download/euca2ools>`__
    is part of the Enterprise project and so is not available for all
    users. However, the source is available
    `here <http://bazaar.launchpad.net/~eucalyptus-maintainers/euca2ools/euca2ools-main/files>`__.

**Resources Overview**
----------------------

Eucalyptus is available to FutureGrid Users on the India and Sierra
clusters. As we will see later, when we instantiate a Virtual Machine
(VM), it is needed to select the type of VM Image that we are going to
use. In this sense, the information of the VM Image types available in
each cluster is summarized below:

INDIA:�
^^^^^^^

::

    AVAILABILITYZONE    �euca3india    149.165.146.135 arn:euca:eucalyptus:euca3india:cluster:euca3indiaCC/
    AVAILABILITYZONE    |- vm types    free / max   cpu   ram  disk
    AVAILABILITYZONE    |- m1.small    0189 / 0192   1    512     5
    AVAILABILITYZONE    |- c1.medium    0170 / 0171   1   2048     7
    AVAILABILITYZONE    |- m1.large    0091 / 0094   2   5120    10
    AVAILABILITYZONE    |- m1.xlarge    0073 / 0075   2   6000    15
    AVAILABILITYZONE    |- c1.xlarge    0044 / 0047   4   9216    20

SIERRA: 
^^^^^^^^

::

    AVAILABILITYZONE    euca3sierra    198.202.120.90 arn:euca:eucalyptus:euca3sierra:cluster:euca3sierraCC/
    AVAILABILITYZONE    |- vm types    free / max   cpu   ram  disk
    AVAILABILITYZONE    |- m1.small    0051 / 0056   1    256     4
    AVAILABILITYZONE    |- c1.medium    0037 / 0042   1    512     5
    AVAILABILITYZONE    |- m1.large    0012 / 0014   2   1024    10
    AVAILABILITYZONE    |- m1.xlarge    0012 / 0014   2   1024    12
    AVAILABILITYZONE    |- c1.xlarge    0009 / 0014   4   2048    15

**Testing Your Setup**
----------------------

Use euca-describe-availability-zones to test the setup:

    ::

        ssh sierra.futuregrid.org
        Last login: Fri May 11 06:39:02 2012 from 129-79-49-230.dhcp-bl.indiana.edu

        Welcome to Sierra.FutureGrid.Org

        torque/2.4.8 version 2.4.8 loaded
        moab version 5.4.0 loaded 

        $ module load euca2ools/2.0.2
        euca2ools version 2.0.2 loaded
        $ euca-version
        euca2ools 2.0.2
        $ source .futuregrid/eucalyptus/fgprojectnumber/eucarc
        $ euca-describe-availability-zones
        AVAILABILITYZONE    euca3sierra    198.202.120.90 arn:euca:eucalyptus:euca3sierra:cluster:euca3sierraCC/

**Available Images**

List the existing images using euca-describe-images:

    ::

        $ euca-describe-images 

        IMAGE    emi-8E1C3B69    euca-centos-2012/euca-centos-2012.1.14-x86_64.img.manifest.xml    available    public    
        IMAGE    emi-D21D3F6C    euca3/ubuntu-natty.img.manifest.xml    available    public    
        IMAGE    emi-1A413C95    centos/centos.5-3.x86-64.img.manifest.xml    available    public    
        IMAGE    eki-9F293A6A    kernel/vmlinuz-2.6.27.21-0.1-xen.manifest.xml    available    public    
        IMAGE    emi-0FA13B83    inca/centos5inca3128800784.img.manifest.xml    available    public    
        IMAGE    emi-A9D33917    ubuntu/ubuntu.9-04.x86-64.img.manifest.xml    available    public    
        IMAGE    eri-D1513DBA    ramdisk/initrd-2.6.27.21-0.1-xen.manifest.xml    available    public    
        IMAGE    eki-919E3C9A    kernel/vmlinuz-2.6.27.21-0.1-xen.manifest.xml    available    public    
        IMAGE    eri-55FE3F76    ramdisk/initrd.img-2.6.32-5-amd64.manifest.xml    available    public    
        IMAGE    eri-9DCC3A6B    ramdisk/initrd-2.6.27.21-0.1-xen.manifest.xml    available    public    


**Image Deployment**
--------------------

-  Before deploying a VM, you need to create at least one key pair. This
   key pair will be injected into the VM, allowing you to SSH into the
   instance. This is done using the euca-add-keypair command:

    ::

        $ euca-add-keypair userkey   > userkey.pem

-  Fix the permissions on the generated private key:

    ::

        $ chmod 0600 userkey.pem 

-  Now you can start a VM using one of the pre-existing images. You need
   the emi-id of the image you want to start. This was listed in the
   output of euca-describe-images command that you saw earlier. Use the
   euca-run-instances command to start the VM:

    ::

        $ euca-run-instances -k userkey -n 1   emi-0B951139 -t c1.medium

        RESERVATION     r-4E730969      archit    archit-default
        INSTANCE        i-4FC40839      emi-0B951139    0.0.0.0 0.0.0.0 pending userkey   2010-07-20T20:35:47.015Z   eki-78EF12D2   eri-5BB61255

-  The euca-describe-instances command can be used to check the status
   of the request. The following image was assigned an ip address and is
   starting up, as demonstrated by the "pending" status:

    ::

        $ euca-describe-instances 

        RESERVATION     r-4E730969      archit    default
        INSTANCE        i-4FC40839      emi-0B951139    149.165.146.153 10.0.2.194      pending         userkey         0       
                  m1.small        2010-07-20T20:35:47.015Z        india   eki-78EF12D2    eri-5BB61255

-  Once started, the status will change to "running":

    ::

        $ euca-describe-instances

        RESERVATION     r-4E730969      archit    default
        INSTANCE        i-4FC40839      emi-0B951139    149.165.146.153 10.0.2.194      running         userkey         0       
                  m1.small        2010-07-20T20:35:47.015Z        india   eki-78EF12D2    eri-5BB61255

-  If you need to delete a deployed VM, you can use the
   euca-terminate-instances command:

       ::

           $ euca-terminate-instances i-4FC40839

**Logging Into the VM**
-----------------------

-  Create rules to allow access to the VM over ssh and to allow ping:

    $ euca-authorize -P tcp -p 22 -s 0.0.0.0/0   default
    $ euca-authorize -P icmp -t -1:-1 -s 0.0.0.0/0 default

-  The ssh private key that was generated earlier can now be used to log
   in to the VM:

    ::

        $ssh -i userkey.pem root@149.165.146.153

        -bash-3.2# uname -a

         Linux localhost 2.6.27.21-0.1-xen #1 SMP   2009-03-31 14:50:44 +0200 x86_64 x86_64 x86_64 GNU/Linux

**VM Network Info**
-------------------

-  The VM itself is visible from outside using the VM public IP. The
   internal network will show the VM private IP address:

    ::

        -bash-3.2# /sbin/ifconfig

        eth0    Link encap:Ethernet  HWaddr D0:0D:33:14:06:40  
                inet addr:10.0.2.194  Bcast:10.0.2.255  Mask:255.255.255.192

**Image Management**
--------------------

-  We will use the example ubuntu 10 image to test uploading images.
   Download the gzipped tar ball:

    ::

        $ wget http://cloud-images.ubuntu.com/releases/precise/release/ubuntu-12.04-server-cloudimg-amd64.tar.gz

-  Uncompress and untar the archive:

    ::

        $ tar zxf ubuntu-12.04-server-cloudimg-amd64.tar.gz

-  Bundle the image with a kernel and a ramdisk using the
   euca-bundle-image command. In this example, we will use the xen
   kernel already registered. euca-describe-images returns the kernel
   and ramdisk IDs that we need:

    ::

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

-  Use the generated manifest file to upload the image to Walrus:

    ::

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

-  Register the uploaded image:

    ::

        $ euca-register   ubuntu-image-bucket/precise-server-cloudimg-amd64.img.manifest.xml

        IMAGE   emi-FFC3154F

-  The returned image ID can now be used to start instances with
   euca-run-instances as described earlier. euca-describe-images also
   shows the new image now:     ::

$ euca-describe-images 

IMAGE emi-FFC3154F   ubuntu-image-bucket/precise-server-cloudimg-amd64.img.manifest.xml archit available public   x86_64 machine eri-5BB61255 eki-78EF12D2 
        IMAGE emi-0B951139   centos53/centos.5-3.x86-64.img.manifest.xml           admin  available public   x86_64 machine 
          ...

-  You can also delete your images:

::

    $ euca-deregister emi-FFC3154F

Status of Deployments
---------------------

At times, you may ask if the Eucalyptus systems on FutureGrid are
operational. You can find this out by visiting the following:

a) The Outage page
at \ `https://portal.futuregrid.org/metrics/html/results/realtime.html#total-count-of-running-vm-instances-updated-every-5-seconds <https://portal.futuregrid.org/metrics/html/results/realtime.html#total-count-of-running-vm-instances-updated-every-5-seconds>`__
b) The Real Time Status monitor
at \ `http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid <http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid>`__
c) Our Runtime History
at \ `http://inca.futuregrid.org:8080/inca/jsp/report.jsp?xml=cloudReport.xml <http://inca.futuregrid.org:8080/inca/jsp/report.jsp?xml=cloudReport.xml>`__
