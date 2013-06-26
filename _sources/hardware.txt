**********************************************************************
Hardware
**********************************************************************

.. todo:
   transfer tables to csv tables

.. todo:
   merge some of the tables

.. todo:
   fix section outline





These are the current resources available in FutureGrid. 

Compute Resources
--------------------------------------------------
.. csv-table:: 
   :header: Name                                                       , System Type           , # Nodes   , # CPUS   , # Cores   , TFLOPS   , RAM (GB   , Storage (TB)   , Site   

   `india <https://portal.futuregrid.org/hardware/india>`__       , IBM iDataplex             , 128           , 256          , 1024          , 11           , 3072          , 335                , IU         
   `hotel <https://portal.futuregrid.org/hardware/hotel>`__       , IBM iDataplex             , 84            , 168          , 672           , 7            , 2016          , 120                , UC         
   `sierra <https://portal.futuregrid.org/hardware/sierra>`__     , IBM iDataplex             , 84            , 168          , 672           , 7            , 2688          , 96                 , SDSC       
   `foxtrot <https://portal.futuregrid.org/hardware/foxtrot>`__   , IBM iDataplex             , 32            , 64           , 256           , 3            , 768           , 0                  , UF         
   `alamo <https://portal.futuregrid.org/hardware/alamo>`__       , Dell Poweredge            , 96            , 192          , 768           , 8            , 1152          , 30                 , TACC       
   `xray <https://portal.futuregrid.org/hardware/xray>`__         , Cray XT5m                 , 1             , 166          , 664           , 6            , 1328          , 5.4                , IU         
   `bravo <https://portal.futuregrid.org/hardware/bravo>`__       , HP Proliant               , 16            , 32           , 128           , 1.7          , 3072          , 128                , IU         
   `delta <https://portal.futuregrid.org/hardware/delta>`__       , GPU Cluster(SuperMicro)   , 16            , 32           , 192           ,              , 1333          , 144                , IU         
   `lima <https://portal.futuregrid.org/hardware/lima>`__         , Aeon Eclipse64            , 8             , 16           , 128           , 1.3          , 512           , 3.8 (SSD)          , SDSC       


Storage Resources
--------------------------------------------------

.. csv-table:: 
   :header:  System Type   , Capacity (TB)      , File System   , Site    

    DDN 9550          , 339 shared with IU +   , Luster            , IU        
    Data Capacitor   ,  16 TB dedicated       ,                   ,            
    DDN 6620          , 120                    , GPFS              , UC         
    SunFire x4540     , 96                     , ZFS               , SDSC       
    Dell MD3000       , 30                     , NFS               , TACC       
    IBM dx360 M3      , 24                     , NFS               , UF         

Status
------

The status of the resources can be monitored through:

-  `https://portal.futuregrid.org/status <https://portal.futuregrid.org/status>`__

This page also contains a link to our operational status of FutureGrid
resources and services, see the FutureGrid Inca server at:

-  `http://inca.futuregrid.org <http://inca.futuregrid.org/>`__

Maintenance
-----------

Activities during the regular maintenance window for FutureGrid machines
are listed in the FutureGrid wiki at:

-  `https://wiki.futuregrid.org/index.php/Hw:MaintActivities <https://wiki.futuregrid.org/index.php/Hw:MaintActivities>`__.

Scheduled outages and maintenance windows on the FutureGrid network are
collected in the Network Operations Calendar at:

-  `https://noc.futuregrid.org/futuregrid/support/operations-calendar3.html <https://noc.futuregrid.org/futuregrid/support/operations-calendar3.html>`__

Compute Resources
----------------------------------------------------------------------

GVL: This section belongs to HPC Services

Compute Hardware Resources & HPC Job Queue Information

.. csv-table:: 
   :header: Resource   , Queue name   , Default Wallclock Limit   , Max Wallclock Limit   , NOTES                 

    india      , batch        , 4 hours                   , 24 hours              ,                       
	       , long         , 8 hours                   , 168 hours             ,                       
	       , scalemp      , 8 hours                   , 168 hours             , restricted access     
	       , b534         , none                      , none                  , restricted access     
	       , ajyounge     , none                      , none                  , restricted access     
    sierra     , batch        , 4 hours                   , 24 hours              ,                       
	       , long         , 8 hours                   , 168 hours             ,                       
    hotel      , extended     , none                      , none                  ,                       
    alamo      , shortq       , none                      , 24 hours              ,                       
	       , longq        , none                      , 24 hours              ,                       
    foxtrot    , batch        , 1 hour                    , none                  , not for general use   

