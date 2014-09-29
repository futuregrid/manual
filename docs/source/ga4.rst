.. _s-ga4:

**********************************************************************
GA4: Deploying Virtual Private Grid Appliance Clusters Using Nimbus
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

**Summary:**
------------

This tutorial provides step-by-step instructions on how to deploy virtual private Grid Appliances on FutureGrid using Nimbus.
 

**Prerequisites:**
------------------

:ref:`Introduction to Nimbus <nimbus>`

:ref:'Running a Grid Appliance on FutureGrid <s-ga9>`



**Hands-On Tutorial**:
----------------------

**1. Getting Started**
~~~~~~~~~~~~~~~~~~~~~~

*1.1 Start up a Grid appliance on Nimbus*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instantiate a Grid Appliance on FutureGrid using Nimbus - refer to the pre-requisite tutorials listed above for instructions.  


**2. Generate a virtual floppy and upload to Grid Appliance**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the appliance reaches "running" state, its hostname/IP address will be displayed. To log into the Grid Appliance, ssh using the root user:
::

     $ ssh root@<grid_appliance.cloudurl.edu>

The appliance is configured to connect automatically to a default shared pool upon start-up when it is instantiated using the cloud-client. To connect the appliance to a different pool (e..g a private pool for you, your group, or your class) it
needs \ `GroupVPN <http://www.grid-appliance.org/wiki/index.php/GroupVPN>`__ and
`GroupAppliance <http://www.grid-appliance.org/wiki/index.php/GroupAppliances>`__
configuration from a group at the Grid appliance web site. 

To connect to any other GroupVPN pool, you need to place a floppy disk containing the GroupVPN configuration files inside the appliance in the /opt/grid\_appliance/etc directory and then restart the grid\_appliance service. This floppy is generated using the grid-appliance.org web front-end following the steps described in the following pages:

-  Create/Join a GroupVPN following instructions on the `GroupVPN Wiki
   page <http://www.grid-appliance.org/wiki/index.php/GroupVPN>`__
-  Create/join a GroupAppliance following instructions on the
   `GroupAppliance Wiki
   page <http://www.grid-appliance.org/wiki/index.php/GroupAppliances>`__.

Once you have created and downloaded a GroupAppliance floppy, the steps to load them into your Nimbus instances are as outlined below:

1. Download a "server" GroupAppliance floppy to your local system from the grid-appliance.org website, and unzip it to extract a file "floppy.img". Transfer it to the Grid Appliance workspace using scp or sftp:
::

     $ scp ./floopy.img root@<grid_appliance.cloudurl.edu>:/opt/grid_appliance/etc/

2. SSH back into Grid Appliance and re-start the Grid Appliance service:
::

     $ ssh root@<grid_appliance.cloudurl.edu>
     # /etc/init.d/grid_appliance.sh re-start

3. Download a "worker" GroupAppliance floppy to your local system from the grid-appliance.org website, and unzip it. Repeat steps 1 and 2 for the other cluster nodes, using this "Worker" version of the appliance virtual floppy.
 
**3. Notes:**
~~~~~~~~~~~~~

The uploading of GroupAppliance floppies can be automated to take place at instantiation time, through the use of lower-level workspace scripts. Documentation on this procedure will be added when this feature becomes available.

Currently, Grid appliances on Nimbus are supported on FutureGrid
resources that run KVM virtualization (alamo at Texas). As additional platforms become available, tihs tutorial will be updated.

**Reference material:**
-----------------------

Presentation: `Deploying Grid Appliance
clusters <http://www.grid-appliance.org/files/docs/edu-docs/LocalGridAppliance1.pdf>`__

Videos: `Grid Appliance YouTube
channel <http://www.youtube.com/acisp2p#p/c/D77781CEF51F72F3>`__


**Authors:**
------------

Arjun Prakash, Renato Figueiredo, University of Florida