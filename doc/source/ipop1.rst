.. _s-ipop1:

**********************************************************************
IPOP (IP-over-P2P) 
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:


`IPOP (IP-over-P2P) <http://www.ipop-project.org>`__ is a
software-defined virtual network that can be used as a basis for
creating virtual private clusters across multiple cloud providers and
administrative domains. IPOP is architected as a peer-to-peer (P2P)
overlay for tunneling and routing of encapsulated IP packets that are
captured/injected into virtual network interfaces (v-NICs). The IPOP
software consists of P2P routers that run on endpoints that are
connected to the virtual network, such as virtual machines (VMs)
distributed across multiple cloud providers.

This tutorial provides step-by-step instructions for deploying a
demonstration IP-over-P2P (IPOP) virtual network among VMs that can be
deployed on different commercial and private clouds, as well as on your
own resources. These include FutureGrid Nimbus/OpenStack clouds, Amazon
EC2, as well as virtual machines that you can run on your own computer
using VMware or VirtualBox.


Prerequisites:
~~~~~~~~~~~~~~

-  Basic understanding of virtual networking and IPOP

   -  Refer to documentation on the `IPOP project's web
      site <http://www.ipop-project.org>`__; a good starting point is
      this open `online course "MOOC"
      module <https://fgmoocs.appspot.com/ipop>`__

-  Basic knowledge of Unix/Linux command line tools
-  If you plan to use a virtual machine on your desktop, you need
   `VMware <http://www.vmware.com>`__ or
   `VirtualBox <http://www.virtualbox.org>`__ installed on your computer
-  If you plan to use Amazon EC2, you need an `Amazon Web Services
   (AWS) <http://aws.amazon.com>`__ account 
-  Depending on whether you plan to use Nimbus, OpenStack, one of the
   following tutorials is required:

   -  `Using Nimbus
      on FutureGrid <https://portal.futuregrid.org/tutorials/nimbus>`__
   -  `Using OpenStack
      on FutureGrid <https://portal.futuregrid.org/tutorials/openstack>`__

 
^

Step 1: Deploying VMs to be connected by IPOP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step in this tutorial is to deploy at least two virtual
machines which will be connected by an IPOP virtual network. IPOP runs
inside VMs - the main requirement for IPOP to work is that the VMs are
connected to the Internet. The VM can either have a public address, or
have a private address that connects to the public Internet through a
Network Address Translator (NAT). You can, for instance deploy one VM on
your computer, and one VM on FutureGrid, and observe how they get
connected by the virtual network.

IPOP is currently packaged for Debian/Ubuntu Linux systems, so you
need to run a virtual machine based off these distributions. The
following steps describe how to run virtual machines on FutureGrid,
Amazon EC2, or your own desktop - select which approach you want to use
and follow the instructions below to deploy at least two virtual
machines.


Option 1: Deploying a VM on FutureGrid Using Nimbus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Nimbus image with Ubuntu 12.04 is available on TACC's cluster
(Alamo) with KVM virtualization technology. The image name is
"ubuntu12.04.x64.kvm" and it is available to all FutureGrid users. Use
the `Nimbus cloud-client.sh client <https://portal.futuregrid.org/tutorials/nimbus>`__ as
described in the Nimbus tutorial to deploy a virtual machine on Alamo::

  cloud-client.sh --conf conf/alamo.conf --run --name ubuntu12.04.x64.kvm --hours 24


Option 2: Deploying a VM on FutureGrid Using OpenStack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An OpenStack image with Ubuntu 12.04 is available on IU's cluster
(india). The image AMI ID is "ami-0000000d" and it is available to
all FutureGrid users. Use euca2ools as described in the OpenStack
tutorial to deploy a virtual machine on india::

   euca-run-instances -k keyname -n 1 ami-0000000d

