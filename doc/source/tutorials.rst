**********************************************************************
Tutorials
**********************************************************************
.. todo::

   hello, Gregor!

If you're looking for the Cloud Summer School 2012 (along with
excellent tutorial material), click on the icon below:




`.. image:: images/summerschool2012.png Science Cloud Summer School 2012 <https://portal.futuregrid.org/projects/241>`_

The following tutorials are broadly organized into topics, with each
tutorial classified by the user's target level of expertise with
FutureGrid (novice, intermediate, advanced). (If you are a tutorial
developer, for instructions on how to add a tutorial to this list,
please \ :portal:`refer to the TEOS
page <outreach>`).

If you have corrections or suggestions related to our tutorial
content, please :portal:`fill out a help
request <help>`.


Tutorial Topic 0: Accessing FutureGrid Resources
------------------------------------------------

-  Accessing FutureGrid Resources:

   - See our manual page in Section :ref:`s-accounts`. [novice]

Tutorial Topic 1: Cloud Provisioning Platforms
----------------------------------------------

-  Using OpenStack on FutureGrid. 

   - Havana: See the Section :ref:`s-openstack-havana` in the manual. [novice] 
   - Grizzly: See the Section :ref:`s-openstack-grizzly` in the manual. [novice] 

-  Using Nimbus on FutureGrid. 

   - See the manual Section :ref:`nimbus`. [novice]
   - An external page is available to `create a cluster with Nimbus
     <http://www.nimbusproject.org/docs/current/clouds/clusters.html>`_
     This link will leave the FG manual. [intermediate]

-  Using Eucalyptus on FutureGrid.

   - :ref:`Using Eucalyptus on FutureGrid <s-eucalyptus>` [novice]

-  Using Vine on FutureGrid.

   - GVL: THIS SECTION IS VERY CONFUSING WHY IS THIS NOT IN ITS OWN
     SECTION FOR EXAMPPLE "NETWORK PROVISIONING"? ALSO THE SECTIONS
     ARE NOT FOLLOWING STANDARD SECTION CONVENTIONS.

   - :ref:`Connecting private network VMs across Nimbus clusters using ViNe <_s_vine>` [novice]
   - :ref:`IPOP1: (IP-over-P2P) Virtual Network Introductory Tutorial <s-vine-overlay>` [novice]
   - TODO :portal:`IPOP1: IP-overP2P <tutorials/ipop1>` [intermediate] 
     
     - See the section in the manual: :ref:`s-ipop1`.

   - TODO :portal:`IPOP2: Deploying your Own P2P Overlay for IPOP
     VPNs <tutorials/ipop2>` [intermediate] 

     - See the section in the manual: :ref:`s-ipop2`

Tutorial Topic 2: Cloud Run-time Map/Reduce Platforms
-----------------------------------------------------

-  :portal:`Running Hadoop as a batch job using
   MyHadoop <tutorials/running-hadoop-batch-job-using-myhadoop>` [novice]
-  :portal:`Running SalsaHadoop (one-click Hadoop) on HPC
   environment <salsahadoop-futuregrid-hpc>` [beginner]
-  :portal:`Running Twister on HPC
   environment <twister-futuregrid-hpc>` [beginner]
-  :portal:`Running SalsaHadoop on
   Eucalyptus <salsahadoop-futuregrid-cloud-eucalyptus>` [intermediate]
-  :portal:`Running <tutorials/eucalyptus-and-twister-futuregrid>`\ :portal:`FG-Twister
   on
   Eucalyptus <tutorials/eucalyptus-and-twister-futuregrid>` [intermediate]
-  :portal:`Running One-click Hadoop WordCount on
   Eucalyptus <tutorials/one-click-hadoop-wordcount-eucalyptus-futuregrid>`
   [beginner]
-  :portal:`Running One-click Twister K-means on
   Eucalyptus <tutorials/one-click-twister-k-means-eucalyptus-futuregrid>`
   [beginner]

