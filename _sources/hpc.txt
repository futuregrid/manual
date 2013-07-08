.. highlight:: bash

.. _s-hpc:

**********************************************************************
HPC Services 
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

.. _s-hpc-access:

Login Nodes
-----------------

Several of the clusters have High Performance Computing (HPC) services
installed. Access to them is provided via a Linux Login node for each
of the clusters on which these services are installed.

To access the login nodes you need a FG resource account and an SSH
public key you have uploaded to FutureGrid (this process is described
in the section about :ref:`s-accounts`. After you are part of a valid
project and have a FutureGrid account, you can log into the FutureGrid
resources with ssh. The resources include the following login nodes:

- alamo.futuregrid.org
- bravo.futuregrid.org
- foxtrot.futuregrid.org
- hotel.futuregrid.org
- india.futuregrid.org
- sierra.futuregrid.org
- xray.futuregrid.org

.. todo:: what are login nodes for delta, echo

For example, assume your portalname is "portalname", than you can
login to sierra as follows::

        $ ssh portalname@sierra.futuregrid.org
        Welcome to sierra.futuregrid.org
        Last login: Thu Aug 12 19:19:22 2010 from ....

Modules
^^^^^^^^^^^^^^^

The login nodes have the `modules <http://modules.sourceforge.net>`__
package installed. It provides a convenient tool to adapt your
environment and enables you to activate different packages and services
dependent on your specific needs. The Modules utility to let you
dynamically control your environment. Modules allows you to load and
unload packages and ensure a coherent working environment. 
This ensures that your $PATH, $LD_LIBRARY_PATH, $LD_PRELOAD, and other
environment variables are properly set, and that you can access the
programs and libraries you need. For additional information about the
Modules package you can consult the `manual page <http://modules.sourceforge.net/man/module.html>`__.

To display the list of available modules::

    $ module avail

To display the list of currently loaded modules::

    $ module list

To add and remove packages from your environment you can use the
*module load* and *module unload* commands::

    $ module load <package name>/<optional package version>
    $ module unload <package name>/<optional package version>

The available command are listed in the next table:

.. csv-table:: Module commands
   :header: Command, Description

   module avail,	List all software packages available on the system.
   module avail package,	List all versions of package available on the system
   module list,	List all packages currently loaded in your environment.
   module load package/version,	Add the specified version of the package to your environment
   module unload package,	Remove the specified package from your environment.
   module swap package_A package_B,	Swap the loaded package (package_A) with another package (package_B).
   module show package,	Shows what changes will be made to your environment (e.g. paths to libraries and executables) by loading the specified package.



**Example** - List the currently loaded modules on sierra after login:: 

   $ module list

   Currently Loaded Modulefiles:
     1) torque/2.4.8   2) moab/5.4.0


**Example** - list the avialable modules on sierra::


   $ module avail

   ----------------- /opt/Modules/3.2.8/modulefiles/applications ------------------
   R/2.11.1(default)      hpcc/1.3.1(default)    velvet/1.0.15
   git/1.7.10             ncbi/2.2.23(default)   wgs/6.1
   gromacs/4.0.7(default) soapdenovo/1.04

   ------------------- /opt/Modules/3.2.8/modulefiles/compilers -------------------
   cmake/2.8.1(default)       java/1.6.0-i586
   intel/10.1                 java/1.6.0-x86_64(default)
   intel/11.1(default)

   ------------------- /opt/Modules/3.2.8/modulefiles/debuggers -------------------
   null                       totalview/8.8.0-2(default)

   ------------------- /opt/Modules/3.2.8/modulefiles/libraries -------------------
   intelmpi/4.0.0.028(default)  openmpi/1.4.3-intel
   mkl/10.2.5.035(default)      otf/1.7.0(default)
   openmpi/1.4.2(default)       unimci/1.0.1(default)
   openmpi/1.4.3-gnu            vampirtrace/intel-11.1/5.8.2

   --------------------- /opt/Modules/3.2.8/modulefiles/tools ---------------------
   cinderclient/1.0.4(default)   moab/5.4.0(default)
   cloudmesh/0.8(default)        myhadoop/0.2a
   euca2ools/1.2                 novaclient/2.13.0(default)
   euca2ools/1.3.1               precip/0.1(default)
   euca2ools/2.0.2(default)      python/2.7(default)
   genesisII/2.7.0               python/2.7.2
   glanceclient/0.9.0(default)   torque/2.4.8(default)
   keystoneclient/0.2.3(default) vim/7.2
   marmot/2.4.0(default)

