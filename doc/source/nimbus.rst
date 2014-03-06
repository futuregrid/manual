**********************************************************************
Nimbus
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:


Nimbus IaaS
====================================================================== 

|image0|
--------

 

What is Nimbus?
---------------

Nimbus is an open source service package that allows users to run
virtual machines on FutureGrid hardware. You can easily upload your own
VM image or customize an image provided by us. When you boot a VM, it is
assigned a public IP address (and/or an optional private address); you
are authorized to log in as root via SSH. You can then run services,
perform computations, and configure the system as desired. After using
and configuring the VM, you can save the modified VM image back to the
Nimbus image repository.
 

Nimbus on FutureGrid
--------------------

Nimbus is installed on four FutureGrid clusters:

#. **Hotel** (University of Chicago)
    42 nodes, 336 cores (30 nodes using Xen and 12 nodes using KVM)
#. **Foxtrot** (University of Florida)
    24 nodes, 192 cores
#. **Sierra** (San Diego Supercomputer Center)
    18 nodes, 144 cores
#. **Alamo** (Texas Advanced Computing Center)
    15 nodes, 120 cores

By default, users are limited to running 16 VMs simultaneously and
claiming two cores per VM. If you have a good reason for this limitation
to be lifted for your account,
contact \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__.

All FutureGrid users are allowed access to Nimbus on all sites.

Getting Started
---------------

Nimbus provides services that can be controlled remotely using a variety
of clients. In this tutorial, we will use a simple command line tool
called the \ **cloud-client**. If you'd rather have programmatic
control, the Amazon EC2 protocols \ `are
supported <http://www.nimbusproject.org/docs/current/elclients.html>`__,
which have a variety of excellent clients available for many
languages.  

Log into hotel
~~~~~~~~~~~~~~

The first step is to ssh into hotel.futuregrid.org.  While you can use
Nimbus clients from anywhere in the world, we recommend that you start
on hotel because the correct version of Java is installed there.

::

    $ ssh -A hotel.futuregrid.org

If this command fails, contact
`https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__. 
It likely means one of the following:

#. Your account is not yet set up.
#. You provide no public key or a corrupted public key.
#. The private key you are using does not match the public one you
   registered with FutureGrid.

Download and install cloud-client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the Nimbus cloud client from the \ `Nimbus
website <http://www.nimbusproject.org/downloads/>`__.

::

    $ wget http://www.nimbusproject.org/downloads/nimbus-cloud-client-022.tar.gz

Unpack the archive into your home directory.

::

    $ tar xzf nimbus-cloud-client-022.tar.gz
    $ ls nimbus-cloud-client-022/
    CHANGES.txt README.txt  conf        lib
    LICENSE.txt bin     history     samples

Obtain Your Nimbus Credentials and Configuration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your home directory on hotel, you will find the file
nimbus\_creds.tar.gz:

::

     username@hotel $ ls ~/nimbus_creds.tar.gz
    nimbus_creds.tar.gz

If your credentials are not present on \ **Hotel**,
contact \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__.

Download and unpack these files into your cloud-client's directory:

::

    $ cd nimbus-cloud-client-022/conf/
    $ tar xvzf ~/nimbus_creds.tar.gz
    usercert.pem
    userkey.pem
    cloud.properties
    alamo.conf
    foxtrot.conf
    hotel.conf
    sierra.conf
    hotel-kvm.conf

Now you should have a functional cloud client. To begin, check out the
help text and file.

::

    $ cd ../

::

    $ bin/cloud-client.sh --help

Check Your ssh Key
~~~~~~~~~~~~~~~~~~

In order to use Nimbus clouds effectively, you need to have your ssh
public key in a known place so that it can be injected into your VM, and
thus allow you (and only you) root access to your VM. When creating your
FutureGrid account you had to upload an ssh public key.  That key can be
found on hotel in the file *~/.ssh/authorized\_keys*.  If you were able
to ssh into hotel then this is the public key are are currently using. 
Nimbus needs this key to be in the\ *~/.ssh/id\_rsa.pub*:

::

    $ cp ~/.ssh/authorized_keys ~/.ssh/id_rsa.pub

Because the security environment can be complicated, cloud-client has an
option to help verify that things are working.  Run the following
command to display some information about your security environment:

::

    $ ./bin/cloud-client.sh --security

Using the Cloud Client
----------------------

