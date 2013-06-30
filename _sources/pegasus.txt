Pegasus (Matts)
===========================

`Pegasus WMS <http://pegasus.isi.edu>`__ is a configurable system for
mapping and executing abstract application workflows over a wide range
of execution environments including a laptop, a campus cluster, a Grid,
or a commercial or academic cloud. One Pegasus workflow can run on a
single system or across a heterogeneous set of resources. Pegasus can
run workflows ranging from just a few computational tasks up to 1
million.

Pegasus has a number of features that contribute to its usability and
effectiveness, as explained in detail in the tutorial and the `Pegasus
online
documentation <https://pegasus.isi.edu/wms/docs/4.0/about.php#overview>`__.
Among the key feature rank abstract workflow portability between
environments, features to better control workflow performance and
resource utilization, scalability, data provenance tracking, data
management, error recovery and multiple operating environments not
limited to clouds.

The main mode of operation of Pegasus on FutureGrid is the usage of IaaS
clouds, as provided by Nimbus, OpenStack, Eucalyptus and bare-metal
(future).

If you want to find out more about Pegasus WMS, please `visit our web
site. <http://pegasus.isi.edu>`__ The liaison for FutureGrid is Jens
Vöckler. He is available as "Expert" on the Portal. If you have general
questions concerning Pegasus, not related to FutureGrid, you may want to
contact

pegasus-support <pegasus-support at isi dot edu>

The Pegasus Run-Time Cloud Architecture
---------------------------------------

Pegasus uses the `Condor high-throughput scheduling
system <http://research.cs.wisc.edu/condor/>`__ to provide the work of
executing a plan created by Pegasus from the abstract workflow
description.

.. figure:: images/fg-pwms-prefio.3.png
   :scale: 70%
   :align: right

   Figure: Cloud Site Layouts example


The figure above shows two cloud sites, typically two distinct IaaS
clouds, with two virtual machines (VMs) running in each site. 
Effectively, it shows a sample layout for sky computing (as in: multiple
clouds) as supported by Pegasus. At this point, it is up to the user to
provision the remote resources with a proper VM image that includes a
Condor *startd* and proper Condor configuration to report back to a
Condor *collector* that the Condor *schedd* has access to.

The submit host is the point where a user submits Pegasus workflows for
execution. In this discussion, the *submit host* (SH) is located
logically external to the cloud provider(s) in order to bridge multiple
clouds. In contrast, the tutorial uses a submit host that is located
within a single cloud site. The site where the SH is located typically
runs a Condor *collector* to gather resource announcements, or is part
of a larger Condor pool that collects these announcement. Condor makes
the remote resources available to the submit host's Condor installation.

The figure above shows the way Pegasus WMS is deployed in cloud
computing resources, ignoring how these resources were provisioned. The
provisioning request shows multiple resources per provisioning request.

The provisioning broker -- Nimbus, Eucalyptus or EC2 -- is responsible
to allocate and set up the resources. Please note that each provisioning
broker comes with its own set of client tools that may be executed
either on your laptop or desktop in front of you, or from a FutureGrid
login node. The FutureGrid tutorials for the various IaaS services have
details on their client tools and usage.

For a multi-node request, the worker nodes often require access to a
form of shared data storage. Concretely, either a POSIX-compliant shared
file system (e.g. NFS, PVFS) is available to the nodes, or can be
brought up for the lifetime of the application workflow. The task steps
of the application workflow facilitate shared file systems to exchange
intermediary results between tasks on the same cloud site. Pegasus also
supports an S3 data mode for the application workflow data staging. As
of Pegasus 4.0, it more easily supports non-shared file system execution
where each worker node uses only its own storage.

The initial stage-in and final stage-out of application data into and
out of the node set is part of any Pegasus-planned workflow. Several
configuration options exist in Pegasus to deal with the dynamics of push
and pull of data, and when to stage data. In many use-cases, some form
of external access to or from the shared file system that is visible to
the application workflow is required to facilitate successful data
staging. However, Pegasus is prepared to deal with a set of boundary
cases.

The data server in the figure is shown at the submit host. This is *not
a strict requirement*. The data server for consumed data (input data)
and data products (output data) may both be different and external to
the submit host.

Once worker nodes (resources) begin appearing in the pool managed by the
submit host's Condor *collector*, the application workflow, as planned
by Pegasus, can be submitted to Condor. A Condor *DAGMan* will manage
the application workflow execution. Pegasus run-time tools obtain
timing-, performance and provenance information as the application
workflow is executed. In the cloud and FutureGrid scenario, it is the
user's responsibility to de-provision the allocated resources.

In the figure, the cloud resources on the right side are assumed to have
uninhibited outside connectivity. This enables the Condor I/O to
communicate directly with the resources. The right side includes a setup
where the worker nodes use all private IP, but have out-going
connectivity and a NAT router to talk to the internet. The *Condor
connection broker* (CCB) facilitates this setup almost effortlessly.

The left side shows a more difficult setup where the connectivity is
fully firewalled without any connectivity except to in-site nodes. In
this case, a proxy server process, the *generic connection broker*
(GCB), needs to be set up in the de-militarized zone (DMZ) of the cloud
site's firewall to facilitate Condor I/O between the submit host and
worker nodes.

If the cloud supports data storage servers, Pegasus 4.0 is starting to
support workflows that require staging in two steps: Consumed data is
first staged to a data server in the remote site's DMZ, and then a
second staging task moves the data from the data server to the worker
node where the job runs. For staging out, data needs to be first staged
from the job's worker node to the site's data server, and possibly from
there to another data server external to the site. Pegasus is capable to
plan both steps: Normal staging to a remote site's data server, and the
worker-node staging from and to the site's data server as part of the
job. We are working on expanding the current code to support a more
generic set in the newly released Pegasus 4.0.

Using Pegasus on FutureGrid
---------------------------

The Pegasus tutorial for FutureGrid is forthcoming shortly. You are
welcome to `review the "Using Pegasus In FutureGrid"
tutorial <http://pegasus.isi.edu/futuregrid/tutorials/>`__ which makes
use of one of the following Virtual Machines:

+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| **IaaS**     | **Resource**   | **Image Name**                               | **CentOS**   | **PWMS**   | **Condor**   | **Globus**   | **Mntge**   |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Nimbus       | alamo          | pegasus-tutorial.x64.kvm.gz                  | 5.7          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Nimbus       | hotel          | pegasus-tutorial.x64.gz                      | 5.7          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Nimbus       | foxtrot        | pegasus-tutorial.x64.gz                      | 5.7          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Nimbus       | sierra         | pegasus-tutorial.x64.gz                      | 5.7          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Eucalyptus   | sierra         | tutorial/pegasus-tutorial.x64.manifest.xml   | 5.8          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| Eucalyptus   | india          | pegasus/pegasus-tutorial.x64.manifest.xml    | 5.8          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+
| OpenStack    | india          | pegasus/pegasus-tutorial.x64.manifest.xml    | 5.8          | 4.0.0      | 7.6.6        | 5.2.0        | 3.3p2       |
+--------------+----------------+----------------------------------------------+--------------+------------+--------------+--------------+-------------+

The table above shows the available Pegasus Virtual Machines you can use
to try out Pegasus. At this point, the Nimbus-based VMs are are
preferred.
