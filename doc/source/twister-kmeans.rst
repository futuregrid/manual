
.. _s-twister-kmeans:

**********************************************************************
Running Twister Kmeans on FutureGrid HPC
**********************************************************************

.. sidebar:: Page Contents

   Author: Tak-Lon Stephen Wu

   .. contents::
      :local:

In statistics and machine learning, Kmeans clustering is a method of
cluster analysis which aims to partition n observation into k clusters
where each observation belongs to the cluster with the nearest mean
[`wikipedia <http://en.wikipedia.org/wiki/K-means_clustering>`_].

In each iteration of Twister Kmeans, all the map tasks get the same
input data (current cluster centers) and each computes a partial cluster
centers by going through the 3D data points owned by itself. A reduce
task computes the average of the partial cluster centers and produce the
cluster centers for the next step. Main program, once it gets these new
cluster centers, calculates the difference between the new cluster
centers and the previous cluster centers, then determine if it needs to
execute another cycle of MapReduce computation.

.. figure:: http://salsahpc.indiana.edu/tutorial/images/kmeans_color.png
   :align: center
   :alt: 

Figure 1. The workflow of Kmeans application with Twister MapReduce
framework

The following tutorial shows the steps running built-in Twister Kmeans
application within the `Twister 0.9
package <http://www.iterativemapreduce.org/twister-0.9.tar.gz>`_.

Acknowledge
~~~~~~~~~~~

This page was original designed by
`SalsaHPC <http://salsahpc.indiana.edu/>`_ group for `Big Data for
Science Workshop <http://salsahpc.indiana.edu/tutorial/>`_, you can see
the original pages
`here <http://salsahpc.indiana.edu/tutorial/twister_kmeans_user_guide.htm>`_.

Requirement
~~~~~~~~~~~

#. Login to FutureGrid Cluster and obtain compute nodes.
   (`HPC <https://portal.futuregrid.org/salsahadoop-futuregrid-hpc#HPC_Nodes>`_/
   `Eucalyptus <https://portal.futuregrid.org/tutorials/eucalyptus>`_)
#. Start ActiveMQ and Twister on compute nodes. (`Twister on FutureGrid
   Tutorial <https://portal.futuregrid.org/twister-futuregrid-hpc>`_)
#. Download and unzip `Twister Kmeans source
   code <http://salsahpc.indiana.edu/tutorial/source_code/Twister-Kmeans.zip>`_
   from `Big Data for Science
   tutorial <http://salsahpc.indiana.edu/tutorial/twister_kmeans_user_guide.htm>`_.
#. Install Apache Ant on the working node.
#. Linux command experience.
#. Open two command prompts, one for Twister driver/master directory
   under $TWISTER\_HOME/bin, another for Twister Kmeans examples
   directory $TWISTER\_HOME/samples/kmeans/bin/

Check if Twister-Kmeans-0.9.jar exist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From now on, you will need to open two command prompts, one for Twister
Driver under $TWISTER\_HOME/bin, another for kmeans application
$TWISTER\_HOME/samples/kmeans/bin. Detail instruction of running Twister
Kmeans can also found in $TWISTER\_HOME/samples/kmeans/README.txt.
Assuming your start Twister with setting $TWISTER\_HOME=~/twister-0.9,
the driver/master is running on i55, and ActiveMQ broker is running on
i56. Then, we check the exist of the Kmeans executable
$TWISTER\_HOME/apps/Twister-Kmeans-0.9.jar. If we cannot find it, please
run ant compiler under Twister Kmeans examples directory
$TWISTER\_HOME/samples/kmeans/

::

    [taklwu@i55 bin]$ ls -l $TWISTER_HOME/apps
    total 20
    -rw------- 1 taklwu users 13876 Oct 21 13:24 Twister-Kmeans-0.9.jar

Prepare input data directory across worker nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before the input data set is generated, we need to make a general
directory on all nodes in order to store them locally. Therefore, on the
Twister Driver command prompt under $TWISTER\_HOME/bin, we make Kmeans
directory with using Twister driver script ./twister.sh mkdir kmeans

