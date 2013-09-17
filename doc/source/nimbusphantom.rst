**********************************************************************
Nimbus Phantom
**********************************************************************

Nimbus Phantom is a hosted service, running on FutureGrid, that makes
it easy to leverage on-demand resources provided by infrastructure
clouds. Phantom allows the user to deploy a set of virtual machines over
multiple private, community, and commercial clouds and then
automatically grows or shrinks this set based on policies defined by the
user. This elastic set of virtual machines can then be used to implement
scalable and highly available services. An example of such service is a
caching service that stands up more workers on more resources as the
number of requests to the service increases. Another example is a
scheduler that grows its set of resources as demand grows.
 
Currently Phantom works with all FutureGrid Nimbus and OpenStack
clouds as well as Amazon and the XSEDE wispy cloud (the only XSEDE cloud
for now). A user can access it via two types of clients: an easy to use
web application and a scripting client. The scripting client is the boto
autoscale client as Phantom currently implements Amazon Autscaling API –
so you can think of it as Amazon Autoscale for FutureGrid clouds that
also allows for cloudburst to XSEDE and commercial clouds and is easy to
extend with your own policies and sensors.
 
The simplest scenario for using Phantom is as a gateway for deploying
and monitoring groups of virtual machines spread over multiple
FutureGrid clouds. In a more complex scenario you can use it to
cloudburst from FutureGrid clouds to Amazon. Finally, you can use it to
explore policies that will automate cloudbursting and VM allocations
between multiple clouds.
 
For more information and/or to use the service go to
`www.nimbusproject.org/phantom <http://www.nimbusproject.org/phantom>`__.
It should take no more than 10-15 minutes to start your own VMs.

-  `Phantom web
   interface <https://phantom.nimbusproject.org/accounts/login/?next=/>`__
-  `Phantom
   publication <http://www.nimbusproject.org/files/keahey_wcs_ocs_2012.pdf>`__

