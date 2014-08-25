**********************************************************************
MP1: Running MPI Tasks on the Grid Appliance
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

Summary:
~~~~~~~~

This tutorial provides step-by-step instructions on how to deploy a pool of Grid Appliances configured with MPICH-2, an open-source
implementation of the MPI (Message Passing Interface) framework. The Grid Appliance/MPICH2 virtual clusters can be used as a basis for running a variety of MPI tutorials.

Prerequisites:
~~~~~~~~~~~~~~

-  To follow this tutorial, it is a pre-requisite that you have gone through this core Grid appliance tutorial:

   -  `Running the Grid Appliance on
      FutureGrid <http://portal.futuregrid.org/tutorials/ga9>`__

Set Up and Submit MPI Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^

#. | First you will build a local installation of MPI on your appliance from source. Use the following commands (note that it will take a few minutes to build MPI). The "-m32" option allows a 64-bit machine to submit MPI jobs to 32-bit machines.

   ::

       su griduser
       cd ~/examples/mpi
       ./setup.sh -m32

#. | Compile the "Hello World" example using the MPI cc compiler you just built in the previous step. (Note: This example builds a 32-bit binary with the "-m32" option):

   ::

       /mnt/local/mpich2/bin/mpicc -m32 -o HelloWorld HelloWorld.c

#. Before proceeding, check that your machine is connected to the public
   pool by using \ ``condor_status`` command. You may need to wait for a
   few minutes before it becomes fully operational.
#. | Submit the "HelloWorld" program to run on 2 nodes:

   ::

       ./mpi_submit.py -n 2 HelloWorld

#. If all goes well, you will see an output similar to the output below;
   if an error occurs and the MPI ring fails to start, you can retry the
   command above.

   ::

       griduser@C111197176:~/examples/mpi$ ./mpi_submit.py -n 2 HelloWorld
       serv ipop ip = 5.111.197.176
       submit condor with file tmpo21uIeMh/submit_mpi_vanilla_o21uIeMh
       Submitting job(s).
       Logging submit event(s).
       1 job(s) submitted to cluster 5.
       Waiting for 1 workers to response .... finished

       host list:
       ['C079184183', '1', 'cndrusr1', '45556', '/var/lib/condor/execute/dir_2824']

       MPD trace:
       C111197176_60625 (5.111.197.176)
       C079184183_43364 (5.79.184.183)

       Processor 0 of 2: Hello World!
       Processor 1 of 2: Hello World!

Building Your Own MPI Cluster Within or Outside FutureGrid:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you would like to re-create your own MPI virtual cluster outside
FutureGrid (e.g. in a local cluster, or on student desktops), the
overall steps to accomplish this are:

#. Create a GroupVPN and GroupAppliance for your class. Please refer to
   `FutureGrid Tutorial
   GA2 <https://portal.futuregrid.org/tutorials/ga2>`__, which explains
   how to create grid appliance clusters.
#. Download virtual appliances for deployment on your own resources, and
   configure them to connect to your GroupVPN/GroupAppliance with one
   Condor server and one or more Condor clients.
#. On the machine that will be the submitter of MPI jobs, install gcc,
   make, MPI, and the scripts used to submit MPI jobs through Condor. A
   tutorial detailing this process is maintained at the Grid Appliance
   portal. See `MPI over Condor with Grid
   Appliance <http://www.grid-appliance.org/wiki/index.php/MPI_Over_Condor_with_Grid_Appliance>`__
   (opens in new window).

Reference material:
~~~~~~~~~~~~~~~~~~~

-  Presentation: `Deploying Grid Appliance
   clusters <http://www.grid-appliance.org/files/docs/edu-docs/LocalGridAppliance1.pdf>`__
-  Videos: `Grid Appliance YouTube
   channel <http://www.youtube.com/acisp2p#p/c/D77781CEF51F72F3>`__

Authors:
~~~~~~~~

Panoat Chuchaisri, David Wolinsky, Renato Figueiredo, (University of Florida)