For availability, please visit:
`http://portal.futuregrid.org/status <http://portal.futuregrid.org/status>`__
.

GVL: This image belongs to the specific cluster desciption:

|image4|

IU iDataplex & Cray

GVL: This section belongs to the specific cluster description:

|image5|

IU Cray

GVL: This belongs to networking:

Compute Networks
======================================================================


**Resource Name**

**Network Devices**

IU Cray  

Cray 2D Torus SeaStar 

 

IU iDataPlex  

DDR IB  

QLogic switch with Mellanox ConnectX adapters

Blade Network Technologies & Force10 Ethernet switches

 

SDSC 

DDR IB 

Cisco switch with Mellanox ConnectX adapters

Juniper Ethernet switches

 

TACC 

QDR IB  

Mellanox switches and adapters

Dell Ethernet switches

 

UC 

DDR IB 

QLogic switch with Mellanox ConnectX adapters

Blade Network Technologies & Juniper switches

UF

Ethernet only (Blade Network Technologies & Force10 switches)

.. csv-table:: 
   :header:   Name , Alamo, Bravo, Delta, Foxtrot, Hotel, India, Sierra, xray

   Organization, Texas Advanced Computing Center, Indiana University, Indiana University, University of Florida, University of Chicago, Indiana University, San Diego Supercomputer Center, Indiana University
   Machine Type                           , Cluster                               , Cluster                               , Cluster                           , Cluster                               , Cluster                               , Cluster                                , Cluster                                                                       , Cluster                         
   System Type                            , Dell PowerEdge M610 Blade             , HP Proliant                           ,, IBM iDataPlex dx 360 M2               , IBM iDataPlex dx 360 M2               , IBM iDataPlex dx 360 M2                , IBM iDataPlex dx 340                                                          , Cray XT5m                       
   CPU type                               , Intel Xeon X5550                      , Intel Xeon E5620                      , Intel Xeon 5660                   , Intel Xeon X5520                      , Intel Xeon X5550                      , Intel Xeon X5550                       , Intel Xeon L5420                                                              , AMD Opteron 2378                
   Host Name                              , alamo                                 , bravo                                 , delta                             , foxtrot                               , hotel                                 , india                                  , sierra                                                                        , xray                            
   CPU Speed                              , 2.66GHz                               , 2.40GHz                               , 2.80 GHz                          , 2.26GHz                               , 2.66GHz                               , 2.66GHz                                , 2.5GHz                                                                        , 2.4GHz                          
   Number of CPUs                         ,192,32,32,64,168,256,168,168
   Number of nodes                        ,96,16,16,32,84,128,84,1
   RAM                                    , 12 GB DDR3 1333Mhz                    , 192 GB DDR3 1333Mhz                   , 192 GB DDR3 1333 Mhz               , 24 GB DDR3 1333Mhz                    , 24 GB DDR3 1333Mhz                    , 24 GB DDR3 1333Mhz                     , 32 GB DDR2-667                                                                , 8 GB DDR2-800                   
   Total RAM (GB)                         ,1152,3072,3072,768,2016,3072,2688,1344
   Number of cores                        ,768,128,,256,672,1024,672,672
   Operating System                       , Linux                                 , Linux                                 ,Linux, Linux                                 , Linux                                 , Linux                                  , Linux                                                                         , Linux                           
   Tflops                                 ,8,1.7,,3,7,11,7,6
   Disk Size (TB)                         ,48,,15,20,120,335,72,335
   Hard Drives                            , 500 GB Internal 7200 RPM SAS Drive    , 6x2TB Internal 7200 RPM SATA Drive    , Seagate Constellation 7.2 K RPM     64 MB Cache SATA 92GB   , 500 GB Internal 7200 RPM SATA Drive   , 1 TB Internal 7200 RPM SATA Drive     , 3000 GB Internal 7200 RPM SATA Drive   , 160 GB Internal 7200 RPM SATA Drive                                           , 6 TB Internal Lustre Storage    
   Primary storage shared by all nodes  , NFS                                   , NFS                                   ,NFS, NFS                                  , GPFS                                  ,  NFS                                   , ZFS filesystem with 76.8 TB raid2 storage and 5.4 TB of raid0 (for scratch)   , NFS                             
   Storage details                        ,,, RAID 9260-4i 1pt SAS2  512 MB SGL  ,,,,,
   Connection configuration               , Mellanox 4x QDR InfiniBand adapters   , Mellanox 4x DDR InfiniBand adapters   ,,, Mellanox 4x DDR InfiniBand adapters   , Mellanox 4x DDR InfiniBand adapters    , Mellanox 4x DDR InfiniBand adapters                                           , Cray SeaStar Interconnect       
   Primary storage shared by all nodes   ,,,92 ????,,,,,
   CPUs (cores) per node                  ,,,2,,,,,
   Cores per CPU,,,6,,,,,
   Total number of GPU cores,,,192,,,,,
   GPU type                               ,,, nVIDIA Tesla C2070                ,,,,,
   Cores per GPU,,,448,,,,,
   GPUs per node,,,2,,,,,
   Batch system                           ,,, Torque                            ,,,,, 


 