Tutorial Topic 3: Grid Appliances for Training, Education, and Outreach
-----------------------------------------------------------------------

-  :portal:`Running a Grid Appliance on your
   desktop <tutorials/ga1>`  [novice]
-  :portal:`Running a Grid Appliance on
   FutureGrid <http://portal.futuregrid.org/tutorials/ga9>` [novice]
-  `Running an OpenStack virtual appliance on
   FutureGrid <http://portal.futuregrid.org/tutorials/os1>`__ [novice]
-  `Running Condor tasks on the Grid
   Appliance <http://portal.futuregrid.org/tutorials/ga8>`__ [novice]
-  :portal:`Running MPI tasks on the Grid
   Appliance <tutorials/mp1>` [novice]
-  `Running Hadoop tasks on the Grid
   Appliance <http://portal.futuregrid.org/tutorials/ga10>`__ [novice]
-  :portal:`Deploying virtual private Grid Appliance clusters using
   Nimbus <tutorials/ga4>`
   [intermediate]
-  :portal:`Building an educational appliance from Ubuntu
   10.04 <tutorials/ga3>` [intermediate]
-  :portal:`Customizing and registering Grid Appliance images using
   Eucalyptus <tutorials/ga7>`
   [intermediate]

Tutorial Topic 4: High Performance Computing
--------------------------------------------

-  `Basic High Performance Computing </tutorials/hpc>`__ [novice]
-  `Running Hadoop as a batch job using
   MyHadoop </tutorials/running-hadoop-batch-job-using-myhadoop>`__
   [novice]
-  `Performance Analysis with Vampir </manual/performance/vampir>`__
   [advanced]
-  `Instrumentation and tracing with
   VampirTrace </manual/vampir/trace>`__ [advanced]

Tutorial Topic 5: Experiment Management
---------------------------------------

-  :portal:`Running interactive
   experiments <tutorials/interactive-experiment-management>`
   [novice]
-  :portal:`Running workflow experiments using
   Pegasus <tutorials/workflow-experiment-management>` [novice]
-  :portal:`Pegasus 4.1 on FutureGrid
   Tutorial <tutorials/pegasus-on-futuregrid-tutorial>` [novice]

Tutorial Topic 6: Image Management and Rain
-------------------------------------------

-  `Using Image Management and
   Rain <http://futuregrid.github.com/rain/quickstart.html>`__ [novice]
-  :portal:`Easy steps to generate and register an
   Image <generate-and-register-os-image-futuregrid-using-fg-shell>`
   [novice]
-  :portal:`Manual Image
   Customization <manually-customize-image>`
   [advanced]
-  :portal:`Register your VirtualBox image in
   OpenStack <register-virtual-box-image-openstack>`
   [intermediate]

Tutorial Topic 7:  Storage
--------------------------

-  :portal:`Using HPSS from
   FutureGrid <tutorials/hpss>` [novice]

Other Tutorials and Educational Materials
-----------------------------------------

-  :portal:`Additional tutorials on FutureGrid-related
   technologies <additional_tutorials>`
-  :portal:`FutureGrid community educational
   materials <community_edu_materials>`
-  `CI Tutor performance
   tutorials <http://www.citutor.org/browse.php?access=&category=-1&search=performance&include=all&filter=Filter>`__
   (requires brief registration to view content)



FutureGrid Grid Appliance for Nimbus and Eucalyptus
===================================================

Summary:
  This tutorial provides step-by-step instructions on how to install
  clients to access Eucalyptus and Nimbus clouds on FutureGrid using the
  Grid appliance.

Pre-requisites:
  `FutureGrid tutorial GA1 - Introduction to the Grid Appliance <http://portal.futuregrid.org/tutorials/ga1>`__