::

    [taklwu@i55 bin]$ ./twister.sh mkdir kmeans
    i55:/N/u/taklwu/twister-0.9/data/kmeans created.
    mkdir: cannot create directory `/N/u/taklwu/twister-0.9/data/kmeans': File exists
    i56:/N/u/taklwu/twister-0.9/data/kmeans created.

The warning "mkdir: cannot create directory
\`/N/u/taklwu/twister-0.9/data/kmeans': File exists" is shown as we are
using Shared File System on HPC nodes. It will not be shown if we run
Twister Kmeans on Eucalyptus.

Generate Kmeans input data
~~~~~~~~~~~~~~~~~~~~~~~~~~

After making the Kmeans directories across all worker nodes, on the
Kmeans application command prompt under
$TWISTER\_HOME/samples/kmeans/bin, run the gen\_data.sh script to
generate the Kmeans input data set and distribute to all worker nodes.

::

    Script usage: ./gen_data.sh  [init clusters file][num of clusters][vector length][sub dir][data file prefix][number of files to generate][number of data points]
    e.g. ./gen_data.sh init_clusters.txt 2 3 /kmeans km_data 80 80000

    [taklwu@i55 bin]$ ./gen_data.sh init_clusters.txt 2 3 /kmeans km_data 80 80000

    kmeans args.len:7
    JobID: kmeans-data-gen2b1ce8c3-fe6d-11e0-9a94-e966ca4f6cd6
    Oct 24, 2011 2:22:45 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://i56:61616
    0    [main] INFO  cgl.imr.client.TwisterDriver  - MapReduce computation termintated gracefully.
    9    [Thread-1] DEBUG cgl.imr.client.ShutdownHook  - Shutting down completed.

Here "sub dir" refers to the directory where you want the data files to
be saved remotely. This is a sub directory under data\_dir of all the
nodes.

Create Partition File
~~~~~~~~~~~~~~~~~~~~~

Irrespective of whether you generate data using above method or manually
you need to create a partition file to run the application. On the
Twister Driver command prompt under $TWISTER\_HOME/bin, run the
create\_partition\_file.sh script to create the partition file (file
location metadata) according to the input data set distribution.

::

    Script usage: ./create_partition_file.sh [common directory][file filter][partition file]
    e.g. ./create_partition_file.sh /kmeans km_data kmeans.pf

    [taklwu@i55 bin]$ ./create_partition_file.sh /kmeans km_data kmeans.pf
    Oct 24, 2011 2:28:50 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://i56:61616
    Partition file created.

Run Kmeans Clustering
~~~~~~~~~~~~~~~~~~~~~

Once the above steps are successful you can simply run the following
shell script to run Kmeans clustering application. Here, on the Kmeans
application command prompt $TWISTER\_HOME/samples/kmeans/bin, run the
application script run\_kmeans.sh and submit the job to Twister
Driver/Master Daemon.

::

    Script usage: ./run_kmeans.sh [init clusters file][number of map tasks][partition file]
    e.g. ./run_kmeans.sh init_clusters.txt 80 $TWISTER_HOME/bin/kmeans.pf

    [taklwu@i55 bin]$ ./run_kmeans.sh init_clusters.txt 80 $TWISTER_HOME/bin/kmeans.pf
    JobID: kmeans-map-reduce52c1b91f-fe6e-11e0-9e5d-3fed4ed93ecd
    Oct 24, 2011 2:31:01 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://i56:61616
    0    [main] INFO  cgl.imr.client.TwisterDriver  - Configure Mappers through the partition file, please wait....
    4226 [main] INFO  cgl.imr.client.TwisterDriver  - Configuring Mappers through the partition file is completed.
    252.4857784991884 , 373.4822574603571 , 245.93135222874267 ,
    244.99837316981603 , 123.22713052183707 , 252.94566387185583 ,
    Total Time for kemeans : 6.487
    Total loop count : 7
    5891 [main] INFO  cgl.imr.client.TwisterDriver  - MapReduce computation termintated gracefully.
    ------------------------------------------------------
    Kmeans clustering took 6.502 seconds.
    ------------------------------------------------------
    5893 [Thread-1] DEBUG cgl.imr.client.ShutdownHook  - Shutting down completed.