Network
=======

The FutureGrid network provides for connectivity among FutureGrid
participants, and network access to the Network Impairments Device
(NID).  Five participants connect through a variety of network providers
(see Figure 1).
 

|image6|
*Figure 1:  Diagram of FutureGrid Network*
 
FutureGrid partners with XSEDE to allow participants of each to
utilize the resources of both networks. Through interconnects at the
Indiana Gigapop, Internet2 and NLR extend access to FutureGrid resources
to researchers nationally.
 
FutureGrid deployed a Juniper EX8208 at the Core in Chicago’s
StarLight facility.
 
|image7|
 
*Figure 2: Juniper EX8208*
 

The Juniper EX series provides for Layer2 and Layer3 connectivity. 
FutureGrid uses the EX to fulfill the network services (i.e.,
interconnectivity and external connectivity). The EX provides a special
feature labeled ‘firewall based forwarding’, allowing seamless
integration with network impairments.

 
GlobalNOC at Indiana University provides network engineering
services, and the Operations Center provides email and phone support
24x7. GlobalNOC resources for public wan information can be found at
`http://noc.futuregrid.org/ <http://noc.futuregrid.org/>`__. Available
tools include:

-  **`FutureGrid
   Atlas <http://noc.futuregrid.org/futuregrid/live-network-status/maps--graphs/futuregrid-atlas.html>`__:** View
   the current level of FutureGrid Network traffic as displayed on a
   geographical map.
-  **`FutureGrid SNAPP Traffic
   Graphs <http://noc.futuregrid.org/futuregrid/live-network-status/traffic-statistics/futuregrid-snapp-trafic-graphs2.html>`__:** View
   high-speed traffic graphs collected at one-minute samples using the
   Indiana University-developed SNAPP tool. Create custom views of the
   FutureGrid network and view historic utilization with greater data
   resolution.
-  **`FutureGrid NOC Router
   Proxy <http://noc.futuregrid.org/futuregrid/live-network-status/traffic-statistics/router-proxy3.html>`__:**
   Submit show commands to the FutureGrid router.

-  **`FutureGrid Physical
   Map <http://noc.futuregrid.org/futuregrid/maps--documentation/maps.html#FutureGrid%20Physical%20Map>`__**

-  **`FutureGrid Topology
   Map <http://noc.futuregrid.org/futuregrid/maps--documentation/maps.html#FutureGrid%20Topology%20Map>`__**

As IPv6 test beds are not available at all FutureGrid partner sites,
early implementation of iPv6 would slow important software development
work. As a result, current plans call for FutureGrid to continue using
IPv4. Any change in plans will be noted here.
 
Below is further information about networking:
 
FutureGrid Core: Juniper EX8200
India; Force10, C-150
Bravo, Delta, Echo; Force10, S60
Sierra: Juniper EX4200
Hotel: EX4200
Dlamo: Dell PowerConnect 6000 Series
Xray: Force10, C-150
foxtrot:
internal network switch: IBM/BLADE Rack Switch G8000
public network switch: Force10 S50
Node NICs: built-in (IBM iDataPlex DX360 M2) dual Intel 82575EB
Gigabit Network Connection
10Gbps: Myricom Myri-10G Dual-Protocol NIC (available on login node)
Alamo: Dell PowerConnett 6224
 
Juniper, EX series
- `https://www.juniper.net/us/en/products-services/switching/ex-series/Force10 <https://www.juniper.net/us/en/products-services/switching/ex-series/Force10>`__ (now
Dell),
 
C Series and S Series:

