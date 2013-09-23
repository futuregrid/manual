.. _s-salsa-hadoop-hpc:

=====================================================
Salsa Hadoop with FutureGrid HPC
=====================================================

.. sidebar:: Page Contents

   .. contents::
      :local:

Author: Tak-Lon Stephen Wu
Improvements: fixed links with full URLs
Version: 1.0
Date: 2013-07-02


Apache Hadoop is widely used by domain scientists for running their
scientific applications in parallel fashion. Here, we provide a detail
instruction to use SalsaHadoop, an automatic method to start Hadoop
without worrying the Hadoop configuration,  on FutureGrid test-bed with
FutureGrid India Cluster. 


Requirement
-----------

#. FutureGrid HPC account, please apply via `FutureGrid
   portal <https://portal.futuregrid.org/user/register>`__ and `request
   a HPC account <https://portal.futuregrid.org/request-hpc-account>`__.
#. FutureGrid Eucalyptus account, please apply via `FutureGrid (India)
   Eucalyptus
   Portal <https://portal.futuregrid.org/request-eucalyptus-account%20>`__
#. Linux command experience.

Get HPC compute nodes
---------------------

Firstly, you will need to login to IU-india with using the command::

    Login command: ssh –i [ssh private key] [username]@india.futuregrid.org

    ssh –i key.pem johnny@india.futuregrid.org
    Enter passphrase for key 'ssh_id_rsa':
    [johnny@i136 ~]$

Here, “i136” is the headnode (first login node) of IU-india cluster.
You will obtain several HPC compute nodes from this node. Noted
that, \ **DO NOT** run any of your program on the “i136” headnode. Then,
on the command prompt, type the following command to get a set of
compute nodes::

    Obtain compute nodes command: qsub -I -l nodes=[numOfComputeNodes]:ppn=[CpuPerNode],walltime=[hh]:[mm]:[ss]

    [johnny@i136 ~]$ module load torque
    [johnny@i136 ~]$ qsub -I -l nodes=2:ppn=8,walltime=12:00:00
    qsub: waiting for job 44418.i136 to start
    qsub: job 44420.i136 ready
    [johnny@i55 ~]$ cat $PBS_NODEFILE
    i55
    i55
    i55
    i55
    i55
    i55
    i55
    i55
    i56
    i56
    i56
    i56
    i56
    i56
    i56
    i56

As shown above, “i55” and “i56” are the assigned compute nodes where
these nodes information are stored to environment
parameter $PBS\_NODEFILE.

Hadoop Configuration
--------------------

Once you obtain several compute nodes, you will need to download a
customized `Hadoop 0.20.203.0
package <http://salsahpc.indiana.edu/tutorial/apps/hadoop-0.20.203.0-customized.tar.gz>`__
from `SalsaHPC <http://salsahpc.indiana.edu/>`__ webserver, then simply
startup Hadoop with a OneClick script MultiNodesOneClickStartUp.sh. 

Script usage: . ./MultiNodesOneClickStartUp.sh [Path to Java JRE/JDK
Home] [Compute Nodes IPs/hostnames Info Files]
The function of script MultiNodesOneClickStartUp.sh mainly fills the
Hadoop required configuration parameters under
$HADOOP\_HOME/conf/hadoop-env.sh, $HADOOP\_HOME/conf/masters,
$HADOOP\_HOME/conf/slaves, $HADOOP\_HOME/conf/core-site.xml,
$HADOOP\_HOME/conf/hdfs-site.xml, and
$HADOOP\_HOME/conf/mapred-site.xml. You can also manually changes these
configuration files, however, please make sure you have the similar
approaches as mentioned below in order to start Hadoop without any
error.


-  conf/hadoop-env.sh

   -  JAVA\_HOME=/usr/lib/jvm/java-sun (CS Linux Machines)

-  conf/masters

   -  Set to login node hostname

-  conf/slaves

   -  Set to worker node hostname

-  conf/core-site.xml

   -  fs.default.name:  get masternode hostname with a unique port  

-  conf/hdfs-site.xml

   -  dfs.http.address: change to unique port other than 50070
   -  dfs.name.dir: must be unique and under control with permission
   -  dfs.data.dir: must be unique and under control with permission
   -  dfs.secondary.http.address: 0.0.0.0:0
   -  dfs.datanode.address: 0.0.0.0:0
   -  dfs.datanode.http.address: 0.0.0.0:0
   -  dfs.datanode.ipc.address: 0.0.0.0:0

-  conf/mapred-site.xml

   -  mapred.job.tracker: change to masternode hostname with a unique
      port
   -  mapred.job.tracker.http.address : change to unique port other than
      50030
   -  mapred.task.tracker.http.address: 0.0.0.0:0
   -  mapred.local.dir: must be unique and under control with permission
   -  mapred.tasktracker.map.tasks.maximum: 8
   -  mapred.tasktracker.reduce.tasks.maximum: 8



