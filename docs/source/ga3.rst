.. _s-ga3:

**********************************************************************
Building an Educational Appliance from Ubuntu 10.04
**********************************************************************

This is a short tutorial describing how to build an educational virtual cluster appliance starting from an Ubuntu 10.04 image. A more detailed description is given at \ `Testing Grid
Appliance <http://www.grid-appliance.org/wiki/index.php/TestingGridAppliance>`__.



#. Deploy an Ubuntu 10.04 appliance locally. You can download an Ubuntu
   9.10 VMware appliance \ `here <http://vmplanet.net/node/105>`__, or
   create an instance on FutureGrid of an Ubuntu 10.04 VM.
     
#. Sudo to root and install the grid-appliance baseline package as
   follows:

   #. apt-get install wget
   #. echo "deb http://www.grid-appliance.org/files/packages/deb/ lucid
      contrib" >> /etc/apt/sources.list
   #. wget http://www.grid-appliance.org/files/packages/deb/repo.key
   #. apt-key add repo.key
   #. apt-get update
   #. apt-get install grid-appliance-base
       

#. To configure the appliance to connect to a GroupVPN, use one of the
   following two options:

   #. To use a default GroupVPN and connect to a public pool hosted at
      UF, simply install the package apt-get-install
      grid-appliance-public-pool.
   #. To use our defined Group:

      #. Create a GroupVPN and GroupAppliance
         at \ `http://grid-appliance.org <http://grid-appliance.org/>`__ .
         For an example, see \ `Deploying independent appliance
         pools <http://www.grid-appliance.org/index.php?option=com_content&view=article&id=79&Itemid=76>`__.
      #. In the GroupAppliance interface, download and extract the
         floppy configuration file for a client (floppy.img) and place
         it in/opt/grid\_appliance/etc/floppy.img .
      #. /etc/init.d/grid\_appliance.sh restart 

#. Within a few seconds, your appliance should obtain a virtual IP address on the virtual network interface tapipop. Once it does, wait a few seconds and type condor\_status to check the status of other nodes in the pool; you may need to retry a couple of times until connected.