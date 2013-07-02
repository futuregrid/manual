**********************************************************************
IaaS
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

.. todo:: update links 
.. todo:: update links to manual pages of rst doc

Nimbus Clouds
--------------

Nimbus is an open-source service package that allows users to run
virtual machines on FutureGrid hardware. You can easily upload your own
VM image or customize an image provided by us. When you boot a VM, it is
assigned a public IP address (and/or an optional private address), and
you are authorized to log in as root via SSH. You can then run services,
perform computations, and configure the system as desired.

Nimbus is available across various FutureGrid sites, and there are
two open-source hypervisors in use in FutureGrid Nimbus clouds: Xen and
KVM. Nimbus in FutureGrid is the recommended platform if you are
interested in experiments within a cloud, across clouds, or in those not
amenable to para-virtualization, as the Nimbus/KVM cloud (alamo)
supports "classic" virtual machines.

For tutorials on getting started with Nimbus, see:

-  `Using Nimbus on
   FutureGrid <https://portal.futuregrid.org/tutorials/nimbus>`__ [novice]
-  `Nimbus One-click Cluster
   Guide <https://portal.futuregrid.org/tutorials/nm2>`__ [intermediate]

OpenStack Clouds
----------------

`OpenStack <http://www.openstack.org/>`__ is a recently open-sourced,
IaaS cloud computing platform founded by Rackspace Hosting and NASA, and
used widely in industry. It includes three components: Compute(Nova),
Object Storage (Swift), and Image Service (Glance). OpenStack Nova
supports an  Amazon Web Services (AWS) complaint EC2-based web service
interface for interacting with the Cloud service, and can be used with
the same client-side "eucatools" that is used with Eucalyptus.

FutureGrid currently features the OpenStack Nova compute cloud. 
OpenStack Nova in FutureGrid is useful if you are interested in
experiments within a cloud, and in comparison of cloud middleware
stacks.

For tutorials on getting started with OpenStack, see:

-  `Using OpenStack Nova on
   FutureGrid <https://portal.futuregrid.org/tutorials/openstack>`__ [novice]

   -  This tutorial targets all users of OpenStack in FutureGrid; it
      describes how to get started with FutureGrid OpenStack resources.

-  `Running an OpenStack virtual appliance on
   FutureGrid <https://portal.futuregrid.org/tutorials/os1>`__ [novice]

   -  This tutorial targets users interested in education and training
      on OpenStack internals; it describes how to run a virtual, private
      OpenStack deployment as an appliance.

Eucalyptus Clouds
-----------------

Eucalyptus is an open-source software platform that implements
IaaS-style cloud computing. Eucalyptus provides an Amazon Web Services
(AWS) complaint EC2-based web service interface for interacting with the
Cloud service. Additionally, Eucalyptus provides services such as the
AWS Complaint Walrus and a user interface for managing users and
images.

Eucalyptus is also available on distributed FutureGrid resources.
Eucalyptus in FutureGrid is useful if  you are interested in experiments
within a cloud, across clouds, and in comparison of cloud middleware
stacks.

For tutorials on getting started with Eucalyptus, see:

-  `Using Eucalyptus on
   FutureGrid <https://portal.futuregrid.org/tutorials/eucalyptus3>`__ [novice]



Virtual Appliances for Training and Education
---------------------------------------------

The IaaS cloud stacks on FutureGrid enable the use of "virtual
appliances" as an environment where hands-on, executable educational and
training modules can be created, shared, and leveraged by the FutureGrid
community. With these appliances, students are able to deploy virtual
machines and virtual private clusters, where they are able to experiment
with various Grid and cloud computing middleware stacks.

For tutorials on getting started with educational virtual appliances,
see:


-  `Running a Grid Appliance on your
   desktop <https://portal.futuregrid.org/tutorials/ga1>`__  [novice]
-  `Running a Grid Appliance on
   FutureGrid <https://portal.futuregrid.org/tutorials/ga9>`__ [novice]
-  `Running Condor tasks on the Grid
   Appliance <https://portal.futuregrid.org/tutorials/ga8>`__ [novice]
-  `Running MPI tasks on the Grid
   Appliance <https://portal.futuregrid.org/tutorials/mp1>`__ [novice]
-  `Running Hadoop tasks on the Grid
   Appliance <https://portal.futuregrid.org/tutorials/ga10>`__ [novice]
-  `Running an OpenStack virtual appliance on
   FutureGrid <https://portal.futuregrid.org/tutorials/os1>`__ [novice]
