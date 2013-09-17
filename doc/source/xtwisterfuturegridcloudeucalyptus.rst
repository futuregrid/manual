.. _s-twister-eucalyptus:

=============================================================
Twister with FutureGrid Cloud Eucalyptus
=============================================================

.. sidebar:: Page Contents

   .. contents::
      :local:
 

Author: Tak-Lon Stephen Wu
Version: 0.1
Date: 2011-10-30

Twister is widely used by domain scientists for running their
scientific applications in parallel fashion. Here, we provide an example
to use Hadoop on FutureGrid test-bed with FutureGrid India Eucalyptus.


Requirement
-----------

#. FutureGrid HPC account, please apply via `FutureGrid
   portal <https://portal.futuregrid.org/user/register>`__ and `request
   a HPC account <https://portal.futuregrid.org/request-hpc-account>`__.
#. FutureGrid Eucalyptus account, please apply via `FutureGrid (India)
   Eucalyptus
   Portal <https://portal.futuregrid.org/request-eucalyptus-account%20>`__
#. FutureGrid Eucalyptus credentials zip file
   (euca2-[username]-x509.zip) stored under user home directory. 
#. Linux command experience.

Get VM compute nodes
--------------------

Before going through this tutorial, please obtain two VM instances
(instance# emi-D778156D) from FutureGrid India-Eucalyptus. For detail
information about starting Eucalyptus VM, please see
the \ `FutureGrid Eucalyptus
tutorial <https://portal.futuregrid.org/tutorials/eucalyptus>`__.
Assuming there are two VM instances running as shown in the following
section, you will then need to set the hostname and mount a attached
disk on each VM before starting Twister.

VM Hostname setting
~~~~~~~~~~~~~~~~~~~

In order to run Twister successfully without getting errors from the
environment setting , please add hostname to each compute node, for
instances, set “10.0.2.131” as “master” and set “10.0.2.132” as “slave”::

    [johnny@i136 johnny-euca]$ euca-describe-instances
    RESERVATION     r-442E080F      johnny  default
    INSTANCE        i-46B007AE      emi-D778156D    149.165.146.207 10.0.2.131       running         johnny        0       c1.medium 2011-02-18T22:37:36.772Z     india   eki-78EF12D2    eri-5BB61255
    INSTANCE        i-574E09D8      emi-D778156D    149.165.159.160 10.0.2.132       running         johnny        0       c1.medium 2011-02-18T22:37:36.772Z     india   eki-78EF12D2    eri-5BB61255

    [johnny@i136 johnny-euca]$ ssh -i johnny.private root@149.165.146.207

    …
    Welcome to Ubuntu!
    …
    root@localhost:~# vim /etc/hosts
    10.0.2.131 master
    10.0.2.132 slave

    root@localhost:~# hostname master
    root@localhost:~# scp /etc/hosts root@slaves:/etc/hosts
    root@localhost:~# ssh slave

    …
    Welcome to Ubuntu!
    …
    root@localhost:~# hostname slave
    root@localhost:~# exit

    root@localhost:~#

VM attached disk configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The started VM instance(s) will normally have an unformatted disk
attached on /dev/sda2. If you require more disk space, you can do the
following to format and to mount it. In our example, we format it and
mount it to /tmp.

Noted that DO NOT format the /dev/sda1 which is the main partition
contains the OS::

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
    root@master:~# df -h

    Filesystem            Size  Used Avail Use% Mounted on
    /dev/sda1             2.0G  1.1G  799M  59% /
    udev                  3.0G   40K  3.0G   1% /dev
    none                  3.0G     0  3.0G   0% /dev/shm
    none                  3.0G   48K  3.0G   1% /var/run
    none                  3.0G     0  3.0G   0% /var/lock
    none                  3.0G     0  3.0G   0% /lib/init/rw
    /dev/sda2             7.4G    1M  0.1G   1% /tmp



Twister Configuration
---------------------

We provide a detail instruction to startup twister 0.9. In this example,
we use "10.0.2.131"/master as Driver/Master node, "10.0.2.132"/slave as
Worker/Slave node.

Download Twister 0.9
~~~~~~~~~~~~~~~~~~~~

In VM mode, since we attach the extra larger disk on /tmp, we will
download Twister package on all VM nodes under /tmp::

    root@master:~# cd /tmp
    root@master:tmp# wget http://salsahpc.indiana.edu/tutorial/apps/Twister-0.9.tar.gz
    root@master:tmp# tar -zxvf Twister-0.9.tar.gz

Set $TWISTER\_HOME, $JAVA\_HOME and Worker nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running Twister configuration script, we need to setup several
environment parameters::

    root@master:tmp# echo export TWISTER_HOME=/tmp/twister-0.9 >> ~/.bashrc
    root@master:tmp# echo export JAVA_HOME=/usr/lib/jvm/java-6-sun/ >> ~/.bashrc
    root@master:tmp# source ~/.bashrc
    root@master:tmp# vi $TWISTER_HOME/bin/nodes
    master
    slave

Run TwisterPowerMakeUp.sh
~~~~~~~~~~~~~~~~~~~~~~~~~

Within twister 0.9 package, there is a TwisterPowerMakeUp.sh script to
automatically configure Twister. Generally, it randomly pick one of the
working node as ActiveMQ messaging broker, set working daemon per node,
and worker (mapper/reducer) per daemon. Also, it creates Twister
required directories such as app\_dir and data\_dir::

    root@master:tmp# cd $TWISTER_HOME/bin
    root@master:bin# ./TwisterPowerMakeUp.sh
    use normal MultiNode Setup
    no special processing to nodes
    ActiveMQ uri=failover:(tcp://slave:61616)
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
uri=failover:(\ `tcp://slave:61616 <//slave:61616>`__)", slave is the
selected node where ActiveMQ messaging broker will be started.  

Download and start ActiveMQ on specific node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now ssh to the selected node, slave, then download and unzip the
ActiveMQ package under /tmp. Finally, we start it up and return the
previous Driver/Master node::

    root@master:bin# ssh slave
    root@slave:~# cd /tmp
    root@slave:tmp# wget http://www.iterativemapreduce.org/apache-activemq-5.4.2-bin.tar.gz
    root@slave:tmp# cd apache-activemq-5.4.2/bin
    root@slave:bin# ./activemq console &
    [1] 4009
    [johnny@slave bin]$ INFO: Using default configuration
    (you can configure options in one of these file: /etc/default/activemq /tmp/.activemqrc)
    INFO: Invoke the following command to create a configuration file
    ./activemq setup [ /etc/default/activemq /tmp/.activemqrc ]
    INFO: Using java '/usr/lib/jvm/java-6-sun/jre/bin/java'
    INFO: Starting in foreground, this is just for debugging purposes (stop process by pressing CTRL+C)
    Java Runtime: Sun Microsystems Inc. 1.6.0_20 /N/soft/jdk1.6.0_20-x86_64/jre
      Heap sizes: current=251264k  free=247327k  max=251264k
        JVM args: -Xms256M -Xmx256M -Dorg.apache.activemq.UseDedicatedTaskRunner=true -Djava.util.logging.config.file=logging.properties -Dcom.sun.management.jmxremote -Dactivemq.classpath=/tmp/apache-activemq-5.4.2/conf; -Dactivemq.home=/tmp/apache-activemq-5.4.2 -Dactivemq.base=/tmp/apache-activemq-5.4.2
    ACTIVEMQ_HOME: /tmp/apache-activemq-5.4.2
    ACTIVEMQ_BASE: /tmp/apache-activemq-5.4.2
    Loading message broker from: xbean:activemq.xml
     INFO Refreshing org.apache.activemq.xbean.XBeanBrokerFactory$1@245e13ad: startup date [Sun Oct 30 23:33:22 EDT 2011]; root of context hierarchy
     WARN destroyApplicationContextOnStop parameter is deprecated, please use shutdown hooks instead
     INFO PListStore:/tmp/apache-activemq-5.4.2/data/localhost/tmp_storage started
     INFO Using Persistence Adapter: KahaDBPersistenceAdapter[/tmp/apache-activemq-5.4.2/data/kahadb]
     INFO KahaDB is version 3
     INFO Recovering from the journal ...
     INFO Recovery replayed 1 operations from the journal in 0.0080 seconds.
     INFO ActiveMQ 5.4.2 JMS Message Broker (localhost) is starting
     INFO For help or more information please see: http://activemq.apache.org/
     INFO Listening for connections at: tcp://slave:61616
     INFO Connector openwire Started
     INFO ActiveMQ JMS Message Broker (localhost, ID:slave-56404-1320032003342-0:1) started
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
    root@slave:bin# exit 
    root@master:bin# 

Start Twister
~~~~~~~~~~~~~

After you go back to the master node (master), simply type command
./start\_twister.sh & under $TWISTER\_HOME/bin::

    [root@master:bin# ./start_twister.sh &
    [1] 7844
    root@master:bin# master
    Oct 30, 2011 11:34:38 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://slave:61616
    1    [main] INFO  cgl.imr.worker.DaemonWorker  - Daemon no: 0 started with 8 workers.
    slave
    Oct 30, 2011 11:34:39 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://slave:61616
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
    root@master:bin# jps
    7878 TwisterDaemon
    7909 Jps


On slave and ActiveMQ node::

    # on slave and ActiveMQ node
    root@slave:bin# jps
    4265 Jps
    4025 run.jar
    4185 TwisterDaemon