Hands-on tutorial:
  This tutorial is maintained at the Grid Appliance portal. See `FutureGrid:clientappliance <http://www.grid-appliance.org/wiki/index.php/FutureGrid:clientappliance>`__.

One-click Hadoop WordCount on Eucalyptus FutureGrid
===================================================

Introduction
~~~~~~~~~~~~~~~

This tutorial shows how to run a one-click Hadoop WordCount job on the
Eucalyptus platform of FutureGrid.


Prerequisite
~~~~~~~~~~~~~~~~

1. FutureGrid HPC account: please apply via \ `FutureGrid
portal <../../user/register>`__ and \ `request a HPC
account <../../request-hpc-account>`__.
2. FutureGrid Eucalyptus account: please see `FutureGrid Eucalyptus
Tutorial <../../tutorials/eucalyptus3>`__ for detailed instructions.
3. FutureGrid Eucalyptus credentials zip file
(euca2-[username]-x509.zip) stored under user's home directory
4. Key pair created and added for use with Eucalyptus virtual
machines

The following sections assume a user has created both an HPC account
and a Eucalpytus account under the username of *gaoxm*.


Login to india.futuregrid.org
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ ssh -i .ssh/id\_rsa\_fg
    india.futuregrid.org                      
    Enter passphrase for key '.ssh/id\_rsa\_fg':
    Last login: Sat May  5 02:17:33 2012 from
    c-71-194-153-252.hsd1.in.comcast.net
    ...
    torque/2.5.5 version 2.5.5 loaded
    moab version 5.4.0 loaded
    euca2ools version 1.2 loaded
    $ cd eucalyptus/
    $ ls
    cloud-cert.pem                 euca2-gaoxm-d108375b-pk.pem 
    eucarc         hosts        nodes
    euca2-gaoxm-d108375b-cert.pem  euca2-gaoxm-x509.zip        
    gaoxm.private  jssecacerts  tmp.out


Download and unzip the “hadoopOneClick.zip” package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ wget
    `http://mypage.iu.edu/~gao4/data/hadoopOneClick.zip <http://mypage.iu.edu/~gao4/data/hadoopOneClick.zip>`__
    ...
    $ ls
    hadoopOneClick.zip
    $ unzip hadoopOneClick.zip


Run hadoop-one-click.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    $ cd hadoopOneClick
    [gaoxm@i136 hadoopOneClick]$ ls
    deploy-hadoop.sh     instanceIds.txt  publicIps.txt           
    stop-hadoop.sh
    hadoop-one-click.sh  ipHosts.txt      run-hadoop-wordcount.sh 
    terminate-instances.sh
    hosts                nodes.txt        start-instances.sh
    [gaoxm@i136 hadoopOneClick]$ chmod +x \*.sh
    [gaoxm@i136 hadoopOneClick]$ ./hadoop-one-click.sh -n 2 -t m1.small
    -i emi-D778156D -k gaoxm -p ~/eucalyptus/gaoxm.private -l
    `http://mypage.iu.edu/~gao4/data/grexp10.txt <http://mypage.iu.edu/~gao4/data/grexp10.txt>`__
    -s
    http://salsahpc.indiana.edu/tutorial/apps/hadoop-0.20.203.0-for-EucaVm.tar.gz

This will run a MapReduce word-count job on a dynamically created
virtual Hadoop cluster on FutureGrid. The user needs to replace the *–k*
and *–p* parameter values with his/her key-pair name and private key
path. For detailed usage information, try::

    $ ./hadoop-one-click.sh -h


Verify output
~~~~~~~~~~~~~~~~~

::

    $ ls outputs_logs  part-r-00000 _SUCCESS
    $ vim outputs/part-r-00000


Extensions
~~~~~~~~~~~~~~~

To run other MapReduce jobs, replace *run-hadoop-wordcount.sh* with
new scripts, and change *hadoop-one-click.sh* to call the corresponding
scripts.


One-click Twister K-means on Eucalyptus FutureGrid
==================================================

