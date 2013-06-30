**********************************************************************
ScaleMP vSMP
**********************************************************************

FutureGrid provides a new experimental distributed large memory SMP
machine. 

Accessing ScaleMP
----------------------------------------------------------------------

Access of the ScaleMP vSMP machine is managed through the job queueing
system on India. Specifically, you must submit a job to the scalemp
queue on the India cluster. If you haven't already, first log into India
and prepare your environment path::

    ssh username@india.futuregrid.org
    module load torque
    module load moab

 

Submitting a job
-----------------

From here, you are now able to submit to the scalemp queue::

    qsub scalemp_job.sh

 

OR run a job interactively::

    qsub -I -q scalemp


 

Developing a job script
----------------------------------------------------------------------

As the ScaleMP vSMP machine is a unique and tool, it requires some
simple but special configuration in order to take full advantage of its
capabilities.  This customization depends on the type of application you
are looking to run, so please consult the configuration type that best
fits your application.

 

MPI
~~~~

Below is an example script to run a MPI job.  Please note that we
currently only support using MPICH2.  Using OpenMPI and IntelMPI is
possible, however we do not currently support such usage at this time.
See /opt/ScaleMP/examples/ for more information::

    # Add path to MPICH2 tuned for vSMP foundation
    export PATH=/opt/ScaleMP/mpich2/1.0.8/bin:$PATH

    # If application binary is MPICH1 and dynamically linked, uncomment this
    # export USE_MPI_WRAPPER=MPICH1

    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so

    # Bind MPI processes on consecutive cores
    # Adding numabind for dynamic placement (according to VSMP_PLACEMENT)
    export PATH=/opt/ScaleMP/numabind/bin:${PATH}

    export VSMP_PLACEMENT=PACKED
    export VSMP_VERBOSE=YES 
    export VSMP_MEM_PIN=YES ulimit -s unlimited


    vsmputil --unpinall 
    time mpirun -np $NPROC ./mpi-app > log-mpi-app-$NPROC.txt

 

OpenMP
~~~~~~~

Below is an example script for running your OpenMP code on the scalemp
machine.  See /opt/ScaleMP/examples/OpenMP for more information::

    # Make sure to use Intel compilers to build the application # Intel compiler runtime environemnt setting 
    source /opt/intel/Compiler/11.1/069/bin/iccvars.sh intel64
    # Setting stacksize to unlimited
    ulimit -s unlimited
    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so

    # Bind OpenMP threads statically to consecutive cpus: last number is the cpu to start from
    export KMP_AFFINITY=compact,verbose,0,0

    # Alternatively you can use dynamic placement using numabind
    # export PATH=/opt/ScaleMP/numabind/bin:${PATH} # export LD_LIBRARY_PATH=/opt/ScaleMP/numabind/lib 
    # The cpu/offset to start from is calculated dynamically by numabind 
    # export KMP_AFFINITY=compact,verbose,0,`numabind --offset $np`

    np=16
    export OMP_NUM_THREADS=$np 
    /usr/bin/time ./openmp-app > log-openmp-app-$np.txt

 

Threaded
~~~~~~~~~

Below is an example script for running a job using Pthreads. See
/opt/ScaleMP/examples/Pthread for more information::

    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so
    # PATH to numabind, See /opt/ScaleMP/examples/ for more information
    export PATH=/opt/ScaleMP/numabind/bin:$PATH
    # Specify sleep duration for each pthread. Default = 60 sec if not set
    export SLEEP_TIME=120

    # 16 pthreads would be created
    NP=16
    ./ptest $NP > log-pthread-app-$NP 2>&1 &
    # Waiting for 15 seconds for all the threads to start
    sleep 15

    # Start numabind with a config file that has a rule for pthread, 
    # which would place all threads to consecutive cpus. 
    numabind --config myconfig >> log-pthread-app-$NP 2>&1
    wait

 

Throughput
~~~~~~~~~~~

Below is an example script to run a throughput job. See
/opt/ScaleMP/examples/ for more information::

    # Setting stacksize to unlimited
    ulimit -s unlimited
    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so

    # Bind the throughput job statically to a particular CPU
    for i in 1 2 3 4; do 
    numactl --physcpubind=$i-1 ./throughput-app $i > log-throughput-app-$i.txt 
    # To bind to a numa node, use numactl –cpunodebind=X 
    done

Serial
~~~~~~~~

Below is an example script to run a serial job.  See
/opt/ScaleMP/examples/ for more information::

    # Setting stacksize to unlimited
    ulimit -s unlimited
    # ScaleMP preload library that throttles down unnecessary system calls
    export LD_PRELOAD=/opt/ScaleMP/libvsmpclib/0.1/lib64/libvsmpclib.so

    # Bind the serial job statically to a particular CPU using numactl
    cpu=1; numactl --physcpubind=$cpu ./serial-app > log-serial-app-$cpu.txt
    # To bind to a numa node, use numactl –cpunodebind=X # See /opt/ScaleMP/examples/ for more information



 

 