Check out the various FutureGrid clouds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the credentials file was untarred in a step above, a
configuration file for each of the four FutureGrid clouds was put in
your *conf/*\ directory.  Now let's take a look at accessing each of
those clouds and seeing what virtual machines are available for use.
This will require two options to cloud client.  The first is --conf ;
this is used to select the cloud you wish to use.  Simply provide a path
to the cloud configuration file.  This --conf switch will be used in all
commands to direct cloud-client at the cloud of interest.

 The second option is --list.  This will simply provide a listing of
all the available virtual machines:

::

    $ bin/cloud-client.sh --conf conf/hotel-kvm.conf --list

This command should list the available images on the system.  Notice the
hello-cloud virtual machine.  This is the test image we will use in this
tutorial:

::

    [Image] 'hello-cloud'                    Read only
            Modified: Mar 6 2014 @ 10:01   Size: 2147483648 bytes (~2048 MB)

Run a Virtual Machine
~~~~~~~~~~~~~~~~~~~~~

Next, try to boot a virtual machine:

::

    $ bin/cloud-client.sh --conf conf/hotel-kvm.conf --run --name hello-cloud --hours 2

    Launching workspace.

    Workspace Factory Service:
        https://login1.uc.futuregrid.org:8443/wsrf/services/WorkspaceFactoryService

    Creating workspace "vm-001"... done.


           IP address: 149.165.149.10
             Hostname: vm-149-10.uc.futuregrid.org
           Start time: Thu Mar 06 10:09:04 CST 2014
        Shutdown time: Thu Mar 06 12:09:04 CST 2014
     Termination time: Thu Mar 06 12:19:04 CST 2014

    Waiting for updates.


    "vm-001" reached target state: Running

    Running: 'vm-001'

Once the image is running, you should be able to log into it with SSH.
Note that you may need to wait another minute or so before you can
actually get it, as the system needs time to boot and start services.
Log in as the root user, and connect to the host printed out by the run
command.  Note that you **must**\ run this command in a location that
has access to your private key.  This means it must be in the *~/.ssh/*
directory on the file system from where you launch this command, or you
must have used the -A option to ssh when logging into hotel (as is shown
above). Make sure you replace the hostname of the VM by the one printed
out by cloud client.

::

    $ ssh root@vm-149-10.uc.futuregrid.org

Create a New VM Image
~~~~~~~~~~~~~~~~~~~~~

Once you have a root shell on your VM, you may modify it as through it
were a real machine.  Here we encourage you to make some changes. 
Create a new user, install some additional software, or simply create a
text file in the root user's account:

::

    # touch /root/CHANGE
    # exit

Save the Changes to a New VM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have modified the VM, you can save it back into your
personal repository.  To do this, you will use the --save and --newname
options.  You will also need the VM handle as it was displayed in the
output from the run command.  If you have forgotten what this was, you
can use the --status option to find it:

::

    $ ./bin/cloud-client.sh --conf conf/hotel-kvm.conf --status
    Querying for ALL instances.

    [*] - Workspace #59. 149.165.149.10 [ vm-149-10.uc.futuregrid.org ]
          State: Running
          Duration: 120 minutes.
          Start time: Thu Mar 06 10:09:04 CST 2014
          Shutdown time: Thu Mar 06 12:09:04 CST 2014
          Termination time: Thu Mar 06 12:19:04 CST 2014
          Details: VMM=c80
          *Handle: vm-001
           Image: hello-cloud

Note the handle *vm-001*.  To save the VM for future use, run the
following command:

::

    $ ./bin/cloud-client.sh --conf conf/hotel-kvm.conf --save --newname myvm --handle vm-001

    Saving workspace.
      - Workspace handle (EPR): '/N/u/priteau/nimbus-cloud-client-022/history/vm-001/vw-epr.xml'
      - New name: 'myvm'

    Waiting for updates.

    The image has successfully been transferred to your repository directory.

    Finalizing the deployment now (terminating the resource lease).

Do another listing of that cloud and you will see your VM is now
available for launch:

::

    $ ./bin/cloud-client.sh --conf conf/hotel-kvm.conf --list
    [Image] 'myvm'                           Read/write
            Modified: Mar 6 2014 @ 16:16   Size: 2147483648 bytes (~2048 MB)

    ----

    [Image] 'hello-cloud'                    Read only
            Modified: Mar 6 2014 @ 10:01   Size: 2147483648 bytes (~2048 MB)

Launch Your New VM
~~~~~~~~~~~~~~~~~~

You can now launch your new VM just like you did the hello-cloud VM
above, simply changing the name from *hello-cloud* to *myvm *:

::

    $ ./bin/cloud-client.sh --conf conf/hotel-kvm.conf --run --name myvm --hours 2

    Launching workspace.

    Workspace Factory Service:
        https://login1.uc.futuregrid.org:8443/wsrf/services/WorkspaceFactoryService

    Creating workspace "vm-002"... done.


           IP address: 149.165.149.10
             Hostname: vm-149-10.uc.futuregrid.org
           Start time: Thu Mar 06 10:28:26 CST 2014
        Shutdown time: Thu Mar 06 12:28:26 CST 2014
     Termination time: Thu Mar 06 12:38:26 CST 2014

    Waiting for updates.


    "vm-002" reached target state: Running

    Running: 'vm-002'


SSH into the machine and verify that your changes persisted.

Terminate the VM
~~~~~~~~~~~~~~~~

Your VM will terminate after its allocated time expires.  In our
examples here, this is after 2 hours.  However, you may wish to
terminate it earlier.  You can do so by again using the --handle option
as you did in the *save a new VM step* and the --terminate option:

::

    $ ./bin/cloud-client.sh --conf conf/hotel-kvm.conf --terminate --handle vm-002

    Terminating workspace.
      - Workspace handle (EPR): '/N/u/priteau/nimbus-cloud-client-022/history/vm-002/vw-epr.xml'

    Destroying vm-002... destroyed.

Converting a Xen image to KVM
-----------------------------

If you have existing virtual machine images running on Nimbus clouds using Xen
virtualization, you will need to convert them to run on a Nimbus cloud using
KVM virtualization (at the moment, Hotel KVM and Alamo).

In order to do this, you will need root access to a Linux machine with
`libguestfs <http://libguestfs.org>`__ available.

These instructions assume that the Xen image is called xen-image and is 6 GiB
(6144 MiB) in size.

First, we will create a file slightly bigger than the Xen image in order to
hold an MBR plus the original content of the image (in this case 6150 MiB
instead of 6144 MiB).

::

    # cd /tmp/
    # dd if=/dev/zero of=kvm.img bs=1M count=6150

Next, we initialize its partition layout:

::

    # parted kvm.img mklabel msdos
    # parted kvm.img mkpart primary ext2 512B 6442451456B
    # parted kvm.img set 1 boot on

And we can now copy the content of the Xen image into the new partition:

::

    # losetup /dev/loop0 kvm.img
    # kpartx -a /dev/loop0
    # dd if=xen-image of=/dev/mapper/loop0p1 bs=1M
    # fsck.ext3 -f /dev/mapper/loop0p1

Now the KVM image has a correct partition layout, but it is missing a
compatible kernel. The following instructions were done on a Debian image, you
might need to adapt to your Linux distribution.

::

    # mount /dev/mapper/loop0p1 /mnt
    # mount --bind /dev /mnt/dev
    # mount --bind /proc /mnt/proc
    # mount --bind /sys /mnt/sys
    # chroot /mnt
    # apt-get update
    # apt-get install linux-image-2.6.32-5-amd64
    # exit
    # umount /mnt/sys
    # umount /mnt/proc
    # umount /mnt/dev
    # umount /mnt

Finally, we install an MBR with libguestfs:

::

    # guestfish -i -a /tmp/kvm.img
    ><fs> command "update-grub"

    ><fs> list-devices
    /dev/vda
    ><fs> command "grub-install --force /dev/vda"
    Installation finished. No error reported.
    ><fs> command "grub-install --force --recheck /dev/vda"
    Installation finished. No error reported.
    ><fs> exit

The image kvm.img should now be ready to be uploaded to a Nimbus KVM cloud!

Virtual Clusters
----------------

This is a basic walkthrough of how to run a sample virtual cluster. 
For more information on how they work, see
*http://www.nimbusproject.org/docs/current/clouds/clusters2.html .*

::

::

Cluster Definition File
~~~~~~~~~~~~~~~~~~~~~~~

For this example, we will use a modification of the sample cluster file
that is distributed with the cloud client.  The file can be found at
*https://portal.futuregrid.org/sites/default/files/tutorial-cluster.xml\_.gz *.
Copy the file to where your cloud-client program is located, and unzip
it.  Open the file and make note of the following:

#. There are 2 workspace definitions. 
#. The head node has a quantity of 1 and a base image
   base-cluster-cc14.gz.  It has the roles of providing a nfs server. 
#. The compute-nodes have the same image, but a quantity of 2.  This
   means there will be 1 head node and 2 compute-nodes in the virtual
   cluster.  This has the role of being a nfs client.

Start the Cluster
~~~~~~~~~~~~~~~~~

::

    $ ./bin/cloud-client.sh --conf conf/sierra.conf --run --hours 2 --cluster <path to your cluster document>
    SSH known_hosts contained tilde:
      - '~/.ssh/known_hosts' --> '/N/u/bresnaha/.ssh/known_hosts'

    Requesting cluster.
      - head-node: image 'base-cluster-cc14.gz', 1 instance
      - compute-nodes: image 'base-cluster-cc14.gz', 2 instances

    Context Broker:
        https://s83r.idp.sdsc.futuregrid.org:8443/wsrf/services/NimbusContextBroker

    Created new context with broker.

    Workspace Factory Service:
        https://s83r.idp.sdsc.futuregrid.org:8443/wsrf/services/WorkspaceFactory...

    Creating workspace "head-node"... done.
      - 198.202.120.134 [ vm-40.sdsc.futuregrid.org ]

    Creating group "compute-nodes"... done.
      - 198.202.120.135 [ vm-41.sdsc.futuregrid.org ]
      - 198.202.120.136 [ vm-42.sdsc.futuregrid.org ]

    Launching cluster-004... done.

    Waiting for launch updates.
      - cluster-004: all members are Running
      - wrote reports to '/N/u/bresnaha/tutorial/nimbus-cloud-client-022/history/cluster-004/reports-vm'

    Waiting for context broker updates.
      - cluster-004: contextualized
      - wrote ctx summary to '/N/u/bresnaha/tutorial/nimbus-cloud-client-022/history/cluster-004/reports-ctx/CTX-OK.txt'
      - wrote reports to '/N/u/bresnaha/tutorial/nimbus-cloud-client-022/history/cluster-004/reports-ctx'

    SSH trusts new key for vm-40.sdsc.futuregrid.org   head-node 

    SSH trusts new key for vm-41.sdsc.futuregrid.org   compute-nodes #0 

    SSH trusts new key for vm-42.sdsc.futuregrid.org   compute-nodes #1 

This command takes a bit of time.  What is happening is cloud-client
is instructing Nimbus to start up three VMs on the user's behalf. 
Information is put into the context broker.  When each VM boots, the
context agent is run.  The context agent checks in with the context
broker and asks for information reflecting the *requires* section in the
cluster document; similarly it registers its *provides* information with
the context broker for other VM context agents to query.  The NFS
clients use this mechanism to provide the nfs server with their IP
addresses.  The NFS server then gets this information out of the context
broker and uses it to authorize those IP addresses to remotely mount its
disks. 

 When it is complete, your virtual cluster will be ready to go.

Check Out the Virtual Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now ssh into one of the worker nodes and check out the file system.

::

    $ df -h
    df -h
    Filesystem            Size  Used Avail Use% Mounted on
    /dev/sda1             2.9G  1.2G  1.7G  42% /
    udev                  1.1G  144K  1.1G   1% /dev
    shm                   1.1G     0  1.1G   0% /dev/shm
    198.202.120.134:/home
                          2.9G  1.2G  1.7G  42% /home
    198.202.120.134:/etc/grid-security/certificates
                          2.9G  1.2G  1.7G  42% /etc/grid-security/certificates

Notice the NFS mounted home directory.  Touch a file in that
directory.

::

    $ echo "Hello FutureGrid" > /home/test_file

Now ssh into the other worker node and verify that the test file is
visible to this node as well.

::

    $cat /home/test_file
    Hello FutureGrid





+--------------------------------------------------------------------------------------------------------------+-------------+
| Attachment                                                                                                   | Size        |
+==============================================================================================================+=============+
| `tutorial-cluster.xml\_.gz <https://portal.futuregrid.org/sites/default/files/tutorial-cluster.xml_.gz>`__   | 342 bytes   |
+--------------------------------------------------------------------------------------------------------------+-------------+

-  `Cloud Quick Start : Launch a VM with 1
   command </manual/nimbus/cloud-quick-start-launch-vm-1-command>`__
-  `FutureGrid Tutorial NM2 - Nimbus One-Click Cluster
   Guide </tutorials/nm2>`__

`‹ OpenStack Grizzly on FutureGrid </manual/openstack/grizzly>`__
`up </manual/iaas>`__ `Cloud Quick Start : Launch a VM with 1 command
› </manual/nimbus/cloud-quick-start-launch-vm-1-command>`__

.. |image0| image:: /images/nimbus_logo.png
   :target: http://www.nimbusproject.org/


Launch A VM via Nimbus
======================

It  simple to run a virtual machine (VM) on
FutureGrid Nimbus.  The VM launched will mount your home files system on
hotel so data can be exchanged with the VM easily.  Users new to cloud
computing, particularly those coming from Grid computing, and those who
are interested in getting a quick hands-on introduction to FutureGrid
clouds, should find this useful.

Once you have a FutureGrid Nimbus account and ssh access to
hotel.futuregrid.org, you can easily begin using the cloud.  All you
need to do is ssh into hotel with ssh forwarding enabled, and type a
single command::

    $ ssh -A hotel.futuregrid.org
    $ /soft/nimbus/tools/bin/launch-vm.sh
    Launching your VM (this may take a minute)...
    Success!
    Access your VM with: ssh root@vm-156.uc.futuregrid.org
    Terminate your VM with: /soft/nimbus/tools/bin/cloudinitd.sh terminate 9ec20044

Notice the output from the above command.  It tells you how to access
the VM, and how to clean it up when you are finished with it.  First
let's access the VM and check out its file system.  The VM should have
remotely mounted your home file system on FutureGrid.  This will allow
you to easily copy data in and out of your VM::

    $ ssh root@vm-156.uc.futuregrid.org
    $ vm-156:~# df -h
    Filesystem            Size  Used Avail Use% Mounted on
    tmpfs                 1.1G     0  1.1G   0% /lib/init/rw
    udev                   10M  1.1M  9.0M  11% /dev
    tmpfs                 1.1G     0  1.1G   0% /dev/shm
    rootfs                1.9G  731M  1.1G  42% /
    sshfs#bresnaha@hotel.futuregrid.org:
                         1000G     0 1000G   0% /mnt/hotel.futuregrid.org

    $ ls /mnt/hotel.futuregrid.org
    ..... <a listing of your FutureGrid home directory>

Options
----------------------------------------------------------------------

Using Other Nimbus Clouds on FutureGrid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


By default, the VMs are launched on hotel's Nimbus cloud.  However,
you can use this script to launch a VM on any cloud to which you have
access, including all of FutureGrid's Nimbus clouds, FutureGrid's
Eucalytpus clouds, and FutureGrid's OpenStack clouds.  To run on a
different FutureGrid Nimbus cloud, set the
env \ *CLOUDINITD\_IAAS\_URL* to one of the following:

-  Hotel KVM:
   `https:/login1.uc.futuregrid.org:8444 <https://login1.uc.futuregrid.org:8444>`__
-  Hotel Xen:
   `https://svc.uc.futuregrid.org:8444 <https://svc.uc.futuregrid.org:8444>`__
-  Sierra:
   `https://s83r.idp.sdsc.futuregrid.org:8444 <https://s83r.idp.sdsc.futuregrid.org:8444>`__
-  Foxtrot:
   `https://f1r.idp.ufl.futuregrid.org:9444 <https://f1r.idp.ufl.futuregrid.org:9444>`__
-  Alamo:
   `https://nimbus.futuregrid.tacc.utexas.edu:8444 <https://nimbus.futuregrid.tacc.utexas.edu:8444>`__

Launching Multiple VMs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To launch many VMs at once, set the env
*CLOUDINITD\_SSHFS\_REPLICA\_COUNT* to the Number of VMs that you would
like launched

Using with Eucalyptus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use the tool with Eucalyptus, the following envs must be
set:

-  export
   CLOUDINITD\_IAAS\_URL='http://149.165.146.135:8773/services/Eucalyptus'
-  export CLOUDINITD\_IAAS\_ACCESS\_KEY=<your access key>
-  export CLOUDINITD\_IAAS\_SECRET\_KEY=<your access secret>
-  export CLOUDINITD\_IAAS\_IMAGE='emi-5F4F1B49'
     

You may have trouble registering your keys.  This is due to Eucalyptus
not yet supporting the latest version of the EC2 API.  To circumvent
this, create a key pair named 'futuregrid', and set the env
*CLOUDINITD\_IAAS\_SSHKEYNAME*\ to 'futuregrid'.  Then, set the env
*CLOUDINITD\_IAAS\_SSHKEY* to point to the private key associated with
that key name.

What Happens
----------------------------------------------------------------------

This script uses the program cloudinit.d
(`http://www.nimbusproject.org/doc/cloudinitd/latest/) <http://www.nimbusproject.org/doc/cloudinitd/latest/>`__. 
This is a Nimbus Platform multi-cloud tool for running cloud
applications.  In this case, it runs a very simple 1 VM application.  It
can launch any debian-based VM and install sshfs on it.  Then it runs
sshfs inside of the VM to remotely mount your FutureGrid home directory.

`‹ Using Nimbus on FutureGrid </tutorials/nimbus>`__
`up </tutorials/nimbus>`__ `FutureGrid Tutorial NM2 - Nimbus One-Click
Cluster Guide › </tutorials/nm2>`__


cloudinit.d
======================================================================

cloudinit.d is a tool designed for launching, controlling, and
monitoring complex environments in the cloud.
 Its most important feature is repeatable, one-click, deployment of sets
of VMs configured with launch plans.  These sets of VMs can be deployed
over multiple clouds (Eucalyptus, Nimbus, OpenStack, and Amazon EC2 are
currently supported), and can also include non-virtualized resources.
Like the Unix init.d process, cloudinit.d can manage dependencies
between deployed VMs. It also provides mechanisms for testing,
monitoring, and repairing a launch.
 For more information about cloudinit.d, see our \ `Teragrid 2011
paper <http://www.nimbusproject.org/files/cloudinitd_tg11_submit3c.pdf>`__. For
repeatable experiment management with cloudinit.d, read the \ `report
on <http://www.nimbusproject.org/downloads/Supporting_Experimental_Computer_Science_final_draft.pdf>`__ `support
for experimental computer
science <http://www.nimbusproject.org/downloads/Supporting_Experimental_Computer_Science_final_draft.pdf>`__.
`‹ Precip - Pegasus Repeatable Experiments for the Cloud in
Python </manual/precip>`__ `up </manual/management-services>`__ `Grid
Services › </manual/grid-services>`__


Phantom
==================================================

Nimbus Phantom is a hosted service running on FutureGrid that makes it
easy to leverage on-demand resources provided by infrastructure clouds.
Phantom allows the user to deploy a set of virtual machines over
multiple private, community, and commercial clouds, and then
automatically grows or shrinks this set based on policies defined by the
user. This elastic set of virtual machines can then be used to implement
scalable and highly available services. An example of such a service is
a caching service that stands up more workers on more resources as the
number of requests to the service increases. Another example is a
scheduler that grows its set of resources as demand grows.

Currently Phantom works with all FutureGrid Nimbus and OpenStack
clouds as well as Amazon and the XSEDE wispy cloud (the only XSEDE cloud
for now). A user can access it via two types of clients: an easy-to-use
web application and a scripting client. The scripting client is the boto
autoscale client as Phantom currently implements Amazon Autscaling API –
so you can think of it as Amazon Autoscale for FutureGrid clouds that
also allows for cloudburst to XSEDE and commercial clouds and is easy to
extend with your own policies and sensors.

The simplest scenario for using Phantom is as a gateway for deploying
and monitoring groups of virtual machines spread over multiple
FutureGrid clouds. In a more complex scenario you can use it to
cloudburst from FutureGrid clouds to Amazon. Finally, you can use it to
explore policies that will automate cloudbursting and VM allocations
between multiple clouds.

For more information and/or to use the service, go to
`www.nimbusproject.org/phantom <http://www.nimbusproject.org/phantom>`__.
It should take no more than 10-15 minutes to start your own VMs.

-  `Phantom web
   interface <https://phantom.nimbusproject.org/accounts/login/?next=/>`__
-  `Phantom
   publication <http://www.nimbusproject.org/files/keahey_wcs_ocs_2012.pdf>`__

`‹ Management Services </manual/management-services>`__
`up </manual/management-services>`__ `Precip - Pegasus Repeatable
Experiments for the Cloud in Python › </manual/precip>`__
