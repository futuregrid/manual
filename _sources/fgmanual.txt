===========
USER MANUAL
===========

 

|image0|
  
========

FutureGrid User Manual
======================

Gregor von Laszewski, Fugang Wang, Javier Diaz, Archit Kulshrestha,
Jonathan Bolte, and many more


Pervasive Technology Institute, Indiana University, Bloomington, IN
47408, U.S.A.

.. note:: 
Please
    If your name is missing in the author list, please add it, or
    send mail to `laszewski@gmail.com <mailto:laszewski@gmail.com>`__
    Many other \ `staff <https://portal.futuregrid.org/staff>`__ members
    have contributed to the FutureGrid project.


This material is based upon work supported in part by the National
Science Foundation under Grant No. 0910812 to Indiana University for
"FutureGrid: An Experimental, High-Performance Grid Test-bed." Partners
in the FutureGrid project include U. Chicago, U. Florida, San Diego
Supercomputer Center - UC San Diego, U. Southern California, U. Texas at
Austin, U. Tennessee at Knoxville, U. of Virginia, Purdue I., and T-U.
Dresden. -Or the shorter- This material is based upon work supported in
part by the National Science Foundation under Grant No. 0910812.




Preface
=======

| 
|  FutureGrid is a project led by Indiana University and funded by the
National Science Foundation (NSF) to develop a high-performance grid
test bed that will allow scientists to collaboratively develop and test
innovative approaches to parallel, grid, and cloud computing.
 FutureGrid will provide the infrastructure to researchers that allows
them to perform their own computational experiments using distributed
systems. The goal is to make it easier for scientists to conduct such
experiments in a transparent manner.

FutureGrid users will be able to deploy their own hardware and software
configurations on a public/private cloud, and run their experiments.
They will be able to save their configurations and execute their
experiments using the provided tools. The FutureGrid test bed is
composed of a high-speed network connecting distributed clusters of high
performance computers. FutureGrid will employ virtualization technology
that will allow the test bed to support a wide range of operating
systems.

| The NSF awarded $10.1 million to enable joint development of
FutureGrid through a partnership of Indiana University, Purdue
University, University of California - San Diego, University of
Chicago/Argonne National Labs, University of Florida, University of
Southern California, University of Texas, and the Center for Information
Services and High Performance Computing at Technische Universität
Dresden. The principal investigator is Dr. Geoffrey C. Fox, Director of
the \ `Digital Science Center <http://pti.iu.edu/dsc>`__ at the
IU \ `Pervasive Technology Institute <http://pti.iu.edu/>`__.
|   

Citation
--------

If you use FutureGrid, we ask you kindly to include the following
reference in your papers:

`Fox, G. <https://portal.futuregrid.org/biblio/author/11>`__, \ `G. von
Laszewski <https://portal.futuregrid.org/biblio/author/1>`__, \ `J.
Diaz <https://portal.futuregrid.org/biblio/author/61>`__, \ `K.
Keahey <https://portal.futuregrid.org/biblio/author/3>`__, \ `J.
Fortes <https://portal.futuregrid.org/biblio/author/18>`__, \ `R.
Figueiredo <https://portal.futuregrid.org/biblio/author/43>`__, \ `S.
Smallen <https://portal.futuregrid.org/biblio/author/24>`__, \ `W.
Smith <https://portal.futuregrid.org/biblio/author/16>`__, and \ `A.
Grimshaw <https://portal.futuregrid.org/biblio/author/17>`__, "`FutureGrid
- a reconfigurable testbed for Cloud, HPC and Grid
Computing <https://portal.futuregrid.org/references/futuregrid-recon-figurable-testbed-cloud-hpc-and-grid-computing>`__\ ", Contemporary
High Performance Computing: From Petascale toward Exascale, April, 2013.
Editor J.
Vetter. Download: `vonLaszewski-fg-bookchapter.pdf <https://portal.futuregrid.org/biblio/view/2034>`__

Acknowledgement
---------------

The FutureGrid project is funded by the National Science Foundation
(NSF) and is led by \ `Indiana
University <http://www.iub.edu/>`__ with `University of
Chicago <http://www.uchicago.edu/index.shtml>`__, \ `University of
Florida <http://www.ufl.edu/>`__, \ `San Diego Supercomputing
Center <http://www.sdsc.edu/>`__, \ `Texas Advanced Computing
Center <http://www.tacc.utexas.edu/>`__, \ `University of
Virginia <http://www.virginia.edu/>`__,\ `University of
Tennessee <http://www.utk.edu/>`__, \ `University of Southern
California <http://www3.isi.edu/home>`__, \ `Dresden <http://tu-dresden.de/>`__, \ `Purdue
University <http://www.purdue.edu/>`__, and \ `Grid
5000 <https://www.grid5000.fr/mediawiki/index.php/Grid5000:Home>`__ as
partner sites. This material is based upon work supported in part by the
National Science Foundation under Grant No. 0910812.

About this Manual

| This manual is the primary location of  information about FutureGrid
software and services. All FG team members update this manual regularly.
| 
|  We would also like to\ ***ask the community to***\ ***help***\ ​.  If
you would enjoy contributing sections and chapters as part of your
community activities, please contact Gregor
at \ `laszewski@gmail.com <mailto:laszewski@gmail.com>`__. We welcome
additional contributors and editors to this manual.

Enjoy using and expanding the FutureGrid User Manual!

| Gregor von Laszewski
|   

 

 

 

Sponsors
========

Citation
========

If you use FutureGrid, we ask you kindly to include the following
reference in your papers:

#. Fox, G., G. von Laszewski, J. Diaz, K. Keahey, J. Fortes, R.
   Figueiredo, S. Smallen, W. Smith, and A. Grimshaw, "FutureGrid - a
   reconfigurable testbed for Cloud, HPC and Grid Computing",
   Contemporary High Performance Computing: From Petascale toward
   Exascale, April, 2013. Editor J. Vetter.
    `[pdf] <https://portal.futuregrid.org/sites/default/files/vonLaszewski-fg-bookchapter.pdf>`__

Sponsors
========

FutureGrid has received funding from a number of agencies. The current
sponsors of FutureGrid include:

|image1|

NSF

You must include the following in all papers and oral presentations if
you use FG: 

*This material is based upon work supported in part by the National
Science Foundation under Grant No. 0910812 to Indiana University for
"FutureGrid: An Experimental, High-Performance Grid Test-bed." Partners
in the FutureGrid project include U. Chicago, U. Florida, San Diego
Supercomputer Center - UC San Diego, U. Southern California, U. Texas at
Austin, U. Tennessee at Knoxville, U. of Virginia, and T-U. Dresden.*

| -Or the shorter version-
|   

| *This material is based upon work supported in part by the National
Science Foundation under Grant No. 0910812.*
|   

|image2|

**Lilly Endowment**

Provided a $15 million grant to Indiana University to establish
Pervasive Technology Institute (PTI).

|image3|

**Indiana University Pervasive Technology Institute**

Indiana University has sponsored this project with $5M in matching
funding.

 

About
=====

The \ `FutureGrid
Project <https://portal.futuregrid.org/award-abstract-091081-futuregrid-experimental-high-performance-grid-test-bed-0>`__ makes
it possible for researchers to tackle complex research challenges in
computer science related to the use and security of grids and clouds.
These include topics ranging from authentication, authorization,
scheduling, virtualization, middleware design, interface design, and
cybersecurity, to the optimization of grid-enabled and cloud-enabled
computational schemes for researchers in astronomy, chemistry, biology,
engineering, atmospheric science and epidemiology. The project team
provides a significant new experimental computing grid and cloud
test-bed, named FutureGrid, to the research community, together with
user support for third-party researchers conducting experiments on
FutureGrid.

| The test-bed makes it possible for researchers to conduct experiments
by submitting an experiment plan that is then executed via a
sophisticated workflow engine, preserving the provenance and state
information necessary to allow reproducibility.
| 
|  The test-bed also includes a geographically distributed set of
heterogeneous computing systems, a data management system that holds
both metadata and a growing library of software images, and a dedicated
network allowing isolatable, secure experiments. The test-bed supports
virtual machine-based environments, as well as native operating systems
for experiments aimed at minimizing overhead and maximizing performance.
The project partners integrate existing open-source software packages to
create an easy-to-use software environment that supports the
instantiation, execution, and recording of grid and cloud computing
experiments.

| One of the goals of the project is to understand the behavior and
utility of cloud computing approaches. Researchers are able to measure
the overhead of cloud technology by requesting linked experiments on
both virtual and bare-metal systems. FutureGrid enables US scientists to
develop and test new approaches to parallel, grid, and cloud computing,
and compare and collaborate with international efforts in this area. The
FutureGrid project provides an experimental platform that accommodates
batch, grid, and cloud computing, allowing researchers to attack a range
of research questions associated with optimizing, integrating and
scheduling the different service models. The FutureGrid also provides a
test-bed for middleware development and, because of its private network,
allows middleware researchers to do controlled experiments under
different network conditions and to test approaches to middleware that
include direct interaction with the network control layer. Another
component of the project is the development of benchmarks appropriate
for grid computing, including workflow-based benchmarks derived from
applications in astronomy, bioinformatics, seismology, and physics.
| 
|  The FutureGrid forms part of NSF's high-performance
cyberinfrastructure. It increases the capability of the XSEDE to support
innovative computer science research requiring access to lower levels of
the grid software stack, the networking software stack, and to
virtualization and workflow orchestration tools.
| 
|  Education and broader outreach activities include the dissemination
of curricular materials on the use of FutureGrid, pre-packaged
FutureGrid virtual machines configured for particular course modules,
and educational modules based on virtual appliance networks and social
networking technologies that focus on education in networking, parallel
computing, virtualization and distributed computing. The project
advances education and training in distributed computing at academic
institutions with less diverse computational resources. It does this
through the development of instructional resources that include
preconfigured environments that provide students with sandboxed virtual
clusters. These can be used for teaching courses in parallel, cloud, and
grid computing. Such resources also provide academic institutions with a
simple opportunity to experiment with cloud technology to see if such
technology can enhance their campus resources. The FutureGrid project
leverages the fruits of several software development projects funded by
the National Science Foundation and the Department of Energy.

Some useful resources are a poster
in\ ` low </sites/default/files/future%20grid.jpg>`__ and `high </sites/default/files/FutureGrid%20poster%20JPEG_0.jpg>`__ resolution
as well as a generic presentation as of \ `October 11
2009 </sites/default/files/talk-FutureGrid-overview_1.pptx>`__ with an
update on \ `November 6
2009 </sites/default/files/FutureGridOverviewNov06-09_0.ppt>`__ and `September
15
2010 <http://grids.ucs.indiana.edu/ptliupages/presentations/FG-NSF-Sept15-10.pptx>`__.

This material is based upon work supported in part by the National
Science Foundation under Grant No. 0910812 to Indiana University for
"FutureGrid: An Experimental, High-Performance Grid Test-bed." Partners
in the FutureGrid project include U. Chicago, U. Florida, San Diego
Supercomputer Center - UC San Diego, U. Southern California, U. Texas at
Austin, U. Tennessee at Knoxville, U. of Virginia, Purdue I., and T-U.
Dresden. 

 

Table of Contents
=================

The manual is also available as a `single HTML
page <https://portal.futuregrid.org/book/export/html/104>`__.

-  `User Manual </manual>`__

   -  `Preface </preface>`__

      -  `Sponsors </sponsors>`__

   -  `About </about>`__
   -  `Table of Contents </manual/toc>`__
   -  `Introduction </manual/introduction>`__

      -  `Overview </overview-0>`__
      -  `Getting Started </manual/gettingstarted>`__
      -  `Accessing FutureGrid </manual/access>`__

         -  `Account Creation </manual/account-creation>`__

      -  `Help and Support </manual/help-and-support>`__
      -  `Guide to Using the FutureGrid Portal </manual/portal>`__

   -  `Overview of the Hardware </manual/hardware>`__

      -  `Compute Resources </compute-resources>`__
      -  `Alamo </hardware/alamo>`__
      -  `Bravo </hardware/bravo>`__
      -  `Delta </hardware/delta>`__
      -  `Foxtrot </hardware/foxtrot>`__
      -  `Hotel </hardware/hotel>`__
      -  `India </hardware/india>`__
      -  `Sierra </hardware/sierra>`__
      -  `Xray </hardware/xray>`__
      -  `Network </network>`__

         -  `FutureGrid Network Impairments Device
            (NID) </manual/services/network-impairment-device>`__

      -  `Storage </storage>`__

         -  `Using HPSS from FutureGrid </tutorials/hpss>`__

   -  `Status </status>`__
   -  `Accessing FutureGrid resources via
      SSH </manual/accessing-futuregrid-resources-ssh>`__
   -  `HPC Services </manual/hpcservices>`__

      -  `Using HPC Services on FutureGrid </tutorials/hpc>`__
      -  `Log in to HPC services </manual/user/login>`__

         -  `Generating SSH Keys for FutureGrid
            Access </generating-ssh-keys-futuregrid-access>`__

      -  `Working with HPC Job Services </working-hpc-job-services>`__
      -  `Analyzing Code Performance </manual/hpc/performance>`__

         -  `PAPI </manual/papi>`__
         -  `Vampir </manual/performance/vampir>`__
         -  `VampirTrace </manual/vampir/trace>`__

      -  `Official HPCC Results from the Acceptance
         Tests </manual/official-hpcc-results-acceptance-tests>`__
      -  `Foxtrot </manual/foxtrot>`__
      -  `India </manual/india>`__
      -  `Sierra </manual/sierra>`__
      -  `Xray </manual/xray>`__
      -  `Alamo </manual/software/alamo>`__
      -  `Delta </manual/delta>`__

         -  `Running MPI/GPU program on the Delta
            cluster </manual/running-mpigpu-program-delta-cluster>`__
         -  `Running programs on a single
            GPU </manual/gpu/running-programs-single-gpu>`__
         -  `C-means clustering using CUDA on
            GPU </contrib/c-means-clustering-using-cuda-gpu>`__

      -  `ScaleMP vSMP </manual/scalemp-vsmp>`__

   -  `IaaS - Infrastructure as a Service </manual/iaas>`__

      -  `Using IaaS Clouds on FutureGrid </using/clouds>`__
      -  `Using Nimbus on FutureGrid </tutorials/nimbus>`__

         -  `Cloud Quick Start : Launch a VM with 1
            command </manual/nimbus/cloud-quick-start-launch-vm-1-command>`__
         -  `FutureGrid Tutorial NM2 - Nimbus One-Click Cluster
            Guide </tutorials/nm2>`__

      -  `Using Eucalyptus on FutureGrid </tutorials/eucalyptus>`__
      -  `Using OpenStack on
         FutureGrid </manual/using-openstack-futuregrid>`__
      -  `Image Management and Rain on
         FutureGrid </image-management-and-rain-futuregrid>`__

         -  `Generate and Register an OS Image on FutureGrid using the
            FG
            Shell </manual/generate-and-register-os-image-futuregrid-using-fg-shell>`__
         -  `FutureGrid Standalone Image
            Repository </futuregrid-standalone-image-repository>`__
         -  `Manual Image Customization </manually-customize-image>`__
         -  `RAIN Manual Pages </rain-manual-pages>`__

            -  `fg-repo </man/fg-repo>`__
            -  `fg-rain </man/fg-rain>`__
            -  `fg-generate </man/fg-generate>`__
            -  `fg-register </man/fg-register>`__
            -  `fg-shell </man/fg-shell>`__
            -  `fg-portal-manage </man/fg-portal-manage>`__

      -  `ViNe </vine>`__
      -  `OpenNebula 2.0 Tutorial </tutorials/opennebula>`__

   -  `PaaS - Platform as a Service </manual/paas>`__

      -  `Using Map/Reduce in FutureGrid </using/mapreduce>`__
      -  `Running Hadoop as a Batch Job using
         MyHadoop </tutorials/running-hadoop-batch-job-using-myhadoop>`__
      -  `Using SalsaHadoop on
         FutureGrid </using-salsahadoop-futuregrid>`__
      -  `Hadoop Blast </manual/hadoop-blast>`__
      -  `Hadoop WordCount </manual/hadoop-wordcount>`__
      -  `Using Twister on FutureGrid </manual/twister>`__
      -  `Twister Blast </manual/twister-blast>`__
      -  `Eucalyptus and Twister on
         FutureGrid </tutorials/eucalyptus-and-twister-futuregrid>`__
      -  `Using Pegasus on FutureGrid </manual/pegasus>`__

   -  `Management Services </manual/management-services>`__

      -  `Nimbus Phantom </nimbus-phantom>`__
      -  `Precip - Pegasus Repeatable Experiments for the Cloud in
         Python </manual/precip>`__
      -  `cloudinit.d </cloudinitd>`__

   -  `Grid Services </manual/grid-services>`__

      -  `Unicore </manual/unicore>`__
      -  `Genesis II </genesisii>`__
      -  `SAGA supporting Distributed Applications on Grids, Clouds on
         FutureGrid </contrib/saga-supporting-distributed-applications-grids-clouds-futuregrid>`__
      -  `EMI Unicore Tutorial </contrib/emi-unicore-tutorial>`__

   -  `Tutorials </tutorials>`__

      -  `FutureGrid Grid Appliance for Nimbus and
         Eucalyptus </tutorials/ga6old>`__
      -  `One-click Hadoop WordCount on Eucalyptus
         FutureGrid </tutorials/one-click-hadoop-wordcount-eucalyptus-futuregrid>`__
      -  `One-click Twister K-means on Eucalyptus
         FutureGrid </tutorials/one-click-twister-k-means-eucalyptus-futuregrid>`__
      -  `Register Virtual Box Image on
         OpenStack </register-virtual-box-image-openstack>`__

   -  `Virtual Appliances </community/appliances>`__
   -  `Development Projects </development-projects>`__
   -  `Appendix </appendix>`__

      -  `Upgrading Nimbus On FG
         clusters </upgrading-nimbus-fg-clusters>`__

   -  `FAQ </node/2477>`__
   -  `FAQ </manual/faq>`__

Introduction
============

Overview
========

 

The \ `FutureGrid
Project <https://portal.futuregrid.org/award-abstract-091081-futuregrid-experimental-high-performance-grid-test-bed-0>`__ allows
researchers to tackle complex research challenges in computer science
related to the use and security of grids and clouds. We provide a
significant new experimental computing grid and cloud test-bed, named
FutureGrid, to the research community, together with user support for
third-party researchers conducting experiments on FutureGrid.

Project & Account Application
-----------------------------

FutureGrid allows you to easily create a project and use FG resources.
All you need to do is to create a portal account and apply for a
project. Detailed information is provided in the
`manual <https://portal.futuregrid.org/manual/access>`__.

Cloud Services
--------------

Currently, FutureGrid provides three cloud services on a variety of
resources: Nimbus, Eucalyptus, and OpenStack. However, not all services
on the different resources are integrated, and an additional account
request is necessary for accessing Eucalyptus and OpenStack . To find
out how the machines are divided, we provide a convenient \ `status
monitor <http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp>`__.

**Nimbus**
~~~~~~~~~~

Nimbus is an open-source service package that allows users to run
virtual machines on FutureGrid hardware. You can easily upload your own
VM image or customize an image provided by us. When you boot a VM, it is
assigned a public IP address (and/or an optional private address); you
are authorized to log in as root via SSH. You can then run services,
perform computations, and configure the system as desired. After using
and configuring the VM, you can save the modified VM image back to the
Nimbus image repository. Users can find more details in the \ `Nimbus
tutorial <https://portal.futuregrid.org/tutorials/nimbus>`__.

Eucalyptus
~~~~~~~~~~

Eucalyptus is an open-source software platform that implements
IaaS-style cloud computing. Eucalyptus provides a Amazon Web Services
(AWS) compliant EC2-based web service interface for interacting with the
Cloud service. Eucalyptus also provides services such as the
AWS-compliant Walrus and a user interface for managing users and images.
Users can find more details in the \ `Eucalyptus
tutorial <https://portal.futuregrid.org/tutorials/eucalyptus>`__.

OpenStack
~~~~~~~~~

OpenStack is a collection of open source components to deliver public
and private clouds. These components currently include OpenStack Compute
(called Nova), OpenStack Object Storage (called Swift), and OpenStack
Image Service (called Glance). OpenStack is a new effort and has
received considerable momentum due to its openness and the support of
companies. Users can find more details in the
`OpenStack Tutorial <https://portal.futuregrid.org/tutorials/openstack>`__.

OpenNebula
~~~~~~~~~~

**Not yet available to the public**, OpenNebula is an open and flexible
tool that fits into existing data center environments to build any type
of IaaS Cloud deployment. OpenNebula can be primarily used as a
virtualization tool to manage your virtual infrastructure in the data
center or cluster, which is usually referred to as Private Cloud.
OpenNebula supports Hybrid Cloud to combine local infrastructure with
public cloud-based infrastructure, enabling highly scalable hosting
environments. OpenNebula also supports Public Clouds by providing Cloud
interfaces to expose its functionality for virtual machine, storage, and
network management. Users can find how to use this software in the
`OpenNebula
tutorial <https://portal.futuregrid.org/tutorials/opennebula>`__. 

High Performance Computing
--------------------------

High Performance Computing can be defined as the application of
supercomputing techniques to solve computational problems that are too
large for standard computers or would take too much time. This is one of
the more important features that the scientific community needs to
achieve their projects. Thus, FutureGrid provides users the possibility
of executing their parallel applications or using scientific software. A
guide to accessing HPC services can be found in the \ `Accessing
FutureGrid <https://portal.futuregrid.org/manual/access>`__ and `HPC
services <https://portal.futuregrid.org/manual/hpcservices>`__ sections of
the \ `User Manual <https://portal.futuregrid.org/manual>`__.

Storage
-------

Users can find different storage systems to cover a wide number of
purposes. In the \ `Storage
Manual <https://portal.futuregrid.org/manual/services/storage>`__, users
can find the information needed to get access and learn the usage. A
summary of the external storage systems available can be found at:
`http://portal.futuregrid.org/manual/hardware <http://portal.futuregrid.org/manual/hardware>`__.

Information Services
--------------------

These services gather the information of the different elements that
make up FutureGrid to provide accurate and complete knowledge of the
computational environment. This information is presented using different
web portals: \ `General System
Status <https://portal.futuregrid.org/status>`__, \ `Cloud, Cluster,
Services Status <http://inca.futuregrid.org/>`__ and `Network
Status <http://noc.futuregrid.org/>`__.

Hardware
--------

FutureGrid includes a geographically distributed set of heterogeneous
computing systems, data management systems, and dedicated networks.
These resources are provided by different institutions across the United
States. Detailed information on the different sites can be
found \ `here <https://portal.futuregrid.org/hardware>`__ and in
the \ `User Manual <https://portal.futuregrid.org/manual>`__.

Support
-------

The best place to start obtaining information about FutureGrid is to
visit our expanding \ `FutureGrid User
Manual <https://portal.futuregrid.org/manual>`__, of which this page is
a part. To obtain support for FutureGrid, you can visit the \ `Knowledge
Base <http://kb.iu.edu/index.cgi?searchOptionBtn=KB&search=futuregrid&Search=Search&maxdocs=300>`__,
which includes a collection of FAQs about FutureGrid. We also provide
some user \ `Forums <https://portal.futuregrid.org/forum>`__. Please
note that some information may already be outdated. We try our best,
however, to keep the manual and the Knowledge Base as up to date as
possible.

If you need help or observe things that are not correct, see
`https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__.

Acknowledgement
---------------

You must include in all papers and oral presentations the following
acknowledgment:

*"This material is based upon work supported in part by the National
Science Foundation under Grant No. 0910812 to Indiana University for
"FutureGrid: An Experimental, High-Performance Grid Test-bed." Partners
in the FutureGrid project include U. Chicago, U. Florida, San Diego
Supercomputer Center - UC San Diego, U. Southern California, U. Texas at
Austin, U. Tennessee at Knoxville, U. of Virginia, Purdue U., and T-U.
Dresden."*

If you run out of space you can use a shorter version:

| *"This material is based upon work supported in part by the National
Science Foundation under Grant No. 0910812."*
|   

Additionally, you should forward a copy of each publication or
presentation
to \ `https://portal.futuregrid.org/help <mailto:help@futuregrid.org>`__.
Please use this instead of sending e-mail. This will allow faster
assignment to our support staff.

Getting Started
===============

In order for you to gain access to the FutureGrid resources, you need to
follow real simple steps:

#. Create a FutureGrid portal account
#. Create or join a project
#. Upload your SSH key
#. Explore our Manual

We will introduce these steps in more detail next.

Step 1: Create a FutureGrid Portal Account
------------------------------------------

In order to utilize \ **any** FutureGrid resource, you must posses a
FutureGrid \ **portal account**. Thus, \ *apply for your \ **portal
account ***\ before you attempt anything else. This account is used to
gather some information that we will use in the next steps. You must
make sure that the information is complete before you proceed to the
second step.  FutureGrid performs basic verification of the information
you provide when creating an account, so it may take a little while
before your account is approved. Once you have a portal account, please
proceed.

Please note that you cannot access FutureGrid resources until you
complete the next steps.  

Here are a few tips that make it easy for you

-  On the portal's main page at
   `https://portal.futuregrid.org <https://portal.futuregrid.org>`__
   appears
   a \ `**Register** <https://portal.futuregrid.org/user/register%20>`__ Link. 
-  Following you will be able to \ **Create a new account** on the
   portal. 
-  Fill in **ALL **\ fields as much as you can.
-  Note that fields with \* are mandatory
-  It is important that you specify your address information completely.
-  If you are a graduate or undergraduate student please fill out your
   advisors contact information in the field specially dedicated for it.
   If he has a FutureGrid Portal name, please also add his portal name
   if you know it in that field.
-  If you have an e-mail address from your institution, we ask that you
   use this address instead of one from gmail, hotmail, or other e-mail
   services that we cannot trace back to your name or institution.
-  Usage of all non institutional addresses will prolong the application
   process.
     
-  Please note that creating a portal account does not give you access
   to any FutureGrid resources, for that you have to complete step 2 and
   3.
     
-  Please remember that checking your information will take time. Thus
   we recommend that you wait till you get a message that tells you that
   your portal account has been approved. Then continue to The next
   step. We are not conducting any portal approval outside of 10am-4pm
   EST. If you are easily to be identified your approval will take 1-2
   days, if not, we have either problems verifying your data or
   something else is not right. In case you appear to be a spammer we
   will not notify you. 
     
-  In case you are teaching a class class we have some special
   instructions for you and after you apply for a portal account you may
   want to get in contact with us via the `help
   form <https://portal.futuregrid.org/help>`__

Step 2: Create a new Project or join an existing one
----------------------------------------------------

You need to either apply for a new FutureGrid project or join an
existing project to use FutureGrid resources. To apply for a new
project, fill out the `project creation
form <https://portal.futuregrid.org/node/add/fg-projects>`__. To join an
existing project, ask the project lead or project manager for that
project to add you to their project using that same form. If the project
is set to "accept public join request", you may also send a request in
the portal. To do this, first view the `project
list <https://portal.futuregrid.org/projects>`__\ and go to the project
detail page by clicking the project title. If the project is set by the
project lead to "accept join request", then you'll see a large gray
'Join this project' button in the upper right corner of the page. Click
the button to send the join request to the project lead and manager so
they can process your request.

Once you have been approved to work on a project, you will be able to
access the resources and services that your project has requested and
been authorized to use. See the `project creation
form <https://portal.futuregrid.org/node/add/fg-projects>`__ for a list
of FutureGrid resources and services.

Here are a view links that may help you:

-  `Create a new project creation
   form <https://portal.futuregrid.org/node/add/fg-projects>`__
     
-  `See the project list to identify the project you like to
   join <https://portal.futuregrid.org/projects>`__
     
-  `Read some FAQs about the account
   creation <https://portal.futuregrid.org/faq>`__

Step 3: Upload Your SSH Public Key(s)
-------------------------------------

In order to be able to log into the started VMs, among other purposes,
you need to provide FG with a secure-shell (ssh) public key. If you are
already a frequent user of ssh, and have a private and public key pair,
it is perfectly reasonable to provide your public key. It's \ *public*,
after all.

To upload the chosen public key:

#. Copy your public identity into your system clipboard.
#. Log into the FG portal \ `https://portal.futuregrid.org/ <../../>`__
#. In the \ **Accounts** menu, select \ **My Portal and HPC
   Account** page. and activate the panel saying **SSH keys**
#. Click the link that says Add a public key.

This step should be fairly instantaneous.

If you are not familiar with ssh key generation, or if you have
difficulty generating a key pair, please inform yourself about ssh keys
or contact us via our `help form <https://portal.futuregrid.org/help>`__
. Detailed instructions on how to generate ssh key pairs will be added
to this document in the near future.

Step 4: Explore the Documentation
  
---------------------------------

Once you have access to FutureGrid resources, a good place to start
learning about how to use FutureGrid are the tutorials, specifically the
following:

-  The \ `Manual <http://portal.futuregrid.org/manual>`__ for detailed
   information

Our manual will include a variety of topics that are of interest to our
users from many different user communities. It would be a disservice to
you to just list a view of them. Hence we provide you with a convenient
link to our table of contents. Please note that the manual also contains
links to our tutorials and our MOOC.

-  `Manual Table of
   Contents <https://portal.futuregrid.org/manual/toc>`__

It will be also easy for you to search for some topics in our search box
at the top of the Web page.

 
=

 
-

Accessing FutureGrid
====================

To use FutureGrid you must be part of a valid "project". Project
leaders are requested to fill out project applications about the use of
FutureGrid. The
`form <https://portal.futuregrid.org/node/add/fg-projects>`__ gathers
some important information about their projects to be conducted. At this
time this information is publicly shared. This information is used to
report and document not only to us but also to our sponsors which
activities are conducted on FutureGrid. The more precise you are in your
descriptions and filling out the forms the better we can highlight your
project. Once a project is formed, project members can join a project.
This must be conducted by the project lead.  A user retains an active
account on FutureGrid when they are in at least one active project. A
user that is inactive does not have to apply for a new account, but
instead apply for a new project. Once that project is activated the user
account becomes active.

Account Management Service
--------------------------

Please note the current process of applying for account may change. 

#. Any user can apply easily for a Portal account: Please go to 

   -  `https://portal.futuregrid.org/user/register <http://portal.futuregrid.org/user/register>`__
   -  it may take a day or two to get a portal account. Portal
      accounts will not be created over the weekend.

#. Once logged in the user has a couple of options

   -  `User Profile
      Management <https://portal.futuregrid.org/manage-my-portal-account>`__:
      Update information regarding the user profile
   -  Project Management: apply for `new
      projects <https://portal.futuregrid.org/node/add/fg-projects>`__,
      join existing projects, update information and results of a
      project, manage members and roles of users participating in your
      projects
   -  Managing Certificates and Keys: Integrate OpenID login for the
      portal (with for example your google ID), manage your ssh key for
      access to the HPC service, Manage Nimbus and Eucalyptus accounts
      and keys 

Apply for a Project or Request an Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get access to FutureGrid (FG), you need to register your project in
it. Please go to:

-  `https://portal.futuregrid.org/node/add/fg-projects <https://portal.futuregrid.org/node/add/fg-projects>`__

to apply for a new project. It may take some time for your project to
get approved. No projects will be approved over the weekend.

In case you like to join an existing project, please find the list of
projects at:

-  `https://portal.futuregrid.org/projects <https://portal.futuregrid.org/projects>`__

Clicking on a project title will bring you to the project information
page, where you may see a large gray button on the upper right corner of
the page named 'Join this project'. Click to send join request to that
project. Please notice the PI of the project has to approve you before
you are part of that project.

Some project may not accept external members so there would be no join
button for them. Please notice this behavior is controlled by the owner
of the project.

You can always communicate with the project PI through external channel
of the FutureGrid portal if you know him/her in person by letting
him/her know your portal username. He/she can then directly add you as a
member to his/her project without going through the join request process
through the portal.

Implicit Project Responsibilities for Project Members and PI Agreement for Reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Project PI has agreed to certain reporting requirements to provide
information to FutureGrid. He will be responsible to make sure that they
are completed and also implemented with the users joining the project.
Thus the user is responsible to comply with the terms of the project in
regards to reporting and acknowledgements in case of publications. Each
project PI has the responsibility to communicate such requirements to
the members and managers. The project agreements overwrite the
individuals agreement. 

Cloud Accounts
~~~~~~~~~~~~~~

The cloud accounts are handled currently separately from the HPC account
creation process. In fact the Eucalyptus clouds are disjunctive on each
machine and have their own user management. For Nimbus uploading your
ssh key is sufficient. The turnaround time for you getting access to the
system is typically between 30 minutes and one day.

Please be kind and only apply for these cloud accounts if you really
need them.

Key Reset or Adding new Keys
----------------------------

To reset or add a new you ssh key, please update your keys first by
visiting the page

-  `https://portal.futuregrid.org/user/23/ssh-keys <https://portal.futuregrid.org/user/23/ssh-keys>`__

and change the keys as needed. Your reset will take 30 minutes to one
day to propagate through the system services.

You are not allowed to use password less keys.  Your account may be
deactivated.

 

Account Creation
================

Creating an HPC account
-----------------------

All you need to do to obtain an HPC account is to be in a valid project
and upload your ssh key. Typically you will get the account within one
business day. There will be typically no accounts approved in non
business hours including weekends.

Please add your SSH keys in your profile which you can find at:

-  `https://portal.futuregrid.org/user/23/ssh-keys <https://portal.futuregrid.org/user/23/ssh-keys>`__

Once you have done that, please go back to this form and complete it.
After submission, this form will create an e-mail request to FutureGrid.
The FG administrators may contact you to verify this request.

| Please, make sure you are a member of a valid project.
|  Project IDs can be found at

-  `https://portal.futuregrid.org/projects <https://portal.futuregrid.org/projects>`__

The project lead is responsible for determining if you can be added to
the project.

Note: Do not send mail to FG staff members about joining a project, as
we are not managing individual project memberships

To view your current memberships and status of your account application,
please visit

-  `https://portal.futuregrid.org/manage-my-portal-account <https://portal.futuregrid.org/manage-my-portal-account>`__

Resetting a ssh-key
-------------------

Simply visit the ssh-key page and upload a new key. YoU can optionally
delete other keys if you do n longer need them.

Nimbus, Eucalyptus, OpenStack
-----------------------------

Once you have uploaded your SSH key, the Nimbus, Eucalyptus, and
OpenStack access will be granted. Please visit the manual pages for more
details on accessing them.

Help and Support
================

Help and Support
----------------

FutureGrid provides help and support to its users through various
services. These services include a ticket system, mailinglists  (soon to
be replaced by a user forums), manuals, a KnowledgeBase, and an
educational outreach activities developing tutorials and other
educational material.

 

Manual
------

We are creating gradually a manual for FutureGrid. This manual contains
contributions from the FG staff and FG users. The link for the manual is

-  `https://portal.futuregrid.org/manual <https://portal.futuregrid.org/manual>`__

In case you have a useful contribution, you can simply comment on each
page, or if you like to create a chapter to be included, please create a
community page.  A community page can be created by clicking on the
following link

-  `Create a
   Community Page <https://portal.futuregrid.org/node/add/page-community>`__

Community pages can also be used to report on elaborate experiment
results. Once you are done with your contribution, please send a ticket
to us so we can make it more prominently visible in the portal:

-  `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__

User Forum
----------

Based on advice from other projects we have established a number of user
forums that are available while following this link

-  `User Forum <https://portal.futuregrid.org/forum>`__

To post to the forum, you must create a portal account.

Help Ticketing System
---------------------

To create a ticket for FutureGrid support, please use out ticket form
from the web page at

-  `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__

in which you describe problems like feature request, or bug report. A
ticket will be automatically generated and you'll receive an auto-reply
mail with the ticket number for further reference. FutureGrid staff will
be looking into the ticket and working on it. You will receive updates
and resolution through email upon the completion of the investigation.
Please be aware that feedback may not be instantaneous. Tickets you have
submitted can be seen at

-  `https://portal.futuregrid.org/tickets <https://portal.futuregrid.org/tickets>`__

 

FutureGrid Experts Team
-----------------------

To facilitate the support of projects, FG has established an expert
team. Each project will be assigned an expert that can be consulted in
case of questions or technical issues. If the expert can not answer the
question, he will consult with other experts. The communication with the
expert is initially conducted simply via e-mail. In future, we will have
forums and a dedicated ticket system available that logs interactions
with these experts. On general topics a forum is used that is monitored
by the experts. For information that can not be publicly shared please
use 

-  https://portal.futuregrid.org/help

The current team of experts is coordinated by Geoffrey C. Fox. The team
includes

    -  `Edit </admin/build/views/edit/expert_list?destination=book%2Fexport%2Fhtml%2F104#views-tab-default>`__
    -  `Export </admin/build/views/export/expert_list>`__
    -  `Clone </admin/build/views/clone/expert_list>`__

    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | Firstname                           | Lastname                              | Institution                                                                                                              |
    +=====================================+=======================================+==========================================================================================================================+
    | `Andrew </users/ajyounge>`__        | `Younge </users/ajyounge>`__          | `Community Grids Laboratory </users/ajyounge>`__                                                                         |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Gregor </users/gvonlasz>`__        | `von Laszewski </users/gvonlasz>`__   | `Community Grids Laboratory </users/gvonlasz>`__                                                                         |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Xiaoming </users/gaoxm>`__         | `Gao </users/gaoxm>`__                | `Pervasive Technology Institute </users/gaoxm>`__                                                                        |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Javier </users/jdiaz>`__           | `Diaz Montes </users/jdiaz>`__        | `Rutgers Discovery Informatics Institute (RDI2) / NSF Center for Cloud and Autonomic Computing (CAC) </users/jdiaz>`__   |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Geoffrey </users/gcf>`__           | `Fox </users/gcf>`__                  | `Community Grids Laboratory </users/gcf>`__                                                                              |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Zhenhua </users/zhguo>`__          | `Guo </users/zhguo>`__                | `Pervasive Technology Institute </users/zhguo>`__                                                                        |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Tak-Lon </users/taklwu>`__         | `Wu </users/taklwu>`__                | `Pervasive Technology Institute / Community Grids Laboratory </users/taklwu>`__                                          |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Yuduo </users/yuduo>`__            | `Zhou </users/yuduo>`__               | `Pervasive Technology Institute </users/yuduo>`__                                                                        |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Tao </users/taohuang>`__           | `Huang </users/taohuang>`__           | `IU PTI </users/taohuang>`__                                                                                             |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Jonathan </users/jklingin>`__      | `Klinginsmith </users/jklingin>`__    | `School of Informatics </users/jklingin>`__                                                                              |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Thilina </users/thilina>`__        | `Gunarathne </users/thilina>`__       | `Community Grids Laboratory </users/thilina>`__                                                                          |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Saliya </users/sekanaya>`__        | `Ekanayake </users/sekanaya>`__       | `Pervasive Technology Institute </users/sekanaya>`__                                                                     |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Ti </users/leggett>`__             | `Leggett </users/leggett>`__          | `Computation Institute </users/leggett>`__                                                                               |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Judy </users/xqiu>`__              | `Qiu </users/xqiu>`__                 | `School of Informatics and Computing </users/xqiu>`__                                                                    |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Mauricio </users/tsugawa>`__       | `Tsugawa </users/tsugawa>`__          | `University of Florida </users/tsugawa>`__                                                                               |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Jerome </users/jemitche>`__        | `Mitchell </users/jemitche>`__        | `Indiana University </users/jemitche>`__                                                                                 |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Bingjing </users/zhangbj>`__       | `Zhang </users/zhangbj>`__            | `Pervasive Technology Institute </users/zhangbj>`__                                                                      |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Shava </users/ssmallen>`__         | `Smallen </users/ssmallen>`__         | `San Diego Supercomputer Center </users/ssmallen>`__                                                                     |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `David </users/dgignac>`__          | `Gignac </users/dgignac>`__           | `TACC </users/dgignac>`__                                                                                                |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Ryan </users/rhartman>`__          | `Hartman </users/rhartman>`__         | `University Information Technological Services </users/rhartman>`__                                                      |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Yang </users/yangruan>`__          | `Ruan </users/yangruan>`__            | `Pervasive Technology Institute </users/yangruan>`__                                                                     |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Fugang </users/fuwang>`__          | `Wang </users/fuwang>`__              | `Community Grids Lab at the Pervasive Technology Institute </users/fuwang>`__                                            |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Koji </users/ktanaka>`__           | `Tanaka </users/ktanaka>`__           | `Community Grids Laboratory </users/ktanaka>`__                                                                          |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Hyungro </users/hrlee>`__          | `Lee </users/hrlee>`__                | `Community Grids Laboratory </users/hrlee>`__                                                                            |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Gary </users/gmiksik>`__           | `Miksik </users/gmiksik>`__           | `Pervasive Technology Institute / Digital Science Center/ Community Grids Laboratory </users/gmiksik>`__                 |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Jun </users/junwang>`__            | `Wang </users/junwang>`__             | `PTI </users/junwang>`__                                                                                                 |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Barbara Ann </users/baoleary>`__   | `O'Leary </users/baoleary>`__         | `Pervasive Technology Institute </users/baoleary>`__                                                                     |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
    | `Carrie </users/cmarnold>`__        | `Arnold </users/cmarnold>`__          | `Texas Advanced Computing Center </users/cmarnold>`__                                                                    |
    +-------------------------------------+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

 

Responsibilities of an expert include

-  help projects through the application process if contacted 
-  help on technical questions related to FG services
-  help creating manual pages from the information they have been asked
   by FG users
-  help on gathering results from the projects
-  help on establishing a web presence of the project on the FG Web site

Training and Education
----------------------

FutureGrid provides training and educational materials through manuals
and tutorials.

FutureGrid leverages technologies contributed by its partners and by the
open-source community in the packaging, configuration, and deployment of
virtual clusters - including the plug-and-play, self-configuring Grid
appliance, the Nimbus science cloud middleware, the IPOP/GroupVPN
self-configuring virtual network, and the ViNe virtual network.

For links to the initial appliance-based FutureGrid tutorials, see the
FutureGrid \ `Education and Outreach
page <https://portal.futuregrid.org/outreach>`__. Additionally, for
video tutorials on the use of the appliances, see the \ `Grid appliance
YouTube
channel <http://www.youtube.com/acisp2p#p/c/D77781CEF51F72F3>`__.

 

`‹ Quickstart <https://portal.futuregrid.org/gettingstarted>`__

Guide to Using the FutureGrid Portal
====================================

Functions of the FutureGrid Portal
----------------------------------

| 
|  The FutureGrid portal aims to:

#. Be the definite source for information about FutureGrid (manuals,
   papers, forums, FAQ, ...)
#. Allow management of your FG accounts (portal, services, and
   resources)
#. Allow management of your futuregrid projects
#. Allow management of FG experiments
#. Allow the dynamic provisioning via RAIN 

A FutureGrid User Dashboard 
----------------------------

After login, you will be redirected to a dashboard-like page (go to the
menu Accounts -> My Portal Account), where you will see the following:

#. A list of useful links, including links to profile, account, SSH key,
   and OpenID management information.
#. A projects summary section that lists the summarized information
   about projects that you are the owner of, that you manage, that you
   are member of, and that you support as a FutureGrid expert,
   respectively. Clicking the project title will bring you to the
   project detail info page. For those projects that you own or manage,
   an 'edit' link is also there so you can quickly update the project
   information.
#. A 'My Content' section where the content that you are responsible for
   maintaining (and/or that you have contributed) is listed. This gives
   a convenient view so you can easily go back to the content and update
   it.
#. A 'My Publications' section that lists your publications.

Update Project Information and Add Results
------------------------------------------

Another frequently used feature is the ability to update your project
information (e.g., add project members) and fill in results in the
'Project Results' section. You can do so only when you are either the
owner of the project or the project manager (if the owner has delegated
that to you). By following the links provided in the 'Dashboard'
section, you can review and edit the project information.

To add a user to your project as a member, the user must have a
FutureGrid portal account first. Then, while editing the project, you
can type a user's first name, and the suggestion feature will pop up
with the user's username to be added. If you have many members to add,
click the 'Add another item' in the 'Project Members' section to add
more. See also `this
FAQ <https://portal.futuregrid.org/how-can-i-add-people-project>`__.

For updating your project results, there is a 'Project Results' section
with a 'Results' window that supports WYSIWYG editing. It supports
simple formatted text, embedded images, etc. For text, you can edit
directly in the window, or copy the content you developed in your
favorite editor and paste the content in the edit window. In the case of
images, you'll need to upload the image to the server first, and then
insert it to the window, or alternatively refer to an external URL for
an image hosted somewhere else.

For more detailed info on how to include an image, please see `this
FAQ <https://portal.futuregrid.org/how-upload-andor-include-image-while-creating-pagenews-etc>`__.

Contribute to the FutureGrid Community
--------------------------------------

The FutureGrid portal also provides its users a place where they can
contribute to the community by sharing their ideas, research topics, FG
experience, etc.; in this way people can learn from you, and also you
can learn from others. Emphasizing user participation and
collaboration is one of the main goals shaping the portal to its current
state.

You can contribute by `creating a 'Community
Page' <https://portal.futuregrid.org/node/add/page-community>`__. You
can find the link in the left side navigation block, under the 'Create
content' menu. After entering the edit page, you'll see a 'Title' text
box, where you put the content/article title, and a 'Body' window where
you put the content. Once again, it supports formatted text and embedded
images, etc.

You can cite FutureGrid references also, by enclosing a citekey within
the 'bib' tag as stated under the editor window (NOTE: Please use '[]'
instead of '<>'), where CITEKEY could be found in the `biblio
page <https://portal.futuregrid.org/biblio>`__ (the content within but
not including the '[ ]').

An example of a user contributed page can be found
`here <https://portal.futuregrid.org/contrib/testexample-page-user-contributed-page>`__.

File Upload and Attachment to a Page
------------------------------------

Please see `this
FAQ <https://portal.futuregrid.org/faq/how-uploadattach-file-page>`__
for instructions on file upload.

Overview of the Hardware
========================

 

These are the current resources available in FutureGrid. More detailed
information is provided
`here <https://portal.futuregrid.org/manual/hardware>`__.

**Compute Resources**

+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| **Name**                                                       | **System Type**           | **# Nodes**   | **# CPUS**   | **# Cores**   | **TFLOPS**   | **RAM (GB**   | **Storage (TB)**   | **Site**   |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `india <https://portal.futuregrid.org/hardware/india>`__       | IBM iDataplex             | 128           | 256          | 1024          | 11           | 3072          | 335                | IU         |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `hotel <https://portal.futuregrid.org/hardware/hotel>`__       | IBM iDataplex             | 84            | 168          | 672           | 7            | 2016          | 120                | UC         |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `sierra <https://portal.futuregrid.org/hardware/sierra>`__     | IBM iDataplex             | 84            | 168          | 672           | 7            | 2688          | 96                 | SDSC       |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `foxtrot <https://portal.futuregrid.org/hardware/foxtrot>`__   | IBM iDataplex             | 32            | 64           | 256           | 3            | 768           | 0                  | UF         |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `alamo <https://portal.futuregrid.org/hardware/alamo>`__       | Dell Poweredge            | 96            | 192          | 768           | 8            | 1152          | 30                 | TACC       |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `xray <https://portal.futuregrid.org/hardware/xray>`__         | Cray XT5m                 | 1             | 166          | 664           | 6            | 1328          | 5.4                | IU         |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `bravo <https://portal.futuregrid.org/hardware/bravo>`__       | HP Proliant               | 16            | 32           | 128           | 1.7          | 3072          | 128                | IU         |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `delta <https://portal.futuregrid.org/hardware/delta>`__       | GPU Cluster(SuperMicro)   | 16            | 32           | 192           |              | 1333          | 144                | IU         |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+
| `lima <https://portal.futuregrid.org/hardware/lima>`__         | Aeon Eclipse64            | 8             | 16           | 128           | 1.3          | 512           | 3.8 (SSD)          | SDSC       |
|                                                                |                           |               |              |               |              |               |  8.0 (HDD)         |            |
+----------------------------------------------------------------+---------------------------+---------------+--------------+---------------+--------------+---------------+--------------------+------------+

**Storage Resources**

+-------------------+------------------------+-------------------+------------+
| **System Type**   | **Capacity (TB)**      | **File System**   | **Site**   |
+-------------------+------------------------+-------------------+------------+
| DDN 9550          | 339 shared with IU +   | Luster            | IU         |
|  Data Capacitor   |  16 TB dedicated       |                   |            |
+-------------------+------------------------+-------------------+------------+
| DDN 6620          | 120                    | GPFS              | UC         |
+-------------------+------------------------+-------------------+------------+
| SunFire x4540     | 96                     | ZFS               | SDSC       |
+-------------------+------------------------+-------------------+------------+
| Dell MD3000       | 30                     | NFS               | TACC       |
+-------------------+------------------------+-------------------+------------+
| IBM dx360 M3      | 24                     | NFS               | UF         |
+-------------------+------------------------+-------------------+------------+

Status
------

The status of the resources can be monitored through:

-  `https://portal.futuregrid.org/status <https://portal.futuregrid.org/status>`__

This page also contains a link to our operational status of FutureGrid
resources and services, see the FutureGrid Inca server at:

-  `http://inca.futuregrid.org <http://inca.futuregrid.org/>`__

Maintenance
-----------

Activities during the regular maintenance window for FutureGrid machines
are listed in the FutureGrid wiki at:

-  `https://wiki.futuregrid.org/index.php/Hw:MaintActivities <https://wiki.futuregrid.org/index.php/Hw:MaintActivities>`__.

Scheduled outages and maintenance windows on the FutureGrid network are
collected in the Network Operations Calendar at:

-  `https://noc.futuregrid.org/futuregrid/support/operations-calendar3.html <https://noc.futuregrid.org/futuregrid/support/operations-calendar3.html>`__

Compute Resources
=================

GVL: This section belongs to HPC Services

Compute Hardware Resources & HPC Job Queue Information

+------------+--------------+---------------------------+-----------------------+-----------------------+
| Resource   | Queue name   | Default Wallclock Limit   | Max Wallclock Limit   | NOTES                 |
+============+==============+===========================+=======================+=======================+
| india      | batch        | 4 hours                   | 24 hours              |                       |
+------------+--------------+---------------------------+-----------------------+-----------------------+
|            | long         | 8 hours                   | 168 hours             |                       |
+------------+--------------+---------------------------+-----------------------+-----------------------+
|            | scalemp      | 8 hours                   | 168 hours             | restricted access     |
+------------+--------------+---------------------------+-----------------------+-----------------------+
|            | b534         | none                      | none                  | restricted access     |
+------------+--------------+---------------------------+-----------------------+-----------------------+
|            | ajyounge     | none                      | none                  | restricted access     |
+------------+--------------+---------------------------+-----------------------+-----------------------+
| sierra     | batch        | 4 hours                   | 24 hours              |                       |
+------------+--------------+---------------------------+-----------------------+-----------------------+
|            | long         | 8 hours                   | 168 hours             |                       |
+------------+--------------+---------------------------+-----------------------+-----------------------+
| hotel      | extended     | none                      | none                  |                       |
+------------+--------------+---------------------------+-----------------------+-----------------------+
| alamo      | shortq       | none                      | 24 hours              |                       |
+------------+--------------+---------------------------+-----------------------+-----------------------+
|            | longq        | none                      | 24 hours              |                       |
+------------+--------------+---------------------------+-----------------------+-----------------------+
| foxtrot    | batch        | 1 hour                    | none                  | not for general use   |
+------------+--------------+---------------------------+-----------------------+-----------------------+

For availability, please visit:
`http://portal.futuregrid.org/status <http://portal.futuregrid.org/status>`__
.

GVL: This image belongs to the specific cluster desciption:

|image4|

IU iDataplex & Cray

GVL: This section belongs to the specific cluster description:

|image5|

IU Cray

GVL: This belongs to networking:

Compute Networks
----------------

**Resource Name**

**Network Devices**

IU Cray  

Cray 2D Torus SeaStar 

 

IU iDataPlex  

DDR IB  

QLogic switch with Mellanox ConnectX adapters

Blade Network Technologies & Force10 Ethernet switches

 

SDSC 

DDR IB 

Cisco switch with Mellanox ConnectX adapters

Juniper Ethernet switches

 

TACC 

QDR IB  

Mellanox switches and adapters

Dell Ethernet switches

 

UC 

DDR IB 

QLogic switch with Mellanox ConnectX adapters

Blade Network Technologies & Juniper switches

UF

Ethernet only (Blade Network Technologies & Force10 switches)

 
-

Alamo
=====

| **ALAMO**
|  *​Texas Advanced Computing Center*
| 
|  Alamo consists of 96 nodes with dual Intel X5550 processors and 1152
GB of memory. Following are detailed specifications for Alamo.
| 
|  SPECIFICATIONS
| 

+----------------------------------------+---------------------------------------+
| Machine Type                           | Cluster                               |
+----------------------------------------+---------------------------------------+
| System Type                            | Dell PowerEdge M610 Blade             |
+----------------------------------------+---------------------------------------+
| CPU type                               | Intel Xeon X5550                      |
+----------------------------------------+---------------------------------------+
| Host Name                              | alamo                                 |
+----------------------------------------+---------------------------------------+
| CPU Speed                              | 2.66GHz                               |
+----------------------------------------+---------------------------------------+
| Number of CPUs                         | 192                                   |
+----------------------------------------+---------------------------------------+
| Number of nodes                        | 96                                    |
+----------------------------------------+---------------------------------------+
| RAM                                    | 12 GB DDR3 1333Mhz                    |
+----------------------------------------+---------------------------------------+
| Total RAM (GB)                         | 1152                                  |
+----------------------------------------+---------------------------------------+
| Number of cores                        | 768                                   |
+----------------------------------------+---------------------------------------+
| Operating System                       | Linux                                 |
+----------------------------------------+---------------------------------------+
| Tflops                                 | 8                                     |
+----------------------------------------+---------------------------------------+
| Disk Size (TB)                         | 48                                    |
+----------------------------------------+---------------------------------------+
| Hard Drives                            | 500 GB Internal 7200 RPM SAS Drive    |
+----------------------------------------+---------------------------------------+
| Primary storage, shared by all nodes   | NFS                                   |
|                                        |                                       |
+----------------------------------------+---------------------------------------+
| Connection configuration               | Mellanox 4x QDR InfiniBand adapters   |
|                                        |                                       |
+----------------------------------------+---------------------------------------+

| 

Bravo
=====

| **BRAVO**
|  *​Indiana University, Bloomington*
| 
|  Bravo consists of 16 nodes with dual Intel Xeon E5620 processors and
192 GB of memory. Following are detailed specifications for Bravo:
| 
|  SPECIFICATIONS
| 

+----------------------------------------+---------------------------------------+
| Machine Type                           | Cluster                               |
+----------------------------------------+---------------------------------------+
| System Type                            | HP Proliant                           |
+----------------------------------------+---------------------------------------+
| CPU type                               | Intel Xeon E5620                      |
+----------------------------------------+---------------------------------------+
| Host Name                              | bravo                                 |
+----------------------------------------+---------------------------------------+
| CPU Speed                              | 2.40GHz                               |
+----------------------------------------+---------------------------------------+
| Number of CPUs                         | 32                                    |
+----------------------------------------+---------------------------------------+
| Number of nodes                        | 16                                    |
+----------------------------------------+---------------------------------------+
| RAM                                    | 192 GB DDR3 1333Mhz                   |
+----------------------------------------+---------------------------------------+
| Total RAM (GB)                         | 3072                                  |
+----------------------------------------+---------------------------------------+
| Number of cores                        | 128                                   |
+----------------------------------------+---------------------------------------+
| Operating System                       | Linux                                 |
+----------------------------------------+---------------------------------------+
| Tflops                                 | 1.7                                   |
+----------------------------------------+---------------------------------------+
| Hard Drives                            | 6x2TB Internal 7200 RPM SATA Drive    |
+----------------------------------------+---------------------------------------+
| Primary storage, shared by all nodes   | NFS                                   |
|                                        |                                       |
+----------------------------------------+---------------------------------------+
| Connection configuration               | Mellanox 4x DDR InfiniBand adapters   |
+----------------------------------------+---------------------------------------+

`Instructions for submitting jobs in
bravo. <https://portal.futuregrid.org/manual/bravo>`__

Delta
=====

| **DELTA**
| 
|  *​Indiana University, Bloomington*
| 
|  Delta consists of 16 nodes with two core Intel X5560 processors and
192 GB of memory. Each node supports two nVIDIA Tesla C2070 GPUs.
| 
|  SPECIFICATIONS
| 

+----------------------------------------+-----------------------------------+
| Machine Type                           | Cluster                           |
+----------------------------------------+-----------------------------------+
| CPU type                               | Intel Xeon 5660                   |
+----------------------------------------+-----------------------------------+
| Host Name                              | delta                             |
+----------------------------------------+-----------------------------------+
| CPU Speed                              | 2.80 GHz                          |
+----------------------------------------+-----------------------------------+
| CPUs (cores) per node                  | 2 (12)                            |
+----------------------------------------+-----------------------------------+
| Number of nodes                        | 16                                |
+----------------------------------------+-----------------------------------+
| GPU type                               | nVIDIA Tesla C2070                |
+----------------------------------------+-----------------------------------+
| GPUs per node                          | 2                                 |
+----------------------------------------+-----------------------------------+
| RAM                                    | 16 GB DDR3 1333 Mhz               |
+----------------------------------------+-----------------------------------+
| Memory per node [GB]                   | 192                               |
+----------------------------------------+-----------------------------------+
| Total CPUs (cores)                     | 32 (192)                          |
+----------------------------------------+-----------------------------------+
| Total Memory [GB]                      | 3072                              |
+----------------------------------------+-----------------------------------+
| Total GPUs                             | 32                                |
+----------------------------------------+-----------------------------------+
| Cores per GPU                          | 448                               |
+----------------------------------------+-----------------------------------+
| Operating System                       | Linux                             |
+----------------------------------------+-----------------------------------+
| Hard Drives                            | Seagate Constellation 7.2 K RPM   |
|                                        |  64 MB Cache SATA 92GB            |
+----------------------------------------+-----------------------------------+
| Storage details                        | RAID 9260-4i 1pt SAS2             |
|                                        |  512 MB SGL                       |
+----------------------------------------+-----------------------------------+
| Batch system                           | Torque                            |
+----------------------------------------+-----------------------------------+
| Disk Size [TB]                         | 15                                |
+----------------------------------------+-----------------------------------+
| Local storage, per node [GB]           | 92                                |
+----------------------------------------+-----------------------------------+
| Primary storage, shared by all nodes   | NFS                               |
+----------------------------------------+-----------------------------------+

| 
| 
|  For more, see the `DELTA GPU User
Manual <https://portal.futuregrid.org/manual/delta%20%20>`__.
| 
| 

Foxtrot
=======

| **FOXTROT**
|  *​University of Florida, Gainesville*
| 
|  Foxtrot consists of 32 nodes with dual Intel X5520 processors and 768
GB of memory. Following are detailed specifications for Foxtrot.
| 
|  SPECIFICATIONS

+----------------------------------------+---------------------------------------+
| Machine Type                           | Cluster                               |
+----------------------------------------+---------------------------------------+
| System Type                            | IBM iDataPlex dx 360 M2               |
+----------------------------------------+---------------------------------------+
| CPU type                               | Intel Xeon X5520                      |
+----------------------------------------+---------------------------------------+
| Host Name                              | foxtrot                               |
+----------------------------------------+---------------------------------------+
| CPU Speed                              | 2.26GHz                               |
+----------------------------------------+---------------------------------------+
| Number of CPUs                         | 64                                    |
+----------------------------------------+---------------------------------------+
| Number of nodes                        | 32                                    |
+----------------------------------------+---------------------------------------+
| RAM                                    | 24 GB DDR3 1333Mhz                    |
+----------------------------------------+---------------------------------------+
| Total RAM (GB)                         | 768                                   |
+----------------------------------------+---------------------------------------+
| Number of cores                        | 256                                   |
+----------------------------------------+---------------------------------------+
| Operating System                       | Linux                                 |
+----------------------------------------+---------------------------------------+
| Tflops                                 | 3                                     |
+----------------------------------------+---------------------------------------+
| Disk Size (TB)                         | 20                                    |
+----------------------------------------+---------------------------------------+
| Hard Drives                            | 500 GB Internal 7200 RPM SATA Drive   |
+----------------------------------------+---------------------------------------+
| Primary storage, shared by all nodes   | NFS                                   |
|                                        |                                       |
+----------------------------------------+---------------------------------------+

| 

Hotel
=====

| **HOTEL**
|  *​University of Illinois, Chicago*
| 
|  Hotel consists of 84 nodes with dual Intel X5550 processors and 2016
GB of memory. Following are detailed specifications for Hotel.
| 
|  SPECIFICATIONS
| 

+----------------------------------------+---------------------------------------+
| Machine Type                           | Cluster                               |
+----------------------------------------+---------------------------------------+
| System Type                            | IBM iDataPlex dx 360 M2               |
+----------------------------------------+---------------------------------------+
| CPU type                               | Intel Xeon X5550                      |
+----------------------------------------+---------------------------------------+
| Host Name                              | hotel                                 |
+----------------------------------------+---------------------------------------+
| CPU Speed                              | 2.66GHz                               |
+----------------------------------------+---------------------------------------+
| Number of CPUs                         | 168                                   |
+----------------------------------------+---------------------------------------+
| Number of nodes                        | 84                                    |
+----------------------------------------+---------------------------------------+
| RAM                                    | 24 GB DDR3 1333Mhz                    |
+----------------------------------------+---------------------------------------+
| Total RAM (GB)                         | 2016                                  |
+----------------------------------------+---------------------------------------+
| Number of cores                        | 672                                   |
+----------------------------------------+---------------------------------------+
| Operating System                       | Linux                                 |
+----------------------------------------+---------------------------------------+
| Tflops                                 | 7                                     |
+----------------------------------------+---------------------------------------+
| Disk Size (TB)                         | 120                                   |
+----------------------------------------+---------------------------------------+
| Hard Drives                            | 1 TB Internal 7200 RPM SATA Drive     |
+----------------------------------------+---------------------------------------+
| Primary storage, shared by all nodes   | GPFS                                  |
|                                        |                                       |
+----------------------------------------+---------------------------------------+
| Connection configuration               | Mellanox 4x DDR InfiniBand adapters   |
|                                        |                                       |
+----------------------------------------+---------------------------------------+

| 

India
=====

| **INDIA**
|  *​Indiana University, Bloomington*
| 
|  India consists of 128 nodes with dual Intel X5550 processors and 24
GB of memory. Following are detailed specifications for India.
| 
|  SPECIFICATIONS
| 

+----------------------------------------+----------------------------------------+
| Machine Type                           | Cluster                                |
+----------------------------------------+----------------------------------------+
| System Type                            | IBM iDataPlex dx 360 M2                |
+----------------------------------------+----------------------------------------+
| CPU type                               | Intel Xeon X5550                       |
+----------------------------------------+----------------------------------------+
| Host Name                              | india                                  |
+----------------------------------------+----------------------------------------+
| CPU Speed                              | 2.66GHz                                |
+----------------------------------------+----------------------------------------+
| Number of CPUs                         | 256                                    |
+----------------------------------------+----------------------------------------+
| Number of nodes                        | 128                                    |
+----------------------------------------+----------------------------------------+
| RAM                                    | 24 GB DDR3 1333Mhz                     |
+----------------------------------------+----------------------------------------+
| Total RAM (GB)                         | 3072                                   |
+----------------------------------------+----------------------------------------+
| Number of cores                        | 1024                                   |
+----------------------------------------+----------------------------------------+
| Operating System                       | Linux                                  |
+----------------------------------------+----------------------------------------+
| Tflops                                 | 11                                     |
+----------------------------------------+----------------------------------------+
| Disk Size (TB)                         | 335                                    |
+----------------------------------------+----------------------------------------+
| Hard Drives                            | 3000 GB Internal 7200 RPM SATA Drive   |
+----------------------------------------+----------------------------------------+
| Primary storage, shared by all nodes   |  NFS                                   |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| Connection configuration               | Mellanox 4x DDR InfiniBand adapters    |
+----------------------------------------+----------------------------------------+

| 

Sierra
======

| **SIERRA**
|  *San Diego Supercomputer Center*
| 
|  Sierra consists of 84 nodes with dual Intel L5420 processors and 2688
GB of memory. Following are detailed specifications for Sierra.
| 
|  SPECIFICATIONS
| 

+----------------------------------------+-------------------------------------------------------------------------------+
| Machine Type                           | Cluster                                                                       |
+----------------------------------------+-------------------------------------------------------------------------------+
| System Type                            | IBM iDataPlex dx 340                                                          |
+----------------------------------------+-------------------------------------------------------------------------------+
| CPU type                               | Intel Xeon L5420                                                              |
+----------------------------------------+-------------------------------------------------------------------------------+
| Host Name                              | sierra                                                                        |
+----------------------------------------+-------------------------------------------------------------------------------+
| CPU Speed                              | 2.5GHz                                                                        |
+----------------------------------------+-------------------------------------------------------------------------------+
| Number of CPUs                         | 168                                                                           |
+----------------------------------------+-------------------------------------------------------------------------------+
| Number of nodes                        | 84                                                                            |
+----------------------------------------+-------------------------------------------------------------------------------+
| RAM                                    | 32 GB DDR2-667                                                                |
+----------------------------------------+-------------------------------------------------------------------------------+
| Total RAM (GB)                         | 2688                                                                          |
+----------------------------------------+-------------------------------------------------------------------------------+
| Number of cores                        | 672                                                                           |
+----------------------------------------+-------------------------------------------------------------------------------+
| Operating System                       | Linux                                                                         |
+----------------------------------------+-------------------------------------------------------------------------------+
| Tflops                                 | 7                                                                             |
+----------------------------------------+-------------------------------------------------------------------------------+
| Disk Size (TB)                         | 72                                                                            |
+----------------------------------------+-------------------------------------------------------------------------------+
| Hard Drives                            | 160 GB Internal 7200 RPM SATA Drive                                           |
+----------------------------------------+-------------------------------------------------------------------------------+
| Primary storage, shared by all nodes   | ZFS filesystem with 76.8 TB raid2 storage and 5.4 TB of raid0 (for scratch)   |
|                                        |                                                                               |
+----------------------------------------+-------------------------------------------------------------------------------+
| Connection configuration               | Mellanox 4x DDR InfiniBand adapters                                           |
|                                        |                                                                               |
+----------------------------------------+-------------------------------------------------------------------------------+

| 

Xray
====

| **XRAY **
|  *​Indiana University, Bloomington*
| 
|  Xray consists of a single node with AMD OPteron 2378 processor and
1344 GB of memory. Following are detailed specifications for Xray.
| 
|  SPECIFICATIONS
| 

+----------------------------------------+---------------------------------+
| Machine Type                           | Cluster                         |
+----------------------------------------+---------------------------------+
| System Type                            | Cray XT5m                       |
+----------------------------------------+---------------------------------+
| CPU type                               | AMD Opteron 2378                |
+----------------------------------------+---------------------------------+
| Host Name                              | xray                            |
+----------------------------------------+---------------------------------+
| CPU Speed                              | 2.4GHz                          |
+----------------------------------------+---------------------------------+
| Number of CPUs                         | 168                             |
+----------------------------------------+---------------------------------+
| Number of nodes                        | 1                               |
+----------------------------------------+---------------------------------+
| RAM                                    | 8 GB DDR2-800                   |
+----------------------------------------+---------------------------------+
| Total RAM (GB)                         | 1344                            |
+----------------------------------------+---------------------------------+
| Number of cores                        | 672                             |
+----------------------------------------+---------------------------------+
| Operating System                       | Linux                           |
+----------------------------------------+---------------------------------+
| Tflops                                 | 6                               |
+----------------------------------------+---------------------------------+
| Disk Size (TB)                         | 335                             |
+----------------------------------------+---------------------------------+
| Hard Drives                            | 6 TB Internal Lustre Storage    |
+----------------------------------------+---------------------------------+
| Primary storage, shared by all nodes   | NFS                             |
|                                        |                                 |
+----------------------------------------+---------------------------------+
| Connection configuration               | Cray SeaStar Interconnect       |
|                                        |                                 |
+----------------------------------------+---------------------------------+

| 

Network
=======

| The FutureGrid network provides for connectivity among FutureGrid
participants, and network access to the Network Impairments Device
(NID).  Five participants connect through a variety of network providers
(see Figure 1).
|   

| |image6|
|  *Figure 1:  Diagram of FutureGrid Network*
|   
|  FutureGrid partners with XSEDE to allow participants of each to
utilize the resources of both networks. Through interconnects at the
Indiana Gigapop, Internet2 and NLR extend access to FutureGrid resources
to researchers nationally.
|   
|  FutureGrid deployed a Juniper EX8208 at the Core in Chicago’s
StarLight facility.
| 
|  |image7|
| 
|  *Figure 2: Juniper EX8208*
|   

The Juniper EX series provides for Layer2 and Layer3 connectivity. 
FutureGrid uses the EX to fulfill the network services (i.e.,
interconnectivity and external connectivity). The EX provides a special
feature labeled ‘firewall based forwarding’, allowing seamless
integration with network impairments.

|  
|  GlobalNOC at Indiana University provides network engineering
services, and the Operations Center provides email and phone support
24x7. GlobalNOC resources for public wan information can be found at
`http://noc.futuregrid.org/ <http://noc.futuregrid.org/>`__. Available
tools include:

-  **`FutureGrid
   Atlas <http://noc.futuregrid.org/futuregrid/live-network-status/maps--graphs/futuregrid-atlas.html>`__:** View
   the current level of FutureGrid Network traffic as displayed on a
   geographical map.
-  **`FutureGrid SNAPP Traffic
   Graphs <http://noc.futuregrid.org/futuregrid/live-network-status/traffic-statistics/futuregrid-snapp-trafic-graphs2.html>`__:** View
   high-speed traffic graphs collected at one-minute samples using the
   Indiana University-developed SNAPP tool. Create custom views of the
   FutureGrid network and view historic utilization with greater data
   resolution.
-  **`FutureGrid NOC Router
   Proxy <http://noc.futuregrid.org/futuregrid/live-network-status/traffic-statistics/router-proxy3.html>`__:**
   Submit show commands to the FutureGrid router.

-  **`FutureGrid Physical
   Map <http://noc.futuregrid.org/futuregrid/maps--documentation/maps.html#FutureGrid%20Physical%20Map>`__**

-  **`FutureGrid Topology
   Map <http://noc.futuregrid.org/futuregrid/maps--documentation/maps.html#FutureGrid%20Topology%20Map>`__**

| As IPv6 test beds are not available at all FutureGrid partner sites,
early implementation of iPv6 would slow important software development
work. As a result, current plans call for FutureGrid to continue using
IPv4. Any change in plans will be noted here.
| 
|  Below is further information about networking:
| 
|  FutureGrid Core: Juniper EX8200
|  India; Force10, C-150
|  Bravo, Delta, Echo; Force10, S60
|  Sierra: Juniper EX4200
|  Hotel: EX4200
|  Dlamo: Dell PowerConnect 6000 Series
|  Xray: Force10, C-150
|  foxtrot:
|  internal network switch: IBM/BLADE Rack Switch G8000
|  public network switch: Force10 S50
|  Node NICs: built-in (IBM iDataPlex DX360 M2) dual Intel 82575EB
Gigabit Network Connection
|  10Gbps: Myricom Myri-10G Dual-Protocol NIC (available on login node)
|  Alamo: Dell PowerConnett 6224
| 
|  Juniper, EX series
- `https://www.juniper.net/us/en/products-services/switching/ex-series/Force10 <https://www.juniper.net/us/en/products-services/switching/ex-series/Force10>`__ (now
Dell),
| 
|  C Series and S Series:

-  `http://www.dell.com/us/enterprise/p/force10-c150/pd <http://www.dell.com/us/enterprise/p/force10-c150/pd>`__ 
-  `http://www.dell.com/us/enterprise/p/force10-s60/pd <http://www.dell.com/us/enterprise/p/force10-s60/pd>`__

| Dell, PowerConnect
- `http://www.dell.com/us/enterprise/p/switch-powerconnect <http://www.dell.com/us/enterprise/p/switch-powerconnect>`__
|  IBM (formerly BNT)
- `http://www-03.ibm.com/systems/networking/switches/rack.html <http://www-03.ibm.com/systems/networking/switches/rack.html>`__
|   
| 
|  |image8|
|  |image9|
|   

FutureGrid Network Impairments Device (NID)
===========================================

| **FutureGrid Network Impairments Device (NID)**
| 
|  Researchers on FutureGrid may perodically employ the use of a Spirent
XGEM, a Network Impairments Emulator.  The XGEM allows users to
accurately create the delays and impairments that occur over live
production networks for validating and evaluating new products and
technologies.  The XGEM supports a variety of impairments with the most
common being delay, packet loss, jitter and re-ordering.
| 
|  |image10|
|  *Figure 1: Spirent XGEM*
|   
|  The XGEM contains two blades, each with a 10GE interface.  Traffic
received on one blade is automatically transmitted on the other blade,
and vice-versa.  This allows the XGEM to be deployed as a pass-through
device.  Impairments are applied unidirectionally.  An identical or
different impairment can be applied in either direction, or
simultaneously in both directions.
|   
|  FutureGrid also utilizes a Juniper EX8208 as the primary network
element between all of the FutureGrid participants.  Juniper’s EX
platform contains firewall-based forwarding, which allows us to insert
the XGEM between FutureGrid participants with only software changes (see
Figure 2).
| 
|  |image11|
|  *Figure 2.  Diagram of FutureGrid Network.*
|   
|  The firewall-based forwarding feature can be configured to forward
traffic unidirectionally or bidirectionally through the XGEM using a
single IP address or any size subnet.  Only traffic defined by the
Juniper EX8208 will be impaired, leaving all other traffic between
FutureGrid participants unaffected.
|   
|  This implementation requires traffic to traverse the FutureGrid Core
in order to be impaired.  Additional configuration might be required at
the participants' individual sites for impairments to occur locally.
|   

Storage
=======

Clustername(site)

Mountpoint\ ````

Size

Type

Backups

Use

Notes

`Sierra <https://portal.futuregrid.org/kb/document/bbns>`__\ (UCSD/SDSC)

/N/u/username

40.6TB

ZFS (RAID2)

Yes (nightly incremental)

Home dir

By default, quotas on home directories are 50 GB and quotas on scratch
directories are 100 GB.

/N/scratch/username

5.44TB

ZFS (RAID0)

No

Scratch

/N/soft

50GB

ZFS (RAID2)

Yes (nightly incremental)

Software installs

/N/images

6TB

ZFS (RAID2)

Yes (nightly incremental)

VM images

`India (IU) <https://portal.futuregrid.org/kb/document/bbms>`__

/N/u/username

15TB

NFS (RAID5)

Yes (nightly incremental)

Home dir

At the moment, we do not have any quota implemented on India and we use
the local/tmp (77 GB) as scratch space.

/share/project

14TB

NFS (RAID5)

Yes (nightly incremental)

Shared/group folders

/tmp

77GB

local disk

No

Scratch

`Bravo <https://portal.futuregrid.org/kb/document/bcao>`__ (IU)

/N/u/username

15TB

NFS (RAID5)

Yes (nightly incremental)

Home dir

The same NFS shares in India are mounted in Bravo (users do not log in
here; jobs are submitted through India). There are two local partitions,
which are used for HDFS and swift tests.

/share/project

14TB

NFS (RAID5)

Yes (nightly incremental)

Shared/group folders

`Delta <https://portal.futuregrid.org/kb/document/bcaj>`__ (IU)

/N/u/username

15TB

NFS (RAID5)

Yes (nightly incremental)

Home dir

Same as Bravo. The NFS shares are mounted for user and group share
(users do not log in directly here; jobs are submitted through India).

/share/project

14TB

NFS (RAID5)

Yes (nightly incremental)

Shared/group folders

Hotel (UC)

/gpfs/home

15TB

GPFS (RAID6)

No

Home dir

By default, quotas on home directories are 10 GB.

/gpfs/scratch

57TB

GPFS (RAID6)

No

Scratch

/gpfs/software

7.1GB

GPFS (RAID6)

No

Software installs

/gpfs/images

7.1TB

GPFS (RAID6)

No

VM images

/scratch/local

862GB

ext3 (local disk)

No

Local scratch

Foxtrot (UFL)

/N/u/username

16TiB

NFS (RAID5)

No

Home dir

At the moment, we do not have any quota implemented on Foxtrot.

Using HPSS from FutureGrid
==========================

**Note**: FutureGrid does not provide an HPSS server. The HSI is used to
access IU's HPSS service from INDIA. This is available only for IU
faculty, staff, and students.

Through the `SDA <http://rc.uits.iu.edu/storage/sda>`__ (formerly known
as MDSS) service, IU provides distributed storage service to faculty,
staff, and graduate students. The
`HSI <http://rc.uits.iu.edu/storage/hsi>`__ (Hierarchical Storage
Interface) client is available in INDIA. To use the HSI client:

-  First, activate your SDA account. Detailed instructions are available
   at IU's `MDSS Service Starter
   Kit <http://rc.uits.iu.edu/storage/mdss-starter-kit>`__ page.
-  Then, from INDIA, load the HSI module as follows:

::

    $ module load hsi
    hsi version 3.5.3 loaded

-  Connect to the SDA:

::

    $ hsi -A combo
    Principal: your_iu_userid                                
    [youriuid]Password:                                
    Username: your_iu_userid  UID: 1122636  Acct: 1122636(1122636) Copies: 1 Firewall: off [hsi.3.5.3 Fri Nov 20 10:01:25 EST 2009]
    ?

**Note:**\ Your Principal is your IU Network ID, and your password is
the IU passphrase.

-  Enable firewall mode; otherwise, you will receive this error:

   ::

       put: Error -5 on transfer

::

    ? firewall -on
    A: firewall mode set ON, I/O mode set to extended (parallel=off), autoscheduling currently set to OFF

-  List local folder:

::

     ? lls
    testfile.txt

-  List the current directory in HPSS:

::

    ? pwd
    pwd0: /hpss/pathtoyouriuusername

-  For transferring files (*put* and *get*), search the `IU Knowledge
   Base <http://kb.iu.edu/?search=hsi>`__.

Status
======

System Status
~~~~~~~~~~~~~

    Please note that the information on this page is not 100% accurate
    as it is maintained by hand. However, dynamic monitoring tools are
    available and can be consulted for more details.

     

Ongoing outages
~~~~~~~~~~~~~~~

    The **first Tuesday of each month** is the standard maintenance
    window.

    -  `Edit </admin/build/views/edit/active_outage_list?destination=book%2Fexport%2Fhtml%2F104#views-tab-default>`__
    -  `Export </admin/build/views/export/active_outage_list>`__
    -  `Clone </admin/build/views/clone/active_outage_list>`__

    +-----------+-------------------+-----------------------------------------------------------------------------------+--------------------+-------------------------------+------------------------------+--------------+---------------------------------------------------------------------+
    | Status    | Type              | Title                                                                             | Impacted Systems   | Start of Outage               | Anticipated End of Outage    | Resolution   | Edit link                                                           |
    +===========+===================+===================================================================================+====================+===============================+==============================+==============+=====================================================================+
    | Ongoing   | Software System   | `Bravo is reserved in 6 weeks </outages/130514/bravo-reserved-6-weeks>`__         | other              | Tue, 14 May 2013, 17:00 EDT   |                              |              | `edit </node/2513/edit?destination=book%2Fexport%2Fhtml%2F104>`__   |
    +-----------+-------------------+-----------------------------------------------------------------------------------+--------------------+-------------------------------+------------------------------+--------------+---------------------------------------------------------------------+
    | Planned   | Software System   | `Eucalyptus GUI not available </outages/120901/eucalyptus-gui-not-available>`__   | india              | Sat, 01 Sep 2012 (All day)    | Fri, 05 Oct 2012 (All day)   |              | `edit </node/2226/edit?destination=book%2Fexport%2Fhtml%2F104>`__   |
    +-----------+-------------------+-----------------------------------------------------------------------------------+--------------------+-------------------------------+------------------------------+--------------+---------------------------------------------------------------------+

You can find a list of previous outages `here </outages_all>`__
including an `RSS </feeds/fg_outages_all_rss.xml>`__ feed.

 
~

System configuration
~~~~~~~~~~~~~~~~~~~~

    The system is configured at this time using either HPC, Nimbus, or
    Eucalyptus services. The distribution used at this time can be
    found \ `here <http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp>`__ and `here <http://inca.futuregrid.org:8080/inca/jsp/status.jsp?suiteNames=Info&xsl=info.xsl>`__.

    |image12|

Status of FutureGrid services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lists the status of keyFutureGrid services (e.g., SSH, Nimbus,
    Eucalyptus) in a sortable table.

    |image13|

Cluster Monitoring
~~~~~~~~~~~~~~~~~~

    | Ganglia:
    | 
    |  |image14|

     

Network Status
~~~~~~~~~~~~~~

    The network status can be viewed via the \ `FutureGrid Network
    Operations Center page <http://noc.futuregrid.org>`__.  Upcoming
    network events are maintained on the \ `Network Operations
    Calendar <http://noc.futuregrid.org/futuregrid/support/operations-calendar3.html>`__.

    |image15|

Software Status
~~~~~~~~~~~~~~~

    The operational status of FutureGrid machines are continuously
    monitored via a number of tools. To view some of the contents,
    please
    visit \ `http://inca.futuregrid.org <http://inca.futuregrid.org>`__

     

    |image16|

Cloud Status
~~~~~~~~~~~~

`Here <https://portal.futuregrid.org/monitoring/cloud>`__ you will find
information about how FG cloud services are currently used.

    |image17|

     

FutureGrid Cloud Metrics
~~~~~~~~~~~~~~~~~~~~~~~~

    | Metric system provides an integrated accounting service to view
    cloud usage statistics and graphs regarding the utilization of
    virtual machine (VM) instances.
    |  |image18|

System software version info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    | The version info of the installed system software across
    all FG sites:
    |  |image19|

Nimbus Usage Reports
~~~~~~~~~~~~~~~~~~~~

`Displays <http://inca.futuregrid.org/nimbus-stats>`__ weekly usage
graphs of each of the FutureGrid Nimbus deployments.

    |image20|

 
~

 
~

 
~

 
~

     

Accessing FutureGrid resources via SSH
======================================

To properly view this manual page, please log into the FutureGrid portal
with your FutureGrid name.

To access the various FutureGrid resources, you need to provide a public
ssh key to FutureGrid. In this manual, we explain how to generate a ssh
key, upload it to the FutureGrid portal and log onto the resources. This
manual covers both UNIX and Windows Users.

Requirement for Windows Users
=============================

Windows users need to have some special software to be able to use the
SSH commands. We recommend you use Cygwin (Linux-like environment for
Windows) because it will ease your experience with FutureGrid. We have
prepared a Cygwin version that is ready to use (If for some reason you
decide to download and install Cygwin from the official site, remember
that you need to install the ssh packages).

#. Download Cygwin from our
   Portal \ `https://portal.futuregrid.org/sites/default/files/cygwin.zip <https://portal.futuregrid.org/sites/default/files/cygwin.zip>`__.
#. Uncompress the file.
#. Execute the file the 'Windows Batch File' called Cygwin.bat
   |image21|
     
#. You may get a warning. Click in the Run button
   |image22|
     
#. You get a Linux-like terminal that will allow you to continue with
   this manual.
   |image23|
     

**NOTE**: When showing examples of commands, the $ symbol precedes the
actual command. So, the other lines are the output obtained after
executing the command.

Instructions for both Windows and Unix users
============================================

Generate SSH key
----------------

Use the tool ssh-keygen. This program is commonly available on most UNIX
systems (this includes Cygwin). It will ask you for the location and
name of the new key. It will also ask you for a passphrase, we
**STRONGLY RECOMMEND** that you use a passphrase. We have seem advise by
teachers and teachin assistants to not use passphrases: this is
**WRONG**. If you are not using a pasphrase and someone were to steal
your private key they have easily access to your account. We recommend
using the default location ~/.ssh/ and the default name id\_rsa. A
sample session:

::

    $ ssh-keygen

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/Javi/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/Javi/.ssh/id_rsa
    Your public key has been saved in /home/Javi/.ssh/id_rsa.pub.
    The key fingerprint is:
    90:46:9b:cf:09:16:94:17:df:43:f4:99:97:0d:42:4a Javi@Javi-PC
    The key's randomart image is:

::

    +--[ RSA 2048]----+
    |     .+...Eo= .       |
    |     ..=.o + o +o    |
    |      O.  o o +.o      |
    |     o = .   . .       |
    |        S                     |
    |                                 |
    |                                 |
    |                 |
    |                                 |
    +-----------------+

This command requires the interaction of the user.

    1. The first question is:

.. code:: rteindent1

    Enter file in which to save the key (/home/Javi/.ssh/id_rsa): 

We recommend you use the default. To do so, just press the enter key. In
case you already have a ssh key in your machine, you can skip this whole
section or use a different file name.

    2. The second and third question is to protect your ssh key with a
passphrase. This password will protect your key because you need to type
it when you want to use it. Thus, you can either type a passphrase or
press enter to leave it without passphrase. To avoid security problems,
we DO recommend that chose a passphrase as discussed previously. Make
sure to not just type return for an empty passphrase.

::

    Enter passphrase (empty for no passphrase):

and

::

    Enter same passphrase again:

 

Check your ssh key
------------------

Once, you have generated your key, you should have them in the .ssh
directory

.. code:: rteindent1

    $ ls -l ~/.ssh

Copy the content of your public key
-----------------------------------

You need to copy the content of your public key to upload it to the
portal. A sample asumming that you used the default options during the
key generation:

::

    $ cat ~/.ssh/id_rsa.pub

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXJH2iG2FMHqC6T/U7uB8kt6KlRh4kUOjgw9sc4Uu+Uwe/EwD0wk6CBQMB+HKb9upvCRW/851UyRUagtlQexCRM2rMCi0VvhTVZhj61pTdhyl1t8hlkoL19JVnVBPP5kIN3wVyNAJjYBrAUNW4dXKXtmfkXp98T3OW4mxAtTH434MaT+QcPTcxims/hwsUeDAVKZY7UgZhEbiExxkejtnRBHTipi0W03W05TOUGRW7EuKf/4ftNVPilCO4DpfY44NFG1xPwHeimUk+t9h48pBQj16FrUCp0rS02Pj+4/9dNeS1kmNJu5ZYS8HVRhvuoTXuAY/UVcynEPUegkp+qYnR Javi@Javi-PC

Go ahead and select the ouptut, right click, and copy

::

    $ cat ~/.ssh/id_rsa.pub

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXJH2iG2FMHqC6T/U7uB8kt6KlRh4kUOjgw9sc4Uu+Uwe/EwD0wk6CBQMB+HKb9upvCRW/851UyRUagtlQexCRM2rMCi0VvhTVZhj61pTdhyl1t8hlkoL19JVnVBPP5kIN3wVyNAJjYBrAUNW4dXKXtmfkXp98T3OW4mxAtTH434MaT+QcPTcxims/hwsUeDAVKZY7UgZhEbiExxkejtnRBHTipi0W03W05TOUGRW7EuKf/4ftNVPilCO4DpfY44NFG1xPwHeimUk+t9h48pBQj16FrUCp0rS02Pj+4/9dNeS1kmNJu5ZYS8HVRhvuoTXuAY/UVcynEPUegkp+qYnR Javi@Javi-PC

Upload the key to the FutureGrid Portal
---------------------------------------

| Click on the button bellow to add your SSH key (Note: The quick link
button below only works if you are logged in before visiting this page.
Otherwise please make sure you login first and REFRESH this page.)
|  |image24|

#. If you were logged into the Portal, this button redirects you to a
   page that includes a link Add a public key.
#. Otherwise, this button redirects you to the login page.

   #. Log into the portal
      |image25|
        
   #. Click in the "ssh key" button
      |image26|
        

#. Click in the "add a public key" link.
   |image27|
     
#. Paste your ssh key into the box marked Key.
   |image28|
     
#. Click the submit button.

-  **IMPORTANT**:

   -  Leave the Title field blank.
   -  Make sure that when you paste your key, it does not contain
      newlines or carriage returns that may have been introduced by
      incorrect pasting and copying. If so, please remove them.

At this point you are all set. However you will still need to wait till
all accounts have been set up to use the resources. Please, check your
email for further updates. You can also refresh this page and see if the
boxes in your account status information are all green. Than you can
continue.

Testing your ssh key
--------------------

Test you key by logging onto India. India cluster gets the new ssh key
updated almost immediately. For other clusters like Hotel, it can take
around 10 minutes to update the ssh keys. If you are viewing this page
anonymously, please replace <USER> with your FutureGrid user name (the
one used to log into the Portal).

If you placed the ssh key in the default location:

::

    $ ssh -A gvonlasz@india.futuregrid.org

If you used a different path or name for your key:

::

    $ ssh -A -i <path to private key> gvonlasz@india.futuregrid.org 

The first time you ssh into a machine you will see a message like the
one shown in the picture. You have to type yes and press enter:

::

**Note**: the presence of the -A argument above is required for Nimbus
tutorials.

**Note 1**: If you are asked for a password when trying to ssh onto
Hotel, do **NOT** type any password. This means that your ssh key is not
updated yet. You need to wait a bit more.

Testing your ssh key on Hotel
-----------------------------

After uploading your ssh key, it can take around 10 minutes to update
the ssh keys of Hotel. So, if you were able to log onto India, you have
set up properly your ssh key. So, after a while you will be able to log
onto Hotel.  If you are viewing this page anonymously, Please replace
<USER> with your FutureGrid user name (the one used to log into the
Portal).

If you placed the ssh key in the default location:

::

    $ ssh -A gvonlasz@hotel.futuregrid.org

If you used a different path or name for your key:

::

    $ ssh -A -i <path to private key> gvonlasz@hotel.futuregrid.org 

The first time you ssh into a machine you will see a message like this:

::

    The authenticity of host 'hotel.futuregrid.org (149.165.148.5)' can't be established.
    RSA key fingerprint is f8:96:15:b7:21:eb:64:92:6c:de:e0:79:f3:fb:86:dd.
    Are you sure you want to continue connecting (yes/no)? yes 

**Note**: the presence of the -A argument above is required for Nimbus
tutorials.

**Note 1**: If you are asked for a password when trying to ssh onto
Hotel, do \ **NOT** type any password. This means that your ssh key is
not updated yet. You need to wait a bit more.

 

HPC Services
============

Using HPC Services on FutureGrid
================================

Accessing Systems
-----------------

| Several of the clusters that are part of FutureGrid have partitions
that operate as High Performance Computing (HPC) systems. These
partitions are batch scheduled, are not virtualized, have computer nodes
with fixed operating systems, and are suitable for running parallel
applications. FutureGrid provides a `list of HPC
partitions <http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp>`__
that currently consists of nodes on Alamo, Hotel, India, Sierra, and
Xray.
| 
|  To access the FutureGrid HPC partitions, you need a FutureGrid
account and an SSH public key you have uploaded to FutureGrid (this
process is described on our `Getting Started
page <https://portal.futuregrid.org/gettingstarted>`__). You can then
simply ssh to the login node of the FutureGrid system you would like to
use. These login nodes are named *<system>.futuregrid.org*,
specifically:

-  alamo.futuregrid.org
-  bravo.futuregrid.org
-  hotel.futuregrid.org
-  india.futuregrid.org
-  sierra.futuregrid.org
-  xray.futuregrid.org

| If your FutureGrid username is different from your username on your
system, you will need to include it in your ssh command: *ssh
<futuregrid user name>@<system>.futuregrid.org*. You can find out your
HPC account name by visiting your Portal account page.
| 

Filesystem Layout
-----------------

-  *Home* ($HOME) directories are located at */N/u/<username>*, with
   automated nightly backups. This is where users are encouraged to keep
   source files, configuration files and executables. Users should not
   run code from their $HOME directories. Please note that this is an
   NFS file system, and may result in slower access for some
   applications.
     
-  *Scratch* directories are located at different locations on the
   systems. To find out more about the file layout, please see `Storage
   information for FutureGrid
   hardware. <http://portal.futuregrid.org/kb/document/bcgv>`__
     
-  *System software* directories are located at\ */N/soft,* with
   automated nightly backups. System and community software are
   typically installed here.

Modules
-------

Resources in the FutureGrid HPC partitions have the Modules utility to
let you dynamically control your environment. Modules allows you to load
and unload packages and ensure a coherent working environment. The most
basic Modules commands let you add and remove packages from your
environment:

::

    module load <package name>/<optional package version>
    module unload <package name>/<optional package version>

To display the list of available modules:

::

    module avail

To display the list of currently loaded modules:

::

    module list

| It is very important to make sure the proper modules are loaded in the
environment before you try to use FutureGrid HPC partitions. This
ensures that your $PATH, $LD\_LIBRARY\_PATH, $LD\_PRELOAD and other
environment variables are properly set and that you can access the
programs and libraries you need. Additional information about the
Modules utility is available via 'man module' on any FutureGrid login
node.
|   

Managing Applications with Torque
---------------------------------

| To run any jobs on resources within FutureGrid HPC partitions (single
core, OpenMP or MPI jobs), users must use the job scheduler and a job
submission script. Users should NOT run jobs on the login or headnodes.
On FutureGrid machines, the job scheduler is the Torque (a variant of
PBS). To load torque into your environment, execute:

::

    -bash-3.2$ module load torque

| 
|  To run a serial job, you start by creating a job submission script
that both describes your job and will be executed on the compute nodes
by Torque. An example of a job script for India, Sierra, and Alamo that
runs */bin/hostname* is:
| 

::

    #!/bin/bash

    #PBS -N hostname_test
    #PBS -o hostname.out
    #PBS -e hostname.err
    #PBS -q short
    #PBS -l nodes=1
    #PBS -l walltime=00:20:00

    /bin/hostname

Options are passed to Torque on lines that begin with #PBS. The options
above are:

-  -N: An optional job name
-  -o: The name of the file to write stdout to
-  -e: The name of the file to write stderr to
-  -q: The queue to submit the job to
-  -l: The resources needed by the job (in the case above, 1 node for 20
   minutes)

| Additional information about the options that can be specified in a
submit script is available in the qsub manual page via 'man qsub'. Note
that there are multiple queues available on each FutureGrid system:

-  Alamo: short, long, default
-  Hotel: extended, batch, long and route
-  India: scalemp, batch, long and b534
-  Sierra: batch and long
-  Xray: batch

You can find information (such as limits) that will help you select
which queue to use by running qstat -q on the login node for the system
you are interested in.

Once you have created a submission script, you can then use the Torque
qsub command to submit this job to be executed on the compute nodes:

::

    -bash-3.2$ qsub ring.sh
    19095.master1.cm.cluster

The qsub command outputs either a job identifier or an error message
describing why Torque would not accept your job. If your job is
submitted successfully, you can track its execution using the qstat
command:

::

    -bash-3.2$ qstat
    Job id                    Name             User            Time Use S Queue
    ------------------------- ---------------- --------------- -------- - -----
    ...
    19095.master1             hostname_test    user            00:00:00 R short
    ...

If the system is busy, your job will initially be queued (Q) waiting for
resources to become available. It will then be in the running state (R),
and finally it will complete and not be visible in the qstat output. The
full set of Torque job states is provided in the qstat manual page via
man qstat on a FutureGrid login node. The stdout and stderr from your
job will be placed in the files you specified in your submission script.

A final Torque command you will use occasionally is the qdel command
that asks Torque to delete a job. If the job hasn't begun running, it is
simply deleted from the queue. If the job has begun, it is killed on the
nodes it's running on, and deleted from the queue.

A list of all available Torque commands is available from the `Torque
manual page <http://www.clusterresources.com/torquedocs21/>`__.

 

Message Passing Interface (MPI)
-------------------------------

| The Message Passing Interface Standard (MPI) is a message passing
library standard based on the consensus of the MPI Forum, which has
dozens of participating organizations, including vendors, researchers,
software library developers, and users. The goal of the Message Passing
Interface is to establish a portable, efficient, and flexible standard
for message passing that will be widely used for writing message passing
programs. MPI is the *de facto* standard communication library for
almost all HPC systems, and is available in a variety of
implementations.
| 
|  For more information, please visit:

-  `http://www.mpi-forum.org/ <http://www.mpi-forum.org/>`__
-  `http://www.mcs.anl.gov/research/projects/mpi/tutorial/ <http://www.mcs.anl.gov/research/projects/mpi/tutorial/>`__

| 
|  For more information on OpenMPI, the default MPI distribution on
FutureGrid, please visit:

-  `http://www.open-mpi.org/ <http://www.open-mpi.org/>`__

| 

MPI Libraries
-------------

| 
|  The FutureGrid systems that support HPC-style usage have an MPI
implementation. In most cases, it is OpenMPI-1.4.x compiled with Intel
11.1 compilers. 
| 

+--------------+-------------------+----------------+--------------------------+-----------------------------+
| **System**   | **MPI version**   | **Compiler**   | **Infiniband Support**   | **Module**                  |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Alamo        | OpenMPI 1.4.3     | Intel 11.1     | yes                      | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Bravo        | OpenMPI 1.4.2     | Intel 11.1     | no                       | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
|              | OpenMPI 1.4.3     | gcc 4.4.6      | no                       | openmpi/1.4.3-gnu           |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
|              | OpenMPI 1.4.3     | Intel 11.1     | no                       | openmpi/1.4.3-intel         |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
|              | OpenMPI 1.5.4     | gcc 4.4.6      | no                       | openmpi/1.5.4-[gnu,intel]   |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Hotel        | OpenMPI 1.4.3     | gcc 4.1.2      | yes                      | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| India        | OpenMPI 1.4.2     | Intel 11.1     | yes                      | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Sierra       | OpenMPI 1.4.2     | Intel 11.1     | no                       | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Xray         |                   |                | N/A                      |                             |
+--------------+-------------------+----------------+--------------------------+-----------------------------+

| 
|  In cases where the OpenMPI is compiled with the Intel compilers,
loading the OpenMPI module will automatically load the Intel compilers
as a dependency:

.. code:: rteindent1

    -bash-3.2$ module load openmpi
    Intel compiler suite version 11.1/072 loaded
    OpenMPI version 1.4.3 loaded

| Loading the OpenMPI module adds the MPI compilers to your $PATH
environment variable and the OpenMPI shared library directory to your
$LD\_LIBRARY\_PATH. This is an important step to ensure MPI applications
will compile and run successfully. Loading the torque module allows you
to submit jobs to the scheduler.
|   

Compiling MPI Applications
--------------------------

To compile MPI applications, users have two options:

#. Use the MPI compilers instead of regular Intel/GNU compilers
#. Use the regular compilers (Intel/GNU) with MPI compilation flags

We recommend using the MPI compilers to avoid compilation issues. This
is accomplished by making the following replacements:

-  CC/icc/gcc with mpicc
-  CXX/icpc/g++ with mpicxx
-  F90/F77/FC/ifort/gfortran with mpif90

| Alternatively, for some codes that require intricate compilation flags
and complicated make systems, and where changing compilers is not an
option, you can edit the compilation/linking options for your codes.
These options are machine, compiler, and language dependent. To view the
options required for C, C++ and Fortran on any machine, you can issue
the commands mpicc-show, mpicxx-show, and mpif90-show. Extra care must
be taken when using these flags, as dependencies govern the order in
which they appear in the link line. Should you run into compilation
errors or problems, please submit a consulting ticket.
| 
|  Assuming you have loaded the openmpi module into your environment,
you can compile a `simple MPI application </tutorials/hpc/ring>`__ as
easily as executing:

.. code:: rteindent1

    -bash-3.2$ mpicc -o ring ring.c

| 

Running MPI Applications
------------------------

| Once your MPI application is compiled, you run it on the compute nodes
of a cluster via Torque. An example of an MPI parallel job script for
India, Sierra, and Alamo that runs the ring application is:
| 

.. code:: rteindent1

    #!/bin/bash

    #PBS -N ring_test
    #PBS -o ring_$PBS_JOBID.out
    #PBS -e ring_$PBS_JOBID.err
    #PBS -q short
    #PBS -l nodes=4:ppn=8
    #PBS -l walltime=00:20:00

    # make sure MPI is in the environment
    module load openmpi

    # launch the parallel application with the correct number of processs
    # Typical usage: mpirun -np <number of processes> <executable> <arguments>
    mpirun -np 32 ring -t 1000

| There are two important differences between this script and the submit
script shown previously. The first is that :ppn=8 is added to the
request for four nodes. What this does is indicate that your application
wants to allocate eight virtual processors per node. A virtual processor
corresponds to a processing core. Alamo, Hotel, India, and Sierra all
have eight cores per node, so the script above asks for exclusive access
to four nodes with a total of 32 cores. The second importand difference
from the previous submit script is that it executes mpirun with
arguments that describe your MPI application. Note that the number of
processes specified to mpirun is 32—matching the 32 cores allocated by
Torque.
| 
|  A minor difference between this script and the previous one is that
the environment variable $PBS\_JOBID is used when creating the stdin and
stdout files. Torque sets a number of environment variables that you can
use in your submit script, starting with PBS\_ .

Log in to HPC services
======================

 

To access a FutureGrid system via Torque/Moab, you should ssh to the
login node for the system. The login node is one of the following:

-  india.futuregrid.org
-  bravo.futuregrid.org
-  sierra.futuregrid.org
-  foxtrot.futuregrid.org
-  hotel.futuregrid.org
-  alamo.futuregrid.org
-  xray.futuregrid.org

An example session follows:

    ::

        $ ssh sierra.futuregrid.org
        Last login: Thu Aug 12 19:19:22 2010 from ....
        Welcome to Sierra.FutureGrid.Org
        $

Once you ssh into these nodes, you'll have access to the HPC queuing
services for the machine you have logged into. You will enter into a
Unix/Linux shell in which you can enter the typical Unix commands.
However, access to the clusters is provided through Torque/Moab commands
from the command line. 

Generating SSH Keys for FutureGrid Access
=========================================

 

Key Generation
==============

To gain access to FutureGrid Resources including HPC and Nimbus
services, you need to provide a public key to FutureGrid. We recommend
that you are familiar with public keys and have the understanding that
we do REQUIRE passphrase protected keys. To generate and send such a
key, please follow the following steps. To find more out about open
ssh you can also go to 

-  `http://openssh.com/manual.html <http://openssh.com/manual.html>`__

Other good resources include 

-  http://help.github.com/key-setup-redirect
-  http://help.github.com/working-with-key-passphrases/
-  http://www.dribin.org/dave/blog/archives/2007/11/28/ssh\_agent\_leopard/

**1. **\ **Generate Public/Private Key Pair**
---------------------------------------------

First, you have to generate a key. You do this as follows:

-  Step 1: use the command “ssh-keygen -t rsa -C <your-e-mail>” to
   generate the key
-  Step 2: specifiy the KeyPair location and name. We recommend that you
   use the default location if you do not yet have another key there.
    e.g. /home/username/.ssh/id\_rsa
-  Step 3: type user defined passphrase when asking passphrase for the
   key

Example:

.. code:: rteindent1

    ssh-keygen -t rsa -C johndoe@indiana.edu

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/johndoe/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/johndoe/.ssh/id_rsa.
    Your public key has been saved in /home/johndoe/.ssh/id_rsa.pub.
    The key fingerprint is:
    34:87:67:ea:c2:49:ee:c2:81:d2:10:84:b1:3e:05:59 johndoe@indiana.edu

**2. **\ **List the result**
----------------------------

| You can find your key under the key location. As we user the .ssh
directory it will be located there. 
|   

.. code:: rteindent1

    $ls -lisa ~/.ssh
    -rw-------  1 johndoe johndoe        1743 2011-02-10 09:44 id_rsa
    -rw-r--r--  1 johndoe johndoe         399 2011-02-10 09:44 id_rsa.pub

 

**3. **\ **Add or Replace Passphrase for an Already Generated Key**
-------------------------------------------------------------------

In case you need to change your change passphrase, you can simply run
“ssh-keygen -p” command. Then specify the location of your current key,
and input (old and) new passphrases. There is no need to re-generate
keys.

.. code:: rteindent1

    ssh-keygen -p

    Enter file in which the key is (/home/johndoe/.ssh/id_rsa):
    Enter old passphrase:
    Key has comment '/home/johndoe/.ssh/id_rsa'
    Enter new passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved with the new passphrase.  

 

**4.**  **Capture the Public Key for FutureGrid**
-------------------------------------------------

Use a text editor to open the “id\_rsa.pub”. Copy the **entire**
contents of this file into the ssh key field as part of your profile
information. You can now add this key to your keys at the following
page:

5. Key Management
-----------------

This is a future section that will include material about how to use
ssh-add and keychain. You can find instructions on them via the
github link that we provided above. However, we are not github ;-)

6. Resetting the SSH key
------------------------

Please follow the instructions given at 

-  `https://portal.futuregrid.org/how-do-i-reset-my-ssh-key <https://portal.futuregrid.org/how-do-i-reset-my-ssh-key>`__

 

7. I still can not access FG resources
--------------------------------------

| In order for you to access FG resources you must be in an active
project. Please make sure you join a project or create your own while
applying for one.
|   

 

 
=

 

Working with HPC Job Services
=============================

 

Running Queued Jobs as Part of the HPC Services
-----------------------------------------------

To run a job in the HPC service, you need to create a job script that
tells the job manager how to run the job and how to handle things like
output and notifications. You can then submit your job to the scheduler,
monitor its progress in the job queue, and examine the output when it
finishes.

 A Simple Job Script
~~~~~~~~~~~~~~~~~~~~

An example job script looks like this:

    ::

        #!/bin/bash
        #PBS -N testjob 
        #PBS -l nodes=1:ppn=1 
        #PBS -q batch 
        #PBS -j oe 
        ##PBS -M username@example.com 
        ##PBS -m ae ##PBS -o testjob.out 
        ## 
        ## Everything following is run by the scheduler 
        ## 
        sleep 10 
        echo -n "Host operating system version: " 
        uname -a 
        echo "Nodes allocated to this job: " 
        cat $PBS_NODEFILE 
        echo 
        sleep 10 
        ## 
        ## End of job script 
        ##

In the job script, lines that begin with \ **#PBS** are directives to
the job scheduler. You can disable any of these lines by adding an
extra \ **#**\ character at the beginning of the line, for example:

    ::

        ##PBS -M username@example.com

This job script shows some common examples of directives that you might
want to use in your job scripts. The directives in this job script are
described below:

    ::

        #!/bin/bash 

This line isn't strictly required, but it is added as a fail-safe in
case something unexpected happens. Normally, the job manager reads your
script and processes the directives, and then runs your script as a
normal shell script. This simply ensures that the system uses the
standard bash shell to run your script.

    ::

        #PBS -N testjob 

This line gives your job a name of \ **testjob**. This name will be used
by the job manager when it shows a job listing, and will be used for
your output file(s) unless you explicitly specify an output file.

    ::

        #PBS -l nodes=1:ppn=1 

This line tells the job manager what your job requires for resources. In
this case, your job is asking for one node (**nodes=1**) and at least
one processor per node (**ppn=1**). See the
[[Sw:Manual/PBSDirectives\|PBSDirectives] page for other options you can
specify here.

    ::

        #PBS -q batch 

This line tells the job manager which job queue your job should be sent
to. Each job queue has different characteristics, such as the maximum
time a job is allowed to run, or the maximum number of nodes a job can
use.

    ::

        #PBS -j oe 

This line tells the job manager to join the job standard output and
standard error into a single file. For jobs with a small amount of
output, this is usually helpful. If your job produces a lot of standard
output, it may be helpful to keep the files separate so you can easily
locate error messages in the single error file.

    ::

        ##PBS -M username@example.com 

Note that this line is a comment since it starts with \ **##** instead
of \ **#PBS**. If you remove the first \ **#**, this line will set the
email address that will get notified about events related to this job.
The events that get reported are set by the next line.

    ::

        ##PBS -m ae 

Again, note that this line is commented out. If you remove the
first \ **#**, this line will send email whenever the job fails
(or **a**\ borts) (**a** option), and when the job ends (**e** option).
This is particularly helpful if your job has to wait a long time in the
queue before it runs.

    ::

        ##PBS -o testjob.out 

Again, note that this line is commented out. If you remove the
first \ **#**, this line will specify the file name to be used for job
output.

  Submitting Your Job
~~~~~~~~~~~~~~~~~~~~~

You can submit your job with the \ **qsub** or **msub** commands.
The \ **msub** and **qsub** are almost identical, and can mostly be used
interchangeably. See the respective man pages for specific differences.
Neither submission command provides much output. Examples of a job
submission using both commands follows:

Using \ **msub**:

    ::

        [62]s1::gpike> msub testjob.pbs 
        292250 
        [63]s1::gpike>

Using \ **qsub**:

    ::

        [63]s1::gpike> qsub testjob.pbs 
        292251.s82 
        [64]s1::gpike>

In both cases, the number that gets returned is the job number that the
scheduler assigned to your job. In the case of \ **qsub**, the job
number is followed by the host name where you submitted the job.

Monitoring Your Job
-------------------

To monitor your job after it has been submitted, you can use
the \ **qstat** or **showq** commands. Both commands will show you the
state of the job manager, but the information is displayed in different
formats. In general, the \ **showq** command gives more complete
information, and in a form that is a bit easier to read.
The \ **qstat** command gives a very concise listing of the job queue,
and in some instances this may give you a better quick overview of the
resource.

Using the test job script as an example, here is the output from
the \ **showq** command:

    ::

        [66]s1::gpike> showq 
        active jobs
        ------------------------ 
        JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME 
        292252   greg       Running     16        3:59:59 Tue Aug 17 09:02:40 
        1 active job 16 of 264 processors in use by local jobs (6.06%) 
                          2 of 33 nodes active (6.06%) eligible jobs
        ----------------------
        JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME
        0 eligible jobs blocked jobs
        ----------------------- 
        JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME
        0 blocked jobs 
        Total job: 1 

You can see the output is divided into three sections: \ **active
jobs**, \ **eligible jobs**, and \ **blocked jobs**.

**1. Active jobs** are jobs that are currently running on the resource.

**2.**\ **Eligible jobs** are jobs that are waiting for nodes to become
available before they can run. As a general rule, jobs are listed in the
order that they will be scheduled, but scheduling algorithms may change
the order over time.

**3.**\ **Blocked jobs** are jobs that the scheduler cannot run for some
reason. Usually a job becomes blocked because it is requesting something
that is impossible, such as more nodes than currently exist, or more
processors per node than are installed.

 

Using the test job as an example again, here is the output from
the \ **qstat** command:

    ::

        [109]i136::gpike> qstat 
        Job id                             Name               User          Time Use S Queue 
        ------------------------- --------------------- ------------------- -------- - ----- 
        1981.i136                       sub19327.sub      inca               00:00:00 C batch 
        1982.i136                       testjob           greg                      0 R batch 

The \ **qstat** command provides output in six columns:

#. Job id is the identifier assigned to your job.
#. Name is the name that you assigned to your job.
#. User is the username of the person who submitted the job.
#. Time Use is the amount of time the job has been running.
#. S shows the job state. Common job states are R for a running job, Q
   for a job that is queued and waiting to run, C for a job that has
   completed, and H for a job that is being held.
#. Queue is the name of the job queue where your job will run.

 

Examining Your Job Output
-------------------------

If you gave your job a name with the \ **#PBS -N <jobname>** directive
in your job script or by specifying the job name on the command line,
your job output will be available in a file named \ **jobname.o######**,
where the \ **######** is the job number assigned by the job manager.
You can type \ **ls jobname.o\*** to see all output files from the same
job name.

If you explicitly name an output file with the \ **#PBS -o
<outfile>** directive in your job script or by specifying the output
file on the command line, your output will be in the file you specified.
If you run the job again, the output file will be overwritten.

If you don't specify any output file, your job output will have the same
name as your job script, and will be numbered in the same manner as if
you had specified a job name (**jobname,o######**).

Analyzing Code Performance
==========================

PAPI
====

|image29|

**Summary**

`PAPI <http://icl.cs.utk.edu/papi/overview/index.html>`__ is an acronym
for \ **P**\ erformance \ **A**\ pplication \ **P**\ rogramming \ **I**\ nterface.
The PAPI Project is being developed at the Computer Science Department
of the \ `University of Tennessee’s Innovative Computing
Laboratory <http://icl.cs.utk.edu/>`__. This project was created to
design, standardize, and implement a portable and efficient API
(Application Programming Interface) to access the hardware performance
counters found on most modern microprocessors.  For more information,
please see the user guides listed below.  `Read more
... <http://icl.cs.utk.edu/projects/papi/wiki/User_Guide>`__

**Availability**

PAPI 4.2.0 is available on the Bravo machine and PAPI version 3.6.2.2 is
available on the Xray machine. To load PAPI on Bravo, 'module add papi'
as below:

    ``% module add papi         papi version 4.2.0 loaded     % env | grep papi     MANPATH=/opt/papi-4.2.0/man:/usr/share/man          LD_LIBRARY_PATH=/opt/papi-4.2.0/lib:/N/u/inca/openssl/lib:         PATH=/opt/papi-4.2.0/bin:...         PAPI_ROOT=/opt/papi-4.2.0``

To load PAPI on Xray, type 'module add xt-papi' as below:

    ``% module add xt-papi     % env | grep PAPI     PAPI_POST_LINK_OPTS= -L/opt/xt-tools/papi/3.6.2.2/lib -lpapi -lpfm     PAPI_VERSION=3.6.2.2     PAPI_INCLUDE_OPTS= -I/opt/xt-tools/papi/3.6.2.2/include``

Our plans are to make PAPI 4.2.0 available on Alamo, India, Sierra, and
Hotel when the machines are upgraded to Redhat 6.

 

**PAPI User Guide**

-  `User Guide <http://icl.cs.utk.edu/projects/papi/wiki/User_Guide>`__

 

Vampir
======

**Introduction**

Performance optimization is a key issue for the development of efficient
parallel software applications. Vampir provides a manageable framework
for analysis, which enables developers to quickly display program
behavior at any level of detail. Detailed performance data obtained from
a parallel program execution can be analyzed with a collection of
different performance views. Intuitive navigation and zooming are the
key features of the tool, which help to quickly identify inefficient or
faulty parts of a program code. Vampir implements optimized event
analysis algorithms and customizable displays which enable a fast and
interactive rendering of very complex performance monitoring data.
Ultra-large data volumes can be analyzed with a parallel version of
Vampir, which is available on request. Vampir has a product history of
more than 15 years and is well established on Unix-based HPC systems.
This tool experience is now available for HPC systems that are based on
Microsoft Windows HPC Server 2008. This new Windows edition of Vampir
combines modern scalable event processing techniques with a fully
redesigned graphical user interface.

**Vampir on FutureGrid**
------------------------

VampirServer is currently available on India
at /N/soft/x86\_64/el5/india/vampirserver.  The VampirTrace modules are
installed on Alamo, Hotel, India, and Sierra.  To load, type 'module
load vampirtrace'. 

**Event-based Performance Tracing and Profiling**
-------------------------------------------------

In software analysis, the term profiling refers to the creation of
tables which summarize the runtime behavior of programs by means of
accumulated performance measurements. Its simplest variant lists all
program functions in combination with the number of invocations and the
time that was consumed. This type of profiling is also called inclusive
profiling, as the time spent in subroutines is included in the
statistics computation. A commonly applied method for analyzing details
of parallel program runs is to record so-called trace log files during
runtime. The data collection process itself is also referred to as
tracing a program. Unlike profiling, the tracing approach records timed
application events like function calls and message communication as a
combination of timestamp, event type, and event specific data. This
creates a stream of events, which allows very detailed observations of
parallel programs. With this technology, synchronization and
communication patterns of parallel program runs can be traced and
analyzed in terms of performance and correctness. The analysis is
usually carried out in a postmortem step, i. e., after completion of the
program. Needless to say, program traces can also be used to calculate
the profiles mentioned above. Computing profiles from trace data allows
arbitrary time intervals and process groups to be specified. This is in
contrast to *fixed profiles accumulated during runtime.*

**The Open Trace Format (OTF)**
-------------------------------

The Open Trace Format (OTF) was designed as a well-defined trace format
with open, public domain libraries for writing and reading. This open
specification of the trace information provides analysis and
visualization tools like Vampir to operate efficiently at large scale.
The format addresses large applications written in an arbitrary
combination of Fortran77, Fortran (90/95/etc.), C, and C++.

|image30|

**Representation of Streams by Multiple Files**

| OTF uses a special ASCII data representation to encode its data items
with numbers and tokens in hexadecimal code without special prefixes.
That enables a very powerful format with respect to storage size, human
readability, and search capabilities on timed event records. In order to
support fast and selective access to large amounts of performance trace
data, OTF is based on a stream-model, i.e., single separate units
representing segments of the overall data. OTF streams may contain
multiple independent processes, whereas a process belongs to a single
stream exclusively. As shown in the figure, each stream is represented
by multiple files, which store definition records, performance events,
status information, and event summaries separately. A single global
master file holds the necessary information for the process to stream
mappings. Each file name starts with an arbitrary common prefix defined
by the user. The master file is always named {name}.otf. The global
definition file is named {name}.0.def. Events and local definitions are
placed in files {name}.x.events and {name}.x.defs, where the latter
files are optional. Snapshots and statistics are placed in files named
{name}.x.snaps and {name}.x.stats, which are also optional.
| 
|  **Note**: Open the master file (\*.otf) to load a trace. When
copying, moving, or deleting traces, it is important to take all
according files into account; otherwise, Vampir will render the whole
trace invalid! Good practice is to hold all files belonging to one trace
in a dedicated directory. Detailed information about the Open Trace
Format can be found in the `*Open Trace Format
(OTF)* documentation <http://www.tu-dresden.de/zih/otf%20>`__.

**Getting Started**
===================

**Generation of Trace Data**
----------------------------

The generation of trace files for the (Vampir) performance visualization
tool requires a working monitoring system to be attached to your
parallel program. Contrary to Windows HPC Server 2008 — whereby the
performance monitor is integrated into the operating system — recording
performance under Linux is done by a separate performance monitor. We
recommend our VampirTrace monitoring facility, which is available as
open source software. During a program run of an application,
VampirTrace generates an OTF trace file, which can be analyzed and
visualized by Vampir. The VampirTrace library allows MPI communication
events of a parallel program to be recorded in a trace file.
Additionally, certain program-specific events can also be included. To
record MPI communication events, simply relink the program with the
VampirTrace library. A new compilation of the program source code is
only necessary if program-specific events should be added. Detailed
information on the installation and usage of VampirTrace can be found at
`VampirTrace <https://portal.futuregrid.org/manual/vampir/trace>`__.

**Enabling Performance Tracing**
--------------------------------

To perform measurements with VampirTrace, the application program needs
to be instrumented. VampirTrace handles this automatically by default,
while manual instrumentation is also possible. All the necessary
instrumentation of user functions, MPI, and OpenMP events is handled by
the compiler wrappers of VampirTrace (vtcc, vtcxx, vtf77, vtf90). All
compile and link commands in the used makefile should be replaced by the
VampirTrace compiler wrapper, which performs the necessary
instrumentation of the program and links the suitable VampirTrace
library. Automatic instrumentation is the most convenient method to
instrument your program. Therefore, simply use the compiler wrappers
without any parameters, e.g.:

    ::

        vtf90 hello.f90 -o hello

For manual instrumentation with the VampirTrace API, simply include:

    ::

        vt_user.inc (Fortran)

        vt_user.h (C, C++)

and label any user defined sequence of statements for instrumentation as
follows:

    ::

        VT_USER_START(name) ... VT_USER_END(name)

in Fortran and C, respectively, and in C++ as follows:

    ::

        VT_TRACER(``name);

Afterwards, use

    ::

        vtcc -DVTRACE hello.c -o hello

to combine the manual instrumentation with automatic compiler
instrumentation or

    ::

        vtcc -vt:inst manual -DVTRACE hello.c -o hello

to prevent an additional compiler instrumentation.

**Tracing an Application**
--------------------------

Running a VampirTrace instrumented application should normally result in
an OTF trace file in the current working directory where the application
was executed. On Linux, Mac OS, and Sun Solaris, the default name of the
trace file will be equal to the application name. For other systems, the
default name is \ *a.otf* but can be defined manually by setting the
environment variable VT\_FILE\_PREFIX to the desired name. After a run
of an instrumented application, the traces of the single processes need
to be unified in terms of timestamps and event IDs. In most cases, this
happens automatically. If it is necessary to perform unification of
local traces manually, use the following command:

    ::

        vtunify <nproc>

If VampirTrace was built with support for OpenMP and/or MPI, it is
possible to speed up the unification of local traces significantly. To
distribute the unification on multiple processes, the MPI parallel
version vtunify-mpi can be used as follows:

    ::

        mpirun -np <nranks> vtunify-mpi <nproc>

**Starting Vampir and Loading a Trace File**
--------------------------------------------

To open a trace file, from the "File" menu, select "Open...". This will
provide the file-open dialog depicted below. It is possible to filter
the files in the list. The file type input selector determines the
visible files. The default "OTF Trace Files (\*.otf )" shows only files
that can be processed by the tool. All file types can be displayed by
using "All Files (\*)". Alternatively, on Windows, a command-line
invocation is possible:

    ::

        C:\Program Files\Vampir\Vampir.exe [trace file]

To open multiple trace files at once, you can take them one after
another as command-line arguments:

    ::

        C:\Program Files\Vampir\Vampir.exe [file 1]...[file n]

It is also possible to start the application by double-clicking on an
\*.otf file (if Vampir was associated with \*.otf files during the
installation process). The trace files to be loaded have to be compliant
with the Open Trace Format (OTF) standard. Microsoft HPC Server 2008 is
shipped with the translator program etl2otf.exe, which produces
appropriate input files.

|image31|

**Loading a Trace Log File in Vampir**

While Vampir is loading the trace file, an empty "Trace View" window
with a progress bar at the bottom opens. After Vampir loaded the trace
data completely, a default set of charts will appear. The illustrated
loading process can be interrupted at any point of time by clicking on
the cancel button in the lower right corner. Because events in the trace
file are traversed one after another, the GUI will also open, but will
show only the earliest information from the tracefile. For huge
tracefiles with performance problems assumed to be at the beginning,
this proceeding is a suitable strategy to save time.

|image32|

**Progress Bar and Cancel Loading Button**

Basic functionality and navigation elements are described
in \ `Basics <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Basics>`__.
The available charts and the information provided by them are explained
in \ `Performance\_Data\_Visualization <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Performance_Data_Visualization>`__.

 

 

**Basics**
==========

After loading has been completed, the \ *Trace View* window title
displays the trace file's name. By default, the \ *Charts* toolbar and
the \ *Zoom Toolbar* are available.

|image33|

**Trace View Window with Charts Toolbar (A) and Zoom Toolbar (B)**

Furthermore, the default set of charts is opened automatically after
loading has been finished. The charts can be divided into three groups:
timeline, statistical, and informational charts. Timeline charts show
detailed event-based information for arbitrary time intervals, while
statistical charts reveal accumulated measures computed from the
corresponding event data. Informational charts provide additional or
explanatory information regarding timeline and statistical charts. All
available charts can be opened with the \ *Charts*\ toolbar (explained
in `The Charts
Toolbar <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#The_Charts_Toolbar>`__).
In the following section, we will explain the basic functions of the
Vampir GUI which are generic to all charts.

**Chart Arrangement**
---------------------

The utility of charts can be increased by correlating them and their
provided information. Vampir supports this mode of operation by allowing
you to display multiple charts at the same time. Charts that display a
sequence of events such as the \ *Master Timeline* and the \ *Process
Timeline*\ chart are aligned vertically. This alignment ensures that the
temporal relationship of events is preserved across chart boundaries.
The user can arrange the placement of the charts according to his
preferences by dragging them into the desired position. When the left
mouse button is pressed while the mouse pointer is located above a
placement decoration, the layout engine will give visual clues as to
where the chart may be moved. As soon as the user releases the left
mouse button, the chart arrangement will be changed according to his
intentions. The entire procedure is depicted in figures below. The
flexible display architecture also allows increasing or decreasing the
screen space that is used by a chart. Charts of particular interest may
get more space in order to render information in more detail.

|image34|

**Moving and Arranging Charts in the Trace View Window**

|image35|

**Moving and Arranging Charts in the Trace View Window**

|image36|

**A Custom Chart Arrangement in the Trace View Window**

|image37|

**Closing (right) and Undocking (left) a Chart**

The \ *Trace View* window can host an arbitrary number of charts. Charts
can be added by clicking on the respective \ *Charts* toolbar icon or
the corresponding \ *Chart* menu entry. With a few more clicks, charts
can be combined to a custom chart arrangement. Customized layouts can be
saved as described in \ `Saving
Policy <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Saving_Policy>`__.
Every chart can be undocked or closed by clicking the dedicated icon in
its upper right corner. Undocking a chart means to free the chart from
the current arrangement and present it in its own window.

|image38|

**Undocking of a Chart**

|image39|

**Docking a Chart**

Considering that labels (e.g., those showing names or values of
functions) often need more space to show their whole text, there is a
further form of resizing/arranging. In order to read labels completely,
it is possible to resize the distribution of space owned by the labels
and the graphical representation in a chart. When one hovers over the
blank space between labels and graphical representation, a moveable
separator appears. After clicking a separator decoration, moving the
mouse while holding the left mouse button causes resizing.

|image40|

**Resizing Labels: (A) Hover over a Separator Decoration; (B) Drag and
Drop the Separator**

**Context Menus**
-----------------

All of the chart displays have their own context menus with common
entries as well as display-specific ones. In the following section, only
the most common entries will be discussed. A context menu can be
accessed by right clicking in the display window. Common entries are:

-  **Reset Zoom:** Go back to the initial state in horizontal zooming.
-  **Reset Vertical Zoom:** Go back to the initial state in vertical
   zooming.
-  **Set Metric:** Change values which should be represented in the
   chart, e.g. *Exclusive Time* to *Inclusive Time*.
-  **Sort By:**\ Rearrange values or bars by a certain characteristic.

**Zooming**
-----------

Zooming is a key feature of Vampir. In most charts it is possible to
zoom in and out to get abstract and detailed views of the visualized
data. In the timeline charts, zooming produces a more detailed view of a
special time interval and therefore reveals new information that could
not be seen in the larger section. Short function calls in the \ *Master
Timeline* may not be visible unless an appropriate zooming level has
been reached. If the execution time of these short functions is too
short regarding the pixel resolution of your computer display, the
selection of a shorter time interval is required. Note: Other charts can
be affected when zooming in timeline displays: The interval chosen in a
timeline chart such as \ *Master Timeline* or *Process Timeline* also
defines the time interval for the calculation of accumulated
measurements in the statistical charts. Statistical charts like
the \ *Function Summary* provide zooming of statistic values. In these
cases zooming does not affect any other chart. Zooming is disabled in
the \ *Pie Chart* mode of the \ *Function Summary* reachable via context
menu under \ *Set Chart Mode->Pie Chart*.

|image41|

**Zooming within a Chart**

To zoom into an area, click and hold the left mouse button and select
the area. It is possible to zoom horizontally and in some charts also
vertically. Horizontal zooming in the \ *Master Timeline* defines the
time interval to be visualized whereas vertical zooming selects a group
of processes to be displayed. To scroll horizontally move the slider at
the bottom or use the mouse wheel. Additionally, the zoom can be
accessed with help of the \ *Zoom Toolbar* by dragging the borders of
the selection rectangle or scrolling down the mouse wheel. To return to
the previous zooming state, the global "Undo" is provided that in the
"Edit" menu; alternatively, press "Ctrl+Z" to revert to the last zoom.
Accordingly, a zooming action can be repeated by selecting "Redo" in the
"Edit" menu or pressing "Ctrl+Shift+Z". Both functions work
independently of the current mouse position. Next to "Undo" and "Redo"
it is shown which kind of action in which display could be undone and
redone, respectively. To get back to the initial state of zooming in a
fast way select \ *Reset Horizontal Zoom* or *Reset Vertical Zoom* in
the context menu of the desired timeline display. To reset zoom is also
an action that can be reverted by "Undo".

**The Zoom Toolbar**
--------------------

| Vampir provides a \ *Zoom Toolbar* that can be used for zooming and
navigation in the trace data. It is situated in the upper right corner
of the *Trace View* window. Of course it is possible to drag and drop it
as desired. The \ *Zoom Toolbar* offers an overview of the data
displayed in the corresponding charts. The current zoomed area can be
seen highlighted as a rectangle within the \ *Zoom Toolbar*. Clicking on
one of the two boundaries and moving it (with left mouse button held) to
the intended position executes horizontal zooming in all charts.
|  **Note**: Instead of dragging boundaries, it is also possible to use
the mouse wheel for zooming. Hover over the \ *Zoom Toolbar* and scroll
up to zoom in and scroll down to zoom out. Dragging the zoom area
changes the section that is displayed without changing the zoom factor.
For dragging, click in the highlighted zoom area and drag and drop it to
the desired region. If the user double clicks in the \ *Zoom Toolbar*,
the initial zooming state is reverted to.

|image42|

**Zooming and Navigation within the Zoom Toolbar: (A+B) Zooming in/out
with Mouse Wheel; (C) Scrolling by Moving the Highlighted Zoom Area; (D)
Zooming by Selecting and Moving a Boundary of the Highlighted Zoom
Area**

The colors represent user-defined groups of functions or activities.
Please note that all charts added to the \ *Trace View* window will
adapt their statistics information according to this time interval
selection. The \ *Zoom Toolbar* can be disabled and enabled with the
toolbar's context menu entry \ *Zoom Toolbar*.

**The Charts Toolbar**
----------------------

Use the \ *Charts* toolbar to open instances of the different charts. It
is situated in the upper left corner of the main window by default. Of
course, it is also possible to drag and drop it as desired.
The \ *Charts* toolbar can be disabled with the toolbar's context menu
entry \ *Charts*. The table below shows the different icons representing
the charts in \ *Charts* toolbar. The icons are arranged in three
groups, divided by a small separator. The first group represents
timeline charts, whose zooming states affect all other charts. The
second group consists of statistical charts, providing special
information and statistics for a chosen interval. Vampir allows multiple
instances for charts of these categories. The last group comprises
informational charts, providing specific textual information or legends.
Only one instance of an informational chart can be opened at a time.

**Icons of the Toolbar**

Icon

Name

Description

|image43|

Master Timeline

`Master
Timeline <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Master_Timeline_and_Process_Timeline>`__

|image44|

Process Timeline

`Process
Timeline <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Master_Timeline_and_Process_Timeline>`__

|image45|

Counter Data Timeline

`Counter
Data <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Counter_Data_Timeline>`__

|image46|

Performance Radar

`Performance
Radar <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Performance_Radar>`__

|image47|

Function Summary

`Function
Summary <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Function_Summary>`__

|image48|

Message Summary

`Message
Summary <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Message_Summary>`__

|image49|

Process Summary

`Process
Summary <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Process_Summary>`__

|image50|

Communication Matrix View

`Communication Matrix
View <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Communication_Matrix_View>`__

|image51|

Call Tree

`Call
Tree <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Call_Tree>`__

|image52|

Function Legend

`Function
Legend <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Function_Legend>`__

|image53|

Context View

`Context
View <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Context_View>`__

|image54|

Marker View

`Marker
View <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir#Information_Filtering_and_Reduction>`__

**Properties of the Tracefile**
-------------------------------

Vampir provides a display containing the most important
characterizations of the used tracefile. This tabular is called \ *Trace
Properties* and can be accessed by \ *File->Trace Properties*. The
information, such as the filename, the creator and its version,
originates from the tracefile and is not changed by Vampir.

**Performance Data Visualization**
==================================

This chapter deals with the different charts that can be used to analyze
the behavior of a program and the comparison between different function
groups, e.g., MPI and Calculation. In addition, the chapter addresses
communication performance issues. Various charts address the
visualization of data transfers between processes. The following
sections describe them in detail.

**Timeline Charts**
-------------------

A very common chart type used in event-based performance analysis is the
so-called timeline chart. This chart type graphically presents the chain
of events of monitored processes or counters on a horizontal time axis.
Multiple timeline chart instances can be added to the \ *Trace
View* window via the \ *Chart* menu or the \ *Charts* toolbar.

**Note**: To measure the duration between two events in a timeline
chart, Vampir provides a tool called ruler. Click on the first event in
a timeline display and move the mouse while keeping the left mouse key
and \ *Shift* pressed. A ruler-like pattern appears in the current
timeline chart, which provides rough measurement directly. The exact
time of the start event and the mouse position and the interval in
between is given at the very bottom. If the \ *Shift* key is released
before the left mouse key, Vampir will proceed with zooming.

**Master Timeline and Process Timeline**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Master and Process Timelines, detailed information about
functions, communication, and synchronization events is shown. Timeline
charts are available for individual processes (*Process Timeline*) as
well as for a collection of processes (*Master Timeline*). The \ *Master
Timeline* consists of a collection of rows. Each row represents a single
process, as shown in the figure below. A \ *Process Timeline* shows the
different levels of function calls in a stacked bar chart for a single
process, as depicted in the second figure.

|image55|

**Master Timeline**

|image56|

**Process Timeline**

Every timeline row consists of a process name on the left and a colored
sequence of function calls or program phases on the right. The color of
a function is defined by its group membership; e.g., MPI\_Send()
belonging to the function group MPI has the same color, presumably red,
as MPI\_Recv(), which also belongs to the function group MPI. Clicking
on a function highlights it and causes the \ *Context View* display to
show detailed information about that particular function, e.g., its
corresponding function group name, time interval, and the complete name.
The \ *Context View* display is explained in its own section below. Some
function invocations are very short, and will not show up in the overall
view because of a lack of display pixels. A zooming mechanism is
provided to inspect a specific time interval in more detail. If zooming
is performed, panning in a horizontal direction is possible with the
scroll bar at the bottom. The \ *Process Timeline* resembles
the \ *Master Timeline*\ with slight differences. The chart's timeline
is divided into levels, which represent the different call stack levels
of function calls. The initial function begins at the first level, a
sub-function called by that function is located a level beneath, and so
forth. If a sub-function returns to its caller, the graphical
representation also returns to the level above. In addition to the
display of categorized function invocations, Vampir's
*Master* and *Process Timeline* also provide information about
communication events. Messages exchanged between two different processes
are depicted as black lines. In timeline charts, the progress in time is
reproduced from left to right. The leftmost starting point of a message
line and its underlying process bar therefore identify the sender of the
message, whereas the rightmost position of the same line represents the
receiver of the message. The corresponding function calls normally
reflect a pair of MPI communication directives like MPI\_Send() and
MPI\_Recv(). It is also possible to show a collective communication like
MPI\_Allreduce() by selecting one corresponding message as shown in the
figure.

|image57|

**Selected MPI Collective in Master Timeline**

Additional information like message bursts, markers, and I/O events is
also available. The table shows the symbols and descriptions of these
objects.

 

**Additional Information in Master and Process Timeline**

**Symbol**

**Description**

Message Burst

|image58|

Because of a lack of pixels it is not possible to display a large number
of messages in a very short interval. Therefore, these messages are
summarized as so-called message bursts. Zooming into this interval
reveals the corresponding single messages.

Markers

|image59|\ multiple

|image60|\ single

To indicate particular points (like errors or warnings) during the
runtime of an application, markers can be used in a tracefile. They are
drawn as triangles, which are colored according to their types. To
illustrate that two or more markers are placed at the same pixel, a
multiple marker is drawn.

I/O Events

|image61|\ multiple

|image62|\ single

|image63|\ single, selected

Vampir shows detailed information about I/O operations, if they are
included in the tracefile. I/O events are depicted as triangles at the
beginning of an I/O interval. Multiple I/O events are tricolored and
occupy a line to the end of the interval. To see the whole interval of a
single I/O event, the triangle has to be selected. In that case, a
second triangle at the end of the interval appears.

Since the \ *Process Timeline* reveals information of one process only,
short black arrows are used to indicate outgoing communication. Clicking
on message lines or arrows shows message details like sender process,
receiver process, message length, message duration, and message tag in
the \ *Context View* display.

**Counter Data Timeline**
~~~~~~~~~~~~~~~~~~~~~~~~~

Counters are values collected over time to count certain events like
floating point operations or cache misses. Counter values can be used to
store not just hardware performance counters but arbitrary sample
values. There can be counters for different statistical information as
well, for instance, counting the number of function calls or a value in
an iterative approximation of the final result. Counters are defined
during the instrumentation of the application and can be individually
assigned to processes.

|image64|

**Counter Data Timeline**

The chart is restricted to one counter at a time. It shows the selected
counter for one process. Using multiple instances of the \ *Counter Data
Timeline,* counters or processes can be compared easily. The context
menu entry \ *Set Counter* allows you to choose the displayed counter
directly from a drop-down list. The entry \ *Set Process* selects the
particular process for which the counter is shown.

**Performance Radar**
~~~~~~~~~~~~~~~~~~~~~

The Performance Radar chart provides the search of function occurrences
in the trace file and the extended visualization of counters. It can
happen that a function is not shown in \ *Master* and *Process
Timeline* due to a short runtime. An alternative to zooming is the
option \ *Find Function...*. A color-coded timeline indicates the
intervals in which the function is executed.

|image65|

**Performance Radar Timeline - Search of Functions**

By default, the Performance Radar shows the values of one counter for
each process (thread). In this mode the user can choose between *Line
Plot* and *Color Coded* drawing. In the latter case, a color scale on
the bottom provides information about the range of values. Clicking
on \ *Set Counter...* leads to a dialog that offers the option of
choosing another counter and calculating the sum or average values.
Summarizing means that the values of the selected counter of all
processes are summed up. The average is this sum divided by the number
of processes. Both options provide a single graph.

|image66|

**Performance Radar Timeline - Visualization of Counters**

**Statistical Charts**
----------------------

**Call Tree**
~~~~~~~~~~~~~

The \ *Call Tree* illustrates the invocation hierarchy of all monitored
functions in a tree representation. The display reveals information
about the number of invocations of a given function, the time spent in
the different calls, and the caller-callee relationship.

|image67|

**Call Tree**

The entries of the \ *Call Tree* can be sorted in various ways. Simply
click on one header of the tree representation to use its characteristic
to resort the \ *Call Tree*. Please note that not all available
characteristics are enabled by default. To add or remove
characteristics, a context menu is accessible by right-clicking on any
of the tree headers. To leaf through the different function calls, it is
possible to fold and unfold the levels of the tree. This can be achieved
by double-clicking a level, or by using the fold level buttons next to
the function name. Functions can be called by many different caller
functions, which is hardly obvious in the tree representation.
Therefore, a relation view shows all callers and callees of the
currently selected function in two separated lists, as shown in the
lower area. To find a certain function by its name, Vampir provides a
search option accessible with the context menu entry \ *Show Find View*.
The entered keyword has to be confirmed by pressing the Return key.
The \ *Previous* and *Next* buttons can be used to flip through the
results afterwards.

**Function Summary**
~~~~~~~~~~~~~~~~~~~~

The \ *Function Summary* chart gives an overview of the accumulated time
consumption across all function groups and functions. For example every
time a process calls the MPI\_Send() function, the elapsed time of that
function is added to the MPI function group time. The chart gives a
condensed view on the execution of the application and a comparison
between the different function groups can be made so that dominant
function groups can be distinguished easily.

|image68|

**Function Summary**

It is possible to change the information displayed via the context menu
entry \ *Set Metric*, which offers values like \ *Average Exclusive
Time*, *Number of Invocations*, \ *Accumulated Inclusive Time* and
others. Note: \ *Inclusive* means the amount of time spent in a function
and all of its subroutines. *Exclusive* means the amount of time just
spent in this function. The context menu entry \ *Set Event
Category* specifies whether either function groups or functions should
be displayed in the chart. The functions own the color of their function
group. It is possible to hide functions and function groups from the
displayed information with the context menu entry \ *Filter*. To mark
the function or function group to be filtered, click the associated
label or color representation in the chart. Using the \ *Process
Filter* allows you to restrict this view to a set of processes. As a
result, only the consumed time of these processes is displayed for each
function group or function. Instead of using the filter (which affects
all other displays by hiding processes), it is possible to select a
single process via \ *Set Process* in the context menu of the *Function
Summary*. This does not have any effect on other timeline displays.
The \ *Function Summary* can be shown as a \ *Histogram* (a bar chart,
as in timeline charts) or as a \ *Pie Chart*. To switch between these
representations, use the \ *Set Chart Mode* entry of the context menu.
The shown functions or function groups can be sorted by name or value
via the context menu option \ *Sort By*.

**Process Summary**
~~~~~~~~~~~~~~~~~~~

The \ *Process Summary* is similar to the \ *Function Summary* but shows
the information for every process independently.

|image69|

**Process Summary**

This is useful for analyzing the balance between processes to reveal
bottlenecks. For instance, finding that one process spends a
significantly high time performing the calculations could indicate an
unbalanced distribution of work that can slow down the entire
application. The context menu entry \ *Set Event Category* specifies
whether either function groups or functions should be displayed in the
chart. The functions own the color of their function group. The chart
can calculate the analysis based on \ *Exclusive Time* or *Inclusive
Time*. To change between these two modes, use the context menu
entry \ *Set Metric*. It is possible to hide functions and function
groups from the displayed information with the context menu
entry \ *Filter*. To mark the function or function group to be filtered,
click on the associated color representation in the chart. Using
the \ *Process Filter* allows you to restrict this view to a set of
processes.

**Message Summary**
~~~~~~~~~~~~~~~~~~~

The \ *Message Summary* is a statistical chart showing an overview of
the different messages grouped by certain characteristics.

|image70|

**Message Summary Chart with metric set to \ *Message Transfer
Rate* showing the average transfer rate (A), and the minimal/maximal
transfer rate (B)**

| All values are represented in a bar chart fashion. The number next to
each bar is the group base, while the number inside a bar depicts the
different values depending on the chosen metric. Therefore, the \ *Set
Metric* sub-menu of the context menu can be used to switch between
*Aggregated Message Volume*, \ *Message Size*, \ *Number of Messages*,
and \ *Message Transfer Rate*. The group base can be changed via the
context menu entry \ *Group By*. It is possible to choose
between \ *Message Size*, \ *Message Tag*, and \ *Communicator (MPI)*.
| 
|  **Note**: There will be one bar for every occurring group. However,
if metric is set to \ *Message Transfer Rate*, the minimal and the
maximal transfer rate is given in an additional bar beneath the one
showing the average transfer rate. The additional bar starts at the
minimal rate and ends at the maximal one. To filter out messages, click
on the associated label or color representation in the chart and
choose \ *Filter* from the context menu afterwards.

**Communication Matrix View**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The \ *Communication Matrix View* is another way of analyzing
communication imbalances. It shows information about messages sent
between processes.

|image71|

**Communication Matrix View**

| The chart is realized as a table. Its rows represent the sending
processes while its columns represent the receivers. The color legend on
the right indicates the displayed values. Depending on the displayed
information, the color legend changes. It is possible to change the type
of displayed values. Different metrics like the average duration of
messages passed from sender to recipient or minimum and maximum
bandwidth are offered. To change the type of value that is displayed,
use the context menu option \ *Set Metric*. Use the \ *Process
Filter* to define which processes/groups should be displayed.
| 
|  **Note**: A high duration is not automatically caused by a slow
communication path between two processes, but can also be due to the
fact that the time between starting transmission and successful
reception of the message can be increased by a recipient that delays
reception for some reason. This will cause the duration to increase (by
this delay) and the message rate, which is the size of the message
divided by the duration, to decrease accordingly.

**Informational Charts**
------------------------

**Function Legend**
-------------------

The \ *Function Legend* lists all visible function groups of the loaded
trace file along with its corresponding color.

|image72|

**Function Legend**

If colors of functions are changed, they appear in a tree-like fashion
under their respective function group as well.

|image73|

**A chosen marker (A) and its representation in the Marker View (B)**

The display is given in a tree-like fashion and organizes the marker
events in their respective groups and types. Additional information,
like the time of occurrence in the trace file and its description, is
provided for each marker. By clicking on a marker event in the \ *Marker
View*, this event gets selected in the timeline displays that are
currently open, and vice-versa. If this marker event is not visible, the
zooming area jumps to this event automatically. It is possible to select
markers and types. Then all events belonging to that marker or type get
selected in the \ *Master Timeline* and the \ *Process Timeline*.
If \ *Ctrl* or *Shift* is pressed, the user can highlight several
events. In this case, the user can fit the borders of the zooming area
in the timeline charts to the timestamps of the two marker events that
were chosen at last.

**Context View**
~~~~~~~~~~~~~~~~

|image74|

**Context View, showing context information (B) of a selected function
(A)**

As implied by its name, the \ *Context View* provides more detailed
information of a selected object compared to its graphical
representation. An object, e.g., a function, function group, message, or
message burst, can be selected directly in a chart by clicking its
graphical representation. For different types of objects, different
context information is provided by the \ *Context View*. For example,
the object-specific information for functions holds properties
like \ *Interval Begin*, \ *Interval End*, and \ *Duration*.
The \ *Context View* may contain several tabs, and a new empty one can
be added by clicking on the \ *add*-symbol on the right hand side. If an
object in another chart is selected, its information is displayed in the
current tab. If the \ *Context View* is closed, it opens automatically
in that moment. The \ *Context View* offers a comparison between the
information that is displayed in different tabs. Just use the \ *=* on
the left hand side and choose two objects in the emerged dialog. It is
possible to compare different elements from different charts, which can
be useful in some cases. The comparison shows a list of common
properties. The corresponding values are displayed, along with their
difference if the values are numbers. The first line always shows the
names of the displays.

|image75|

**Comparison between Context Information**

**Information Filtering and Reduction**
---------------------------------------

Due to the large amount of information that can be stored in trace
files, it is usually necessary to reduce the displayed information
according to some filter criteria. In Vampir, there are different ways
of filtering. It is possible to limit the displayed information to a
certain choice of processes or to specific types of communication
events, e.g., to certain types of messages or collective operations.
Deselecting an item in a filter means that this item is fully masked. In
Vampir, filters are global. Therefore, masked items will no longer show
up in any chart. Filtering not only affects the different charts, but
also the *Zoom Toolbar. The different filters can be reached via
the *\ Filter *entry in the main menu.*

The example below shows a typical process representation in
the \ *Process Filter* window. This kind of representation is equal to
all other filters. Processes can be filtered by their \ *Process
Group*, \ *Communicators* and *Process Hierarchy*. Items to be filtered
are arranged in a spreadsheet representation. In addition to selecting
or deselecting an entire group of processes, it is certainly possible to
filter single processes.

|image76|

**Process Filter**

Different selection methods can be used in a filter. The check
box \ *Include/Exclude All* either selects or deselects every item.
Specific items can be selected/deselected by clicking the check box next
to it. Furthermore, it is possible to select/deselect multiple items at
once; mark the desired entries by clicking their names while holding
either the \ *Shift* or the \ *Ctrl* key. By holding the \ *Shift* key
every item in between the two clicked items will be marked. Holding
the \ *Ctrl* key, on the other hand, enables you to add or remove
specific items from/to the marked ones. Clicking the check box of one of
the marked entries will cause selection/deselection for all of them.

**Options of Filtering**

+-------------------------+-------------------------+
| **Filter Object**       | **Filter Criteria**     |
+-------------------------+-------------------------+
| Processes               | Process Groups          |
+-------------------------+-------------------------+
|                         | Communicators           |
+-------------------------+-------------------------+
|                         | Process Hierarchy       |
+-------------------------+-------------------------+
|                         | Single Processes        |
+-------------------------+-------------------------+
| Collective Operations   | Communicators           |
+-------------------------+-------------------------+
|                         | Collective Operations   |
+-------------------------+-------------------------+
| Messages                | Message Communicators   |
+-------------------------+-------------------------+
|                         | Message Tags            |
+-------------------------+-------------------------+
| I/O Events              | I/O Groups              |
+-------------------------+-------------------------+
|                         | Files                   |
+-------------------------+-------------------------+
|                         | Types                   |
+-------------------------+-------------------------+

**Customization**
=================

The appearance of the trace file and various other application settings
can be altered in the preferences accessible via the main menu entry
*File->Preferences*. Settings concerning the trace file itself, e.g.,
layout or function group colors, are saved individually next to the
tracefile in a file, whose end is \ *.vsettings*. In this way, it is
possible to adjust the colors for one trace file without interfering
with other trace files. The options *Import Preferences* and *Export
Preferences* provide the loading and saving of preferences of arbitrary
tracefiles.

**General Preferences**
-----------------------

The \ *General* settings allow you to change application and trace
specific values.

|image77|

**General Settings**

*Show time as*\ decides whether the time format for the trace analysis
is based on seconds or ticks. The next point \ *Use color gradient in
charts*\ allows you to switch off the color gradient used in the
performance charts. The next option is to change the style and size of
the font. *Show source code* allows you to open an editor showing the
respective source file. In order to open a source file, first click on
the intended function in the \ *Master Timeline* and then on the source
code path in the \ *Context View*. For the source code location to work
properly, you need a trace file with source code location support. The
path of the source file can be adjusted in \ *Preferences*. A limit for
the size of the file can be set, too. Finally, the user can decide if he
wants Vampir to automatically check for new versions.

**Appearance**
--------------

In the \ *Appearance* settings of the \ *Preferences* dialog, there are
six different objects for which the color options can be changed: the
functions/function groups, markers, counters, collectives, messages and
I/O events. Choose an entry and click on its color to make a
modification. A color picker dialog opens where it is possible to adjust
the color. For messages and collectives, a change of the line width is
also available.

|image78|

**Appearance Settings**

In order to quickly find the desired item a search box is provided at
the bottom of the dialog.

**Saving Policy**
-----------------

Vampir detects whenever changes to the various settings are made. In
the \ *Saving Policy* dialog it is possible to adjust the saving
behavior of the different components to your own needs.

 

**Saving Policy Settings**

| In the dialog \ *Saving Behavior* you tell Vampir what to do in the
case of changed preferences. The user can choose the categories of
settings (e.g., layout) that should be treated. Possible options are
that the application automatically \ *Always* or *Never* saves changes.
The default option is to have Vampir asking you whether to save or
discard changes. Usually the settings are stored in the folder of the
tracefile. If the user has no access to it, it is possible to place them
in the \ *Application Data Folder*. They are listed in the
tab \ *Locally Stored Preferences* with creation and modification date.
| 
|  **Note**: On loading, Vampir favors settings in the \ *Application
Data Folder*. *Default Preferences* offers to save preferences of the
current trace file as default settings, where they are then used for
tracefiles without settings. Another option is to restore the default
settings; in this case, the current preferences of the tracefile are
reverted.

**Footnotes**
=============

Additional links that might be of interest to the reader:

...
(OTF) `http://www.tu-dresden.de/zih/otf <http://www.tu-dresden.de/zih/otf>`__

...
WindowsHPC \ `http://resourcekit.windowshpc.net/MORE\_INFO/TracingMPIApplications.html <http://resourcekit.windowshpc.net/MORE_INFO/TracingMPIApplications.html>`__

...
Manual \ `http://www.tu-dresden.de/zih/vampirtrace <http://www.tu-dresden.de/zih/vampirtrace>`__

Retrieved from
"`https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir <https://wiki.futuregrid.org/index.php/Docs/Performance/Vampir>`__\ "

 

 

VampirTrace
===========

 

VampirTrace consists of a tool set and a runtime library for
instrumentation and tracing of software applications. It is particularly
tailored to parallel and distributed High Performance Computing (HPC)
applications.

**Availability**\ ****

VampirTrace is currently available on FutureGrid machines under module
'vampirtrace'. VampirTrace is also available in OpenMPI versions 1.5.x
or higher. For example on Bravo, it is available as *openmpi/1.5.4-gnu*
or *openmpi/1.5.4-intel*.

**Overview**\ ****

The instrumentation part of VampirTrace modifies a given application in
order to inject additional measurement calls during runtime. The tracing
part provides the actual measurement functionality used by the
instrumentation calls. By this means, a variety of detailed performance
properties can be collected and recorded during runtime. This includes
function enter and leave events, MPI communication, OpenMP events, and
performance counters.

After a successful tracing run, VampirTrace writes all collected data to
a trace file in the Open Trace Format (OTF). As a result, the
information is available for post-mortem analysis and visualization by
various tools. Most notably, VampirTrace provides the input data for the
Vampir analysis and visualization tool.

Trace files can quickly become very large, especially with automatic
instrumentation. Tracing applications for only a few seconds can result
in trace files of several hundred megabytes. To protect users from
creating trace files of several gigabytes, the default behavior of
VampirTrace limits the internal buffer to 32MB per process (2GB on
FutureGrid systems). Thus, even for larger scale runs the total trace
file size will be moderate.

The following list shows a summary of all instrumentation and tracing
features that VampirTrace offers. Note that not all features are
supported on all platforms.

**Tracing of User Functions**

-  Record function enter and leave events
-  Record name and source code location (file name, line)
-  Manual instrumentation using VampirTrace API

**MPI Tracing**

-  Record MPI functions
-  Record MPI communication: participating processes, transferred bytes,
   tag, communicator

**OpenMP Tracing**

-  OpenMP directives, synchronization, thread idle time
-  Also hybrid (MPI and OpenMP) applications are supported

**Pthread Tracing**

-  Trace POSIX thread API calls
-  Also hybrid (MPI and POSIX threads) applications are supported

**Java Tracing**

-  Record method calls
-  Using JVMTI as interface between VampirTrace and Java Applications

**3rd-Party Library tracing**

-  Trace calls to arbitrary third party libraries
-  Generate wrapper for library functions based on library’s header
   file(s)
-  No recompilation of application or library is required

**MPI Correctness Checking**

-  Record MPI usage errors
-  Using UniMCI as interface between VampirTrace and a MPI correctness
   checking tool (e.g., Marmot)

**User API**

-  Manual instrumentation of source code regions
-  Measurement controls
-  User-defined counters
-  User-defined marker

**Performance Counters**

-  Hardware performance counters using PAPI, CPC, or NEC SX performance
   counter
-  Resource usage counters using getrusage

**Memory Tracing**

-  Trace GLIBC memory allocation and free functions
-  Record size of currently allocated memory as counter

**I/O Tracing**

-  Trace LIBC I/O calls
-  Record I/O events: file name, transferred bytes

**CPU ID Tracing**

-  Trace core ID of a CPU on which the calling thread is running
-  Record core ID as counter

**Fork/System/Exec Tracing**

-  Trace applications calling LIBC’s fork, system, or one of the exec
   functions
-  Add forked processes to the trace

**Filtering & Grouping**

-  Runtime and post-mortem filter (i.e., exclude functions from being
   recorded in the trace)
-  Runtime grouping (i.e., assign functions to groups for improved
   analysis)

**OTF Output**

-  Writes compressed OTF files
-  Output as trace file, statistical summary (profile), or both

**Instrumentation**

 

To perform measurements with VampirTrace, the user's application program
needs to be instrumented; that is, at specific points of interest
(called "events"), VampirTrace measurement calls have to be activated.
Common events are, among others, entering and leaving of functions as
well as sending and receiving of MPI messages. VampirTrace handles this
automatically by default. In order to enable the instrumentation of
function calls, the user needs only to replace the compiler and linker
commands with VampirTrace’s wrappers (see below). VampirTrace supports
different ways of instrumentation as described in the sections below.

**Compiler Wrappers**

All the necessary instrumentation of user functions, MPI, and OpenMP
events is handled by VampirTrace’s compiler wrappers (vtcc, vtcxx,
vtf77, and vtf90). In the script used to build the application (e.g., a
makefile), all compile and link commands should be replaced by the
VampirTrace compiler wrapper. The wrappers perform the necessary
instrumentation of the program and link the suitable VampirTrace
library. The following list shows some examples specific to the
parallelization type of the program:

-  Serial programs

Compiling serial codes is the default behavior of the wrappers. Simply
replace the compiler by VampirTrace’s wrapper:

 

original:             gfortran hello.f90 -o hello

with instrumentation: **vtf90** hello.f90 -o hello 

 

This will instrument user functions (if supported by the compiler) and
link the VampirTrace library.

-  MPI parallel programs

MPI instrumentation is always handled by means of the PMPI interface,
which is part of the MPI standard. This requires the compiler wrapper to
link with an MPI-aware version of the VampirTrace library. If your MPI
implementation uses special MPI compilers (e.g. mpicc, mpxlf90), you
will need to tell VampirTrace’s wrapper to use this compiler instead of
the serial one:

 

original:             mpicc hello.c -o hello           

with instrumentation: **vtcc -vt:cc mpicc** hello.c -o hello

 

MPI implementations without their own compilers require the user to link
the MPI library manually. In this case, simply replace the compiler by
VampirTrace’s compiler wrapper:

original:             icc hello.c -o hello –lmpi

with instrumentation: **vtcc** hello.c -o hello -lmpi

 

If you want to instrument MPI events only (this creates smaller trace
files and less overhead), use the option *-vt:inst manual* to disable
automatic instrumentation of user functions.

-  Threaded parallel programs

When VampirTrace detects OpenMP or Pthread flags on the command line,
special instrumentation calls are invoked. For OpenMP events, OPARI is
invoked for automatic source code instrumentation.

 

original:             ifort <-openmp\|-pthread> hello.f90 -o hello

with instrumentation: **vtf90** <-openmp\|-pthread> hello.f90 -o hello

 

For more information about OPARI, read the documentation available in
VampirTrace’s installation directory at:
`share/vampirtrace/doc/opari/Readme.html <http://share/vampirtrace/doc/opari/Readme.html%20>`__

-  Hybrid MPI/Threaded parallel programs

With a combination of the above mentioned approaches, hybrid
applications can be instrumented:

original:             mpif90 <-openmp\|-pthread> hello.F90 -o
hello             

with instrumentation: **vtf90 -vt:f90 mpif90** <-openmp\|-pthread>
hello.F90 -o hello

 

The VampirTrace compiler wrappers automatically try to detect which
parallelization method is used by means of the compiler flags (e.g.,
-lmpi, -openmp or -pthread) and the compiler command (e.g. mpif90). If
the compiler wrapper failed to detect this correctly, the
instrumentation could be incomplete and an unsuitable VampirTrace
library would be linked to the binary. In this case, you should tell the
compiler wrapper which parallelization method your program uses by using
the switches -vt:mpi, -vt:mt, and -vt:hyb for MPI, multithreaded, and
hybrid programs, respectively. Note that these switches do not change
the underlying compiler or compiler flags. Use the option -vt:verbose to
see the command line that the compiler wrapper executes.

The default settings of the compiler wrappers can be modified in the
files *share/vampirtrace/vtcc-wrapper-data.txt* (and similar for the
other languages) in the installation directory of VampirTrace. The
settings include compilers, compiler flags, libraries, and
instrumentation types. You could, for instance, modify the default C
compiler from gcc to mpicc by changing the line *compiler=gcc* to
*compiler=mpicc*. This may be convenient if you instrument MPI parallel
programs only.

**Instrumentation Types**

 

The wrapper option *-vt:inst <insttype>* specifies the instrumentation
type to be used. The following values for *<insttype>* are possible:

-  compinst

Fully-automatic instrumentation by the compiler

 

-  manual

Manual instrumentation by using VampirTrace’s API (needs source-code
modifications)

**Automatic Instrumentation**

 

Automatic instrumentation is the most convenient method to instrument
your program. If available, simply use the compiler wrappers without any
parameters, e.g.:

vtf90 hello.f90 -o hello

**Notes for Using the GNU or Intel Compiler**

For these compilers, the command nm is required to get symbol
information of the running application executable. To get the
application executable for nm during runtime, VampirTrace uses the /proc
file system. As /proc is not present on all operating systems, automatic
symbol information might not be available. In this case, it is necessary
to set the environment variable VT APPPATH to the pathname of the
application executable to get symbols resolved via nm.

Should any problems emerge to get symbol information automatically, then
the environment variable VT GNU NMFILE can be set to a symbol list file,
which is created with the command nm, like:

nm hello > hello.nm

To get the source code line for the application functions use nm -l (on
Linux systems). VampirTrace will include this information in the trace.
Note that the output format of nm must be written in BSD-style. See the
manual page of nm for help in dealing with the output format setting.

**Notes on Instrumentation of Inline Functions**

Compilers behave differently when they automatically instrument inlined
functions. The GNU and Intel (10.0++) compilers instrument all functions
by default when they are used with VampirTrace. They therefore switch
off inlining completely, disregarding the optimization level chosen. One
can prevent these particular functions from being instrumented by
appending the following attribute to function declarations, hence making
them able to be inlined (this works only for C/C++):

\_\_attribute\_\_ ((\_\_no\_instrument\_function\_\_))

The PGI and IBM compilers prefer inlining over instrumentation when
compiling with enabled inlining. Thus, one needs to disable inlining to
enable the instrumentation of inline functions and vice versa.

The bottom line is that a function cannot be inlined and instrumented at
the same time. Note that you can also use the option *-vt:inst manual*
with non-instrumented sources. Binaries created in this manner only
contain MPI and OpenMP instrumentation, which might be desirable in some
cases. For more on how to inline functions, read your compiler’s manual.

**Manual Instrumentation**

**Using the VampirTrace API**

The *VT USER START, VT USER END* calls can be used to instrument any
user-defined sequence of statements.

Fortran

 

#include "vt\_user.inc"

VT\_USER\_START(’name’)

...

VT\_USER\_END(’name’)

 

C

 

#include "vt\_user.h"

VT\_USER\_START("name");

...

VT\_USER\_END("name");

If a block has several exit points (as is often the case for functions),
all exit points have to be instrumented with VT USER END, too.

For C++ it is simpler, as is demonstrated in the following example. Only
entry points into a scope need to be marked. The exit points are
detected automatically when C++ deletes scope-local variables.

C++

#include "vt\_user.h"

{

    VT\_TRACER("name");

    ...

}

The instrumented sources have to be compiled with -DVTRACE for all three
languages; otherwise the VT \* calls are ignored. Note that Fortran
source files instrumented this way have to be preprocessed, too.

In addition, you can combine this particular instrumentation type with
all other types. In such a way, all user functions can be instrumented
by a compiler while special source code regions (e.g., loops) can be
instrumented by VT’s API.

Use VT’s compiler wrapper (described above) for compiling and linking
the instrumented source code, such as:

-  combined with automatic compiler instrumentation:

vtcc **-DVTRACE** hello.c -o hello

 

-  without compiler instrumentation:

vtcc -vt:inst manual **-DVTRACE** hello.c -o hello

Note that you can also use the option -vt:inst manual with
non-instrumented sources. Binaries created in this manner only contain
MPI and OpenMP instrumentation, which might be desirable in some cases.

**Measurement Controls**

**Switching Tracing On/Off:** In addition to instrumenting arbitrary
blocks of code, one can use the VT\_ON/ VT\_OFF instrumentation calls to
start and stop the recording of events. These constructs can be used to
stop recording of events for a part of the application and later resume
recording. For example, one could not collect trace events during the
initialization phase of an application and turn on tracing for the
computation part.

Furthermore, the "on/off" functionality can be used to control the
tracing behavior of VampirTrace, and allows you to trace only parts of
interests. Essentially, then, the amount of trace data can be reduced.

To check whether if tracing is enabled or not, use the call VT\_IS\_ON.

Please note that stopping and starting the recording of events has to be
performed at the same call stack level. If this is not the case, an
error message will be printed during runtime, and VampirTrace will abort
execution.

**Intermediate Buffer Flush:** In addition to an automated buffer flush
when the buffer is filled, it is possible to flush the buffer at any
point of the application. This way you can guarantee that after a manual
buffer flush there will be a sequence of the program with no automatic
buffer flush interrupting. To flush the buffer, you can use the call
VT\_BUFFER\_FLUSH.

**Intermediate Time Synchronisation:** VampirTrace provides several
mechanisms for timer synchronization. In addition, it is also possible
to initiate a timer synchronization at any point of the application by
calling VT\_TIMESYNC. Please note that the user has to ensure that all
processes are actual at a synchronized point in the program (e.g., at a
barrier). To use this call, make sure that the enhanced timer
synchronization is activated (set the environment variable
VT\_ETIMESYNC).

**Intermediate Counter Update:** VampirTrace provides the functionality
to collect the values of arbitrary hardware counters. Chosen counter
values are automatically recorded whenever an event occurs. Sometimes
(e.g., within a long-lasting function) it is desirable to get the
counter values at an arbitrary point within the program. To record the
counter values at any given point, you can call VT\_UPDATE\_COUNTER.

**Note:** For all three languages the instrumented sources have to be
compiled with -DVTRACE. Otherwise the VT \* calls are ignored. In
addition, if the sources contain further VampirTrace API calls and only
the calls for measurement controls will be disabled, then the sources
must also be compiled with -DVTRACE\_NO\_CONTROL.

**Tracing Calls to 3rd-Party Libraries**

VampirTrace is also capable of tracing calls to third-party libraries
which come with at least one C header file, even without the library’s
source code. If VampirTrace was built with support for library tracing,
the tool vtlibwrapgen can be used to generate a wrapper library to
intercept each call to the actual library functions. This wrapper
library can be linked to the application, or used in combination with
the LD PRELOAD mechanism provided by Linux. The generation of a wrapper
library is done using the vtlibwrapgen command and consists of two
steps. The first step generates a C source file, providing the wrapped
functions of the library header file:

vtlibwrapgen -g SDL -o SDLwrap.c /usr/include/SDL/\*.h

This generates the source file *SDLwrap.c* that contains
wrapper-functions for all library functions found in the header-files
located in */usr/include/SDL/*, and instructs VampirTrace to assign
these functions to the new group SDL. The generated wrapper source file
can be edited in order to add manual instrumentation or alter attributes
of the library wrapper. A detailed description can be found in the
generated source file or in the header file *vt libwrap.h* , which can
be found in the include directory of VampirTrace. To adapt the library
instrumentation it is possible to pass a filter file to the generation
process. The rules are like these for normal VampirTrace
instrumentation, where only 0 (exclude functions) and -1 (generally
include functions) are allowed.

The second step is to compile the generated source file:

vtlibwrapgen --build --shared -o libSDLwrap SDLwrap.c

This builds the shared library *libSDLwrap.so*, which can be linked to
the application or preloaded by using the environment variable LD
PRELOAD:

LD\_PRELOAD=$PWD/libSDLwrap.so <executable>

**Runtime Measurement**

Running a VampirTrace instrumented application should normally result in
an OTF trace file in the current working directory where the application
was executed. If a problem occurs, set the environment variable
VT\_VERBOSE to 2 before executing the instrumented application in order
to see control messages of the VampirTrace runtime system which might
help tracking down the problem.

The internal buffer of VampirTrace is limited to 32 MB per process. Use
the environment variables VT\_BUFFER\_SIZE and VT\_MAX\_FLUSHES to
increase this limit.

**Trace File Name and Location**

The default name of the trace file depends on the operating system where
the application is run. On Linux, MacOS and Sun Solaris, the trace file
will be named like the application, e.g., *hello.otf*\ for the
executable hello. For other systems, the default name is *a.otf*.
Optionally, the trace file name can be defined manually by setting the
environment variable VT\_FILE\_PREFIX to the desired name. The suffix
.\ *otf* will be added automatically.

To prevent overwriting of trace files by repetitive program runs, one
can enable unique trace file naming by setting VT\_FILE\_UNIQUE to yes.
In this case, VampirTrace adds a unique number to the file names as soon
as a second trace file with the same name is created. A \*.lock file is
used to count up the number of trace files in a directory. Be aware that
VampirTrace potentially overwrites an existing trace file if you delete
this lock file. The default value of VT\_FILE\_UNIQUE is no. You can
also set this variable to a number greater than zero, which will be
added to the trace file name. This way you can manually control the
unique file naming.

The default location of the final trace file is the working directory at
application start time. If the trace file will be stored in another
place, use VT\_PFORM\_GDIR to change the location of the trace file.

**Environment Variables**

Environment variables can be used to control nearly every aspect of the
measurement of a VampirTrace instrumented executable. (ToDo: link to
CheatSheet and Doku-PDF)

**Variable**

**Purpose**

**Default**

 

Global Settings

 

VT\_APPPATH

Path to the application executable.

-

VT\_BUFFER\_SIZE

Size of internal event trace buffer. This is the place where event
records are stored, before being written to a file.

32M

VT\_CLEAN

Remove temporary trace files?

yes

VT\_COMPRESSION

Write compressed trace files?

yes

VT\_FILE\_PREFIX

Prefix used for trace filenames.

-

VT\_FILE\_UNIQUE

Enable unique trace file naming? Set to yes, no, or a numerical ID.

no

VT\_MAX\_FLUSHES

Maximum number of buffer flushes.

1

VT\_MAX\_THREADS

Maximum number of threads per process that VampirTrace reserves
resources for.

65536

VT\_PFORM\_GDIR

Name of global directory to store final trace file in.

./

VT\_PFORM\_LDIR

Name of node-local directory which can be used to store temporary trace
files.

/tmp/

VT\_UNIFY

Unify local trace files afterwards?

yes

VT\_VERBOSE

Level of VampirTrace related information messages: Quiet (0), Critical
(1), Information (2)

1

 

Optional Features

 

VT\_CPUIDTRACE

Enable tracing of CPU ID?

no

VT\_ETIMESYNC

Enable enhanced timer synchronization? ⇒ Section
[#timer\_synchronization [\*]]

no

VT\_ETIMESYNC\_INTV

Interval between two successive synchronization phases in s.

120

VT\_IOLIB\_PATHNAME

Provides an alternative library to use for LIBC I/O calls.

-

VT\_IOTRACE

Enable tracing of application I/O calls?

no

VT\_LIBCTRACE

Enable tracing of fork/system/exec calls?

yes

VT\_MEMTRACE

Enable memory allocation counter?

no

VT\_MODE

Colon-separated list of VampirTrace modes: Tracing (TRACE), Profiling
(STAT).

TRACE

VT\_MPICHECK

Enable MPI correctness checking via UniMCI?

no

VT\_MPICHECK\_ERREXIT

Force trace write and application exit if an MPI usage error is
detected?

no

VT\_MPITRACE

Enable tracing of MPI events?

yes

VT\_PTHREAD\_REUSE

Reuse IDs of terminated Pthreads?

yes

VT\_STAT\_INV

Length of interval for writing the next profiling record

0

VT\_STAT\_PROPS

Colon-separated list of event types that will be recorded in profiling
mode: Functions (FUNC), Messages (MSG), Collective Ops. (COLLOP) or all
of them (ALL)

ALL

VT\_SYNC\_FLUSH

Enable synchronized buffer flush?

no

VT\_SYNC\_FLUSH\_LEVEL

Minimum buffer fill level for synchronized buffer flush in percent.

80

 

Counters

 

VT\_METRICS

Specify counter metrics to be recorded with trace events as a
colon-separated list of names

-

VT\_RUSAGE

Colon-separated list of resource usage counters which will be recorded.

-

VT\_RUSAGE\_INTV

Sample interval for recording resource usage counters in ms.

100

 

Filtering, Grouping

 

VT\_DYN\_BLACKLIST

Name of blacklist file for Dyninst instrumentation.

-

VT\_DYN\_SHLIBS

Colon-separated list of shared libraries for Dyninst instrumentation.

-

VT\_FILTER\_SPEC

Name of function/region filter file.

 

VT\_GROUPS\_SPEC

Name of function grouping file.

-

VT\_JAVA\_FILTER\_SPEC

Name of Java specific filter file.

-

VT\_GROUP\_CLASSES

Create a group for each Java class automatically?

yes

VT\_MAX\_STACK\_DEPTH

Maximum number of stack level to be traced. (0 = unlimited)

0

 

Demangle, Symbol List

 

VT\_GNU\_DEMANGLE

Decode (demangle) low-level symbol names into user-level names?

no

VT\_GNU\_GETSRC

Retrieve the source code line of functions instrumented automatically
with the GNU interface?

yes

VT\_GNU\_NMFILE

Name of file with symbol list information.

-

When you use these environment variables, make sure that they have the
same value for all processes of your application on all nodes of your
cluster. Some cluster environments do not automatically transfer your
environment when executing parts of your job on remote nodes of the
cluster, and you may need to explicitly set and export them in batch job
submission scripts.

**Influencing Trace Buffer Size**

The default values of the environment variables VT\_BUFFER\_SIZE and
VT\_MAX\_FLUSHES limit the internal buffer of VampirTrace to 32 MB per
process, and the number of times that the buffer is flushed to 1,
respectively. Events that are to be recorded after the limit has been
reached are no longer written into the trace file. The environment
variables apply to every process of a parallel application, meaning that
applications with n processes will typically create trace files n times
the size of a serial application.

To remove the limit and get a complete trace of an application, set
VT\_MAX\_FLUSHES to 0. This causes VampirTrace to always write the
buffer to disk when it is full. To change the size of the buffer, use
the environment variable VT\_BUFFER\_SIZE. The optimal value for this
variable depends on the application which is to be traced. Setting a
small value will increase the memory available to the application, but
will trigger frequent buffer flushes by VampirTrace. These buffer
flushes can significantly change the behavior of the application. On the
other hand, setting a large value, like 2G, will minimize buffer flushes
by VampirTrace, but decrease the memory available to the application. If
not enough memory is available to hold the VampirTrace buffer and the
application data, parts of the application may be swapped to disk,
leading to a significant change in the behavior of the application.

Note that you can decrease the size of trace files significantly by
using the runtime function filtering.

**Profiling an Application**

Profiling an application collects aggregated information about certain
events during a program run, whereas tracing records information about
individual events. Profiling can therefore be used to get a summary of
the program activity and to detect events that are called very often.
The profiling information can also be used to generate filter rules to
reduce the trace file size.

To profile an application, set the variable VT\_MODE to STAT. Setting
VT\_MODE to STAT:TRACE tells VampirTrace to perform tracing and
profiling at the same time. By setting the variable VT STAT PROPS, the
user can influence whether functions, messages, and/or collective
operations shall be profiled.

**Unification of Local Traces**

After a run of an instrumented application, the traces of the single
processes need to be unified in terms of timestamps and event IDs. In
most cases, this happens automatically. If the environment variable
VT\_UNIFY is set to no, and in the case of certain other circumstances,
it will be necessary to perform unification of local traces manually. To
do this, use the following command:

vtunify <nproc> <prefix>

If VampirTrace was built with support for OpenMP and/or MPI, it is
possible to speedup the unification of local traces significantly. To
distribute the unificationon multible processes, the MPI parallel
version vtunify-mpi can be used as follows:

mpirun -np <nranks> vtunify-mpi <nproc> <prefix>

 

Furthermore, both tools vtunify and vtunify-mpi are capable of opening
additional OpenMP threads for unification. The number of threads can be
specified by the OMP\_NUM\_THREADS environment variable.

**Synchronized Buffer Flush**

When tracing an application, VampirTrace temporarily stores the recorded
events in a trace buffer. Typically, if a buffer of a process or thread
has reached its maximum fill level, the buffer has to be flushed and
other processes or threads may have to wait for this process or thread.
This will result in an asynchronous runtime behavior.

To avoid this problem, VampirTrace provides a buffer flush in a
synchronized manner. This means that if one buffer has reached its
minimum buffer fill level VT\_SYNC\_FLUSH\_LEVEL, all buffers will be
flushed. This buffer flush is only available at appropriate points in
the program flow. Currently, VampirTrace makes use of all MPI collective
functions associated with MPI\_COMM\_WORLD. Use the environment variable
VT\_SYNC\_FLUSH to enable synchronized buffer flush.

**Enhanced Timer Synchronization**

Especially on cluster environments, where each process has its own local
timer, tracing relies on precisely synchronized timers. Therefore,
VampirTrace provides several mechanisms for timer synchronization. The
default synchronization scheme is a linear synchronization at the very
beginning and very end of a trace run with a master-slave communication
pattern.

However, this way of synchronization can become too imprecise for long
trace runs. Therefore, we recommend the usage of the enhanced timer
synchronization scheme of VampirTrace. This scheme inserts additional
synchronization phases at appropriate points in the program flow.
Currently, VampirTrace makes use of all MPI collective functions
associated with MPI\_COMM\_WORLD.

To enable this synchronization scheme, a LAPACK library with C wrapper
support has to be provided for VampirTrace, and the environment variable
VT\_ETIMESYNC has to be set before the tracing. The length of the
interval between two successive synchronization phases can be adjusted
with VT\_ETIMESYNC\_INTV. The following LAPACK libraries provide a
C-LAPACK API that can be used by VampirTrace for the enhanced timer
synchronization:

-  CLAPACK
-  AMD ACML
-  IBM ESSL
-  Intel MKL
-  SUN Performance Library

**Note:** Systems equipped with a global timer do not need timer
synchronization.

**Note:** It is recommended to combine enhanced timer synchronization
and synchronized buffer flush.

**Note:** Be aware that the asynchronous behavior of the application
will be disturbed since VampirTrace makes use of asynchronous MPI
collective functions for timer synchronization and synchronized buffer
flush. Only make use of these approaches if your application does not
rely on an asynchronous behavior! Otherwise, keep this fact in mind
during the process of performance analysis.

**Recording Additional Events and Counters**

**Hardware Performance Counters**

If VampirTrace has been built with hardware counter support, it is
capable of recording hardware counter information as part of the event
records. To request the measurement of certain counters, the user is
required to set the environment variable VT\_METRICS. The variable
should contain a colon-separated list of counter names or a predefined
platform-specific group.

The user can leave the environment variable unset to indicate that no
counters are requested. If any of the requested counters are not
recognized or the full list of counters cannot be recorded due to
hardware resource limits, program execution will be aborted with an
error message.

**PAPI Hardware Performance Counters**

If the PAPI library is used to access hardware performance counters,
metric names can be any PAPI preset names or PAPI native counter names.
For example, set

VT\_METRICS=PAPI\_FP\_OPS:PAPI\_L2\_TCM

to record the number of floating point instructions and level 2 cache
misses.

**Resource Usage Counters**

The Unix system call getrusage provides information about consumed
resources and operating system events of processes such as user/system
time, received signals, and context switches.

If VampirTrace has been built with resource usage support, it is able to
record this information as performance counters to the trace. You can
enable tracing of specific resource counters by setting the environment
variable VT\_RUSAGE to a colon-separated list of counter names. For
example, set

VT\_RUSAGE=ru\_stime:ru\_majflt

to record the system time consumed by each process and the number of
page faults. Alternatively, one can set this variable to the value all
to enable recording of all 16 resource usage counters. Note that not all
counters are supported by all Unix operating systems. Linux 2.6 kernels,
for example, support only resource information for six of them.

The resource usage counters are not recorded at every event. They are
only read if 100 ms have passed since the last sampling. The interval
can be changed by setting VT\_RUSAGE\_INTV to the number of desired
milliseconds. Setting VT\_RUSAGE\_INTV to zero leads to sampling
resource usage counters at every event, which may introduce a large
runtime overhead. Note that in most cases the operating system does not
update the resource usage information at the same high frequency as the
hardware performance counters. Setting VT\_RUSAGE\_INTV to a value less
than 10 ms does not usually improve the granularity.

Be aware that, when using the resource usage counters for multi-threaded
programs, the information displayed is valid for the whole process and
not for each single thread.

**Memory Allocation Counter**

The GNU LIBC implementation provides a special hook mechanism that
allows intercepting all calls to memory allocation and free functions
(e.g. malloc, realloc, free). This is independent from compilation or
source code access, but relies on the underlying system library.

If VampirTrace has been built with memory-tracing support, VampirTrace
is capable of recording memory allocation information as part of the
event records. To request the measurement of the application’s allocated
memory, the user must set the environment variable VT\_MEMTRACE to yes.

**Note:** This approach to get memory allocation information requires
changing internal function pointers in a non-thread-safe way, so
VampirTrace currently does not support memory tracing for threadable
programs, e.g., programs parallelized with OpenMP or Pthreads!

**Pthread API Calls**

When tracing applications with Pthreads, only user events and functions
are recorded which are automatically or manually instrumented. Pthread
API functions will not be traced by default. To enable tracing of all
C-Pthread API functions, include the header *vt user.h* and compile the
instrumented sources with -DVTRACE PTHREAD.

C/C++

 

#include "vt\_user.h"

vtcc **-DVTRACE\_PTHREAD** hello.c -o hello

**I/O Calls**

Calls to functions which reside in external libraries can be intercepted
by implementing identical functions and linking them before the external
library. Such "wrapper functions" can record the parameters and return
values of the library functions.

If VampirTrace has been built with I/O tracing support, it uses this
technique for recording calls to I/O functions of the standard C
library, which are executed by the application. The following functions
are intercepted by VampirTrace:

close

creat

creat64

dup

dup2

fclose

fcntl

fdopen

fgetc

fgets

flockfile

fopen

fopen64

fprintf

fputc

fputs

fread

fscanf

fseek

fseeko

fseeko64

fsetpos

fsetpos64

ftrylockfile

funlockfile

fwrite

getc

gets

lockf

lseek

lseek64

open

open64

pread

pread64

putc

puts

pwrite

pwrite64

read

readv

rewind

unlink

write

writev

 

 

 

The gathered information will be saved as I/O event records in the trace
file. This feature has to be activated for each tracing run by setting
the environment variable VT\_IOTRACE to yes.

This works for both dynamically and statically linked executables. Note
that when linking statically, a warning like the following may be
issued: Using "dlopen" in statically linked applications requires at
runtime the shared libraries from the glibc version used for linking.
This is ok as long as the mentioned libraries are available for running
the application.

If you’d like to experiment with some other I/O library, set the
environment variable VT\_IOLIB\_PATHNAME to the alternative one. Beware
that this library must provide all I/O functions mentioned above;
otherwise VampirTrace will abort.

**fork/system/exec Calls**

If VampirTrace has been built with LIBC trace support, it is capable of
tracing programs which call functions from the LIBC exec family (execl,
execlp, execle, execv, execvp, execve), system, and fork. VampirTrace
records the call of the LIBC function to the trace. This feature works
for sequential (i.e., no MPI or threaded parallelization) programs only.
It works for both dynamically and statically linked executables. Note
that when linking statically, a warning like the following may be
issued: Using "dlopen" in statically linked applications requires at
runtime the shared libraries from the glibc version used for linking.
This is ok as long as the mentioned libraries are available for running
the application.

When VampirTrace detects a call of an exec function, the current trace
file is closed before executing the new program. If the executed program
is also instrumented with VampirTrace, it will create a different trace
file. Note that VampirTrace aborts if the exec function returns
unsuccessfully. Calling fork in an instrumented program creates an
additional process in the same trace file.

**MPI Correctness Checking Using UniMCI**

VampirTrace supports the recording of MPI correctness events, e.g.,
usage of invalid MPI requests. This is implemented by using the
Universal MPI Correctness Interface (UniMCI), which provides an
interface between tools like VampirTrace and existing runtime MPI
correctness checking tools. Correctness events are stored as markers in
the trace file and are visualized by Vampir. If VampirTrace is built
with UniMCI support, the user only has to enable MPI correctness
checking. This is done by merely setting the environment variable
VT\_MPICHECK to yes. Further, if your application crashes due to an MPI
error you should set VT\_MPICHECK\_ERREXIT to yes. This environmental
variable forces VampirTrace to write its trace to disk and exit
afterwards. As a result, the trace with the detected error is stored
before the application might crash.

To install VampirTrace with correctness checking support, it is
necessary to have UniMCI installed on your system. UniMCI in turn
requires you to have a supported MPI correctness checking tool installed
(currently only the tool Marmot is known to have UniMCI support). So,
all in all, you should use the following order to install with
correctness checking support:

#. Marmot

`http://www.hlrs.de/organization/av/amt/research/marmot <http://www.hlrs.de/organization/av/amt/research/marmot>`__

#. UniMCI

`http://www.tu-dresden.de/zih/unimci <http://www.tu-dresden.de/zih/unimci>`__

#. VampirTrace

`http://www.tu-dresden.de/zih/vampirtrace <http://www.tu-dresden.de/zih/vampirtrace>`__

Information on how to install Marmot and UniMCI is given in their
respective manuals. VampirTrace will automatically detect an UniMCI
installation if the unimci-config tool is in path.

**User-defined Counters**

In addition to the manual instrumentation, the VampirTrace API provides
instrumentation calls which allow recording of program variable values
(e.g., iteration counts, calculation results, ...) or any other
numerical quantity. A user-defined counter is identified by its name,
the counter group it belongs to, the type of its value (integer or
floating-point) and the unit that the value is quoted (e.g.
"GFlop/sec"). The VT\_COUNT\_GROUP\_DEF and VT\_COUNT\_DEF
instrumentation calls can be used to define counter groups and counters:

Fortran

 

#include "vt\_user.inc"

integer :: id, gid

VT\_COUNT\_GROUP\_DEF(’name’, gid)

VT\_COUNT\_DEF(’name’, ’unit’, type, gid, id)

 

C/C++

 

#include "vt\_user.h"

unsigned int id, gid;

gid = VT\_COUNT\_GROUP\_DEF("name");

id = VT\_COUNT\_DEF("name", "unit", type, gid);

The definition of a counter group is optional. If no special counter
group is desired, the default group "User" can be used. In this case,
set the parameter gid of VT\_COUNT\_DEF() to VT\_COUNT\_DEFGROUP. The
third parameter type of VT\_COUNT\_DEF specifies the data type of the
counter value. To record a value for any of the defined counters, the
corresponding instrumentation call VT\_COUNT \* VAL must be invoked.

**Fortran:**

 

 

**Type**

Count call

Data type

VT\_COUNT\_TYPE\_INTEGER

VT\_COUNT\_INTEGER\_VAL

integer (4 byte)

VT\_COUNT\_TYPE\_INTEGER8

VT\_COUNT\_INTEGER8\_VAL

integer (8 byte)

VT\_COUNT\_TYPE\_REAL

VT\_COUNT\_REAL\_VAL

real

VT\_COUNT\_TYPE\_DOUBLE

VT\_COUNT\_DOUBLE\_VAL

double precision

 

**C/C++:**

 

 

**Type**

Count call

Data type

VT\_COUNT\_TYPE\_SIGNED

VT\_COUNT\_SIGNED\_VAL

signed int (max. 64-bit)

VT\_COUNT\_TYPE\_UNSIGNED

VT\_COUNT\_UNSIGNED\_VAL

unsigned int (max. 64-bit)

VT\_COUNT\_TYPE\_FLOAT

VT\_COUNT\_FLOAT\_VAL

float

VT\_COUNT\_TYPE\_DOUBLE

VT\_COUNT\_DOUBLE\_VAL

double

The following example records the loop index i:

Fortran

 

#include "vt\_user.inc"

program main

integer :: i, cid, cgid

VT\_COUNT\_GROUP\_DEF(’loopindex’, cgid)

VT\_COUNT\_DEF(’i’, ’#’, VT\_COUNT\_TYPE\_INTEGER, cgid, cid)

do i=1,100

    VT\_COUNT\_INTEGER\_VAL(cid, i)

end do

end program main

 

C/C++

 

#include "vt\_user.h"

int main() {

   unsigned int i, cid, cgid;

   cgid = VT\_COUNT\_GROUP\_DEF(’loopindex’);

   cid = VT\_COUNT\_DEF("i", "#", VT\_COUNT\_TYPE\_UNSIGNED, cgid);

   for( i = 1; i <= 100; i++ ) {

       VT\_COUNT\_UNSIGNED\_VAL(cid, i);

   }

   return 0;

}

For all three languages, the instrumented sources have to be compiled
with -DVTRACE. Otherwise, the VT \* calls are ignored. Optionally, if
the sources contain further VampirTrace API calls and only the calls for
user-defined counters will be disabled, then the sources have to be
compiled with -DVTRACE\_NO\_COUNT in addition to -DVTRACE .

**User-Defined Markers**

In addition to the manual instrumentation, the VampirTrace API provides
instrumentation calls which allow recording of special user information,
which can be used to better identify parts of interest. A user-defined
marker is identified by its name and type.

Fortran

 

#include "vt\_user.inc"

integer :: mid

VT\_MARKER\_DEF(’name’, type, mid)

VT\_MARKER(mid, ’text’)

 

C/C++

 

#include "vt\_user.h"

unsigned int mid;

mid = VT\_MARKER\_DEF("name",type);

VT\_MARKER(mid, "text");

 

Types for Fortran/C/C++

 

VT\_MARKER\_TYPE\_ERROR

VT\_MARKER\_TYPE\_WARNING

VT\_MARKER\_TYPE\_HINT

For all three languages, the instrumented sources have to be compiled
with -DVTRACE. Otherwise, the VT \* calls are ignored. Optionally, if
the sources contain further VampirTrace API calls and only the calls for
user-defined markers will be disabled, then the sources have to be
compiled with -DVTRACE\_NO\_MARKER in addition to -DVTRACE .

**Filtering and Grouping**

By default, all calls of instrumented functions will be traced;
consequently, the resulting trace files can easily become very large. In
order to decrease the size of a trace, VampirTrace allows the
specification of filter directives before running an instrumented
application. The user can decide on how often an instrumented
function/region should be recorded to a trace file. To use a filter, the
environment variable VT\_FILTER\_SPEC needs to be defined. It should
contain the path and name of a file with filter directives. Following is
an example of a file containing filter directives:

#VampirTrace region filter specification

#

#call limit definitions and region assignments

#

#syntax: <regions> -- <limit>

#

#regions  semicolon-separated list of regions

#         (can be wildcards)

#limit    assigned call limit

#         0 = region(s) denied

#        -1 = unlimited

#

add;sub;mul;div -- 1000

\* -- 3000000

These region filter directives allow the functions add, sub, mul and div
to be recorded at most 1000 times. The remaining functions \* will be
recorded at most 3,000,000 times.

Besides creating filter files manually, you can also use the vtfilter
tool to generate them automatically. This tool reads a provided trace
and decides whether a function should be filtered or not, based on the
evaluation of certain parameters.

**Rank Specific Filtering**

An experimental extension allows rank specific filtering. Use @ clauses
to restrict all following filters to the given ranks. The rank selection
must be given as a list of <from> - <to> pairs or single values.

@ 4 - 10, 20 - 29, 34

foo;bar -- 2000

\* -- 0

 

The example defines two limits for the ranks 4 - 10, 20 - 29, and 34.

**Attention:** The rank specific rules are activated later than usual at
MPI Init, because the ranks are not available earlier. The special MPI
routines MPI Init, MPI Init thread, and MPI Initialized cannot be
filtered in this way.

**Function Grouping**

VampirTrace allows assigning functions/regions to a group. Groups can,
for instance, be highlighted by different colors in Vampir displays. The
following standard groups are created by VampirTrace:

**Group name**

**Contained functions/regions**

MPI

MPI functions

OMP

OpenMP API function calls

OMP\_SYNC

OpenMP barriers

OMP\_PREG

OpenMP parallel regions

Pthreads

Pthread API function calls

MEM

Memory allocation functions (⇒ Section [#mem\_alloc\_counter [\*]])

I/O

I/O functions (⇒ Section [#io\_calls [\*]])

LIBC

LIBC fork/system/exec functions (⇒ Section [#execfork [\*]])

Application

remaining instrumented functions and source code regions

Additionally, you can create your own groups, if, for example, you wish
to better distinguish different phases of an application. To use
function/region grouping, set the environment variable VT\_GROUPS\_SPEC
to the path of a file which contains the group assignments. Below is an
example of how to use group assignments:

# VampirTrace region groups specification

#

# group definitions and region assignments

#

# syntax: <group>=<regions>

#

# group       group name

# regions     semicolon-separated list of regions

#             (can be wildcards)

#

CALC=add;sub;mul;div

USER=app\_\*

These group assignments associate the functions add, sub, mul and div
with group "CALC", and all functions with the prefix app are associated
with group "USER".

 

Official HPCC Results from the Acceptance Tests
===============================================

-  `1 HPCC Results <#HPCC_Results>`__

   -  `1.1 Official HPCC Results from the Acceptance
      Tests <#Official_HPCC_Results_from_the_Acceptance_Tests>`__

      -  `1.1.1 Alamo <#Alamo>`__
      -  `1.1.2 India <#India>`__
      -  `1.1.3 Hotel <#Hotel>`__
      -  `1.1.4 XRay <#XRay>`__

-  `2 HPCC Configuration <#HPCC_Configuration>`__

   -  `2.1 General Information <#General_Information>`__

      -  `2.1.1 India <#India_2>`__
      -  `2.1.2 Hotel <#Hotel_2>`__
      -  `2.1.3 Xray <#Xray_2>`__

   -  `2.2 Configuration Files <#Configuration_Files>`__

      -  `2.2.1 India <#India_3>`__
      -  `2.2.2 Hotel <#Hotel_3>`__
      -  `2.2.3 XRay <#XRay_3>`__

HPCC Results
============

Official HPCC Results from the Acceptance Tests
-----------------------------------------------

Alamo \ **(`view machine details </manual/alamo>`__)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| **HPCC Results**   | **G-HPL**   | **G-PTRANS**   | **G-FFTE**    | **G-Random**   | **G-STREAM**   | **EP-STREAM**   | **EP-DGEMM**   | **Random Ring Bandwidth**   | **Random Ring Latency**   | **% HPL Peak(\*)**   |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| **Node**           | **CPU**     | **Core**       | **TFLOP/s**   | **GB/s**       | **GLFOP/s**    | **Gup/s**       | **GB/s**       | **GB/s**                    | **GFLOP/s**               | **GB/s**             | **usec**   | **Percent**   |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| 32                 | 64          | 256            | 2.291         | 29.81          | 93.54          | 0.92            | 3700.060       | 3.71                        | 10.691                    | 0.219                | 14.86      | 84.12         |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+

India \ **(`view machine details </manual/india>`__)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| **HPCC Results**   | **G-HPL**   | **G-PTRANS**   | **G-FFTE**    | **G-Random**   | **G-STREAM**   | **EP-STREAM**   | **EP-DGEMM**   | **Random Ring Bandwidth**   | **Random Ring Latency**   | **% HPL Peak(\*)**   |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| **Node**           | **CPU**     | **Core**       | **TFLOP/s**   | **GB/s**       | **GLFOP/s**    | **Gup/s**       | **GB/s**       | **GB/s**                    | **GFLOP/s**               | **GB/s**             | **usec**   | **Percent**   |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| 128                | 256         | 1024           | 11.3428       | 59.5363        | 225.7700       | 2.2630          | 3700.060       | 3.6133                      | 12.0419                   | 0.0852               | 19.6622    | 94.513        |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| 84                 | 168         | 672            | 7.3097        | 65.9453        | 135.6070       | 1.7364          | 2438.271       | 3.6284                      | 11.7255                   | 0.0968               | 18.1360    | 92.812        |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| 32                 | 64          | 512            | 2.8210        | 21.1257        | 70.3138        | 0.0507          | 865.193        | 3.3797                      | 12.0083                   | 0.1264               | 15.0372    | 94.022        |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+

(\*) Calculated using the base frequency of the processor. (Intel Turbo
Boost technology was enabled)

Hotel \ **(`view machine details </manual/hotel>`__)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| **HPCC Results**   | **G-HPL**   | **G-PTRANS**   | **G-FFTE**    | **G-Random**   | **G-STREAM**   | **EP-STREAM**   | **EP-DGEMM**   | **Random Ring Bandwidth**   | **Random Ring Latency**   | **% HPL Peak(\*)**   |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| **Node**           | **CPU**     | **Core**       | **TFLOP/s**   | **GB/s**       | **GLFOP/s**    | **Gup/s**       | **GB/s**       | **GB/s**                    | **GFLOP/s**               | **GB/s**             | **usec**   | **Percent**   |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| 84                 | 168         | 672            | 6.9401        | 83.3561        | 158.4620       | 2.3839          | 2512.2854      | 3.7385                      | 11.2254                   | 0.1280               | 6.1591     | 90.36         |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| 32                 | 64          | 256            | 2.6360        | 26.8054        | 95.6900        | 1.4378          | 959.4496       | 3.7479                      | 11.2031                   | 0.1502               | 5.5892     | 90.09         |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+

XRay \ **(`view machine details </manual/xray>`__)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| **HPCC Results**   | **G-HPL**   | **G-PTRANS**   | **G-FFTE**    | **G-Random**   | **G-STREAM**   | **EP-STREAM**   | **EP-DGEMM**   | **Random Ring Bandwidth**   | **Random Ring Latency**   | **% HPL Peak(\*)**   |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| **Node**           | **CPU**     | **Core**       | **TFLOP/s**   | **GB/s**       | **GLFOP/s**    | **Gup/s**       | **GB/s**       | **GB/s**                    | **GFLOP/s**               | **GB/s**             | **usec**   | **Percent**   |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+
| 84                 | 168         | 672            | 5.38          | 29.27          | 75.47          | 0.62            | 2017           | 3.00                        | 8.93                      | 0.047                | 26.8       | 83.40         |
+--------------------+-------------+----------------+---------------+----------------+----------------+-----------------+----------------+-----------------------------+---------------------------+----------------------+------------+---------------+

| 
|   

HPCC Configuration
==================

General Information
-------------------

What version was used, how as it compiled etc.

India
~~~~~

-  HPCC version: 1.3.1
-  Compiler: Intel compiler 11.1.038 with OpenMPI-1.3.1.
-  Math Library: Intel MKL library.
-  A few important settings in Makefile:

   -  CC=mpicc
   -  LINKER=mpicc -mkl

Hotel
~~~~~

-  HPCC version: 1.3.1
-  Compiler: Intel compiler 11.1.038 with Intel MPI-4.0.0.
-  Math Library: Intel MKL library.
-  A few important settings in Makefile:

   -  CC=mpicc
   -  LINKER=mpicc -mkl

Xray
~~~~

-  HPCC version: 1.3.1
-  Compiler: Cray compiler (xt-asyncpe-3.4)
-  A few important settings in Makefile:
-  Settings in Makefile: CC=mpicc and LINKER=mpicc -mkl

   -  CC=cc
   -  CCNOOPT=$(HPL\_DEFS) -DLONG\_IS\_64BITS
   -  CCFLAGS=$(HPL\_DEFS) -fast -Minfo=loop -Mneginfo=loop
      -DLONG\_IS\_64BITS -DFFTE\_NP=4
   -  CCFLAGS\_STREAM=$(HPL\_DEFS) -Mnontemporal
      -Mprefetch=distance:8,nta -Msafeptr -fastsse -Minfo=loop
      -Mneginfo=loop -DLONG\_IS\_64BITS

Configuration Files
-------------------

Below are the contents of input files, hpccinf.txt, for HPCC.

India
~~~~~

::

    HPLinpack benchmark input file
    Innovative Computing Laboratory, University of Tennessee
    HPL.out output file name (if any)
    8 device out (6=stdout,7=stderr,file)
    1 # of problems sizes (N)
    409600 Ns
    1 # of NBs
    112 NBs
    0 PMAP process mapping (0=Row-,1=Column-major)
    1 # of process grids (P x Q)
    32 Ps
    32 Qs
    16.0 threshold
    1 # of panel fact
    2 PFACTs (0=left, 1=Crout, 2=Right)
    1 # of recursive stopping criterium
    4 NBMINs (>= 1)
    1 # of panels in recursion
    3 NDIVs
    1 # of recursive panel fact.
    2 RFACTs (0=left, 1=Crout, 2=Right)
    1 # of broadcast
    3 BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
    1 # of lookahead depth
    0 DEPTHs (>=0)
    2 SWAP (0=bin-exch,1=long,2=mix)
    64 swapping threshold
    0 L1 in (0=transposed,1=no-transposed) form
    0 U in (0=transposed,1=no-transposed) form
    1 Equilibration (0=no,1=yes)
    16 memory alignment in double (> 0)
    ##### This line (no. 32) is ignored (it serves as a separator). ######
    0 Number of additional problem sizes for PTRANS
    1200 10000 30000 values of N
    0 number of additional blocking sizes for PTRANS
    40 9 8 13 13 20 16 32 64 values of NB

 

Hotel
~~~~~

::

    HPLinpack benchmark input file
    Innovative Computing Laboratory, University of Tennessee
    HPL.out output file name (if any)
    8 device out (6=stdout,7=stderr,file)
    1 # of problems sizes (N)
    338688 Ns
    1 # of NBs
    112 NBs
    0 PMAP process mapping (0=Row-,1=Column-major)
    1 # of process grids (P x Q)
    32 Ps
    32 Qs
    16.0 threshold
    1 # of panel fact
    2 PFACTs (0=left, 1=Crout, 2=Right)
    1 # of recursive stopping criterium
    4 NBMINs (>= 1)
    1 # of panels in recursion
    3 NDIVs
    1 # of recursive panel fact.
    2 RFACTs (0=left, 1=Crout, 2=Right)
    1 # of broadcast
    3 BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
    1 # of lookahead depth
    0 DEPTHs (>=0)
    2 SWAP (0=bin-exch,1=long,2=mix)
    64 swapping threshold
    0 L1 in (0=transposed,1=no-transposed) form
    0 U in (0=transposed,1=no-transposed) form
    1 Equilibration (0=no,1=yes)
    16 memory alignment in double (> 0)
    ##### This line (no. 32) is ignored (it serves as a separator). ######
    0 Number of additional problem sizes for PTRANS
    1200 10000 30000 values of N
    0 number of additional blocking sizes for PTRANS
    40 9 8 13 13 20 16 32 64 values of NB

 

 

XRay
~~~~

::

    HPLinpack benchmark input file
    Innovative Computing Laboratory, University of Tennessee
    HPL.out output file name (if any)
    6 device out (6=stdout,7=stderr,file)
    1 # of problems sizes (N)
    373056 Ns
    1 # of NBs
    232 NBs
    0 PMAP process mapping (0=Row-,1=Column-major)
    1 # of process grids (P x Q)
    24 Ps
    28 Qs
    16.0 threshold
    1 # of panel fact
    1 PFACTs (0=left, 1=Crout, 2=Right)
    1 # of recursive stopping criterium
    4 NBMINs (>= 1)
    1 # of panels in recursion
    2 NDIVs
    1 # of recursive panel fact.
    2 RFACTs (0=left, 1=Crout, 2=Right)
    1 # of broadcast
    1 BCASTs (0=1rg,1=1rM,2=2rg,3=2rM,4=Lng,5=LnM)
    1 # of lookahead depth
    0 DEPTHs (>=0)
    2 SWAP (0=bin-exch,1=long,2=mix)
    64 swapping threshold
    0 L1 in (0=transposed,1=no-transposed) form
    0 U in (0=transposed,1=no-transposed) form
    1 Equilibration (0=no,1=yes)
    8 memory alignment in double (> 0)
    ##### This line (no. 32) is ignored (it serves as a separator). ######
    0 Number of additional problem sizes for PTRANS
    1200 values of N
    4 number of additional blocking sizes for PTRANS
    23 31 33 63 values of NB

    HPLinpack benchmark input file
    Innovative Computing Laboratory, University of Tennessee
    HPL.out output file name (if any)
    8 device out (6=stdout,7=stderr,file)

| 

Foxtrot
=======

 

UF iDataPlex User Manual

  Hostname
^^^^^^^^^^

• foxtrot.futuregrid.org

  Login
^^^^^^^

    ::

        ssh username@foxtrot.futuregrid.org

where *username* is your FutureGrid username. You must have an account
on FutureGrid.

Compute **(**\ domain: idp.ufl.futuregrid.org)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**2x IBM x3650 M2 management nodes** (fm1, fm2):

| • 2 x 4-Core Intel Xeon E5530 (Nehalem-EP) processors
|  • 24GB Main Memory 
|  • 2 x 146GB 2.5-Inch 6Gbps SAS Disks

**32x IBM iDataPlex dx360 M2 nodes** (f1 through f2):

| • 2 x 4-Core Intel Xeon E5520 (Nehalem-EP) processors
|  • 24GB Main Memory 
|  • 1 x 500GB 3.5-Inch SATA Disk

**1x Dell PowerEdge R310 Network monitoring node**
(bwctl.ufl.net.futuregrid.org)

 Storage
^^^^^^^^

**Hardware**:  IBM iDataPlex dx360 M3 storage node with 24TB raw
capacity (fs1).

| • 2 x 4-Core Intel Xeon E5520 (Nehalem-EP) processors
|  • 24GB Main Memory 
|  • 12 x 2TB 7200 rpm 3.5-Inch 6Gbps SAS Disks

**Capacity**:  20TB RAID5

**Storage Interconnect**:  NFS export over GigE.

**Filesystem Type**:  XFS 

**Filesystem Layout**:

| • Home directories mounted to all foxtrot nodes (f1 thorugh f32) at
/N/u/<username>
|  • Backup is not provided

Network
^^^^^^^

**Hardware**

| • Force10 S50 48-port GigE switch, with 10GigE uplink to Florida
LambdaRail
|  • BLADE Rackswitch 48-port GigE switch (Management Network)

Services
^^^^^^^^

**Nimbus**

• Refer to `Nimbus
manual. <https://portal.futuregrid.org/manual/services/nimbus>`__

India
=====

IU iDataplex User Manual
------------------------

  Hostname
^^^^^^^^^^

| • india.futuregrid.org 
|  • i136r.idp.iu.futuregrid.org 

  Login
^^^^^^^

    ::

        ssh username@india.futuregrid.org

Above, *username* represents your FutureGrid username. You must have an
account on FutureGrid to log in.

Sierra
======

UCSD iDataPlex User Manual
--------------------------

  Hostname
^^^^^^^^^^

• sierra.futuregrid.org

  Login
^^^^^^^

    ::

        ssh sierra.futuregrid.org

  Storage
^^^^^^^^^

**Hardware**:  Two Sun Fire x4540 Servers @ 48 TB each.  Specifications
for each Sun Fire X4540 Server are: 

| • 2 x 6-Core AMD Opteron Model 2435, 2.6 GHz Processors 
|  • 32 GB (16 x 2 GB DIMMs) Memory 
|  • 48 x 1 TB 7200 rpm 3.5-Inch SATA Disks

**Capacity**:  76.8 TB raid2 and 5.4 TB of raid0 (for scratch)

**Storage Interconnect**:  Currently mounted to cluster over GigE
ethernet.  Our long-term plan is to mount over Infiniband. 

**Filesystem Type**:  ZFS 

**Filesystem Layout**:

| • Home directories mounted to Sierra at /N/u/<username>, snapshots
taken nightly, quota set at 50 GB 
|  • Scratch directories mount to Sierra at /N/scratch/<username>, no
backup, quota at 100 GB 
|  • Project directories, software directory mounted to Sierra as
/N/soft, snapshots taken nightly, quota set at 50 GB 
|  • Image directory (internal), mounts to Sierra at /images, snapshots
taken nightly, quota set at 6 TB

**Overview of ZFS Data Snapshots**

A zfs snapshot is a read-only copy of a Solaris ZFS file system or
volume. Snapshots can be created almost instantly and initially consume
no additional disk space within the pool. All users on Sierra have
access to their ZFS hidden file system at

    $HOME/.zfs/

ZFS supports the ability to restore lost files with the standard UNIX
copy command. See the example below.

Users are expected to make their own permanent backups of valuable data
on the home file system. ZFS Snapshots are NOT permanent backups. Users
are currently limited to a quota of 50 GB of snapshots. 

**Example of ZFS Data Snapshot Restore Session**

    ::

        $ ls
        1G  4G

    ::

        $ ls .zfs
        snapshot/

    ::

        $ ls .zfs/snapshot
        SNAPSHOT2009-06-22-1245668520/  SNAPSHOT2009-06-24-1245841320/
        SNAPSHOT2009-06-22-1245668674/  SNAPSHOT2009-06-25-1245927720/
        SNAPSHOT2009-06-23-1245754920/  SNAPSHOT2009-06-26-1246014120/

    ::

        $ rm 1G
        $ ls
        4G

    ::

        $ ls .zfs/snapshot/SNAPSHOT2009-06-26-1246014120/
        1G  4G

    ::

        $ cp .zfs/snapshot/SNAPSHOT2009-06-26-1246014120/1G .

    ::

        $ ls
        1G  4G

 Dynamic Provisioning sing Moab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

THIS FEATURE IS NOT YET SUPPORTED OFFICIALLY

FutureGrid now supports dynamic provisioning through Moab, and in
Sierra, some instructions are listed below:

| • The executable tools are installed at /usr/local/bin, and the $PATH
should have been all set. So a user could start running from his home
directory. 
|  • Command \ *qnodes* will list all the nodes and status. As for now,
node s36~s39 is up and running and should be available for
test/experiment. 
|  • \ *checknode s36* will list info on node s36. Os info can be found
at line such as:

    ::

         Opsys:      statelessrhels5.5  Arch:      x86_64

Now we have \ *statelessrhels5.5* and *statefulrhels5* as two options.

• If all the four nodes are running stateless os, submit a command like
this:

    ::

         msub -l os=statelessrhels5.5 testcmd.sh

will schedule the job in some node.

| • \ *showq* will list the current queue info, and you could see the
submitted job in the \ *active jobs* section. 
|  • Check job running status using command \ *checkjob <jobid>*. The
resource allocation info could be found in some lines like these:

    ::

         Allocated Nodes:
         [s36:1]

In this case the job is scheduled at node s36.

• In the case where all four nodes are running stateless os, submitting
a job like this:

    ::

         msub -l os=statefulrhels5 testcmd.sh

will try first to dynamically provision the requested os at some node,
and then schedule the job.

| • \ *showq* once again could list the jobs. 
|  • \ *checkjob <jobid>* will first tell you the dependency
job \ *provisioning os* is not completed.

    ::

          NOTE:  job cannot run  (dependency provision-73 jobsuccessfulcomplete not met)

| • \ *checkjob provision-68(the provision job id)* will list the
provisioning status. 
|  • Once the provisioning is done, \ *checkjob <jobid>* will show the
job is scheduled, and also allow us to see where is it scheduled, for
example s37. 
|  • By running \ *checknode s37* again, we could see that the running
os was changed from \ *statelessrhels5.5* to*statefulrhels5*.

• \ *testcmd.sh* used in the example:

    ::

         $ cat testcmd.sh 
         #!/bin/bash
         /bin/date
         sleep 300
         /bin/date

 

Xray
====

 

This section is maintained by Greg Pike; please contact  `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__ for more information.
----------------------------------------------------------------------------------------------------------------------------------------------------------

It will include system specific information relevant to xray.

IU Cray User Manual
-------------------

  Hostname
^^^^^^^^^^

• xray.futuregrid.org

  Login
^^^^^^^

    ::

        ssh xray.futuregrid.org

 Filesystem
^^^^^^^^^^^

 Compiler
^^^^^^^^^

For MPI jobs, use cc (pgcc).

For best performance, add the xtpe-barcelona module 

    ::

        % module add xtpe-module

 Cray Programming Environment Manuals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `http://docs.cray.com/cgi-bin/craydoc.cgi?q=&mode=Search&hw=%22Cray+XT5%22 <http://docs.cray.com/cgi-bin/craydoc.cgi?mode=View;id=S-2396-21>`__
-  `http://docs.cray.com/cgi-bin/craydoc.cgi?mode=View;id=S-2396-21 <http://docs.cray.com/cgi-bin/craydoc.cgi?mode=View;id=S-2396-21>`__

  Queue
^^^^^^^

Currently there is only one queue (batch) available to users on the
Cray, and all jobs are automatically routed to that queue.

 Listing Queues on Xray
^^^^^^^^^^^^^^^^^^^^^^^

    ::

         qstat -Q

The primary queue for running jobs on Xray is batch. To obtain details
of running jobs and available processors, use the showq command.

    ::

        /opt/moab/default/bin/showq

 Submitting a job
~~~~~~~~~~~~~~~~~

**MPI run cmd**:  aprun

Example \ **job script (16 processors / 2 nodes):**

    ::

        % cat job.sub 

    ::

        #!/bin/sh
        #PBS -l mppwidth=16 
        #PBS -l mppnppn=8 
        #PBS -N hpcc-16 
        #PBS -j oe 
        #PBS -l walltime=7:00:00 
        #cd to directory where job was submitted from 
        cd $PBS_O_WORKDIR 
        export MPICH_FAST_MEMCPY=1 
        export MPICH_PTL_MATCH_OFF=1 
        aprun -n 16 -N 8 -ss -cc cpu hpcc
        % qsub job.sub 

 Looking at the Queue

    ::

        % qstat

How Do I Submit a Job to the Cray XT5m on FutureGrid?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`http://kb.iu.edu/data/azse.html <http://kb.iu.edu/data/azse.html>`__

The XT5m is a 2D mesh of nodes. Each node has two sockets, and each
socket has four cores.

The batch scheduler interfaces with a Cray resource scheduler called
APLS. When you submit a job, the batch scheduler talks to ALPS to find
out what resources are available, and ALPS then makes the reservation.

Currently ALPS is a "gang scheduler" and only allows one "job" per node.
If a user submits a job in the format aprun -n 1 a.out , ALPS will put
that job on one core of one node and leave the other seven cores empty.
When the next job comes in, either from the same user or a different
one, it will schedule that job to the next node.

If the user submits a job with aprun -n 10 a.out , then the scheduler
will put the first eight tasks on the first node and the next two tasks
on the second node, again leaving six empty cores on the second node.
The user can modify the placement with -N , -S , and -cc .

A user might also run a single job with multiple treads, as with OpenMP.
If a user runs this job aprun -n 1 -d 8 a.out , the job will be
scheduled to one node and have eight threads running, one on each core.

You can run multiple, different binaries at the same time on the same
node, but only from one submission. Submitting a script like this
will not work:

    ::

        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 0 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 1 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 2 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 3 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 4 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 5 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 6 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 7 ./my-binary

This will run a job on each core, but not at the same time. To run all
jobs at the same time, you need to first bury all the binaries under
one aprun command:

    ::

        $ more run.sh
        ./my-binary1
        ./my-binary2
        ./my-binary3
        ./my-binary4
        ./my-binary5
        ./my-binary6
        ./my-binary7
        ./my-binary8
        $ aprun -n 1 run.sh

Alternatively, use the command aprun -n 1 -d 8 run.sh . To run multiple
serial jobs, you must build a batch script to divide the number of jobs
into groups of eight, and the

Alamo
=====

| Alamo is a 96 node Dell cluster running 2.66 GHz Intel Xeon X5550
processors.  The OS is CentOS 5.8 and 6.3.  It runs Torque and Moab for
scheduling.  Alamo has a QDR IB interconnect and 15 TB of attached disk
storage.   Alamo is partitioned into different resources for Nimbus and
HPC.  See the Alamo hardware page for more
detail: \ `https://portal.futuregrid.org/hardware/alamo <https://portal.futuregrid.org/hardware/alamo>`__
.
| 
|  **Nimbus partition -** see nimbus
documentation: \ `https://portal.futuregrid.org/tutorials/nimbus <https://portal.futuregrid.org/tutorials/nimbus>`__
| 
|  **HPC partition**
| 
|  Max cores 584.  Submit
`ticket <http://%20https://portal.futuregrid.org/help>`__ if you need to
run larger than the 320 limit per user. 
| 
|  Available queues: 
|     short - 24 hours runtime limit
|     long - 72 hours runtime limit
| 
|  After registering your .ssh key on the portal, go to
`https://portal.futuregrid.org/manual/access <https://portal.futuregrid.org/manual/access>`__
.
| 
|  If you key has been uploaded, you can ssh to the login node using the
following command. 
|  **Note**: If you are prompted for a password, your account has not
been set up correctly or the .ssh key has not been propagated. 
| 
|    ssh alamo.futuregrid.org
| 
|  To submit a test job use the qsub command.
| 
|  ex.  qsub -N job\_name -l nodes=1 -q short  job\_script

-  qstat - show current jobs in the queue with status
-  showq - show current running and queued jobs and job id
-  checkjob -v <jobid>   - more detailed information about your job

| Applications are available via modules.  To see a list of available
applications:
|    module avail
| 
|  File systems:
|     /home   - Quota enforced home directory, backed up nightly.
|     /N/work - 6.3 TB work directory, not backed up. NFS mounted from
login node. 
|     /N/images - 11 TB directory for system images, not backed up. NFS
mounted from login node.
| 
|  Administrator: David Gignac
|  For issues or questions please
use \ `https://tickets.futuregrid.org <https://tickets.futuregrid.org>`__
. You can conveniently submit a ticket
via \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__.
To look at your previously submitted tickets you can
use \ `https://portal.futuregrid.org/tickets <https://portal.futuregrid.org/tickets>`__
.
| 
|    
| 

Delta
=====

GPU User Manual
---------------

| FutureGrid's supercomputer, Delta (delta.futuregrid.org), is a 16-node
GPU cluster running Red Hat Linux, with TORQUE (also called PBS) and
Moab for job management, and Module to simplify application and
environment configuration. Delta consists of 16 nodes with two 6-core
Intel X5560 processors at 2.8GHz, 192 GB of DDR3 memory, and 15TB
of RAID5 disk storage. Each node supports 2 nVIDIA Tesla C2070 GPUs
with 448 processing cores. For details on Delta's hardware
configuration, see the
`Delta <https://portal.futuregrid.org/hardware/delta>`__\ page.
| 
| 
|  The FutureGrid *delta* cluster is accessible via a batch queue that
is managed from india (india.futuregrid.org). To use delta
interactively, first log into india:

::

     ssh username@india.futuregrid.org

| Then, on india, the following command lets you use one of the delta
compute nodes:

::

     qsub -I -q delta myprg

| If you want to use delta with your job script, please use

::

     #PBS -q 

::

::

    delta

| to indicate that you'd like to use this queue.
| 
|  For more details about how to manage queues with qsub, see the Delta
manual page.
| 
|  Utilization of GPU resources on Delta:
|  1) Utilize GPU node
|      ` Running Program on single GPU
node <https://portal.futuregrid.org/manual/gpu/running-programs-single-gpu>`__
|  2) Utilize GPU cluster
|  `     Running MPI/CUDA program on the Delta
cluster <https://portal.futuregrid.org/manual/running-mpigpu-program-delta-cluster>`__
|  3) Utilize GPU cloud
|  4) Mixing utilization of GPU and CPU
|  5) Non-trivial service or applications using GPU
| 
| 
|       

Running MPI/GPU program on the Delta cluster
============================================

| GPUs provide the ability to use mathematical operations at a fraction
of the cost and with higher performance than on the current generation
of processors. FutureGrid provides the ability to test such an
infrastructure as part of its delta cluster. Here, we provide a
step-by-step guide on how to run a
parallel matrix multiplication program using IntelMPI and CUDA on Delta
machines. The MPI framework distributes the work among compute
nodes, each of which use CUDA to execute the shared workload. We also
provide the complete parallel
matrix multiplication code using MPI/CUDA that has already been tested
on Delta cluster in attachment.  
| 
|  **MPI code: pmm\_mpi.c**
| 

.. code:: rteindent1

    #include <mpi.h>

    void invoke_cuda_vecadd();

           int main(int argc, char *argv[])
    {
              int rank, size;

              MPI_Init (&argc, &argv); /* starts MPI */
              MPI_Comm_rank (MPI_COMM_WORLD, &rank); /* get current process id */
              MPI_Comm_size (MPI_COMM_WORLD, &size); /* get number of processes */
              invoke_cuda_vecadd();  /* the cuda code */
              MPI_Finalize();
     return 0;
    } 

| 
|  **CUDA code: dgemm\_cuda.cu**

| #include <stdio.h>
| 
|  \_\_global\_\_ void cuda\_vecadd(int \*array1, int \*array2, int
\*array3)
|  {
|          int index = blockIdx.x \* blockDim.x + threadIdx.x;
|          array3[index] = array1[index] + array2[index];
|  }
| 
|    extern "C" void invoke\_cuda\_vecadd()
|   {
|          cudaMalloc((void\*\*) &devarray1, sizeof(int)\*10);
|          cudaMalloc((void\*\*) &devarray2, sizeof(int)\*10);
|          cudaMalloc((void\*\*) &devarray3, sizeof(int)\*10);
|          cudaMemcpy(devarray1, hostarray1, sizeof(int)\*10,
cudaMemcpyHostToDevice);
|          cudaMemcpy(devarray2, hostarray2, sizeof(int)\*10,
cudaMemcpyHostToDevice);
|          cuda\_vec\_add<<<1, 10>>>(devarray1, devarray2, devarray3);
|         cudaMemcpy(hostarray3, devarray3, sizeof(int)\*10,
cudaMemcpyDeviceToHost);
|         cudaFree(devarray1);
|         cudaFree(devarray2);
|         cudaFree(devarray3);
|  }

Note: Mixing MPI and CUDA code may cause problems during linking because
of the difference between C and C++ calling conventions. The use of
extern "C" around invoke\_cuda\_code which instructs the nvcc (a wrapper
of c++) compiler to make that function callable from the C runtime. 

| **Compiling the MPI/CUDA program:**
| 
|  Load the Modules
|  > module load IntelMPI # load Intel MPI
|  > module load Intel # load icc > module load cuda # load cuda tools
|  This will load the Intel MPI, the compiler, and the cuda tools. Next
compile the code with 
| 
|  > nvcc -c dgemm\_cuda.cu -o dgemm\_cuda.o   > mpiicc
-o pmm\_mpi.c -o pmm\_mpi.o
|  > mpiicc -o mpicuda pmm\_mpi.o dgemm\_cuda.o -lcudart -lcublas -L
/opt/cuda/lib64 -I /opt/cuda/include
| 
|  Note: The CUDA compiler nvcc is used only to compile the CUDA source
file, and the IntelMPI compiler mpiicc is used to compile the C code and
do the linking
|    **Setting Up and Submitting MPI Jobs:**
| 
|  1. qsub -I -l nodes=4 -q delta        # get 4 nodes from FG
|  2. uniq /var/spool/torque/aux/399286.i136
> gpu\_nodes\_list       #create machine file list
|  3. module load IntelMPI                # load Intel MPI
|  4. module load Intel                     # load icc
|  5. module load cuda                     # load cuda tools
|  6. mpdboot -r ssh -f gpu\_nodes\_list -n 4  # will start an mpd ring
on 4 nodes including local host 
|  7. mpiexec -l -machinefile gpu\_nodes\_list -n 4 ./mpicuda 10000 1 4 
# run mpi program using 4 nodes
| 
|  **Comparison between four implementations of sequential matrix
multiplication on Delta:**
| 
|      |image79|
|  **References:** `Source Code
Package <https://portal.futuregrid.org/sites/default/files/mpi_cuda_mkl.zip>`__
|  [1] High Performance Computing using CUDA,2009 User Group Conference
|  [2]
`http://www.nvidia.com/content/global/global.php <http://www.nvidia.com/content/global/global.php>`__
| 
|  To get source code: git clone git@github.com:futuregrid/GPU.git
| 
|  Compiling source code on Delta machine:

.. code:: rteindent1

    module load intelmpi
    module load intel
    module load cuda
    cd mpi_cuda_mkl
    make

| 

+-----------------------------------------------------------------------------------------------+-------------+
| Attachment                                                                                    | Size        |
+===============================================================================================+=============+
| `mpi\_cuda\_mkl.zip <https://portal.futuregrid.org/sites/default/files/mpi_cuda_mkl.zip>`__   | 888.92 KB   |
+-----------------------------------------------------------------------------------------------+-------------+

Running programs on a single GPU
================================

**Summary:**

|      GPUs provide the ability to use mathematical operations at a
fraction of the cost and with higher performance than on the
current generation of processors. CUDA is a parallel programming model
and software environment that leverages the parallel computational power
of GPU for non-graphics computing in a fraction of the time required on
a CPU. FutureGrid provides the ability to test such a hardware and
software environment as part of its Delta cluster. Here, we illustrate
some details of data-parallel computational model of CUDA, and then
provide a step-by-step guide on how to make a parallel matrix
multiplication program using CUDA. In the supplied attachment, we also
provide the complete code that has already been tested on Delta node.
| 
|     |image80|
|  Figure 1: GPU Kernel and Thread model [1]
| 
|   **CUDA Kernel and Threads:**
|         The fundamental part of the CUDA code is the kernel program.
Kernel is the function that can be executed in parallel in the GPU
device. A CUDA kernel is executed by an array of CUDA threads. All
threads run the same code. Each thread has an ID that it uses to compute
memory address and make a control decision. CUDA supports to run
thousands of threads on the GPU. CUDA organizes thousands
of threads into a hierarchy of a grid of thread blocks. A grid is a set
of thread blocks that can be processed on the device in parallel. A
thread block is a set of concurrent threads that can cooperate among
themselves through a synchronization barrier and access to a shared
memory space private to the block. Each thread is given a unique thread
ID— thread.Idx within its thread block. Each thread block is given a
unique block ID— block.Idx within its grid. 
| 
|    **CUDA Kernel code for Matrix Multiplication:**
| 
|   \_\_global\_\_ void matrixMul( float\* C, float\* A, float\* B, int
wA, int wB)
|   {
|       // Block index
|             int bx = blockIdx.x;
|             int by = blockIdx.y;
|       // Thread index
|             int tx = threadIdx.x;
|             int ty = threadIdx.y;
| 
|       // Index of the first sub-matrix of A processed by the block
|             int aBegin = wA \* BLOCK\_SIZE \* by;
|       // Index of the last sub-matrix of A processed by the block
|             int aEnd   = aBegin + wA - 1;
|       // Step size used to iterate through the sub-matrices of A
|             int aStep  = BLOCK\_SIZE;
|       // Index of the first sub-matrix of B processed by the block
|             int bBegin = BLOCK\_SIZE \* bx;
|       // Step size used to iterate through the sub-matrices of B
|             int bStep  = BLOCK\_SIZE \* wB;
|       // Csub is used to store the element of the block
sub-matrix that is computed by the thread
|       float Csub = 0;
|       // Loop over all the sub-matrices of A and B required to compute
the block sub-matrix
|       for (int a = aBegin, b = bBegin; a <= aEnd; a += aStep, b +=
bStep) {
|            // Declaration of the shared memory array As used to store
the sub-matrix of A
|            \_\_shared\_\_ float As[BLOCK\_SIZE][BLOCK\_SIZE];
|            // Declaration of the shared memory array Bs used to store
the sub-matrix of B
|            \_\_shared\_\_ float Bs[BLOCK\_SIZE][BLOCK\_SIZE];
|             As[ty][tx] = A[a + wA \* ty +
tx];                                                                 
|                  Bs[ty],[tx] = B[b + wB \* ty +
tx];                                                                 
|            // Synchronize to make sure the matrices are
loaded                                               
|                 
\_\_syncthreads();                                                                                  
|            // multiply two matrices together; each thread computes one
element  of  sub-matrix
|   #pragma
unroll                                                                                            
|            for (int k = 0; k < BLOCK\_SIZE;
++k)                                                              
|                         Csub += As[ty][k] \*
Bs[k][tx];                                                                
| 
                                                                                                           
|            // Synchronize to make sure that the preceding computation
is done                   
|                 
\_\_syncthreads();                                                                                  
|       
}                                                                                                     
|        // Write the block sub-matrix to device memory; each thread
only writes one element!
|          int c = wB \* BLOCK\_SIZE \* by + BLOCK\_SIZE \*
bx;                                                       
|        C[c + wB \* ty + tx] =
Csub;                                                                           
|  }                                   
| 
|     
|    |image81|
|  Figure 2: GPU memory architecture [1][1] [1]
| 
| 
|   **CUDA Memory Architecture:**
|      All multiprocessors of the GPU device access a large global
device memory for both gather and scatter operations. This memory is
relatively slow because it does not provide caching. Shared memory is
fast compared to device memory, and normally takes the same amount of
time as required to access registers. Shared memory is “local” to each
multiprocessor unlike device memory and allows more efficient local
synchronization. It is divided into many parts. Each thread block within
a multiprocessor accesses its own part of shared memory, and this part
of shared memory is not accessible by any other thread block of this
multiprocessor or of some other multiprocessor. All threads within a
thread block that have the same lifetime as the block share this part of
memory for both read and write operations. To declare variables in
shared memory, \_\_shared\_\_ qualifier is used, and to declare in
global memory, \_\_device\_\_ qualifier is used.
| 
|  **CPU code invoke CUDA kernel code:**
| 
|  void invoke\_matrixMul(int size){    
| 
|            int devID;
|            cudaDeviceProp props;
|            checkCudaErrors(cudaGetDevice(&devID));
|            checkCudaErrors(cudaGetDeviceProperties(&props, devID));
| 
|            int block\_size = (props.major < 2) ? 16 : 32;
|      unsigned int uiWA, uiHA, uiWB, uiHB, uiWC, uiHC;
|            uiWA = uiHA= uiWB = uiHB = uiWC = uiHC;
| 
|      // allocate host memory for matrices A and B
|      unsigned int size\_A = uiWA \* uiHA;
|      unsigned int mem\_size\_A = sizeof(float) \* size\_A;
|      float\* h\_A = (float\*)malloc(mem\_size\_A);
|      unsigned int size\_B = uiWB \* uiHB;
|      unsigned int mem\_size\_B = sizeof(float) \* size\_B;
|      float\* h\_B = (float\*)malloc(mem\_size\_B);
| 
|  **    **// initialize host memory
|            srand(2012);
|            randomInit(h\_A, size\_A);
|            randomInit(h\_B, size\_B);
| 
|      // allocate device memory
|      float\* d\_A, \*d\_B, \*d\_C;
|      unsigned int size\_C = uiWC \* uiHC;
|      unsigned int mem\_size\_C = sizeof(float) \* size\_C;
| 
|      // allocate host memory for the result
|      float\* h\_C      = (float\*) malloc(mem\_size\_C);
|      float\* h\_CUBLAS = (float\*)
malloc(mem\_size\_C);                                                        
|            checkCudaErrors(cudaMalloc((void\*\*) &d\_A,
mem\_size\_A));                                               
|            checkCudaErrors(cudaMalloc((void\*\*) &d\_B,
mem\_size\_B));                                               
|      // copy host memory to
device                                                                         
|           checkCudaErrors(cudaMemcpy(d\_A, h\_A, mem\_size\_A,
cudaMemcpyHostToDevice) );                           
|           checkCudaErrors(cudaMemcpy(d\_B, h\_B, mem\_size\_B,
cudaMemcpyHostToDevice) );                           
|           checkCudaErrors(cudaMalloc((void\*\*) &d\_C,
mem\_size\_C));                                               
|      // setup execution
parameters                                                                         
|            dim3 threads(block\_size,
block\_size);                                                                 
|            dim3 grid(uiWC / threads.x, uiHC /
threads.y);                                                        
| 
                                                                                                           
|       //Performs warmup operation using matrixMul CUDA
kernel                                               
|      if (block\_size 16) {
|                    matrixMul<16><<< grid, threads >>>(d\_C, d\_A,
d\_B, uiWA, uiWB);                                
|      } else
{                                                                                              
|                   matrixMul<32><<< grid, threads >>>(d\_C, d\_A, d\_B,
uiWA, uiWB);                                
|     
}                                                                                                     

    
cudaDeviceSynchronize();                                                                              

|     // clean up
memory                                                                                    
|     
free(h\_A);                                                                              
|     
free(h\_B);                                                                                            
|      free(h\_C);                      
|   }                 

| **References:**
|  [1] High Performance Computing with CUDA, 2009 User Group Conference
|  [2] http://www.nvidia.com/content/global/global.php

| source code: git clone git@github.com:futuregrid/GPU.git
| 
|  Usage:
|  module load cuda
|  module load intel
|    nvcc -c matrixMul.cu -L/opt/cuda/lib64 -lcudart

+-----------------------------------------------------------------------------------------+-----------+
| Attachment                                                                              | Size      |
+=========================================================================================+===========+
| `matrixMul.zip <https://portal.futuregrid.org/sites/default/files/matrixMul_0.zip>`__   | 3.13 KB   |
+-----------------------------------------------------------------------------------------+-----------+

C-means clustering using CUDA on GPU
====================================

| **Summary:**
|  The computational demands for multivariate clustering are
increasing rapidly, and therefore processing large data sets is
time consuming on a single CPU. To address the computational demands, we
implemented the cmeans clustering algorithm, using the NVIDIA's CUDA's
framework and the latest GPU devices on the Delta machine. 
| 
|  **Fuzzy C-Means Clustering**
|   Fuzzy c-means is an algorithm of clustering which allows one element
to belong to two or more clusters with different probability. This
method is frequently used in multivariate clustering. This algorithm is
based on minimization of the following objective function: |image82|
|  Here, M is a real number greater than 1, N is the number of elements,
Uij is the value of membership of Xi in cluster Cj,  xi is the ith of
d-dimensional measured data, cj is the d-dimension center of the
cluster, and \|\|Xi-Cj\|\| is any norm expressing the similarity between
any measured data and the center.  Fuzzy partitioning is performed
through an iterative optimization of the objective function shown above.
Within each iteration, the algorithm updates the membership uij and the
cluster centers cj by:
|  |image83|       |image84|
|  This iteration will stop when |image85|, where 'e' is a termination
criterion between 0 and 1, and k represents the iteration steps.
|  ****Algorithm of CUDA C-means:**
 1**) Copy data to GPU
|  2) DistanceMatrix kernel
|  3) MembershipMatrix kernel
|  4) UpdateCenters kernel, copy partial centers to host from GPUs
|  5) ClusterSizes kernel, copy cluster sizes to host from each GPU
|  6) Aggregate partial cluster centers and reduce
|  10) Compute difference between current cluster centers and previous
iteration.
|  11) Compute cluster distance and memberships using final centers.
| 
|    **  CUDA kernels of C-means program:**
|  1) DistanceMatrix
|  2) MembershipMatrix
|  3) UpdateCetners
|  4) ClusterSizes
| 
|      **CUDA C-means performance on Delta:**
|  |image86|
|  Figure 1: C-means performance using GPU and CPU
|    Reference:
|    [1]
`http://en.wikipedia.org/wiki/Cluster\_analysis <http://en.wikipedia.org/wiki/Cluster_analysis>`__
|    [2] Scalable Data Clustering using GPU Clusters,  Andrew
Pangborn, Gregor von Laszewski

Average: Select ratingPoorOkayGoodGreatAwesome

Your rating: None Average: 4 (1 vote)

ScaleMP vSMP
============

 

FutureGrid provides a new experimental distributed large memory SMP
machine. 

 

Accessing ScaleMP:
==================

Access of the ScaleMP vSMP machine is managed through the job queueing
system on India. Specifically, you must submit a job to the scalemp
queue on the India cluster. If you haven't already, first log into India
and prepare your environment path:

.. code:: p1

    ssh username@india.futuregrid.org


    module load torque
    module load moab

 

Submitting a job:
-----------------

From here, you are now able to submit to the scalemp queue:

.. code:: p4

    qsub scalemp_job.sh

 

OR run a job interactively 

.. code:: p3

    qsub -I -q scalemp

| 
|   

Developing a job script:
========================

As the ScaleMP vSMP machine is a unique and tool, it requires some
simple but special configuration in order to take full advantage of its
capabilities.  This customization depends on the type of application you
are looking to run, so please consult the configuration type that best
fits your application.

 

MPI:
----

Below is an example script to run a MPI job.  Please note that we
currently only support using MPICH2.  Using OpenMPI and IntelMPI is
possible, however we do not currently support such usage at this time.
 See /opt/ScaleMP/examples/ for more information.

 

.. code:: p9

    # Add path to MPICH2 tuned for vSMP foundation
    export PATH=/opt/ScaleMP/mpich2/1.0.8/bin:$PATH

    # If application binary is MPICH1 and dynamically linked, uncomment this
    # export USE_MPI_WRAPPER=MPICH1

    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so

    # Bind MPI processes on consecutive cores
    # Adding numabind for dynamic placement (according to VSMP_PLACEMENT)
    export PATH=/opt/ScaleMP/numabind/bin:${PATH}

    export VSMP_PLACEMENT=PACKED
    export VSMP_VERBOSE=YES 
    export VSMP_MEM_PIN=YES ulimit -s unlimited


    vsmputil --unpinall 
    time mpirun -np $NPROC ./mpi-app > log-mpi-app-$NPROC.txt

 

OpenMP:
-------

Below is an example script for running your OpenMP code on the scalemp
machine.  See /opt/ScaleMP/examples/OpenMP for more information

.. code:: p8

    # Make sure to use Intel compilers to build the application # Intel compiler runtime environemnt setting 
    source /opt/intel/Compiler/11.1/069/bin/iccvars.sh intel64
    # Setting stacksize to unlimited
    ulimit -s unlimited
    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so

    # Bind OpenMP threads statically to consecutive cpus: last number is the cpu to start from
    export KMP_AFFINITY=compact,verbose,0,0

    # Alternatively you can use dynamic placement using numabind
    # export PATH=/opt/ScaleMP/numabind/bin:${PATH} # export LD_LIBRARY_PATH=/opt/ScaleMP/numabind/lib 
    # The cpu/offset to start from is calculated dynamically by numabind 
    # export KMP_AFFINITY=compact,verbose,0,`numabind --offset $np`

    np=16
    export OMP_NUM_THREADS=$np 
    /usr/bin/time ./openmp-app > log-openmp-app-$np.txt

 

Threaded:
---------

Below is an example script for running a job using Pthreads. See
/opt/ScaleMP/examples/Pthread for more information

.. code:: p9

    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so
    # PATH to numabind, See /opt/ScaleMP/examples/ for more information
    export PATH=/opt/ScaleMP/numabind/bin:$PATH
    # Specify sleep duration for each pthread. Default = 60 sec if not set
    export SLEEP_TIME=120

    # 16 pthreads would be created
    NP=16
    ./ptest $NP > log-pthread-app-$NP 2>&1 &
    # Waiting for 15 seconds for all the threads to start
    sleep 15

    # Start numabind with a config file that has a rule for pthread, 
    # which would place all threads to consecutive cpus. 
    numabind --config myconfig >> log-pthread-app-$NP 2>&1
    wait

 

Throughput:
-----------

Below is an example script to run a throughput job. See
/opt/ScaleMP/examples/ for more information. 

.. code:: p9

    # Setting stacksize to unlimited
    ulimit -s unlimited
    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so

    # Bind the throughput job statically to a particular CPU
    for i in 1 2 3 4; do 
    numactl --physcpubind=$i-1 ./throughput-app $i > log-throughput-app-$i.txt 
    # To bind to a numa node, use numactl –cpunodebind=X 
    done

 Serial:
--------

Below is an example script to run a serial job.  See
/opt/ScaleMP/examples/ for more information. 

.. code:: p7

    # Setting stacksize to unlimited
    ulimit -s unlimited
    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so

    # Bind the serial job statically to a particular CPU using numactl
    cpu=1; numactl --physcpubind=$cpu ./serial-app > log-serial-app-$cpu.txt
    # To bind to a numa node, use numactl –cpunodebind=X # See /opt/ScaleMP/examples/ for more information

 

 

 

IaaS - Infrastructure as a Service
==================================

This chapter contains information in regards to Infrastructure as a
Service offerings on FutureGrid

Using IaaS Clouds on FutureGrid
===============================

| Infrastructure-as-a-Service (IaaS) cloud computing encompasses
techniques that have driven major recent advances in information
technology supporting elastic, on-demand, "pay as you go" computing as a
service. Key technologies behind IaaS cloud computing are resource
virtualization, as well as cloud middleware that enables the management
of clusters of virtualized resources through service interfaces. 
| 
|  The FutureGrid testbed provides capabilities that allow users to
experiment with open-source cloud middleware and virtualization
platforms, and there are different ways you may want to use these
platforms in the testbed. This page guides you in selecting from
FutureGrid capabilities best suited to your goals, and provides links to
respective tutorials:

 Nimbus Clouds
--------------

| Nimbus is an open-source service package that allows users to run
virtual machines on FutureGrid hardware. You can easily upload your own
VM image or customize an image provided by us. When you boot a VM, it is
assigned a public IP address (and/or an optional private address), and
you are authorized to log in as root via SSH. You can then run services,
perform computations, and configure the system as desired.
| 
|  Nimbus is available across various FutureGrid sites, and there are
two open-source hypervisors in use in FutureGrid Nimbus clouds: Xen and
KVM. Nimbus in FutureGrid is the recommended platform if you are
interested in experiments within a cloud, across clouds, or in those not
amenable to para-virtualization, as the Nimbus/KVM cloud (alamo)
supports "classic" virtual machines.
| 
|  For tutorials on getting started with Nimbus, see:

-  `Using Nimbus on
   FutureGrid <https://portal.futuregrid.org/tutorials/nimbus>`__ [novice]
-  `Nimbus One-click Cluster
   Guide <https://portal.futuregrid.org/tutorials/nm2>`__ [intermediate]

OpenStack Clouds
----------------

| `OpenStack <http://www.openstack.org/>`__ is a recently open-sourced,
IaaS cloud computing platform founded by Rackspace Hosting and NASA, and
used widely in industry. It includes three components: Compute(Nova),
Object Storage (Swift), and Image Service (Glance). OpenStack Nova
supports an  Amazon Web Services (AWS) complaint EC2-based web service
interface for interacting with the Cloud service, and can be used with
the same client-side "eucatools" that is used with Eucalyptus.
| 
|  FutureGrid currently features the OpenStack Nova compute cloud. 
OpenStack Nova in FutureGrid is useful if you are interested in
experiments within a cloud, and in comparison of cloud middleware
stacks.
| 
|  For tutorials on getting started with OpenStack, see:

-  `Using OpenStack Nova on
   FutureGrid <https://portal.futuregrid.org/tutorials/openstack>`__ [novice]

   -  This tutorial targets all users of OpenStack in FutureGrid; it
      describes how to get started with FutureGrid OpenStack resources.

-  `Running an OpenStack virtual appliance on
   FutureGrid <https://portal.futuregrid.org/tutorials/os1>`__ [novice]

   -  This tutorial targets users interested in education and training
      on OpenStack internals; it describes how to run a virtual, private
      OpenStack deployment as an appliance.

Eucalyptus Clouds
-----------------

| Eucalyptus is an open-source software platform that implements
IaaS-style cloud computing. Eucalyptus provides an Amazon Web Services
(AWS) complaint EC2-based web service interface for interacting with the
Cloud service. Additionally, Eucalyptus provides services such as the
AWS Complaint Walrus and a user interface for managing users and
images. 
| 
|  Eucalyptus is also available on distributed FutureGrid resources.
Eucalyptus in FutureGrid is useful if  you are interested in experiments
within a cloud, across clouds, and in comparison of cloud middleware
stacks.
| 
|  For tutorials on getting started with Eucalyptus, see:

-  `Using Eucalyptus on
   FutureGrid <https://portal.futuregrid.org/tutorials/eucalyptus3>`__ [novice]

| 

Virtual Appliances for Training and Education
---------------------------------------------

| The IaaS cloud stacks on FutureGrid enable the use of "virtual
appliances" as an environment where hands-on, executable educational and
training modules can be created, shared, and leveraged by the FutureGrid
community. With these appliances, students are able to deploy virtual
machines and virtual private clusters, where they are able to experiment
with various Grid and cloud computing middleware stacks.
| 
|  For tutorials on getting started with educational virtual appliances,
see:
| 

-  `Running a Grid Appliance on your
   desktop <https://portal.futuregrid.org/tutorials/ga1>`__  [novice]
-  `Running a Grid Appliance on
   FutureGrid <https://portal.futuregrid.org/tutorials/ga9>`__ [novice]
-  `Running Condor tasks on the Grid
   Appliance <https://portal.futuregrid.org/tutorials/ga8>`__ [novice]
-  `Running MPI tasks on the Grid
   Appliance <https://portal.futuregrid.org/tutorials/mp1>`__ [novice]
-  `Running Hadoop tasks on the Grid
   Appliance <https://portal.futuregrid.org/tutorials/ga10>`__ [novice]
-  `Running an OpenStack virtual appliance on
   FutureGrid <https://portal.futuregrid.org/tutorials/os1>`__ [novice]

 

Using Nimbus on FutureGrid
==========================

 

 

|image87|
---------

 

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

#. **Hotel** (University of Chicago)
    41 nodes, 328 cores
#. **Foxtrot** (University of Florida)
    26 nodes, 208 cores
#. **Sierra** (San Diego Supercomputer Center)
    18 nodes, 144 cores
#. **Alamo**\ (Texas Advanced Computing Center)
    15 nodes, 120 cores

By default, users are limited to running 16 VMs simultaneously and
claiming two cores per VM. If you have a good reason for this limitation
to be lifted for your account,
contact \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__.

All FutureGrid users are allowed access to Nimbus on all sites.

Getting Started
---------------

Nimbus provides services that can be controlled remotely using a variety
of clients. In this tutorial, we will use a simple command line tool
called the \ **cloud-client**. If you'd rather have programmatic
control, the Amazon EC2 protocols \ `are
supported <http://www.nimbusproject.org/docs/current/elclients.html>`__,
which have a variety of excellent clients available for many
languages.  

Log into hotel
~~~~~~~~~~~~~~

The first step is to ssh into hotel.futuregrid.org.  While you can use
Nimbus clients from anywhere in the world, we recommend that you start
on hotel because the correct version of Java is installed there.

::

    $ ssh -A hotel.futuregrid.org

If this command fails, contact
`https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__. 
It likely means one of the following:

#. Your account is not yet set up.
#. You provide no public key or an corrupted public key.
#. The private key you are using does not match the public one you
   registered with FutureGrid.

Download and install cloud-client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the Nimbus cloud client from the \ `Nimbus
website <http://www.nimbusproject.org/downloads/>`__.

::

    $ wget http://www.nimbusproject.org/downloads/nimbus-cloud-client-021.tar.gz

Unpack the archive onto your system. You can also use one of the
FutureGrid login nodes directly.

::

    $ tar xzf nimbus-cloud-client-021.tar.gz
    $ ls nimbus-cloud-client-021/
    CHANGES.txt README.txt  conf        lib
    LICENSE.txt bin     history     samples
    Obtain your Nimbus credentials and configuration files

Obtain Your Nimbus Credentials and Configuration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your home directory on hotel, you will find the file
nimbus\_creds.tar.gz:

::

     username@hotel $ ls ~/nimbus_creds.tar.gz
    nimbus_creds.tar.gz

If your credentials are not present on \ **Hotel**,
contact \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__.

Back on your system, download and unpack these files into your
cloud-client's directory:

::

    $ cd nimbus-cloud-client-021/conf/ 
    $ tar xvzf ~/nimbus_creds.tar.gz
    usercert.pem
    userkey.pem
    cloud.properties
    hotel.conf
    sierra.conf
    foxtrot.conf
    alamo.conf

Now you should have a functional cloud client. To begin, check out the
help text and file.

::

    $ cd ../

::

    $ bin/cloud-client.sh --help

Check Your ssh Key
~~~~~~~~~~~~~~~~~~

In order to use Nimbus clouds effectively, you need to have your ssh
public key in a known place so that it can be injected into your VM, and
thus allow you (and only you) root access to your VM. When creating your
FutureGrid account you had to upload an ssh public key.  That key can be
found on hotel in the file *~/.ssh/authorized\_keys*.  If you were able
to ssh into hotel then this is the public key are are currently using. 
Nimbus needs this key to be in the\ *~/.ssh/id\_rsa.pub*:

::

    $ cp ~/.ssh/authorized_keys ~/.ssh/id_rsa.pub

Because the security environment can be complicated, cloud-client has an
option to help verify that things are working.  Run the following
command to display some information about your security environment:

::

    $ ./bin/cloud-client.sh --security

Using the Cloud Client
----------------------

Check out the various FutureGrid clouds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| When the credentials file was untarred in a step above, a
configuration file for each of the four FutureGrid clouds was put in
your *conf/*\ directory.  Now let's take a look at accessing each of
those clouds and seeing what virtual machines are available for use.
This will require two options to cloud client.  The first is --conf ;
this is used to select the cloud you wish to use.  Simply provide a path
to the cloud configuration file.  This --conf switch will be used in all
commands to direct cloud-client at the cloud of interest.
| 
|  The second option is --list.  This will simply provide a listing of
all the available virtual machines:

::

    $ bin/cloud-client.sh --conf conf/hotel.conf --list

This command should list the available images on the system.  Notice the
hello-cloud virtual machine.  This is the test image we will use in this
tutorial:

::

    [Image] 'hello-cloud'                    Read only
            Modified: Jan 13 2011 @ 14:15   Size: 576716800 bytes (~550 MB)

Run a Virtual Machine
~~~~~~~~~~~~~~~~~~~~~

| Next, try to boot a virtual machine:

::

    $ bin/cloud-client.sh --conf conf/hotel.conf --run --name hello-cloud --hours 2
    Launching workspace.

::

    Workspace Factory Service:
         https://svc.uc.futuregrid.org:8443/wsrf/services/WorkspaceFactoryService

::

     

::

    Creating workspace "vm-001"... done.

::

           IP address: 149.165.148.253         
             Hostname: vm-253.uc.futuregrid.org       
           Start time: Wed Jul 25 15:44:33 CDT 2012
        Shutdown time: Wed Jul 25 17:44:33 CDT 2012
     Termination time: Wed Jul 25 17:46:33 CDT 2012

::

    Waiting for updates.

::

    "vm-001" reached target state: Running

Once the image is running, you should be able to log into it with SSH.
Note that you may need to wait another minute or so before you can
actually get it, as the system needs time to boot and start services.
Log in as the root user, and connect to the host printed out by the run
command.  Note that you **must**\ run this command in a location that
has access to your private key.  This means it must be in the *~/.ssh/*
directory on the file system from where you launch this command, or you
must have used the -A option to ssh when logging into hotel (as is shown
above).

::

    $ ssh root@vm-253.uc.futuregrid.org

Create a New VM Image
~~~~~~~~~~~~~~~~~~~~~

Once you have a root shell on your VM, you may modify it as through it
were a real machine.  Here we encourage you to make some changes. 
Create a new user, install some additional software, or simply create a
text file in the root user's account:

::

    # touch /root/CHANGE
    # exit

Save the Changes to a New VM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have modified the VM ,you can save it back into your
personal repository.  To do this, you will use the --save and --newname
options.  You will also need the VM handle as it was displayed in the
output from the run command.  If you have forgotten what this was, you
can use the --status option to find it:

::

    $ ./bin/cloud-client.sh --conf conf/hotel.conf --status
    Querying for ALL instances.

    [*] - Workspace #32292. 149.165.148.253 [ vm-253.uc.futuregrid.org ]
          State: Running
          Duration: 120 minutes.
          Start time: Wed Jul 25 15:44:33 CDT 2012
          Shutdown time: Wed Jul 25 17:44:33 CDT 2012
          Termination time: Wed Jul 25 17:46:33 CDT 2012
          *Handle: vm-001
           Image: hello-cloud

Note the handle *vm-001*.  To save the VM for future use, run the
following command:

::

    $ ./bin/cloud-client.sh --conf conf/hotel.conf --save --newname myvm --handle vm-001

    Saving workspace.
      - Workspace handle (EPR): '/N/u/bresnaha/nimbus-cloud-client-021/history/vm-001/vw-epr.xml'
      - New name: 'myvm'

    Waiting for updates.

    The image has successfully been transferred to your repository directory.

    Finalizing the deployment now (terminating the resource lease).

Do another listing of that cloud and you will see your VM is now
available for launch:

::

    $ ./bin/cloud-client.sh --conf conf/hotel.conf --list
    [Image] 'myvm'                           Read/write
            Modified: Jul 25 2012 @ 20:49   Size: 576716800 bytes (~550 MB)

    ----

    [Image] 'hello-cloud'                    Read only
            Modified: Apr 8 2011 @ 13:56   Size: 576716800 bytes (~550 MB)

Launch Your New VM
~~~~~~~~~~~~~~~~~~

| You can now launch your new VM just like you did the hello-cloud VM
above, simply changing the name from *hello-cloud* to *myvm *:

::

    $ ./bin/cloud-client.sh --conf conf/hotel.conf --run --name myvm --hours 2

    Launching workspace.

    Workspace Factory Service:
        https://svc.uc.futuregrid.org:8443/wsrf/services/WorkspaceFactoryService

    Creating workspace "vm-002"... done.


           IP address: 149.165.148.151
             Hostname: vm-151.uc.futuregrid.org
           Start time: Wed Jul 25 15:58:31 CDT 2012
        Shutdown time: Wed Jul 25 17:58:31 CDT 2012
     Termination time: Wed Jul 25 18:08:31 CDT 2012

    Waiting for updates.


    "vm-002" reached target state: Running

    Running: 'vm-002'

SSH into the machine and verify that your changes persisted.

Terminate the VM
~~~~~~~~~~~~~~~~

Your VM will terminate after its allocated time expires.  In our
examples here, this is after 2 hours.  However, you may wish to
terminate it earlier.  You can do so by again using the --handle option
as you did in the *save a new VM step* and the --terminate option:

::

    $ ./bin/cloud-client.sh --conf conf/hotel.conf --terminate --handle vm-002

    Terminating workspace.
      - Workspace handle (EPR): '/N/u/bresnaha/nimbus-cloud-client-021/history/vm-002/vw-epr.xml'

    Destroying vm-002... destroyed.

 

Virtual Clusters
----------------

| This is a basic walkthrough of how to run a sample virtual cluster. 
For more information on how they work, see
*http://www.nimbusproject.org/docs/current/clouds/clusters2.html .*

::


::

Cluster Definition File
~~~~~~~~~~~~~~~~~~~~~~~

For this example, we will use a modification of the sample cluster file
that is distributed with the cloud client.  The file can be found at
*https://portal.futuregrid.org/sites/default/files/tutorial-cluster.xml\_.gz *.
Copy the file to where your cloud-client program is located, and unzip
it.  Open the file and make note of the following:

#. There are 2 workspace definitions. 
#. The head node has a quantity of 1 and a base image
   base-cluster-cc14.gz.  It has the roles of providing a nfs server. 
#. The compute-nodes have the same image, but a quantity of 2.  This
   means there will be 1 head node and 2 compute-nodes in the virtual
   cluster.  This has the role of being a nfs client.

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
      - wrote reports to '/N/u/bresnaha/tutorial/nimbus-cloud-client-021/history/cluster-004/reports-vm'

    Waiting for context broker updates.
      - cluster-004: contextualized
      - wrote ctx summary to '/N/u/bresnaha/tutorial/nimbus-cloud-client-021/history/cluster-004/reports-ctx/CTX-OK.txt'
      - wrote reports to '/N/u/bresnaha/tutorial/nimbus-cloud-client-021/history/cluster-004/reports-ctx'

    SSH trusts new key for vm-40.sdsc.futuregrid.org   head-node 

    SSH trusts new key for vm-41.sdsc.futuregrid.org   compute-nodes #0 

    SSH trusts new key for vm-42.sdsc.futuregrid.org   compute-nodes #1 

| This command takes a bit of time.  What is happening is cloud-client
is instructing Nimbus to start up three VMs on the user's behalf. 
Information is put into the context broker.  When each VM boots, the
context agent is run.  The context agent checks in with the context
broker and asks for information reflecting the *requires* section in the
cluster document; similarly it registers its *provides* information with
the context broker for other VM context agents to query.  The NFS
clients use this mechanism to provide the nfs server with their IP
addresses.  The NFS server then gets this information out of the context
broker and uses it to authorize those IP addresses to remotely mount its
disks. 
| 
|  When it is complete, your virtual cluster will be ready to go.

Check Out the Virtual Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Now ssh into one of the worker nodes and check out the file system.

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

| Notice the NFS mounted home directory.  Touch a file in that
directory.

::

    $ echo "Hello FutureGrid" > /home/test_file

| Now ssh into the other worker node and verify that the test file is
visible to this node as well.

::

    $cat /home/test_file
    Hello FutureGrid

| 
| 
| 

+--------------------------------------------------------------------------------------------------------------+-------------+
| Attachment                                                                                                   | Size        |
+==============================================================================================================+=============+
| `tutorial-cluster.xml\_.gz <https://portal.futuregrid.org/sites/default/files/tutorial-cluster.xml_.gz>`__   | 342 bytes   |
+--------------------------------------------------------------------------------------------------------------+-------------+

Cloud Quick Start : Launch a VM with 1 command
==============================================

This page explains how to very simply run a virtual machine (VM) on
FutureGrid Nimbus.  The VM launched will mount your home files system on
hotel so data can be exchanged with the VM easily.  Users new to cloud
computing, particularly those coming from Grid computing, and those who
are interested in getting a quick hands-on introduction to FutureGrid
clouds, should find this useful.

Launch A VM via Nimbus
======================

| Once you have a FutureGrid Nimbus account and ssh access to
hotel.futuregrid.org, you can easily begin using the cloud.  All you
need to do is ssh into hotel with ssh forwarding enabled, and type a
single command:
| 

::

    $ ssh -A hotel.futuregrid.org
    $ /soft/nimbus/tools/bin/launch-vm.sh
    Launching your VM (this may take a minute)...
    Success!
    Access your VM with: ssh root@vm-156.uc.futuregrid.org
    Terminate your VM with: /soft/nimbus/tools/bin/cloudinitd.sh terminate 9ec20044

| Notice the output from the above command.  It tells you how to access
the VM, and how to clean it up when you are finished with it.  First
let's access the VM and check out its file system.  The VM should have
remotely mounted your home file system on FutureGrid.  This will allow
you to easily copy data in and out of your VM.

::

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

| By default, the VMs are launched on hotel's Nimbus cloud.  However,
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
   (coming soon)
-  Alamo:
   `https://master1.futuregrid.tacc.utexas.edu:8444 <https://master1.futuregrid.tacc.utexas.edu:8444>`__
   (coming soon)

Launching Multiple VMs
----------------------

| To launch many VMs at once, set the env
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
     

| You may have trouble registering your keys.  This is due to Eucalyptus
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

FutureGrid Tutorial NM2 - Nimbus One-Click Cluster Guide
========================================================

 

**Summary:**

This tutorial demonstrates using the Nimbus cloud client to create
auto-configured clusters of virtual machines on Nimbus.

 

**Prerequisites:**

Java 1.5+ and a working Nimbus cloud client.

 

**Hands-On Tutorial**:

This tutorial is maintained at the Nimbus website. See \ `One Click
Clusters <http://www.nimbusproject.org/docs/current/clouds/clusters.html>`__.

 

**Reference Material:**

`Nimbus Documentation <http://www.nimbusproject.org/docs/>`__

 

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

| Users get access to the Eucalyptus features using the Eucalyptus EC2
Interface, which is only available for GNU/Linux platforms. Therefore,
users will require a machine with a GNU/Linux installed on it.
|   

Eucalyptus 3
''''''''''''

| As of May 15, 2012, FutureGrid is using `Eucalyptus version
3 <http://www.eucalyptus.com/eucalyptus-cloud/iaas/features>`__ which
requires `euca2ools
2.0.2 <http://www.eucalyptus.com/download/euca2ools>`__ and python > 2.4
(available by modules in india and sierra). Make sure to load **"module
load euca2ools/2.0.2"** before using Eucalyptus. `euca2ools
2.0.2 <http://www.eucalyptus.com/download/euca2ools>`__ is part of
Eucalyptus Enterprise package. However, the source is available
`here <http://bazaar.launchpad.net/~eucalyptus-maintainers/euca2ools/euca2ools-main/revision/>`__.
|   

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
   *username@fgnumber *.)

| NOTICE: Due to an incompatibility problem introduced during the
upgrade to the Eucalyptus 3.1 system, accessing the dashboard of
Eucalyptus on india is tempararily unavailable. However, your credential
will be in place so you can execute the later steps of this manual.
|  On Sierra, the access is still available so you could download the
credential zip file. Make sure to put it to Sierra first and then set up
the environment as the following steps.
|  Please be reminded that the credential for one cluster should/could
not be used in another.
|   

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

INDIA: 
^^^^^^^

::

    AVAILABILITYZONE    euca3india    149.165.146.135 arn:euca:eucalyptus:euca3india:cluster:euca3indiaCC/
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

    | $ euca-authorize -P tcp -p 22 -s 0.0.0.0/0   default
    |  $ euca-authorize -P icmp -t -1:-1 -s 0.0.0.0/0 default

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
   shows the new image now:

    ::

        $ euca-describe-images 

        IMAGE emi-FFC3154F   ubuntu-image-bucket/precise-server-cloudimg-amd64.img.manifest.xml archit available public   x86_64 machine eri-5BB61255 eki-78EF12D2 
        IMAGE emi-0B951139   centos53/centos.5-3.x86-64.img.manifest.xml           admin  available public   x86_64 machine 
          ...

-  You can also delete your images:

.. code:: rteindent1

    $ euca-deregister emi-FFC3154F

Status of Deployments
---------------------

At times, you may ask if the Eucalyptus systems on FutureGrid are
operational. You can find this out by visiting the following:

| a) The Outage page
at \ `https://portal.futuregrid.org/metrics/html/results/realtime.html#total-count-of-running-vm-instances-updated-every-5-seconds <https://portal.futuregrid.org/metrics/html/results/realtime.html#total-count-of-running-vm-instances-updated-every-5-seconds>`__
|  b) The Real Time Status monitor
at \ `http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid <http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid>`__
|  c) Our Runtime History
at \ `http://inca.futuregrid.org:8080/inca/jsp/report.jsp?xml=cloudReport.xml <http://inca.futuregrid.org:8080/inca/jsp/report.jsp?xml=cloudReport.xml>`__

Using OpenStack on FutureGrid
=============================

NOTE: 
======

-  **This tutorial contains material that is customized for the
   particular user. The best way to view this tutorial is to  ask for a
   FutureGrid portal account and to log into the portal. You will also
   need to be in a valid FG project to execute the directions.**

Summary
=======

We currently have twenty nodes in the FG India cluster dedicated to the
`Essex <http://www.openstack.org/software/essex/>`__ release of
`OpenStack <http://www.openstack.org>`__, a collection of open-source
technology that provides scalable, open-source cloud computing software.
OpenStack consists of a series of `interrelated
projects <http://www.openstack.org/software/>`__ that deliver various
components for a cloud infrastructure solution. This tutorial provides
an overview of OpenStack Nova installation on FutureGrid, as well as
steps for deploying virtual machines.

Getting Started
===============

Be sure you have a valid portal account
(`https://portal.futuregrid.org) <https://portal.futuregrid.org>`__ and
are part of a valid FG project. If you're not part of any project, you
can either create a new one (it will need approval) or join an existing
one with the permission of the Lead.

Once the previous requirements are fulfilled, your OpenStack account is
automatically created.

Log into India
==============

+-------------------------------------------------------------------------------------------------------------------------+
|  Tip: to login into FutureGrid \ `see this page <https://portal.futuregrid.org/accessing-futuregrid-resources-ssh>`__   |
+-------------------------------------------------------------------------------------------------------------------------+

The first step is to ssh into india.futuregrid.org using your FG
username:

.. code:: rteindent1

    $ ssh gvonlasz@india.futuregrid.org

If this command fails,
contact \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__. 
It likely means one of the following:

#. Your account is not yet set up.

#. You provided no public key, or a corrupted public key.

#. The private key you are using does not match the public key you
   registered with FutureGrid.

Account and Credentials
=======================

As noted above, OpenStack credentials and configuration files are
automatically created for all valid users, and are placed in your home
directory on the India system under the ***.futuregrid/openstack***
folder. The file name is called
***openstack-essex-<username>-india.zip***. The credential .zip file
contains the user keys and novarc file. The novarc file contains the
necessary environment variables.

Unzip the credential file:

.. code:: rteindent1

    $ unzip ~/.futuregrid/openstack/openstack-essex-gvonlasz-india.zip -d ~/openstack

Load Environment variables:

.. code:: rteindent1

    $ source ~/openstack/novarc

**Note:** As both Eucalyptus and OpenStack use the same EC2
environmental variables (i.e. EC2\_URL, EC2\_ACCESS), using novarc will
overwrite previous Eucalyptus credentials. If you have the eucarc file
in your home directory, doing a *source eucarc* will bring back those
variables and overwrite the OpenStack ones. In this way, you can go back
and forth with OpenStack and Eucalyptus.

Euca2ools (EC2 client tools)
============================

OpenStack services can be controlled using an EC2 interface (only
available for GNU/Linux platforms). In this tutorial, we are going to
use the \ `Euca2ools <http://www.eucalyptus.com/download/euca2ools>`__
client installed in India.

.. code:: rteindent1

    $ module load euca2ools

Testing Your Setup
==================

Use euca-describe-availability-zones to test the setup:

.. code:: rteindent1

    $ euca-describe-availability-zones 

    AVAILABILITYZONE    india   available

List of Common Images
=====================

Following are the current images uploaded in essex:

.. code:: rteindent1

    $ euca-describe-images |grep common

    IMAGE   ami-000000b4   common/precise-server-cloudimg-amd64.img.manifest.xml   available   private   x86_64   machine   aki-000000b3   instance-store

VM Types
========

The following types of VM are available:

$ nova flavor-list

| +----+-------------+-----------+------+-----------+------+-------+-------------+-----------+-------------+
|  \| ID \| Name        \| Memory\_MB \| Disk \| Ephemeral \| Swap \|
VCPUs \| RXTX\_Factor \| Is\_Public \| extra\_specs \|
| 
+----+-------------+-----------+------+-----------+------+-------+-------------+-----------+-------------+
|  \| 1  \| m1.tiny     \| 512       \| 0    \| 0         \|      \|
1     \| 1.0         \| N/A       \| {}          \|
|  \| 2  \| m1.small    \| 2048      \| 10   \| 20        \|      \|
1     \| 1.0         \| N/A       \| {}          \|
|  \| 3  \| m1.medium   \| 4096      \| 10   \| 40        \|      \|
2     \| 1.0         \| N/A       \| {}          \|
|  \| 4  \| m1.large    \| 8192      \| 10   \| 80        \|      \|
4     \| 1.0         \| N/A       \| {}          \|
|  \| 5  \| m1.xlarge   \| 16384     \| 10   \| 160       \|      \|
8     \| 1.0         \| N/A       \| {}          \|
|  \| 6  \| m1.special1 \| 16384     \| 50   \| 1500      \|      \|
8     \| 1.0         \| N/A       \| {}          \|
| 
+----+-------------+-----------+------+-----------+------+-------+-------------+-----------+-------------+

Key Management
==============

Before you instantiate a VM, you need to create at least one key pair.
This key pair will be injected into the VM, allowing you to SSH into the
instance. This is done using the *euca-add-keypair* command:

.. code:: rteindent1

    $ euca-add-keypair gvonlaszkey1 > gvonlaszkey1.pem

**Important Tip: **\ In case you execute this command twice this will
naturally not work in case the key is already added and imported. You
can check this by doing a cat on the .pem file and make sure that there
is a key in ther and not an error! If there is an error, you can either
delete the key and add it again, or you can create a new key name and
use that. Also if you have used that key before and you overwrote it you
will not have access to your images anymore. so be careful and before
issuing the above command think about what you do.

Fix the permissions on the generated private key:

.. code:: rteindent1

    $ chmod 0600 gvonlaszkey1.pem

Note: Instead of creating a new keypair, you can import a public key
created with a third-party tool using *euca-import-keypair*. For
instance, if you have your ssh public key in india, you can do the
following:

.. code:: rteindent1

    $ euca-import-keypair -f .ssh/id_rsa.pub gvonlaszkey2

You can add multiple keys, and here's the command to check the list of
your keys:

.. code:: rteindent1

    $ chmod 0600 keyname.pem
    euca-describe-keypairs
    KEYPAIR    key1    53:e3:01:c1:70:df:94:ef:59:93:1a:3f:c0:10:a5:34
    KEYPAIR    key2    07:a5:da:30:b4:55:16:eb:35:54:a2:5a:56:68:f6:cb

::

Key pair verification
---------------------

Please verify that you do not have any error in the key file.

Image Instantiation
===================

At this point, you can start a VM using one of the pre-existing images.
You need the ami-id of the image you want to start. This was listed in
the output of the *euca-describe-images* command you saw earlier. Use
the *euca-run-instances* command to start the VM (use the key name you
specified before).

.. code:: rteindent1

    $ euca-run-instances -k gvonlaszkey -n 1 ami-000000b4

    RESERVATION r-gbs9hpmm 461884eef90047fbb4eb9ec92f22a1e3 default
    INSTANCE i-00000a27 ami-000000b4 server-2599 server-2599 pending gvonlaszkey 0 m1.small 2012-07-31T14:54:40.000Z unknown zone

The output shows the id of your VM, which in this case is i-00000a27.

This id will be useful to do operations with your VM. You can also see
the status of your VM, which is pending now. You need to wait until the
VM is in running status to be able to log into the VM.

Better Server Names
===================

Unfortunately, the default use of the euca commands uses the name
server-<number> to identify a started instance. This is often not
desirable, as many users have similar names and it will be difficult to
find your own images when lots of users start images. To fix this, you
van however use the nova commands and say

$ nova rename Server-2599 <yourusername>-001

Monitoring Instances
====================

You can monitor the status of the instances by using the
*euca-describe-instances* command. The public IP is highligthed in
yellow; each VM should have one:

.. code:: rteindent1

    $ euca-describe-instances

.. code:: rteindent1

    RESERVATION r-xfj0nag8 461884eef90047fbb4eb9ec92f22a1e3 default
    INSTANCE i-0000090e ami-00000016 149.165.158.157 server-2318 running clegoues 0 m1.medium 2012-07-24T19:39:21.000Z india aki-00000014 ari-00000015

    RESERVATION r-8mwsq0n0 461884eef90047fbb4eb9ec92f22a1e3 default
    INSTANCE i-000008f2 ami-000000b4 149.165.158.130 server-2290 running clegoues 0 m1.medium 2012-07-24T02:19:38.000Z india aki-00000014 ari-00000015
    INSTANCE i-000008f3 ami-000000b4 149.165.158.149 server-2291 running clegoues 1 m1.medium 2012-07-24T02:19:38.000Z india aki-00000014 ari-00000015
    INSTANCE i-000008f4 ami-000000b4 149.165.158.156 server-2292 running clegoues 2 m1.medium 2012-07-24T02:19:39.000Z india aki-00000014 ari-00000015

    RESERVATION r-p90m3pno 461884eef90047fbb4eb9ec92f22a1e3 default
    INSTANCE i-000007e2 ami-000000b4 149.165.158.158 server-2018 running jiaazeng 0 m1.medium 2012-07-15T20:56:16.000Z india aki-00000026 
    INSTANCE i-000007e3 ami-000000b4 149.165.158.159 server-2019 running jiaazeng 1 m1.medium 2012-07-15T20:56:17.000Z india aki-00000026
    ...

You can monitor or restrict the output simply by checking the status of
your VM:

.. code:: rteindent1

    $ euca-describe-instances i-00000a27

    RESERVATION r-zvtbbj8j default
    INSTANCE i-00000a27 ami-000000b4 server-1854 server-1854 pending gvonlaszkey 0 m1.small 2012-07-09T15:49:46.000Z  unknown zone aki-0000000e ari-0000000f

This VM does not have public IP yet. Getting the public IP may take some
time, but it is needed to be able to connect to the VM:

.. code:: rteindent1

    $ euca-describe-instances i-00000a27

    RESERVATION r-zvtbbj8j default
    INSTANCE i-00000a27 ami-000000b4 149.165.158.175 server-1854 running gvonlaszkey 0 m1.small 2012-07-09T15:49:46.000Z  unknown zone aki-0000000e ari-0000000f

Log into your VM
================

The ssh private key that was generated earlier can now be used to log in
to the VM. You also need to indicate the public IP associated with your
VM (use the key name you have specified before).

.. code:: rteindent1

    $ ssh -i gvonlaszkey.pem ubuntu@149.165.158.175

    $ ssh ubuntu@149.165.158.175 (for imported keys) 

Note: For some ubuntu images, log in with the user *ubuntu,* then
*sudo*.

Exit from the VM to continue with the tutorial.

.. code:: rteindent1

    # exit

Making a snapshot with nova client
----------------------------------

You can make a snapshot of your instance:

.. code:: rteindent1

    $ nova image-create <instance name> <snapshot name>
    $ euca-describe-images

Your snapshot will be listed at the end of the output, and it will be
available in 5 to 10 minutes. There's a bug that snapshots are created
as "snapshot" whatever you name it. So please remember the image ID.

Nova Volumes (Not available)
============================

Nova-volume provides persistent block storage compatible with Amazon’s
Elastic Block Store. The storage in the instances is non-persistent and
gets lost when the instance is terminated. Therefore, we need persistent
volumes to keep data generated during instance lifetime after the
instance is terminated. Volumes are accessed via iSCSI, although they
will appear as a new device in your VM.

List available Volumes
----------------------

You can see the available volumes by using the *euca-describe-volumes*
command:

.. code:: rteindent1

    $  euca-describe-volumes

    VOLUME  vol-00000027  100  india  in-use  2012-06-06T21:39:47.000Z
               ATTACHMENT  vol-00000027  i-0000070f  /dev/vdc  attached 
    VOLUME  vol-00000028  50  india  available  2012-06-06T21:44:30.000Z
    VOLUME  vol-0000002a  30  india  available  2012-06-06T21:45:37.000Z

Create a Volume
---------------

Create a 1 GB volume in the India zone:

.. code:: rteindent1

    $  euca-create-volume -s 1 -z india

    VOLUME  vol-00000031  1  india  creating  2012-07-10T15:15:47.244Z

Attach Volume
-------------

A volume can only be attached to one instance. Once the volume is
attached to a VM, *euca-describe-volumes* will show its status as
“attached”. 

Attach a volume to a running instance:

.. code:: rteindent1

    $  euca-attach-volume -i i-00000a27 -d /dev/vdc vol-0000031

After this command is executed, an additional SCSI disk is created in
the instance. Although we specified the device, it may differ if that
device already exists (look into */dev* or */var/log/syslog* to find the
new device).

Using the new Disk
------------------

Log into the VM again (use the key name you specified before):

.. code:: rteindent1

    $ ssh -i gvonlaszkey.pem ubuntu@149.165.158.175

Format the disk (skip this step if you want to reuse data stored):

.. code:: rteindent1

    # mkfs /dev/vdc

Mount the disk:

.. code:: rteindent1

    # mount /dev/vdc /mnt

You now have the new disk mounted in your system. In this way, you can
use it as a normal directory to store information. However, the
information stored there will be kept after you terminate the VM.

Exit from the VM to continue with the tutorial:

.. code:: rteindent1

    # exit

Detach Volumes
--------------

Volumes are automatically detached when the instance is terminated.

To detach a volume:

.. code:: rteindent1

    $  euca-detach-volume vol-00000031 

If you detach the volume while the instance is running, and with disk
mounted, it loses access to the disk. Thus, you need to make sure that
you umount (umount /mnt) the disk before you detach the volume. If you
terminate the instance, the volume is automatically detached.

Volume Snapshots
================

Snapshots are useful to create backups or replicate volumes in different
zones.

Create Snapshot
---------------

.. code:: rteindent1

    $  euca-create-snapshot -d 'Testing snapshot' vol-00000027

    SNAPSHOT    snap-00000001    vol-00000027    creating    2012-07-16T14:22:21.728Z    0%    Testing snapshot

List Snapshot
-------------

.. code:: rteindent1

    $  euca-describe-snapshots

    SNAPSHOT    snap-00000001    vol-00000027    available    2012-07-16T14:22:21.000Z    100%

Create Volume from Snapshot (not yet functional in OpenStack Essex)
-------------------------------------------------------------------

The snapshot must be in available status (100% completed). The new
volume can be bigger if desired, and you can also create this volume in
a different zone (*-z* option).

To create a 2 GB volume from snapshot:

.. code:: rteindent1

    $  euca-create-volume -s 2 --snapshot snap-00000001 -z india

    VOLUME    vol-00000032    2    snap-00000001    india    creating    2012-07-16T14:47:07.916Z

Image Registration
==================

We will use an CentOS 5 image to test the image registration:

.. code:: rteindent1

    $ wget i120/test-image/centos5.tgz

Uncompress and untar the archive:

.. code:: rteindent1

    $ tar xvfz centos5.tgz

Bundle the image with a kernel and a ramdisk using the
*euca-bundle-image* command. In this example, we will use the KVM kernel
already registered. *euca-describe-images* returns the kernel and
ramdisk IDs that we need.

.. code:: rteindent1

    $ euca-bundle-image -i centos5.img --kernel aki-0000000e --ramdisk ari-0000000f

.. code:: rteindent1

    Checking image
    Encrypting image
    Splitting image...
    Part: centos5.img.part.00
    ...
    Part: centos5.img.part.35
    Generating manifest /tmp/centos5.img.manifest.xml

Use the generated manifest file to upload the image. You need to specify
a bucket name; it can be anything you want:

.. code:: rteindent1

    $ euca-upload-bundle -b gvonlasz-bucket -m /tmp/centos5.img.manifest.xml

    Checking bucket: gvonlasz-bucket
    Creating bucket: gvonlasz-bucket
    Uploading manifest file
    Uploading part: centos5.img.part.00
    ...
    Uploading part: centos5.img.part.35

    Uploaded image as gvonlasz-bucket/centos5.img.manifest.xml

Register the upload image:

.. code:: rteindent1

    $ euca-register gvonlasz-bucket/centos5.img.manifest.xml

    IMAGE  ami-00000033

The returned image ID can now be used to start instances
with\ *euca-run-instances* as described earlier. However, you cannot run
instances until the image is in available status. You can check the
status using \ *euca-describe-images*:

.. code:: rteindent1

    $ euca-describe-instances ami00000033 IMAGE ami-00000033 gvonlasz-bucket/centos5.img.manifest.xml available private x86_64 machine aki-0000000e ari-0000000f instance-store

Delete your images
==================

.. code:: rteindent1

    $ euca-deregister ami-00000033

Terminate your VMs
==================

.. code:: rteindent1

    $ euca-terminate-instances i-00000a27

Limitations
===========

Our current installation has the following limitations. We are working
on finding a fix:

#. Instances cannot ping their own IP address from within the instance
   (it is pingable and reachable from the outside). The private IP
   (which can be found via ifconfig) is pingable.

   | ubuntu@server-837:~$ ifconfig
   |  eth0      Link encap:Ethernet  HWaddr fa:16:3e:00:e5:2a 
   |            inet addr:10.1.2.16  Bcast:10.1.2.255 
   Mask:255.255.255.0
   |            inet6 addr: fe80::f816:3eff:fe00:e52a/64 Scope:Link
   |            UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
   |            RX packets:199 errors:0 dropped:0 overruns:0 frame:0
   |            TX packets:188 errors:0 dropped:0 overruns:0 carrier:0
   |            collisions:0 txqueuelen:1000
   |            RX bytes:32213 (32.2 KB)  TX bytes:21676 (21.6 KB)

   | lo        Link encap:Local Loopback 
   |            inet addr:127.0.0.1  Mask:255.0.0.0
   |            inet6 addr: ::1/128 Scope:Host
   |            UP LOOPBACK RUNNING  MTU:16436  Metric:1
   |            RX packets:0 errors:0 dropped:0 overruns:0 frame:0
   |            TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
   |            collisions:0 txqueuelen:0
   |            RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

#. In Essex, each instance gets an internal DNS name.
   *euca-describe-instance* will show this name along with the public IP
   addresses. If you are building a cluster and need to communicate
   among all the nodes in the cluster, you will need to do so with these
   names or the private IP addresses:

   | ubuntu@server-837:~$ ping server-716
   |  PING server-716.novalocal (10.1.2.10) 56(84) bytes of data.
   |  64 bytes from server-716.novalocal (10.1.2.10): icmp\_req=1 ttl=64
   time=5.06 ms
   |  ^C
   |  --- server-716.novalocal ping statistics ---
   |  1 packets transmitted, 1 received, 0% packet loss, time 0ms
   |  rtt min/avg/max/mdev = 5.062/5.062/5.062/0.000 ms
   |  ubuntu@server-837:~$ ping server-837
   |  PING server-837.novalocal (127.0.1.1) 56(84) bytes of data.
   |  64 bytes from server-837.novalocal (127.0.1.1): icmp\_req=1 ttl=64
   time=0.032 ms
   |  64 bytes from server-837.novalocal (127.0.1.1): icmp\_req=2 ttl=64
   time=0.018 ms

Troubleshooting:
================

Console output will provide you more details about the VM:

.. code:: rteindent1

    $ euca-get-console-output <instanceId>

For any other issue, please submit a ticket.

 

style="font-size: small;"> 

Image Management and Rain on FutureGrid
=======================================

`FutureGrid <https://portal.futuregrid.org/kb/document/ayzv>`__ image
management defines the full lifecycle of the images in FutureGrid. It
involves the process of creating, customizing, storing, sharing, and
deploying images for different FutureGrid environments. For information
and instructions on managing your images in FutureGrid, and the Rain
environment, see 

-  `http://futuregrid.github.com/rain <http://futuregrid.github.com/rain/quickstart.html>`__ and
     
-  `http://futuregrid.github.com/rain/quickstart.html <http://futuregrid.github.com/rain/quickstart.html>`__

+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| `**RAIN Documentation:** <http://futuregrid.github.com/rain/quickstart.html>`__   | `**RAIN Quickstart:** <http://futuregrid.github.com/rain/quickstart.html>`__   |
+===================================================================================+================================================================================+
| |image91|                                                                         | |image92|                                                                      |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

`  <http://futuregrid.github.com/rain/quickstart.html>`__

Generate and Register an OS Image on FutureGrid using the FG Shell
==================================================================

Summary
-------

| Below, we summarize the different steps needed to create a new image
and register it in a FutureGrid infrastructure. In this case, we will
register the image in OpenStack, but it can be registered in any other
FutureGrid infrastructure, such as Eucalyptus, Nimbus, or HPC. Detailed
information about these tools can be found
in \ `http://futuregrid.github.com/rain/ <http://futuregrid.github.com/rain/>`__.

Request access
--------------

| Submit a ticket to request
access \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__
| 
|  Please use the subject: "Request to access FutureGrid Rain". Include
in the body "I would like to obtain access to FutureGrid Rain".

| *Note: In future we may just create a checkbox for this request in the
help form.*
|   

Once you have access, you can continue the tutorial. Typically, it will
take a business day for you to get added (a business day is 9am-5pm EST
Mon-Fri). 

Log into India
--------------

.. code:: rteindent1

    $ ssh <username>@india.futuregrid.org
    $ module load futuregrid

Start the Shell
---------------

Execute the FG Shell. Please remember to replace <username> with your
portal user name. Then, you will be asked for a password (which is your
portal password):

.. code:: rteindent1

    $ fg-shell -u <username>

This command will change your shell and the prompt will be fg-rain>. If
your prompt is different, you need to execute "use rain".

Generate the Image
------------------

| We are going to generate an Ubuntu 12.04 image. The -s parameter
allows you to specify the software you want to install in your image.
Currently, only the software available in the official repositories can
be installed.

.. code:: rteindent1

    fg-rain> generate -o ubuntu -v 12.04 -a x86_64 -s wget, openmpi-bin

| After a while, your image will be stored in the repository, and your
image ID will be printed.

Image Repository
----------------

We can consult the information of the image by executing the following
(please replace <imageid> with the ID that you got from the previous
command):

.. code:: rteindent1

    fg-rain> list * where imgId=<imageId>

Register Image
--------------

Next, we need to register that image in the infrastructure we want to
use. In this case, we will register the image in OpenStack (if you
followed the FG Openstack tutorial, your novarc will probably be in
~/openstack/novarc). This command will return an <ami-ID>, which is the
ID of the image in OpenStack.

.. code:: rteindent1

    fg-rain> register -r <imageId> -s india -v ~/novarc

Once you have registered the image, you need to wait until it becames
available. To check the status of the image, you can execute the
following command.

.. code:: rteindent1

    fg-rain> cloudlist -s india -v ~/novarc | grep <imageId>

| The status is the second field. You may experience that this command
takes time to respond when the image is being uploaded (it is an
OpenStack issue).

Start Image
-----------

| Once the image is in "available" status, we can proceed to start a VM
using the ami-ID that we got from the register command. In this case, we
are going in Interative mode, which means that we are going to get
logged into the VM once it is running.

.. code:: rteindent1

    fg-rain> launch -i <ami-ID> -s india -v ~/novarc -I

| 
| 
| 
| 

FutureGrid Standalone Image Repository
======================================

Introduction
------------

| The FutureGrid image repository is a standalone service that is not
tied to FutureGrid nor to any IaaS infrastructure. This image repository
offers a common interface that can distinguish image types for different
IaaS frameworks like Nimbus, Eucalyptus, and also bare-metal images.
This allows us in FG to include a diverse image set not only contributed
by the FG development team, but also by the user community that
generates such images and wishes to share them. The images can be
described with information about the software stack that is installed on
them including versions, libraries, and available services. This
information is maintained in the catalog and can be searched by users
and/or other FutureGrid services. Users looking for a specific image can
discover available images ﬁtting their needs, and ﬁnd their location in
the repository by using the catalog interface.
| 
|  The repository supports different storage systems that allow you to
choose the most appropriate one for you. It includes MySQL, where the
image ﬁles are stored directly in the POSIX ﬁle system; MongoDB, where
both data and ﬁles are stored in the NoSQL database; the OpenStack
Object Store (Swift); and Cumulus from the Nimbus project. For the last
two cases, the data can be stored in either MySQL or in MongoDB. These
storage plugins not only increase the interoperability of the image
repository, but can also be used by the community as templates to create
their own plugins to support other storage systems.

Requirement
-----------

-  Python 2.6 or 2.7
-  LDAP server for user authentication

Software
--------

| The software is open-source under an Apache 2 license. The image
repository can be found in github as part of our Image Management and
Rain
software \ `https://github.com/futuregrid/rain <https://github.com/futuregrid/rain>`__ .

Documentation
-------------

| The documentation can be found
in \ `http://futuregrid.github.com/rain/index.html <http://futuregrid.github.com/rain/index.html>`__.
Since this link provides information about all our tools, in this
section we collect the links that refer to the image repository.

User Manual
~~~~~~~~~~~

Information about the command-line interface is found
in \ `http://futuregrid.github.com/rain/man-repo.html <http://futuregrid.github.com/rain/man-repo.html>`__.
If you are interested on using the shell, the manual is
in \ `http://futuregrid.github.com/rain/man-shell.html <http://futuregrid.github.com/rain/man-shell.html>`__.

Installation
~~~~~~~~~~~~

| You need to install the complete software, even if you only want to
use the image repository. This information is found
in \ `http://futuregrid.github.com/rain/install.html <http://futuregrid.github.com/rain/install.html>`__.

Configuration
~~~~~~~~~~~~~

The configuration information can be found
in \ `http://futuregrid.github.com/rain/configure\_futuregrid.html <http://futuregrid.github.com/rain/configure_futuregrid.html>`__.
You will be interested in:

-  Configuration
   files \ `http://futuregrid.github.com/rain/configure\_futuregrid.html#configuration-files <http://futuregrid.github.com/rain/configure_futuregrid.html#configuration-files>`__
-  Setting up LDAP
   information \ `http://futuregrid.github.com/rain/configure\_futuregrid.html#setting-up-ldap <http://futuregrid.github.com/rain/configure_futuregrid.html#setting-up-ldap>`__
-  Setting up the Image
   Repository \ `http://futuregrid.github.com/rain/configure\_futuregrid.html#setting-up-the-image-repository <http://futuregrid.github.com/rain/configure_futuregrid.html#setting-up-the-image-repository>`__

Manual Image Customization
==========================

| Sometimes users need to further customize their images by installing
their own software—software which may not be able to be installed with
the image generation tool. In this tutorial, we explain how users can
perform this customization in the images created with the FG image
generation tool. Detailed information about FG image management tools
can be found in
`http://futuregrid.github.com/rain/ <http://futuregrid.github.com/rain/>`__.

Logging into India
------------------

::

    $ ssh <username>@india.futuregrid.org 
    $ module load futuregrid

 
-

Requesting access
-----------------

Submit a ticket to request
access \ `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__

Obtaining the image
-------------------

You can get your image from our repository, or generate a new one.

Getting an image from the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ fg-repo -u <username> -g <imageId>

Generating a new image
~~~~~~~~~~~~~~~~~~~~~~

We are going to generate an Ubuntu image. Since we want to modify the
image, we have specified the -g parameter to retrieve the image after it
is generated. By default, it is uploaded to the image repository.

::

    $ fg-generate -u jdiaz -o ubuntu -v 12.04 -a x86_64 -s wget, openmpi-bin -g

In both cases, we will obtain a tgz file that contains the image file
(.img) and a manifest (.manifest.xml). For example, our image could be
in */N/u/<username>/123123123.tgz* .

Customizing the image
---------------------

| To continue with the rest of the tutorial, we need a UNIX machine
where we have root privileges.
| 
|  Assuming that we are in a UNIX machine with root privileges:
| 
|  1. Retrieve the image from India:

::

    $ scp <username>@india.futuregrid.org:/N/u/<username/123123123.tgz .

| 2. Decompress the image:

::

    $ tar vxfz 123123123.tgz

    jdiaz859434.img
    jdiaz859434.manifest.xml

| 3. Mount the image. This will mount the image file into a directory.
In this way, we will have access to the OS files that are inside the
image.

::

    $ mkdir image
    $ sudo mount -o loop jdiaz859434.img image

| Copy your software into the image directory (if needed). In this case,
I am going to copy a software directory to the tmp directory of the
image:

::

    $ cp -r /home/javi/mysoftware image/tmp

| *Chroot* into the image. This changes the root of the OS to the one of
the image. In this way, evey operation we execute will have effect only
inside the image. After executing this command, you will be the root
users inside the image.

::

    $ sudo chroot image

| Now you can install whatever software you need. You can also use
*yum/apt* to install packages from the software repository. Remember
that they will be installed inside the image. As example, here I install
tomcat with *apt* and compile my software with *make*:

::

    # apt-get install tomcat6
    # cd /tmp/mysoftware
    # make && make install

| You can also configure the OS of image to start services during the
boot time. The easiest way to do that is by modifying
the\ */etc/rc.local*\ file.
| 
|  Once you have finished customizing your image, you need to exit from
the *chroot* command, unmount the image, and compress it again:

::

    # exit
    $ sudo umount image
    $ tar vxfz mynewimage.tgz jdiaz859434.img jdiaz859434.manifest.xml

Transfer the image back to India
--------------------------------

::

    $ scp mynewimage.tgz <username>@india.futuregrid.org:/N/u/<username>/

Log into India
--------------

::

    $ ssh <username>@india.futuregrid.org 
    $ module load futuregrid

Upload the image to the repository
----------------------------------

We upload the image to the repository so we can reuse it and share it
with other users. When uploading the image, you can specify some
metadata to describe the properties of the image:

::

    $ fg-repo -p mynewimage.tgz "os=Ubuntu12 & arch=x86_64 & description=My new customized image & tag=tomcat, openmpi"

This command will provide you the ID your image has in the repository.
This ID is needed for the next step.

Register your image in different infrastructures
------------------------------------------------

| You now have your image ready to be registered in the different
FutureGrid infrastructures. To use OpenStack
(`tutorial <https://portal.futuregrid.org/tutorials/openstack>`__) and
Eucalyptus
(`tutorial <https://portal.futuregrid.org/tutorials/eucalyptus3>`__),
you need to indicate the location of you novarc and eucarc file.

Register the image in Openstack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ fg-register -u <username> -r <imageID> -s india -v ~/novarc

Register the image in Eucalyptus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ fg-register -u <username> -r <imageID> -e india -v ~/eucarc

Register the image in HPC
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ fg-register -u <username> -r <imageID> -x india

| 
|  Each command will provide you with the ami-ID that your image has in
the specified infrastructure.

Using your Registered Image
---------------------------

OpenStack (more info in \ `https://portal.futuregrid.org/tutorials/openstack <https://portal.futuregrid.org/tutorials/openstack>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    source novarc
    euca-run-instance -k <keyname> <ami-ID>

Eucalyptus (more info in \ `https://portal.futuregrid.org/tutorials/eucalyptus3 <https://portal.futuregrid.org/tutorials/eucalyptus3>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    source eucarc
    euca-run-instance -k <keyname> <ami-ID>

HPC (more info in \ `https://portal.futuregrid.org/tutorials/hpc <https://portal.futuregrid.org/tutorials/hpc>`__)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Provision a machine with our image and go into Interactive mode (you
are logged into the machine):

::

    qsub -l os=<ami-ID> -I

| Provision two machines with our image and execute an script:

::

    qsub -l os=<ami-ID> -l nodes=2:ppn=8 myscript.sh

| 
| 

RAIN Manual Pages
=================

FutureGrid provides a number of manual pages, listed below.

| (For Rain, our up-to-date documentation of rain can be found at
`https://portal.futuregrid.org/doc/rain/index.html <https://portal.futuregrid.org/doc/rain/index.html>`__
and\ `http://futuregrid.github.com/rain/index.html <http://futuregrid.github.com/rain/index.html>`__
.
| 
| 

fg-repo
=======

Please see
`http://futuregrid.github.com/rain/man-repo.html <http://futuregrid.github.com/rain/man-repo.html>`__

fg-rain
=======

Please see
`http://futuregrid.github.com/rain/man-rain.html <http://futuregrid.github.com/rain/man-rain.html>`__

fg-generate
===========

Please see
`http://futuregrid.github.com/rain/man-generate.html <http://futuregrid.github.com/rain/man-generate.html>`__

fg-register
===========

Please see
`http://futuregrid.github.com/rain/man-register.html <http://futuregrid.github.com/rain/man-register.html>`__

fg-shell
========

Please see
`http://futuregrid.github.com/rain/man-shell.html <http://futuregrid.github.com/rain/man-shell.html>`__

fg-portal-manage
================

The tool is for admin purpose only. An admin person or an system script
can call this to get user/project information from the portal.

NAME
----

**fg-portal-manage** - Futuregrid account management script - the portal
portion

| 

SYNOPSIS
--------

::

    fg-portal-manage 
     -h, --help            show this help message and exit
     -n NAME, --name=NAME  querying by name
     -m MAIL, --mail=MAIL  querying by email
     -i UID, --uid=UID     querying by portal uid
     -u USERNAME, --username=USERNAME
                           querying by portal username
     -k, --attrib          specifying attrib(s) to be displayed, inlcuding:
                           firstname, lastname, email, phone, organization,
                           institution_name, citizenship, sshkey, projectall,
                           project
     -l, --ldif            output ldif format of user info(no dn). If provided
                           all attributes will be included in the output
                           disregarding the setting from -k
     -v, --vetted          Show only those vetted users. If omitted all users
                           that meet the creteria will be shown
     -w, --waiting         Show the waiting list in which a user is eligible to
                           get an LDAP account
     -y, --withsshkey      A sub-option for -w, which shows the waiting list, but
                           only for those who have submitted a sshkey
     -p, --project         Get list of project in table view
     -s STATUS, --status=STATUS
                           A sub-option for -p, which specifies project status
                           that would like to be retrieved. Try pending,
                           approved, completed, denied
     -1, --pidonly         A sub-option for -p which prints out only the project

| 

DESCRIPTION
-----------

FutureGrid account admin tool queries user profile info from the portal
and also checks status against the ldap.

To run the script, python 2.7 is needed (if trying on lower version, try
to install the argparse module; it may also work), as well as the
mysqldb module. Depending on the os distribution, the installation could
be different. E.g., in ubuntu, it's simply: apt-get install
python-mysqldb .

The futuregrid.cfg file needs to be put into the same directory as the
script, and the dummy config values need to be replaced with those real
ones. (Whoever has access to the portal server should have knowledge on
this. We will not distribute this to anymore other than the portal admin
and sys admin.)

| 

EXAMPLES
--------

Run this to get the help info:

::

    ./fg-portal-manage.py -h

This will give a table viewed info of user with uid 3:

::

    ./fg-portal-manage.py -i 3

However, the following: 

::

    ./fg-portal-manage.py -i 3 -l

will print the long quasi-ldif formatted info.

Other commands:

::

    -u for username; -n for realname(first or last); as well as -m for email does similar thing.

./fg-portal-manage.py -l

—will simply print out all users in the portal in the ldif-like format.

./fg-portal-manage.py -l -v

—will print out a similar list but only for (all) those vetted users,
i.e., approved users with an active project.

./fg-portal-manage.py -w

—prints out all users who have approved portal account and are members
of an active project(s) (i.e., vetted users), but don't have an LDAP
account yet.

::

    ./fg-portal-manage.py -l -w

—the same as -w but in long quasi-ldif format.

::

    ./fg-portal-manage.py -w -y

—the same as -w, but prints out only those who have submitted a sshkey.

::

    ./fg-portal-manage.py -p

—lists all FG projects registered in the portal, in the format of:

::

    pid: title|project lead|project manager|status|[members list]

—project lead/manager and members are represented by the portaluid.

::

    ./fg-portal-manage.py -p -s approved

—prints a list of projects but only those in 'approved' status. Other
valid statuses are: pending, completed, denied.

::

    ./fg-portal-manage.py -p -s completed -1(number '1')

| —prints a list of completed projects but only display the projectids.
|   

**SEE ALSO**
------------

ViNe
====

| ViNe is available to FutureGrid users on the foxtrot and sierra
clusters, and can be deployed in any cloud on virtual machines (requires
overlay network knowledge).
| 
|  **Overview**
|  ViNe is a project developed at University of Florida that implements
routing and other communication mechanisms needed to deploy a user-level
virtual network. ViNe is particularly appealing for cloud computing
because it allows the establishment of wide-area virtual networks
supporting symmetric communication among public and private network
resources (even when they are behind firewalls), does not require
changes to either the physical network or the OS of machines, and has
low virtualization overheads. ViNe can provide communication among
FutureGrid and external resources (including those with private IP
addresses) without the need to reconfigure the (FutureGrid) physical
network infrastructure.
| 
|  **Prerequisites**
|  In order for a host to participate in ViNe overlays, users need root
privilege to adjust operating system routing tables. Currently, users
can get root privilege on the virtual machines (VMs) started on FG
clouds. ViNe routers are available on foxtrot and sierra, and VMs
started through Nimbus can be configured to participate on ViNe
overlays.
| 
|  **Setup**
|  All VMs must be members of ViNe overlays, independently wether they
are on public or private networks. In order to enable the ViNe
communication, the following command needs to be executed on
participating VMs:

::

    wget -P /tmp -N http://www.acis.ufl.edu/vine/enablevine.php
    . /tmp/enablevine.sh

| 
|  **Tutorial**

| A step-by-step tutorial on connecting VMs to ViNe overlays is
available at:
| 
`https://portal.futuregrid.org/contrib/simple-vine-tutorial <https://portal.futuregrid.org/contrib/simple-vine-tutorial>`__
|   

OpenNebula 2.0 Tutorial
=======================

This document is aimed to be a guide to start using OpenNebula 2.0.
Therefore, if you need more information about any particular OpenNebula
aspect that it is not addressed here, please refer to the official
documentation located in
(`http://www.opennebula.org/documentation:documentation <http://www.opennebula.org/documentation:documentation>`__)

If you are a user that is only interested in test OpenNebula with some
pre-configured VM, you can use this guide
(`http://www.opennebula.org/documentation:rel2.0:vmg <http://www.opennebula.org/documentation:rel2.0:vmg>`__).

ALL users have to add the following lines to their $HOME/.bashrc or
$HOME/.profile file.

::

    export PATH=$PATH:$ONE_LOCATION/bin
    export ONE_AUTH=$HOME/.one/one_ssh

Create a VM Image Contextualized for OpenNebula
===============================================

In this section we are going to explain how to create a KVM image and
how to contextualize for OpenNebula.

Create VM Image Using KVM
-------------------------

This process is generic and it is not related with OpenNebula directly.
Therefore, this image can be deploy in any machine with KVM and could be
used to create a VM image for any IaaS framework. The first step is
install KVM.

Ubuntu

::

    sudo apt-get install qemu kvm

    sudo apt-get install libvirt-bin

RHEL or CentOS

::

    sudo yum install kvm virt-manager

Be sure that the virtualization features of your machine are enabled in
the BIOS. If they are, you should be able to load the KVM
modules        

::

    sudo modprobe kvm-intel
    or
    sudo modprobe kvm-amd        

Now, we need to download the ISO that we are going to install in the VM,
in this case Ubuntu iso. You can do it from
`http://ubuntu-releases.cs.umn.edu/10.10/ubuntu-10.10-server-amd64.iso. <http://ubuntu-releases.cs.umn.edu/10.10/ubuntu-10.10-server-amd64.iso>`__

Every VM need a disk to be used as a virtual hard drive (1GB is enough
for Ubuntu server). Thus, to create this we use the next command:

::

    qemu-img create machine_name.img -f raw 1G

After this, we are prepared to boot the VM and install the OS.

::

    kvm -m 512 -cdrom /home/user/ubuntu-10.10-server-amd64.iso -boot d machine_name.img

This command will start the VM and you can install the OS as in a normal
PC. When you install the OS in the VM you can boot it using this
command:

::

    kvm -no-acpi -m 512 machine_name.img

 

Contextualize VM
----------------

There are two contextualization mechanisms available in OpenNebula: the
automatic IP assignment, and a more generic way to give any file and
configuration parameters. You can use any of them individually, or both.
Nevertheless, we need to prepare the VM image to use this mechanism
(`http://www.opennebula.org/documentation:rel2.0:cong <http://www.opennebula.org/documentation:rel2.0:cong>`__).  

 

First, download the vmcontext.sh  file in your machine. This file depend
of your linux distribution.

::

    http://dev.opennebula.org/projects/opennebula/repository/show/share/scripts

| In this address you can find the vmcontext for each supported
distribution.
|  CentOS

::

    wget http://dev.opennebula.org/projects/opennebula/repository/revisions/master/raw/share/scripts/centos-5/net-vmcontext/vmcontext -O vmcontext.sh

Ubuntu

::

    wget http://dev.opennebula.org/projects/opennebula/repository/revisions/master/raw/share/scripts/ubuntu/net-vmcontext/vmcontext -O vmcontext.sh

Copy this file to the VM. To do that you can configure a network
interface in the VM and send the file using ssh. For example if your
machine has the private IP 192.168.1.1, you could assign to the VM the
192.168.1.2. So, execute this command in the VM:

::

    sudo ifconfig eht0 192.168.1.2

From your machine execute this command to send the file to your VM:

::

    scp vmcontext.sh 192.168.1.2:/home/user

In the VM copy the file to the /etc/init.d directory:

::

    sudo cp vmcontext.sh /etc/init.d
    sudo chmod +x /etc/init.d/vmcontext.sh

| Configure init.d to execute the script during the VM startup
|  Centos

::

    sudo chkconfig --add vmcontext.sh

Ubuntu

::

    ln /etc/init.d/vmcontext.sh /etc/rc2.d/S01vmcontext.sh

Add at the end of this file (this may not be needed):

::

    ifup -a

or

::

    /etc/init.d/networking restart  #(in ubuntu)
    /etc/init.d/network restart     #(in centos)

Remove the udev persistent files (ubuntu only)

::

    sudo rm -f /etc/udev/rules.d/z25_persistent-net.rules

    sudo rm -f /etc/udev/rules.d/z45_persistent-net-generator.rules

 

With all these steps we have configured the automatic IP assignment in
the VM. Now, we need to enable the generic contextualization by copying
these lines to /etc/rc.local.

::

    mount -t iso9660 /dev/sr0 /mnt  #(in ubuntu)
    mount -t iso9660 /dev/hdc /mnt  #(in centos. Actually this depend on the initrd that you uses. If you use the one provided by Ubuntu then you use the previous line instead of this one)

    if [ -f /mnt/context.sh ]; then

          . /mnt/init.sh

    fi

    umount /mnt

    exit 0

 

The file init.sh is different for each distribution and you can find
them in the `OpenNebula
repository <http://dev.opennebula.org/projects/opennebula/repository/revisions/master/show/share/scripts>`__.
You do not need to include it in the VM because it is included
automatically by OpenNebula when you require it in the VM template.

 

Managing Virtual Machines
=========================

`(http://www.opennebula.org/documentation:rel2.0:vm\_guide) <http://www.opennebula.org/documentation:rel2.0:vm_guide>`__

A Virtual Machine within the OpenNebula system consists of:

-  A capacity in terms memory and CPU
-  A set of NICs attached to one or more virtual networks
-  A set of **disk images**.
-  A state file (optional) or **recovery file**, that contains the
   memory image of a running VM plus some hypervisor specific
   information.

The above items, plus some additional VM attributes like the OS kernel
and context information to be used inside the VM, are specified in a
**`VM
template <http://www.opennebula.org/documentation:rel2.0:template>`__**
file.

Each VM in OpenNebula is identified by an unique number, the ``<VID>``.
Also, the user can assign it a name in the `VM
template <http://www.opennebula.org/documentation:rel2.0:template>`__,
the default name for each VM is ``one-<VID>``.

Virtual Machine Template
------------------------

OpenNebula templates are designed to be hypervisor-agnostic, but there
are still some peculiarities to be taken into account, and mandatory
attributes change depending on the target hypervisor. Hypervisor
specific information for this attributes can be found in the drivers
configuration guides:

-  `Xen Adaptor <http://www.opennebula.org/documentation:rel2.0:xeng>`__
-  `KVM Adaptor <http://www.opennebula.org/documentation:rel2.0:kvmg>`__
-  `VMware
   Adaptor <http://www.opennebula.org/documentation:rel2.0:vmwareg>`__

OpenNebula has been designed to be easily extended, so any attribute
name can be defined for later use in any OpenNebula module. There are
some pre-defined attributes, though.

Please check the `Virtual Machine definition
file <http://www.opennebula.org/documentation:rel2.0:template>`__
reference for details on all the sections.

| A basic VM template to be run using KVM could be this:
|   

::

    #---------------------------------------
    # VM definition example
    #---------------------------------------

    NAME = "ttylinux"

    CPU    = 0.5
    MEMORY = 64

    # --- disks ---

    DISK = [
      source   = "/srv/cloud/images/ttylinux/ttylinux.img",
      target   = "hda",
      readonly = "no" ]

    # --- 1 NIC ---

    NIC = [ NETWORK="Red LAN"]

    FEATURES=[ acpi="no" ]

    # --- VNC server ---

    GRAPHICS = [
      type    = "vnc",
      listen  = "127.0.0.1"]

In the previous template KVM will asume that the image is RAW. If you
have a image with the qcow2 format, you have to add the following to the
DISK description:       

::

    driver = "qcow2"     

Assuming we have a VM template called "ttylinux.one" describing a
virtual machine. Then, we can allocate the VM in OpenNebula issuing a:

.. code:: xterm

    $ onevm create ttylinux.one

afterwards, the VM can be listed with the ``list`` option:

.. code:: xterm

    $ onevm list
       ID     USER     NAME STAT CPU     MEM        HOSTNAME        TIME
       45   oneadmin ttylinux runn   0     64M     192.168.1.5 00 05:19:31

Managing the Image Repository
=============================

The Image Repository system allows OpenNebula administrators and users
to set up images, which can be operative systems or data, to be used in
Virtual Machines easily. These images can be used by several Virtual
Machines simultaneously, and also shared with other users.

Create an OS Image
~~~~~~~~~~~~~~~~~~

This is what a sample template looks like:

.. code:: xterm

    $ cat ubuntu.one.img
    NAME          = "Ubuntu Desktop"
    PATH          = /home/cloud/images/ubuntu-desktop/disk.0
    PUBLIC        = YES
    DESCRIPTION   = "Ubuntu 10.04 desktop for students."

To submit the template, you have to issue the command

.. code:: xterm

    $ oneimage register ubuntu_img.one  

You can use the ``oneimage list`` command to check the available images
in the repository.

.. code:: xterm

    $ oneimage list
      ID     USER                 NAME TYPE              REGTIME PUB PER STAT  #VMS
       1   carlos       Ubuntu Desktop   OS   Jul 11, 2010 15:17 Yes  No  rdy     0

There other commands to manage the images sotored in the Image
Repository:

-  Use the ``oneimage publish`` and ``oneimage unpublish`` commands to
   make your images public for every user to use in their virtual
   machines, or private.
-  Use the ``oneimage persistent`` and ``oneimage nonpersistent``
   commands to make your images persistent (they are not cloned, but
   rather used from the original image) or not. A persistent image
   cannot be published.

Using an Image Stored in the Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The only difference with the previous VM template is that now, you only
need to specify the name of the image that you want to use in the DISK
section.

.. code:: code

    CPU    = 1
    MEMORY = 512

    DISK = [ image     = "Ubuntu Desktop" ]

    NIC    = [ NETWORK = "Public network" ]
    NIC    = [ NETWORK = "Private network" ]

    # FEATURES=[ acpi="no" ]

    GRAPHICS = [ 
      type    = "vnc",              
      listen  = "1.2.3.4",
      port    = "5902"  ]

Assuming that the template containing the previous information is called
template.one, you can deploy the VM using the command:

.. code:: xterm

    onevm create template.one

Save Changes
~~~~~~~~~~~~

Once the VM is deployed you can save the changes made to any disk as a
new image. To do so, use the ``onevm saveas`` command. This command
takes three or four arguments: The VM name (or ID), the disk\_id to
save, the name of the new image to register, and optionally the image
type.

To know the DISK\_ID of the disk you want to save, just take a look at
the ``onevm show`` output for your VM.

The DISK\_IDs are assigned in the same order the disks were defined in
the `VM
template <http://www.opennebula.org/documentation:rel2.0:template>`__.

.. code:: xterm

    $ onevm saveas one-5 0 "Ubuntu with Apache and MySQL"

This will register a new image called “Ubuntu with Apache and MySQL”,
that will be ready as soon as the VM is shut down.

The disks can be saved even if they were defined from a local disk file
(see the `VM
template <http://www.opennebula.org/documentation:rel2.0:template>`__
reference guide for more information on the different kinds of disks).

 

Managing Physical Hosts and Clusters
====================================

(`http://www.opennebula.org/documentation:rel2.0:cluster\_guide <http://www.opennebula.org/documentation:rel2.0:cluster_guide>`__)

In order to use your existing physical nodes, you have to add them to
the system as OpenNebula hosts. You need the following information:

-  *Hostname* of the cluster node or IP
-  *Information Driver* to be used to monitor the host, e.g. ``im_kvm``.
-  *Storage Driver* to clone, delete, move or copy images into the host,
   e.g. ``tm_nfs``.
-  *Virtualization Driver* to boot, stop, resume or migrate VMs in the
   host, e.g. ``vmm_kvm``.

|:!:| Before adding a host check that you can ssh to it without being
prompt for a password

Managing Hosts
--------------

Hosts can be added to the system anytime with the ``onehost`` command.
You can add the cluster nodes to be used by OpenNebula.

This is two example of adding a KVM host.

.. code:: xterm

    $ onehost create host01 im_kvm vmm_kvm tm_nfs

    $ onehost create 192.168.1.5 im_kvm vmm_kvm tm_nfs

This is an example of adding a XEN host.

.. code:: xterm

    $ onehost create host02 im_xen vmm_xen tm_nfs

Note that in the two previous examples we are using tm\_nfs. This means
that OpenNebula is configured to share the VM directory or to use SSH
with no share directory. Other option is the use of LVM. More
information about the diferent storage system supported can be found in
`http://www.opennebula.org/documentation:rel2.0:sm <http://www.opennebula.org/documentation:rel2.0:sm>`__

The status of the cluster can be checked with the ``onehost list``
command:

.. code:: xterm

    $ onehost list
      ID NAME                      CLUSTER                   RVM   TCPU   FCPU   ACPU    TMEM    FMEM STAT
       0 host01                    default                     2    100     90     90  523264  205824   on
       2 host02                    default                     0    100     99     99  523264  264192  off
       3 192.168.1.5               default                     1    400    400    350    7.7G    7.5G   on

And specific information about a host with ``show``:

.. code:: xterm

    $ onehost show 3
    HOST 3 INFORMATION                                                              
    ID                    : 3                   
    NAME                  : 192.168.1.5         
    CLUSTER               : default             
    STATE                 : MONITORED           
    IM_MAD                : im_kvm              
    VM_MAD                : vmm_kvm             
    TM_MAD                : tm_nfs              

    HOST SHARES                                                                     
    MAX MEM               : 8043848             
    USED MEM (REAL)       : 821384              
    USED MEM (ALLOCATED)  : 65536               
    MAX CPU               : 400                 
    USED CPU (REAL)       : 0                   
    USED CPU (ALLOCATED)  : 50                  
    RUNNING VMS           : 1                   

    MONITORING INFORMATION                                                          
    ARCH=x86_64
    CPUSPEED=2000
    FREECPU=400.0
    FREEMEMORY=7819560
    HOSTNAME=fg-gravel5.futuregrid.iu.edu
    HYPERVISOR=kvm
    MODELNAME=Intel(R) Core(TM)2 Quad CPU Q9550 @ 2.83GHz
    NETRX=144207042
    NETTX=23584321
    TOTALCPU=400
    TOTALMEMORY=8043848
    USEDCPU=0.0
    USEDMEMORY=821384

If you want not to use a given host you can temporarily disable it:

 

.. code:: xterm

    $ onehost disable host01

A disabled host should be listed with ``STAT off`` by ``onehost list``.
You can also remove a host permanently with:

 

.. code:: xterm

    $ onehost delete host01

 

|:!:| Detailed information of the ``onehost`` utility can be found `in
the Command Line
Reference <http://www.opennebula.org/documentation:rel2.0:cli#onehost>`__

 

If you use the ``onecluster list`` command you will see that the
“default” cluster is created automatically.

.. code:: xterm

    $ onecluster list
      ID     NAME
       0  default

    $ onehost list
      ID NAME                      CLUSTER                   RVM   TCPU   FCPU   ACPU    TMEM    FMEM STAT
       0 ursa                      default                     0      0      0    100       0       0   on
       1 ursa01                    default                     0      0      0    100       0       0   on
       2 ursa02                    default                     0      0      0    100       0       0   on
       3 ursa03                    default                     0      0      0    100       0       0   on
       4 ursa04                    default                     0      0      0    100       0       0   on

You may want to isolate your physical hosts running virtual machines
containing important services for you business, from the virtual
machines running a development version of your software. The OpenNebula
administrator can do so with these commands:

 

.. code:: xterm

    $ onecluster create testing
    $ onecluster create production

    $ onecluster addhost ursa01 production
    $ onecluster addhost ursa03 testing
    $ onecluster addhost ursa04 testing

    $ onehost list
      ID NAME                      CLUSTER                   RVM   TCPU   FCPU   ACPU    TMEM    FMEM STAT
       0 ursa                      default                     0      0      0    100       0       0   on
       1 ursa01                    production                  0      0      0    100       0       0   on
       2 ursa02                    default                     0      0      0    100       0       0   on
       3 ursa03                    testing                     0      0      0    100       0       0   on
       4 ursa04                    testing                     0      0      0    100       0       0   on

From this point, the newly created machines can use this cluster names
as a `placement
requirement <http://www.opennebula.org/documentation:rel2.0:template#placement_section>`__:

 

.. code:: xterm

    REQUIREMENTS = "CLUSTER = \"testing\""

Once your development cycle is finished, this “testing” and “production”
clusters may not be useful any more. Let's delete the testing cluster.

 

.. code:: xterm

    $ onecluster delete testing
    $ onehost list
      ID NAME                      CLUSTER                   RVM   TCPU   FCPU   ACPU    TMEM    FMEM STAT
       0 ursa                      default                     0      0      0    100       0       0   on
       1 ursa01                    production                  0      0      0    100       0       0   on
       2 ursa02                    default                     0      0      0    100       0       0   on
       3 ursa03                    default                     0      0      0    100       0       0   on
       4 ursa04                    default                     0      0      0    100       0       0   on

As you can see, the hosts assigned to the “testing” cluster have been
moved to the “default” one.

|:!:| Detailed information of the ``onecluster`` utility can be found in
the `Command Line
Reference <http://www.opennebula.org/documentation:rel2.0:cli#onecluster>`__

 

 

Managing Virtual Networks
=========================

`( <http://www.opennebula.org/documentation:rel2.0:vgg>`__\ `http://www.opennebula.org/documentation:rel2.0:vgg <http://www.opennebula.org/documentation:rel2.0:vgg>`__)

A cluster node is connected to one or more networks that are available
to the virtual machines through the corresponding bridges. To set up a
virtual networks you just need to know the name of the bridge to bind
the virtual machines to.

Defining a Virtual Network
--------------------------

OpenNebula allows for the creation of Virtual Networks by mapping them
on top of the physical ones. All Virtual Networks are going to share a
default value for the MAC preffix, set in the ``oned.conf`` file.

There are two types of Virtual Networks in OpenNebula:

#. **Fixed**, defines a fixed set of IP-MAC pair addresses
#. **Ranged**, defines a class network.

|:!:| Virtual Networks created by ``oneadmin`` can be used by every
other user.

 

Fixed Virtual Network
~~~~~~~~~~~~~~~~~~~~~

For example to create a Fixed Virtual Network, called ``Public`` with
the set of public IPs to be used by the VMs, just create a file with the
following contents:

.. code:: code

    NAME = "Public"
    TYPE = FIXED

    #We have to bind this network to ''virbr1'' for Internet Access
    BRIDGE = vbr1

    LEASES = [IP=130.10.0.1, MAC=50:20:20:20:20:20]
    LEASES = [IP=130.10.0.2, MAC=50:20:20:20:20:21]
    LEASES = [IP=130.10.0.3]
    LEASES = [IP=130.10.0.4]

where **LEASES**: Definition of the IP-MAC pairs. If an IP is defined,
and there is no associated MAC, OpenNebula will generate it using the
following rule: ``MAC = MAC_PREFFIX:IP``. So, for example, from IP
10.0.0.1 and MAC\_PREFFIX 00:16, we get 00:16:0a:00:00:01. Defining only
a MAC address with no associated IP is not allowed.

 

Ranged Virtual Network
~~~~~~~~~~~~~~~~~~~~~~

The following is an example of a Ranged Virtual Network template:

.. code:: code

    NAME = "Red LAN"
    TYPE = RANGED

    # This vnet can be only used by the owner user
    PUBLIC = NO

    #Now we'll use the cluster private network (physical)
    BRIDGE = vbr0

    NETWORK_SIZE    = C
    NETWORK_ADDRESS = 192.168.0.0

where:

-  **NETWORK\_ADDRESS**: Base network address to generate IP addresses.
-  **NETWORK\_SIZE**: Number of hosts that can be connected using this
   network. It can be defined either using a number or a network class
   (B or C).

Adding and Deleting Virtual Networks
------------------------------------

Once a template for a VN has been defined, the ``onevnet`` command can
be used to create it.

To create the previous networks put their definitions in two different
files, ``public.net`` and ``red.net``, respectively. Then, execute:

.. code:: xterm

    $ onevnet -v create public.net
    $ onevnet -v create red.net

Also, ``onevnet`` can be used to query OpenNebula about available VNs:

.. code:: xterm

    $ onevnet list
      ID USER     NAME              TYPE BRIDGE P #LEASES
       2 oneadmin Public           Fixed   vbr1 Y       0
       3 oneadmin Red LAN         Ranged   vbr0 N       0

with ``USER`` the owner of the network and ``#LEASES`` the number of
IP-MACs assigned to a VM from this network.

We can see the details of a particular VN:

::

    $onevnet show 0

    VIRTUAL NETWORK 0 INFORMATION                                                   
    ID:       : 0                   
    UID:      : 0                   
    PUBLIC    : N                   

    VIRTUAL NETWORK TEMPLATE                                                        
    BRIDGE=br1
    LEASES=[ IP=192.168.1.7 ]
    LEASES=[ IP=192.168.1.8 ]
    LEASES=[ IP=192.168.1.9 ]
    LEASES=[ IP=192.168.1.10 ]
    NAME=Small LAN
    TYPE=FIXED

    LEASES INFORMATION                                                              
    LEASE=[ IP=192.168.1.7, MAC=02:00:c0:a8:01:07, USED=1, VID=54 ]
    LEASE=[ IP=192.168.1.8, MAC=02:00:c0:a8:01:08, USED=1, VID=45 ]
    LEASE=[ IP=192.168.1.9, MAC=02:00:c0:a8:01:09, USED=0, VID=-1 ]
    LEASE=[ IP=192.168.1.10, MAC=02:00:c0:a8:01:0a, USED=0, VID=-1 ]

To delete a virtual network just use ``onevnet delete``. For example to
delete the previous networks:

.. code:: xterm

    $onevnet delete 2
    $onevnet delete 'Red LAN'

|:!:| Check the ``onevnet`` command help or `reference
guide <http://www.opennebula.org/documentation:rel2.0:cli#onevnet>`__
for more options to list the virtual networks.

Using the Leases Within the Virtual Machine
-------------------------------------------

Hypervisors can attach a specific MAC address to a virtual network
interface, but Virtual Machines need to obtain an IP address. There are
a variety of ways to achieve this within OpenNebula:

-  Obtain the IP from the MAC address, using the default MAC assignment
   schema (**PREFERRED**)

-  Use the ``CONTEXT`` attribute, check the `Contextualization
   Guide <http://www.opennebula.org/documentation:rel2.0:cong>`__

Configuring the Virtual Machine to Use the Leases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please visit the `contextualization
guide <http://www.opennebula.org/documentation:rel2.0:cong>`__ to learn
how to configure your Virtual Machines.

Accounting
==========

(`http://opennebula.org/documentation:rel2.0:accounting <http://opennebula.org/documentation:rel2.0:accounting>`__)

Physical Resources
------------------

Usage of a physical resource can be obtained for a given user or a given
virtual machine. Accounting reports always show aggregated information,
considering possible migration of a virtual machine to between physical
resources.

``oneacct host`` - prints accounting information for the physical
resources

Obtaining the accounting information for user john

.. code:: xterm

    $ oneacct host -u john
        HOST       XFR      RUNN  VMS
         sun  00:00:05  00:18:40    2
       rigil  00:00:05  00:00:02    1
     schedar  00:00:02 198:17:53    1

The columns are:

-  XFR: Total transfer time. It includes cloning VM disk images in the
   target resource and transfer back of modified images when applicable
-  RUNN: Total running time. It includes boot, running and saving times
-  VMS: Total number of virtual machines

Obtaining accounting information for host

.. code:: xterm

    $ oneacct host -r rigil
        USER       XFR      RUNN  VMS
       admin  00:00:05  00:00:02    1
        hugo  00:00:02 194:25:30    1

  Virtual Resources
-------------------

Accounting information for Virtual Machines can be obtained for a given
user or a given virtual machine.

The current version of the virtual resources reports does not consider
possible migration of a virtual machine to between physical resources.

``oneacct vm`` - prints accounting information for virtual machines

Obtaining the accounting information for a given VM

.. code:: xterm

    $ oneacct vm 2
        HOST       XFR      RUNN
         sun  00:00:01  00:00:21
     schedar  00:00:02 198:17:53

The columns are:

-  HOST: where the VM has been executed
-  XFR: Total transfer time in that host
-  RUNN: Total running time in the host

Obtaining the accounting information for a given host

.. code:: xterm

    $ oneacct vm -r rigil
    VMID     NAME       XFR      RUNN
       5      xee         2 194:25:30
       6      phi         5  00:00:02

Obtaining the accounting information for a given user

.. code:: xterm

    $ oneacct vm -u carroll
    VMID     NAME       XFR      RUNN    HOSTS
       3 Ubuntu-9  00:00:01  00:02:54        3
       4 Ubuntu-9  00:00:00  00:00:10        2

In this last example columns show aggregated transfer and running times.

 

User Management
===============

(`http://www.opennebula.org/documentation:rel2.0:users) <http://www.opennebula.org/documentation:rel2.0:users>`__

Adding New Users
----------------

Current Authentication/Authorization module (from now on auth module)
has support for user/password and rsa private/public key authentication
and also user quota support. Here, we are going to talk about the SSH
module and how to add users using SSH keys. More information can be
found in the official documentation:
`http://www.opennebula.org/documentation:rel2.0:users <http://www.opennebula.org/documentation:rel2.0:users>`__

Public Key Extraction (Done by Users)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a user compatible with ``ssh`` option for authentication the
administrator needs to add the user's public key into the database. The
file with public key generated by ``ssh-keygen``
(``$HOME/.ssh/id_rsa.pub``) is written in a format readable by
``openssl`` so the public key should be extracted by the user and sent
to the administrator. The way to extract it is the following:

.. code:: code

    $ oneauth key
    Enter PEM pass phrase:
    MIIBCAKCAQEApUO+JISjSf02rFVtDr1yar/34EoUoVETx0n+RqWNav+5wi+gHiPp3e03AfEkXzjDYi8F
    voS4a4456f1OUQlQddfyPECn59OeX8Zu4DH3gp1VUuDeeE8WJWyAzdK5hg6F+RdyP1pT26mnyunZB8Xd
    bll8seoIAQiOS6tlVfA8FrtwLGmdEETfttS9ukyGxw5vdTplse/fcam+r9AXBR06zjc77x+DbRFbXcgI
    1XIdpVrjCFL0fdN53L0aU7kTE9VNEXRxK8sPv1Nfx+FQWpX/HtH8ICs5WREsZGmXPAO/IkrSpMVg5taS
    jie9JAQOMesjFIwgTWBUh6cNXuYsQ/5wIwIBIw

The string the user has to send to the administrator to create the user
is written to the console.

User Creation (done by the administrator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the user sends the rsa public key the administration needs to
create a new account in OpenNebula system. This is done in a similar way
as standard user/password users but using the public key provided by the
user and adding a parameter to the command so the password (in this case
the public key) is stored as is in the database. Here is the command to
create a user called ``test`` with the previously extracted public key:

.. code:: code

    $ oneuser create -n test "MIIBCAKCAQEApUO+JISjSf02rFVtDr1yar/34EoUoVETx0n+RqWNav+5wi+gHiPp3e03AfEkXzjDYi8F
    voS4a4456f1OUQlQddfyPECn59OeX8Zu4DH3gp1VUuDeeE8WJWyAzdK5hg6F+RdyP1pT26mnyunZB8Xd
    bll8seoIAQiOS6tlVfA8FrtwLGmdEETfttS9ukyGxw5vdTplse/fcam+r9AXBR06zjc77x+DbRFbXcgI
    1XIdpVrjCFL0fdN53L0aU7kTE9VNEXRxK8sPv1Nfx+FQWpX/HtH8ICs5WREsZGmXPAO/IkrSpMVg5taS
    jie9JAQOMesjFIwgTWBUh6cNXuYsQ/5wIwIBIw"

After this the administrator can check that the user is in the system:

.. code:: code

    $ oneuser list
      ID USER            PASSWORD                                          
       0 oneadmin        5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8          
       1 test            MIIBCAKCAQEApUO+JISjSf02rFVtDr1yar/34EoUoVETx0n+Rq

User Login (Done by Users)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Before performing any action in OpenNebula system the user needs to
login. To do this we must issue this command:

.. code:: code

    $ oneauth login test
    Enter PEM pass phrase:
    export ONE_AUTH=/home/test/.one/one_ssh

The command on success will print the command needed to execute so
OpenNebula knows where to find the login file generated.

.. code:: code

    $ export ONE_AUTH=/home/test/.one/one_ssh

This line can also be added by the user to $HOME/.profile or
$HOME/.bashrc so it is not needed to be executed every new system login.

By default the login file will be valid for one hour. This expire time
can be changed adding another parameter with the number of seconds you
want the login to be valid. For example to create a 2 hours valid login
you can issue this command:

.. code:: code

    $ oneauth login test 7200
    Enter PEM pass phrase:
    export ONE_AUTH=/home/test/.one/one_ssh

 

Quota
-----

When quota module is enabled it checks for user resource consumption
before letting a VM to created in OpenNebula system. You have to take
into account that all resources for VMs listed by ``onevm list`` for a
user are counted as used. Administrator user has unlimited quota.

Quotas Database Security (Done by the Administrator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default user quota database is an *sqlite* database located at
``$ONE_LOCATION/var/auth.db``. This database on creation does not have
secure permissions and the administrator may change its permission and
maybe its location. To change its location you can use a full path to
the database in the auth module configuration file:

.. code:: code

    :database: sqlite:///somewhere/in/your/hdd/auth.db
    ...

You may also change its permissions to ``0600`` so the unix user that
runs OpenNebula daemons is the only with read/write access permissions.

Default Quotas (Done by the Administrator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Default quotas for all users are configured as previously stated in
*Configuring and Enabling Auth Module*. This is the first configuration
you will have to do if you enable quota system as any user without
explicit quotas can only use that amount of resources.

Explicit User Quotas (Done by the Administrator)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting special quotas for a user can be done using ``oneauth`` command.
If you have secured the database only unix user that runs OpenNebula
will be able to update them. The steps to change permissions for a user
are as follows:

-  Find the user id for the user we want to change limits. We are
   searching for user ``test``:

.. code:: code

    $ oneuser list
      ID USER            PASSWORD                                          
       0 oneadmin        5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8          
       1 test            MIIBCAKCAQEApUO+JISjSf02rFVtDr1yar/34EoUoVETx0n+Rq

-  The user id for ``test`` is 1. Now we use
   ``oneauth quota set <user id> <cpu> <memory>`` to change user limits:

.. code:: code

    $ oneauth quota set 1 20 10000000

 

PaaS - Platform as a Service
============================

This chapter contains information in regards to Platform as a Service
offerings on FutureGrid

Using Map/Reduce in FutureGrid
==============================

| As the computing landscape becomes increasingly data-centric,
data-intensive computing environments are poised to transform scientific
research. In particular, MapReduce based programming models and run-time
systems such as the open-source Hadoop system have increasingly been
adopted by researchers with data-intensive problems, in areas including
bio-informatics, data mining and analytics, and text processing. 
| 
|  FutureGrid provides capabilities that allow users to experiment with
MapReduce applications and middleware, including the widely-used
Hadoop platform and the iterative map/reduce Twister plaftorm. There are
different ways you may want to use MapReduce platforms in the testbed.
This page guides you in selecting from FutureGrid capabilities that are
best suited depending on your goals, and links to respective tutorials:

 MapReduce on Physical Machines
-------------------------------

| 
|  While there exist MapReduce systems that run on virtual machines,
many dedicated Hadoop deployments run the Hadoop run-time and
data-processing applications on physical machines to avoid I/O
virtualization overheads. Currently, we have two major approaches for
deploying Hadoop on physical machines in FutureGrid: The first uses
"MyHadoop", where Hadoop tasks are instantiated dynamically using an HPC
scheduler (Torque). The second uses "SalsaHadoop", where Hadoop starts
with a 'one-click script' automatically on obtained HPC nodes and
tasks are submitted to the Hadoop master directly. In addition,
FutureGrid also supports Twister, a lightweight iterative MapReduce
runtime, running on the HPC cluster. 
| 
|  Associated tutorials:

-  `Basic High Performance
   Computing <https://portal.futuregrid.org/tutorials/hpc>`__ [novice]
-  `Running Hadoop as a batch job using
   MyHadoop <https://portal.futuregrid.org/tutorials/running-hadoop-batch-job-using-myhadoop>`__ [novice]
-  `Running SalsaHadoop (one-click Hadoop) on HPC
   environment <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc>`__
   [beginner]
-  `Running Twister on HPC
   environment <https://portal.futuregrid.org/twister-futuregrid-hpc>`__
   [beginner]

 MapReduce on Virtual Machines
------------------------------

| 
|  Running Hadoop on virtual machines gives users the flexibility to
customize the Hadoop runtime system and any additional middleware as
desired, e.g. for research on novel MapReduce middleware approaches.
Currently, Hadoop images can be deployed on FutureGrid resources in the
following ways:
| 

-  `Using <https://portal.futuregrid.org/tutorials/eucalyptus>`__\ ` Eucalyptus
   on
   FutureGrid <https://portal.futuregrid.org/tutorials/eucalyptus>`__\ ` [novice] <https://portal.futuregrid.org/tutorials/eucalyptus>`__
-  `Running SalsaHadoop on
   Eucalyptus <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus>`__
   [intermediate]
-  `Running FG-Twister on
   Eucalyptus <https://portal.futuregrid.org/tutorials/eucalyptus-and-twister-futuregrid>`__ [intermediate]
-  `Running Twister on
   Eucalyptus <https://portal.futuregrid.org/twister-futuregrid-cloud-eucalyptus>`__
   [intermediate]

| 

Education / Training with MapReduce
-----------------------------------

| 
|  FutureGrid offers educational virtual appliances that allow users to
deploy virtual private clusters where Hadoop tasks can be deployed using
Condor. This approach allows users to not only experiment with Hadoop on
FutureGrid, but also with virtual clusters, on their own resources.
Currently, Hadoop virtual appliances can be deployed on FutureGrid
resources in the following ways:
| 

-  `Running a Grid Appliance on
   FutureGrid <http://portal.futuregrid.org/tutorials/ga9>`__ [novice]
-  `Running Condor tasks on the Grid
   Appliance <http://portal.futuregrid.org/tutorials/ga8>`__ [novice]
-  `Running Hadoop tasks on the Grid
   Appliance <http://portal.futuregrid.org/tutorials/ga10>`__ [novice]
-  `Running Hadoop WordCount on
   FutureGrid <https://portal.futuregrid.org/hadoop-wordcount>`__
   [novice]
-  `Running Hadoop Blast on
   FutureGrid <https://portal.futuregrid.org/hadoop-blast>`__ [novice]
-  `Running Twister Kmeans on
   FutureGrid <https://portal.futuregrid.org/twister-kmeans>`__ [novice]
-  `Running Twister Blast on
   FutureGrid <https://portal.futuregrid.org/twister-blast>`__ [novice]

Running Hadoop as a Batch Job using MyHadoop
============================================

|image94|          |Hadoop logo|

 
=

Overview
========

MapReduce is a programming model developed by Google\ **.**\ Their
definition of MapReduce is as follows:  "MapReduce is a programming
model and an associated implementation for processing and generating
large data sets. Users specify a map function that processes a key/value
pair to generate a set of intermediate key/value pairs, and a reduce
function that merges all intermediate values associated with the same
intermediate key."  For more information about MapReduce, please see the
Google paper `here <http://labs.google.com/papers/mapreduce.html>`__.

The `Apache Hadoop Projec <http://hadoop.apache.org>`__\ t provides an
open source implementation of MapReduce and HDFS (Hadoop Distributed
File System).   

This tutorial illustrates how to run Apache Hadoop thru the batch
systems on FutureGrid using the MyHadoop tool.  

Hadoop on FutureGrid
====================

Hadoop 0.20.2 is currently installed on Alamo, Hotel, India, and Sierra
FutureGrid systems.  Please see the `Getting Started
guide <https://portal.futuregrid.org/gettingstarted>`__ to get accounts
on those systems.

What is myHadoop?
=================

`MyHadoop <http://sourceforge.net/projects/myhadoop/>`__ is a set of
scripts that configure and instantiate Hadoop as a batch job. 

Running myHadoop on FutureGrid
==============================

To run the example, use the following steps.

#. Log into a FutureGrid system that has myHadoop available.  In this
   tutorial, we are executing from the Hotel machine.

   ::

       $ ssh hotel.futuregrid.org
       This machine accepts SSH public key and One Time Password (OTP) logins only.
       If you do not have a public key set up, you will be prompted for a password.
       This is *not* your FutureGrid password, but the One Time Password generated from your
       OTP token.  Do not type your FutureGrid password, it will not work.  If you do not
       have a token or public key, you will not be able to login.
       [gvonlasz@login1 ~]$

#. Load the myHadoop module.  On some FutureGrid systems, you may also
   need to load the "torque" module as well if qstat is not already in
   your environment.

   ::

       [gvonlasz@login1 ~]$ module load myhadoop
       SUN Java JDK version 1.6.0 (x86_64 architecture) loaded
       Apache Hadoop Common version 0.20.203.0 loaded
       myHadoop version 0.2a loaded
       [gvonlasz@login1 ~]$ 

#. To run the example now, skip to step 9.  Otherwise, view the
   pbs-example.sh script located in $MY\_HADOOP\_HOME/pbs-example.sh.
    At the top of the file, you will see standard batch directives
   indicating which queue to run the Hadoop job, how many nodes, etc.
#. ::

       #PBS -q batch
       #PBS -N hadoop_job
       #PBS -l nodes=4:ppn=8
       #PBS -o hadoop_run.out
       #PBS -e hadoop_run.err
       #PBS -V

#. Next, there is a line to load Java via modules under the above lines:

   ::

       module add java

#. In the example script, a temporary directory to store Hadoop
   configuration files is specified as ${HOME}/myHadoop-config (although
   any globally accessible place is fine):

   ::

       #### Set this to the directory where Hadoop configs should be generated
       # Don't change the name of this variable (HADOOP_CONF_DIR) as it is
       # required by Hadoop - all config files will be picked up from here
       #
       # Make sure that this is accessible to all nodes
       export HADOOP_CONF_DIR="${HOME}/myHadoop-config"

#. The pbs-example.sh script runs the "wordcount" program from
   the hadoop-0.20.2-examples.jar.  There is sample text data from the
   `Project Gutenberg website <http://www.gutenberg.org/>`__ located a
   $MY\_HADOOP\_HOME/gutenberg.

   ::

       -bash-3.2$ ls $MY_HADOOP_HOME/gutenberg
       1342.txt.utf8

#. The following lines create a Data directory in HDFS (directory
   specified in $MY\_HADOOP\_HOME/bin/setenv.sh), copies over the
   gutenberg data, executes the Hadoop job, and then copies the output
   back your ${HOME}/Hadoop-Outputs directory.  

   ::

       #### Run your jobs here
       echo "Run some test Hadoop jobs"
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -mkdir Data
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -copyFromLocal $MY_HADOOP_HOME/gutenberg Data
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -ls Data/gutenberg
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR jar $HADOOP_HOME/hadoop-0.20.2-examples.jar wordcount Data/gutenberg Outputs
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -ls Outputs
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -copyToLocal Outputs ${HOME}/Hadoop-Outputs

#. Now submit the pbs-example.sh script to Hotel:

   ::

       [gvonlasz@login1 ~]$ qsub $MY_HADOOP_HOME/pbs-example.sh 
       40256.svc.uc.futuregrid.org

#. The job will take about 5 minutes to complete.  To monitor its
   status, type 'qstat'.  The "R" means the job is running.

   ::

       [gvonlasz@login1 ~]$ qstat
       Job id                    Name             User            Time Use S Queue
       ------------------------- ---------------- --------------- -------- - -----
       40256.svc                  hadoop_job       gvonlasz               0 R batch                  

#. When it is done, the status of the job will be "C" meaning the job
   has completed (or it will no longer be displayed in qstat output).
    You should see a new hadoop\_run.out file and an "Hadoop-Outputs"
   directory :

   ::

       [gvonlasz@login1 ~]$ qstat
       Job id                    Name             User            Time Use S Queue
       ------------------------- ---------------- --------------- -------- - -----
       40256.svc                  hadoop_job       gvonlasz       00:00:05 C batch                   
       -bash-3.2$ ls
       Hadoop-Outputs hadoop_run.out

#. View results of the word count operation:

   ::

       [gvonlasz@login1 ~]$ head Hadoop-Outputs/part-r-00000  
       "'After    1
       "'My   1
       "'Tis  2
       "A 12
       "About 2
       "Ah!   2
       "Ah!" 1
       "Ah,   1
       "All   2
       "All!  1

Now to run you own custom Hadoop job, make a copy of the
$MY\_HADOOP\_HOME/pbs-example.sh script and modify the lines described
in Step 7.

Persistent Mode
===============

The above example copies input to local HDFS scratch space you specified
in $MY\_HADOOP\_HOME/bin/setenv.sh, runs MapReduce, and copies output
from HDFS back to your home directory.  This is called non-persistent
mode and is good for small amounts of data.  Alternatively, you can run
in persistent mode which is good if you have access to a parallel file
system or have a large amount of data that will not fit in scratch
space.  To enable persistent mode, follow the directions in
pbs-example.sh.

Customizing Hadoop Settings
===========================

To modify any of the Hadoop settings
like maximum\_number\_of\_map\_task, maximum\_number\_of\_reduce\_task,
etc., make you own copy of myHadoop and customize the settings
accordingly.  For example:

#. Copy the $MY\_HADOOP\_HOME directory to your home directory

   ::

       -bash-3.2$ cp -r $MY_HADOOP_HOME $HOME/myHadoop

#. Then edit $HOME/myHadoop/pbs-example.sh and on line 16, replace it
   with:

   ::

       . ${HOME}/myHadoop/bin/setenv.sh

#. Similarly edit $HOME/myHadoop/bin/setenv.sh and on line 4, replace it
   with:

   ::

       export MY_HADOOP_HOME=$HOME/myHadoop

#. Customize the settings in the Hadoop files as needed in
   $HOME/myHadoop/etc

#. Submit your copy of pbs-example.sh:

   ::

       -bash-3.2$ qsub $HOME/myHadoop/pbs-example.sh

Using a Different Installation of Hadoop
========================================

If you would like to use a different version of my Hadoop or have
customized the Hadoop code in some way, you can specify a different
installation of Hadoop by redefining the HADOOP\_HOME variable after
$MY\_HADOOP\_HOME/bin/setenv.sh is called within your own copy of
pbs-example.sh.  

::

    ### Run the myHadoop environment script to set the appropriate variables
    #
    # Note: ensure that the variables are set correctly in bin/setenv.sh
    . /opt/myHadoop/bin/setenv.sh
    export HADOOP_HOME=${HOME}/my-custom-hadoop

More Information
================

For more information about how myHadoop works, please see the
documentation in $MY\_HADOOP\_HOME/docs/myHadoop.pdf 

Using SalsaHadoop on FutureGrid
===============================

| PLEASE NOTE: THIS MANUAL PAGE IS A DRAFT, PLEASE PROVIDE FEEDBACK IN
THE COMMENT SECTION.
|   

SalsaHadoop Introduction
------------------------

| Apache Hadoop is widely used by domain scientists for running their
scientific applications in parallel fashion. For our research
convenience, SalsaHPC research group develops SalsaHadoop, an automatic
method to start Hadoop without worrying the Hadoop configuration, can be
running on any general cluster and multiple machines. SalsaHadoop has
been used by `SalsaHPC research group <http://salsahpc.indiana.edu/>`__
and a graduate-level course `CSCI B649 Cloud Computing for Data
Intensive Sciences <http://salsahpc.indiana.edu/csci-b649-2011/>`__. 
| 

Running SalsaHadoop on FutureGrid
---------------------------------

SalsaHadoop can be run in various modes within FG either in FutureGrid
HPC and FutureGrid Cloud/IaaS environments. The following tutorials
provide step-by-step instructions to use SalsaHadoop on these modes, and
also it shows some examples of running Hadoop applications after
starting Hadoop. In general, the HPC environment is easier if you do not
have experience with IaaS Eucalyptus. 

-  SalsaHadoop on FutureGrid

   -  `SalsaHadoop with FutureGrid
      HPC <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc>`__ [recommended]

      -  `Get HPC compute
         nodes <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc#HPC_Nodes>`__
      -  `Hadoop
         Configuration <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc#Configuration>`__
      -  `Verify Hadoop HDFS and MapReduce Daemon
         status <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc#Verify>`__

   -  `SalsaHadoop with FutureGrid Cloud
      Eucalyptus <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus>`__

      -  `Get VM compute
         nodes <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus#VM_Nodes>`__

         -  `VM Hostname
            setting <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus#VM_Nodes_Set>`__
         -  `VM attached disk
            configuration <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus#Euca_Disk>`__

      -  `Hadoop
         Configuration <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus#Configuration>`__ (same
         as above with different masters and slaves hostname)
      -  `Verify Hadoop HDFS and MapReduce Daemon
         status <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus#Verify>`__

   -  Run SalsaHadoop Applications

      -  `Hadoop
         WordCount <https://portal.futuregrid.org/tutorials/one-click-hadoop-wordcount-eucalyptus-futuregrid>`__
      -  `Hadoop
         Blast <https://portal.futuregrid.org/manual/hadoop-blast>`__

   -  Run Hadoop with static FutureGrid-Bravo HDFS\*

Hadoop Blast
============

| Number:
|  Author: Tak-Lon Stephen Wu
|  Improvements: 
|  Version: 0.1
|  Date: 2011-11-01

Hadoop Blast
------------

BLAST (Basic Local Alignment Search Tool) is one of the most widely used
bioinformatics applications written in C++, and the version we are using
is v2.2.23. Hadoop Blast is an advanced Hadoop program which helps
Blast, a bioinformatics application, utilizes the Computing Capability
of Hadoop. The database used in the following settings is a subset (241
MB) of Non-redundant protein sequence database from
`nr <http://www.ncbi.nlm.nih.gov/staff/tao/URLAPI/blastdb.html>`__
(8.5GB) database.

You can download the `Hadoop Blast source
code <http://salsahpc.indiana.edu/tutorial/source_code/Hadoop-Blast.zip>`__
and customized Blast program and Database archive
(`BlastProgramAndDB.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`__)
from `Big Data for Science
tutorial <http://salsahpc.indiana.edu/tutorial/hadoopblast.html>`__.

 
-

 
-

Acknowledge
-----------

| This page was original designed by
`SalsaHPC <http://salsahpc.indiana.edu/>`__ group for `Big Data for
Science Workshop <http://salsahpc.indiana.edu/tutorial/>`__, you can see
the original pages
`here <http://salsahpc.indiana.edu/tutorial/hadoopblast.html>`__.

Requirement
-----------

#. Login to FutureGrid Cluster and obtain compute nodes.
   (`HPC <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc#HPC_Nodes>`__/
   `Eucalyptus <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus>`__)
#. Start SalsaHadoop/Hadoop on compute nodes. (`SalsaHadoop
   Tutorial <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc#Configuration>`__)
#. Download and unzip \ `Hadoop Blast source
   code <http://salsahpc.indiana.edu/tutorial/source_code/Hadoop-Blast.zip>`__
   from `Big Data for Science
   tutorial <http://salsahpc.indiana.edu/tutorial/hadoopwordcount.html>`__.
#. Download customized Blast binary and Database archive
   `BlastProgramAndDB.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`__
#. Linux command experience.

1. Download Hadoop Blast under $
--------------------------------

HADOOP\_HOME
------------

| Assuming your start SalsaHadoop/Hadoop with setting
$HADOOP\_HOME=~/hadoop-0.20.203.0, and is running the master node on
i55. Then, we download the `Hadoop Blast source
code <http://salsahpc.indiana.edu/tutorial/source_code/Hadoop-Blast.zip>`__
and customized Blast program and Database archive
(`BlastProgramAndDB.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`__)
from `Big Data for Science
tutorial <http://salsahpc.indiana.edu/tutorial/hadoopblast.html>`__ to
$HADOOP\_HOME.

::

    [taklwu@i55 ~]$ cd $HADOOP_HOME
    [taklwu@i55 hadoop-0.20.203.0]$ wget http://salsahpc.indiana.edu/tutorial/source_code/Hadoop-Blast.zip
    [taklwu@i55 hadoop-0.20.203.0]$ wget http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz
    [taklwu@i55 hadoop-0.20.203.0]$ unzip Hadoop-Blast.zip

2. Prepare Hadoop Blast
-----------------------

Assuming the program are already stored in $HADOOP\_HOME/Hadoop-Blast,
we need to copy the input files, Blast program and Database archive
(`BlastProgramAndDB.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`__)
onto HDFS.

::

    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop fs -put $HADOOP_HOME/Hadoop-Blast/blast_input HDFS_blast_input
    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop fs -ls HDFS_blast_input
    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop fs -copyFromLocal $HADOOP_HOME/BlastProgramAndDB.tar.gz BlastProgramAndDB.tar.gz
    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop fs -ls BlastProgramAndDB.tar.gz

-  Line 1 push all the blast input files (FASTA formatted queries) onto
   HDFS “HDFS\_blast\_input” directory from local disk.
-  Line 2 list the pushed files on HDFS directory "HDFS\_blast\_input"
-  Line 3 copies the Blast program and database archive
   (BlastProgramAndDB.tar.gz) from $HADOOP\_HOME onto the HDFS as
   distributed caches which will be used later.
-  Line 4 double check the pushed Blast program and database archive
   "BlastProgramAndDB.tar.gz" on HDFS

3. Execute Hadoop-Blast
-----------------------

After deploying those required files onto HDFS, run the Hadoop Blast
program with the following commands:

::

    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop jar $HADOOP_HOME/Hadoop-Blast/executable/blast-hadoop.jar BlastProgramAndDB.tar.gz \
     bin/blastx /tmp/hadoop-taklwu-test/ db nr HDFS_blast_input HDFS_blast_output '-query #_INPUTFILE_# -outfmt 6 -seg no -out #_OUTPUTFILE_#'

Here is the description of the above command:

::

    bin/hadoop jar Executable BlastProgramAndDB_on_HDFS bin/blastx Local_Work_DIR db nr HDFS_Input_DIR Unique_HDFS_Output_DIR '-query #_INPUTFILE_# -outfmt 6 -seg no -out #_OUTPUTFILE_#'

+----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| **Parameter**                    | **Description**                                                                                                   |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Executable                       | The full path of the Hadoop-Blast Jar program, e.g. $HADOOP\_HOME/apps/Hadoop-Blast/executable/blast-hadoop.jar   |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| BlastProgramAndDB\_on\_HDFS      | The archive name of Blast Program and Database on HDFS, e.g. BlastProgramAndDB.tar.gz                             |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Local\_Work\_DIR                 | The local directory for storing temporary output of Blast Program, e.g. /tmp/hadoop-test/                         |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| HDFS\_Input\_DIR                 | The HDFS remote directory where stored input files, e.g. HDFS\_blast\_input                                       |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Unique\_HDFS\_Output\_DIR        | A Never used HDFS remote directory for storing output files, e.g. HDFS\_blast\_output                             |
+----------------------------------+-------------------------------------------------------------------------------------------------------------------+

| 
|  If Hadoop is running correctly, it will print hadoop running messages
similar to the following:

::

    11/11/01 19:31:08 INFO input.FileInputFormat: Total input paths to process : 16
    11/11/01 19:31:08 INFO mapred.JobClient: Running job: job_201111021738_0002
    11/11/01 19:31:09 INFO mapred.JobClient:  map 0% reduce 0%
    11/11/01 19:31:31 INFO mapred.JobClient:  map 18% reduce 0%
    11/11/01 19:31:34 INFO mapred.JobClient:  map 50% reduce 0%
    11/11/01 19:31:53 INFO mapred.JobClient:  map 75% reduce 0%
    11/11/01 19:32:04 INFO mapred.JobClient:  map 100% reduce 0%
    ...
    Job Finished in 191.376 seconds

3. Monitoring Hadoop
--------------------

We can also monitor the job status using lynx, a text browser, on i136
based Hadoop monitoring console. Assuming the Hadoop Jobtracker is
running on i55:9003:

::

    [taklwu@i136 ~]$ lynx i55:9003

In addition, all the outputs will stored in the HDFS output directory
(e.g. HDFS\_blast\_output).

::

    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop fs -ls HDFS_blast_output
    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop fs -cat HDFS_blast_output/*
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|298916876|dbj|BAJ09735.1|    100.00  11      0       0       3       35      9       19      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|298708397|emb|CBJ48460.1|    100.00  11      0       0       3       35      37      47      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|298104210|gb|ADI54942.1|     100.00  11      0       0       3       35      11      21      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|297746593|emb|CBM42053.1|    100.00  11      0       0       3       35      11      21      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|297746591|emb|CBM42052.1|    100.00  11      0       0       3       35      11      21      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|297746589|emb|CBM42051.1|    100.00  11      0       0       3       35      11      21      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|297746587|emb|CBM42050.1|    100.00  11      0       0       3       35      11      21      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|297746585|emb|CBM42049.1|    100.00  11      0       0       3       35      11      21      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|297746583|emb|CBM42048.1|    100.00  11      0       0       3       35      11      21      7.0     27.7
    BG3:2_30MNAAAXX:7:1:981:1318/1  gi|297746581|emb|CBM42047.1|    100.00  11      0       0       3       35      11      21      7.0     27.7

    ...

5. Finishing the Map-Reduce process
-----------------------------------

After finishing the Job, please use the command to kill the HDFS and
Map-Reduce daemon:

::

    [taklwu@i55 hadoop-0.20.203.0]$ bin/stop-all.sh

Hadoop WordCount
================

| Number:
|  Author: Tak-Lon Stephen Wu
|  Improvements: 
|  Version: 0.1
|  Date: 2011-11-01

Hadoop WordCount
----------------

WordCount is a simple program which counts the number of occurrences of
each word in a given text input data set. WordCount fits very well with
the MapReduce programming model making it a great eample to understand
the Hadoop Map/Reduce programming style. You can download the `WordCount
source
code <http://salsahpc.indiana.edu/tutorial/source_code/Hadoop-WordCount.zip>`__
from `Big Data for Science
tutorial <http://salsahpc.indiana.edu/tutorial/hadoopwordcount.html>`__.

 
-

Acknowledge
-----------

| This page was original designed by
`SalsaHPC <http://salsahpc.indiana.edu/>`__ group for `Big Data for
Science Workshop <http://salsahpc.indiana.edu/tutorial/>`__, you can see
the original pages
`here <http://salsahpc.indiana.edu/tutorial/hadoopwordcount.html>`__.

Requirement
-----------

#. Login to FutureGrid Cluster and obtain compute nodes.
   (`HPC <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc#HPC_Nodes>`__/
   `Eucalyptus <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus>`__)
#. Start SalsaHadoop/Hadoop on compute nodes. (`SalsaHadoop
   Tutorial <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc#Configuration>`__)
#. Download and unzip `WordCount source
   code <http://salsahpc.indiana.edu/tutorial/source_code/Hadoop-WordCount.zip>`__
   from `Big Data for Science
   tutorial <http://salsahpc.indiana.edu/tutorial/hadoopwordcount.html>`__.
#. Linux command experience.

1. Download and unzip WordCount under $HADOOP\_HOME
---------------------------------------------------

| Assuming your start SalsaHadoop/Hadoop with setting
$HADOOP\_HOME=~/hadoop-0.20.203.0, and is running the master node on
i55. Then, we download and unzip the `WordCount source
code <http://salsahpc.indiana.edu/tutorial/source_code/Hadoop-WordCount.zip>`__
from  `Big Data for Science
tutorial <http://salsahpc.indiana.edu/tutorial/hadoopwordcount.html>`__
under $HADOOP\_HOME.

::

    [taklwu@i55 ~]$ cd $HADOOP_HOME
    [taklwu@i55 hadoop-0.20.203.0]$ wget http://salsahpc.indiana.edu/tutorial/source_code/Hadoop-WordCount.zip
    [taklwu@i55 hadoop-0.20.203.0]$ unzip Hadoop-WordCount.zip

2. Execute
----------

Hadoop-WordCount
----------------

First, we need to uplaod the input files (any text format file) into
Hadoop distributed file system (HDFS):

::

    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop fs -put $HADOOP_HOME/Hadoop-WordCount/input/ input
    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop fs -ls input

Here, $HADOOP\_HOME/Hadoop-WordCount/input/ is the local directory where
the program inputs are stored. The second "input" represents the remote
destination directory on the HDFS.

After uploading the inputs into HDFS, run the WordCount program with the
following commands. We assume you have already compiled the word count
program.

::

    [taklwu@i55 hadoop-0.20.203.0]$ bin/hadoop jar $HADOOP_HOME/Hadoop-WordCount/wordcount.jar WordCount input output

If Hadoop is running correctly, it will print hadoop running messages
similar to the following:

::

    WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    11/11/02 18:34:46 INFO input.FileInputFormat: Total input paths to process : 1
    11/11/02 18:34:46 INFO mapred.JobClient: Running job: job_201111021738_0001
    11/11/02 18:34:47 INFO mapred.JobClient:  map 0% reduce 0%
    11/11/02 18:35:01 INFO mapred.JobClient:  map 100% reduce 0%
    11/11/02 18:35:13 INFO mapred.JobClient:  map 100% reduce 100%
    11/11/02 18:35:18 INFO mapred.JobClient: Job complete: job_201111021738_0001
    11/11/02 18:35:18 INFO mapred.JobClient: Counters: 25
    ...

3. Monitoring Hadoop
--------------------

We can also monitor the job status using lynx, a text browser, on i136
based Hadoop monitoring console. Assuming the Hadoop Jobtracker is
running on i55:9003:

::

    [taklwu@i136 ~]$ lynx i55:9003

4. Check the result
-------------------

After finishing the Job, please use the command to check the output:

::

    [taklwu@i55 ~]$ cd $HADOOP_HOME
    [taklwu@i55 ~]$ bin/hadoop fs -ls output
    [taklwu@i55 ~]$ bin/hadoop fs -cat output/*

Here, "output" is the HDFS directory where the result stored. The result
will look like as following:

::

    you." 15
    you; 1
    you? 2
    you?" 23
    https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptusyoung 42

5. Finishing the Map-Reduce process
-----------------------------------

After finishing the Job, please use the command to kill the HDFS and
Map-Reduce daemon:

::

    [taklwu@i55 hadoop-0.20.203.0]$ bin/stop-all.sh

Using Twister on FutureGrid
===========================

| PLEASE NOTE: THIS MANUAL PAGE IS A DRAFT, PLEASE PROVIDE FEEDBACK IN
THE COMMENT SECTION.

What is Twister?
----------------

MapReduce programming model has simplified the implementations of many
data parallel applications. The simplicity of the programming model and
the quality of services provided by many implementations of MapReduce
attract a lot of enthusiasm among parallel computing communities. From
the years of experience in applying MapReduce programming model to
various scientific applications we identified a set of extensions to the
programming model and improvements to its architecture that will expand
the applicability of MapReduce to more classes of
applications. `Twister <http://www.iterativemapreduce.org/>`__ is a
lightweight MapReduce runtime we have developed by incorporating these
enhancements.

`Twister <http://www.iterativemapreduce.org/>`__ provides the following
features to support MapReduce computations. (Twister is developed as
part of \ `Jaliya
Ekanayake's <http://www.cs.indiana.edu/%7Ejekanaya/>`__ Ph.D. research
and is supported by
the \ **`S A L S  <http://salsahpc.indiana.edu/>`__**\ ****\ **`A <http://salsahpc.indiana.edu/>`__**\ Team
@ \ `IU <http://www.iub.edu/>`__)

+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image105|   | Distinction on static and variable data                                                                                                                                                                   |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image106|   | Configurable long running (cacheable) map/reduce tasks                                                                                                                                                    |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image107|   | Pub/sub messaging based communication/data transfers                                                                                                                                                      |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image108|   | Efficient support for Iterative MapReduce computations (extremely faster than\ `Hadoop <http://hadoop.apache.org/>`__ or `Dryad/DryadLINQ <http://research.microsoft.com/en-us/projects/DryadLINQ/>`__)   |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image109|   | Combine phase to collect all reduce outputs                                                                                                                                                               |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image110|   | Data access via local disks                                                                                                                                                                               |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image111|   | Lightweight (~5600 lines of Java code)                                                                                                                                                                    |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image112|   | Support for typical MapReduce computations                                                                                                                                                                |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image113|   | Tools to manage data                                                                                                                                                                                      |
+--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

|image114|
----------

Iterative MapReduce programming model using Twister

Running Twister on FutureGrid
-----------------------------

Twister can be run in various modes within FG either in FutureGrid HPC
and FutureGrid Cloud environment.

-  Twister on FutureGrid

   -  `Twister with FutureGrid
      HPC <https://portal.futuregrid.org/twister-futuregrid-hpc>`__

      -  `Get HPC compute
         nodes <https://portal.futuregrid.org/twister-futuregrid-hpc#HPC_Nodes>`__
      -  `Twister
         Configuration <https://portal.futuregrid.org/twister-futuregrid-hpc#Twister_Conf>`__

         -  `Download Twister
            0.9 <https://portal.futuregrid.org/twister-futuregrid-hpc#Twister_Conf_Download>`__
         -  `Set $TWISTER\_HOME and
            $JAVA\_HOME <https://portal.futuregrid.org/twister-futuregrid-hpc#Twister_Conf_Set>`__
         -  `Run
            TwisterPowerMakeUp.sh <https://portal.futuregrid.org/twister-futuregrid-hpc#Twister_Conf_PowerMakeUp>`__
         -  `Download and start ActiveMQ on specific
            nodes <https://portal.futuregrid.org/twister-futuregrid-hpc#Twister_Conf_ActiveMQ>`__
         -  `Start
            Twister <https://portal.futuregrid.org/twister-futuregrid-hpc#Twister_Conf_Start>`__

      -  `Verify Twister MapReduce Daemon
         status <https://portal.futuregrid.org/twister-futuregrid-hpc#Verify>`__

   -  `Twister with FutureGrid Cloud
      Eucalyptus <https://portal.futuregrid.org/twister-futuregrid-cloud-eucalyptus>`__

      -  `Get VM compute
         nodes <../../twister-futuregrid-cloud-eucalyptus#VM_Nodes>`__

         -  `VM Hostname
            setting <../../twister-futuregrid-cloud-eucalyptus#VM_Nodes_Set>`__
         -  `VM attached disk
            configuration <../../twister-futuregrid-cloud-eucalyptus#Euca_Disk>`__

      -  `Twister
         Configuration <../../twister-futuregrid-cloud-eucalyptus#Twister_Conf>`__

         -  `Download Twister
            0.9 <../../twister-futuregrid-cloud-eucalyptus#Twister_Conf_Download>`__
         -  `Set $TWISTER\_HOME,  $JAVA\_HOME and Worker
            Nodes <../../twister-futuregrid-cloud-eucalyptus#Twister_Conf_Set>`__
         -  `Run
            TwisterPowerMakeUp.sh <../../twister-futuregrid-cloud-eucalyptus#Twister_Conf_PowerMakeUp>`__
         -  `Download and start ActiveMQ on specific
            node <../../twister-futuregrid-cloud-eucalyptus#Twister_Conf_ActiveMQ>`__
         -  `Start
            Twister <../../twister-futuregrid-cloud-eucalyptus#Twister_Conf_Start>`__

      -  `Verify Twister MapReduce Daemon
         status <../../twister-futuregrid-cloud-eucalyptus#Verify>`__

   -  Run Twister Applications

      -  `Twister
         Kmeans <https://portal.futuregrid.org/twister-kmeans>`__
      -  `Twister Blast <https://portal.futuregrid.org/twister-blast>`__

Papers and Presentations
------------------------

+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image121|   | Jaliya Ekanayake, Hui Li, Bingjing Zhang, Thilina Gunarathne, Seung-Hee Bae, Judy Qiu, Geoffrey Fox, \ `Twister: A Runtime for Iterative MapReduce <http://www.iterativemapreduce.org/hpdc-camera-ready-submission.pdf>`__," The First International Workshop on MapReduce and its Applications (MAPREDUCE'10) - HPDC2010                                                                                                                |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image122|   | Jaliya Ekanayake, (Advisor: Geoffrey Fox) \ `Architecture and Performance of Runtime Environments for Data Intensive Scalable Computing <http://grids.ucs.indiana.edu/ptliupages/publications/SC09-abstract-jaliya-ekanayake.pdf>`__, Doctoral Showcase, SuperComputing2009. (`Presentation <http://www.slideshare.net/jaliyae/architecture-and-performance-of-runtime-environments-for-data-intensive-scalable-computing-2653554>`__)   |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image123|   | Jaliya Ekanayake, Atilla Soner Balkir, Thilina Gunarathne, Geoffrey Fox, Christophe Poulain, Nelson Araujo, Roger Barga, \ `DryadLINQ for Scientific Analyses <http://grids.ucs.indiana.edu/ptliupages/publications/eScience09-camera-ready-submission.pdf>`__, Fifth IEEE International Conference on e-Science (eScience2009), Oxford, UK.                                                                                             |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image124|   | Jaliya Ekanayake, Geoffrey Fox, \ `High Performance Parallel Computing with Clouds and Cloud Technologies <http://grids.ucs.indiana.edu/ptliupages/publications/cloud_handbook_final-with-diagrams.pdf>`__, First International Conference on Cloud Computing (CloudComp09) Munich, Germany, 2009.                                                                                                                                       |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image125|   | Geoffrey Fox, Seung-Hee Bae, Jaliya Ekanayake, Xiaohong Qiu, and Huapeng Yuan,\ `Parallel Data Mining from Multicore to Cloudy Grids <http://grids.ucs.indiana.edu/ptliupages/publications/CetraroWriteupJan09_v12.pdf>`__, High Performance Computing and Grids workshop, 2008.                                                                                                                                                         |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image126|   | Jaliya Ekanayake, Shrideep Pallickara, and Geoffrey Fox \ `MapReduce for Data Intensive Scientific Analysis <http://www.cs.indiana.edu/%7Ejekanaya/papers/eScience-final.pdf>`__, Fourth IEEE International Conference on eScience, 2008, pp.277-284.                                                                                                                                                                                    |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 

Twister Blast
=============

| Number:
|  Author: Yang Ruan
|  Improvements: 
|  Version: 0.1
|  Date: 2011-11-07

Twister Blast
-------------

BLAST (Basic Local Alignment Search Tool) is one of the most widely used
bioinformatics applications written in C++, and the version we are using
is v2.2.23. `Twister <http://www.iterativemapreduce.org/>`__\ is an
iterative mapreduce framework which can be used both for iterative and
non-iterative applications. Twister Blast is an advanced Twister program
which helps Blast, a bioinformatics application, utilizes the Computing
Capability of Twister. With the flexibility of Twister run-time
environment, this application can run on a single machine, a cluster, or
Amazon EC2 cloud platform.

Twister-BLAST can divide original query file into small chunks, and
distribute them to all available computing nodes. Twister-BLAST manages
and schedules Map tasks to process each query chunk based on its
location. Output can also be collected by Twister-BLAST. Compared with
other parallel BLAST applications, Twister-BLAST is efficient and with
little overhead.

You can download the\ `Twister
Blast <http://salsahpc.indiana.edu/tutorial/apps/twister-blast.tar.gz>`__
Source code and customized Blast program and Database archive
(`BlastProgramAndDB.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`__)
from `Big Data for Science
tutorial <http://salsahpc.indiana.edu/tutorial/hadoopblast.html>`__.

 
-

Acknowledge
-----------

| This page was original designed by
`SalsaHPC <http://salsahpc.indiana.edu/>`__ group for `Big Data for
Science Workshop <http://salsahpc.indiana.edu/tutorial/>`__, you can see
the original pages `here <http://salsahpc.indiana.edu/tutorial/>`__.

Requirement
-----------

#. Login to FutureGrid Cluster and obtain compute nodes.
   (`HPC <../../salsahadoop-futuregrid-hpc#HPC_Nodes>`__/
   `Eucalyptus <../../salsahadoop-futuregrid-cloud-eucalyptus>`__)
#. Start Twister on compute nodes. (`SalsaTwister
   Tutorial <http://salsahpc.indiana.edu/tutorial/twister-intro.html>`__)
#. Download and unzip `Twister
   Blast <http://salsahpc.indiana.edu/tutorial/apps/twister-blast.tar.gz>`__
   Source code.
#. Download customized Blast binary and Database archive
   `BlastProgramAndDB.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`__
#. Linux command experience.

1. Download and prepare the
---------------------------

Twister-Blast
-------------

| First, Download and unzip the `Twister
Blast <http://salsahpc.indiana.edu/tutorial/apps/twister-blast.tar.gz>`__
package (named as $TWISTER\_BLAST\_PROGRAM here), then ​copy the
unzipped ​$TWISTER\_BLAST\_PROGRAM/blast/dist/Twister-Blast.jar to the
$TWISTER\_HOME/apps. Also, we download and unzip the blast program and
the database
`here <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`__,
and set $BLAST\_HOME=/path/to/BlastProgramAndDB/. Go to
$TWISTER\_BLAST\_PROGRAM/blast/bin/, in **twister\_blast.properties**,
set the BLAST+ execution command (execmd property)  to the BLAST program
(blastx) under $BLAST\_HOME/bin/. Execution options can be reset
according to users' needs. However, Input option (-query) and output
option (-out) are not set in execmd but in inop and outop in order to be
compatible with both BLAST+ and BLAST. Twister-BLAST will merge these
command options by itself when invoking BLAST+ parallel.
|  The execution command template inside\ **twister\_blast.properties**
is given below.

::

    execmd = time /N/u/yangruan/Quarry/workflow/ncbi-blast-2.2.23+/bin/blastp -db /N/dc/scratch/yangruan/blast/db/cog/10k/cog.10000 -evalue 100 -max_target_seqs 1000000 -num_alignments 1000000 -outfmt 6 -seg no
    inop = -query
    outop = -out

2. Prepare Twister-Blast input
------------------------------

Assume you have already download the input fasta file into some location
called [input file path]. Use the
$TWISTER\_BLAST\_PROGRAM/blast/bin/blastNewFileSpliter.sh to split the
input fasta file into multiple partitions. The parameters in as
following:

::

    args:  [query_file] [sequence_count]  [num_partition] [data_dir] [output_prefix] [output_map_file]

-  query\_file: input fasta file
-  sequence\_count: sequence count in the input fasta file
-  num\_partition: number of partitions, this number should be larger or
   equal to the total worker number started with twister
-  data\_dir: The output folder of partitioned fasta files
-  output\_prefix: The output prefix of partitioned fasta files
-  output\_map\_file: The file contains the information of all the
   partitions width and height.

3. Execute Twister-Blast
------------------------

After deploying those required files onto file system, run the
twister-Blast program with the following commands:

::

    ./blastNew.sh 128 /N/dc/scratch/yangruan/fasta/cog/10000/400/ input_ .fa 400 /N/dc/scratch/yangruan/blast/result/cog/10k/eval_100_400p/ blastOut_

Here is the description of the above command:

::

    args:  [map number] [input folder] [input prefix] [input postfix (None for none)] [partition number] [output folder] [output prefix]

+--------------------+-----------------------------------------------------------------------------+
| **Parameter**      | **Description**                                                             |
+--------------------+-----------------------------------------------------------------------------+
| map number         | The map task number (usually equals to the number of worker started)        |
+--------------------+-----------------------------------------------------------------------------+
| input folder       | The folder of input fasta file partitions                                   |
+--------------------+-----------------------------------------------------------------------------+
| input prefix       | The prefix of input fasta file partitions                                   |
+--------------------+-----------------------------------------------------------------------------+
| input postfix      | The postfix (file extension) of input fasta file partitions (default .fa)   |
+--------------------+-----------------------------------------------------------------------------+
| partition number   | The number of input fasta file partitions                                   |
+--------------------+-----------------------------------------------------------------------------+
| output folder      | The folder to store output blast result                                     |
+--------------------+-----------------------------------------------------------------------------+
| output prefix      | The prefix of output blast result                                           |
+--------------------+-----------------------------------------------------------------------------+

| 
|  If Twister Blast is running correctly, it will print twister running
messages similar to the following:

::

    ./blastNew.sh 128 /N/dc/scratch/yangruan/fasta/cog/10000/400/ input_ .fa 400 /N/dc/scratch/yangruan/blast/result/cog/10k/eval_100_400p/ blastOut_ 
    time /N/u/yangruan/Quarry/workflow/ncbi-blast-2.2.23+/bin/blastp -db /N/dc/scratch/yangruan/blast/db/cog/10k/cog.10000 -evalue 100 -max_target_seqs 1000000 -num_alignments 1000000 -outfmt 6 -seg no
    -query
    -out
    JobID: BlastNewac4d15a9-0997-11e1-81b4-5b7f60de01d2
    Nov 7, 2011 11:24:43 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://149.165.229.100:61616
    0    [main] INFO  cgl.imr.client.TwisterDriver  - MapReduce computation termintated gracefully.
    Total Time of BLAST : 28.12Seconds
    2    [Thread-1] DEBUG cgl.imr.client.ShutdownHook  - Shutting down completed.

4. Finishing the Map-Reduce process
-----------------------------------

After finishing the Job, please use the command to kill the Map-Reduce
daemon and broker:

::

    $TWISTER_HOME/bin/stop_twister.sh

| 

Eucalyptus and Twister on FutureGrid
====================================

The FutureGrid Twister Tutorial
===============================

| SALSA Group
|  PTI Indiana University

 

I. Introduction
~~~~~~~~~~~~~~~

| This tutorial will show you how to use Twister under Eucalyptus on
India, FutureGrid.
|   

II. Prerequisite
~~~~~~~~~~~~~~~~

| Follow tutorial `Using Eucalyptus on
FutureGrid <http://portal.futuregrid.org/tutorials/eucalyptus>`__ to
learn how to install and use the Eucalyptus client tool to access
resources on India, FutureGrid.
|   

III. Download FutureGrid Eucalyptus Twister Tool 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| This tool is a set of python scripts. They can provide a
pre-configured Twister environment, and also can terminate the
environment. Please 
|  download the tool in the attachment below.

 IV. Start Twister Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To start a Twister environment, execute the following program: 

.. code:: rteleft

    $ python fg_euca_start_twister.py [-k user key] [-i public key file path] [-n number of instances][-t instance type]

    e.g.
    $ python fg_euca_start_twister.py -k userkey -i userkey.pem -n 3 -t c1.medium

| 
|  Here,

-  -k is the user key name generated by the **euca-add-keypair** step in
   the Eucalyptus tutorial.
-  -i  is the private key .pem file path. It is also generated in the
   **euca-add-keypair** step in the Eucalyptus tutorial.
-  -n is the number of instances for starting.
-  -t  is the type of image.

| The following is an execution example:
|  |image127|
| 
|  Once the script is executed, the user can get a prepared Twister
environment.
|  Then, the user can follow the instructions provided by
**fg\_euca\_start\_twister.py** to start ActiveMQ on the assigned node,
|  and also start the Twister environment (could be on any node just
applied).
|   

V. Terminate Twister Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To terminate a Twister environment, execute the following command:

.. code:: rteleft

    $ python fg_euca_terminate_twister.py

 

VI. Run Twister-Kmeans
~~~~~~~~~~~~~~~~~~~~~~

1. Ant and Deploy Twister-Kmeans
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Log into the node assigned for ActiveMQ broker. 

::

    $ cd /opt/Twister/samples/kmeans
    $ ant
    $ cd ../../lib
    $ mv Twister-Kmeans-0.9.jar ../apps/
    $ cd ../bin/
    $ chmod a+x twister.sh
    $ ./twister.sh cpj ../apps/Twister-Kmeans-0.9.jar

2. Start Twister and ActiveMQ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Open two terminals and log into the node mentioned above. One is for
starting ActiveMQ; the other is for starting Twister.
| 
|  In Terminal 1:

::

    $ cd /opt/apache-activemq-5.4.2/bin/
    $ activemq console

In Terminal 2: 

::

    $ cd /opt/Twister/bin
    $ ./start_twister.sh  

 

3. Create Twister-Kmeans Data Folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open another terminal, and create a folder for operating kmeans data:

::

    $ cd /opt/Twister/bin
    $ ./twishter.sh mkdir kmeans 

4. Generate Twister-Kmeans
^^^^^^^^^^^^^^^^^^^^^^^^^^

 
^

 
^

Data
^^^^

Open a new terminal:

::

    $ cd /opt/Twister/samples/kmeans/bin/
    $./gen_data.sh init_clusters.txt 2 3 /kmeans km_data 3 30000

In the terminal used in Step 3, do the following:

::

    $ ./create_partition_file.sh kmeans km ../samples/kmeans/bin/p.pf

| Back in the terminal used in Step 4, do the following:

::

    $ ./run_kmeans.sh init_clusters.txt 3 p.pf

 

The output is as follows:

|image128|

+-----------------------------------------------------------------------------------------------+-----------+
| Attachment                                                                                    | Size      |
+===============================================================================================+===========+
| `fgeucatwister.zip <https://portal.futuregrid.org/sites/default/files/fgeucatwister.zip>`__   | 4.38 KB   |
+-----------------------------------------------------------------------------------------------+-----------+

Using Pegasus on FutureGrid
===========================

About Pegasus
-------------

`Pegasus WMS <http://pegasus.isi.edu>`__ is a configurable system for
mapping and executing abstract application workflows over a wide range
of execution environments including a laptop, a campus cluster, a Grid,
or a commercial or academic cloud. One Pegasus workflow can run on a
single system or across a heterogeneous set of resources. Pegasus can
run workflows ranging from just a few computational tasks up to 1
million.

Pegasus has a number of features that contribute to its usability and
effectiveness, as explained in detail in the tutorial and the `Pegasus
online
documentation <https://pegasus.isi.edu/wms/docs/4.0/about.php#overview>`__.
Among the key feature rank abstract workflow portability between
environments, features to better control workflow performance and
resource utilization, scalability, data provenance tracking, data
management, error recovery and multiple operating environments not
limited to clouds.

The main mode of operation of Pegasus on FutureGrid is the usage of IaaS
clouds, as provided by Nimbus, OpenStack, Eucalyptus and bare-metal
(future).

If you want to find out more about Pegasus WMS, please `visit our web
site. <http://pegasus.isi.edu>`__ The liaison for FutureGrid is Jens
Vöckler. He is available as "Expert" on the Portal. If you have general
questions concerning Pegasus, not related to FutureGrid, you may want to
contact

pegasus-support <pegasus-support at isi dot edu>

The Pegasus Run-Time Cloud Architecture
---------------------------------------

| Pegasus uses the `Condor high-throughput scheduling
system <http://research.cs.wisc.edu/condor/>`__ to provide the work of
executing a plan created by Pegasus from the abstract workflow
description.

| |Cloud site sample layouts.|
|  **Figure:** Cloud Site Layouts example.

| The figure above shows two cloud sites, typically two distinct IaaS
clouds, with two virtual machines (VMs) running in each site. 
Effectively, it shows a sample layout for sky computing (as in: multiple
clouds) as supported by Pegasus. At this point, it is up to the user to
provision the remote resources with a proper VM image that includes a
Condor *startd* and proper Condor configuration to report back to a
Condor *collector* that the Condor *schedd* has access to.

The submit host is the point where a user submits Pegasus workflows for
execution. In this discussion, the *submit host* (SH) is located
logically external to the cloud provider(s) in order to bridge multiple
clouds. In contrast, the tutorial uses a submit host that is located
within a single cloud site. The site where the SH is located typically
runs a Condor *collector* to gather resource announcements, or is part
of a larger Condor pool that collects these announcement. Condor makes
the remote resources available to the submit host's Condor installation.

The figure above shows the way Pegasus WMS is deployed in cloud
computing resources, ignoring how these resources were provisioned. The
provisioning request shows multiple resources per provisioning request.

| The provisioning broker -- Nimbus, Eucalyptus or EC2 -- is responsible
to allocate and set up the resources. Please note that each provisioning
broker comes with its own set of client tools that may be executed
either on your laptop or desktop in front of you, or from a FutureGrid
login node. The FutureGrid tutorials for the various IaaS services have
details on their client tools and usage.
| 
|  For a multi-node request, the worker nodes often require access to a
form of shared data storage. Concretely, either a POSIX-compliant shared
file system (e.g. NFS, PVFS) is available to the nodes, or can be
brought up for the lifetime of the application workflow. The task steps
of the application workflow facilitate shared file systems to exchange
intermediary results between tasks on the same cloud site. Pegasus also
supports an S3 data mode for the application workflow data staging. As
of Pegasus 4.0, it more easily supports non-shared file system execution
where each worker node uses only its own storage.

The initial stage-in and final stage-out of application data into and
out of the node set is part of any Pegasus-planned workflow. Several
configuration options exist in Pegasus to deal with the dynamics of push
and pull of data, and when to stage data. In many use-cases, some form
of external access to or from the shared file system that is visible to
the application workflow is required to facilitate successful data
staging. However, Pegasus is prepared to deal with a set of boundary
cases.

The data server in the figure is shown at the submit host. This is *not
a strict requirement*. The data server for consumed data (input data)
and data products (output data) may both be different and external to
the submit host.

Once worker nodes (resources) begin appearing in the pool managed by the
submit host's Condor *collector*, the application workflow, as planned
by Pegasus, can be submitted to Condor. A Condor *DAGMan* will manage
the application workflow execution. Pegasus run-time tools obtain
timing-, performance and provenance information as the application
workflow is executed. In the cloud and FutureGrid scenario, it is the
user's responsibility to de-provision the allocated resources.

In the figure, the cloud resources on the right side are assumed to have
uninhibited outside connectivity. This enables the Condor I/O to
communicate directly with the resources. The right side includes a setup
where the worker nodes use all private IP, but have out-going
connectivity and a NAT router to talk to the internet. The *Condor
connection broker* (CCB) facilitates this setup almost effortlessly.

The left side shows a more difficult setup where the connectivity is
fully firewalled without any connectivity except to in-site nodes. In
this case, a proxy server process, the *generic connection broker*
(GCB), needs to be set up in the de-militarized zone (DMZ) of the cloud
site's firewall to facilitate Condor I/O between the submit host and
worker nodes.

If the cloud supports data storage servers, Pegasus 4.0 is starting to
support workflows that require staging in two steps: Consumed data is
first staged to a data server in the remote site's DMZ, and then a
second staging task moves the data from the data server to the worker
node where the job runs. For staging out, data needs to be first staged
from the job's worker node to the site's data server, and possibly from
there to another data server external to the site. Pegasus is capable to
plan both steps: Normal staging to a remote site's data server, and the
worker-node staging from and to the site's data server as part of the
job. We are working on expanding the current code to support a more
generic set in the newly released Pegasus 4.0.

Using Pegasus on FutureGrid
---------------------------

The Pegasus tutorial for FutureGrid is forthcoming shortly. You are
welcome to `review the "Using Pegasus In FutureGrid"
tutorial <http://pegasus.isi.edu/futuregrid/tutorials/>`__ which makes
use of one of the following Virtual Machines:

+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| **IaaS**     | **Resource**   | **Image Name**                               | **CentOS**   | **PWMS**   | **Condor**   | **Globus**   | **Mntge**   |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Nimbus       | alamo          | pegasus-tutorial.x64.kvm.gz                  | 5.7          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Nimbus       | hotel          | pegasus-tutorial.x64.gz                      | 5.7          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Nimbus       | foxtrot        | pegasus-tutorial.x64.gz                      | 5.7          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Nimbus       | sierra         | pegasus-tutorial.x64.gz                      | 5.7          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Eucalyptus   | sierra         | tutorial/pegasus-tutorial.x64.manifest.xml   | 5.8          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Eucalyptus   | india          | pegasus/pegasus-tutorial.x64.manifest.xml    | 5.8          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| OpenStack    | india          | pegasus/pegasus-tutorial.x64.manifest.xml    | 5.8          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+

The table above shows the available Pegasus Virtual Machines you can use
to try out Pegasus. At this point, the Nimbus-based VMs are are
preferred.

Management Services
===================

FutureGrid contains a number of interresting management services. This
includes image management services to deploy and provision images onto
bare metal or virtualized machines as well as experiment management that
allows the creation of easy to use workflows to run repeatable
experiments on FutureGrid. These services are curently under development
and you are welcome to join the development teams by contacting
`laszewski@gmail.com <mailto:laszewski@gmail.com>`__

Nimbus Phantom
==============

| Nimbus Phantom is a hosted service, running on FutureGrid, that makes
it easy to leverage on-demand resources provided by infrastructure
clouds. Phantom allows the user to deploy a set of virtual machines over
multiple private, community, and commercial clouds and then
automatically grows or shrinks this set based on policies defined by the
user. This elastic set of virtual machines can then be used to implement
scalable and highly available services. An example of such service is a
caching service that stands up more workers on more resources as the
number of requests to the service increases. Another example is a
scheduler that grows its set of resources as demand grows.
| 
|  Currently Phantom works with all FutureGrid Nimbus and OpenStack
clouds as well as Amazon and the XSEDE wispy cloud (the only XSEDE cloud
for now). A user can access it via two types of clients: an easy to use
web application and a scripting client. The scripting client is the boto
autoscale client as Phantom currently implements Amazon Autscaling API –
so you can think of it as Amazon Autoscale for FutureGrid clouds that
also allows for cloudburst to XSEDE and commercial clouds and is easy to
extend with your own policies and sensors.
| 
|  The simplest scenario for using Phantom is as a gateway for deploying
and monitoring groups of virtual machines spread over multiple
FutureGrid clouds. In a more complex scenario you can use it to
cloudburst from FutureGrid clouds to Amazon. Finally, you can use it to
explore policies that will automate cloudbursting and VM allocations
between multiple clouds.
| 
|  For more information and/or to use the service go to
`www.nimbusproject.org/phantom <http://www.nimbusproject.org/phantom>`__.
It should take no more than 10-15 minutes to start your own VMs.

-  `Phantom web
   interface <https://phantom.nimbusproject.org/accounts/login/?next=/>`__
-  `Phantom
   publication <http://www.nimbusproject.org/files/keahey_wcs_ocs_2012.pdf>`__

Precip - Pegasus Repeatable Experiments for the Cloud in Python
===============================================================

 

Overview
--------

Precip is a flexible exeperiment management API for running experiments
on clouds. Precip was developed for use on FutureGrid infrastructures
such as OpenStack, Eucalyptus (>=3.2), Nimbus, and at the same time
commercial clouds such as Amazon EC2. The API allows you to easily
provision resources, which you can then can run commands on and copy
files to/from subsets of instances identified by tags. The goal of the
API is to be flexible and simple to use in Python scripts to control
your experiments.

The API does not require any special images, which makes it easy to get
going. Any basic Linux image will work. More complex images can be used
if your experiment requires so, or you can use the experiment API to run
bootstrap scripts on the images to install/configure required software.

A concept which simplfies interacting with the API is instance tagging.
When you start an instance, you can add arbitrary tags to it. The
instance also gets a set of default tags. API methods such as running a
remote command, or copying files, all use tags for specify which
instances you want to target.

Precip also handles ssh keys and security groups automatically. This is
done to make sure the experiment management is not interfering with your
existing cloud setup. The first time you use Precip, a directory will be
created called ~/.precip. Inside this directory, a ssh keypair will be
created and used for accessing instances. On clouds which supports it,
the keypair is automatically registered as 'precip', and a 'precip'
security group is created. If your experiement requires more ports to be
open you can use the cloud interface to add those ports to the precip
security group.

Precip is a fairly new API, and if you have questions or suggestions for
improvements, please contact
`pegasus-support@isi.edu <mailto:pegasus-support@isi.edu>`__

Installation
------------

| If you want to use the India or Sierra FutureGrid resources to manage
your experiment, Precip is available on the interactive logins nodes via
modules: module load precip/0.1
| 
|  You can also install Precip on your own machine. Prerequisites are
the Paramiko and Boto Python modules. The Python source package and RPMs
are available at:
`http://pegasus.isi.edu/static/precip/software/ <http://pegasus.isi.edu/static/precip/software/>`__

API
---

**provision(image\_id, instance\_type='m1.small', count=1, tags=None)**
    Provision a new instance. Note that this method starts the
    provisioning cycle, but does not block for the instance to finish
    booting. For blocking on instance creation/booting, see wait()

    Parameters:

    -  **image\_id** - the id of the image to instanciate

    -  **instance\_type** - the type of instance. This is infrastructure
       specific, but usually follows the Amazon EC2 model with m1.small,
       m1.large, and so on.

    -  **count** - number of instances to create

    -  **tags** - these are used to manipulate the instance later. Use
       this to create logical groups of your instances.

**wait(tags=[], timeout=600)**
    Barrier for all instances matching the tags argument. This method
    will block until the instances have finish booting and are
    accessible via their external hostnames.

    Parameters:

    -  **tags** - tags specifying the subset of instances to block on.
       The default value is [] which means wait for all instances.

    -  **timeout** - timeout in seconds for the instances to boot. If
       the timeout is reached, an ExperimentException is raised. The
       default is 600 seconds.

**deprovision(tags)**
    Deprovisions (terminates) instances matching the tags argument

    Parameters:

    -  **tags** - tags specifying the subset of instances to
       deprovision.

**list(tags)**
    Returns a list of details about the instances matching the tags. The
    details include instance id, hostnames, and tags.

    Parameters:

    -  **tags** - tags specifying the subset of instances to give
       information on. If you want details on all current instances, use
       [].

    Returns:

    -  List of dictionaries, one for each instance.

**get\_public\_hostnames(tags)**
    Provides a list of public hostnames for the instances matching the
    tags. The public hostnames can be provided to other instances in
    order to let the instances know about eachother.

    Parameters:

    -  **tags** - tags specifying the subset of instances.

    Returns:

    -  A list of public hostnames

**get\_private\_hostnames(tags)**
    Provides a list of private hostnames for the instances matching the
    tags. The private hostnames can be provided to other instances in
    order to let the instances know about eachother.

    Parameters:

    -  **tags** - tags specifying the subset of instances.

    Returns:

    -  A list of private hostnames

**get(tags, remote\_path, local\_path, user="root")**
    Transfers a file from a set of remote machines matching the tags,
    and stores the file locally. If more than one instance matches the
    tags, an instance id will be appended to the local\_path.

    Parameters:

    -  **tags** - these are used to manipulate the instance later. Use
       this to create logical groups of your instances.

    -  **remote\_path** - the path of the file on the remote instance

    -  **local\_path** - the local path to tranfer to

    -  **user** - remote user. If not specified, the default is 'root'

**put(tags, local\_path, remote\_path, user="root")**
    Transfers a local file to a set of remote machines matching the
    tags.

    Parameters:

    -  **tags** - these are used to manipulate the instance later. Use
       this to create logical groups of your instances.

    -  **local\_path** - the local path to tranfer from

    -  **remote\_path** - the path on the remote instance to store the
       file as

    -  **user** - remote user. If not specified, the default is 'root'

**run(tags, cmd, user="root", check\_exit\_code=True)**
    Runs a command on the instances matches the tags. The commands are
    run in series, on one instance after the other.

    Parameters:

    -  **tags** - these are used to manipulate the instance later. Use
       this to create logical groups of your instances.

    -  **cmd** - the command to run

    -  **user** - remote user. If not specified, the default is 'root'.
       If you need to run commands as another user, you will have to
       make sure that user accepts the ssh key in ~/.precip/

    -  **check\_exit\_code** - If set to True (default), commands
       returning non-zero exit codes will result in a
       ExperimentException being raised.

    Returns:

    -  A list of lists, containing exit\_code[], stdout[] and stderr[]
       for the commands run

**copy\_and\_run(tags, local\_script, args=[], user="root",
check\_exit\_code=True)**
    Copies a script from the local machine to the remote instances and
    executes the script. The script is run in series, on one instance
    after the other.

    Parameters:

    -  **tags** - these are used to manipulate the instance later. Use
       this to create logical groups of your instances.

    -  **local\_script** - the local script to run

    -  **args** - arguments for the script

    -  **user** - remote user. If not specified, the default is 'root'.
       If you need to run commands as another user, you will have to
       make sure that user accepts the ssh key in ~/.precip/

    -  **check\_exit\_code** - If set to True (default), commands
       returning non-zero exit codes will result in a
       ExperimentException being raised.

    Returns:

    -  A list of lists, containing exit\_code[], stdout[] and stderr[]
       for the commands run

The basic methods above are standard across all the Cloud
infrastructures. What is different is the constructors as each
infrastructure handles initialization a little bit different. For
example, to create a new OpenStack using the EC2\_\* environment
provided automatically by FutureGrid:

.. code:: programlisting

                
        exp = OpenStackExperiment(
                os.environ['EC2_URL'],
                os.environ['EC2_ACCESS_KEY'],
                os.environ['EC2_SECRET_KEY'])
                
            

i For Amazon EC2, you have to specify region, endpoint, and
access/secret keys. Note that it is not required to use environment
variables for your credentials, but seperating the crenditals from the
code prevents the credentials from being check in to source control
systems.

.. code:: programlisting

                
        exp = EC2Experiment(
                "us-west-2c",
                "ec2.us-west-2.amazonaws.com",
                os.environ['AMAZON_EC2_ACCESS_KEY'],
                os.environ['AMAZON_EC2_SECRET_KEY'])
                
            

Examples
--------

Hello World
~~~~~~~~~~~

.. code:: programlisting

                    
    #!/usr/bin/python

    import os
    import time
    from pprint import pprint

    from precip import *

    exp = None

    # Use try/except liberally in your experiments - the api is set up to
    # raise ExperimentException on most errors
    try:

        # Create a new OpenStack based experiment. In this case we pick
        # up endpoints and access/secret cloud keys from the environment
        # as exposing those is the common setup on FutureGrid
        exp = OpenStackExperiment(
                os.environ['EC2_URL'],
                os.environ['EC2_ACCESS_KEY'],
                os.environ['EC2_SECRET_KEY'])

        # Provision an instance based on the ami-0000004c. Note that tags are
        # used throughout the api to identify and manipulate instances. You 
        # can give an instance an arbitrary number of tags.
        exp.provision("ami-0000004c", tags=["test1"], count=1)

        # Wait for all instances to boot and become accessible. The provision
        # method only starts the provisioning, and can be used to start a large
        # number of instances at the same time. The wait method provides a 
        # barrier to when it is safe to start the actual experiment.
        exp.wait()

        # Print out the details of the instance. The details include instance id,
        # private and public hostnames, and tags both defined by you and some
        # added by the api
        pprint(exp.list())
       
        # Run a command on the instances having the "test1" tag. In this case we
        # only have one instance, but if you had multiple instances with that
        # tag, the command would run on each one.
        exp.run(["test1"], "echo 'Hello world from a experiment instance'")

    except ExperimentException as e:
        # This is the default exception for most errors in the api
        print "ERROR: %s" % e

    finally:
        # Be sure to always deprovision the instances we have started. Putting
        # the deprovision call under finally: make the deprovisioning happening
        # even in the case of failure.
        if exp is not None:
            exp.deprovision()
                    
                

Resources from mulitple infrastructures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: programlisting

                    
    #!/usr/bin/python

    import os
    import time

    from precip import *

    ec2 = None
    fg = None

    try:

        # This example show how to run an experiment between Amazon EC2
        # and an OpenStack resource on FutureGrid. The setup is pretty
        # similar to the HelloWorld example, except that we now have to
        # experiment to handle. The first step is to get the experiments
        # initialized. Note that it is not required to use environment
        # variables for your credentials, but seperating the crenditals
        # from the code prevents the credentials from being check in to
        # source control systems.
        
        ec2 = EC2Experiment(
                "us-west-2c",
                "ec2.us-west-2.amazonaws.com",
                os.environ['AMAZON_EC2_ACCESS_KEY'],
                os.environ['AMAZON_EC2_SECRET_KEY'])
       
        fg = OpenStackExperiment(
                os.environ['EC2_URL'],
                os.environ['EC2_ACCESS_KEY'],
                os.environ['EC2_SECRET_KEY'])

        # Next we provision two instances, one on Amazon EC2 and one of
        # FutureGrid
        ec2.provision("ami-8a1e92ba", tags=["id=ec2_1"])
        fg.provision("ami-0000004c", tags=["id=fg_1"])

        # Wait for all instances to boot and become accessible. The provision
        # method only starts the provisioning, and can be used to start a large
        # number of instances at the same time. The wait method provides a 
        # barrier to when it is safe to start the actual experiment.
        ec2.wait([])
        fg.wait([])
        
        # Run commands on the remote instances
        ec2.run([], "echo 'Hello world Amazon EC2'")
        fg.run([], "echo 'Hello world FutureGrid OpenStack'")

    except ExperimentException as e:
        # This is the default exception for most errors in the api
        print "ERROR: %s" % e
        raise e
    finally:
        # Be sure to always deprovision the instances we have started. Putting
        # the deprovision call under finally: make the deprovisioning happening
        # even in the case of failure.
        if ec2 is not None:
            ec2.deprovision([])
        if fg is not None:
            fg.deprovision([])
                    
                

Setting up a Condor pool and run a Pegasus workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a more complex example in which a small Condor pool is set up
and then a Pegasus workflow is run and benchmarked. The Precip script is
similar to what we have seen before, but it has two groups of instances,
one master acting as the Condor central manager, and a set of Condor
worker nodes.

.. code:: programlisting

                    
    #!/usr/bin/python

    import os
    import time

    from precip import *

    try:

        # This experiment is targeted to run on OpenStack
        exp = OpenStackExperiment(
                os.environ['OPENSTACK_URL'],
                os.environ['OPENSTACK_ACCESS_KEY'],
                os.environ['OPENSTACK_SECRET_KEY'])

        # We need a master Condor node and a set of workers
        exp.provision("ami-0000004c", tags=["master"],
                      instance_type="m1.large")
        exp.provision("ami-0000004c", tags=["compute"],
                      instance_type="m1.large", count=2)
        exp.wait()

        # The workers need to know what the private hostname of the master is
        master_priv_addr = exp.get_private_hostnames(["master"])[0]

        # Bootstrap the instances. This includes installing Condor and Pegasus,
        # downloading and settup the workflow.
        exp.copy_and_run(["master"], "./bootstrap.sh")
        exp.copy_and_run(["compute"], "./bootstrap.sh", args=[master_priv_addr])

        # Give the workers some time to register with the Condor central 
        # manager
        time.sleep(60)

        # Make sure Condor came up correctly
        exp.run(["master"], "condor_status")

        # Run the workflow
        exp.run(["master"], "cd ~/montage && ./run-montage", user="wf")

        # At this point, in a real experiment, you could for example provision
        # more resources and run the workflow again, or run the workflow with
        # different parameters/settings.

    except ExperimentException as e:
        print "ERROR: %s" % e
    finally:
        # always want to clean up all the instances we have started
        exp.deprovision([])
                    
                

We also need a bootstrap.sh which sets up the instances:

.. code:: programlisting

                    
    #!/bin/bash

    # This script bootstraps a basic RHEL6 instance to be have working
    # Condor and Pegasus installs. The script takes one optional
    # argument which is the address of the master instance (central
    # manager in Condor terminology). If the argument is not given,
    # the script sets up the instance to be the master.

    MASTER_ADDR=$1

    # for images with condor already installed, stop condor
    /etc/init.d/condor stop >/dev/null 2>&1 || /bin/true

    # correct clock is important for most projects
    yum -q -y install ntpdate
    /etc/init.d/ntpdate start

    # Add the EPEL repository
    wget -nv http://mirror.utexas.edu/epel/6/x86_64/epel-release-6-7.noarch.rpm
    rpm -Uh epel-release-*.noarch.rpm

    # Add the Condor repository
    cat >/etc/yum.repos.d/condor.repo <<EOF
    [condor-stable]
    name=Condor Stable RPM Repository for Redhat Enterprise Linux 6
    baseurl=http://www.cs.wisc.edu/condor/yum/stable/rhel6
    enabled=1
    gpgcheck=0
    EOF

    # Add the Pegasus repository
    cat >/etc/yum.repos.d/pegasus.repo <<EOF
    [Pegasus]
    name=Pegasus
    baseurl=http://download.pegasus.isi.edu/wms/download/rhel/6/x86_64
    gpgcheck=0
    enabled=1
    priority=50
    EOF

    # Install required software
    yum -q -y clean all
    yum -q -y install gcc gcc-g++ gcc-gfortran make gawk bison diffutils \
                      java-1.7.0-openjdk.x86_64 \
                      java-1.7.0-openjdk-devel.x86_64 \
                      ganglia-gmond condor pegasus

    # Clear the Condor local config file - we use config.d instead
    cat /dev/null >/etc/condor/condor_config.local

    # Common Condor config between master and workers
    cat >/etc/condor/config.d/50-main.conf <<EOF

    CONDOR_HOST = $MASTER_ADDR

    FILESYSTEM_DOMAIN = \$(FULL_HOSTNAME)
    TRUST_UID_DOMAIN = True

    DAEMON_LIST = MASTER, STARTD

    # security
    ALLOW_WRITE = 10.*
    ALLOW_READ = \$(ALLOW_WRITE)

    # default policy
    START = True
    SUSPEND = False
    CONTINUE = True
    PREEMPT = False
    KILL = False

    EOF

    # Master gets extra packages/configs
    if [ "x$MASTER_ADDR" = "x" ]; then
        yum -q -y install ganglia-gmetad ganglia-web

        cat >/etc/condor/config.d/90-master.conf <<EOF
    CONDOR_HOST = \$(FULL_HOSTNAME)
    DAEMON_LIST = MASTER, COLLECTOR, NEGOTIATOR, SCHEDD
    EOF
    fi

    # Restarting daemons
    /etc/init.d/condor start

    # User to run the workflows as, and allow the experiment management
    # ssh key to authenticate
    adduser wf
    mkdir -p ~wf/.ssh
    cp ~/.ssh/authorized_keys ~wf/.ssh/
    chown -R wf: ~wf/.ssh
        
    # Master is the submit host, so deploy our workflow on it
    if [ "x$MASTER_ADDR" = "x" ]; then
        # install the workflow tarball and wait script
        cd ~wf
        wget -q http://pegasus.isi.edu/static/precip/wf-experiment/montage.tar.gz
        tar xzf montage.tar.gz
        chown -R wf: montage*
    fi
                    
                

| 

cloudinit.d
===========

| cloudinit.d is a tool designed for launching, controlling, and
monitoring complex environments in the cloud.
| 
|  Its most important feature is repeatable, one-click, deployment of
sets of VMs configured with launch plans.  These sets of VMs can be
deployed over multiple clouds (Eucalyptus, Nimbus, OpenStack, and Amazon
EC2 are currently supported) as well as include non-virtualized
resources. Like the Unix init.d process, cloudinit.d can manage
dependencies between deployed VMs. It also provides mechanisms for
testing, monitoring, and repairing a launch.
| 
|  For more information about cloudinit.d see our \ `Teragrid 2011
paper <http://www.nimbusproject.org/files/cloudinitd_tg11_submit3c.pdf>`__. For
repeatable experiment management with cloudinit.d read the \ `report
on <http://www.nimbusproject.org/downloads/Supporting_Experimental_Computer_Science_final_draft.pdf>`__ `support
for experimental computer
science <http://www.nimbusproject.org/downloads/Supporting_Experimental_Computer_Science_final_draft.pdf>`__.

Grid Services
=============

Unicore
=======

This page is maintained by Karolina Sarnowska-Upton from the University
of Virginia.

|image130|
  
==========

UNICORE 6 on FutureGrid
 User Manual
=======================

| Author: Karolina Sarnowska-Upton, University of Virginia
|  Version: 1.0
|  Today's Date: 2010-12-21
|  Last Revision: 2011-11-28

Introduction
============

`UNICORE 6 <http://www.unicore.eu/download/unicore6%A0>`__ has been
deployed at various FutureGrid sites. This tutorial explains how to
connect to the existing FutureGrid UNICORE endpoints from other grid
middleware platforms or a UNICORE Commandline Client (UCC) as well as
how runs jobs on UNICORE sites and how to deploy a new UNICORE grid.

What is UNICORE?
================

UNICORE (Uniform Interface to Computing Resources) is a Grid middleware
system. Listed below are the key principles of the UNICORE design. More
information about UNICORE can be found at
`http://www.unicore.eu <http://www.unicore.eu>`__.

-  Open source under BSD license.

-  Standards-based, conforming to the latest standards from the Open
   Grid Forum (OGF), W3C, OASIS, and IETF, in particular the Open Grid
   Services Architecture (OGSA) and the Web Services Resource Framework
   (WS-RF 1.2).

-  Open and extensible realized with a modern Service- Oriented
   Architecture (SOA), which allows easily replacement of particular
   components with others.

-  Interoperable with other Grid technologies to enable a coupling of
   Grid infrastructures or the users needs

-  Seamless, secure, and intuitive following a vertical, end-to-end
   approach and offering components at all levels of a modern Grid
   architecture from intuitive user interfaces down to the resource
   level. Like previous versions UNICORE 6 seamlessly integrates in
   existing environments.

-  Mature security mechanisms adequate for the use in supercomputing
   environments and Grid infrastructures. X.509 certificates form the
   basis for authentication and authorization, enhanced with a support
   for proxy certificates and virtual organizations (VO) based access
   control.

-  Workflow support tightly integrated into the stack while being
   extensible in order to use different workflow languages and engines
   for domain-specific usage.

-  Application integration mechanisms on the client, services and
   resource level for a tight integration of various types of
   applications from the scientific and industrial domain.

-  Different clients serving the needs of various scientific
   communities, e.g. graphical clients to define complex workflows,
   command line tool, web based access.

-  Quick and simple to install and configure to address requirements
   from operational teams and to lower the barrier of adopting Grid
   technologies. Similar the configuration of the various services and
   components is easy to handle.

-  Various operating and batch systems are supported on all layers, i.e.
   clients, services and systems; Windows, MacOS, Linux, and Unix
   systems as well as different batch systems are supported such as
   LoadLeveler, Torque, SLURM, LSF, OpenCCS, etc.

-  Implemented in Java to achieve platform independence.

Connecting to the UNICORE BES Endpoints From Other Grid Middleware Clients
==========================================================================

Two UNICORE BES endpoints have been deployed on FutureGrid for
interoperability testing. One endpoint is located on Sierra and the
other is located on India. This section contains the information needed
for other grid middleware platforms to connect to the UNICORE BES
endpoints.

India Endpoint Info <currently unavailable>
-------------------------------------------

-  **Endpoint URL**:
   `https://149.165.146.134:8081/DEMO-SITE/services/ <https://149.165.146.134:8081/DEMO-SITE/services/>`__\ BESFactory?res=default\_bes\_factory

-  **Security**: configured for username/password authentication;
   `Email <mailto:karolina@virginia.edu>`__ for username token and CA
   cert.

-  **OS**: Red Hat Enterprise Linux Server release 5.5

-  **Arch**: x86\_64

-  **Cores**: 8 (Jobs submitted directly to machine - i.e. not through
   PBS queue)

Sierra Endpoint Info
--------------------

-  **Endpoint URL**:
   `https://198.202.120.85:8081/DEMO-SITE/services/ <https://198.202.120.85:8081/DEMO-SITE/services/>`__\ BESFactory?res=default\_bes\_factory

-  **Security**: configured for X-509 based mutual client
   authentication; `Email <mailto:karolina@virginia.edu>`__ with X-509
   cert and for CA cert.

-  **OS**: Red Hat Enterprise Linux Server release 5.5

-  **Arch**: x86\_64

-  **Cores**: 320 (Jobs submitted to PBS queue)

--------------

Connecting to the UNICORE BES Endpoints Using a UNICORE Commandline Client
==========================================================================

A UNICORE client can be used to connect to the FutureGrid UNICORE6
endpoints. This section describes how to install a UCC ( UNICORE
Commandline Client), configure it to connect to a FutureGrid U6 endpoint
via X-509 based mutual client authentication, and then submit jobs via
BES.

Installing the UNICORE6 Commandline Client (UCC)
------------------------------------------------

Acquire Client Bundle
~~~~~~~~~~~~~~~~~~~~~

#. Navigate to the UNICORE website:
   `http://www.unicore.eu/ <http://www.unicore.eu/>`__
#. Select “Download” link in left hand tool bar
#. Under Clients section, select “Download” link for Commandline Client
#. Click on folder for desired version  (i.e. 6.4.1)
#. Click on desired distribution bundle to download  (i.e.
   ucc-6.4.1-all.tar.gz)

Unpack UCC
~~~~~~~~~~

-  Unpack files from downloaded distribution bundle  (i.e. tar -xvzf
   ucc-6.4.1-all.tar.gz)
-  On completion, there should be a directory containing the UNICORE6
   commandline client  (i.e. ucc-6.4.1)
-  You can add the bin directory to your path for easier client
   execution

.. code:: _fck_mw_lspace

     export PATH=$PATH:<UCC_HOME>/bin,  where UCC_HOME is the directory you installed UCC

Examine UCC Files
~~~~~~~~~~~~~~~~~

Directory Structure

-  bin – contains executable “ucc”
-  certs
-  conf – contains *preferences*\ file to be configured with security
   and registry settings
-  doc
-  extras
-  lib
-  samples

Run Commandline
~~~~~~~~~~~~~~~

 
~

Client
~~~~~~

Run ucc to get list and description of available commands

.. code:: _fck_mw_lspace

     $UCC_HOME/bin/

.. code:: _fck_mw_lspace

.. code:: _fck_mw_lspace

    ucc

| Usage: ucc <command> [OPTIONS] <args>
|  The following commands are available:
|  DATA MANAGEMENT
|   ls                     - list a storage
|   rm                    - remove a remote file or directory
|   copy-file-status      - check status of a copy-file
|   get-file              - get remote files
|   find                 - find files on storages
|   resolve                - resolve remote location
|   mkdir                  - create a directory remotely
|   copy-file             - copy remote files
|   put-file               - puts a local file to a remote server
|  GENERAL
|   create-storage       - create a storage service instance
|   connect               - connect to UNICORE
|   list-storages         - list the available remote storages
|   list-applications    - lists applications on target systems
|   list-jobs             - list your jobs
|   list-sites             - list remote sites
|   system-info            - checks the availability of services
|  JOB EXECUTION
|   run                    - run a job through UNICORE 6
|   get-status             - get job status
|   abort-job             - abort a job
|   batch                  - run ucc on a set of files
|   get-output            - get output files
|  OGSA-BES
|   bes-list-att           - provides information about U6 BES Interface
|   bes-terminate-job      - terminate bes activity
|   bes-submit-job         - run a job through UNICORE 6 BES Interface
|   bes-list-jobs         - list jobs running on BES.
|   bes-job-status         - get bes activity status
|  OTHER
|   shell                  - starts an interactive UCC session
|   issue-delegation      - allows to issue a trust delegation assertion
|   connect-to-testgrid   - get credentials for the public testgrid
|   wsrf                   - perform a WSRF operation
|   cip-query              - query a CIS Infoprovider at a UNICORE site
|   run-groovy            - run a Groovy script
|  WORKFLOW
|   workflow-trace        - trace info on a workflow in Chemomentum
|   workflow-control      - offers workflow control functions
|   workflow-submit       - submit a workflow
|   workflow-info         - lists info on workflows.
|   broker-run             - submit work assignment to service
orchestrator
|  Enter 'ucc <command> -h' for help on a particular

Installation Conclusion
~~~~~~~~~~~~~~~~~~~~~~~

-  At this point, the UNICORE Commandline Client has been installed
-  However, the client is currently not connected to any UNICORE sites
-  The next section will explain how to configure the client so that the
   client will connect to one of the FutureGrid U6 endpoints

Configuring Client to Connect to FutureGrid U6 Endpoints
--------------------------------------------------------

Configuration Overview
~~~~~~~~~~~~~~~~~~~~~~

-  To connect to a FutureGrid U6 endpoint, you need to

   -  setup security information so that your client will trust the
      FutureGrid U6 endpoint and vice-versa
   -  specify the connection address that the client should use (aka
      registry address)

-  This configuration process consists of

   -  setting up keystore and truststore files with security info
   -  specifying a registry address for the FutureGrid endpoint

-  This information is stored in a “preferences” file (starter at
   $UCC\_HOME/conf/preferences)

Setting Up Security in UNICORE
------------------------------

To setup security, you will need to inform the UNICORE software of your
identity and who you trust via keystore and truststore files:

-  **Keystore**- a file from which UNICORE software reads your identity,
   i.e. your private key and your certificate. As your private key is
   very sensitive, the keystore is encrypted and you will need a
   password to "unlock” it before usage.
-  **Truststore**- a file from which UNICORE software reads certificates
   of the Certificate Authorities you trust. It is not as sensitive as a
   keystore, but it is also encrypted.

| For an overview of the security mechanism found in the UNICORE grid
middleware, please consult the `Users' UNICORE Security Guide \| UCC
version <http://unicore.svn.sourceforge.net/svnroot/unicore/documentation/old/securityGuide/Main-UCCOnly.pdf>`__
|  This guide also discusses common security configuration problems and
details how to create keystores/truststores

Setting Up a
------------

Keystore
--------

Assumption: you want to use a preexisting X.509 certificate for security
validation

-  If your key and certificate are in a keystore (in PKCS12 or JKS
   format), you can directly use this keystore
-  If you have PEM files, you will need to wrap your key and certificate
   files into a PKCS12 keystore:

.. code:: _fck_mw_lspace

    openssl pkcs12 -export -in myCert.pem -inkey myKey.pem -out keystore.p12 -name mykey 

Creating a Truststore
~~~~~~~~~~~~~~~~~~~~~

Assumption: you have certificates for CAs that you trust and want to put
into a truststore file. This should include:

CA cert for CA that issued your certificate

| CA cert for CA that issued FutureGrid U6 endpoint certs (Email
`uvacse@virginia.edu <mailto:uvacse@virginia.edu>`__ for cert)
|   

To create a truststore with keytool

.. code:: _fck_mw_lspace

    keytool -import -keystore truststore.jks -file CAcert.pem -alias 

.. code:: _fck_mw_lspace

    myTrustedCA

Repeat command for every CA certificate file (set a unique alias for
each certificate)

Acquiring the Registry
~~~~~~~~~~~~~~~~~~~~~~

Address
~~~~~~~

The UNICORE Registry server provides information about available
services to clients and other services

Registry address for FutureGrid U6 Endpoint on Sierra (as of 08/2011)

.. code:: _fck_mw_lspace

    https://198.202.120.85:8081/DEMO-SITE/services/Registry?res=default_registry

Connecting to Endpoints w/o Registries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Registry URL is expected to be provided in the preferences file. If a
BES endpoint is not advertised via a UNICORE Registry, the configuration
options can be modified to allow this behavior.

#. In the preferences file, set the contact-registry to false:

.. code:: rteindent1

      contact-registry=false

2. Instead, provide at least one BESFactory URL using the following
   format.

.. code:: rteindent1

      bes.1=https://site1.com/services/BESFactory
      bes.4=file:///tmp/bes.xml
      bes.5=/tmp/bes.xml

If the "contact-registry" option is set to false and no OGSA-BES URL is
specified, UCC will report an error.

To use an XML endpoint reference (EPR) read from a file for contacting a
BESFactory service, the contents of a EPR file must validate against the
WS-Addressing’s endpoint reference schema.

Preferences File Modifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have keystore and truststore files, configure the client
preferences file to use this security information

$UCC\_HOME/conf/preferences

**Keystore Settings**

-  Set keystore path to the full path to where your keystore file is
   saved locally
-  Provide the password that “unlocks” your keystore file
-  If you do not want specify the password, you will be asked for it on
   the commandline
-  Provide keystore’s alias
-  Provide keystore’s storetype (PKCS12 or JKS)

**Truststore Settings**

-  Set truststore path to the full path to where your truststore file is
   saved locally
-  Provide the password that “unlocks” your truststore file

**Registry Address or BESFactory URL Information**

-  Provide registry address/BESFactory URL of FutureGrid U6 endpoint

Example Preferences File
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: rteindent1

    keystore=/home/gridcerts/keystore.p12
    password=YOUR-KEYSTORE-PASSWORD
    storetype=pkcs12
    alias=myKeystore

    truststore=/home/gridcerts/truststore.jks
    truststorePassword=YOUR-TRUSTSTORE-PASSWORD

    # The address(es) of the registries to contact (space separated list)
    registry=https://198.202.120.85:8081/DEMO-SITE/services/Registry?res=default_registry

    # ... other properties can follow

Locating the Preferences
~~~~~~~~~~~~~~~~~~~~~~~~

File
~~~~

By default, UCC checks for the existence of a file at
$USER\_HOME/.ucc/preferences and reads default settings from there

Copy your preferences file to this location or specify it’s a location
every time you issue a UCC command

::

      -c $UCC_HOME/conf/preferences

Validate Client
~~~~~~~~~~~~~~~

Setup
~~~~~

To check access to FutureGrid endpoints, try a command while specifying
the path to your preferences file

::

    $UCC_HOME/bin/ucc system-info -v -l -c $UCC_HOME/conf/preferences
    $UCC-HOME/bin/ucc list-sites -c $UCC_HOME/conf/

::

    preferences

If everything is alright you should see information about the FutureGrid
endpoint.

Configuration
~~~~~~~~~~~~~

Conclusion
~~~~~~~~~~

| Your UCC has now been configured to access the FutureGrid U6 endpoint
via X-509 based mutual client authentication
|  Consult the next section to learn about getting started and submit
jobs

Submitting Jobs to FutureGrid U6 Endpoints
------------------------------------------

Getting
~~~~~~~

Started
~~~~~~~

Make sure you have access to some target system

::

    $UCC_HOME/bin/ucc connect -c $UCC_HOME/conf/preferences

List the sites available to you using

::

      $UCC_HOME/bin/ucc list-sites -c $UCC_HOME/conf/

::

    preferences

Run a sample job

::

      $UCC_HOME/bin/ucc run -v $UCC_HOME/samples/date.u -c $UCC_HOME/conf/preferences

Submit Jobs to
~~~~~~~~~~~~~~

BES
~~~

To send a job read from a JSDL file

-  to a site listed in the preferences file:

.. code:: rteindent1

            $UCC_HOME/bin/ucc bes-submit-job -j hellompi.xml -s bes.3 -v

-  using a BESFactory URL:

.. code:: rteindent1

      ucc bes-submit-job -j hellompi.xml -s https://example.com/services/BESFactory -v

-  using an endpoint reference file path:

.. code:: rteindent1

      ucc bes-submit-job -j hellompi.xml -s file:///tmp/bes.xml -v

Other BES Related
~~~~~~~~~~~~~~~~~

Commands
~~~~~~~~

Check job status

::

      ucc bes-job-status jobid.job

Terminate job

::

    ucc bes-terminate-job jobid.job

List user’s jobs on a BESFactory

::

    ucc bes-list-job-s bes.1

List BESFactory properties:

::

    ucc bes-list-att -s bes.1

\*Descriptor (.job) file is automatically generated after a successful
execution of "bes-submit-job" command

Job Submission Conclusion
~~~~~~~~~~~~~~~~~~~~~~~~~

You should now be able to submit jobs to a BES service on a FutureGrid
U6 endpoint

 
-

 
-

References
----------

The information provided in this section has been extracted from the
following sources. Each contains much more detail about the various
topics discussed here.

-  `UNICORE6
   Manuals <https://unicore.svn.sourceforge.net/svnroot/unicore/documentation/old/securityGuide/Main-UCCOnly.pdf>`__
-  `UNICORE Commandline Client: User
   Manual <http://www.unicore.eu/documentation/manuals/unicore6/files/ucc/ucc-manual.html>`__
-  `UNICORE Security Guide:
   UCC <https://unicore.svn.sourceforge.net/svnroot/unicore/documentation/old/securityGuide/Main-UCCOnly.pdf>`__

  Questions/Comments
--------------------

Please email uvacse@virginia.edu

--------------

Running Jobs on UNICORE Sites
=============================

This section provides a general overview of running jobs on UNICORE
sites.

First, you can check whether there is an available target system for
execution:

.. code:: _fck_mw_lspace

     $ucc connect -c <path_to_ucc.preferences> 

You can also list the available target sites:

.. code:: _fck_mw_lspace

     $ucc list-sites

To run a job, you can specify the job using the UNICORE `job description
format <http://www.unicore.eu/documentation/manuals/unicore6/ucc/jobdescription.html>`__.

.. code:: _fck_mw_lspace

     $ucc run <job_description_file>

Or you can specify a job to run using a Job Submission Description
Language (JSDL) file.

.. code:: _fck_mw_lspace

     $ucc run -j <JSDL_file>

For example, a simple job to run the date, date.u, could be described
using the UNICORE description format as follows:

.. code:: _fck_mw_lspace

     #
    # simple job: run Date
    #

    {
     ApplicationName: Date,
     ApplicationVersion: 1.0,
    }

This job can then be run with the command:

.. code:: _fck_mw_lspace

    $ucc run date.u

Alternately, this job could be described using a JSDL file, date.jsdl,
as follows:

.. code:: _fck_mw_lspace

     <?xml version="1.0" encoding="UTF-8"?>
    <jsdl:JobDefinition xmlns="http://www.example.org/"
           xmlns:jsdl="http://schemas.ggf.org/jsdl/2005/11/jsdl"
           xmlns:jsdl-posix="http://schemas.ggf.org/jsdl/2005/11/jsdl-posix"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

           <jsdl:JobDescription>
                   <jsdl:JobIdentification>
                           <jsdl:JobName>Test Job</jsdl:JobName>
                   </jsdl:JobIdentification>

                   <jsdl:Application>
                           <jsdl:ApplicationName>Date 1.0</jsdl:ApplicationName>
                           <jsdl-posix:POSIXApplication>
                                 <jsdl-posix:Executable>
                                         /bin/date
                                 </jsdl-posix:Executable>
                         </jsdl-posix:POSIXApplication>
                 </jsdl:Application>
           </jsdl:JobDescription> 
    </jsdl:JobDefinition>

This JSDL job can then be run with the command:

.. code:: _fck_mw_lspace

     $ucc run -j date.jsdl.

--------------

Deploying a New UNICORE 6 Grid
==============================

This section details how to install and setup a UNICORE 6 grid. This
will create a new grid infrastructure separate from the existing
deployments mentioned above.

Prerequisites
-------------

Prerequisites listed in UNICORE 6 README.txt file:

-  Java 5 JRE or SDK (or later). We recommend using SUN Java 6.

You can check what version of java is installed by running:

.. code:: _fck_mw_lspace

     $java -version

If the java version is too old or the command is not found, download the
latest JRE version. After unpacking, update JAVA\_HOME and PATH.

.. code:: _fck_mw_lspace

     JAVA_HOME=<JAVA_LOCATION>
    PATH=<JAVA_LOCATION>/bin:$PATH

-  Perl 5 (only for the classic TSI)

You will need Perl if you will be running jobs via a queue management
system. By default, jobs run directly on the local machine. Extra
configuration is needed to setup a TSI and run jobs via a queue
management system.

Installing the Core Server Bundle
---------------------------------

The UNICORE 6 Core Server Bundle can be downloaded from the `UNICORE
website <http://www.unicore.eu/download/unicore6/>`__. This bundle will
provide you with the minimal set of UNICORE components (Gateway,
UNICORE/X, TSI, XUUDB) needed to get a UNICORE 6 grid up and running
quickly.

.. code:: _fck_mw_lspace

    From the README.txt:
    The basic configuration and installation is as follows
    1) edit configure.properties
    2) ./configure.py <unicore_user> [<hostname>]
    3) run ./install.py to install UNICORE in the selected directory

    To start the configuration process, do (as non-root user)
    ./configure.py <login> [<hostname>]
    where <login> is the Unix account that the installation shall use, and the   
    optional <hostname> indicates which hostname shall be used. If not given,
    a hostname lookup will be performed.

    If you want to customize this process, edit the "configure.properties" file,
    which contains all the ports and other settings (except security settings 
    such as keystore locations).

    To finally copy the files into the installation directory, run
    ./install.py

    More documentation at http://www.unicore.eu/documentation.
     

Starting/Stopping the UNICORE Servers
-------------------------------------

| The servers are started with the start.sh script and stopped with the
stop.sh script. Both of these scripts are located under the UNICORE
install directory.
|   

.. code:: _fck_mw_lspace

    You can confirm that the UNICORE servers are running with the ps command. 
    You should see three processes running: XUUDB, Gateway, and UNICOREX. 
      $ps aux| grep unicore

 

Genesis II
==========

|image131|
 Genesis II on FutureGrid
 User Manual
=========================

| Author: University of Virginia
|   Version: 1.0
|    Last Revision: 2011-11-02

 Introduction
=============

`GenesisII <http://www.genesis2.virginia.edu/wiki>`__ compute endpoints
are currently deployed on three FutureGrid HPC resources: XRay, Sierra
and India.  Additional endpoints are planned for Hotel and Alamo in the
near future.  This tutorial explains:

-  How to connect to these GenesisII endpoints from other grid
   middleware platforms;
-  How to download GenesisII client software and use the UVa Corss
   Campus Grid (XCG) which includes the FutureGrid endpoints.

What is GenesisII
=================

GenesisII is a Grid middleware system. Listed below are the key
principles/features of the GenesisII design. More information about
GenesisII can be found `here <http://www.genesis2.virginia.edu/wiki>`__.

-  Open source.

-  Standards-based. GenesisII follows grid standards from the Open Grid
   Forum (OGF), W3C, and OASIS, including many from the Open Grid
   Services Architecture (OGSA) and the Web Services Resource Framework
   (WSRF).  In particular, GenesisII adheres to parts or all of OGSA
   Basic Execution Service (BES), Resource Naming Service (RNS), OGSA
   ByteIO, WS-Security, WS-Naming, WS-Trust, and Job Submission
   Description Language (JSDL).

-  Open and extensible realized with a modern Service- Oriented
   Architecture (SOA), which allows to easily replace particular
   components with others.

-  Interoperable with other Grid technologies to enable a coupling of
   Grid infrastructures or the users needs

-  End user focused. Whenever possible GenesisII was designed to use
   concepts already familiar to users (such as hierarchical directory
   structures) and to provide easy to use commands and GUIs to simplify
   the user's experience.  GenesisII provides a number of commands based
   on familiar UNIX tools and provides GUIs for to browse the grid
   directory structure, monitor jobs, create JSDL job descriptions, etc.

-  Strong security mechanisms built in from the ground up.  Flexible
   access control for all grid resources.  Support for X.509
   certificates and username/password (based on WS-Security and OGF
   Basic Security Profile).  Support for virtual organizations via
   user-defined groups.

-  Quick and simple to install and configure.

-  Client and server software supported on a number of platforms
   (Windows XP, Linux, and MacOS).  Support for various batch systems
   such as PBS, Sun Grid Engine, etc.

-  Implemented in Java to achieve platform independence.

Connecting to the GenesisII BES Endpoints
=========================================

To date, three GenesisII BES endpoints have been deployed on FutureGrid
for interoperability testing as well as grid client usage. Endpoints are
located on Sierra, India, and Alamo. This section contains the
information needed for other grid middleware platforms to connect to the
GenesisII BES endpoints.

Supported Data Staging
----------------------

Protocols
---------

| Each of the GenesisII endpoints supports a number of protocols for
staging data into and out of jobs as supported by the JSDL
specification's Data Staging elements.  The following are the protocols
currently supported by the GenesisII endpoints:
| 

Stage in:
~~~~~~~~~

-  HTTP
-  RNS/ByteIO
-  ftp
-  scp
-  sftp

Stage out:
~~~~~~~~~~

-  mailto
-  RNS/ByteIO
-  ftp
-  scp
-  sftp

| \*\* NOTE: ftp, scp, sftp is supported as per the HPC FSE standard and
only for the username/password security token version.

Endpoint Connection Information
-------------------------------

India
~~~~~

-  **Endpoint EPR**: `click
   here <https://portal.futuregrid.org/sites/default/files/india-epr-Nov-01-2011.txt>`__

-  **Security**: configured for username/password authentication;
   `Email <mailto:uvacse@virginia.edu>`__ for username token and CA
   cert.

-  **OS**: Red Hat Enterprise Linux Server release 5.7

-  **Arch**: x86\_64

-  **Cores**: Approximately 400. Jobs submitted to HPC (i.e. batch)
   queue via PBS
     
-  **Grid Path**:
   /bes-containers/FutureGrid/IU/pbs-long.from-daemon.india.futuregrid.org

Sierra
~~~~~~

-  **Endpoint EPR**: `click
   here <https://portal.futuregrid.org/sites/default/files/sierra-epr-Mar-22-2012_0.txt>`__

-  **Security**: configured for username/password authentication;
   `Email <mailto:uvacse@virginia.edu>`__ for username token and CA
   cert.

-  **OS**: Red Hat Enterprise Linux Server release 6.1

-  **Arch**: x86\_64

-  **Cores**: Approximately 300. Jobs submitted to HPC (i.e. batch)
   queue via PBS
     
-  **Grid Path**:
   /bes-containers/FutureGrid/SDSC/pbs-long.from-daemon.sierra.futuregrid.org

Alamo
~~~~~

-  **Endpoint EPR**: `click
   here <https://portal.futuregrid.org/sites/default/files/alamo-epr-Mar-22-2012_0.txt>`__

-  **Security**: configured for username/password authentication;
   `Email <mailto:uvacse@virginia.edu>`__ for username token and CA
   cert.

-  **OS**: CentOS release 5.6

-  **Arch**: x86\_64

-  **Cores**: Approximately 200. Jobs submitted to HPC (i.e. batch)
   queue via PBS
     
-  **Grid Path**: /bes-containers/FutureGrid/TACC/pbs-long.from-alamo1

Hotel
~~~~~

-  **Endpoint EPR**: `click
   here <https://portal.futuregrid.org/sites/default/files/hotel-epr-Apr-24-2012.txt>`__

-  **Security**: `Email <mailto:uvacse@virginia.edu>`__ for
   username/password authentication token and CA cert.

-  **OS**: Red Hat Enterprise Linux Server release 5.8 (Tikanga)

-  **Arch**: x86\_64
     
-  **Cores**: Approximately 300. Jobs submitted to HPC (i.e. batch)
   queue via PBS
     
-  **Grid Path**:
   /bes-containers/FutureGrid/UC/pbs-long.from-hotel1.futuregrid.org

Using the Futuregrid GenesisII Endpoints as a Client
====================================================

There are two ways a client can use the GenesisII endpoints deployed
within Futuregrid: using a standards-compliant non-GenesisII middleware
client or using the GenesisII client.

Non-GenesisIIUsing a Standards-Compliant Client
-----------------------------------------------

| If you wish to use a standards-based middleware client, you may be
able to use that client to access the GenesisII BES endpoints within
Futuregrid.  The first step is to determine whether the grid client
software you wish to use is properly compliant with the GenesisII BES
implementation.  GenesisII BES endpoints have been tested for
interoperability against several grid software systems.  You will need
to contact the developer/vendor of your system to determine if their
software is compatible with GenesisII.  Depending on your system works,
you will either need to contact your grid system administrator to have
him/her add the Futuregrid GenesisII BES endpoints or you will need to
provide a reference to the endpoints to the client tooling.  In either
case, the information you or your grid administrator needs is included
in the section above (`Connecting to the GenesisII BES
Endpoints <#Connecting%20To%20GenesisII%20BES%20Endpoints>`__).
| 

Using The GenesisII Client
--------------------------

GenesisII has a rich client package available for Windows, MacOS and
LINUX platforms that includes UNIX-style command line tools as well as
several graphical user interface tools.  The University of Virginia
maintains a grid called the Cross Campus Grid (XCG) that already
includes the FurtureGrid GenesisII BES endpoints in it - already
configured and ready to go.  To get started, the first step is to
download and install the GenesisII/XCG installation package.

Acquiring GenesisII Client Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GenesisII/XCG installers are available at
`http://www.cs.virginia.edu/~vcgr/wiki/index.php/Genesis\_II\_Downloads <http://www.genesis2.virginia.edu/wiki/Main/Downloads>`__.
Choose the platform that matches the machine/OS where you will be
running your client and click the corresponding "Download" link to
download the installer.

 
^

Linux
^^^^^

The Linux installer is a shell script named XCG-Installer.sh encoded
with the entire GenesisII package inside.  Simply execute the shell
script (./XCG-Installer in proper directory) to begin installation. 
Follow the steps here in answering the installation questions.

 
^

Windows
^^^^^^^

| The Windows installer is an executable named XCG-Installer.exe. 
Simply run it like any other executable (e.g. double-clicking) and
follow the steps here in answering the installation questions.
| 
|  Note that currently, the GenesisII software is only tested for
Windows XP.  However, our early experience with Windows 7 (and Vista)
indicates that the client installation will work fine as long as you
install GenesisII in a folder that does not have special security
meaning to Windows (such as your Documents and Settings directory or
C:\\).

 
^

MacOS
^^^^^

| The MacOS installer is a dmg file named XCG-Installer.dmg encoded with
the entire GenesisII package inside.  Simply execute the dmg file (e.g.
by double clicking) to begin installation.  Follow the steps here in
answering the installation questions.
| 

Installing the GenesisII/XCG Client Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The installation process requires answering a few questions about
license agreement and configuration options.

-  **Agree to license terms**.  The GenesisII license follows the Apache
   License model.  For command line versions, this may require hitting
   enter a number of time to scroll the license text on the screen.
-  **Select the directory for the installation**.  In most cases the
   default is sufficient, though you can feel free to change it.  As
   noted earlier, Windows Vista and 7 users should choose a directory
   that is not given special protection from those operating systems. 
   For example, the default C:\\Program Files is given special treatment
   and blocks writes made there by the software.  This causes GenesisII
   problems because GenesisII has a patch mechanism built which needs to
   overwrite package files in the installation directory.  For Windows
   7/Vista, we recommend a directory within your user folder.
-  **Client v Full Container Install.**  The entire GenesisII software
   package is included in the installer.  This includes both client-side
   command line tools and GUIs as well as server-side programs for
   installing grid servers.  We recommend installing the client only
   version.  Select XCG Client Install option.  
-  **Shortcuts/Start Menu options.**  For Windows users, you can select
   whether to create a shortcut for all users (default yes), create a
   start menu item for GenesisII (default: yes) and pick a name for the
   start menu folder (default: GenesisII).  The defaults are
   recommended, but you can change if you like.  For Linux and MacOS,
   you can choose whether to create shortcuts in the standard binary
   directory (Linux: /usr/bin; MacOS: /Applications/?).  Unless you are
   installing with root privileges, we recommend choosing "No" to this
   question.

| That's it.  Since the installer is specific to the UVA Cross Campus
Grid, you not only have GenesisII successfully installed, but you have
also configured your system to connect to the XCG.
| 

Getting Started
---------------

To get started using the XCG, you will need an XCG account - which is
**not** the same as your local machine account or your FutureGrid
resource account. To request an XCG account, fill out the XCG user
application form located at
`http://www.cs.virginia.edu/~vcgr/userrequest <https://www.cs.virginia.edu/~vcgr/userrequest/>`__.

Once you have an account and have the appropriate GenesisII software
installed, you are ready to start a GenesisII grid shell and login.

Start Grid Shell
~~~~~~~~~~~~~~~~

To start a grid shell start the "grid" executable from the installation
directory.

Windows
^^^^^^^

| Double click the "grid" file in the installation directory;
|  or
|  Open a Windows command line window, cd to the installation directory,
and enter the grid.exe command.

Linux or MacOS
^^^^^^^^^^^^^^

| If you have a Window manager running, double click on the grid binary
in the installation directory
|  or
|  Open a shell, cd to the installation directory and enter the grid
command

.. code:: _fck_mw_lspace

     $> cd <installation directory>
     $> grid

| **LogIn**
|  Once you have a grid shell open, you need to be logged into your XCG
grid account in order to perform most useful commands. First check to
see if you are already logged in - the "whoami" command prints out your
current credentials. If you are not logged in, it should look like this
(the Client Tool Identity is an automatically generated certificate used
by GenesisII client commands and does not carry any authentication
information):

.. code:: _fck_mw_lspace

     $XCG> whoami
     Client Tool Identity:
        "Client Cert EFC05BB7-295A-B313-E0E0-95A8CE61EB68"
     $XCG>

| To login, use the "login" command.  The syntax is "login
--username=<grid user name>".  After running this command, a popup
window will prompt you for your password

.. code:: _fck_mw_lspace

     $XCG> login --username=jfk3w
     $XCG> whoami
     Client Tool Identity:
        "Client Cert EFC05BB7-295A-B313-E0E0-95A8CE61EB68"
     "jfk3w" -> "Client Cert EFC05BB7-295A-B313-E0E0-95A8CE61EB68"
     "uva-idp-group.2010" -> "Client Cert EFC05BB7-295A-B313-E0E0-95A8CE61EB68" 
     $XCG> 

| The output from the post-login whoami command indicates that I have 2
new certificates - one that asserts that I am user jfk3w, and another
that asserts that I have the permissions of the group
"uva-idp-group.2010".  The XCG uses the uva-idp-group.2010 to set
permissions for all approved XCG users.  Your membership in this group
is done by XCG administrators when you account is created.  If you later
create new groups or are added to other existing groups, your login will
automatically acquire the extra credentials to assert that you are a
member of that group (assuming the group allows you access).

Running Jobs
~~~~~~~~~~~~

To learn how the basics about executing and monitoring jobs using
GenesisII and the XCG, please refer to `XCG
Tutorial <https://portal.futuregrid.org/sites/default/files/XCG%20Tutorial.pdf>`__
document.

Getting Help
------------

To get help using the XCG send email to the UVA Computational Science
and Engineering (UVACSE) group at uvacse@virginia.edu.  You can also use
the `GenesisII web
site <http://www.genesis2.virginia.edu/wiki/Main/HomePage>`__ and the
`XCG web
site <http://www.cs.virginia.edu/~xcgshare/wiki/index.php/Homepage>`__
to look at further documentation and FAQs

+-------------------------------------------------------------------------------------------------------------------+-----------+
| Attachment                                                                                                        | Size      |
+===================================================================================================================+===========+
| `india-epr-Nov-01-2011.txt <https://portal.futuregrid.org/sites/default/files/india-epr-Nov-01-2011.txt>`__       | 7.8 KB    |
+-------------------------------------------------------------------------------------------------------------------+-----------+
| `sierra-epr-Mar-22-2012.txt <https://portal.futuregrid.org/sites/default/files/sierra-epr-Mar-22-2012_0.txt>`__   | 7.8 KB    |
+-------------------------------------------------------------------------------------------------------------------+-----------+
| `alamo-epr-Mar-22-2012.txt <https://portal.futuregrid.org/sites/default/files/alamo-epr-Mar-22-2012_0.txt>`__     | 7.82 KB   |
+-------------------------------------------------------------------------------------------------------------------+-----------+
| `hotel-epr-Apr-24-2012.txt <https://portal.futuregrid.org/sites/default/files/hotel-epr-Apr-24-2012.txt>`__       | 7.86 KB   |
+-------------------------------------------------------------------------------------------------------------------+-----------+

SAGA supporting Distributed Applications on Grids, Clouds on FutureGrid
=======================================================================

| ***SAGA on FutureGrid***
| 
| 
|  ***Activity***:
| 
|  The Simple API for Grid Applications (SAGA) is an OGF standard
(`http://www.ogf.org/ <http://www.ogf.org/>`__), and defines a high
level, application-driven API for developing first-principle distributed
applications, and for distributed application frameworks and tools. Our
SAGA project (see
`http://www.saga-project.org/ <http://www.saga-project.org/>`__)
provides SAGA API implementations in C++ and Python, which interface to
a variety of middleware backends, as well as higher level application
frameworks, such as Master-Worker, MapReduce, AllPairs, and BigJob.  For
all those components, we use FutureGrid and the different software
environments available on FG for extensive portability and
interoperability testing, but also for scale-up and scale-out
experiments. These activities allow to harden the SAGA components
described above, and support CS and Science experiments based on SAGA.
| 
|  ***Achievements:***
| 
|  FG has provided a persistent, production-grade experimental
infrastructure with the ability to perform controlled experiments,
without violating production policies and disrupting production
infrastructure priorities.  These attributes, coupled with FutureGrid's
technical support, have resulted in the following specific advances in
the short period of under a year:
| 
|  *1: Use of FG for Standards-based development and interoperability
tests:*
| 
|  We have, in particular, been able to prepare SAGA for future
deployments on XSEDE; this has occurred by testing the SAGA-BES adaptor
in a variety of configurations: against Unicore and Genesis-II backends,
with UserPass and Certificate-based authentication, with POSIX and HPC
application types, with and without file staging support.  While those
tests are still ongoing, it allows us to be confident about the expected
XSEDE middleware evolution; in the vast majority of cases, the
standards-based approach seems to work without a hitch.
| 
|  Furthermore, we are continuously using FG-based job submission
endpoints for GIN-driven interoperation tests with a variety of other
production Grid infrastructures, including DEISA, PRACE, Teragrid and
EGI (see
`http://forge.gridforum.org/sf/projects/gin/ <http://forge.gridforum.org/sf/projects/gin/>`__
and
`http://www.saga-project.org/interop-demos/ <http://www.saga-project.org/interop-demos/>`__).
| 
|  In order to simplify the deployment and to improve end user support
for SAGA, we have been using FG hosts to develop, test and harden our
deployment procedures by mimicking the CSA approach we currently use on
TeraGrid and XSEDE.  At the same time, that deployment procedure makes
SAGA and SAGA-based components available and maintained on all FG
endpoints.
| 
| 
|  *2: Use of FG for Analysing & Comparing Programming Models and
Run-time tools for Computation and Data-Intensive Science.*
| 
|  *2.a: Development of Tools and Frameworks:*

-  P\* experiments
    'P\*' is a conceptual model of pilot-based abstractions, in
   particular for pilot jobs.  Our work on P\* includes comparison
   between different PilotJob frameworks (BigJob, Condor GlideIn, Diane,
   Swift), and between different coordination models within those
   frameworks.  We used FG for a number of those experiments, as it
   allowed us to compare a range of characteristics in a controlled
   environment.
-  Advanced dynamic partitioning and distribution of data-intensive
   distributed applications
    Futuregrid resources have been crucial in carrying out a first set
   of scoping experiments for O.W.'s Ph.D thesis: "Towards a Reasoning
   Framework and Software System to Aid the Dynamic Partitioning,
   Distribution and Execution of Data-Intensive Applications". In these
   scoping experiments, three distinct FutureGrid resources (india,
   hotel, alamo) were used to coordinately execute a data-intensive
   genome matching workload (HTC). The partitioning and distribution
   decisions were dynamically made by an experimental software system
   based on autonomic computing concepts, and which is capable of
   monitoring FG HPC resources as well as jobs during workload
   execution.
-  Bliss (Bliss is SAGA)
    Bliss
   (`http://oweidner.github.com/bliss/ <http://oweidner.github.com/bliss/>`__)
   is an experimental implementation of SAGA written in pure Python.
   Bliss does not rely on any distributed Grid middleware; however, it
   allows distributed access to all FutureGrid HPC resources by
   providing an SFTP plugin for file transfer as well as 'PBS over SSH'
   for SAGA's job submission and resource information capabilities. 
   Bliss has been developed specifically with FutureGrid in mind and has
   been used in several cross-site experiments as the primary access
   mechanism to computing and storage resources.  While 'PBS over SSH'
   probably won't be a replacement for 'real' Grid middleware (like,
   e.g., Globus), its exposure through the standardized SAGA API
   presents an attractive and lightweight alternative to traditionally
   large Grid middleware stacks.
-  High-performance dynamic applications
    In extreme-scale computational science, there is a growing
   importance and need for specialized architectures and multi-model
   simulations. In this emerging environment, different simulation
   components will have different computational requirements.  Instead
   of coarsely assigning resources to all simulation components for
   their lifetime, we research methodologies whereby simulations can be
   split into their constituent components, and distributed
   computational resources are allocated according to the needs of these
   individual components.  Each simulation component is transferred
   along with the data and parameters needed to execute the simulation
   component on the target hardware.  This approach enables
   multi-component applications to more easily benefit from
   heterogeneous and distributed computing environments, in which
   multiple types of processing elements and storage may be available.
    In cases where software is developed with a static execution mode
   and only one resource in mind, the choice to distribute may not be
   available. By creating a dynamic method of execution and developing
   software which can package, transmit, and execute sub-applications
   remotely, existing simulations may be extended to make use of
   distributed resources. Through specially-designed modules that are
   compatible with pre-existing Cactus framework applications, we
   demonstrated means of improving task-level parallelism and extended
   the range of computing resources used with a minimal amount of change
   needed to existing applications.  Experiments were conducted using
   production cyberinfrastructures on FutureGrid and XSEDE, with up to
   128 cores.
-  Grid/Cloud interop (with Andre Luckow) [finished]
    We demonstrated for the first time the use of Pilot-Jobs
   concurrently on different types of infrastructures; specifically, we
   use BigJob both on FutureGrid HPC and Cloud resources as well as on
   other resources such as the XSEDE and OSG Condor resources.

|    
|  *2.b: Data Intensive Apps:*

-  MapReduce [with Andre Luckow]
    In Ref. [1], published in Future Generation Computing Systems, we
   compare implementations of the word-count application to not only use
   multiple, heterogeneous infrastructure (Sector versus DFS), but also
   to use different programming models (Sphere versus MapReduce).
-  Grid/Cloud NGS analysis experiments
    Building upon SAGA-based MapReduce, we have constructed an efficient
   pipeline for gene sequencing. This pipeline is capable of dynamic
   resource utilization and task/worker placement.
-  Hybrid cloud-Grid scientific applications and tools (autonomic
   schedulers) [with Manish Parashar, finished]
    Policy-based (objective driven) Autonomic Scheduler provides a
   system-level approach to hybrid grid-cloud usage.  FG has been used
   for the development and extension of such Autonomic Scheduling and
   application requirements.  We have integrated the distributed and
   heterogeneous resources of FG as a pool of resources which can be
   allocated by the policy-based Autonomic Scheduler (Comet). The
   Autonomic Scheduler dynamically determines and allocates instances to
   meet specific objectives, such as lowest time-to-completion, lowest
   cost etc. We also used FG supplement objective-driven pilot jobs on
   TeraGrid (ranger).
-  Investigate run time fluctuations of application kernels
    We attempt to explore and characterize run-time fluctuations for a
   given application kernel representative of both a large number of
   MPI/parallel workloads and workflows.  Fluctuation appears to be
   independent of the system load and a consequence of the complex
   interaction of the MPI library specifics and virtualization layer, as
   well as operating environment.  Thus we have been investigating
   fluctuations in application performance due to the cloud operational
   environment.  An explicit aim is to correlate these fluctuations to
   details of the infrastructure.  As it is difficult to discern or
   reverse engineer the specific infrastructure details on EC2 or other
   commercial infrastructure, FG has provided us a controlled and well
   understood environment at infrastructure scales that are not possible
   at the individual PI/resource level.

| 
|  *3. SAGA has also produced the following papers (selection):*
|   

See Refs:
`[1] <#ref1>`__,\ `[2] <#ref2>`__,\ `[3] <#ref3>`__,\ `[4] <#ref4>`__,\ `[5] <#ref5>`__

| 
| 
|  ***FuturePlans:***
| 
|  We will be continuing to use FG as a resource for SAGA development. 
Among other goals, we intend the following: to move the testing
infrastructure to other SAGA based components, like our PilotJob and
PilotData frameworks; to widen the set of middlewares used for testing
(again, keeping XSEDE and other PGIs in mind); to enhance the scope and
scale of our scalability testing; and to test and harden our deployment
and packaging procedures.
| 
| 
|   

--------------

References
~~~~~~~~~~

#. [fg-1975] `Sehgal, S. </biblio/author/175>`__, `M.
   Erdelyi </biblio/author/176>`__, `A. Merzky </biblio/author/177>`__,
   and `S. Jha </biblio/author/115>`__, "`Understanding
   application-level interoperability: Scaling-out MapReduce over
   high-performance grids and
   clouds </references/understanding-application-level-interoperability-scaling-out-mapreduce-over-high-performa>`__\ ",
   Future Generation Computer Systems, vol. 27, issue 5, 2011.
#. [fg-1976] `Luckow, A. </biblio/author/178>`__, `L.
   Lacinski </biblio/author/179>`__, and `S.
   Jha </biblio/author/115>`__, "`SAGA BigJob: An Extensible and
   Interoperable Pilot-Job Abstraction for Distributed Applications and
   Systems </references/saga-bigjob-extensible-and-interoperable-pilot-job-abstraction-distributed-applications-a>`__\ ",
   10th IEEE/ACM International Symposium on Cluster, Cloud and Grid
   Computing, 2010.
#. [fg-1977] `Luckow, A. </biblio/author/178>`__, and `S.
   Jha </biblio/author/115>`__, "`Abstractions for Loosely-Coupled and
   Ensemble-Based Simulations on
   Azure </references/abstractions-loosely-coupled-and-ensemble-based-simulations-azure>`__\ ",
   IEEE International Conference on Cloud Computing Technology and
   Science, 2010.
#. [fg-1978] `Kim, J. </biblio/author/180>`__, `S.
   Maddineni </biblio/author/181>`__, and `S.
   Jha </biblio/author/115>`__, "`Building Gateways for Life-Science
   Applications using the Dynamic Application Runtime Environment (DARE)
   Framework </references/building-gateways-life-science-applications-using-dynamic-application-runtime-environment>`__\ ",
   The 2011 TeraGrid Conference: Extreme Digital Discovery, 2011.
#. [fg-1979] `Kim, J. </biblio/author/180>`__, `S.
   Maddineni </biblio/author/181>`__, and `S.
   Jha </biblio/author/115>`__, "`Characterizing Deep Sequencing
   Analytics using BFAST: Towards a Scalable Distributed Architecture
   for Next-Generation Sequencing
   Data </references/characterizing-deep-sequencing-analytics-using-bfast-towards-scalable-distributed-archite>`__\ ",
   The Second International Workshop on Emerging Computational Methods
   for the Life Sciences, 06/2011.

Average: Select ratingPoorOkayGoodGreatAwesome

Your rating: 5 Average: 4.5 (2 votes)

EMI Unicore Tutorial
====================

What is EMI?
------------

`European Middleware Initiative <http://www.eu-emi.eu/>`__ (EMI) is a
software platform for high performance distributed computing.

It is at the core of grid middleware distributions used by scientific
research communities and distributed computing infrastructures all over
the world including WLCG--the Worldwide LHC Computing Grid--which
supports, for example, the search for the Higgs boson and new types of
matter searches of the physicists at LHC, together with other large
scientific challenges in astronomy, biology, computational chemistry and
other sciences.

Being a close collaboration among well-established grid middleware
providers and other specialized software providers, EMI proposes itself
as a leading platform for scientific grid computing and looks at
expanding outside of its natural environment.

EMI on FutureGrid
-----------------

EMI have created a number of Virtual Appliances which run on FutureGrid.
This tutorial describes how to use the the EMI UNICORE server tools.
Users can connect an EMI user interface node to the UNICORE instance
running on the VM in order to submit jobs, monitor them and retrieve
results.

The emi-unicore virtual appliance is available on the following
resources

-  Sierra
-  Hotel
-  Foxtrot

Launching the UNICORE appliance
-------------------------------

To launch the emi-unicore VM you must use the Nimbus cloud-client tool.
For instructions on how to install and configure Nimbus please see
the \ `Nimbus
tutorial <https://portal.futuregrid.org/tutorials/nimbus>`__.

Once you have a working Nimbus client you can search for the emi-unicore
appliance using the following command

::

    $ bin/cloud-client.sh --list

You should see a the emi-unicore appliance in the list. To instantiate
an emi-unicore appliance use the following command

::

    $ bin/cloud-client.sh --run --name <VM appliance name> --hours <number of hours>

For example, if the emi-unicore appliance is called
emi1-unicore-centos-5.3-x64-p1.gz and you want to run it for three
hours, use the following command

::

    $ bin/cloud-client.sh --run --name emi1-unicore-centos-5.3-x64-p1.gz --hours 3

Once the VM is running you should have a working UNICORE server. You can
log in as root using your ssh key and test the UNICORE services with the
command

::

    $ unicore-unicorex-status.sh

Using your UNICORE Server
-------------------------

The emi-unicore appliance contains the UNICORE server packages. In order
to submit jobs to this server you must have access to a user interface
machine with the emi-ui package installed.

This can be an external machine, or another VM, but it must run
Scientific Linux versions 5 or 6.

The emi-ui package can be obtained from the \ `EMI
repository <http://emisoft.web.cern.ch/emisoft/index.html>`__. EMI
packages are signed with the EMI GPG key, which can be obtained
from \ `http://emisoft.web.cern.ch/emisoft/dist/EMI/2/RPM-GPG-KEY-emi <http://emisoft.web.cern.ch/emisoft/dist/EMI/2/RPM-GPG-KEY-emi>`__.
Download the key and run rpm --import <keyfilename> in order to allow
packages signed with this key to be verified.

First configure the repository by installing the relevant yum repository
file:

-  `SL5 <http://emisoft.web.cern.ch/emisoft/dist/EMI/2/sl5/x86_64/base/emi-release-2.0.0-1.sl5.noarch.rpm>`__
-  `SL6 <http://emisoft.web.cern.ch/emisoft/dist/EMI/2/sl6/x86_64/base/emi-release-2.0.0-1.sl6.noarch.rpm>`__

You should now be able to install packages from the EMI repository. To
install the emi-ui type

::

    $ yum install emi-ui

To configure your emi user interface to use the UNICORE server running
in your emi-unicore virtual appliance you must edit the file
.ucc/preferences. If this file does not exist first run the command ucc
to create it.

Set the registry line to the uri of the EMI UNICORE instance, you will
need to ensure that the hostname matches that of the emi-unicore VM
which you previously instantiated. The hostname was given in the output
of the Nimbus cloud-client.sh --run command. For example, if your
UNICORE appliance was instantiated on host vm-7.sdsc.futuregrid.org then
you would set the registry line as follows in the .ucc/preferences file:

::

    registry=https://vm-7.sdsc.futuregrid.org:8080/DEFAULT-SITE/services/Registry?res=default_registry

You will also need to configure the UNICORE authentication. Your UNICORE
server is configured to allow access to the UNICORE "demo user". You can
find the keystore for this
user \ `here <http://www.eu-emi.eu/documents/10147/45270/user-keystore.jks>`__,
download it and put it in the .ucc/certs/ directory. Next set the
following parameters in the .ucc/preferences file:

::

    keystore=certs/user-keystore.jks password=the!user

You are now ready to begin using your EMI UNICORE installation. To test
it use the command

::

    $ ucc connect

Querying Resources on EMI UNICORE
---------------------------------

Before you run any jobs, you should investigate what resources are
available. You can query the UNICORE server using the following commands

::

    $ ucc list-sites $ ucc list-storages $ ucc list-applications

The first two commands will tell you about the computing and storage
resources available to you. The last command tells you the supported
applications which you are permitted to use. If you look in more detail
at output of the list-applications command you will see that it provides
a list of common applications along with their version number.

::

    $ ucc list-applications Applications on target system <DEFAULT-SITE> Korn shell Version M 1993-12-28 q C shell 6.14.00 Bash shell 3.1.16 POVRay 3.5 Python Script 2.4.2 Perl 5.8.8 Date 1.0 Custom executable 1.0

When you submit a job to a UNICORE server, you must specify which of
these applications the job will use. You can also upload data files or
scripts for execution by any of these commands. The details of which
application to use and any input and output files must be stored in a
job description file which is submitted to UNICORE for execution.

Runing a job and the job description file
-----------------------------------------

Let's get started with a very simple example. Create a file on your user
interface machine called date.u with the follwoing content:

::

    # simple job: run Date { ApplicationName: Date, ApplicationVersion: 1.0, }

This file tells UNICORE to execute the application Date version 1.0.

To submit this job we use the command 

::

    $ ucc run date.u -v

In the output from this command you should see a line specifying where
the output file was downloaded to, for example:

::

    [ucc run] Downloading remote file 'https://vm-7.sdsc.futuregrid.org:8080/DEFAULT-SITE/services/StorageManagement?res=f884b431-4660-4b7a-b91c-260b647604db#//stdout' -> /root/./205d109d-42a6-4cea-8cd3-c85ecc201e4d/stdout

This line indicates that the standard output of your job has been
downloaded to the file
/root/./205d109d-42a6-4cea-8cd3-c85ecc201e4d/stdout

You can view your job's output by typing

::

    $ cat /root/./205d109d-42a6-4cea-8cd3-c85ecc201e4d/stdout Thu Jul 12 10:32:29 EDT 2012

Congratulations, you have now succesfully run your first EMI UNICORE
grid job! Of course, this was a very simple job, so next we will go on
to look at how you can submit your own data and scripts for execution by
UNICORE.

Running your own scripts
------------------------

The job that you ran above didn't require any input or output files, and
used a native command on the server that does not require any input.
This is not the case with most useful jobs.

If you want to run your own script you will need to upload the script to
the UNICORE storage device and specify it in the job description file to
tell UNICORE which of your input files to pass to the interpreter.

Let's start with a simple bash script. The emi-unicore appliance comes
with a version of the Bash shell, run ucc list-appliances to check the
version number.

Next create a job description file to run this application, for example:

::

    # a job to run a bash script { ApplicationName: Bash shell, ApplicationVersion: 3.1.16, }

Create a script that you want to run and copy it to the UI machine. A
"Hello world" example is given below.

::

    echo "Hello World!" > output.txt

This script should be set as the Source in your job description file as
follows

::

    Environment: [ "SOURCE=remoteScript.sh", ],

Next you must tell ucc to upload the script with your job, and to
download the output file using the Imports and Exports 

::

    Imports: [ { From: "./script.sh", To: "remoteScript.sh" }, ], Exports: [ { From: "output.txt", To:"./output.txt" }, ]

Your full job description file will now look something like this

::

    # a job to run a bash script { ApplicationName: Bash shell, ApplicationVersion: 3.1.16,  Environment: [ "SOURCE=remoteScript.sh", ],  Imports: [ { From: "./script.sh", To: "remoteScript.sh" }, ], Exports: [ { From: "output.txt", To:"./output.txt" }, ] }

| Now run this job with the ucc run command. You can do the same with
Perl, Python or other scripting languages. Use ucc list-applications to
see a full list of available scripting languages.

Handling Data
-------------

If you have data files that you want to use with multiple jobs it can be
inefficient to stage them in with each job. In this case it may be
useful to copy the files to the UNICORE storage in advance. You can do
this using the ucc command line tool. Once done, your job can tell
UNICORE to copy the files to your local directory by specifying them in
your job description file.

To copy a file to a storage element first list the available storages:

::

    $ ucc list-storages Home https://vm-143.uc.futuregrid.org:8080/DEFAULT-SITE/services/StorageManagement?res=demo-Home

This tells you that your Home directory is available addressable via
this URI. You can use this URI to access your Home directory as follows

::

    $ ucc ls https://vm-143.uc.futuregrid.org:8080/DEFAULT-SITE/services/StorageManagement?res=demo-Home

::

    $ ucc put-file -s localfile.data -t https://vm-143.uc.futuregrid.org:8080/DEFAULT-SITE/services/StorageManagement?res=demo-Home#/remotefile.data

| Note that the -s parameter for ucc put-file specifies the source file
while -t specifies the target file.

Using the full URI is sometimes inconvenient, so you can use a shorter,
more intuitive format. This is also a URI, but you need to know only the
site (target system) name, and the storage or job id. For example

::

    unicore6://DEFAULT-SITE/Home/file

will resolve the "Home" storage at the target system named
"DEFAULT-SITE".

::

    $ ucc put-file -s localfile.data -t u6://DEFAULT-SITE/Home/testdata  $ ucc get-file -s u6://DEFAULT-SITE/Home/testdata -t newlocalfile.data

| Remember that you will need to copy the file to the local working
directory as part of your job in order to use it. To do this, include it
in the job description file as an import as follows:

::

    { From: "u6://DEFAULT-SITE/Home/testdata", To: "testdata"}

You can also refer to a job Uspace (the job's working directory) on a
given site. For this, you will need the unique ID of that job, which you
can get for example using the 'list-jobs' command. For example,

::

    unicore6://DEFAULT-SITE/1f3bc2e2-d814-406e-811d-e533f8f7a93b/outfile

refers to the file "outfile" in the working directory of the given job
on the "DEFAULT-SITE" target system. This may be useful for checking the
content of files during the job's execution, allowing you to steer the
analysis on the basis of partial results.

Resources
---------

In the Resources section of the .u script user can specify resources to
run the job on the remote system. The section may look as follows:

::

    Resources: { Memory: 128000000, Nodes: 1, CPUs: 8 , }

Running job on a set of files
-----------------------------

To run UNICORE on a set of files user can put jobs descriptions in one
directory (e.g. indir/) and use batch command: batch. -i argument
indicate source directory (with .u scripts), -o - directory for output
files:

::

    $ ucc batch -i indir -o outdir

 

Average: Select ratingPoorOkayGoodGreatAwesome

No votes yet

Tutorials
=========

| 
|  If you're looking for the Cloud Summer School 2012 (along with
excellent tutorial material), click on the icon below:
|   

|image132|

**Note:**\ This page is maintained by Renato Figueiredo from UF.

 

The following tutorials are broadly organized into topics, with each
tutorial classified by the user's target level of expertise with
FutureGrid (novice, intermediate, advanced). (If you are a tutorial
developer, for instructions on how to add a tutorial to this list,
please \ `refer to the TEOS
page <https://portal.futuregrid.org/outreach>`__).

| If you have corrections or suggestions related to our tutorial
content, please `fill out a help
request <https://portal.futuregrid.org/help>`__.
|   

Tutorial Topic 0: Accessing FutureGrid Resources
------------------------------------------------

-  `https://portal.futuregrid.org/accessing-futuregrid-resources-ssh <https://portal.futuregrid.org/accessing-futuregrid-resources-ssh>`__ [novice]

Tutorial Topic 1: Cloud Provisioning Platforms
----------------------------------------------

-  `Using Nimbus on
   FutureGrid <https://portal.futuregrid.org/tutorials/nimbus>`__
   [novice]
-  `Nimbus One-click Cluster
   Guide <https://portal.futuregrid.org/tutorials/nm2>`__ [intermediate]
-  `Using OpenStack Grizzly on
   FutureGrid <https://portal.futuregrid.org/manual/openstack/grizzly>`__
   [novice] ***\* NEW \****
-  `Using OpenStack Essex
   on FutureGrid <https://portal.futuregrid.org/tutorials/openstack>`__ [novice]
-  `Using Eucalyptus on
   FutureGrid <https://portal.futuregrid.org/tutorials/eucalyptus3>`__
   [novice]
-  `Connecting private network VMs across Nimbus clusters using
   ViNe <https://portal.futuregrid.org/contrib/simple-vine-tutorial>`__ [novice]
-  `IPOP1: (IP-over-P2P) Virtual Network Introductory
   Tutorial <https://portal.futuregrid.org/tutorials/ipop1>`__ [novice]
-  `IPOP2: Deploying your Own P2P Overlay for IPOP
   VPNs <https://portal.futuregrid.org/tutorials/ipop1>`__ [intermediate]

Tutorial Topic 2: Cloud Run-time Map/Reduce Platforms
-----------------------------------------------------

-  `Running Hadoop as a batch job using
   MyHadoop <https://portal.futuregrid.org/tutorials/running-hadoop-batch-job-using-myhadoop>`__ [novice]
-  `Running SalsaHadoop (one-click Hadoop) on HPC
   environment <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc>`__ [beginner]
-  `Running Twister on HPC
   environment <https://portal.futuregrid.org/twister-futuregrid-hpc>`__ [beginner]
-  `Running SalsaHadoop on
   Eucalyptus <https://portal.futuregrid.org/salsahadoop-futuregrid-cloud-eucalyptus>`__ [intermediate]
-  `Running <https://portal.futuregrid.org/tutorials/eucalyptus-and-twister-futuregrid>`__\ `FG-Twister
   on
   Eucalyptus <https://portal.futuregrid.org/tutorials/eucalyptus-and-twister-futuregrid>`__ [intermediate]
-  `Running One-click Hadoop WordCount on
   Eucalyptus <https://portal.futuregrid.org/tutorials/one-click-hadoop-wordcount-eucalyptus-futuregrid>`__
   [beginner]
-  `Running One-click Twister K-means on
   Eucalyptus <https://portal.futuregrid.org/tutorials/one-click-twister-k-means-eucalyptus-futuregrid>`__
   [beginner]

Tutorial Topic 3: Grid Appliances for Training, Education, and Outreach
-----------------------------------------------------------------------

-  `Running a Grid Appliance on your
   desktop <https://portal.futuregrid.org/tutorials/ga1>`__  [novice]
-  `Running a Grid Appliance on
   FutureGrid <http://portal.futuregrid.org/tutorials/ga9>`__ [novice]
-  `Running an OpenStack virtual appliance on
   FutureGrid <http://portal.futuregrid.org/tutorials/os1>`__ [novice]
-  `Running Condor tasks on the Grid
   Appliance <http://portal.futuregrid.org/tutorials/ga8>`__ [novice]
-  `Running MPI tasks on the Grid
   Appliance <https://portal.futuregrid.org/tutorials/mp1>`__ [novice]
-  `Running Hadoop tasks on the Grid
   Appliance <http://portal.futuregrid.org/tutorials/ga10>`__ [novice]
-  `Deploying virtual private Grid Appliance clusters using
   Nimbus <https://portal.futuregrid.org/tutorials/ga4>`__
   [intermediate]
-  `Building an educational appliance from Ubuntu
   10.04 <https://portal.futuregrid.org/tutorials/ga3>`__ [intermediate]
-  `Customizing and registering Grid Appliance images using
   Eucalyptus <https://portal.futuregrid.org/tutorials/ga7>`__
   [intermediate]

Tutorial Topic 4: High Performance Computing
--------------------------------------------

-  `Basic High Performance Computing </tutorials/hpc>`__ [novice]
-  `Running Hadoop as a batch job using
   MyHadoop </tutorials/running-hadoop-batch-job-using-myhadoop>`__
   [novice]
-  `Performance Analysis with Vampir </manual/performance/vampir>`__
   [advanced]
-  `Instrumentation and tracing with
   VampirTrace </manual/vampir/trace>`__ [advanced]

Tutorial Topic 5: Experiment Management
---------------------------------------

-  `Running interactive
   experiments <https://portal.futuregrid.org/tutorials/interactive-experiment-management>`__
   [novice]
-  `Running workflow experiments using
   Pegasus <https://portal.futuregrid.org/tutorials/workflow-experiment-management>`__ [novice]
-  `Pegasus 4.1 on FutureGrid
   Tutorial <https://portal.futuregrid.org/tutorials/pegasus-on-futuregrid-tutorial>`__ [novice]

Tutorial Topic 6: Image Management and Rain
-------------------------------------------

-  `Using Image Management and
   Rain <http://futuregrid.github.com/rain/quickstart.html>`__ [novice]
-  `Easy steps to generate and register an
   Image <https://portal.futuregrid.org/generate-and-register-os-image-futuregrid-using-fg-shell>`__
   [novice]
-  `Manual Image
   Customization <https://portal.futuregrid.org/manually-customize-image>`__
   [advanced]
-  `Register your VirtualBox image in
   OpenStack <https://portal.futuregrid.org/register-virtual-box-image-openstack>`__
   [intermediate]

Tutorial Topic 7:  Storage
--------------------------

-  `Using HPSS from
   FutureGrid <https://portal.futuregrid.org/tutorials/hpss>`__ [novice]

Other Tutorials and Educational Materials
-----------------------------------------

-  `Additional tutorials on FutureGrid-related
   technologies <https://portal.futuregrid.org/additional_tutorials>`__
-  `FutureGrid community educational
   materials <https://portal.futuregrid.org/community_edu_materials>`__
-  `CI Tutor performance
   tutorials <http://www.citutor.org/browse.php?access=&category=-1&search=performance&include=all&filter=Filter>`__
   (requires brief registration to view content)

| 

FutureGrid Grid Appliance for Nimbus and Eucalyptus
===================================================

**Summary:**

This tutorial provides step-by-step instructions on how to install
clients to access Eucalyptus and Nimbus clouds on FutureGrid using the
Grid appliance.

**Pre-requisites:**

`FutureGrid tutorial GA1 - Introduction to the Grid
Appliance <http://portal.futuregrid.org/tutorials/ga1>`__

**Hands-on tutorial**:

This tutorial is maintained at the Grid Appliance portal. See
`FutureGrid:clientappliance <http://www.grid-appliance.org/wiki/index.php/FutureGrid:clientappliance>`__.

One-click Hadoop WordCount on Eucalyptus FutureGrid
===================================================

I. Introduction
~~~~~~~~~~~~~~~

| This tutorial shows how to run a one-click Hadoop WordCount job on the
Eucalyptus platform of FutureGrid.
| 

II. Prerequisite
~~~~~~~~~~~~~~~~

| 1. FutureGrid HPC account: please apply via \ `FutureGrid
portal <../../user/register>`__ and \ `request a HPC
account <../../request-hpc-account>`__.
|  2. FutureGrid Eucalyptus account: please see `FutureGrid Eucalyptus
Tutorial <../../tutorials/eucalyptus3>`__ for detailed instructions.
|  3. FutureGrid Eucalyptus credentials zip file
(euca2-[username]-x509.zip) stored under user's home directory
|  4. Key pair created and added for use with Eucalyptus virtual
machines
| 
|  The following sections assume a user has created both an HPC account
and a Eucalpytus account under the username of *gaoxm*.
| 

III. Login to india.futuregrid.org
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| [gaoxm@129-79-49-98 ~]$ ssh -i .ssh/id\_rsa\_fg
india.futuregrid.org                      
|  Enter passphrase for key '.ssh/id\_rsa\_fg':
|  Last login: Sat May  5 02:17:33 2012 from
c-71-194-153-252.hsd1.in.comcast.net
|  ...
|  torque/2.5.5 version 2.5.5 loaded
|  moab version 5.4.0 loaded
|  euca2ools version 1.2 loaded
|  [gaoxm@i136 ~]$ cd eucalyptus/
|  [gaoxm@i136 eucalyptus]$ ls
|  cloud-cert.pem                 euca2-gaoxm-d108375b-pk.pem 
eucarc         hosts        nodes
|  euca2-gaoxm-d108375b-cert.pem  euca2-gaoxm-x509.zip        
gaoxm.private  jssecacerts  tmp.out
| 

IV. Download and unzip the “hadoopOneClick.zip” package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| [gaoxm@i136 test]$ wget
`http://mypage.iu.edu/~gao4/data/hadoopOneClick.zip <http://mypage.iu.edu/~gao4/data/hadoopOneClick.zip>`__
|  ...
|  [gaoxm@i136 test]$ ls
|  hadoopOneClick.zip
|  [gaoxm@i136 test]$ unzip hadoopOneClick.zip
| 

V. Run hadoop-one-click.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~

| [gaoxm@i136 test]$ cd hadoopOneClick
|  [gaoxm@i136 hadoopOneClick]$ ls
|  deploy-hadoop.sh     instanceIds.txt  publicIps.txt           
stop-hadoop.sh
|  hadoop-one-click.sh  ipHosts.txt      run-hadoop-wordcount.sh 
terminate-instances.sh
|  hosts                nodes.txt        start-instances.sh
|  [gaoxm@i136 hadoopOneClick]$ chmod +x \*.sh
|  [gaoxm@i136 hadoopOneClick]$ ./hadoop-one-click.sh -n 2 -t m1.small
-i emi-D778156D -k gaoxm -p ~/eucalyptus/gaoxm.private -l
`http://mypage.iu.edu/~gao4/data/grexp10.txt <http://mypage.iu.edu/~gao4/data/grexp10.txt>`__
-s
http://salsahpc.indiana.edu/tutorial/apps/hadoop-0.20.203.0-for-EucaVm.tar.gz
| 
|  This will run a MapReduce word-count job on a dynamically created
virtual Hadoop cluster on FutureGrid. The user needs to replace the *–k*
and *–p* parameter values with his/her key-pair name and private key
path. For detailed usage information, try
| 
|  [gaoxm@i136 hadoopOneClick]$ ./hadoop-one-click.sh -h
| 

VI. Verify output
~~~~~~~~~~~~~~~~~

| [gaoxm@i136 hadoopOneClick]$ ls outputs/
|  \_logs  part-r-00000  \_SUCCESS
|  [gaoxm@i136 hadoopOneClick]$ vim outputs/part-r-00000
| 

VII. Extensions
~~~~~~~~~~~~~~~

| To run other MapReduce jobs, replace *run-hadoop-wordcount.sh* with
new scripts, and change *hadoop-one-click.sh* to call the corresponding
scripts.
| 

One-click Twister K-means on Eucalyptus FutureGrid
==================================================

I. Introduction
~~~~~~~~~~~~~~~

| This tutorial shows how to run a one-click Twister K-means job on the
Eucalyptus platform of FutureGrid.
| 

II. Prerequisite
~~~~~~~~~~~~~~~~

| 1. FutureGrid HPC account, please apply via \ `FutureGrid
portal <https://portal.futuregrid.org/user/register>`__ and `request a
HPC account <https://portal.futuregrid.org/request-hpc-account>`__.
|  2. FutureGrid Eucalyptus account, please see \ `FutureGrid Eucalyptus
Tutorial <https://portal.futuregrid.org/tutorials/eucalyptus>`__ for
detailed instructions.
|  3. FutureGrid Eucalyptus credentials zip file
(euca2-[username]-x509.zip) stored under user's home directory.
|  4. Key pair created and added for use with Eucalyptus virtual
machines.
| 
|  The following sections assume a user has created both HPC account and
Eucalpytus account under the username of “gaoxm”.
| 

III. Login to india.futuregrid.org
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| [gaoxm@129-79-49-98 ~]$ ssh -i .ssh/id\_rsa\_fg
india.futuregrid.org                      
|  Enter passphrase for key '.ssh/id\_rsa\_fg':
|  Last login: Sat May  5 02:17:33 2012 from
c-71-194-153-252.hsd1.in.comcast.net
|  ...
|  torque/2.5.5 version 2.5.5 loaded
|  moab version 5.4.0 loaded
|  euca2ools version 1.2 loaded
|  [gaoxm@i136 ~]$ cd eucalyptus/
|  [gaoxm@i136 eucalyptus]$ ls
|  cloud-cert.pem                 euca2-gaoxm-d108375b-pk.pem 
eucarc         hosts        nodes
|  euca2-gaoxm-d108375b-cert.pem  euca2-gaoxm-x509.zip        
gaoxm.private  jssecacerts  tmp.out
| 

IV. Download and unzip the “twisterOneClick.zip” package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| [gaoxm@i136 test]$
wget \ `http://mypage.iu.edu/~gao4/data/twisterOneClick.zip <http://mypage.iu.edu/~gao4/data/hadoopOneClick.zip>`__
|  ...
|  [gaoxm@i136 test]$ ls
|  hadoopOneClick  hadoopOneClick.zip  twisterOneClick.zip
|  [gaoxm@i136 test]$ unzip twisterOneClick.zip
| 

V. Run twister-one-click.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| [gaoxm@i136 test]$ cd twisterOneClick
|  [gaoxm@i136 twisterOneClick]$ ls
|  deploy-twister.sh  instanceIds.txt  publicIps.txt         
stop-twister.sh
|  hostnames.txt      ipHosts.txt      run-twister-kmeans.sh 
terminate-instances.sh
|  hosts              nodes.txt        start-instances.sh    
twister-one-click.sh
|  [gaoxm@i136 twisterOneClick]$ chmod +x \*.sh
|  [gaoxm@i136 twisterOneClick]$ ./twister-one-click.sh -n 2 -t m1.small
-i emi-D778156D -k gaoxm -p ~/eucalyptus/gaoxm.private
-l\ `http <http://salsahpc.indiana.edu/tutorial/apps/Twister-0.9.tar.gz>`__\ `://salsahpc.indiana.edu/tutorial/apps/Twister-0.9.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/Twister-0.9.tar.gz>`__ -a
http://www.iterativemapreduce.org/apache-activemq-5.4.2-bin.tar.gz
| 
|  This will run a MapReduce K-means job on a dynamically created
virtual Twister cluster on  FutureGrid. The user needs to replace the
“–k” and “–p” parameter values with his/her key-pair name and private
key path. For detailed usage information, try
| 
|  [gaoxm@i136 twisterOneClick]$ ./twister-one-click.sh -h
| 

VI. Verify results in the standard output of the scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Calling run\_kmeans.sh on 149.165.159.140...
|  JobID: kmeans-map-reduce9ec9eaa2-9731-11e1-80d7-156f25bd362a
|  May 6, 2012 4:11:57 AM
org.apache.activemq.transport.failover.FailoverTransport doReconnect
|  INFO: Successfully connected
to \ `tcp://master:61616 <https://master:61616/>`__
|  0    [main] INFO  cgl.imr.client.TwisterDriver  - Configure Mappers
through the partition file, please wait....
|  1975 [main] INFO  cgl.imr.client.TwisterDriver  - Configuring Mappers
through the partition file is completed.
|  250.77056136584878 , 125.15021341387315 , 249.21561041359857 ,
|  246.74715176402833 , 375.350251646343 , 249.17570173022511 ,
|  Total Time for kemeans : 6.808
|  Total loop count : 15
|  6260 [main] INFO  cgl.imr.client.TwisterDriver  - MapReduce
computation termintated gracefully.
|  ------------------------------------------------------
|  Kmeans clustering took 6.841 seconds.
|  ------------------------------------------------------
| 

VII. Extensions
~~~~~~~~~~~~~~~

| To run other iterative MapReduce jobs, replace run-twister-kmeans.sh
with new scripts, and change twister-one-click.sh to call the
corresponding scripts.
| 
| 

Register Virtual Box Image on OpenStack
=======================================

In this tutorial we explain how to convert a Virtual Box image to kvm
format and then register it on OpenStack.

Prerequisites
-------------

There is two main prerequisites for your images to work with OpenStack

Disable SELinux (Only for RedHat-based Linux like CentOS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the file /etc/selinux/config and set the SELINUX option to disabled

::

    SELINUX=disabled

Configuring the image network interface (eth0) for DHCP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Ubuntu, you edit the file /etc/network/interfaces and configure eth0
to:

::

    auto eth0
    iface eth0 inet dhcp

In CentOS, you edit the file /etc/sysconfig/network-scripts/ifcfg-eth0
and make sure it contains:

::

    DEVICE=eth0
    BOOTPROTO=dhcp
    ONBOOT=yes

Configure the image to allow OpenStack to inject the ssh key 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Ubuntu (it may not be needed for Ubuntu, but it is recomended)

.. code:: rteindent2

    $ sudo apt-get install cloud-init curl

-  CentOS. Edit the file /etc/rc.local

.. code:: rteindent2

    route del -net 169.254.0.0 netmask 255.255.0.0 dev eth0
    # load pci hotplug for dynamic disk attach in KVM (for EBS)
    depmod -a
    modprobe acpiphp

    # simple attempt to get the user ssh key using the meta-data service
    mkdir -p /root/.ssh
    echo >> /root/.ssh/authorized_keys
    curl -m 10 -s http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key | grep 'ssh-rsa' >> /root/.ssh/authorized_keys
    echo "AUTHORIZED_KEYS:"
    echo "************************"
    cat /root/.ssh/authorized_keys
    echo "************************"

Configure udev persistent rules (only CentOS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit the file /etc/udev/rules.d/70-persistent-net.rules, delete
everything and add:

::

    ACTION=="add",SUBSYSTEM=="net", IMPORT{program}="/lib/udev/rename_device"
    SUBSYSTEM=="net", RUN+="/etc/sysconfig/network-scripts/net.hotplug"

Convert your virtual box image to raw format
--------------------------------------------

::

    VBoxManage clonehd /path/to/imagefile/vboximage.vdi /path/to/rawimage.img --format raw

Make sure that you specify the full path. Otherwise, you may experience
errors and the new image will be placed in  ~/.VirtualBox/HardDisks/

Convert the image to qcow2 format (optional)
--------------------------------------------

This step is optional, but it is recommended if your image as a
considerable size because the qcow2 format will compress your image.
Nevertheless, it will takes a while to finish this command. As example
my 8GB image took a couple of hours to get ready and was compressed to
less than 6 GB.

::

    qemu-img convert -f raw rawimage.img -O qcow2 qcow2image.img

Test your image
---------------

If you are in a computer with graphical interface, the easiest way to
test it is by executing the following command. This command will open a
window and you will see if your image boots correctly.

::

    kvm -hda rawimage.img -m 1024

or

::

    kvm -hda qcow2image.img -m 1024

From now on, we refer only to the rawimage.img, but it works in the same
way with the qcow2image.img.

Transfer your Image to India
----------------------------

::

    $ scp rawimage.img <username>@india.futuregrid.org:/N/u/<username>/

Log into India
--------------

::

    $ ssh <username>@india.futuregrid.org

::

Upload your image to OpenStack
------------------------------

First, we need to load the euca2ools module that contains the command
line interface to interact with OpenStack. Then we need to load our own
credentials that are typically in a novarc file. Finally you update and
register the image. Although, we are going to briefly explain these
steps here, this is part of the OpenStack tutorial that can be found
in \ `https://portal.futuregrid.org/tutorials/openstack <https://portal.futuregrid.org/tutorials/openstack>`__.

::

    $ module load euca2ools
    $ source ~/novarc

Upload the image

::

    $ euca-bundle-image -i rawimage.img 

    Checking image
    Encrypting image
    Splitting image...
    Part: rawimage.img.part.00
    Part: rawimage.img.part.01
    Part: rawimage.img.part.02
    .....
    Generating manifest /tmp/rawimage.img.manifest.xml

At the end you get a manifest file that you use in the next step. You
also need to specify a bucket name (option -b). We can use our username
(jdiazz in my case), but it can be any other string.

::

    $ euca-upload-image -m /tmp/rawimage.img.manifest.xml -b jdiazz

    Checking bucket: jdiaz
    Uploading manifest file
    Uploading part: rawimage.img.part.00
    Uploading part: rawimage.img.part.01
    Uploading part: rawimage.img.part.02
    .....
    Uploaded image as jdiazz/rawimage.img.manifest.xml

Finally we register the image.

::

    $ euca-register jdiazz/rawimage.img.manifest.xml

    IMAGE ami-00000058

From this last command we get the ami-ID that identifies the image in
OpenStack (marked in yellow). You will need this to start instances.

Checking Status Image
---------------------

You cannot run instances until your image is in available status. You
can check the status of your image with the euca-describe-images
command. This command can take some time to respond because the system
will be busy processing your image.

::

    $ euca-describe-images ami-00000058

Test Image in OpenStack
-----------------------

For this step we recomend to go to the OpenStack tutorial where we
explain how to create a key-pair and run an instance with our image.
Please
see \ `https://portal.futuregrid.org/using-openstack-futuregrid#key\_management <https://portal.futuregrid.org/using-openstack-futuregrid#key_management>`__

Running the instance can be something like this:

::

    $ euca-run-instances -k jdiaznova ami-00000058 -t m1.large

where jdiaznova is the key name of my openstack key pairs. This key will
allow us to ssh into the image. Please refer to the OpenStack tutorial
for more information.

Troubleshooting
---------------

One problem of this way of using our images is that we cannot use
euca-get-console-output command to debug the boot process of the images.
Therefore it makes more complicated solving runtime problems. However,
if your image boots properly when doing the "Test your Image" section,
it should work also on OpenStack and the only problem could be wrong
configuration of network interface or SELinux enabled.

Notes:
------

This tutorial has been tested with Ubuntu 12 and CentOS 6 using
OpenStack Essex. 

Virtual Appliances
==================

**Overview:**
~~~~~~~~~~~~~

| Virtual appliances are virtual machine images encapsulating
pre-installed, pre-configured software that can be easily deployed on
cloud resources. Users of FutureGrid can use public appliance images
posted by other users, as well as contribute to the repository of
images.
| 
|  This page provides a summary of community-provided virtual appliances
that are available for use on FutureGrid. If you have created a virtual
appliance and you would like to advertise its availability and features
with the community, feel free to edit this page and include information
about your appliance.

 **Creating Your Own Appliance:**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Any FutureGrid user with Eucalyptus or Nimbus accounts can create and
register an appliance. The approach is similar in both cases: you can
upload an existing image into FutureGrid (e.g. from another Eucalyptus
or Nimbus cloud, or an image you create on your own computer), or you
can customize an instance interactively in FutureGrid and save it in a
FutureGrid resource.
| 

***Nimbus***:
^^^^^^^^^^^^^

| You can upload a "common" image so it becomes available to others in a
FutureGrid cloud resource - to do this, add the flag --common to the
cloud\_client.sh command line when you transfer an image (ensure you are
using cloud client version 020 or above).  You can also save a Nimbus
instance that you are using interactively (through ssh) as an image.
Please refer to the `manual for
cloud\_client.sh <http://www.nimbusproject.org/docs/current/clouds/cloudquickstart.html>`__ and
the  `Nimbus tutorial <http://portal.futuregrid.org/tutorials/nimbus>`__
for instructions.
| 

***Eucalyptus***: 
^^^^^^^^^^^^^^^^^^

| Please refer to `FutureGrid tutorial
GA7 <https://portal.futuregrid.org/tutorials/ga7>`__.
| 

**Reusing an Existing Appliance:**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several appliances already available on FutureGrid. The table
below summarizes a list of appliances, where they are available, and
their image names. If you have an appliance that you would like to add
to this list, please add it to the table.

 *Editing tips for the table:*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *You can add rows to the table by right-clicking the last row of the
   table and selecting Row->Insert Row After*
-  *If you make a mistake (e.g., deleting a row), you can undo it by
   pressing CTRL-Z*
-  *You need to click on the Submit button so your changes take effect*
-  *You can `create a community
   page <https://portal.futuregrid.org/node/add/page-community>`__
   explaining your appliance and its usage in more depth, and can link
   to it from this page*

| 

+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------+------------------------------+
| **Appliance name**                                                                            | **Appliance description**                                                                       | **FutureGrid system(s) available**   | **Appliance ID**                                          | **Installed                  |
|                                                                                               |                                                                                                 |                                      |                                                           |  by (FutureGrid user ID)**   |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------+------------------------------+
| `Grid Appliance <https://portal.futuregrid.org/tutorials/ga9>`__                              | Self-configures Condor/MPI/Hadoop virtual clusters for training/education                       | alamo, india                         | grid-appliance-2.05.03.gz (alamo), emi-E4ED1880 (india)   | panoat                       |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------+------------------------------+
| `OpenStack                                                                                    | Deploys a single-node OpenStack compute virtual cloud                                           | alamo                                | openstack-ubuntu-10.10-amd64.img                          | menghan                      |
|  Appliance <https://portal.futuregrid.org/tutorials/os1>`__                                   |                                                                                                 |                                      |                                                           |                              |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------+------------------------------+
| `ViNe Appliance <https://portal.futuregrid.org/contrib/simple-vine-tutorial>`__               | Deploys the ViNe virtual network overlay to connect private-address VMs in sierra and foxtrot   | sierra, foxtrot                      | centos-5.5-x64-vine.gz                                    | menghan                      |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------+------------------------------+
| `Twister Appliance <https://portal.futuregrid.org/contrib/fg-twister-appliance-tutorial>`__   | Deploys a virtual private cluster running the Twister iterative MapReduce system                | india                                | emi-F0B8194D                                              | jemitche                     |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------+------------------------------+
| (Add your appliance here)                                                                     |                                                                                                 |                                      |                                                           |                              |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------+------------------------------+
|                                                                                               |                                                                                                 |                                      |                                                           |                              |
+-----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------+------------------------------+

| 

Average: Select ratingPoorOkayGoodGreatAwesome

No votes yet

Development Projects
====================

| FutureGrid provides a number of software development projects. Much
(but not all) of our work we have just begun to move to github.
| 
|  The documentation for these projects can be found
at \ `http://futuregrid.github.com/doc/ <http://futuregrid.github.com/doc/>`__
.
| 
| 
|   As a part of FutureGrid, many other projects perform development as
well. These include Inca, Nimbus, Pegasus, PAPI, Vampir, as well as a
project called hostlists. These projects either maintain their own
repositories or use the FutureGrid sourceforge repository.
| 
|   Actvities on github include:
| 

Rain

    -  A project to do bare metal and VM-based dynamic provisioning
    -  Documentation: \ `http://futuregrid.github.com/rain <http://futuregrid.github.com/rain>`__
    -  Source: \ `https://github.com/futuregrid/rain <https://github.com/futuregrid/rain>`__

Cloud Shift

    -  A project to move resources between different cloud and HPC
       services
    -  Documentation: todo
    -  Source: todo
    -  Issues: todo

Cloud Metric

    -  A project to measure and display metric information about usage
       and utilization of your cloud
    -  Documentation:\ `https://portal.futuregrid.org/doc/metric/index.html <https://portal.futuregrid.org/doc/metric/index.html>`__
    -  Source: \ `https://github.com/futuregrid/futuregrid-cloud-metrics <https://github.com/futuregrid/futuregrid-cloud-metrics>`__
    -  Issues: \ `https://github.com/futuregrid/futuregrid-cloud-metrics/issues <https://github.com/futuregrid/futuregrid-cloud-metrics/issues>`__

Virtual Cluster

    -  A project to create a SLURM-based cluster in your cloud and run
       MPI jobs on it
    -  Documentation: \ `http://futuregrid.github.com/virtual-cluster <http://futuregrid.github.com/virtual-cluster>`__
    -  Source: \ `https://github.com/futuregrid/virtual-cluster <https://github.com/futuregrid/virtual-cluster>`__
    -  Issues: \ `https://github.com/futuregrid/virtual-cluster/issues <https://github.com/futuregrid/virtual-cluster/issues>`__

Authentication

    -  A project to unify authentication between Eucalyptus, OpenStack,
       and Nimbus
    -  Documentation: todo
    -  Source: todo
    -  Issues: todo

Mediawiki Jira Issues

    -  A project that can be used to automatically create reports based
       on comments submitted to jira, returning jira issues in
       mediawiki, and executing arbitrary queries from mediawiki to jira
       that are rendered in mediawiki
    -  Documentation: todo
    -  Source: todo
    -  Issues: todo

      

Appendix
========

Upgrading Nimbus On FG clusters
===============================

Disclaimer
----------

| This document provides guidelines on how to upgrade Nimbus on
FutureGrid sites.  It is not a definitive guide to upgrading Nimbus
anywhere.  An admin's own skills and intuition should be in full force
while following this guide.  This page should be considered little more
than the notes from one effective upgrade from 2.7 to 2.8.

Upgrading Workspace Service and Cumulus
---------------------------------------

| First create a source directory and download the latest Nimbus release
from
`http://www.nimbusproject.org/downloads/ <http://www.nimbusproject.org/downloads/>`__,
and untar the distributions:

::

    mkdir ~/src
    wget http://www.nimbusproject.org/downloads/nimbus-iaas-2.8-src.tar.gz
    tar -xzf nimbus-iaas-2.8-src.tar.gz
    wget http://www.nimbusproject.org/downloads/nimbus-iaas-controls-2.8.tar.gz
    tar -zxf nimbus-iaas-controls-2.8.tar.gz

| For convenience set the following variables:

::

    export OLD_NIMBUS=<path to old nimbus install>
    export NEW_NIMBUS=<path to new nimbus install>

| Make sure that the old install is not running:

::

    $OLD_NIMBUS/bin/nimbusctl stop

Install the new Nimbus. If you are on an old distribution such as CentOS
5, you might need to set the OLD\_OPENSSL\_VERSION environment variable.
If you run into Java OOM issues, export the following variable: export
ANT\_OPTS=-Xmx1024M. When asked any questions just hit enter:

::

    ./install $NEW_NIMBUS

Run the following commands to transfer over the env. **\*NOTE\*** please
check that you are ok with these commands first, do not blindly copy and
paste them. ***These commands DELETE things!***

::

    rm -rf $NEW_NIMBUS/var/ca
    rm $NEW_NIMBUS/var/hostcert.pem
    rm $NEW_NIMBUS/var/hostkey.pem
    rm $NEW_NIMBUS/var/keystore.jks

    cp $OLD_NIMBUS/nimbus-setup.conf $NEW_NIMBUS/nimbus-setup.conf

    export PREVIOUS_NIMBUS_HOME_VALIDATED=$OLD_NIMBUS
    $NEW_NIMBUS/bin/nimbus-configure --conf $NEW_NIMBUS/nimbus-setup.conf  --import-cumulusdb
    $NEW_NIMBUS/bin/nimbus-configure --conf $NEW_NIMBUS/nimbus-setup.conf --import-prev

    cp $OLD_NIMBUS/services/etc/nimbus/workspace-service/metadata.conf $NEW_NIMBUS/services/etc/nimbus/workspace-service/metadata.conf

Import SSH keys from the Elastic interface:

::

    sqlite3 $OLD_NIMBUS/services/var/nimbus/elastic.db
    sqlite> .output /N/u/nimbus/ssh_keypairs
    sqlite> .dump ssh_keypairs
    sqlite> .quit

    sqlite3 $NEW_NIMBUS/services/var/nimbus/elastic.db
    sqlite> .read /N/u/nimbus/ssh_keypairs
    sqlite> .quit

Manually check the remaining differences in the configuration files. 
The differences will be very site dependent so put on your thinking
cap.  The following script will diff out all the conf files.  Go through
the output and make sure you merge over all the needed changes for your
site

::

    cd $OLD_NIMBUS
    confs=`find . -name '*.conf'`
    for c in $confs
    do
        diff -q -u $OLD_NIMBUS/$c $NEW_NIMBUS/$c

::

    done

| Now verify that services/etc/nimbus-context-broker/jndi-config.xml has
the right caCertPath and caKeyPath (in almost every case it will not
have the right values).
|  Also verify that services/etc/globus\_wsrf\_core/server-config.wsdd
has the right logicalHost.
|  Also verify the customizations
in services/etc/nimbus/workspace-service/other/authz-callout-ACTIVE.xml
are still enabled (for example cp propagation).
| 
|  Also check $NEW\_NIMBUS/cumulus/etc/cumulus.ini for the backend
data\_dir if you are using type 'posix' (which you likely are).
|  And check
$NEW\_NIMBUS/services/etc/nimbus/workspace-service/cumulus.conf for the
cumulus.authz.db and cumulus.repo.dir settings.
| 
|  Now you must load up the new Nimbus install with the backends from
the old install.  The following python script can help with that task. 
Simply give it two arguments: $OLD\_NIMBUS $NEW\_NIMBUS
| 
| 
`https://raw.github.com/nimbusproject/nimbus/master/docs/src/admin/reload.py <https://raw.github.com/nimbusproject/nimbus/master/docs/src/admin/reload.py>`__

Upgrading Workspace Control
---------------------------

Set up the workspace control nodes by doing the following:

#. Move the old install from /opt/nimbus to /opt/nimbus2.7
#. Create the directory /opt/nimbus2.8 and have it owned by the nimbus
   user and group
#. Create a symlink from /opt/nimbus to /opt/nimbus2.8

| Now copy the old working workspace control code from a working VMM
node to the source directory:

::

    scp -r working_node:/opt/nimbus2.7 ~/src/

| Just like in the above step, run the following diff script to find
configuration differences, give it the full path to nimbus2.7 as the
first argument and the full path to the new distribution at the second:

::

    cd $1
    confs=`find . -name '*.conf'`
    for c in $confs
    do
        diff -u $1/$c $2/$c

::

    done

| Merge all of the differences.  Check out the following files and merge
the differences:
| 
|  libexec/workspace-control/mount-alter.sh
|  lantorrent/etc/\*
|  etc/workspace-control/libvirt\_template.xml
| 
|  Make sure that everything in nimbus2.7/var/workspace-control/kernels
is also in
nimbus-iaas-controls-2.8/workspace-control/var/workspace-control/kernels
| 
|  scp everything under nimbus-iaas-controls-2.8/workspace-control to
all VMM nodes:/opt/nimbus/

FAQ
===

FAQ
===

`https://portal.futuregrid.org/faq <https://portal.futuregrid.org/faq>`__

.. |image0| image:: https://portal.futuregrid.org/sites/default/files/u30/fg-logo-md.gif
.. |image1| image:: https://portal.futuregrid.org/sites/default/files/u30/nsf.jpg
.. |image2| image:: https://portal.futuregrid.org/sites/default/files/images/lilly_endowment.jpg
.. |image3| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/iu-logo-50x64.jpeg
.. |image4| image:: https://portal.futuregrid.org/sites/default/files/resize/images/FutureGrid_iDataPlex_Cray_IU-sm-640x425.jpg
.. |image5| image:: https://portal.futuregrid.org/sites/default/files/resize/images/Cray_XT5m_Front_closed-small-427x640.jpg
.. |image6| image:: https://portal.futuregrid.org/sites/default/files/images/FutureGrid%20Logocal%20v3.png
.. |image7| image:: https://portal.futuregrid.org/sites/default/files/resize/images/Juniper%20EX8208-140x184.png
.. |image8| image:: https://portal.futuregrid.org/sites/default/files/u23/futuregrid-physical.png
.. |image9| image:: https://portal.futuregrid.org/sites/default/files/u23/futuregrid-topology.png
.. |image10| image:: https://portal.futuregrid.org/sites/default/files/images/Spirent%20XGEM.png
.. |image11| image:: https://portal.futuregrid.org/sites/default/files/images/FutureGrid%20Logocal%20v3.png
.. |image12| image:: https://portal.futuregrid.org/sites/default/files/images/status_incapart.PNG
   :target: http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp
.. |image13| image:: https://portal.futuregrid.org/sites/default/files/ScreenSnapz.jpg
   :target: http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid
.. |image14| image:: https://portal.futuregrid.org/sites/default/files/ganglia.png
   :target: http://ganglia.futuregrid.org
.. |image15| image:: https://portal.futuregrid.org/sites/default/files/images/large_status_nocmap.PNG
   :target: http://noc.futuregrid.org
.. |image16| image:: https://portal.futuregrid.org/sites/default/files/u23/Screen%20shot%202011-01-14%20at%207.48.06%20PM.png
   :target: http://inca.futuregrid.org
.. |image17| image:: https://portal.futuregrid.org/sites/default/files/u23/Screen%20shot%202011-04-07%20at%203.23.05%20PM.png
   :target: https://portal.futuregrid.org/monitoring/cloud
.. |image18| image:: https://portal.futuregrid.org/sites/default/files/screenshot-for-status-small.png
   :target: https://portal.futuregrid.org/metrics
.. |image19| image:: https://portal.futuregrid.org/sites/default/files/fg-sys-sw-ver.PNG
   :target: http://inca.futuregrid.org:8080/inca/HTML/rest/HPC/FutureGrid
.. |image20| image:: https://portal.futuregrid.org/sites/default/files/u15/nimbus-usage.png
   :target: http://inca.futuregrid.org/nimbus-stats
.. |image21| image:: https://portal.futuregrid.org/sites/default/files/u30/cygwim1.png
.. |image22| image:: https://portal.futuregrid.org/sites/default/files/u30/cygwin2.png
.. |image23| image:: https://portal.futuregrid.org/sites/default/files/u30/cygwinfirst.png
.. |image24| image:: https://portal.futuregrid.org/sites/default/files/u23/register-sshkey.png
   :target: https://portal.futuregrid.org/user/23/ssh-keys
.. |image25| image:: https://portal.futuregrid.org/sites/default/files/u30/portalLogin_0.png
.. |image26| image:: https://portal.futuregrid.org/sites/default/files/u30/portalsshkey.png
.. |image27| image:: https://portal.futuregrid.org/sites/default/files/u30/portalclikaddkey_0.png
.. |image28| image:: https://portal.futuregrid.org/sites/default/files/u30/portalkeypaste_0.png
.. |image29| image:: https://portal.futuregrid.org/sites/default/files/u30/icl_footer.gif
.. |image30| image:: https://portal.futuregrid.org/sites/default/files/images/otf_0.png
.. |image31| image:: https://portal.futuregrid.org/sites/default/files/images/open_file.png
.. |image32| image:: https://portal.futuregrid.org/sites/default/files/images/cancel_loading_resize.png
.. |image33| image:: https://portal.futuregrid.org/sites/default/files/images/Startup.png
.. |image34| image:: https://portal.futuregrid.org/sites/default/files/images/Display_arranging_a.png
.. |image35| image:: https://portal.futuregrid.org/sites/default/files/images/Display_arranging_b.png
.. |image36| image:: https://portal.futuregrid.org/sites/default/files/images/Custom_arrangement.png
.. |image37| image:: https://portal.futuregrid.org/sites/default/files/images/close_display.png
.. |image38| image:: https://portal.futuregrid.org/sites/default/files/images/Undocking_1.png
.. |image39| image:: https://portal.futuregrid.org/sites/default/files/images/Undocking_2.png
.. |image40| image:: https://portal.futuregrid.org/sites/default/files/images/Resize_labels.png
.. |image41| image:: https://portal.futuregrid.org/sites/default/files/images/Zooming.png
.. |image42| image:: https://portal.futuregrid.org/sites/default/files/images/Zoom_toolbar.png
.. |image43| image:: https://portal.futuregrid.org/sites/default/files/images/icon_master_tl.png
.. |image44| image:: https://portal.futuregrid.org/sites/default/files/images/icon_process_tl.png
.. |image45| image:: https://portal.futuregrid.org/sites/default/files/images/icon_counter_tl.png
.. |image46| image:: https://portal.futuregrid.org/sites/default/files/images/icon_radar.png
.. |image47| image:: https://portal.futuregrid.org/sites/default/files/images/icon_function_summ.png
.. |image48| image:: https://portal.futuregrid.org/sites/default/files/images/icon_message_summ.png
.. |image49| image:: https://portal.futuregrid.org/sites/default/files/images/icon_process_summ.png
.. |image50| image:: https://portal.futuregrid.org/sites/default/files/images/icon_matrix.png
.. |image51| image:: https://portal.futuregrid.org/sites/default/files/images/icon_calltree.png
.. |image52| image:: https://portal.futuregrid.org/sites/default/files/images/icon_legend.png
.. |image53| image:: https://portal.futuregrid.org/sites/default/files/images/icon_context.png
.. |image54| image:: https://portal.futuregrid.org/sites/default/files/images/icon_marker.png
.. |image55| image:: https://portal.futuregrid.org/sites/default/files/images/Master_timeline.png
.. |image56| image:: https://portal.futuregrid.org/sites/default/files/images/Process_timeline.png
.. |image57| image:: https://portal.futuregrid.org/sites/default/files/images/collectives.png
.. |image58| image:: https://portal.futuregrid.org/sites/default/files/images/burst.png
.. |image59| image:: https://portal.futuregrid.org/sites/default/files/images/marker-multiple.png
.. |image60| image:: https://portal.futuregrid.org/sites/default/files/images/marker-template.png
.. |image61| image:: https://portal.futuregrid.org/sites/default/files/images/io-multiple.png
.. |image62| image:: https://portal.futuregrid.org/sites/default/files/images/io-single.png
.. |image63| image:: https://portal.futuregrid.org/sites/default/files/images/io-single-selected.png
.. |image64| image:: https://portal.futuregrid.org/sites/default/files/images/Counter_data_timeline.png
.. |image65| image:: https://portal.futuregrid.org/sites/default/files/images/performance_radar_find_function.png
.. |image66| image:: https://portal.futuregrid.org/sites/default/files/images/performance_radar_set_counter.png
.. |image67| image:: https://portal.futuregrid.org/sites/default/files/images/Call_tree.png
.. |image68| image:: https://portal.futuregrid.org/sites/default/files/images/Function_summary.png
.. |image69| image:: https://portal.futuregrid.org/sites/default/files/images/Process_summary.png
.. |image70| image:: https://portal.futuregrid.org/sites/default/files/images/Messagesummary.png
.. |image71| image:: https://portal.futuregrid.org/sites/default/files/images/Communication_matrix_view.png
.. |image72| image:: https://portal.futuregrid.org/sites/default/files/images/Function_legend.png
.. |image73| image:: https://portal.futuregrid.org/sites/default/files/images/Marker_view.png
.. |image74| image:: https://portal.futuregrid.org/sites/default/files/images/Context_view.png
.. |image75| image:: https://portal.futuregrid.org/sites/default/files/images/context_compare.png
.. |image76| image:: https://portal.futuregrid.org/sites/default/files/images/process_filter.png
.. |image77| image:: https://portal.futuregrid.org/sites/default/files/images/pref_general.png
.. |image78| image:: https://portal.futuregrid.org/sites/default/files/images/pref_appearance.png
.. |image79| image:: https://portal.futuregrid.org/sites/default/files/resize/u28/CUBLAS2-800x280.png
.. |image80| image:: https://portal.futuregrid.org/sites/default/files/resize/u28/cudaarchi_threadsmode-544x300.png
.. |image81| image:: https://portal.futuregrid.org/sites/default/files/resize/u28/cudaMemoryArchitecture-500x173.png
.. |image82| image:: https://portal.futuregrid.org/sites/default/files/u28/cmeans_objective_function.gif
.. |image83| image:: https://portal.futuregrid.org/sites/default/files/u28/cmeans_uij_ck.gif
.. |image84| image:: https://portal.futuregrid.org/sites/default/files/u28/cmeans_ck.gif
.. |image85| image:: https://portal.futuregrid.org/sites/default/files/u28/cmeans_stop_condition.gif
.. |image86| image:: https://portal.futuregrid.org/sites/default/files/resize/u28/cmeansPerformance2-600x178.png
.. |image87| image:: https://portal.futuregrid.org/sites/default/files/images/nimbus_logo.png
   :target: http://www.nimbusproject.org/
.. |image88| image:: https://portal.futuregrid.org/sites/default/files/resize/euca_fg_login-290x240.png
.. |image89| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/Screen%20Shot%202013-03-06%20at%2012.47.32%20PM-201x200.png
   :target: http://futuregrid.github.com/rain/
.. |image90| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/Screen%20Shot%202013-03-06%20at%2012.51.48%20PM-200x200.png
   :target: http://futuregrid.github.com/rain/quickstart.html
.. |image91| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/Screen%20Shot%202013-03-06%20at%2012.47.32%20PM-201x200.png
   :target: http://futuregrid.github.com/rain/
.. |image92| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/Screen%20Shot%202013-03-06%20at%2012.51.48%20PM-200x200.png
   :target: http://futuregrid.github.com/rain/quickstart.html
.. |:!:| image:: http://www.opennebula.org/lib/images/smileys/icon_exclaim.gif
.. |image94| image:: https://portal.futuregrid.orghttps://portal.futuregrid.org/sites/default/files/resize/myHadoop-300x70.png
.. |Hadoop logo| image:: http://hadoop.apache.org/images/hadoop-logo.jpg
.. |image96| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image97| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image98| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image99| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image100| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image101| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image102| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image103| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image104| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image105| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image106| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image107| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image108| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image109| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image110| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image111| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image112| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image113| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image114| image:: http://www.iterativemapreduce.org/images/imrmodel.png
.. |image115| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image116| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image117| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image118| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image119| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image120| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image121| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image122| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image123| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image124| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image125| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image126| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image127| image:: https://portal.futuregrid.orghttps://portal.futuregrid.org/sites/default/files/u192/start_twister.jpg
.. |image128| image:: https://portal.futuregrid.orghttps://portal.futuregrid.org/sites/default/files/resize/u192/twister_kmeans-906x257.jpg
.. |Cloud site sample layouts.| image:: https://pegasus.isi.edu/wms/docs/4.0/images/fg-pwms-prefio.3.png
.. |image130| image:: https://portal.futuregrid.org/sites/default/files/u30/fg-logo-md.gif
.. |image131| image:: https://portal.futuregrid.org/sites/default/files/u30/fg-logo-md.gif
.. |image132| image:: https://portal.futuregrid.org/sites/default/files/u23/summerschool2012.png
   :target: https://portal.futuregrid.org/projects/241
