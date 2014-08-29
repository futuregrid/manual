.. _s-salsa-hadoop-eucalyptus:

=================================================================
SalsaHadoop with FutureGrid Cloud Eucalyptus
=================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:

Author: Tak-Lon Stephen Wu
Version: 0.2
Date: 2013-05-22

Apache Hadoop is widely used by domain scientists for running their
scientific applications in parallel fashion. Here, we provide an example
to use SalsaHadoop, an automatic method to start Hadoop without worrying
about the Hadoop configuration, on FutureGrid test-bed with FutureGrid
India Eucalyptus.

Requirement
-----------

#. FutureGrid Resource account.
#. Started FutureGrid Eucalyptus VM instances with pre-existed
   instance emi-A8F63C29
#. Linux command experience.

Get VM compute nodes
--------------------

Before going through this tutorial, please obtain two VM instances
(instance# emi-A8F63C29) from FutureGrid India-Eucalyptus. For
detailed information about starting Eucalyptus VM, please see the
section :ref:`s-eucalyptus`. Assuming there are two VM instances
running as shown in the following section, you will then need to set
the hostname and mount an attached disk on each VM before starting
Hadoop.

VM Hostname setting
~~~~~~~~~~~~~~~~~~~

In order to run Hadoop 0.20.203.0 successfully without "HDFS path not
found" error, please add hostname to each compute node. For instance,
set “10.0.2.131” as “master” and “10.0.2.132” as “slave”::

    [johnny@i136 johnny-euca]$ euca-describe-instances
    RESERVATION     r-442E080F      johnny  default
    INSTANCE        i-46B007AE emi-A8F63C29 149.165.146.207 10.0.2.131       running         johnny        0       c1.medium 2011-02-18T22:37:36.772Z     india   eki-78EF12D2    eri-5BB61255
    INSTANCE        i-574E09D8 emi-A8F63C29 149.165.159.160 10.0.2.132       running         johnny        0       c1.medium 2011-02-18T22:37:36.772Z     india   eki-78EF12D2    eri-5BB61255


    # copy the ssh keys to each node for internal VM communication
    [johnny@i136 johnny-euca]$ scp -i johnny.private root@149.165.146.207:~/.ssh/id_rsa

    [johnny@i136 johnny-euca]$ scp -i johnny.private root@149.165.146.160:~/.ssh/id_rsa

    [johnny@i136 johnny-euca]$ ssh -i johnny.private root@149.165.146.207 

      … Welcome to Ubuntu! …

    root@localhost:~# vim /etc/hosts

    10.0.2.131 master

    10.0.2.132 slave

    root@localhost:~# hostname master

    root@localhost:~# scp /etc/hosts

    root@slave:/etc/hosts

    root@localhost:~# ssh slave

    … Welcome to Ubuntu! …

    root@localhost:~# hostname slave

    root@localhost:~# exit

    root@localhost:~#

VM attached disk configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The started VM instance(s) will normally have an unformatted disk
attached on /dev/sda2. If you require more disk space, you can do the
following to format and to mount it. In our example, we format it and
mount it to /tmp.

Note: DO NOT format /dev/sda1. This is the main partition containing
the OS::

    root@master:~/# fdisk -l | grep '^Disk'
    Disk /dev/sda1 doesn't contain a valid partition table
    Disk /dev/sda2 doesn't contain a valid partition table
    Disk /dev/sda3 doesn't contain a valid partition table
    Disk /dev/sda1: 2147 MB, 2147483648 bytes
    Disk identifier: 0x00000000
    Disk /dev/sda2: 8045 MB, 8045723648 bytes
    Disk identifier: 0x00000000
    Disk /dev/sda3: 536 MB, 536870912 bytes
    Disk identifier: 0x00000000

    root@master:~/# mkfs.ext3 /dev/sda2
    .....

    root@master:~# mount /dev/sda2 /tmp
    root@master:/tmp# df -h

    Filesystem            Size  Used Avail Use% Mounted on
    /dev/sda1             2.0G  1.1G  799M  59% /
    udev                  3.0G   40K  3.0G   1% /dev
    none                  3.0G     0  3.0G   0% /dev/shm
    none                  3.0G   48K  3.0G   1% /var/run
    none                  3.0G     0  3.0G   0% /var/lock
    none                  3.0G     0  3.0G   0% /lib/init/rw
    /dev/sda2             7.4G    1M  0.1G   1% /tmp



Hadoop Configuration
--------------------

Once you obtain several VM compute instances, you will need to download
a customized `Hadoop 0.20.203.0 package (for Euca
VM) <http://salsahpc.indiana.edu/tutorial/apps/hadoop-0.20.203.0-for-EucaVm.tar.gz>`__
from `SalsaHPC <http://salsahpc.indiana.edu/>`__ webserver to each VM
instance and unzip it to the same directory location, then simply
startup Hadoop with a OneClick script MultiNodesOneClickStartUp.sh::

    Script usage: . ./MultiNodesOneClickStartUp.sh [Path to Java JRE/JDK Home] [Compute Nodes IPs/hostnames Info Files]

The script MultiNodesOneClickStartUp.sh mainly fills the Hadoop
required configuration parameters under
$HADOOP\_HOME/conf/hadoop-env.sh, $HADOOP\_HOME/conf/masters,
$HADOOP\_HOME/conf/slaves, $HADOOP\_HOME/conf/core-site.xml,
$HADOOP\_HOME/conf/hdfs-site.xml, and
$HADOOP\_HOME/conf/mapred-site.xml. You can also manually change these
configuration files, however, please make sure you have similar
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


Make sure you download the hadoop package to each VM and unzip to
same location::

    # please do this on each VM under same location
    root@master:~# apt-get install lynx
    root@master:~# wget http://salsahpc.indiana.edu/tutorial/apps/hadoop-0.20.203.0-for-EucaVm.t...
    root@master:~# tar -zxvf hadoop-0.20.203.0-for-EucaVm.tar.gz    
    root@master:~# cd hadoop-0.20.203.0

    # add a nodes file included VMs' IPs for hadoop framework 
     root@master:hadoop-0.20.203.0# vim nodes
    10.0.2.131
    10.0.2.132

    root@master:hadoop-0.20.203.0# . ./MultiNodesOneClickStartUp.sh /root/jdk1.6.0_33/ nodes

    *********************************************************************
    Hadoop 0.20.203.0 Multinodes OneClick Startup script
    *********************************************************************
    HADOOP_HOME = /N/u/johnny/hadoop-0.20.203.0
    Master Hostname = master
    Slaves IP/Hostname = 10.0.2.131
    10.0.2.132
    Username = root
    …
    …
    bin/start-all.sh
    starting namenode, logging to /root/hadoop-0.20.203.0/bin/../logs/hadoop-root-namenode-master.out
    WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    master: starting datanode, logging to /root/hadoop-0.20.203.0/bin/../logs/hadoop-root-datanode-master.out
    slave: starting datanode, logging to /root/hadoop-0.20.203.0/bin/../logs/hadoop-root-datanode-slave.out
    master: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    slave: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    master: starting secondarynamenode, logging to /root/hadoop-0.20.203.0/bin/../logs/hadoop-root-secondarynamenode-master.out
    master: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    starting jobtracker, logging to /N/u/root/hadoop-0.20.203.0/bin/../logs/hadoop-root-jobtracker-master.out
    WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    master: starting tasktracker, logging to /root/hadoop-0.20.203.0/bin/../logs/hadoop-root-tasktracker-master.out
    slave: starting tasktracker, logging to /root/hadoop-0.20.203.0/bin/../logs/hadoop-root-tasktracker-slave.out
    master: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    slave: WARNING: org.apache.hadoop.metrics.jvm.EventCounter is deprecated. Please use org.apache.hadoop.log.metrics.EventCounter in all the log4j.properties files.
    *************************************
    Hadoop has been started successfully.
    *************************************

    Please use lynx 10.0.2.131:9001 to see HDFS status
    Please use lynx 10.0.2.132:9003 to see MapReduce Daemon status

Verify Hadoop HDFS and MapReduce Daemon status
----------------------------------------------

After starting Hadoop with the OneClick startup script, you will need
to make sure HDFS and MapReduce Daemon are also started correctly before
running any program. As shown above, the last two messages indicate the
​http addresses to check HDFS and MapReduce status. Then, type the
commands lynx 10.0.2.131:9001 and lynx 10.0.2.131:9003::

    root@master:hadoop-0.20.203.0# lynx 10.0.2.131:9001
    …
    Cluster Summary
       8 files and directories, 1 blocks = 9 total.
       Heap Memory used 15.19 MB is 20% of Commited Heap Memory 72.5 MB. Max Heap Memory is 888.94 MB.
       Non Heap Memory used 18.91 MB is 81% of Commited Non Heap Memory 23.19 MB. Max Non Heap Memory is 130 MB.

       Configured Capacity                    : 15.73 GB
       DFS Used                               : 56.03 KB
       Non DFS Used                           : 0.45 GB
       DFS Remaining                          : 15.29 GB
       DFS Used%                              : 0 %
       DFS Remaining%                         : 97.92 %
       Live Nodes                             : 2
       Dead Nodes                             : 0
       Decommissioning Nodes             : 0
       Number of Under-Replicated Blocks : 1

    root@master:hadoop-0.20.203.0# lynx 10.0.2.131:9003
    Cluster Summary (Heap Size is 56.94 MB/888.94 MB)
       Queues Running Map Tasks Running Reduce Tasks Total Submissions Nodes Occupied Map Slots Occupied Reduce
       Slots Reserved Map Slots Reserved Reduce Slots Map Slot Capacity Reduce Slot Capacity Avg. Slots/Node
       Blacklisted Nodes Excluded Nodes
       1 0 0 0 2 0 0 0 0 4 4 4.00 0 

    0

If you see all “0” in above text, you should wait until it turns into
number(s) other than “0”. Here, as we are running Hadoop with 2 nodes,
"Live Nodes" is shown as “2” in HDFS section; it is similar to
MapReduce Section. If there is not any change after 15 minutes, you
should restart it by rerunning the MultiNodesOneClickStartUp.sh script.

Run Hadoop Applications
-----------------------

Now, after startung Hadoop successfully, you can try to run the provided
examples `Hadoop
WordCount <https://portal.futuregrid.org/manual/hadoop-wordcount>`__ and
`Hadoop Blast <https://portal.futuregrid.org/manual/hadoop-blast>`__.
