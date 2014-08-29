.. sidebar:: Page Contents

   .. contents::
      :local:

.. _s-iaas:

IaaS
======================================================================


Nimbus Clouds
----------------------------------------------------------------------

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

-  :portal:`Using Nimbus on
   FutureGrid <tutorials/nimbus>` [novice]
-  :portal:`Nimbus One-click Cluster
   Guide <tutorials/nm2>` [intermediate]

OpenStack Clouds
----------------------------------------------------------------------

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

-  `Using OpenStack Nova on FutureGrid <openstackhavana>`_ [novice]

   -  This tutorial targets all users of OpenStack in FutureGrid; it
      describes how to get started with FutureGrid OpenStack resources.

-  :portal:`Running an OpenStack virtual appliance on
   FutureGrid <tutorials/os1>` [novice]

   -  This tutorial targets users interested in education and training
      on OpenStack internals; it describes how to run a virtual, private
      OpenStack deployment as an appliance.

Eucalyptus Clouds
----------------------------------------------------------------------

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

-  :ref:`Using Eucalyptus on
   FutureGrid <s-eucalyptus>` [novice]



Virtual Appliances for Training and Education
----------------------------------------------------------------------

The IaaS cloud stacks on FutureGrid enable the use of "virtual
appliances" as an environment where hands-on, executable educational and
training modules can be created, shared, and leveraged by the FutureGrid
community. With these appliances, students are able to deploy virtual
machines and virtual private clusters, where they are able to experiment
with various Grid and cloud computing middleware stacks.

For tutorials on getting started with educational virtual appliances,
see:


-  :portal:`Running a Grid Appliance on your
   desktop <tutorials/ga1>`  [novice]
-  :portal:`Running a Grid Appliance on
   FutureGrid <tutorials/ga9>` [novice]
-  :portal:`Running Condor tasks on the Grid
   Appliance <tutorials/ga8>` [novice]
-  :portal:`Running MPI tasks on the Grid
   Appliance <tutorials/mp1>` [novice]
-  :portal:`Running Hadoop tasks on the Grid
   Appliance <tutorials/ga10>` [novice]
-  :portal:`Running an OpenStack virtual appliance on
   FutureGrid <tutorials/os1>` [novice]
