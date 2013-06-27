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

   india      , IBM iDataplex             , 128           , 256          , 1024          , 11           , 3072          , 335                , IU         
   hotel      , IBM iDataplex             , 84            , 168          , 672           , 7            , 2016          , 120                , UC         
   sierra    , IBM iDataplex             , 84            , 168          , 672           , 7            , 2688          , 96                 , SDSC       
   foxtrot   ,IBM iDataplex             , 32            , 64           , 256           , 3            , 768           , 0                  , UF         
   alamo      , Dell Poweredge            , 96            , 192          , 768           , 8            , 1152          , 30                 , TACC       
   xray        , Cray XT5m                 , 1             , 166          , 664           , 6            , 1328          , 5.4                , IU         
   bravo      , HP Proliant               , 16            , 32           , 128           , 1.7          , 3072          , 128                , IU         
   delta      , GPU Cluster(SuperMicro)   , 16            , 32           , 192           ,              , 1333          , 144                , IU         
   lima         , Aeon Eclipse64            , 8             , 16           , 128           , 1.3          , 512           , 3.8 (SSD)          , SDSC       


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


GVL: This belongs to networking:

Compute Networks
======================================================================

.. csv-table::
   :header: Resource Name, Network Devices
   
   IU Cray, Cray 2D Torus SeaStar 
   IU iDataPlex , DDR IB , QLogic switch with Mellanox ConnectX adapters,Blade Network Technologies & Force10 Ethernet switches
   SDSC, DDR IB, Cisco switch with Mellanox ConnectX adapters, Juniper Ethernet switches
   TACC, QDR IB , Mellanox switches and adapters, Dell Ethernet switches
   UC, DDR IB, QLogic switch with Mellanox ConnectX adapters, Blade Network Technologies & Juniper switches
   UF, Ethernet only (Blade Network Technologies & Force10 switches)

.. csv-table:: 
   :header:   Name , Alamo, Bravo, Delta, Foxtrot, Hotel, India, Sierra, xray

   Image,a,b,d,f,h,|image-india-cray|,s,|image-cray|
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

-  `FutureGrid
   Atlas <http://noc.futuregrid.org/futuregrid/live-network-status/maps--graphs/futuregrid-atlas.html>`__: View
   the current level of FutureGrid Network traffic as displayed on a
   geographical map.
-  `FutureGrid SNAPP Traffic
   Graphs <http://noc.futuregrid.org/futuregrid/live-network-status/traffic-statistics/futuregrid-snapp-trafic-graphs2.html>`__: View
   high-speed traffic graphs collected at one-minute samples using the
   Indiana University-developed SNAPP tool. Create custom views of the
   FutureGrid network and view historic utilization with greater data
   resolution.
-  `FutureGrid NOC Router
   Proxy <http://noc.futuregrid.org/futuregrid/live-network-status/traffic-statistics/router-proxy3.html>`__:
   Submit show commands to the FutureGrid router.

-  `FutureGrid Physical
   Map <http://noc.futuregrid.org/futuregrid/maps--documentation/maps.html#FutureGrid%20Physical%20Map>`__

-  `FutureGrid Topology
   Map <http://noc.futuregrid.org/futuregrid/maps--documentation/maps.html#FutureGrid%20Topology%20Map>`__

As IPv6 test beds are not available at all FutureGrid partner sites,
early implementation of iPv6 would slow important software development
work. As a result, current plans call for FutureGrid to continue using
IPv4. Any change in plans will be noted here.
 
Below is further information about networking:

.. csv-table::
 
   FutureGrid Core, Juniper EX8200
   India, Force10 C-150
   Bravo, Force10 S60
   Delta, Force10 S60
   Echo, Force10 S60
   Sierra, Juniper EX4200
   Hotel, Juniper EX4200
   Alamo, Dell PowerConnect 6000 Series
   Xray, Force10, C-150
   foxtrot, internal network switch: IBM/BLADE Rack Switch G8000
              , public network switch: Force10 S50
   Node NICs, built-in (IBM iDataPlex DX360 M2) dual Intel 82575EB Gigabit Network Connection
   10Gbps, Myricom Myri-10G Dual-Protocol NIC (available on login node)
   Alamo, Dell PowerConnett 6224
 
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

FutureGrid Network Impairments Device (NID)
 
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