Option 3: Deploying a VM on Amazon EC2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Amazon EC2 has a Ubuntu 12.04 image available (Ubuntu Server 12.04.2
LTS) with AMI ID ami-d0f89fb9 which has been tested and is known to work
with this tutorial; other recent Debian/Ubuntu AMIs should also work.
Follow instructions from Amazon EC2 to deploy instances of this virtual
machine. NOTE: This has been tested on an EC2 instance configured with a
Security Group that does not block UDP traffic - i.e. with a rule for
UDP::

    1 - 65535   0.0.0.0/0

Option 4: Deploying a VM on your computer (VMware, VirtualBox)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
While there are several possible Debian/Ubuntu images that you can use
for this tutorial, an image that has been tested and is known to work is
a `Debian Squeeze
appliance <http://www.trendsigma.net/vmware/debian6t.html>`__ that runs
on VMware.


Step 2: Establishing IPOP connectivity between two VMs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One you finish step 1 and have two VMs up and running, you will
install and deploy IPOP on the VMs to establish connectivity between
them over a virtual network.
 
To make the process simpler for the first time you use IPOP, this
tutorial uses configuration files with several pre-set values to
minimize configuration steps from your part. Once you finish the
tutorial and understand how IPOP can be deployed, you can use these
configuration files as templates to deploy other IPOP virtual networks.
 
We assume that you have deployed two VMs - we will be refer to them
as "Alice" and "Bob" in the rest of the tutorial. The "Alice" VM will be
configured with an IPOP virtual IP address 192.168.10.10, while the
"Bob" VM will be configured with an IPOP virtual IP address
192.168.10.20.

***2.1) Bring up IPOP in the "Alice" VM***  
First, you need to remote login (using ssh) into the first VM
instance you deployed - let's call it "Alice". To ssh into the VM using
ssh, follow the instructions based on the respective cloud/VM you are
using (Nimbus, OpenStack, EC2). Once you are logged to the VM, install
the tutorial files as follows (you can copy and paste the commands below
to avoid mistakes):

*(Note: you must perform these steps as the user "root". If you have
not ssh'ed into the machine as root, *\ *e.g. as the "ubuntu"
user", *\ *you need to first run "sudo bash" to become root; in the
Debian squeeze appliance, type "su" and enter "password" - without
quotes - when prompted)*::

  wget http://www.acis.ufl.edu/~renato/ipopdemo/ipop_demo_prepare_debian.zip 
  apt-get install unzip
  unzip ipop_demo_prepare_debian.zip

Now, on to configuring your virtual network node for this demo. To do
this, you need two pieces of information: the IPOP "namespace", which is
a string that uniquely identifies your virtual network in the P2P
system, and a virtual IP address. The script below helps configure these
parameters: you need to substitute CHANGE\_THIS by another string to
uniquely identify your IPOP network during this tutorial. For instance,
if you run this tutorial on May 21 2013, you could substitute
CHANGE\_THIS by a string such as
ipop\_tutorial\_05\_21\_2013\_your\_name. The second parameter is the
last byte of the virtual IP address - we will use "10" for Alice, so it
gets 192.168.10.10::

  ./ipop_demo_prepare.sh CHANGE_THIS 10

At the end of this process, you should be able to see a "tapipop"
virtual network interface configured with the 192.168.10.10 virtual IP
address. (**Note:** the tutorial files assume the private network
192.168.10.0/255.255.255.0 does not conflict with a network your VM is
attached to, which is typically the case. If needed, you can change the
base address/netmask by editing the respective in
ipop\_demo\_prepare.sh)

Type the following command to confirm::

  ifconfig tapipop

And you should see an output that looks like this::

  tapipop  Link encap:Ethernet HWaddr 96:44:a8:53:67:2a 
      inet addr:192.168.10.10 Bcast:192.168.255.255
  Mask:255.255.255.0
      UP BROADCAST RUNNING MULTICAST MTU:1200 Metric:1
      RX packets:525 errors:0 dropped:0 overruns:0 frame:0
      TX packets:277 errors:0 dropped:0 overruns:0 carrier:0
      collisions:0 txqueuelen:500
       RX bytes:56314 (56.3 KB) TX bytes:32314 (32.3 KB)

