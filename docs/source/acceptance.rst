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

• 2 x 4-Core Intel Xeon E5530 (Nehalem-EP) processors
• 24GB Main Memory 
• 2 x 146GB 2.5-Inch 6Gbps SAS Disks

**32x IBM iDataPlex dx360 M2 nodes** (f1 through f2):

• 2 x 4-Core Intel Xeon E5520 (Nehalem-EP) processors
• 24GB Main Memory 
• 1 x 500GB 3.5-Inch SATA Disk

**1x Dell PowerEdge R310 Network monitoring node**
(bwctl.ufl.net.futuregrid.org)

 Storage
^^^^^^^^

**Hardware**:  IBM iDataPlex dx360 M3 storage node with 24TB raw
capacity (fs1).

• 2 x 4-Core Intel Xeon E5520 (Nehalem-EP) processors
• 24GB Main Memory 
• 12 x 2TB 7200 rpm 3.5-Inch 6Gbps SAS Disks

**Capacity**:  20TB RAID5

**Storage Interconnect**:  NFS export over GigE.

**Filesystem Type**:  XFS 

**Filesystem Layout**:

• Home directories mounted to all foxtrot nodes (f1 thorugh f32) at
/N/u/<username>
• Backup is not provided

Network
^^^^^^^

**Hardware**

• Force10 S50 48-port GigE switch, with 10GigE uplink to Florida
LambdaRail
• BLADE Rackswitch 48-port GigE switch (Management Network)

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

• india.futuregrid.org 
• i136r.idp.iu.futuregrid.org 

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

• 2 x 6-Core AMD Opteron Model 2435, 2.6 GHz Processors 
• 32 GB (16 x 2 GB DIMMs) Memory 
• 48 x 1 TB 7200 rpm 3.5-Inch SATA Disks

**Capacity**:  76.8 TB raid2 and 5.4 TB of raid0 (for scratch)

**Storage Interconnect**:  Currently mounted to cluster over GigE
ethernet.  Our long-term plan is to mount over Infiniband. 

**Filesystem Type**:  ZFS 

**Filesystem Layout**:

• Home directories mounted to Sierra at /N/u/<username>, snapshots
taken nightly, quota set at 50 GB 
• Scratch directories mount to Sierra at /N/scratch/<username>, no
backup, quota at 100 GB 
• Project directories, software directory mounted to Sierra as
/N/soft, snapshots taken nightly, quota set at 50 GB 
• Image directory (internal), mounts to Sierra at /images, snapshots
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

• The executable tools are installed at /usr/local/bin, and the $PATH
should have been all set. So a user could start running from his home
directory. 
• Command \ *qnodes* will list all the nodes and status. As for now,
node s36~s39 is up and running and should be available for
test/experiment. 
• \ *checknode s36* will list info on node s36. Os info can be found
at line such as:

    ::

         Opsys:      statelessrhels5.5  Arch:      x86_64

Now we have \ *statelessrhels5.5* and *statefulrhels5* as two options.

• If all the four nodes are running stateless os, submit a command like
this:

    ::

         msub -l os=statelessrhels5.5 testcmd.sh

will schedule the job in some node.

• \ *showq* will list the current queue info, and you could see the
submitted job in the \ *active jobs* section. 
• Check job running status using command \ *checkjob <jobid>*. The
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

• \ *showq* once again could list the jobs. 
• \ *checkjob <jobid>* will first tell you the dependency
job \ *provisioning os* is not completed.

    ::

          NOTE:  job cannot run  (dependency provision-73 jobsuccessfulcomplete not met)

• \ *checkjob provision-68(the provision job id)* will list the
provisioning status. 
• Once the provisioning is done, \ *checkjob <jobid>* will show the
job is scheduled, and also allow us to see where is it scheduled, for
example s37. 
• By running \ *checknode s37* again, we could see that the running
os was changed from \ *statelessrhels5.5* to*statefulrhels5*.

• \ *testcmd.sh* used in the example:

    ::

         $ cat testcmd.sh 
         #!/bin/bash
         /bin/date
         sleep 300
         /bin/date

 