**Example** - load a default module (in thi case cloudmesh)::

   $ module load cloudmesh

Please note that for loading the default you do not have to specify the version number.

List of Available Modules on Various Machines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :header: Module,hotel,india,sierra

   R,,2.11.1,2.11.1
   atlas,3.9.35,3.10.1,
   cbench,20110407-openmpi,,
   cinderclient,,,1.0.4
   cloudmesh,,,0.8
   cmake,2.8.4,2.8.1,2.8.1
   ctool,2.12,,
   euca2ools,,2.1.2,2.0.2
   fftw,3.2.2,,
   glanceclient,,,0.9.0
   globus,5.0.3,,
   goto2,1.13,,
   gromacs,4.5.4,4.0.7,4.0.7
   gsl,1.14,,
   hadoop,0.20.203.0,,
   hdf5,1.8.7,,
   hostlists,0.2,,
   hpcc,,1.3.1,1.3.1
   intel,11.1,11.1,11.1
   intelmpi,4.0.0.028,4.0.0.028,4.0.0.028
   java,1.6.0_31-x86_64,1.6.0-x86_64,1.6.0-x86_64
   keystoneclient,,,0.2.3
   lapack,3.3.0,,
   marmot,2.4.0,2.4.0,2.4.0
   mkl,10.2.5.035,10.2.5.035,10.2.5.035
   moab,,5.4.0,5.4.0
   myhadoop,0.2a,,
   ncbi,,2.2.23,2.2.23
   novaclient,,,2.13.0
   openmpi,1.4.5,1.4.3-gnu,1.4.2
   otf,1.7.1,1.7.0,1.7.0
   precip,,0.1,0.1
   python,2.7,2.7,2.7
   szip,2.1,,
   taktuk,3.7.3,,
   torque,,2.5.5,2.4.8
   totalview,,8.8.0-2,8.8.0-2
   unimci,1.0.1,1.0.1,1.0.1
   vampirtrace,5.9,,
   zookeeper,3.3.5,,

 
Filesystem Layout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Home* directories:
   Home directories are accessible through the $HOME shell variable are
   located at */N/u/<username>*. This is where users are encouraged to
   keep source files, configuration files and executables. Users
   should not run code from their $HOME directories. Please note that
   this is an NFS file system, and may result in slower access for
   some applications. We also advise the users to provide external
   backup storage at their home institution or a code repository. For
   example, we recommend that you use git or svn to make sure you
   backup your changes to the code. Also make sure you backup your
   data. As a testbed, we do not guarantee dataloss.
    
*Scratch* directories:
   Scratch directories are located at different locations on the
   systems. To find out more about the file layout, please see the
   section :ref:`s-storage`
    
*System software* directories: 
   System software directories are located at */N/soft*. System and
   community software are typically installed here. Table
   :ref:`t-storage-mountpoint` provides a summary of the various mount
   points.

.. _t-storage-mountpoint:

.. exceltable:: Storage mountpoints on the Clusters
   :file: fg-cluster-details.xls
   :header: 1
   :selection: A1:G18
   :sheet: fg-storage




Message Passing Interface (MPI)
-------------------------------

The *Message Passing Interface Standard (MPI)* is the *de facto*
standard communication library for almost many HPC systems, and is
available in a variety of implementations. It has been created through
consensus of the MPI Forum, which has dozens of participating
organizations, including vendors, researchers, software library
developers, and users. The goal of the Message Passing Interface is to
provide a portable, efficient, and flexible standard for programs
using message passing. For more information about MPI, please visit:

-  `http://www.mpi-forum.org/ <http://www.mpi-forum.org/>`__
-  `http://www.mcs.anl.gov/research/projects/mpi/tutorial/ <http://www.mcs.anl.gov/research/projects/mpi/tutorial/>`__
-  `http://www.open-mpi.org/ <http://www.open-mpi.org/>`__



MPI Libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Several FutureGrid systems support MPI as part of their HPC services. 
An up to date status about it can be retrieved via our `Inca
status pages <http://inca.futuregrid.org:8080/inca/jsp/status.jsp?suiteNames=HPC,HPC_Tests,Benchmarks&resourceIds=FG_BATCH>`__.

.. todo:: this table is outdated.

