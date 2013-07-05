
.. csv-table:: Selected Details of the Compute Resources
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
