.. _s-workflow-experiment-management:

**********************************************************************
Workflow Experiment Management
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

Overview
--------

Experiment Management is the general set of capabilities provided by
FutureGrid so that users can easily execute distributed experiments. The
primary capabilities are planning an experiment, executing the
distributed tasks that make up an experiment, and monitoring and
recording the effects of these tasks. Experiment management is layered
atop other services such as resource provisioning (allocation and
configuration of resources), remote execution, file transfer, and
monitoring.

The workflow-based experiment management approach allows users to
pre-plan their experiment in detail as a workflow and then to execute
the experiment workflow in a batch manner. This approach is most suited
to situations such as when an experiment needs to be run a number of
times, when a set of experiments that are variations need to be run, or
when a user wants to take advantage of the additional compute resources
that are typically available during non-work hours.

Example Experiment 1
--------------------

The first example is a simple web server load test, and the second
example is running workflows on different sized Condor pools. The
experiments are Pegasus workflows which decide when to provision,
deprovision, and run experiment tasks. For experiments with a time axis.
the workflows are pretty simple Â because the provision and deprovision
steps are most commonly set up as barriers which can only be passed if a
certain number of resources are provisioned. A simple experiment would
be:

#. Request N resource from the cloud provider. Wait until the N
   resources are up and ready.
#. Run experiment task
#. Request deprovisioning of the resources. Wait until all the resources
   have been deprovisioned.

In the two examples below we are using a single provisioning tool called
nimbus-provisioner.py. This tool takes two arguments, a lower bound and
an upper bound for the number of necessary resources:

::

    Usage: nimbus-provisioner.py [options]
    Options:
    -h, --help show this help message and exit
    --loglevel=LOG_LEVEL Log level.
    Â  Valid levels are: debug,info,warning,error,
    Â  Default is info.
    -i IMAGE_NAME, --image-name=IMAGE_NAME
    Â  The name of the Nimbus image to provision
    -l MIN_INSTANCES, --min=MIN_INSTANCES
    Â  The minimum number of instances to have before exiting
    -u MAX_INSTANCES, --max=MAX_INSTANCES
    Â  The maximum number of instances to have before exiting

nimbus-provisioner.py will query the Nimbus instance to see what number
of resources are already provisioned. If the number of resources are
below the lower bound, more resources will be requested. If the number
of resources are above the upper bound, resources will be terminated
until the upper bound has been met. Once the number of resources are
within the bounds, the tool will exit, making it a tool which is easy to
use as a barrier. However, nimbus-provisioner.py is not yet very
generic: it does not make a distinction between resources provisioned
with the tool and resources provisioned using other methods.

nimbus-provisioner.py uses the AWS REST interface to Nimbus, and is
based on code examples from `SC11 Nimbus
tutorial <http://www.nimbusproject.org/docs/sc11/>`__.

The web server load test experiment is set up to test the performance of
a web server. The server is regular web server, with Ganglia to collect
the performance data. Clients are virtual machines running on the
FutureGrid, each VM running 10 threads of continuousÂ wgets against the
web server. The experiment was run with 1, 5 and 10 virtual machines,
resulting in the web server being tested with 10, 50, and 100 clients
accessing it simultaneously. All the clients were accessing the same
static file on the web server. The experiment workflow was:

#. Provision 1 client
#. Collect data for 15 minutes
#. Increase the provisioned clients to 5
#. Collect data for 15 minutes
#. Increase the provisioned clients to 10
#. Collect data for 15 minutes
#. Deprovision all clients

Visually:

|Web Server Workflow|

The Pegasus workflow was a little bit more complex once staging and
other auxiliary jobs were added, but we expect most of the experiment
workflows to be pretty simple as they are bound by the time axis of the
experiment. The workflow DAX generator and scripts can be found in
the \ `web-server-work-load-20120227.tar.gz <https://confluence.pegasus.isi.edu/download/attachments/16318513/web-server-work-load-20120227.tar.gz?version=1&modificationDate=1330356553000>`__ file.
Top level is a run-experiment script which generates a new workflow and
submits it to the local Condor instance. Under tooling/, there are three
scripts:

-  experiment-dax-generator.py - Creates a DAX for the experiment
-  nimbus-provisioner.py - As described above
-  stats - Script which is run during the collect stats states. In
   current form, it queries a Ganglia server for the bandwidth graphs.

The output is a set of stored graphs from Ganglia showing the bandwidth
used by the web server. Other statistics can be collected by adding to
the stats script.

+-----------------------------------------------------------------------------------------------+------------+
| Attachment                                                                                    | Size       |
+===============================================================================================+============+
| `web-server-wf.jpg <https://portal.futuregrid.org/sites/default/files/web-server-wf.jpg>`__   | 19.28 KB   |
+-----------------------------------------------------------------------------------------------+------------+