Introduction
~~~~~~~~~~~~~~~

This tutorial shows how to run a one-click Twister K-means job on the
Eucalyptus platform of FutureGrid.


Prerequisite
~~~~~~~~~~~~~~~~

#. FutureGrid HPC account, please apply via \ :portal:`FutureGrid
   portal <user/register>` and :portal:`request a
   HPC account <request-hpc-account>`.
#. FutureGrid Eucalyptus account, please see \ :portal:`FutureGrid Eucalyptus
   Tutorial <tutorials/eucalyptus>` for
   detailed instructions.
#. FutureGrid Eucalyptus credentials zip file
   (euca2-[username]-x509.zip) stored under user's home directory.
#. Key pair created and added for use with Eucalyptus virtual
   machines.

The following sections assume a user has created both HPC account and
Eucalpytus account under the username of “gaoxm”.


Login to india.futuregrid.org
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ ssh -i .ssh/id\_rsa\_fg
    india.futuregrid.org                      
    Enter passphrase for key '.ssh/id\_rsa\_fg':
    Last login: Sat May  5 02:17:33 2012 from
    c-71-194-153-252.hsd1.in.comcast.net
    ...
    torque/2.5.5 version 2.5.5 loaded
    moab version 5.4.0 loaded
    euca2ools version 1.2 loaded
    $ cd eucalyptus/
    $ ls
    cloud-cert.pem                 euca2-gaoxm-d108375b-pk.pem 
    eucarc         hosts        nodes
    euca2-gaoxm-d108375b-cert.pem  euca2-gaoxm-x509.zip        
    gaoxm.private  jssecacerts  tmp.out


Download and unzip the “twisterOneClick.zip” package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ wget http://mypage.iu.edu/~gao4/data/twisterOneClick.zip 
    ...
    $ ls
    hadoopOneClick  hadoopOneClick.zip  twisterOneClick.zip
    $ unzip twisterOneClick.zip


Run twister-one-click.sh
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ cd twisterOneClick
    $ ls
    deploy-twister.sh  instanceIds.txt  publicIps.txt         
    stop-twister.sh
    hostnames.txt      ipHosts.txt      run-twister-kmeans.sh 
    terminate-instances.sh
    hosts              nodes.txt        start-instances.sh    
    twister-one-click.sh
    $ chmod +x \*.sh
    $ ./twister-one-click.sh -n 2 -t m1.small
    -i emi-D778156D -k gaoxm -p ~/eucalyptus/gaoxm.private
    -l http://salsahpc.indiana.edu/tutorial/apps/Twister-0.9.tar.gz -a
    http://www.iterativemapreduce.org/apache-activemq-5.4.2-bin.tar.gz

This will run a MapReduce K-means job on a dynamically created
virtual Twister cluster on  FutureGrid. The user needs to replace the
“–k” and “–p” parameter values with his/her key-pair name and private
key path. For detailed usage information, try::

    $ ./twister-one-click.sh -h


Verify results in the standard output of the scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    Calling run\_kmeans.sh on 149.165.159.140...
    JobID: kmeans-map-reduce9ec9eaa2-9731-11e1-80d7-156f25bd362a
    May 6, 2012 4:11:57 AM
    org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected
    to \ `tcp://master:61616 <https://master:61616/>`__
    0    [main] INFO  cgl.imr.client.TwisterDriver  - Configure Mappers
    through the partition file, please wait....
    1975 [main] INFO  cgl.imr.client.TwisterDriver  - Configuring Mappers
    through the partition file is completed.
    250.77056136584878 , 125.15021341387315 , 249.21561041359857 ,
    246.74715176402833 , 375.350251646343 , 249.17570173022511 ,
    Total Time for kemeans : 6.808
    Total loop count : 15
    6260 [main] INFO  cgl.imr.client.TwisterDriver  - MapReduce
    computation termintated gracefully.
    ------------------------------------------------------
    Kmeans clustering took 6.841 seconds.
    ------------------------------------------------------