-  `http://www.dell.com/us/enterprise/p/force10-c150/pd <http://www.dell.com/us/enterprise/p/force10-c150/pd>`__ 
-  `http://www.dell.com/us/enterprise/p/force10-s60/pd <http://www.dell.com/us/enterprise/p/force10-s60/pd>`__

Dell, PowerConnect
- `http://www.dell.com/us/enterprise/p/switch-powerconnect <http://www.dell.com/us/enterprise/p/switch-powerconnect>`__
IBM (formerly BNT)
- `http://www-03.ibm.com/systems/networking/switches/rack.html <http://www-03.ibm.com/systems/networking/switches/rack.html>`__
 
 
|image8|
|image9|
 

FutureGrid Network Impairments Device (NID)
===========================================

**FutureGrid Network Impairments Device (NID)**
 
Researchers on FutureGrid may perodically employ the use of a Spirent
XGEM, a Network Impairments Emulator.  The XGEM allows users to
accurately create the delays and impairments that occur over live
production networks for validating and evaluating new products and
technologies.  The XGEM supports a variety of impairments with the most
common being delay, packet loss, jitter and re-ordering.
 
|image10|
*Figure 1: Spirent XGEM*
 
The XGEM contains two blades, each with a 10GE interface.  Traffic
received on one blade is automatically transmitted on the other blade,
and vice-versa.  This allows the XGEM to be deployed as a pass-through
device.  Impairments are applied unidirectionally.  An identical or
different impairment can be applied in either direction, or
simultaneously in both directions.
 
FutureGrid also utilizes a Juniper EX8208 as the primary network
element between all of the FutureGrid participants.  Juniper’s EX
platform contains firewall-based forwarding, which allows us to insert
the XGEM between FutureGrid participants with only software changes (see
Figure 2).
 
|image11|
*Figure 2.  Diagram of FutureGrid Network.*
 
The firewall-based forwarding feature can be configured to forward
traffic unidirectionally or bidirectionally through the XGEM using a
single IP address or any size subnet.  Only traffic defined by the
Juniper EX8208 will be impaired, leaving all other traffic between
FutureGrid participants unaffected.
 
This implementation requires traffic to traverse the FutureGrid Core
in order to be impaired.  Additional configuration might be required at
the participants' individual sites for impairments to occur locally.
 

Storage
=======

Clustername(site)

Mountpoint\ ````

Size

Type

Backups

Use

Notes

`Sierra <https://portal.futuregrid.org/kb/document/bbns>`__\ (UCSD/SDSC)

/N/u/username

40.6TB

ZFS (RAID2)

Yes (nightly incremental)

Home dir

By default, quotas on home directories are 50 GB and quotas on scratch
directories are 100 GB.

/N/scratch/username

5.44TB

ZFS (RAID0)

No

Scratch

/N/soft

50GB

ZFS (RAID2)

Yes (nightly incremental)

Software installs

/N/images

6TB

ZFS (RAID2)

Yes (nightly incremental)

VM images

`India (IU) <https://portal.futuregrid.org/kb/document/bbms>`__

/N/u/username

15TB

NFS (RAID5)

Yes (nightly incremental)

Home dir

At the moment, we do not have any quota implemented on India and we use
the local/tmp (77 GB) as scratch space.

/share/project

14TB

NFS (RAID5)

Yes (nightly incremental)

Shared/group folders

/tmp

77GB

local disk

No

Scratch

`Bravo <https://portal.futuregrid.org/kb/document/bcao>`__ (IU)

/N/u/username

15TB

NFS (RAID5)

Yes (nightly incremental)

Home dir

The same NFS shares in India are mounted in Bravo (users do not log in
here; jobs are submitted through India). There are two local partitions,
which are used for HDFS and swift tests.

/share/project

14TB

NFS (RAID5)

Yes (nightly incremental)

Shared/group folders

`Delta <https://portal.futuregrid.org/kb/document/bcaj>`__ (IU)

/N/u/username

15TB

NFS (RAID5)

Yes (nightly incremental)

Home dir

Same as Bravo. The NFS shares are mounted for user and group share
(users do not log in directly here; jobs are submitted through India).

/share/project

14TB

NFS (RAID5)

Yes (nightly incremental)

Shared/group folders

Hotel (UC)

/gpfs/home

15TB

GPFS (RAID6)

No

Home dir

By default, quotas on home directories are 10 GB.

/gpfs/scratch

57TB

GPFS (RAID6)

No

Scratch

/gpfs/software

7.1GB

GPFS (RAID6)

