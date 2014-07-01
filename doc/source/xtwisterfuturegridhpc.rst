.. _s-salsa-hadoop-hpc:

================================================
Twister with FutureGrid HPC
================================================

.. sidebar:: Page Contents

   .. contents::
      :local:

Author: Tak-Lon Stephen Wu
Version: 0.1
Date: 2011-10-30


Twister is widely used by domain scientists for running their
scientific applications in parallel fashion. Here, we provide a detail
instruction to use Hadoop on FutureGrid test-bed with FutureGrid India
Cluster.

Requirement
-----------

#. FutureGrid HPC account, please apply via `FutureGrid
   portal <https://portal.futuregrid.org/user/register>`__ and `request
   a HPC account <https://portal.futuregrid.org/request-hpc-account>`__.
#. Linux command experience.

Get HPC compute nodes
---------------------

First, you will need to login to IU-india using the command: 

::

    Login command: ssh –i [ssh private key] [username]@india.futuregrid.org

::

    ssh –i key.pem johnny@india.futuregrid.org
    Enter passphrase for key 'ssh_id_rsa':
    [johnny@i136 ~]$

Here, “i136” is the headnode (first login node) of IU-india cluster.
You will obtain several HPC compute nodes from this node. Noted
that, \ **DO NOT** run any of your program on the “i136” headnode. Then,
on the command prompt, type the following command to get a set of
compute nodes:

::

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

Twister Configuration
---------------------

We provide a detail instruction to startup twister 0.9. In this example,
we use i55 as Driver/Master node, i56 as Worker/Slave node.

Download Twister 0.9
~~~~~~~~~~~~~~~~~~~~

::

    [johnny@i55 ~]$ wget http://salsahpc.indiana.edu/tutorial/apps/Twister-0.9.tar.gz
    [johnny@i55 ~]$ tar -zxvf Twister-0.9.tar.gz

Set $TWISTER\_HOME, $JAVA\_HOME and Worker nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running Twister configuration script, we need to setup several
environment parameters:

::

    [johnny@i55 ~]$ echo export TWISTER_HOME=/N/u/johnny/twister-0.9 >> ~/.bashrc
    [johnny@i55 ~]$ echo export JAVA_HOME=/N/soft/jdk1.6.0_20-x86_64 >> ~/.bashrc
    [johnny@i55 ~]$ source ~/.bashrc
    [johnny@i55 ~]$ vi $TWISTER_HOME/bin/nodes
    i55
    i56

Run TwisterPowerMakeUp.sh
~~~~~~~~~~~~~~~~~~~~~~~~~

Within twister 0.9 package, there is a TwisterPowerMakeUp.sh script to
automatically configure Twister. Generally, it randomly picks one of the
working nodes as ActiveMQ messaging broker, sets working daemon per node,
and worker (mapper/reducer) per daemon. Also, it creates Twister
required directories such as app\_dir and data\_dir. 

