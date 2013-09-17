.. _s-vine-overlay:

Vine Overlay
==========================================================

This tutorial provides instructions on how to take advantage of ViNe to
connect VMs deployed through Nimbus on sierra and foxtrot.

ViNe is a user-level virtual networking middleware that establishes
wide-area virtual networks supporting symmetric communication among
public and private network resources. ViNe is particularly useful when
deploying virtual clusters spanning multiple clouds with VMs on private
networks.

Prerequisite
------------

This procedure requires familiarity with launching virtual machines
with Nimbus—specifically, how to set up and use the Nimbus cloud client
and credentials (see :ref:`s-nimbus`).

.. sidebar:: Hint 
   All commands should be issued from the cloud-client
   directory, and that all nimbus configuration files are also
   installed in the cloud-client conf directory (i.e., cd
   $HOME/nimbus-cloud-client-021, if cloud-client version 0.21 is
   installed on the users' home directory).

Deploying a virtual cluster across foxtrot and sierra
---------------------------------------------------------

Below is a simple example on how to construct a cluster spanning two
administrative domains, sierra and foxtrot (we will use a private
network on foxtrot). One VM in each site will be used.

.. sidebar:: Hint 
   Users interested in larger clusters can use the Nimbus
   “one-click cluster” feature described in this
   `tutorial <https://portal.futuregrid.org/tutorials/nm2>`__.

“centos-5.5-x64-vine.gz” is a VM image that, when booted, automatically
connects VMs to ViNe. Launch one instance on sierra and foxtrot (note
that, by default, VMs on foxtrot use a private network).

Before launching on each site, make sure that the
*centos-5.5-x64-vine.gz* image is included in the local image pool. You
can verify that the image is available using::

    $ ./bin/cloud-client.sh --list --conf conf/sierra.conf
    $ ./bin/cloud-client.sh --list --conf conf/foxtrot.conf
    ...
    [Image] ' centos-5.5-x64-vine.gz '           Read only
            Modified: Jul 5 2011 @ 14:40   Size: 676457559 bytes (~645 MB)
    ...

Launch two VMs (one on sierra, and one on foxtrot)::

    $ ./bin/cloud-client.sh --run --hours 1 --name centos-5.5-x64-vine.gz --conf conf/sierra.conf

    Launching workspace.

    Workspace Factory Service:
       https://s83r.idp.sdsc.futuregrid.org:8443/wsrf/services/WorkspaceFactory...

    Creating workspace "vm-020"... done.


           IP address: 198.202.120.121
             Hostname: vm-27.sdsc.futuregrid.org
           Start time: Fri Jul 15 15:25:36 EDT 2011
        Shutdown time: Fri Jul 15 16:25:36 EDT 2011
     Termination time: Fri Jul 15 16:27:36 EDT 2011

    Waiting for updates.


    "vm-020" reached target state: Running

    Running: 'vm-020'

::

    $ ./bin/cloud-client.sh --run --hours 1 --name centos-5.5-x64-vine.gz --conf conf/foxtrot.conf

    Launching workspace.

    Workspace Factory Service:
        https://f1r.idp.ufl.futuregrid.org:9443/wsrf/services/WorkspaceFactorySe...

    Creating workspace "vm-019"... done.


           IP address: 172.31.10.102
             Hostname: fvm2.nimbus.ufl.futuregrid.intranet
           Start time: Fri Jul 15 15:23:13 EDT 2011
        Shutdown time: Fri Jul 15 16:23:13 EDT 2011
     Termination time: Fri Jul 15 16:25:13 EDT 2011

    Waiting for updates.


    "vm-019" reached target state: Running

    Running: 'vm-019'

ViNe is necessary here because, without it, nodes on sierra have no way
to ssh into foxtrot private IPs. In order to enable the communication
with nodes on foxtrot, ViNe must be enabled on both foxtrot and sierra
VMs. ViNe is enabled through the following command, which is already
included in the *rc.local* file of *centos-5.5-x64-vine.gz*::

    wget -P /tmp -N http://vine.acis.ufl.edu/vine/enablevine.php
    . /tmp/enablevine.sh

We now get a virtual cluster that offers full connectivity among all
VMs. Log in to the VM on sierra, and verify  you can directly access the
VM on foxtrot (with a private IP)::

    $ ssh root@198.202.120.121
    Last login: Fri Jul  1 17:39:51 2011 from 172.31.10.34
    -bash-3.2#
    -bash-3.2# ping -c 3 172.31.10.102
    PING 172.31.10.102 (172.31.10.102) 56(84) bytes of data.
    64 bytes from 172.31.10.102: icmp_seq=1 ttl=63 time=66.6 ms
    64 bytes from 172.31.10.102: icmp_seq=2 ttl=63 time=64.4 ms
    64 bytes from 172.31.10.102: icmp_seq=3 ttl=63 time=64.4 ms

    --- 172.31.10.102 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 1999ms
    rtt min/avg/max/mdev = 64.424/65.172/66.661/1.092 ms
    -bash-3.2#