***2.2) Bring up IPOP in the "Bob" VM***
| 
Now using another terminal, ssh into the "Bob" VM and repeat the same
process you did for Alice (again, as root)::

   wget
  `http://www.acis.ufl.edu/~renato/ipopdemo/ipop\_demo\_prepare\_debian.zip <http://www.acis.ufl.edu/~renato/ipopdemo/ipop_demo_prepare_debian.zip>`__
  apt-get install unzip
  unzip ipop\_demo\_prepare\_debian.zip

To configure IPOP namespace and IP address in the Bob VM, substitute
CHANGE\_THIS **by the exact same string**you used when configuring
Alice, and set the IP address last byte to be "20", as follows. Be
careful when typing, because if the namespace strings do not exactly
match, your tutorial will not work correctly::

  ./ipop\_demo\_prepare.sh CHANGE\_THIS 20

At the end of this process, as in the Alice VM, you should be able to
also see a "tapipop" virtual network interface; in the Bob VM, it is
configured with the 192.168.10.20 virtual IP address.

***2.3) Get Alice and Bob connected***

We will now use the "ping" tool to send ICPM echo packets between
Alice and Bob over the IPOP virtual network. Ping is a helpful tool for
basic diagnostics of network connectivity, so we use it in this
demonstration; once you confirm that ICMP packets are flowing with ping,
you should be able to have any other TCP/IP traffic running over the
virtual network.

Login into Alice, and ping Bob, as follows::

  ping 192.168.10.20

(Or, vice versa, you can log in Bob and ping Alice:ping
192.168.10.10)

In the typical case, assuming you are not behind a symmetric NAT, you
should see the following pattern: First, a few ICMP ping packets being
dropped in the beginning, followed by a few packets that may have long
latencies (hundreds of miliseconds, see packet with icmp\_seq 6 below),
then packets with lower latency. The following snapshot shows an example
of the kind of output you should expect if you deploy your VMs in the
same data center (the latency may be shorter or longer in your case
depending on network conditions and NAT/firewall behavior)::

  PING 192.168.10.20 (192.168.10.20) 56(84) bytes of data.
  From 192.168.10.10 icmp\_seq=1 Destination Host Unreachable
  From 192.168.10.10 icmp\_seq=2 Destination Host Unreachable
  From 192.168.10.10 icmp\_seq=3 Destination Host Unreachable
  From 192.168.10.10 icmp\_seq=4 Destination Host Unreachable
  From 192.168.10.10 icmp\_seq=5 Destination Host Unreachable
  64 bytes from 192.168.10.20: icmp\_req=6 ttl=64 time=1008 ms
  64 bytes from 192.168.10.20: icmp\_req=7 ttl=64 time=8.46 ms
  64 bytes from 192.168.10.20: icmp\_req=8 ttl=64 time=1.87 ms
  64 bytes from 192.168.10.20: icmp\_req=9 ttl=64 time=1.87 ms
  64 bytes from 192.168.10.20: icmp\_req=10 ttl=64 time=1.64 ms

What is going on in this example? Your two virtual macihnes are
connected to a larger P2P overlay, with nodes distributed all over the
world - we use the PlanetLab system to host a "bootstrapping" IPOP
overlay.

Before Alice and Bob communicate with each other, they need to locate
each other's identifier in the P2P overlay. During the first few
seconds, Alice and Bob are part of the P2P overlay, but they have not
communicated before, so the first thing that needs to take place is a
lookup to map Namespace:virtualIP of each node to their respective IPOP
P2P identifier in the overlay. This lookup is performed as a Distributed
Hash Table (DHT) query in the P2P overlay, and until the query is
complete, packets will be dropped(ICMP packets 1-5 in the example
above).

