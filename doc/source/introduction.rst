**********************************************************************
Overview
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

Executive Summary 
---------------------------------------------------------------------

The FutureGrid Project (for citation see Section :ref:`my-how-to-cite`.) makes it possible for researchers to tackle complex research challenges in computer science related to the use and security of grids and clouds.  These include topics ranging from authentication, authorization, scheduling, virtualization, middleware design, interface design, and cybersecurity, to the optimization of grid-enabled and cloud-enabled computational schemes for researchers in astronomy, chemistry, biology, engineering, atmospheric science and epidemiology. The project team provides a significant new experimental computing grid and cloud test-bed, named FutureGrid, to the research community, together with user support for third-party researchers conducting experiments on FutureGrid.

The test-bed makes it possible for researchers to conduct experiments by submitting an experiment plan that is then executed via a sophisticated workflow engine, preserving the provenance and state information necessary to allow reproducibility.

The test-bed also includes a geographically distributed set of heterogeneous computing systems, a data management system that holds both metadata and a growing library of software images, and a dedicated network allowing isolatable, secure experiments. The test-bed supports virtual machine-based environments, as well as native operating systems for experiments aimed at minimizing overhead and maximizing performance.  The project partners integrate existing open-source software packages to create an easy-to-use software environment that supports the instantiation, execution, and recording of grid and cloud computing experiments.

One of the goals of the project is to understand the behavior and utility of cloud computing approaches. Researchers are able to measure the overhead of cloud technology by requesting linked experiments on both virtual and bare-metal systems. FutureGrid enables US scientists to develop and test new approaches to parallel, grid, and cloud computing, and compare and collaborate with international efforts in this area. The FutureGrid project provides an experimental platform that accommodates batch, grid, and cloud computing, allowing researchers to attack a range of research questions associated with optimizing, integrating and scheduling the different service models. The FutureGrid also provides a test-bed for middleware development and, because of its private network, allows middleware researchers to do controlled experiments under different network conditions and to test approaches to middleware that include direct interaction with the network control layer. Another component of the project is the development of benchmarks appropriate for grid computing, including workflow-based benchmarks derived from applications in astronomy, bioinformatics, seismology, and physics.

The FutureGrid forms part of NSF's high-performance cyberinfrastructure. It increases the capability of the XSEDE to support innovative computer science research requiring access to lower levels of the grid software stack, the networking software stack, and to virtualization and workflow orchestration tools.

Education and broader outreach activities include the dissemination of curricular materials on the use of FutureGrid, pre-packaged FutureGrid virtual machines configured for particular course modules, and educational modules based on virtual appliance networks and social networking technologies that focus on education in networking, parallel computing, virtualization and distributed computing. The project advances education and training in distributed computing at academic institutions with less diverse computational resources. It does this through the development of instructional resources that include preconfigured environments that provide students with sandboxed virtual clusters. These can be used for teaching courses in parallel, cloud, and grid computing. Such resources also provide academic institutions with a simple opportunity to experiment with cloud technology to see if such technology can enhance their campus resources. The FutureGrid project leverages the fruits of several software development projects funded by the National Science Foundation and the Department of Energy.


Project and Account Application
-----------------------------

FutureGrid allows you to easily create a project and use FG resources.
All you need to do is to create a portal account and apply for a
project. Detailed information is provided in the section :ref:`s-accounts`.

Services
--------------------

Currently, FutureGrid provides a number of different services. However, not all services
are offerd on all of the FG resources. To find
out how the machines are used please see the Section :ref:`s-status`.
The following services are most popular with our users

OpenStack:
    OpenStack is a collection of open source components to deliver
    public and private clouds. These components currently include
    OpenStack Compute (called Nova), OpenStack Object Storage (called
    Swift), and OpenStack Image Service (called Glance). OpenStack is
    a new effort and has received considerable momentum due to its
    openness and the support from companies. Users can find more details
    in the section :ref:`s-openstack`.

