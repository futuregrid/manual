SAGA supporting Distributed Applications on Grids, Clouds on FutureGrid
=======================================================================

***SAGA on FutureGrid***


***Activity***:

The Simple API for Grid Applications (SAGA) is an OGF standard
(`http://www.ogf.org/ <http://www.ogf.org/>`__), and defines a high
level, application-driven API for developing first-principle distributed
applications, and for distributed application frameworks and tools. Our
SAGA project (see
`http://www.saga-project.org/ <http://www.saga-project.org/>`__)
provides SAGA API implementations in C++ and Python, which interface to
a variety of middleware backends, as well as higher level application
frameworks, such as Master-Worker, MapReduce, AllPairs, and BigJob.  For
all those components, we use FutureGrid and the different software
environments available on FG for extensive portability and
interoperability testing, but also for scale-up and scale-out
experiments. These activities allow to harden the SAGA components
described above, and support CS and Science experiments based on SAGA.

***Achievements:***

FG has provided a persistent, production-grade experimental
infrastructure with the ability to perform controlled experiments,
without violating production policies and disrupting production
infrastructure priorities.  These attributes, coupled with FutureGrid's
technical support, have resulted in the following specific advances in
the short period of under a year:

*1: Use of FG for Standards-based development and interoperability
tests:*

We have, in particular, been able to prepare SAGA for future
deployments on XSEDE; this has occurred by testing the SAGA-BES adaptor
in a variety of configurations: against Unicore and Genesis-II backends,
with UserPass and Certificate-based authentication, with POSIX and HPC
application types, with and without file staging support.  While those
tests are still ongoing, it allows us to be confident about the expected
XSEDE middleware evolution; in the vast majority of cases, the
standards-based approach seems to work without a hitch.

Furthermore, we are continuously using FG-based job submission
endpoints for GIN-driven interoperation tests with a variety of other
production Grid infrastructures, including DEISA, PRACE, Teragrid and
EGI (see
`http://forge.gridforum.org/sf/projects/gin/ <http://forge.gridforum.org/sf/projects/gin/>`__
and
`http://www.saga-project.org/interop-demos/ <http://www.saga-project.org/interop-demos/>`__).

In order to simplify the deployment and to improve end user support
for SAGA, we have been using FG hosts to develop, test and harden our
deployment procedures by mimicking the CSA approach we currently use on
TeraGrid and XSEDE.  At the same time, that deployment procedure makes
SAGA and SAGA-based components available and maintained on all FG
endpoints.


*2: Use of FG for Analysing & Comparing Programming Models and
Run-time tools for Computation and Data-Intensive Science.*

*2.a: Development of Tools and Frameworks:*

-  P\* experiments
    'P\*' is a conceptual model of pilot-based abstractions, in
   particular for pilot jobs.  Our work on P\* includes comparison
   between different PilotJob frameworks (BigJob, Condor GlideIn, Diane,
   Swift), and between different coordination models within those
   frameworks.  We used FG for a number of those experiments, as it
   allowed us to compare a range of characteristics in a controlled
   environment.
-  Advanced dynamic partitioning and distribution of data-intensive
   distributed applications
    Futuregrid resources have been crucial in carrying out a first set
   of scoping experiments for O.W.'s Ph.D thesis: "Towards a Reasoning
   Framework and Software System to Aid the Dynamic Partitioning,
   Distribution and Execution of Data-Intensive Applications". In these
   scoping experiments, three distinct FutureGrid resources (india,
   hotel, alamo) were used to coordinately execute a data-intensive
   genome matching workload (HTC). The partitioning and distribution
   decisions were dynamically made by an experimental software system
   based on autonomic computing concepts, and which is capable of
   monitoring FG HPC resources as well as jobs during workload
   execution.
-  Bliss (Bliss is SAGA)
    Bliss
   (`http://oweidner.github.com/bliss/ <http://oweidner.github.com/bliss/>`__)
   is an experimental implementation of SAGA written in pure Python.
   Bliss does not rely on any distributed Grid middleware; however, it
   allows distributed access to all FutureGrid HPC resources by
   providing an SFTP plugin for file transfer as well as 'PBS over SSH'
   for SAGA's job submission and resource information capabilities. 
   Bliss has been developed specifically with FutureGrid in mind and has
   been used in several cross-site experiments as the primary access
   mechanism to computing and storage resources.  While 'PBS over SSH'
   probably won't be a replacement for 'real' Grid middleware (like,
   e.g., Globus), its exposure through the standardized SAGA API
   presents an attractive and lightweight alternative to traditionally
   large Grid middleware stacks.
-  High-performance dynamic applications
    In extreme-scale computational science, there is a growing
   importance and need for specialized architectures and multi-model
   simulations. In this emerging environment, different simulation
   components will have different computational requirements.  Instead
   of coarsely assigning resources to all simulation components for
   their lifetime, we research methodologies whereby simulations can be
   split into their constituent components, and distributed
   computational resources are allocated according to the needs of these
   individual components.  Each simulation component is transferred
   along with the data and parameters needed to execute the simulation
   component on the target hardware.  This approach enables
   multi-component applications to more easily benefit from
   heterogeneous and distributed computing environments, in which
   multiple types of processing elements and storage may be available.
    In cases where software is developed with a static execution mode
   and only one resource in mind, the choice to distribute may not be
   available. By creating a dynamic method of execution and developing
   software which can package, transmit, and execute sub-applications
   remotely, existing simulations may be extended to make use of
   distributed resources. Through specially-designed modules that are
   compatible with pre-existing Cactus framework applications, we
   demonstrated means of improving task-level parallelism and extended
   the range of computing resources used with a minimal amount of change
   needed to existing applications.  Experiments were conducted using
   production cyberinfrastructures on FutureGrid and XSEDE, with up to
   128 cores.
