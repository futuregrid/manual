.. _s-twister-appliance:

**********************************************************************
FG Twister Appliance Tutorial
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:



I. Introduction
~~~~~~~~~~~~~~~

| This tutorial will demonstrate how to setup a private cluster for a
Twister appliance on FutureGrid.
|  

II. Prerequisites
~~~~~~~~~~~~~~~~~

1. Setting up GroupVPN for Creating a Virtual Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the process of creating a virtual private network (VPN)
interconnecting your virtual machine instances in order to form a
virtual cluster.
`GroupVPN <http://www.grid-appliance.org/wiki/index.php/GroupVPN>`__ is
a group secured VPN network using the
`IPOP <http://www.grid-appliance.org/wiki/index.php/IPOP>`__ IP-over-P2P
virtual network to create virtual clusters for running parallel and
batch applications. GroupVPN can be used to easily consolidate physical
machines, virtual machine instances, and cloud instances into a single
virtual cluster.

Click
`here <http://www.grid-appliance.org/index.php?option=com_user&view=register>`__
to create an account at
`www.grid-appliance.org <http://www.grid-appliance.org/>`__.

2. Set up a GroupVPN
^^^^^^^^^^^^^^^^^^^^

Log into `www.grid-appliance.org <http://www.grid-appliance.org/>`__.
Follow the instructions at `GroupVPN Web User
Interface <http://www.grid-appliance.org/wiki/index.php/GroupVPN#GroupVPN_Web_User_Interface>`__
and configure a GroupVPN with the desired configuration.

3. Set up a Group Appliance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The grid appliance website allows for the creation of floppy disks with
the configuration files required by GroupVPN. To do this, follow the
instruction
`here <http://www.grid-appliance.org/index.php?option=com_content&view=article&id=79&Itemid=76#floppy>`__.

4. Choose the Twister Grid Appliance Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Choose a gridappliance image: a Twister grid appliance image
(emi-F0B8194D) has been tailored for FutureGrid. Deploy as many nodes
preferable in private cluster. For information on how to access
Eucalyptus features, follow the
`tutorial <../../tutorials/eucalyptus>`__.

III. Deploying a grid appliance connected to your own pool using GroupVPN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To connect to any other
`GroupVPN <http://www.grid-appliance.org/wiki/index.php/GroupVPN>`__
pool, place a floppy disk containing the GroupVPN configuration files
inside the appliance in the /opt/grid\_appliance/etc directory and
restart the grid appliance service. This floppy can be generated using
the grid `appliance.org <http://appliance.org/>`__ web front-end. In the
case of executing a private cluster for a Twister appliance, download
the server and worker floppies. Designate one node as the server and the
remaining nodes as workers. The steps for starting and stopping the grid
appliance service are as outlined below:

#. Stop the grid\_appliance service in the grid-appliance
    /etc/init.d/
    
   grid\_appliance.sh
   stop
   exit
    
#. Download the GroupVPN floppy to your local system from the
   grid-appliance website. Transfer it to the Grid Appliance workspace
   using scp or sftp.
    
   scp - i userkey.private floopy.img (server)
   root@public.ip.address:/opt/grid\_appliance/etc/
    scp - i userkey.private floopy.img (worker)
   root@public.ip.address:/opt/grid\_appliance/etc/
    
    
#. SSH back into grid appliance and start the grid appliance service
    ssh -i userkey.private root@public.ip.address
   /etc/init.d/grid\_appliance.sh start

IV. Setup Twister Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Edit **$TWISTER\_HOME/bin/twister.properties** and set the correct
paths to the following:

**nodes\_file** = /opt/Twister/bin/nodes

**app\_dir** = /opt/Twister/apps

**data\_dir** = /opt/Twister/data

**pubsub\_broker** = Naradabrokering

| 2. Edit **$TWISTER\_HOME/bin/nb.properties** and set **broker\_host**
= (to the IP address on the tapipop interface of the machine you
designated as the server)
|  3. Edit **$TWISTER\_HOME/bin/nodes** and add your IP addresses on the
tapipop interface of the machines you designated as workers.

V. Twister-Kmeans
~~~~~~~~~~~~~~~~~

Open two terminals - One for starting the broker and the second for
starting Twister.

For steps 2 - 4, execute the following commands on the second terminal.

1. Start Twister and Naradabrokering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Terminal 1:

| $ cd /opt/Naradabrokering/bin/
|  $ chmod 755 startbr.sh
|  $ ./startbr.sh

In Terminal 2: 
| $ cd /opt/Twister/bin
|  $ chmod 755 start\_twister.sh
|  $ ./start\_twister.sh

2. Ant  Twister-Kmeans
^^^^^^^^^^^^^^^^^^^^^^

| $ cd /opt/Twister/samples/kmeans
|  $ ant
|  $ cd ../../lib
|  $ mv Twister-Kmeans-0.9.jar ../apps/

3. Create Twister-Kmeans Data Folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| $ cd /opt/Twister/bin
|  $ ./twister.sh mkdir kmeans

4. Generate Twister-Kmeans Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| $ cd /opt/Twister/samples/kmeans/bin/
|  $./gen\_data.sh init\_clusters.txt 2 3 kmeans km\_data 3 30000

$ ./create\_partition\_file.sh kmeans km
../samples/kmeans/bin/\ `p.pf <http://p.pf/>`__

Execute Twister-Kmeans application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

$ ./run\_kmeans.sh init\_clusters.txt 3 `p.pf <http://p.pf/>`__

The output is as follows:

|image1|

A video detailing the above steps can be shown
`here <https://www.slashtmp.iu.edu/files/download?FILE=jeromitc%2F76089Sok5vi>`__
password: tutorial