.. csv-table:: MPI versions installed on FutureGrid HPC services
   :header:   System   , MPI version   , Compiler   , Infiniband Support   , Module                  

   Alamo        , OpenMPI 1.4.5     , Intel 11.1     , yes   , openmpi           
   Bravo        , OpenMPI 1.4.2     , Intel 11.1     , no    , openmpi                
		, OpenMPI 1.4.3     , gcc 4.4.6      , no    , openmpi/1.4.3-gnu      
		, OpenMPI 1.4.3     , Intel 11.1     , no    , openmpi/1.4.3-intel    
		, OpenMPI 1.5.4     , gcc 4.4.6      , no    , openmpi/1.5.4-[gnu,intel]   
   Hotel        , OpenMPI 1.4.3     , gcc 4.1.2      , yes   , openmpi                
   India        , OpenMPI 1.4.2     , Intel 11.1     , yes   , openmpi                
   Sierra       , OpenMPI 1.4.2     , Intel 11.1     , no    , openmpi                
   Xray         ,                   ,                , N/A   ,                             

Loading the OpenMPI module adds the MPI compilers to your $PATH
environment variable and the OpenMPI shared library directory to your
$LD_LIBRARY_PATH. This is an important step to ensure MPI applications
will compile and run successfully. In cases where the OpenMPI is
compiled with the Intel compilers loading the OpenMPI module will
automatically load the Intel compilers as a dependency. To load the
default openmpi module and associated compilers, just use::

    $ module load openmpi


Compiling MPI Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To compile MPI applications, users can simply use the available mpi
compile commands:

mpicc:
   To compile C programs with the the CC/icc/gcc compilers

mpicxx:
   To compile c++ programs with CXX/icpc/g++ with mpicxx

mpif90:
   To compile programs with F90/F77/FC/ifort/gfortran


To see in detail what these commands do you can add a *-show*  as an
option. Thus the following commands::
   
   $ mpicc -show
   $ mpicxx -show
   $ mpif90 -show

will show you the detail of each of them. The resulting output can be
used as a template to adapt compile flags in case the default settings are
not suitable for you.


Assuming you have loaded the openmpi module into your environment,
you can compile a `simple MPI application <ring>`__ with
easily as executing::

    $ mpicc -o ring ring.c


Users MUST NOT run jobs on the login or headnodes. These nodes are
reserved for editing and compiling programs. Furthermore running your
commands on such nodes will not provide any useful information as you
actually do not use the standard cluster node. 

Batch Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once your MPI application is compiled, you run it on the compute nodes
of a cluster via a batch processing. With the help of a batch
processing services a job is run on the cluster without the users
intervention via a job queue. The user does not have to worry much
about the internal details of the job queue, but must provide the
scheduler with some guidance about the job so it can be efficiently
scheduled on the system.  

To run jobs on resources with the HPC services, users must first
activate their environment to use the job scheduler::

    $ module load torque

A complete manual for the torque scheduler can be found in the `Torque
manual<http://www.clusterresources.com/torquedocs21/>`__.

Next we need to create a script so we can run the program on the
cluster.  We will be using our simple ring example to illustrate some
of the parameters you need to adjust:

.. code-block:: bash
   :linenos:

    #! /bin/bash

    # OPTIONS FOR THE SCRIPT
    #PBS -M username@example.com 
    #PBS -N ring_test
    #PBS -o ring_$PBS_JOBID.out
    #PBS -e ring_$PBS_JOBID.err
    #PBS -q short
    #PBS -l nodes=4:ppn=8
    #PBS -l walltime=00:20:00


    # make sure MPI is in the environment
    module load openmpi

    # launch the parallel application with the correct number of process
    # Typical usage: mpirun -np <number of processes> <executable> <arguments>
    mpirun -np 32 ring -t 1000

    echo "Nodes allocated to this job: " 
    cat $PBS_NODEFILE 

In the job script, lines that begin with  **#PBS** are directives to
the job scheduler. You can disable any of these lines by adding an
extra  **#** character at the beginning of the line, as *##* is
interpreted to be a comment. Common options include:

-  -M: specify a mail address that is notified upon completion
-  -N: To specify a job name
-  -o: The name of the file to write stdout to
-  -e: The name of the file to write stderr to
-  -q: The queue to submit the job to
-  -l: Resources specifications to execute the job


