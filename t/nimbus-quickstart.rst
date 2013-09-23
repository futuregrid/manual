**********************************************************************
Nimbus -  Virtual Cluster
**********************************************************************

This page explains how to very simply run a virtual machine (VM) on
FutureGrid Nimbus.  The VM launched will mount your home files system on
hotel so data can be exchanged with the VM easily.  Users new to cloud
computing, particularly those coming from Grid computing, and those who
are interested in getting a quick hands-on introduction to FutureGrid
clouds, should find this useful.

Launch A VM via Nimbus
======================

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
=======

Using Other Nimbus Clouds on FutureGrid
---------------------------------------

By default, the VMs are launched on hotel's Nimbus cloud.  However,
you can use this script to launch a VM on any cloud to which you have
access, including all of FutureGrid's Nimbus clouds, FutureGrid's
Eucalytpus clouds, and FutureGrid's OpenStack clouds.  To run on a
different FutureGrid Nimbus cloud, set the
env \ *CLOUDINITD\_IAAS\_URL* to one of the following:

-  Hotel:
   `https://svc.uc.futuregrid.org:8444 <https://svc.uc.futuregrid.org:8444>`__
-  Sierra:
   `https://s83r.idp.sdsc.futuregrid.org:8444 <https://s83r.idp.sdsc.futuregrid.org:8444>`__
-  Foxtrot:
   `https://f1r.idp.ufl.futuregrid.org:9444 <https://f1r.idp.ufl.futuregrid.org:9444>`__
-  Alamo:
   `https://nimbus.futuregrid.tacc.utexas.edu:8444 <https://nimbus.futuregrid.tacc.utexas.edu:8444>`__

Launching Multiple VMs
----------------------

To launch many VMs at once, set the env
*CLOUDINITD\_SSHFS\_REPLICA\_COUNT* to the Number of VMs that you would
like launched

Using with Eucalyptus
---------------------

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
============

This script uses the program cloudinit.d
(`http://www.nimbusproject.org/doc/cloudinitd/latest/) <http://www.nimbusproject.org/doc/cloudinitd/latest/>`__. 
This is a Nimbus Platform multi-cloud tool for running cloud
applications.  In this case, it runs a very simple 1 VM application.  It
can launch any debian-based VM and install sshfs on it.  Then it runs
sshfs inside of the VM to remotely mount your FutureGrid home directory.

`‹ Using Nimbus on FutureGrid </tutorials/nimbus>`__
`up </tutorials/nimbus>`__ `FutureGrid Tutorial NM2 - Nimbus One-Click
Cluster Guide › </tutorials/nm2>`__
