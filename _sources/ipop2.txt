.. _s-ipop2:

**********************************************************************
IPOP2 (IP-over-P2P) 
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:


`IPOP (IP-over-P2P) <http://www.ipop-project.org>`__ is a
software-defined virtual network that can be used as a basis for
creating virtual private clusters across multiple cloud providers and
administrative domains. IPOP is architected as a peer-to-peer (P2P)
overlay for tunneling and routing of encapsulated IP packets that are
captured/injected into virtual network interfaces (v-NICs). The IPOP
software consists of P2P routers that run on endpoints that are
connected to the virtual network, such as virtual machines (VMs)
distributed across multiple cloud providers.

This tutorial provides step-by-step instructions for deploying a
minimal independent P2P overlay upon which you can run IP-over-P2P
(IPOP) virtual private networks. This tutorial is a follow-up to the
`introductory IPOP
tutorial <http://manual.futuregrid.org/ipop1.html>`__, which
guides you through the process of connecting two VMs by using a public
P2P overlay that runs on `PlanetLab <http://www.planetlab.org>`__
resources. In this follow-up tutorial, you will learn how to deploy your
own P2P overlay which can be used instead of PlanetLab's public overlay.
This is useful if you plan to deploy your own isolated IPOP overlays for
private overlay networks.

Prerequisites:
~~~~~~~~~~~~~~

-  It is a pre-requisite that you have gone through the \ `introductory
   IPOP tutorial <http://manual.futuregrid.org/ipop1.html>`__
-  Basic knowledge of Unix/Linux command line tools



Step 1: Bringing up Alice and Bob VMs 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The first step in this tutorial is to deploy at least two virtual
machines which will be connected by an IPOP virtual network. Please
follow the instructions of the \ `introductory IPOP
tutorial <http://manual.futuregrid.org/ipop1.html>`__ before you
continue; is assumed you have started two VMs "Alice" and "Bob" as
described in that tutorial before proceeding to the next step.


Step 2: Disconnecting Alice and Bob VMs from the PlanetLab P2P overlay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The instructions of the `introductory IPOP tutorial <http://manual.futuregrid.org/ipop1.html>`__ work by
connecting Alice and Bob through an IPOP configuration where the P2P
overlay runs on PlanetLab. You will now disconnect the two VMs from this
IPOP network before you configure them to connet through a different P2P
overlay - one which you will set up in the next step.

Disconnect Alice and Bob from IPOP and make sure IPsec is disabled,
by running these commands, *as root, on both Alice and Bob*::
 
  /etc/init.d/groupvpn.sh stop
  /etc/init.d/racoon stop
  setkey -F
  setkey -FP
 

Step 3: Deploy Pam, a P2P Bootstrapping VM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you will deploy a VM that will run a small P2P overlay from which
you can bootstrap your independent IPOP system - we will refer to this
third VM as "Pam" in the rest of the tutorial.
 
Any of the options described in the \ `introductory IPOP
tutorial <http://manual.futuregrid.org/ipop1.html>`__ work
(FutureGrid, EC2, VMware) will work here, as long as the "Pam" VM can be
reached by both "Alice" and "Bob" through the Internet. In general,
"Pam" should be a machine deployed with a public IP interface (e.g. in
EC2 or FutureGrid). (If you run "Pam" on your own desktop using
VMware/VirtualBox, it is likely not to have a public IP interface - but
it should work for this tutorial, as long as Alice and Bob are also
deployed in the same computer).
 
Before you continue to the next step:

-  Deploy the Pam VM using the method of your choice
-  Log in to Pam and take notice of its IP address

   -  This can be found by using the "ifconfig" command and looking for
      the "eth0" interface.
   -  We will refer to this IP address as IP\_Pam in the remainder of
      this tutorial. 

Step 4: Configure Pam to run P2P Bootstrapping Overlay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


First, download a zip archive with template configuration files and
scripts prepared for this tutorial, *on Pam, as root*::
 
  wget http://www.acis.ufl.edu/~renato/ipopdemo/bootstrap/bootstrap\_demo.zip
  apt-get install unzip
  unzip bootstrap\_demo.zip
 
Now run the configuration script; you need to provide three
parameters: a P2P namespace string, the IP\_Pam address, and a port.

-  The P2P namespace is akin to the IPOP namespace of the previous
   tutorial, but it establishes a name that P2P nodes joining the same
   overlay agree on. For simplicity, you can use the same namespace you
   chose in the previous tutorial
-  The IP\_Pam address and port configure the network endpoint that
   other nodes (Alice and Bob) will use to join the P2P overlay. By
   default, we'll use port 40000 in this tutorial, but you are free to
   choose another number if you'd like. 

| Configure these parameters by running \ *on Pam, as root, and
replacing Namespace and IP\_Pam as appropriate*::

./bootstrap\_demo\_prepare.sh P2PNamespace IP\_Pam 40000

This creates a XML configuration file called "bootstrap.config". You
can take a look at this file and check where the information is stored;
it should look like this::
 
  <?xml version="1.0"?>
  <NodeConfig>
    <BrunetNamespace>P2PNamespace</BrunetNamespace>
    <EdgeListeners>
      <EdgeListener type="udp">
        <port>40000</port>
      </EdgeListener>
    </EdgeListeners>
    <RemoteTAs>
      <Transport>brunet.udp://IP\_Pam:40000</Transport>
    </RemoteTAs>
 