-  Grid/Cloud interop (with Andre Luckow) [finished]
    We demonstrated for the first time the use of Pilot-Jobs
   concurrently on different types of infrastructures; specifically, we
   use BigJob both on FutureGrid HPC and Cloud resources as well as on
   other resources such as the XSEDE and OSG Condor resources.

   
*2.b: Data Intensive Apps:*

-  MapReduce [with Andre Luckow]
    In Ref. [1], published in Future Generation Computing Systems, we
   compare implementations of the word-count application to not only use
   multiple, heterogeneous infrastructure (Sector versus DFS), but also
   to use different programming models (Sphere versus MapReduce).
-  Grid/Cloud NGS analysis experiments
    Building upon SAGA-based MapReduce, we have constructed an efficient
   pipeline for gene sequencing. This pipeline is capable of dynamic
   resource utilization and task/worker placement.
-  Hybrid cloud-Grid scientific applications and tools (autonomic
   schedulers) [with Manish Parashar, finished]
    Policy-based (objective driven) Autonomic Scheduler provides a
   system-level approach to hybrid grid-cloud usage.  FG has been used
   for the development and extension of such Autonomic Scheduling and
   application requirements.  We have integrated the distributed and
   heterogeneous resources of FG as a pool of resources which can be
   allocated by the policy-based Autonomic Scheduler (Comet). The
   Autonomic Scheduler dynamically determines and allocates instances to
   meet specific objectives, such as lowest time-to-completion, lowest
   cost etc. We also used FG supplement objective-driven pilot jobs on
   TeraGrid (ranger).
-  Investigate run time fluctuations of application kernels
    We attempt to explore and characterize run-time fluctuations for a
   given application kernel representative of both a large number of
   MPI/parallel workloads and workflows.  Fluctuation appears to be
   independent of the system load and a consequence of the complex
   interaction of the MPI library specifics and virtualization layer, as
   well as operating environment.  Thus we have been investigating
   fluctuations in application performance due to the cloud operational
   environment.  An explicit aim is to correlate these fluctuations to
   details of the infrastructure.  As it is difficult to discern or
   reverse engineer the specific infrastructure details on EC2 or other
   commercial infrastructure, FG has provided us a controlled and well
   understood environment at infrastructure scales that are not possible
   at the individual PI/resource level.


*3. SAGA has also produced the following papers (selection):*
 

See Refs:
`[1] <#ref1>`__,\ `[2] <#ref2>`__,\ `[3] <#ref3>`__,\ `[4] <#ref4>`__,\ `[5] <#ref5>`__



***FuturePlans:***

We will be continuing to use FG as a resource for SAGA development. 
Among other goals, we intend the following: to move the testing
infrastructure to other SAGA based components, like our PilotJob and
PilotData frameworks; to widen the set of middlewares used for testing
(again, keeping XSEDE and other PGIs in mind); to enhance the scope and
scale of our scalability testing; and to test and harden our deployment
and packaging procedures.


 

--------------

References
~~~~~~~~~~

#. [fg-1975] `Sehgal, S. </biblio/author/175>`__, `M.
   Erdelyi </biblio/author/176>`__, `A. Merzky </biblio/author/177>`__,
   and `S. Jha </biblio/author/115>`__, "`Understanding
   application-level interoperability: Scaling-out MapReduce over
   high-performance grids and
   clouds </references/understanding-application-level-interoperability-scaling-out-mapreduce-over-high-performa>`__\ ",
   Future Generation Computer Systems, vol. 27, issue 5, 2011.
#. [fg-1976] `Luckow, A. </biblio/author/178>`__, `L.
   Lacinski </biblio/author/179>`__, and `S.
   Jha </biblio/author/115>`__, "`SAGA BigJob: An Extensible and
   Interoperable Pilot-Job Abstraction for Distributed Applications and
   Systems </references/saga-bigjob-extensible-and-interoperable-pilot-job-abstraction-distributed-applications-a>`__\ ",
   10th IEEE/ACM International Symposium on Cluster, Cloud and Grid
   Computing, 2010.
#. [fg-1977] `Luckow, A. </biblio/author/178>`__, and `S.
   Jha </biblio/author/115>`__, "`Abstractions for Loosely-Coupled and
   Ensemble-Based Simulations on
   Azure </references/abstractions-loosely-coupled-and-ensemble-based-simulations-azure>`__\ ",
   IEEE International Conference on Cloud Computing Technology and
   Science, 2010.
#. [fg-1978] `Kim, J. </biblio/author/180>`__, `S.
   Maddineni </biblio/author/181>`__, and `S.
   Jha </biblio/author/115>`__, "`Building Gateways for Life-Science
   Applications using the Dynamic Application Runtime Environment (DARE)
   Framework </references/building-gateways-life-science-applications-using-dynamic-application-runtime-environment>`__\ ",
   The 2011 TeraGrid Conference: Extreme Digital Discovery, 2011.
#. [fg-1979] `Kim, J. </biblio/author/180>`__, `S.
   Maddineni </biblio/author/181>`__, and `S.
   Jha </biblio/author/115>`__, "`Characterizing Deep Sequencing
   Analytics using BFAST: Towards a Scalable Distributed Architecture
   for Next-Generation Sequencing
   Data </references/characterizing-deep-sequencing-analytics-using-bfast-towards-scalable-distributed-archite>`__\ ",
   The Second International Workshop on Emerging Computational Methods
   for the Life Sciences, 06/2011.

Average: Select ratingPoorOkayGoodGreatAwesome

Your rating: 5 Average: 4.5 (2 votes)