Extensions
~~~~~~~~~~~~~~~

To run other iterative MapReduce jobs, replace run-twister-kmeans.sh
with new scripts, and change twister-one-click.sh to call the
corresponding scripts.



Virtual Appliances
==================

Virtual appliances are virtual machine images encapsulating
pre-installed, pre-configured software that can be easily deployed on
cloud resources. Users of FutureGrid can use public appliance images
posted by other users, as well as contribute to the repository of
images.

This page provides a summary of community-provided virtual appliances
that are available for use on FutureGrid. If you have created a virtual
appliance and you would like to advertise its availability and features
with the community, feel free to edit this page and include information
about your appliance.

Creating Your Own Appliance:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any FutureGrid user with Eucalyptus or Nimbus accounts can create and
register an appliance. The approach is similar in both cases: you can
upload an existing image into FutureGrid (e.g. from another Eucalyptus
or Nimbus cloud, or an image you create on your own computer), or you
can customize an instance interactively in FutureGrid and save it in a
FutureGrid resource.


Nimbus:
^^^^^^^^^^^^^

You can upload a "common" image so it becomes available to others in a
FutureGrid cloud resource - to do this, add the flag --common to the
cloud\_client.sh command line when you transfer an image (ensure you are
using cloud client version 020 or above).  You can also save a Nimbus
instance that you are using interactively (through ssh) as an image.
Please refer to the `manual for
cloud\_client.sh <http://www.nimbusproject.org/docs/current/clouds/cloudquickstart.html>`__ and
the  `Nimbus tutorial <http://portal.futuregrid.org/tutorials/nimbus>`__
for instructions.


Eucalyptus: 
^^^^^^^^^^^^^^^^^^

Please refer to :portal:`FutureGrid tutorial
GA7 <tutorials/ga7>`.

.. todo:: errors in portal page reported, seems not to work

Reusing an Existing Appliance:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are several appliances already available on FutureGrid. The table
below summarizes a list of appliances, where they are available, and
their image names. If you have an appliance that you would like to add
to this list, please add it to the table.

Editing tips for the table:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  *You can add rows to the table by right-clicking the last row of the
   table and selecting Row->Insert Row After*
-  *If you make a mistake (e.g., deleting a row), you can undo it by
   pressing CTRL-Z*
-  *You need to click on the Submit button so your changes take effect*
-  *You can :portal:`create a community
   page <node/add/page-community>`
   explaining your appliance and its usage in more depth, and can link
   to it from this page*

.. todo:: no portal names bt real names 

.. list-table::

    * - Appliance name 
      - Appliance description                                                                       
      - FutureGrid system(s) available   
      - Appliance ID                                          
      - Installed                  
    * - :portal:`Grid Appliance <tutorials/ga9>`                              
      - Self-configures Condor/MPI/Hadoop virtual clusters for training/education                       
      - alamo, india                         
      - grid-appliance-2.05.03.gz (alamo), emi-E4ED1880 (india)   
      - panoat                       
    * - :portal:`OpenStack Appliance <tutorials/os1>`                         
      - Deploys a single-node OpenStack compute virtual cloud                                           
      - alamo                                
      - openstack-ubuntu-10.10-amd64.img                          
      - menghan                      
    * - :portal:`ViNe Appliance <contrib/simple-vine-tutorial>`               
      - Deploys the ViNe virtual network overlay to connect
	private-address VMs in sierra and foxtrot   
      - sierra, foxtrot                      
      - centos-5.5-x64-vine.gz                                    
      - menghan                      
    * - :portal:`Twister Appliance <contrib/fg-twister-appliance-tutorial>`   
      - Deploys a virtual private cluster running the Twister iterative
	MapReduce system                
      - india                                
      - emi-F0B8194D                                              
      - jemitche                     





