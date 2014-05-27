
.. _s-twister:

**********************************************************************
Using Twister in FutureGrid
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

PLEASE NOTE: THIS MANUAL PAGE IS A DRAFT, PLEASE PROVIDE FEEDBACK IN THE
COMMENT SECTION.

What is Twister?
----------------

MapReduce programming model has simplified the implementations of many
data parallel applications. The simplicity of the programming model and
the quality of services provided by many implementations of MapReduce
attract a lot of enthusiasm among parallel computing communities. From
the years of experience in applying MapReduce programming model to
various scientific applications, we identified a set of extensions to
the programming model and improvements to its architecture that will
expand the applicability of MapReduce to more classes of applications.
`Twister <http://www.iterativemapreduce.org/>`_ is a lightweight
MapReduce runtime we have developed by incorporating these enhancements.

`Twister <http://www.iterativemapreduce.org/>`_ provides the following
features to support MapReduce computations. (Twister is developed as
part of `Jaliya Ekanayake's <http://www.cs.indiana.edu/%7Ejekanaya/>`_
Ph.D. research and is supported by the `Salsa <http://salsahpc.indiana.edu/>`_ Team
@ `IU <http://www.iub.edu/>`_)


* Distinction on static and variable data                                                                  
* Configurable long running (cacheable) map/reduce tasks                                                                 
* Pub/sub messaging based communication/data transfers                                                             
* Efficient support for Iterative MapReduce computations (much faster than `Hadoop <http://hadoop.apache.org/>`_ or `Dryad/DryadLINQ <http://research.microsoft.com/en-us/projects/DryadLINQ/>`_)   
* Combine phase to collect all reduce outputs                                                               
* Data access via local disks                                                                 
* Lightweight (~5600 lines of Java code)                                                                 
* Support for typical MapReduce computations                                                          
* Tools to manage data                                                                  

|image19|

Iterative MapReduce programming model using Twister

Running Twister on FutureGrid
-----------------------------

Twister can be run in various modes within FG either in FutureGrid HPC
or FutureGrid Cloud environment.

-  Twister on FutureGrid

   -  `Running Twister on FutureGrid HPC
      HPC <twister-futuregrid-hpc.html>`_

      -  `Get HPC compute
         nodes <twister-futuregrid-hpc.html#hpc-nodes>`_
      -  `Twister
         Configuration <twister-futuregrid-hpc.html#twister-conf>`_

         -  `Download Twister
            0.9 <twister-futuregrid-hpc.html#download-twister>`_
         -  `Set $TWISTER\_HOME and
            $JAVA\_HOME <twister-futuregrid-hpc.html#set-twister-conf>`_
         -  `Run
            TwisterPowerMakeUp.sh <twister-futuregrid-hpc.html#twisterpowermakeup>`_
         -  `Download and start ActiveMQ on specific
            nodes <twister-futuregrid-hpc.html#start-activemq>`_
         -  `Start
            Twister <twister-futuregrid-hpc.html#run-twister>`_

      -  `Verify Twister MapReduce Daemon
         status <twister-futuregrid-hpc.html#verify-twister-status>`_

   -  `Twister with FutureGrid Cloud OpenStack
      OpenStack <twister-futuregrid-cloud-openstack.html>`_

      -  `Get VM compute
         nodes <twister-futuregrid-cloud-openstack.html#vm-nodes>`_

         -  `VM Hostname
            setting <twister-futuregrid-cloud-openstack.html#vm-nodes-setting>`_

      -  `Twister
         Configuration <twister-futuregrid-cloud-openstack.html#twister-conf>`_

         -  `Download Twister
            0.9 <twister-futuregrid-cloud-openstack.html#twister-download>`_
         -  `Set $TWISTER\_HOME, $JAVA\_HOME and Worker
            Nodes <twister-futuregrid-cloud-openstack.html#twister-conf-setup>`_
         -  `Run
            TwisterPowerMakeUp.sh <twister-futuregrid-cloud-openstack.html#twisterpowermakeup>`_
         -  `Download and start ActiveMQ on specific
            node <twister-futuregrid-cloud-openstack.html#twister-conf-activemq>`_
         -  `Start
            Twister <twister-futuregrid-cloud-openstack.html#run-twister>`_

      -  `Verify Twister MapReduce Daemon
         status <twister-futuregrid-cloud-openstack.html#verify-twister-status>`_

Run Twister Applications
------------------------

We provide Kmeans and Blast run on Twister as examples.

-  `Twister Kmeans <twister-kmeans.html>`_
-  `Twister Blast <twister-blast.html>`_

Papers and Presentations
------------------------


* Jaliya Ekanayake, Hui Li, Bingjing Zhang, Thilina Gunarathne, Seung-Hee Bae, Judy Qiu, Geoffrey Fox, `Twister: A Runtime for Iterative MapReduce <http://www.iterativemapreduce.org/hpdc-camera-ready-submission.pdf>`_," The First International Workshop on MapReduce and its Applications (MAPREDUCE'10) - HPDC2010                                                              
* Jaliya Ekanayake, (Advisor: Geoffrey Fox) `Architecture and Performance of Runtime Environments for Data Intensive Scalable Computing <http://grids.ucs.indiana.edu/ptliupages/publications/SC09-abstract-jaliya-ekanayake.pdf>`_, Doctoral Showcase, SuperComputing2009. (`Presentation <http://www.slideshare.net/jaliyae/architecture-and-performance-of-runtime-environments-for-data-intensive-scalable-computing-2653554>`_)   * Jaliya Ekanayake, Atilla Soner Balkir, Thilina Gunarathne, Geoffrey Fox, Christophe Poulain, Nelson Araujo, Roger Barga, `DryadLINQ for Scientific Analyses <http://grids.ucs.indiana.edu/ptliupages/publications/eScience09-camera-ready-submission.pdf>`_, Fifth IEEE International Conference on e-Science (eScience2009), Oxford, UK.                                                                   
* Jaliya Ekanayake, Geoffrey Fox, `High Performance Parallel Computing with Clouds and Cloud Technologies <http://grids.ucs.indiana.edu/ptliupages/publications/cloud_handbook_final-with-diagrams.pdf>`_, First International Conference on Cloud Computing (CloudComp09) Munich, Germany, 2009.                                                                 
* Geoffrey Fox, Seung-Hee Bae, Jaliya Ekanayake, Xiaohong Qiu, and Huapeng Yuan,`Parallel Data Mining from Multicore to Cloudy Grids `<http://grids.ucs.indiana.edu/ptliupages/publications/CetraroWriteupJan09_v12.pdf>`_, High Performance Computing and Grids workshop, 2008.                                                                 
* Jaliya Ekanayake, Shrideep Pallickara, and Geoffrey Fox `MapReduce for Data Intensive Scientific Analysis <http://www.cs.indiana.edu/%7Ejekanaya/papers/eScience-final.pdf>`_, Fourth IEEE International Conference on eScience, 2008, pp.277-284.                                                           



.. |Home| image:: /sites/all/themes/fgtheme/logo.png
.. |image19| image:: http://www.iterativemapreduce.org/images/imrmodel.png
.. |image32| image:: /sites/default/files/images/nsf-logo.png
.. |image33| image:: /sites/default/files/u876/xsede-logo.png
