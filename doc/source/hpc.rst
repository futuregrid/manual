.. _s-hpc:

**********************************************************************
HPC Services 
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

.. _s-hpc-access:

Accessing Systems
-----------------

Several of the clusters have High Performance Computing (HPC) services
installed. Access to them is provided via a Linux Login node for each
of the clusters.

To access ligin you need a FG resource account and an SSH public key you have uploaded to FutureGrid (this
process is described in the section about 
:ref:`s-accounts`. After you are part of a valid project
and have a FutureGrid account, you can log into the FutureGrid
resources with ssh. The resources include the following login nodes:

- alamo.futuregrid.org
- bravo.futuregrid.org
- foxtrot.futuregrid.org
- hotel.futuregrid.org
- india.futuregrid.org
- sierra.futuregrid.org
- xray.futuregrid.org

For example, assume your portalname is "portalname", than you can
login to sierra as follows::

        $ ssh portalname@sierra.futuregrid.org
        Welcome to sierra.futuregrid.org
        Last login: Thu Aug 12 19:19:22 2010 from ....

Modules
-------

The login nodes have the `modules <http://modules.sourceforge.net>`__
packace installed. It provides a convenient tool to adapt your
environment and enables you to activate different packges and services
dependent on your spcific needs. The Modules utility to let you
dynamically control your environment. Modules allows you to load and
unload packages and ensure a coherent working environment. 
This ensures that your $PATH, $LD_LIBRARY_PATH, $LD_PRELOAD, and other
environment variables are properly set, and that you can access the
programs and libraries you need. For additional information about the
Modules package you can consult the manual page on a login node with::

    $ man module

The available command ar elisted in the next table:


To display the list of available modules::

    $ module avail

To display the list of currently loaded modules::

    $ module list

To add and remove packages from your environment you can use the
*module load* and *module unload* commands::

    $ module load <package name>/<optional package version>
    $ module unload <package name>/<optional package version>


.. csv-table:: Module commands
   :header: Command, Description

   $ module avail,	List all software packages available on the system.
   $ module avail package,	List all versions of package available on the system
   $ module list,	List all packages currently loaded in your environment.
   $ module load package/version,	Add the specified version of the package to your environment
   $ module unload package,	Remove the specified package from your environment.
   $ module swap package_A package_B,	Swap the loaded package (package_A) with another package (package_B).
   $ module show package,	Shows what changes will be made to your environment (e.g. paths to libraries and executables) by loading the specified package.


WRONG TEXT hallo test test



FutureGrid provides a `list of HPC
services <http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp>`__
that currently consists of nodes on Alamo, Hotel, India, Sierra, and
Xray.

.. todo: this list is incomplete


Once you ssh into these nodes, you'll have access to the HPC queuing
services for the machine you have logged into. You will enter into a
Unix/Linux shell in which you can enter the typical Unix commands.
Access to the clusters is provided through Torque/Moab commands
from the command line. 

 
Filesystem Layout
-----------------

-  *Home* ($HOME) directories are located at */N/u/<username>*, with
   automated nightly backups. This is where users are encouraged to keep
   source files, configuration files and executables. Users should not
   run code from their $HOME directories. Please note that this is an
   NFS file system, and may result in slower access for some
   applications.
    
-  *Scratch* directories are located at different locations on the
   systems. To find out more about the file layout, please see the
   section :ref:`s-storage`
    
-  *System software* directories are located at */N/soft,* with
   automated nightly backups. System and community software are
   typically installed here. Tbale :ref:`t-storage-mountpoint`
   provides a summary of the various mount points.



Managing Applications with Torque
---------------------------------

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



To run any jobs on resources within FutureGrid HPC services (single
core, OpenMP or MPI jobs), users must use the job scheduler and a job
submission script. Users should NOT run jobs on the login or headnodes.
On FutureGrid machines, the job scheduler is the Torque (a variant of
PBS). To load torque into your environment, execute::

    $ module load torque


To run a serial job, you start by creating a job submission script
that both describes your job and will be executed on the compute nodes
by Torque. An example of a job script for India, Sierra, and Alamo that
runs */bin/hostname* is::

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

Additional information about the options that can be specified in a
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
qsub command to submit this job to be executed on the compute nodes::

    $ qsub ring.sh
    19095.master1.cm.cluster

The qsub command outputs either a job identifier or an error message
describing why Torque would not accept your job. If your job is
submitted successfully, you can track its execution using the qstat
command::

    $ qstat
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

The Message Passing Interface Standard (MPI) is a message passing
library standard based on the consensus of the MPI Forum, which has
dozens of participating organizations, including vendors, researchers,
software library developers, and users. The goal of the Message Passing
Interface is to establish a portable, efficient, and flexible standard
for message passing that will be widely used for writing message passing
programs. MPI is the *de facto* standard communication library for
almost all HPC systems, and is available in a variety of
implementations.

For more information, please visit:

-  `http://www.mpi-forum.org/ <http://www.mpi-forum.org/>`__
-  `http://www.mcs.anl.gov/research/projects/mpi/tutorial/ <http://www.mcs.anl.gov/research/projects/mpi/tutorial/>`__


For more information on OpenMPI, the default MPI distribution on
FutureGrid, please visit:

-  `http://www.open-mpi.org/ <http://www.open-mpi.org/>`__



MPI Libraries
-------------


The FutureGrid systems that support HPC-style usage have an MPI
implementation. In most cases, it is OpenMPI-1.4.x compiled with Intel
11.1 compilers. 


+--------------+-------------------+----------------+--------------------------+-----------------------------+
| **System**   | **MPI version**   | **Compiler**   | **Infiniband Support**   | **Module**                  |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Alamo        | OpenMPI 1.4.3     | Intel 11.1     | yes                      | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Bravo        | OpenMPI 1.4.2     | Intel 11.1     | no                       | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
|              | OpenMPI 1.4.3     | gcc 4.4.6      | no                       | openmpi/1.4.3-gnu           |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
|              | OpenMPI 1.4.3     | Intel 11.1     | no                       | openmpi/1.4.3-intel         |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
|              | OpenMPI 1.5.4     | gcc 4.4.6      | no                       | openmpi/1.5.4-[gnu,intel]   |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Hotel        | OpenMPI 1.4.3     | gcc 4.1.2      | yes                      | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| India        | OpenMPI 1.4.2     | Intel 11.1     | yes                      | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Sierra       | OpenMPI 1.4.2     | Intel 11.1     | no                       | openmpi                     |
+--------------+-------------------+----------------+--------------------------+-----------------------------+
| Xray         |                   |                | N/A                      |                             |
+--------------+-------------------+----------------+--------------------------+-----------------------------+

In cases where the OpenMPI is compiled with the Intel compilers,
loading the OpenMPI module will automatically load the Intel compilers
as a dependency::

    $ module load openmpi
    Intel compiler suite version 11.1/072 loaded
    OpenMPI version 1.4.3 loaded

Loading the OpenMPI module adds the MPI compilers to your $PATH
environment variable and the OpenMPI shared library directory to your
$LD\_LIBRARY\_PATH. This is an important step to ensure MPI applications
will compile and run successfully. Loading the torque module allows you
to submit jobs to the scheduler.
 

Compiling MPI Applications
--------------------------

To compile MPI applications, users have two options:

#. Use the MPI compilers instead of regular Intel/GNU compilers
#. Use the regular compilers (Intel/GNU) with MPI compilation flags

We recommend using the MPI compilers to avoid compilation issues. This
is accomplished by making the following replacements:

-  CC/icc/gcc with mpicc
-  CXX/icpc/g++ with mpicxx
-  F90/F77/FC/ifort/gfortran with mpif90

Alternatively, for some codes that require intricate compilation flags
and complicated make systems, and where changing compilers is not an
option, you can edit the compilation/linking options for your codes.
These options are machine, compiler, and language dependent. To view the
options required for C, C++ and Fortran on any machine, you can issue
the commands mpicc-show, mpicxx-show, and mpif90-show. Extra care must
be taken when using these flags, as dependencies govern the order in
which they appear in the link line. Should you run into compilation
errors or problems, please submit a consulting ticket.

Assuming you have loaded the openmpi module into your environment,
you can compile a `simple MPI application </tutorials/hpc/ring>`__ as
easily as executing::

    $ mpicc -o ring ring.c



Running MPI Applications
------------------------

Once your MPI application is compiled, you run it on the compute nodes
of a cluster via Torque. An example of an MPI parallel job script for
India, Sierra, and Alamo that runs the ring application is::

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

There are two important differences between this script and the submit
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

A minor difference between this script and the previous one is that
the environment variable $PBS\_JOBID is used when creating the stdin and
stdout files. Torque sets a number of environment variables that you can
use in your submit script, starting with PBS\_ .

 

Working with HPC Job Services
----------------------------------------------------------------------

 

Running Queued Jobs as Part of the HPC Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run a job in the HPC service, you need to create a job script that
tells the job manager how to run the job and how to handle things like
output and notifications. You can then submit your job to the scheduler,
monitor its progress in the job queue, and examine the output when it
finishes.

An example job script looks like this::

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

In the job script, lines that begin with  **#PBS** are directives to
the job scheduler. You can disable any of these lines by adding an
extra  **#** character at the beginning of the line, for example::


        ##PBS -M username@example.com

This job script shows some common examples of directives that you might
want to use in your job scripts. The directives in this job script are
described below::

        #!/bin/bash 

This line isn't strictly required, but it is added as a fail-safe in
case something unexpected happens. Normally, the job manager reads your
script and processes the directives, and then runs your script as a
normal shell script. This simply ensures that the system uses the
standard bash shell to run your script::

        #PBS -N testjob 

This line gives your job a name of  **testjob**. This name will be used
by the job manager when it shows a job listing, and will be used for
your output file(s) unless you explicitly specify an output file::

        #PBS -l nodes=1:ppn=1 

This line tells the job manager what your job requires for resources. In
this case, your job is asking for one node (**nodes=1**) and at least
one processor per node (**ppn=1**). See the
[[Sw:Manual/PBSDirectives\|PBSDirectives] page for other options you can
specify here::

        #PBS -q batch 

This line tells the job manager which job queue your job should be sent
to. Each job queue has different characteristics, such as the maximum
time a job is allowed to run, or the maximum number of nodes a job can
use::

        #PBS -j oe 

This line tells the job manager to join the job standard output and
standard error into a single file. For jobs with a small amount of
output, this is usually helpful. If your job produces a lot of standard
output, it may be helpful to keep the files separate so you can easily
locate error messages in the single error file::

        ##PBS -M username@example.com 

Note that this line is a comment since it starts with  **##** instead
of  **#PBS**. If you remove the first  **#**, this line will set the
email address that will get notified about events related to this job.
The events that get reported are set by the next line::

        ##PBS -m ae 

Again, note that this line is commented out. If you remove the
first  **#**, this line will send email whenever the job fails
(or **a** borts) (**a** option), and when the job ends (**e** option).
This is particularly helpful if your job has to wait a long time in the
queue before it runs::

        ##PBS -o testjob.out 

Again, note that this line is commented out. If you remove the
first  **#**, this line will specify the file name to be used for job
output.

Submitting Your Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can submit your job with the  **qsub** or **msub** commands.
The  **msub** and **qsub** are almost identical, and can mostly be used
interchangeably. See the respective man pages for specific differences.
Neither submission command provides much output. Examples of a job
submission using both commands follows:

Using  **msub**::

        $ msub testjob.pbs 
        292250 

Using  **qsub**::

        $ qsub testjob.pbs 
        292251.s82 

In both cases, the number that gets returned is the job number that the
scheduler assigned to your job. In the case of  **qsub**, the job
number is followed by the host name where you submitted the job.

Monitoring Your Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To monitor your job after it has been submitted, you can use
the  **qstat** or **showq** commands. Both commands will show you the
state of the job manager, but the information is displayed in different
formats. In general, the  **showq** command gives more complete
information, and in a form that is a bit easier to read.
The  **qstat** command gives a very concise listing of the job queue,
and in some instances this may give you a better quick overview of the
resource.

Using the test job script as an example, here is the output from
the  **showq** command::

        $ showq 
        active jobs
        ------------------------ 
        JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME 
        292252   yourusername       Running     16        3:59:59 Tue Aug 17 09:02:40 
        1 active job 16 of 264 processors in use by local jobs (6.06%) 
                          2 of 33 nodes active (6.06%) eligible jobs
        ----------------------
        JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME
        0 eligible jobs blocked jobs
        ----------------------- 
        JOBID    USERNAME       STATE PROCS    REMAINING            STARTTIME
        0 blocked jobs 
        Total job: 1 

You can see the output is divided into three sections:  **active
jobs**,  **eligible jobs**, and  **blocked jobs**.

#. **Active jobs** are jobs that are currently running on the resource.

#. **Eligible jobs** are jobs that are waiting for nodes to become
   available before they can run. As a general rule, jobs are listed in the
   order that they will be scheduled, but scheduling algorithms may change
   the order over time.

#. **Blocked jobs** are jobs that the scheduler cannot run for some
   reason. Usually a job becomes blocked because it is requesting something
   that is impossible, such as more nodes than currently exist, or more
   processors per node than are installed.

 

Using the test job as an example again, here is the output from
the  **qstat** command::

        $ qstat 
        Job id                             Name               User          Time Use S Queue 
        ------------------------- --------------------- ------------------- -------- - ----- 
        1981.i136                       sub19327.sub      inca               00:00:00 C batch 
        1982.i136                       testjob           yourusername                      0 R batch 

The  **qstat** command provides output in six columns:

#. Job id is the identifier assigned to your job.
#. Name is the name that you assigned to your job.
#. User is the username of the person who submitted the job.
#. Time Use is the amount of time the job has been running.
#. S shows the job state. Common job states are R for a running job, Q
   for a job that is queued and waiting to run, C for a job that has
   completed, and H for a job that is being held.
#. Queue is the name of the job queue where your job will run.

 

Examining Your Job Output
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
Cray, and all jobs are automatically routed to that queue.


To list the queues please use::

         qstat -Q

To obtain details of running jobs and available processors, use the showq command::

        /opt/moab/default/bin/showq

Submitting a job on xray
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: this example is incomplete and connfusing. we cat the job. submit but do
   not show how we submit ;-)


**MPI run cmd**:  aprun

Example job script (16 processors / 2 nodes)::

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

Looking at the Queue ::

        % qstat

The XT5m is a 2D mesh of nodes. Each node has two sockets, and each
socket has four cores.

The batch scheduler interfaces with a Cray resource scheduler called
APLS. When you submit a job, the batch scheduler talks to ALPS to find
out what resources are available, and ALPS then makes the reservation.

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
jobs at the same time, you need to first bury all the binaries under
one aprun command::

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

Alternatively, use the command aprun -n 1 -d 8 run.sh. To run multiple
serial jobs, you must build a batch script to divide the number of jobs
into groups of eight, and the

.. todo:: where is run.sh, is see job.sub but not run.sh

.. _s-storage:



Storage Services
----------------------------------------------------------------------

.. _t-storage-mountpoint:

.. exceltable:: Storage mountpoints on the CLusters
   :file: fg-cluster-details.xls
   :header: 1
   :selection: A1:G18
   :sheet: fg-storage




Using Indiana Universities Storage Services from FutureGrid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: This section has not be tested recently
  
FutureGrid does not provide an HPSS server. However, if you have an IU
account (available only for IU faculty, staff, and students), you can
use the following services from india:

* `SDA <http://rc.uits.iu.edu/storage/sda>`__ service
* `HSI <http://rc.uits.iu.edu/storage/hsi>`__, the Hierarchical Storage
Interface client is available in india. 

To use the HSI client on india:

-  First, activate your SDA account as descreibed in the `MDSS Service Starter
   Kit <http://rc.uits.iu.edu/storage/mdss-starter-kit>`__ documentation.
-  Then, from india, load the HSI module as follows::

    $ module load hsi
    hsi version 3.5.3 loaded

-  Connect to the SDA::

    $ hsi -A combo
    Principal: your_iu_userid                                
    [youriuid]Password:                                
    Username: your_iu_userid  UID: 1122636  Acct: 1122636(1122636) Copies: 1 Firewall: off [hsi.3.5.3 Fri Nov 20 10:01:25 EST 2009]
    ?

Your principal is your IU Network ID, and your password is
the IU passphrase.

-  Enable firewall mode; otherwise, you will receive this error::

    put: Error -5 on transfer

    ? firewall -on
    A: firewall mode set ON, I/O mode s<et to extended (parallel=off), autoscheduling currently set to OFF

-  List local folder::

     ? lls
     testfile.txt

-  List the current directory in HPSS::

    ? pwd
    pwd0: /hpss/pathtoyouriuusername

-  For transferring files (*put* and *get*), search the `IU Knowledge
   Base <http://kb.iu.edu/?search=hsi>`__.