The first parameters are rather obvious, so let us focus on the
*-q* option. Each batch service is configured with a number of
queues that are targeting different classes of jobs to more
efficiently schedule them. These queues can be switch on or of,
modified or new queues can be added to the system. It is useful to get
a list of available queues on the system where you like to submit your
jobs and inspect which would be most suitable to use for your
purpose with the qstat command on the appropriate login node::

   $ qstat -q 

Currently we have the following queues:


HPC Job Queue Information:
    .. csv-table:: 
       :header: Resource   , Queue name   , Default Wallclock Limit   , Max Wallclock Limit   , NOTES                

	india      , batch        , 4 hours                   , 24 hours              ,                       
		   , long         , 8 hours                   , 168 hours             ,                       
		   , scalemp      , 8 hours                   , 168 hours             , restricted access     
		   , b534         , none                      , none                  , restricted access     
		   , ajyounge     , none                      , none                  , restricted access     
	sierra     , batch        , 4 hours                   , 24 hours              ,                       
		   , long         , 8 hours                   , 168 hours             ,                       
	hotel      , extended     , none                      , none                  ,                       
	alamo      , shortq       , none                      , 24 hours              ,                       
		   , longq        , none                      , 24 hours              ,                       
	foxtrot    , batch        , 1 hour                    , none                  , not for general use   


.. todo:: remove the queue ajyounge from the system, can this be done
   by preserving the logs?

.. todo:: remove the queue b534 from the system, can this be done
   while preserving the logs?

Next we focus on the -l option that specifies the resources. The
term::

  nodes=4

means that we specify 4 servers on which we execute the job. The
term::

  ppn=8 

means that we use 8 virtual processors per node, while a virtual
processor is typically executed on a core of the server. Thus it is
advisable not to exceed the number of cores per server. For some
programs choosing the best performing number of servers and cores may
be dependent on factors such as memory needs, IO access and other
resource bounded properties. You may have to experiment with the
parameters. To identify the number of servers and cores available
please see Tables :ref:`t-clusters` and :ref:`t-clusters-details`.
For example, Alamo, Hotel, India, and Sierra have 8 cores per node,
thus 4 servers would provide you access to 32 processing units.

Often you may just want to have the stdout and stderr in one file,
than you simply can replace the line with -e in it with:: 

        #PBS -j oe 

which simply means that you *join* stdout and stderr. Here j stands
for join, o for stdout and e for stderr. In case you like to have
e-mail send to you based on the status of the job, you can achieve
this with adding::

        #PBS -m ae 

to your script. It will send you mail when the job aborts (indicated
by a), or when the job ends (indicated by e).

Job Management
---------------------------------

A list of all available  scheduler commands is available from the `Torque
manual page <http://www.clusterresources.com/torquedocs21/>`__. We
describe next the use of some typical interactions to manage your jobs
in the batch queue.

Job Submission
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have created a submission script, you can then use the 
qsub command to submit this job to be executed on the compute nodes::

    $ qsub ring.pbs
    20311.i136

The qsub command outputs either a job identifier or an error message
describing why the scheduler would not accept your job. Alternatively,
you can also use the msub command, which is very similar to the qsub
command. For differences we ask you to consult the man pages.

Job Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sometimes you may want to delete a job from the queue, which can be
easily done with the qdel command, followed by the id::

   $ qdel 20311

Job Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your job is submitted successfully, you can track its execution
using the qstat or showq commands. Both commands will show you the
state of the jobs submitted to the scheduler. The difference is mostly
in their output format.



showq:
    divides the output into three sections:  active
    jobs,  eligible jobs, and blocked jobs::

       $ showq 
       active jobs
       ------------------------ 
       JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME 
       20311   yourusername       Running     16        3:59:59 Tue Aug 17 09:02:40 
       1 active job 16 of 264 processors in use by local jobs (6.06%) 
                         2 of 33 nodes active (6.06%) eligible jobs
       ----------------------
       JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME
       0 eligible jobs blocked jobs
       ----------------------- 
       JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME
       0 blocked jobs 
       Total job: 1 

    Legend:
       Active jobs:
	  are jobs that are currently running on resources.

       Eligible jobs: 
	  are jobs that are waiting for nodes to become available before
	  they can run. As a general rule, jobs are listed in the order
	  that they will be scheduled, but scheduling algorithms may
	  change the order over time.

       Blocked jobs:
	  are jobs that the scheduler cannot run for some reason. Usually
	  a job becomes blocked because it is requesting something that
	  is impossible, such as more nodes than currently exist, or more
	  processors per node than are installed.