.. csv-table::

    Clustername (site),    Mountpoint,    Size,    Type,    Backups,    Use,    Notes,
    Sierra (UCSD/SDSC),    /N/u/*username*,    40.6TB,    ZFS  (RAID2),    Yes  (nightly incremental),    Home dir,    By default quotas on home directories are 50 GB and quotas on scratch directories are 100 GB.,
    Sierra (UCSD/SDSC),    /N/scratch/*username*,    5.44TB,    ZFS  (RAID0),    No,    Scratch,  
    Sierra (UCSD/SDSC),    /N/soft,    50GB,    ZFS  (RAID2),    Yes  (nightly incremental),    Software installs,  
    Sierra (UCSD/SDSC),    /N/images,    6TB,    ZFS  (RAID2),    Yes  (nightly incremental),    VM images,  
    India  (IU),    /N/u/*username*,    15TB,    NFS  (RAID5),    Yes  (nightly incremental),    Home dir,    At the moment we do not have any quota implemented on India and we use the local/tmp  (77 GB) as scratch space.,
    India  (IU),    /share/project,    14TB,    NFS  (RAID5),    Yes  (nightly incremental),    Shared/group folders,  
    India  (IU),    /tmp,    77GB,    local disk,    No,    Scratch,  
    Bravo  (IU),    /N/u/*username*,    15TB,    NFS  (RAID5),    Yes  (nightly incremental),    Home dir,    The same NFS shares in India are mounted in Bravo   (users do not log in here; jobs are submitted through India). There  are two local partitions which are used for HDFS and swift tests.,
    Bravo  (IU),    /share/project,    14TB,    NFS  (RAID5),    Yes  (nightly incremental),    Shared/group folders,  
    Delta  (IU),    /N/u/*username*,    15TB,    NFS  (RAID5),    Yes  (nightly incremental),    Home dir,    Same as Bravo. The NFS shares are mounted for user and group share (users do not log in directly here; jobs are submitted through India).,
    Delta (IU),    /share/project,    14TB,    NFS (RAID5),    Yes (nightly incremental),    Shared/group folders,  
    Hotel (UC),    /gpfs/home,    15TB,    GPFS (RAID6),    No,    Home dir,    By default quotas on home directories are 10 GB.,
    Hotel (UC),    /gpfs/scratch,    57TB,    GPFS (RAID6),    No,    Scratch,  
    Hotel (UC),    /gpfs/software,    7.1GB,    GPFS (RAID6),    No,    Software installs,  
    Hotel (UC),    /gpfs/images,    7.1TB,    GPFS (RAID6),    No,    VM images,  
    Hotel (UC),    /scratch/local,    862GB,    ext3 (local disk),    No,    Local scratch,  
    Foxtrot (UFL),    /N/u/*username*,    16TiB,    NFS (RAID5),    No,    Home dir,    At the moment we do not have any quota implemented on Foxtrot.,



Using HPSS from FutureGrid
==========================

Note: FutureGrid does not provide an HPSS server. The HSI is used to
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

Note:\ Your Principal is your IU Network ID, and your password is
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

System Status:
    Please note that the information on this page is not 100% accurate
    as it is maintained by hand. However, dynamic monitoring tools are
    available and can be consulted for more details.

Ongoing outages:
    The **first Tuesday of each month** is the standard maintenance
    window.
    .. todo:
       move this to operations

.. todo::
   fix the links
  
You can find a list of previous outages `here </outages_all>`__
including an `RSS </feeds/fg_outages_all_rss.xml>`__ feed.

.. list-table:: System Information
   :header-rows: 1
   :widths: 20,10,70

   * - Image
     - Info
     - Description
   * - |image12| 
     - System configuration
     - The system is configured at this time using either HPC, Nimbus,
         or Eucalyptus services. The distribution used at this time can be
         found \ `here <http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp>`__ and `here <http://inca.futuregrid.org:8080/inca/jsp/status.jsp?suiteNames=Info&xsl=info.xsl>`__.
   * - |image13| 
     - Status of FutureGrid services
     - Lists the status of keyFutureGrid services (e.g., SSH, Nimbus,
       Eucalyptus) in a sortable table.
   * - |image14| 
     - Ganglia
     - Cluster Monitoring  
       crunchy, now would it?
   * - |image15|
     - Network Status:
     - The network status can be viewed via the \ `FutureGrid Network
       Operations Center page <http://noc.futuregrid.org>`__.
       Upcoming network events are maintained on the \ `Network Operations
       Calendar <http://noc.futuregrid.org/futuregrid/support/operations-calendar3.html>`__.
   * - |image16|
     - Software Status
     - The operational status of FutureGrid machines are continuously
       monitored via a number of tools. To view some of the contents,
       please visit \ `http://inca.futuregrid.org <http://inca.futuregrid.org>`__
   * - |image17|
     - Cloud Status:
     - `Here <https://portal.futuregrid.org/monitoring/cloud>`__ you will find
        information about how FG cloud services are currently used.
   * - |image18|
     - FutureGrid Cloud Metrics:
     - Metric system provides an integrated accounting service to view
       cloud usage statistics and graphs regarding the utilization of
       virtual machine (VM) instances.
   * - |image19|
     - System software version info:
     - The version info of the installed system software across
       all FG sites:
   * - |image20|
     - Nimbus Usage Reports:
     - `Displays <http://inca.futuregrid.org/nimbus-stats>`__ weekly usage
        graphs of each of the FutureGrid Nimbus deployments.



.. |image-india-cray| image:: https://portal.futuregrid.org/sites/default/files/resize/images/FutureGrid_iDataPlex_Cray_IU-sm-640x425.jpg
   :width: 100px
   :height: 100px

.. |image-cray| image:: https://portal.futuregrid.org/sites/default/files/resize/images/Cray_XT5m_Front_closed-small-427x640.jpg
   :width: 100px
   :height: 100px

.. |image6| image::  https://portal.futuregrid.org/sites/default/files/images/FutureGrid%20Logocal%20v3.png
   :height: 300px
   :width: 400px

.. |image7| image:: https://portal.futuregrid.org/sites/default/files/resize/images/Juniper%20EX8208-140x184.png
   :width: 100px
   :height: 100px

.. |image8| image:: https://portal.futuregrid.org/sites/default/files/u23/futuregrid-physical.png
   :width: 300px
   :height: 200px

.. |image9| image:: https://portal.futuregrid.org/sites/default/files/u23/futuregrid-topology.png
   :width: 300px
   :height: 200px

.. |image10| image:: https://portal.futuregrid.org/sites/default/files/images/Spirent%20XGEM.png
   :width: 100px
   :height: 100px

.. |image11| image:: https://portal.futuregrid.org/sites/default/files/images/FutureGrid%20Logocal%20v3.png
   :width: 100px
   :height: 100px

.. |image12| image:: https://portal.futuregrid.org/sites/default/files/images/status_incapart.PNG
   :target: http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp
   :width: 100px
   :height: 100px

.. |image13| image:: https://portal.futuregrid.org/sites/default/files/ScreenSnapz.jpg
   :target: http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid
   :width: 100px
   :height: 100px

.. |image14| image:: https://portal.futuregrid.org/sites/default/files/ganglia.png
   :target: http://ganglia.futuregrid.org
   :width: 100px
   :height: 100px

.. |image15| image:: https://portal.futuregrid.org/sites/default/files/images/large_status_nocmap.PNG
   :target: http://noc.futuregrid.org
   :width: 100px
   :height: 100px

.. |image16| image:: https://portal.futuregrid.org/sites/default/files/u23/Screen%20shot%202011-01-14%20at%207.48.06%20PM.png
   :target: http://inca.futuregrid.org
   :width: 100px
   :height: 100px

.. |image17| image:: https://portal.futuregrid.org/sites/default/files/u23/Screen%20shot%202011-04-07%20at%203.23.05%20PM.png
   :target: https://portal.futuregrid.org/monitoring/cloud
   :width: 100px
   :height: 100px

.. |image18| image:: https://portal.futuregrid.org/sites/default/files/screenshot-for-status-small.png
   :target: https://portal.futuregrid.org/metrics
   :width: 100px
   :height: 100px

.. |image19| image:: https://portal.futuregrid.org/sites/default/files/fg-sys-sw-ver.PNG
   :target: http://inca.futuregrid.org:8080/inca/HTML/rest/HPC/FutureGrid
   :width: 100px
   :height: 100px

.. |image20| image:: https://portal.futuregrid.org/sites/default/files/u15/nimbus-usage.png
   :target: http://inca.futuregrid.org/nimbus-stats
   :width: 100px
   :height: 100px