Once the IP-P2P lookup is done, packets can flow between Alice and
Bob; however, initially they can take a long overlay path, going through
several intermediate nodes, because it is very unlikely that Alice and
Bob are P2P "neighbors" to begin with. In the example above, Alice and
Bob are in the same data center, but ICMP packet #6 takes about a second
of round trip time because it's routed over multiple P2P nodes. This
interaction triggers a process whereby Alice and Bob simultaneuously
attempt to create a direct connection between each other. Once it is
established, the round-trip time drops significantly (packets 7-10).


Step 3: Securing communications between Alice and Bob
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One you finish steps 1 and 2, you have two VMs up and running and
connected by the IPOP virtual network. Up to this point, however,
communication between Alice and Bob is not private. In this step, we
will configure IPsec to secure communications between Alice and Bob,
providing privacy, integrity, and authentication at the IP layer.

There are many options to configure IPsec - what is important to
notice is that IPsec is layered atop IPOP, and because of this layering
and separation of concerns, neither the IPsec software (in the Linux
kernel) nor IPOP need to be modified.

***3.1) Bring up IPsec in the "Alice" VM***

This step also uses configuration files with several pre-set values
to minimize configuration steps from your part. We use the "racoon"
software to configure IPsec, and the configuration is based on the use
of X.509 certificates. In this example, both Alice and Bob are
configured with certificates signed by the same certificate authority
(CA), and racoon is configured at each node to allow any VM with a valid
certificate signed by this trusted CA to communicate. Run the following
commands on Alice to setup IPsec/racoon (again, as root)::

  wget http://www.acis.ufl.edu/~renato/ipopdemo/ipop_ipsec_demo_prepare_debian.zip
  unzip ipop_ipsec_demo_prepare_debian.zip
  ./ipop_ipsec_demo_prepare.sh

The main configuration that takes place as part of this demo script
are as follows:

-  The CA's certificate (cacert.pem), as well as the certificate
   (host-cert.pem) and private key (host-key.pem) of each node, are
   placed in the /etc/racoon/certs directory
-  The racoon configuration file is placed in /etc/racoon/racoon.conf -
   it describes that x.509 certificates will be used to set up IPsec
   security associations, and configures other security policies
-  The IPsec configuration file is placed in /etc/ipsec-tools.conf - it
   establishes that all communications within the IPOP virtual network
   (192.168.10.0/24 by default in this demo) are subject to IPsec
   security.


***3.2) Bring up IPsec in the "Bob" VM***

Repeat the same steps, again, as root::

  wget http://www.acis.ufl.edu/~renato/ipopdemo/ipop_ipsec_demo_prepare_debian.zip
  unzip ipop_ipsec_demo_prepare_debian.zip
  ./ipop_ipsec_demo_prepare.sh

***3.3) Connecting Alice and Bob***

As done in the previous step, log in to Alice and ping Bob. On Alice::

  ping 192.168.10.20

You will notice a similar behavior to the previous step - ping
packets may drop in the beginning, then communication flows. Here, the
reason packets may drop is due to the negotiation of security keys done
by IPsec.

Alice and Bob continue to ping each other in the same manner now -
what is different is that all communication now is authenticated and
encrypted. For instance, if Alice stops running IPsec, or does not
produce a valid signed certificate when they negotiate keys, it will not
be able to connect to Bob (and vice-versa).

***3.4) Inspecting secure communications***

To confirm this, let's change the ping command slightly to add a
"payload" to the message, and inspect IP packets using the "tcpdump"
tool.

On Bob, run tcpdump to capture and show a count of ten packets
sent/received to/from Alice's IP in the tapipop interface::

  tcpdump -X -i tapipop -c 10 'ip host 192.168.10.10'

