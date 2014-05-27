
.. _s-twister-on-opestack:

**********************************************************************
Running Twister on FutureGrid OpenStack
**********************************************************************

.. sidebar:: Page Contents

   Author: Tak-Lon Stephen Wu

   .. contents::
      :local:



Twister is widely used by domain scientists for running their scientific
applications in parallel fashion. Here, we provide an example to use
Hadoop on FutureGrid test-bed with FutureGrid India Eucalyptus.


Requirement
-----------

#. FutureGrid HPC account, please apply via `FutureGrid
   portal <https://portal.futuregrid.org/user/register>`_ and `request a
   HPC account <https://portal.futuregrid.org/request-hpc-account>`_.
#. FutureGrid OpenStack account
#. FutureGrid OpenStack credentials stored under user home directory .futuregrid/openstack_havana.
#. Linux command experience.


.. _vm-nodes:

Get VM compute nodes
--------------------

Before going through this tutorial, please obtain two m1.large VM instances
(instance# salsahpc/cloud-mooc-m1-large-4GB) from FutureGrid India-OpenStack. For detail
information about starting OpenStack VM, please see the `FutureGrid
OpenStack
tutorial <openstackhavana.html>`_.
Assuming there are two VM instances running as shown in the following
section, you will then need to set the hostname to /etc/hosts file and scp your VM ssh 
login private key file to the started VMs.

.. _vm-nodes-setting:

VM Hostname setting
~~~~~~~~~~~~~~~~~~~
Assmuning the two started VMs are show as following, and we will need to upload VM ssh
login private to each node as ~/.ssh/id_rsa to enable VMs communicate with each 
other. If you have followed the `FutureGrid OpenStack tutorial <openstackhavana.html>`_, 
and assuming you have created the ssh login private key as ~/.ssh/$USER-key, we upload 
this key to each node with using the commands below.

::

    [taklwu@i136 ~]$ source .futuregrid/openstack_havana/novarc
    [taklwu@i136 ~]$ nova list
	+--------------------------------------+---------------+--------+---------------------+
	| ID                                   | Name          | Status | Networks            |
	+--------------------------------------+---------------+--------+---------------------+
	| e15ad5b6-c3f0-4c07-996c-3bbe709a63b7 | taklwu-001    | ACTIVE | private=10.35.23.18 |
	| e15ad5b6-c3f0-4c07-996c-33rff4gg45g7 | taklwu-002    | ACTIVE | private=10.35.23.19 |
	+--------------------------------------+---------------+--------+---------------------+
    [taklwu@i136 ~]$ scp -i ~/.ssh/$USER-key root@10.35.23.18:~/.ssh/id_rsa
    [taklwu@i136 ~]$ scp -i ~/.ssh/$USER-key root@10.35.23.19:~/.ssh/id_rsa


In order to run Twister successfully without getting errors from the
environment setting , please modify the /etc/hosts file on each compute node, for
instances, set “10.35.23.18” as “taklwu-001 ” and set “10.35.23.19” as “taklwu-002”.

::

    [taklwu@i136 ~]$ ssh -i ~/.ssh/$USER-key root@10.35.23.18

    …
    Welcome to Ubuntu!
    …
    root@localhost:~# vim /etc/hosts
    10.35.23.18 taklwu-001
    10.35.23.19 taklwu-002

    root@taklwu-001:~# scp /etc/hosts root@taklwu-002:/etc/hosts
    root@taklwu-001:~# ssh slave

    …
    Welcome to Ubuntu!
    …
    root@taklwu-002:~# exit

    root@taklwu-001:~#

.. _twister-conf:

Twister Configuration
---------------------

We provide a detail instruction to startup twister 0.9. In this example,
we use "10.35.23.18"/taklwu-001 as Driver/Master node, "10.35.23.19"/taklwu-002 as
Worker/Slave node.

.. _twister-download:

Download Twister 0.9
~~~~~~~~~~~~~~~~~~~~

In VM mode, since we attach the larger disk on /tmp, we will
download Twister and Java JDK package on all VM nodes under /tmp.

::

    root@taklwu-001:~# cd /tmp
    root@taklwu-001:tmp# wget http://salsahpc.indiana.edu/tutorial/apps/Twister-0.9.tar.gz
    root@taklwu-001:tmp# tar -zxvf Twister-0.9.tar.gz

.. _twister-conf-setup:

Set $TWISTER\_HOME, $JAVA\_HOME and Worker nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running Twister configuration script, we need to setup several
environment parameters:

::

    root@master:tmp# echo export TWISTER_HOME=/tmp/twister-0.9 >> ~/.bashrc
    root@master:tmp# echo export JAVA_HOME=/usr/lib/jvm/java-6-sun/ >> ~/.bashrc
    root@master:tmp# source ~/.bashrc
    root@master:tmp# vi $TWISTER_HOME/bin/nodes
    taklwu-001
    taklwu-002

.. _twisterpowermakeup:

Run TwisterPowerMakeUp.sh
~~~~~~~~~~~~~~~~~~~~~~~~~

Within twister 0.9 package, there is a TwisterPowerMakeUp.sh script to
automatically configure Twister. Generally, it randomly pick one of the
working node as ActiveMQ messaging broker, set working daemon per node,
and worker (mapper/reducer) per daemon. Also, it creates Twister
required directories such as app\_dir and data\_dir.

::

    root@taklwu-001:tmp# cd $TWISTER_HOME/bin
    root@taklwu-001:bin# ./TwisterPowerMakeUp.sh
    use normal MultiNode Setup
    no special processing to nodes
    ActiveMQ uri=failover:(tcp://taklwu-002:61616)
    nodes_file=/tmp/twister-0.9/bin/nodes
    daemons_per_node=1
    workers_per_daemon=8
    app_dir=/tmp/twister-0.9/apps
    master:/tmp/twister-0.9/data created.
    slave:/tmp/twister-0.9/data created.
    data_dir=/tmp/twister-0.9/data
    Change max memory to 16054 MB
    copied to master:/tmp/twister-0.9
    copied to slave:/tmp/twister-0.9
    Auto configuration is done.

As shown in the message above "ActiveMQ
uri=failover:(tcp://taklwu-002:61616)", taklwu-002 is the
selected node where ActiveMQ messaging broker will be started. (it may
randonly choose taklwu-001 as the broker node)


.. _twister-conf-activemq:

Download and start ActiveMQ on specific node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now ssh to the selected node, taklwu-002, then download and unzip the
ActiveMQ package under /tmp. Finally, we start it up and return the
previous Driver/Master node.

::

    root@taklwu-001:bin# ssh taklwu-002
    root@taklwu-002:~# cd /tmp
    root@taklwu-002:tmp# wget http://www.iterativemapreduce.org/apache-activemq-5.4.2-bin.tar.gz
    root@taklwu-002:tmp# cd apache-activemq-5.4.2/bin
    root@taklwu-002:bin# ./activemq console &
    [1] 4009
    [taklwu@slave bin]$ INFO: Using default configuration
    (you can configure options in one of these file: /etc/default/activemq /tmp/.activemqrc)
    INFO: Invoke the following command to create a configuration file
    ./activemq setup [ /etc/default/activemq | /tmp/.activemqrc ]
    INFO: Using java '/usr/lib/jvm/java-6-sun/jre/bin/java'
    INFO: Starting in foreground, this is just for debugging purposes (stop process by pressing CTRL+C)
    Java Runtime: Sun Microsystems Inc. 1.6.0_20 /N/soft/jdk1.6.0_20-x86_64/jre
      Heap sizes: current=251264k  free=247327k  max=251264k
        JVM args: -Xms256M -Xmx256M -Dorg.apache.activemq.UseDedicatedTaskRunner=true -Djava.util.logging.config.file=logging.properties -Dcom.sun.management.jmxremote -Dactivemq.classpath=/tmp/apache-activemq-5.4.2/conf; -Dactivemq.home=/tmp/apache-activemq-5.4.2 -Dactivemq.base=/tmp/apache-activemq-5.4.2
    ACTIVEMQ_HOME: /tmp/apache-activemq-5.4.2
    ACTIVEMQ_BASE: /tmp/apache-activemq-5.4.2
    Loading message broker from: xbean:activemq.xml
     INFO | Refreshing org.apache.activemq.xbean.XBeanBrokerFactory$1@245e13ad: startup date [Sun Oct 30 23:33:22 EDT 2011]; root of context hierarchy
     WARN | destroyApplicationContextOnStop parameter is deprecated, please use shutdown hooks instead
     INFO | PListStore:/tmp/apache-activemq-5.4.2/data/localhost/tmp_storage started
     INFO | Using Persistence Adapter: KahaDBPersistenceAdapter[/tmp/apache-activemq-5.4.2/data/kahadb]
     INFO | KahaDB is version 3
     INFO | Recovering from the journal ...
     INFO | Recovery replayed 1 operations from the journal in 0.0080 seconds.
     INFO | ActiveMQ 5.4.2 JMS Message Broker (localhost) is starting
     INFO | For help or more information please see: http://activemq.apache.org/
     INFO | Listening for connections at: tcp://slave:61616
     INFO | Connector openwire Started
     INFO | ActiveMQ JMS Message Broker (localhost, ID:slave-56404-1320032003342-0:1) started
     INFO | jetty-7.1.6.v20100715
     INFO | ActiveMQ WebConsole initialized.
     INFO | Initializing Spring FrameworkServlet 'dispatcher'
     INFO | ActiveMQ Console at http://0.0.0.0:8161/admin
     INFO | Initializing Spring root WebApplicationContext
     INFO | camel-osgi.jar/camel-spring-osgi.jar not detected in classpath
     INFO | Apache Camel 2.4.0 (CamelContext: camel) is starting
     INFO | JMX enabled. Using ManagedManagementStrategy.
     INFO | Found 4 packages with 15 @Converter classes to load
     INFO | Loaded 146 type converters in 0.337 seconds
     INFO | Connector vm://localhost Started
     INFO | Route: route1 started and consuming from: Endpoint[activemq://example.A]
     INFO | Started 1 routes
     INFO | Apache Camel 2.4.0 (CamelContext: camel) started in 0.783 seconds
     INFO | Camel Console at http://0.0.0.0:8161/camel
     INFO | ActiveMQ Web Demos at http://0.0.0.0:8161/demo
     INFO | RESTful file access application at http://0.0.0.0:8161/fileserver
     INFO | Started SelectChannelConnector@0.0.0.0:8161
    root@taklwu-002:bin# exit 
    root@taklwu-001:bin# 


.. _run-twister:

Start Twister
~~~~~~~~~~~~~

After you go back to the master node (taklwu-001), simply type command
./start\_twister.sh & under $TWISTER\_HOME/bin.

::

    [root@master:bin# ./start_twister.sh &
    [1] 7844
    root@master:bin# 
    taklwu-001
    Oct 30, 2011 11:34:38 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://taklwu-002:61616
    1    [main] INFO  cgl.imr.worker.DaemonWorker  - Daemon no: 0 started with 8 workers.
    taklwu-002
    Oct 30, 2011 11:34:39 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://taklwu-002:61616
    0    [main] INFO  cgl.imr.worker.DaemonWorker  - Daemon no: 1 started with 8 workers.

    [1]+  Done                    ./start_twister.sh

If you can see similar message above, twister has started successfully.


.. _verify:

Verify Twister Status
---------------------

Also you can use command "jps" on each node to make sure Twister
(TwisterDaemon) is running.

On master node

::

    # on master node
    root@master:bin# jps
    7878 TwisterDaemon
    7909 Jps

On slave and ActiveMQ node

::

    # on slave and ActiveMQ node
    root@slave:bin# jps
    4265 Jps
    4025 run.jar
    4185 TwisterDaemon