qstat:
    provides a single table view, where the status of each job is
    added via a status column called S::

        $ qstat 
        Job id                             Name               User          Time Use S Queue 
        ------------------------- --------------------- ------------------- -------- - ----- 
        1981.i136                       sub19327.sub      inca               00:00:00 C batch 
        20311.i136                      testjob           yourusername              0 R batch 

    Legend:
       Job id:
	  is the identifier assigned to your job.
       Name:
	  is the name that you assigned to your job.
       User:
	  is the username of the person who submitted the job.
       Time:
	  is the amount of time the job has been running.
       S:
	  shows the job state. Common job states are R for a running job, Q
	  for a job that is queued and waiting to run, C for a job that has
	  completed, and H for a job that is being held.
       Queue: 
	  is the name of the job queue where your job will run.

If you are interested in only your job by for example using grep::

    $ qstat | grep 20311

 

Job Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you gave your job a name with the  **#PBS -N <jobname>** directive
in your job script or by specifying the job name on the command line,
your job output will be available in a file named  **jobname.o######**,
where the  **######** is the job number assigned by the job manager.
You can type  **ls jobname.o\*** to see all output files from the same
job name.

If you explicitly name an output file with the  **#PBS -o
<outfile>** directive in your job script or by specifying the output
file on the command line, your output will be in the file you specified.
If you run the job again, the output file will be overwritten.

If you don't specify any output file, your job output will have the same
name as your job script, and will be numbered in the same manner as if
you had specified a job name (**jobname,o######**).

Xray HPC Services
----------------------------------------------------------------------

To log into the login node of xreay please use the command::

    ssh portalname@xray.futuregrid.org

Extensive documentation about the user environment of the Cray can be
found at 

- `Cray XTTM Programming Environment User's Guide <http://docs.cray.com/cgi-bin/craydoc.cgi?mode=View;id=S-2396-21>`__

For MPI jobs, use cc (pgcc). For best performance, add the xtpe-barcelona module::

    % module add xtpe-module

Currently there is only one queue (batch) available to users on the
Cray, and all jobs are automatically routed to that queue.  You can
use the same commands as introduced in the previous sections. Thus, to
list the queues please use::

         qstat -Q

To obtain details of running jobs and available processors, use the showq command::

        /opt/moab/default/bin/showq

Submitting a Job on xray
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To execute an MPI program on xray we use a special program called aprun in
the submit script. Additionally we have some special resource
specifications that we can pass along, such as mppwidth and
mppppn. An example is the following program that will use 16
processors on 2 nodes::

        $ cat job.pbs

::

        #! /bin/sh
        
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

        $ qsub job.pbs 

The XT5m is a 2D mesh of nodes. Each node has two sockets, and each
socket has four cores. The batch scheduler interfaces with a Cray
resource scheduler called APLS. When you submit a job, the batch
scheduler talks to ALPS to find out what resources are available, and
ALPS then makes the reservation.

Currently ALPS is a "gang scheduler" and only allows one "job" per node.
If a user submits a job in the format aprun -n 1 a.out , ALPS will put
that job on one core of one node and leave the other seven cores empty.
When the next job comes in, either from the same user or a different
one, it will schedule that job to the next node.

If the user submits a job with aprun -n 10 a.out , then the scheduler
will put the first eight tasks on the first node and the next two tasks
on the second node, again leaving six empty cores on the second node.
The user can modify the placement with -N , -S , and -cc .

A user might also run a single job with multiple treads, as with OpenMP.
If a user runs this job aprun -n 1 -d 8 a.out , the job will be
scheduled to one node and have eight threads running, one on each core.

You can run multiple, different binaries at the same time on the same
node, but only from one submission. Submitting a script like this
will not work::

        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 0 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 1 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 2 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 3 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 4 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 5 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 6 ./my-binary
        OMP_NUM_THREADS=1 aprun -n 1 -d 1 -cc 7 ./my-binary

This will run a job on each core, but not at the same time. To run all
jobs at the same time, you need to first add all the binaries within 
one aprun command::

        $ cat run-all.pbs
        ./my-binary1
        ./my-binary2
        ./my-binary3
        ./my-binary4
        ./my-binary5
        ./my-binary6
        ./my-binary7
        ./my-binary8
        $ aprun -n 1 run.pbs

Alternatively, use the command aprun -n 1 -d 8 run.pbs. To run multiple
serial jobs, you must build a batch script to divide the number of jobs
into groups of eight, and the