On Alice, send five ICMP packets to Bob, with the payload "deadbeef"
(a pattern that will make it easier to observe at the output of
tcpdump)::
  
   ping -p deadbeef -c 5 192.168.10.20
  
   On Bob, you should see tcpdump output that looks like this:
  
   11:41:55.084606 IP ip-192-168-10-10.ec2.internal > ip-192-168-10-20.ec2.internal:
   ESP(spi=0x03ae3438,seq=0x1c), length 100
   0x0000: 4500 0078 0000 4000 4032 a4e5 c0a8 0a0a E..x..@.@2......
   0x0010: c0a8 0a14 03ae 3438 0000 001c b7b9 013a  ......48.......:
   0x0020:  7f0d ff58 7968 2f35 7997 08d1 7a0f 8f00  ...Xyh/5y...z...
   0x0030:  f004 1721 f902 3545 7263 ca5f bd9c 0724  ...!..5Erc.\_...$
   0x0040:  d2cf df0e b097 470a 862e ac50 6c95 c755  ......G....Pl..U
   0x0050:  0ebb 0283 0633 4f98 0578 ec8f 6e09 aadf  .....3O..x..n...
   0x0060:  e120 4806 d914 7d2c 4ccc 643f 6269 8f92  ..H...},L.d?bi..
   0x0070:  f3df 4a70 cfde 80a6                      ..Jp....
  
The tcpdump output tells you that the packet is ESP, which stands for
Encapsulated Security Payload. Note that you don't see the "deadbeef"
pattern, as there is privacy in the communicaiton - nodes in the path
between Alice and Bob will not be able to see the payload of any IP
packet they communicate.
  
   ***3.5) Inspecting IPsec authentication***
  
   Now let's show how IPsec prevents non-authenticated nodes to
communicate. Disable IPsec by running the following commands, *on Bob,
as root*::
  
   /etc/init.d/racoon stop
   setkey -F
   setkey -FP
  
Then, try to ping Alice from Bob, or vice-versa. You will see that
packets do not flow now.
  
   ***3.6) Inspecting packets without IPsec***
  
  
Now let's show how, without IPsec, the payload is not kept private.
Disable IPsec, *on Alice, as root*::

  /etc/init.d/racoon stop
  setkey -F
  setkey -FP

*On Bob*, run tcpdump to capture and show a count of ten packets
sent/received to/from Alice's IP in the tapipop interface::

  tcpdump -X -i tapipop -c 10 'ip host 192.168.10.10'

*On Alice*, send five ICMP packets to Bob, with the payload
"deadbeef" (a pattern that will make it easier to observe at the output
of tcpdump)::

  ping -p deadbeef -c 5 192.168.10.20

On Bob, you should now see tcpdump output that looks like this:

  11:46:10.258390 IP ip-192-168-10-10.ec2.internal > ip-192-168-10-20.ec2.internal:
  ICMP echo request, id 6107, seq 5, length 64
  0x0000: 4500 0054 0000 4000 4001 a53a c0a8 0a0a E..T..@.@..:....
  0x0010: c0a8 0a14 0800 e859 17db 0005 825e 9b51 .......Y.....^.Q
  0x0020: 0000 0000 aeed 0300 0000 0000 dead beef ................
  0x0030: dead beef dead beef dead beef dead beef ................
  0x0040: dead beef dead beef dead beef dead beef ................
  0x0050: dead beef 

And you can discern the "deadbeef" pattern in the packet now that it
is no longer encrypted by IPsec.


Troubleshooting and for more information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you find connectivity problems when running this tutorial, you can
try restarting the IPOP process by running::

   /etc/init.d/groupvpn.sh stop
   /etc/init.d/groupvpn.sh start

And stopping IPsec::

   setkey -F
   setkey -FP
   /etc/init.d/racoon stop

If you run into problems that do not seem to go away, or are
interested in using IPOP and would like to learn more about advanced
configuration and deployment, please contact the IPOP team by joining
the ACIS P2P Users malining list at: acisp2p [at] googlegroups [dot]
com, or contact Renato Figueiredo at: renato [at] acis [dot] ufl [dot]
edu.


|image2|\ Futuregrid is a resource provider for
`XSEDE <https://www.xsede.org/>`__.

.. |Home| image:: /sites/all/themes/fgtheme/logo.png
   :target: /
.. |image1| image:: /sites/default/files/images/nsf-logo.png
   :target: http://www.tacc.utexas.edu/
.. |image2| image:: /sites/default/files/u876/xsede-logo.png