No

Software installs

/gpfs/images

7.1TB

GPFS (RAID6)

No

VM images

/scratch/local

862GB

ext3 (local disk)

No

Local scratch

Foxtrot (UFL)

/N/u/username

16TiB

NFS (RAID5)

No

Home dir

At the moment, we do not have any quota implemented on Foxtrot.

Using HPSS from FutureGrid
==========================

**Note**: FutureGrid does not provide an HPSS server. The HSI is used to
access IU's HPSS service from INDIA. This is available only for IU
faculty, staff, and students.

Through the `SDA <http://rc.uits.iu.edu/storage/sda>`__ (formerly known
as MDSS) service, IU provides distributed storage service to faculty,
staff, and graduate students. The
`HSI <http://rc.uits.iu.edu/storage/hsi>`__ (Hierarchical Storage
Interface) client is available in INDIA. To use the HSI client:

-  First, activate your SDA account. Detailed instructions are available
   at IU's `MDSS Service Starter
   Kit <http://rc.uits.iu.edu/storage/mdss-starter-kit>`__ page.
-  Then, from INDIA, load the HSI module as follows:

::

    $ module load hsi
    hsi version 3.5.3 loaded

-  Connect to the SDA:

::

    $ hsi -A combo
    Principal: your_iu_userid                                
    [youriuid]Password:                                
    Username: your_iu_userid  UID: 1122636  Acct: 1122636(1122636) Copies: 1 Firewall: off [hsi.3.5.3 Fri Nov 20 10:01:25 EST 2009]
    ?

**Note:**\ Your Principal is your IU Network ID, and your password is
the IU passphrase.

-  Enable firewall mode; otherwise, you will receive this error:

   ::

       put: Error -5 on transfer

::

    ? firewall -on
    A: firewall mode set ON, I/O mode set to extended (parallel=off), autoscheduling currently set to OFF

-  List local folder:

::

     ? lls
    testfile.txt

-  List the current directory in HPSS:

::

    ? pwd
    pwd0: /hpss/pathtoyouriuusername

-  For transferring files (*put* and *get*), search the `IU Knowledge
   Base <http://kb.iu.edu/?search=hsi>`__.

Status
======

System Status
~~~~~~~~~~~~~

    Please note that the information on this page is not 100% accurate
    as it is maintained by hand. However, dynamic monitoring tools are
    available and can be consulted for more details.

     

Ongoing outages
~~~~~~~~~~~~~~~

    The **first Tuesday of each month** is the standard maintenance
    window.

    -  `Edit </admin/build/views/edit/active_outage_list?destination=book%2Fexport%2Fhtml%2F104#views-tab-default>`__
    -  `Export </admin/build/views/export/active_outage_list>`__
    -  `Clone </admin/build/views/clone/active_outage_list>`__

    +-----------+-------------------+-----------------------------------------------------------------------------------+--------------------+-------------------------------+------------------------------+--------------+---------------------------------------------------------------------+
    | Status    | Type              | Title                                                                             | Impacted Systems   | Start of Outage               | Anticipated End of Outage    | Resolution   | Edit link                                                           |
    +===========+===================+===================================================================================+====================+===============================+==============================+==============+=====================================================================+
    | Ongoing   | Software System   | `Bravo is reserved in 6 weeks </outages/130514/bravo-reserved-6-weeks>`__         | other              | Tue, 14 May 2013, 17:00 EDT   |                              |              | `edit </node/2513/edit?destination=book%2Fexport%2Fhtml%2F104>`__   |
    +-----------+-------------------+-----------------------------------------------------------------------------------+--------------------+-------------------------------+------------------------------+--------------+---------------------------------------------------------------------+
    | Planned   | Software System   | `Eucalyptus GUI not available </outages/120901/eucalyptus-gui-not-available>`__   | india              | Sat, 01 Sep 2012 (All day)    | Fri, 05 Oct 2012 (All day)   |              | `edit </node/2226/edit?destination=book%2Fexport%2Fhtml%2F104>`__   |
    +-----------+-------------------+-----------------------------------------------------------------------------------+--------------------+-------------------------------+------------------------------+--------------+---------------------------------------------------------------------+

You can find a list of previous outages `here </outages_all>`__
including an `RSS </feeds/fg_outages_all_rss.xml>`__ feed.

 
~