Nimbus:
    Nimbus is an open-source service package that allows users to run
    virtual machines on FutureGrid hardware. You can easily upload
    your own VM image or customize an image provided by us. When you
    boot a VM, it is assigned a public IP address (and/or an optional
    private address); you are authorized to log in as root via
    SSH. You can then run services, perform computations, and
    configure the system as desired. After using and configuring the
    VM, you can save the modified VM image back to the Nimbus image
    repository. Users can find more details in the section :ref:`s-nimbus`.

Eucalyptus:
    Eucalyptus is an open-source software platform that implements
    IaaS-style cloud computing. Eucalyptus provides a Amazon Web
    Services (AWS) compliant EC2-based web service interface for
    interacting with the Cloud service. Eucalyptus also provides
    services such as the AWS-compliant Walrus and a user interface for
    managing users and images.  Users can find more details in the
    section :ref:`s-eucalyptus`

.. 
    OpenNebula:
    **Not yet available to the public**, OpenNebula is an open and
    flexible tool that fits into existing data center environments to
    build any type of IaaS Cloud deployment. OpenNebula can be
    primarily used as a virtualization tool to manage your virtual
    infrastructure in the data center or cluster, which is usually
    referred to as Private Cloud.  OpenNebula supports Hybrid Cloud to
    combine local infrastructure with public cloud-based
    infrastructure, enabling highly scalable hosting
    environments. OpenNebula also supports Public Clouds by providing
    Cloud interfaces to expose its functionality for virtual machine,
    storage, and network management. Users can find how to use this
    software in the `OpenNebula tutorial
    <https://portal.futuregrid.org/tutorials/opennebula>`__. 

High Performance Computing:
    High Performance Computing can be defined as the application of
    supercomputing techniques to solve computational problems that are too
    large for standard computers or would take too much time. This is one of
    the more important features that the scientific community needs to
    achieve their projects. Thus, FutureGrid provides users the possibility
    of executing their parallel applications or using scientific software. A
    guide to accessing HPC services can be found in the section :ref:`s-hpc`.

Storage: 
    Users can find different storage systems to cover a wide
    number of purposes. In the section :ref:`s-storage`, users can
    find the information needed to get access and learn the usage. A
    summary of the external storage systems available can be found at
    :ref:`s-hpc`.


Information Services:
    These services gather the information of the different elements that
    make up FutureGrid to provide accurate and complete knowledge of the
    computational environment. This information is presented using different
    web portals in our section about the FutureGrid :ref:`s-status`.


Hardware
------------------

FutureGrid includes a geographically distributed set of heterogeneous
computing systems, data management systems, and dedicated networks.
These resources are provided by different institutions across the United
States. Detailed information on the different sites can be found in
the section :ref:`s-hardware`.



Support
-------------

Whe have the following activities that help you with FutureGrid.

Manual:
    The best place to start obtaining information about FutureGrid is this
    expanding :ref:`s-manual`. 

    In case you have a useful contribution, you can simply comment on each
    page, or if you like to create a chapter to be included, please  
 
    - `create a community page <https://portal.futuregrid.org/node/add/page-community>`__

    Community pages can also be used to report on elaborate experiment
    results. Once you are done with your contribution, please 

    - `send a ticket <https://portal.futuregrid.org/help>`__

    to us so we can make it more prominently visible in the portal.


User Forum:
    Based on advice from other projects we have established a number
    of 

    -  `user forums <https://portal.futuregrid.org/forum>`__.

    To post to the forum, you must create a portal account.

Help Ticketing System:
    To create a ticket for FutureGrid support, please use our 

    - `ticket form <https://portal.futuregrid.org/help>`__

    in which you describe problems like feature request, or bug report. A
    ticket will be automatically generated and you'll receive an auto-reply
    mail with the ticket number for further reference. FutureGrid staff will
    be looking into the ticket and working on it. You will receive updates
    and resolution through email upon the completion of the investigation.
    Please be aware that feedback may not be instantaneous. Tickets you have
    submitted can be viewed in your

    -  `ticket list <https://portal.futuregrid.org/tickets>`__.

