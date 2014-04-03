Summary:
~~~~~~~~

This tutorial provides step-by-step instructions for deploying a Grid
Appliance on FutureGrid. The Grid Appliance can be used as a basis for
running a variety of educational, training, and outreach activities.

Prerequisites:
~~~~~~~~~~~~~~

-  The `Introduction to the Grid
   Appliance <https://portal.futuregrid.org/tutorials/ga1>`__ tutorial
   is not a requirement, but provides hands-on experience with a Grid
   appliance on your desktop.
-  Depending on whether you plan to use Nimbus or OpenStack, one of the
   following tutorials is required:

   -  `Using Nimbus
      on FutureGrid <https://portal.futuregrid.org/tutorials/nimbus>`__
   -  `Using OpenStack
      on FutureGrid <https://portal.futuregrid.org/tutorials/openstack>`__
   -  `Using OpenStack Grizzly on
      FutureGrid <https://portal.futuregrid.org/manual/openstack/grizzly>`__

Deploying a Grid Appliance on FutureGrid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| This tutorial assumes you have an account on FutureGrid and have gone
through the prerequisite tutorials for Nimbus or OpenStack. Once you
complete these simple steps, later on you will have the ability to
deploy your own private Grid appliance clusters on FutureGrid resources,
as well as on your own resources, to use in your courses or research.

-  Using Nimbus

   A Nimbus Grid appliance image with all required packages has been
   created at TACC's cluster (Alamo) with KVM virtualization technology.
   The image name is "grid-appliance-2.05.03.gz" and it is available to
   all FutureGrid users.

   #. Use
      the \ `Nimbus cloud-client.sh client <https://portal.futuregrid.org/tutorials/nimbus>`__ to
      deploy a Grid appliance on Alamo::

          ./bin/cloud-client.sh --conf conf/alamo.conf --run --name grid-appliance-2.05.03.gz --hours 24

   #. Wait until Nimbus tells you the machine is running; log into the
      Grid appliance using ssh, with the IP address given by Nimbus
      (129.114.x.y in this example)::

          ssh root@129.114.x.y

-  Using OpenStack on india

   #. An image with all required packages has been created; it is
      available to all FutureGrid users in the "india" cloud resource.
      To deploy the VM, use the command below (replacing "mykey" with
      your appropriate key)::

          euca-run-instances -k mykey ami-00000177

      Check the status of your instance as described in the OpenStack
      tutorial; once the instance has an IP address, log into it with
      ssh  (149.165.x.y in this example)::

          ssh -i mykey.pem root@149.165.x.y

-  Using OpenStack on sierra

   #. An image with all required packages is also available to
      all FutureGrid users in the "sierra" cloud resource. To deploy the
      VM, use the command::

          nova boot --flavor m1.small --image "grid-appliance/grid-appliance-2.05.04" --key_name $LOGNAME-key $LOGNAME-001

      Check the status of your instance as described in the OpenStack tutorial; once the instance has an IP address, log into it with ssh  (10.35.x.y in this example)::

          ssh -i .ssh/$LOGNAME-key root@10.35.x.y


   Running Tasks - Condor, MPI, Hadoop

-  At this point, you are connected to a Unix shell in the Grid
   appliance, and can use it to run tasks through Condor, Hadoop or MPI.
   Follow the steps outlined in the appropriate tutorial(s) found on the
   `main tutorials page <http://portal.futuregrid.org/tutorials>`__. 


.. |image1| image:: /sites/default/files/images/nsf-logo.png
   :target: http://www.tacc.utexas.edu/
.. |image2| image:: /sites/default/files/u876/xsede-logo.png