System configuration
~~~~~~~~~~~~~~~~~~~~

    The system is configured at this time using either HPC, Nimbus, or
    Eucalyptus services. The distribution used at this time can be
    found \ `here <http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp>`__ and `here <http://inca.futuregrid.org:8080/inca/jsp/status.jsp?suiteNames=Info&xsl=info.xsl>`__.

    |image12|

Status of FutureGrid services
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Lists the status of keyFutureGrid services (e.g., SSH, Nimbus,
    Eucalyptus) in a sortable table.

    |image13|

Cluster Monitoring
~~~~~~~~~~~~~~~~~~

Ganglia:
 
    |image14|

     

Network Status
~~~~~~~~~~~~~~

    The network status can be viewed via the \ `FutureGrid Network
    Operations Center page <http://noc.futuregrid.org>`__.  Upcoming
    network events are maintained on the \ `Network Operations
    Calendar <http://noc.futuregrid.org/futuregrid/support/operations-calendar3.html>`__.

    |image15|

Software Status
~~~~~~~~~~~~~~~

    The operational status of FutureGrid machines are continuously
    monitored via a number of tools. To view some of the contents,
    please
    visit \ `http://inca.futuregrid.org <http://inca.futuregrid.org>`__

     

    |image16|

Cloud Status
~~~~~~~~~~~~

`Here <https://portal.futuregrid.org/monitoring/cloud>`__ you will find
information about how FG cloud services are currently used.

    |image17|

     

FutureGrid Cloud Metrics
~~~~~~~~~~~~~~~~~~~~~~~~

    | Metric system provides an integrated accounting service to view
    cloud usage statistics and graphs regarding the utilization of
    virtual machine (VM) instances.
    |image18|

System software version info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    | The version info of the installed system software across
    all FG sites:
    |image19|

Nimbus Usage Reports
~~~~~~~~~~~~~~~~~~~~

`Displays <http://inca.futuregrid.org/nimbus-stats>`__ weekly usage
graphs of each of the FutureGrid Nimbus deployments.

    |image20|

.. |image4| image:: https://portal.futuregrid.org/sites/default/files/resize/images/FutureGrid_iDataPlex_Cray_IU-sm-640x425.jpg
.. |image5| image:: https://portal.futuregrid.org/sites/default/files/resize/images/Cray_XT5m_Front_closed-small-427x640.jpg
.. |image6| image:: https://portal.futuregrid.org/sites/default/files/images/FutureGrid%20Logocal%20v3.png
.. |image7| image:: https://portal.futuregrid.org/sites/default/files/resize/images/Juniper%20EX8208-140x184.png
.. |image8| image:: https://portal.futuregrid.org/sites/default/files/u23/futuregrid-physical.png
.. |image9| image:: https://portal.futuregrid.org/sites/default/files/u23/futuregrid-topology.png
.. |image10| image:: https://portal.futuregrid.org/sites/default/files/images/Spirent%20XGEM.png
.. |image11| image:: https://portal.futuregrid.org/sites/default/files/images/FutureGrid%20Logocal%20v3.png
.. |image12| image:: https://portal.futuregrid.org/sites/default/files/images/status_incapart.PNG
   :target: http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp
.. |image13| image:: https://portal.futuregrid.org/sites/default/files/ScreenSnapz.jpg
   :target: http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid
.. |image14| image:: https://portal.futuregrid.org/sites/default/files/ganglia.png
   :target: http://ganglia.futuregrid.org
.. |image15| image:: https://portal.futuregrid.org/sites/default/files/images/large_status_nocmap.PNG
   :target: http://noc.futuregrid.org
.. |image16| image:: https://portal.futuregrid.org/sites/default/files/u23/Screen%20shot%202011-01-14%20at%207.48.06%20PM.png
   :target: http://inca.futuregrid.org
.. |image17| image:: https://portal.futuregrid.org/sites/default/files/u23/Screen%20shot%202011-04-07%20at%203.23.05%20PM.png
   :target: https://portal.futuregrid.org/monitoring/cloud
.. |image18| image:: https://portal.futuregrid.org/sites/default/files/screenshot-for-status-small.png
   :target: https://portal.futuregrid.org/metrics
.. |image19| image:: https://portal.futuregrid.org/sites/default/files/fg-sys-sw-ver.PNG
   :target: http://inca.futuregrid.org:8080/inca/HTML/rest/HPC/FutureGrid
.. |image20| image:: https://portal.futuregrid.org/sites/default/files/u15/nimbus-usage.png
   :target: http://inca.futuregrid.org/nimbus-stats