::

    [johnny@i55 bin]$ cd $TWISTER_HOME/bin
    [johnny@i55 bin]$ ./TwisterPowerMakeUp.sh
    use normal MultiNode Setup
    no special processing to nodes
    ActiveMQ uri=failover:(tcp://i56:61616)
    nodes_file=/N/u/johnny/twister-0.9/bin/nodes
    daemons_per_node=1
    workers_per_daemon=8
    app_dir=/N/u/johnny/twister-0.9/apps
    i55:/N/u/johnny/twister-0.9/data created.
    i56:/N/u/johnny/twister-0.9/data created.
    data_dir=/N/u/johnny/twister-0.9/data
    Change max memory to 16054 MB
    copied to i55:/N/u/johnny/twister-0.9
    copied to i56:/N/u/johnny/twister-0.9
    Auto configuration is done.

As shown in the message above "ActiveMQ
uri=failover:(\ `tcp://i56:61616 <//i56:61616>`__)", i56 is the selected
node where ActiveMQ messaging broker will be started.  

Download and start ActiveMQ on specific nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now ssh to the selected node, i56, then download and unzip the ActiveMQ
package. Finally start it up and return the previous master node, i56.

::

    [johnny@i55 bin]$ ssh i56
    [johnny@i56 ~]$ wget http://www.iterativemapreduce.org/apache-activemq-5.4.2-bin.tar.gz
    [johnny@i56 ~]$ cd apache-activemq-5.4.2
    [johnny@i56 apache-activemq-5.4.2]$ cd bin
    [johnny@i56 bin]$ ./activemq console &
    [1] 4009
    [johnny@i56 bin]$ INFO: Using default configuration
    (you can configure options in one of these file: /etc/default/activemq /N/u/johnny/.activemqrc)
    INFO: Invoke the following command to create a configuration file
    ./activemq setup [ /etc/default/activemq /N/u/johnny/.activemqrc ]
    INFO: Using java '/N/soft/jdk1.6.0_20-x86_64/bin/java'
    INFO: Starting in foreground, this is just for debugging purposes (stop process by pressing CTRL+C)
    Java Runtime: Sun Microsystems Inc. 1.6.0_20 /N/soft/jdk1.6.0_20-x86_64/jre
      Heap sizes: current=251264k  free=247327k  max=251264k
        JVM args: -Xms256M -Xmx256M -Dorg.apache.activemq.UseDedicatedTaskRunner=true -Djava.util.logging.config.file=logging.properties -Dcom.sun.management.jmxremote -Dactivemq.classpath=/N/u/johnny/apache-activemq-5.4.2/conf; -Dactivemq.home=/N/u/johnny/apache-activemq-5.4.2 -Dactivemq.base=/N/u/johnny/apache-activemq-5.4.2
    ACTIVEMQ_HOME: /N/u/johnny/apache-activemq-5.4.2
    ACTIVEMQ_BASE: /N/u/johnny/apache-activemq-5.4.2
    Loading message broker from: xbean:activemq.xml
     INFO Refreshing org.apache.activemq.xbean.XBeanBrokerFactory$1@245e13ad: startup date [Sun Oct 30 23:33:22 EDT 2011]; root of context hierarchy
     WARN destroyApplicationContextOnStop parameter is deprecated, please use shutdown hooks instead
     INFO PListStore:/N/u/johnny/apache-activemq-5.4.2/data/localhost/tmp_storage started
     INFO Using Persistence Adapter: KahaDBPersistenceAdapter[/N/u/johnny/apache-activemq-5.4.2/data/kahadb]
     INFO KahaDB is version 3
     INFO Recovering from the journal ...
     INFO Recovery replayed 1 operations from the journal in 0.0080 seconds.
     INFO ActiveMQ 5.4.2 JMS Message Broker (localhost) is starting
     INFO For help or more information please see: http://activemq.apache.org/
     INFO Listening for connections at: tcp://i56:61616
     INFO Connector openwire Started
     INFO ActiveMQ JMS Message Broker (localhost, ID:i56-56404-1320032003342-0:1) started
     INFO jetty-7.1.6.v20100715
     INFO ActiveMQ WebConsole initialized.
     INFO Initializing Spring FrameworkServlet 'dispatcher'
     INFO ActiveMQ Console at http://0.0.0.0:8161/admin
     INFO Initializing Spring root WebApplicationContext
     INFO camel-osgi.jar/camel-spring-osgi.jar not detected in classpath
     INFO Apache Camel 2.4.0 (CamelContext: camel) is starting
     INFO JMX enabled. Using ManagedManagementStrategy.
     INFO Found 4 packages with 15 @Converter classes to load
     INFO Loaded 146 type converters in 0.337 seconds
     INFO Connector vm://localhost Started
     INFO Route: route1 started and consuming from: Endpoint[activemq://example.A]
     INFO Started 1 routes
     INFO Apache Camel 2.4.0 (CamelContext: camel) started in 0.783 seconds
     INFO Camel Console at http://0.0.0.0:8161/camel
     INFO ActiveMQ Web Demos at http://0.0.0.0:8161/demo
     INFO RESTful file access application at http://0.0.0.0:8161/fileserver
     INFO Started SelectChannelConnector@0.0.0.0:8161
    [johnny@i56 bin]$ exit 
    [johnny@i55 bin]$

Start Twister
~~~~~~~~~~~~~

After you go back to the master node (i55), simply type command
./start\_twister.sh & under $TWISTER\_HOME/bin.

::

    [johnny@i55 bin]$ ./start_twister.sh &
    [1] 7844
    [johnny@i55 bin]$ i55
    Oct 30, 2011 11:34:38 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://i56:61616
    1    [main] INFO  cgl.imr.worker.DaemonWorker  - Daemon no: 0 started with 8 workers.
    i56
    Oct 30, 2011 11:34:39 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://i56:61616
    0    [main] INFO  cgl.imr.worker.DaemonWorker  - Daemon no: 1 started with 8 workers.

    [1]+  Done                    ./start_twister.sh

If you can see similar message above, twister has started
successfully.

Verify Twister Status
---------------------

Also you can use command "jps" on each node to make sure Twister
(TwisterDaemon) is running.

On master node::

    # on master node
    [johnny@i55 bin]$ jps
    7878 TwisterDaemon
    7909 Jps

 
On slave and ActiveMQ node::

    # on slave and ActiveMQ node
    [johnny@i56 bin]$ jps
    4265 Jps
    4025 run.jar
    4185 TwisterDaemon

Next step, try out the Twister Applications section to run Twister
Kmeans or Twister Blast.