Brunet is the name of the P2P software "under the hood" of IPOP. This
configuration tells Brunet to listen on endpoint, IP\_Pam:40000, on
protocol UDP. It is possible to also configure the P2P overlay to use
TCP, but UDP is preferrable in most cases as it supports NAT traversal.
Other nodes (Alice, Bob), will be configured to contact these
endpoints. Now run the P2P bootstrapping code with this configuration,
as follows:

(Note: this command first installs mono, if it's not already
installed on the VM, which may take a few minutes to complete)::

./run\_bootstrap\_node.sh ./bootstrap.config


Step 5: Configure Alice and Bob to use Pam as P2P overlay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
Now you will change the configuration of IPOP on Alice and Bob to use
Pam instead of PlanetLab for bootstrapping. To do so, run the following
commands, *on Alice and Bob, as root:*
 
Download configuration files for this tutorial::

  mkdir tmp
  cd tmp
  wget http://www.acis.ufl.edu/~renato/ipopdemo/bootstrap/bootstrap\_demo.zip
  unzip bootstrap\_demo.zip
 
For the following command, ***make sure you use the same exact
parameters you configured for Pam***::

  ./bootstrap\_demo\_prepare.sh P2PNamespace IP\_Pam 40000
 
Place the configuration file where IPOP can find it::

  cp bootstrap.config /opt/ipop/etc/node.config
 
Start IPOP::
 
  /etc/init.d/groupvpn.sh start  

Step 6: Send messages between Alice and Bob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The Alice and Bob VMs are now configured with the same virtual IP
addresses as in the previous tutorial, and the same operations you have
done then (ping, IPsec, etc), should also work here - the main
difference being that your overlay is not confined to Alice, Bob, and
Pam, and is independent of PlanetLab.
 

Step 7: (Optional) Advanced topics
 
7.1) Inspecting the P2P network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
The previous steps show how you can create a separate overlay
network; from a user's perspective (Alice and Bob), it does not look
very different from the previous tutorial. If you are curious as to
whether the overlay is indeed connected through Pam, you can run the
following command::
 
  /opt/ipop/bin/crawl.py
 
This will "crawl" the P2P network node by node and dump statistics
about nodes and connections. You should see an output that looks like
this::
 
  Total Nodes: 18
  Consistent Nodes: 18
  Consistency: 1.0
  Connections: 296
  SecurityAssociations: 0
  WrappedEdges: 0
  Edges: 469
  RelayEdges: 15
  SubringEdges: 0
  TcpEdges: 54
  UdpEdges: 400
  Crawl took: 1.07016801834

There should be a total of 18 P2P nodes; 16 of the nodes are running
in a single VM (Pam) to create a small overlay-in-a-node, while the
remaining two nodes are Alice and Bob.
 
You can also check how the mapping between IPOP IP and P2P
identifiers mapping works by querying the DHT. On Alice, check what P2P
identifier it has been assigned by executing::
 
  grep node /opt/ipop/etc/node.config
 
You should get an output that looks like this::

  <NodeAddress>brunet:node:X33YDT5FA3GTBQ3Q5AJ3PNE3YQSRNRBQ</NodeAddress>

Alice's P2P identifier is a self-assigned randomly generated 160-bit
long integer encoded as a string (X33YDT5FA3GTBQ3Q5AJ3PNE3YQSRNRBQ). If
you check Bob, you will see its identifier is a different 160-bit
number.
 
If you query the DHT for the IPOP namespace you chose, and for
Alice's IP address, you will see that it maps to this P2P identifier.
Query the DHT with this command, replacing the IPOP namespace
appropriately::
 
  /opt/ipop/bin/bget.py dhcp:IPOPnamespace:192.168.10.10

And you will see it maps to Alice's P2P identifier. Substitute for
Bob's IPOP address and query the DHT again.

7.2) Adding fault tolerance by deploying multiple bootstrap nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, we only deployed one overlay bootstrapping VM - Pam.
In practice, this is not a very good idea, as Pam becomes a central
point of failure - if it crashes, the network loses connectivity. In
practice, IPOP bootstrap overlays span across multiple nodes; the
network is then resilient to failures of a fraction of the nodes. The
PlanetLab overlay used in the previous tutorial, for instance, runs
hundreds of nodes where it is not uncommon for dozes of nodes to
crash/reboot every day.
 
If you want to deploy a multi-node IPOP overlay, the overall approach
is to add to the bootstrap.config file of each bootstrapping node the
IP:port endpoints of all the other bootstrapping nodes, and use this
list of endpoints in the /opt/ipop/etc/node.config files of each node
that joins IPOP. 

***For more information***
 
If you run into problems that do not seem to go away, or are
interested in using IPOP and would like to learn more about advanced
configuration and deployment, please contact the IPOP team by joining
the ACIS P2P Users malining list at: acisp2p [at] googlegroups [dot]
com, or contact Renato Figueiredo at: renato [at] acis [dot] ufl [dot]
edu.

 

.. |image1| image:: /sites/default/files/images/nsf-logo.png
   :target: http://www.tacc.utexas.edu/
.. |image2| image:: /sites/default/files/u876/xsede-logo.png