::

    [johnny@i55 ~]$ wget http://salsahpc.indiana.edu/tutorial/apps/hadoop-0.20.203.0-customized.t...
    [johnny@i55 ~]$ tar -zxvf hadoop-0.20.203.0-customized.tar.gz   
    [johnny@i55 ~]$ cd hadoop-0.20.203.0
    [johnny@i55 hadoop-0.20.203.0]$ cat nodes
    i55
    i56

    [johnny@i55 hadoop-0.20.203.0]$ . ./MultiNodesOneClickStartUp.sh /N/soft/jdk1.6.0_20-x86_64/ nodes

    *********************************************************************
    Hadoop 0.20.203.0 Multinodes OneClick Startup script
    *********************************************************************
    HADOOP_HOME = /N/u/johnny/hadoop-0.20.203.0
    Master Hostname = i55
    Slaves IP/Hostname = i55
    i56
    Username = johnny
    …
    …
    bin/start-all.sh
    starting namenode, logging to /N/u/johnny/hadoop-0.20.203.0/bin/../logs/hadoop-johnny-namenode-i55.out
    WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    i55: starting datanode, logging to /N/u/johnny/hadoop-0.20.203.0/bin/../logs/hadoop-johnny-datanode-i55.out
    i56: starting datanode, logging to /N/u/johnny/hadoop-0.20.203.0/bin/../logs/hadoop-johnny-datanode-i56.out
    i55: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    i56: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    i55: starting secondarynamenode, logging to /N/u/johnny/hadoop-0.20.203.0/bin/../logs/hadoop-johnny-secondarynamenode-i55.out
    i55: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    starting jobtracker, logging to /N/u/johnny/hadoop-0.20.203.0/bin/../logs/hadoop-johnny-jobtracker-i55.out
    WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    i55: starting tasktracker, logging to /N/u/johnny/hadoop-0.20.203.0/bin/../logs/hadoop-johnny-tasktracker-i55.out
    i56: starting tasktracker, logging to /N/u/johnny/hadoop-0.20.203.0/bin/../logs/hadoop-johnny-tasktracker-i56.out
    i55: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    i56: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    *************************************
    Hadoop has been started successfully.
    *************************************

    Please use lynx i55:9001 from i136 to see HDFS status
    Please use lynx i55:9003 from i136 to see MapReduce Daemon status

Verify Hadoop HDFS and MapReduce Daemon status
----------------------------------------------

After starting Hadoop with the OneClick startup script, you will need
to make sure HDFS and MapReduce Daemon are also started correctly before
running any program. As shown above, the last two messages indicate the
​http addresses to check HDFS and MapReduce status. Then, open a new
command prompt with login to i136 India headnode, type the command lynx
i55:9001 and lynx i55:9003::

    [johnny@i136 ~]$ lynx i55:9001
    …
    Cluster Summary
       8 files and directories, 1 blocks = 9 total.
       Heap Memory used 15.19 MB is 20% of Commited Heap Memory 72.5 MB. Max Heap Memory is 888.94 MB.
       Non Heap Memory used 18.91 MB is 81% of Commited Non Heap Memory 23.19 MB. Max Non Heap Memory is 130 MB.

       Configured Capacity                    : 554.73 GB
       DFS Used                               : 56.03 KB
       Non DFS Used                           : 61.45 GB
       DFS Remaining                          : 493.29 GB
       DFS Used%                              : 0 %
       DFS Remaining%                         : 88.92 %
       Live Nodes                             : 2
       Dead Nodes                             : 0
       Decommissioning Nodes             : 0
       Number of Under-Replicated Blocks : 1

    [johnny@i136 ~]$ lynx i55:9003
    Cluster Summary (Heap Size is 56.94 MB/888.94 MB)
       Queues Running Map Tasks Running Reduce Tasks Total Submissions Nodes Occupied Map Slots Occupied Reduce
       Slots Reserved Map Slots Reserved Reduce Slots Map Slot Capacity Reduce Slot Capacity Avg. Slots/Node
       Blacklisted Nodes Excluded Nodes
       1 0 0 0 2 0 0 0 0 16 16 16.00 0 0

If you see all “0” in above text, you should wait until it turns into
number(s) other than “0”. Here, as we are running Hadoop with 2 nodes,
"Live Nodes" is shown as “2” in HDFS section; it is similar to
MapReduce Section. If there does not have any change after 15 minutes,
you should restart it with rerunning the MultiNodesOneClickStartUp.sh
script.

Running Hadoop Applications
---------------------------

Now, after startung Hadoop successfully, you can try to run the provided
examples `Hadoop
WordCount <https://portal.futuregrid.org/manual/hadoop-wordcount>`__ and
`Hadoop Blast <https://portal.futuregrid.org/manual/hadoop-blast>`__.
