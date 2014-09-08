
.. _s-twister-blast:

**********************************************************************
Running Twister Blast on FutureGrid HPC
**********************************************************************
.. sidebar:: Page Contents

   Author: Tak-Lon Stephen Wu

   This page was original designed by `SalsaHPC <http://salsahpc.indiana.edu/>`_ group for `Big Data for Science
   Workshop <http://salsahpc.indiana.edu/tutorial/>`_, you can see the
   original pages `here <http://salsahpc.indiana.edu/tutorial/>`_.

   .. contents::
      :local:


BLAST (Basic Local Alignment Search Tool) is one of the most widely used
bioinformatics applications written in C++, and the version we are using
is v2.2.23. `Twister <http://www.iterativemapreduce.org/>`_is an
iterative mapreduce framework which can be used both for iterative and
non-iterative applications. Twister Blast is an advanced Twister program
which helps Blast, a bioinformatics application, utilizes the Computing
Capability of Twister. With the flexibility of Twister run-time
environment, this application can run on a single machine, a cluster, or
Amazon EC2 cloud platform.

Twister-BLAST can divide original query file into small chunks, and
distribute them to all available computing nodes. Twister-BLAST manages
and schedules Map tasks to process each query chunk based on its
location. Output can also be collected by Twister-BLAST. Compared with
other parallel BLAST applications, Twister-BLAST is efficient and with
little overhead.

You can download the`Twister Blast <http://salsahpc.indiana.edu/tutorial/apps/twister-blast.tar.gz>`_
Source code and customized Blast program and Database archive
(`BlastProgramAndDB.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`_)
from `Big Data for Science
tutorial <http://salsahpc.indiana.edu/tutorial/hadoopblast.html>`_.


Requirement
~~~~~~~~~~~

#. Login to FutureGrid Cluster and obtain compute nodes.
   (`HPC <hpc.html>`_/
   `OpenStack <twister-futuregrid-cloud-openstack.html#id1>`_)
#. Start Twister on compute nodes. (`SalsaTwister
   Tutorial <http://salsahpc.indiana.edu/tutorial/twister-intro.html>`_)
#. Download and unzip `Twister
   Blast <http://salsahpc.indiana.edu/tutorial/apps/twister-blast.tar.gz>`_
   Source code.
#. Download customized Blast binary and Database archive
   `BlastProgramAndDB.tar.gz <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`_
#. Linux command experience.

Download and prepare the Twister-Blast
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, Download and unzip the `Twister Blast <http://salsahpc.indiana.edu/tutorial/apps/twister-blast.tar.gz>`_ 
package (named as $TWISTER\_BLAST\_PROGRAM here), then ​copy the
unzipped ​$TWISTER\_BLAST\_PROGRAM/blast/dist/Twister-Blast.jar to the
$TWISTER\_HOME/apps. Also, we download and unzip the blast program and
the database
`here <http://salsahpc.indiana.edu/tutorial/apps/BlastProgramAndDB.tar.gz>`_,
and set $BLAST\_HOME=/path/to/BlastProgramAndDB/. Go to
$TWISTER\_BLAST\_PROGRAM/blast/bin/, in **twister\_blast.properties**,
set the BLAST+ execution command (execmd property) to the BLAST program
(blastx) under $BLAST\_HOME/bin/. Execution options can be reset
according to users' needs. However, Input option (-query) and output
option (-out) are not set in execmd but in inop and outop in order to be
compatible with both BLAST+ and BLAST. Twister-BLAST will merge these
command options by itself when invoking BLAST+ parallel.
The execution command template inside**twister\_blast.properties** is
given below.

::

    execmd = time /N/u/yangruan/Quarry/workflow/ncbi-blast-2.2.23+/bin/blastp -db /N/dc/scratch/yangruan/blast/db/cog/10k/cog.10000 -evalue 100 -max_target_seqs 1000000 -num_alignments 1000000 -outfmt 6 -seg no
    inop = -query
    outop = -out

Prepare Twister-Blast input
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assume you have already download the input fasta file into some location
called [input file path]. Use the
$TWISTER\_BLAST\_PROGRAM/blast/bin/blastNewFileSpliter.sh to split the
input fasta file into multiple partitions. The parameters in as
following:

::

    args:  [query_file] [sequence_count]  [num_partition] [data_dir] [output_prefix] [output_map_file]

-  query\_file: input fasta file
-  sequence\_count: sequence count in the input fasta file
-  num\_partition: number of partitions, this number should be larger or
   equal to the total worker number started with twister
-  data\_dir: The output folder of partitioned fasta files
-  output\_prefix: The output prefix of partitioned fasta files
-  output\_map\_file: The file contains the information of all the
   partitions width and height.

Execute Twister-Blast
~~~~~~~~~~~~~~~~~~~~~

After deploying those required files onto file system, run the
twister-Blast program with the following commands:

::

    ./blastNew.sh 128 /N/dc/scratch/yangruan/fasta/cog/10000/400/ input_ .fa 400 /N/dc/scratch/yangruan/blast/result/cog/10k/eval_100_400p/ blastOut_

Here is the description of the above command:

::

    args:  [map number] [input folder] [input prefix] [input postfix (None for none)] [partition number] [output folder] [output prefix]

+--------------------+-----------------------------------------------------------------------------+
| **Parameter**      | **Description**                                                             |
+--------------------+-----------------------------------------------------------------------------+
| map number         | The map task number (usually equals to the number of worker started)        |
+--------------------+-----------------------------------------------------------------------------+
| input folder       | The folder of input fasta file partitions                                   |
+--------------------+-----------------------------------------------------------------------------+
| input prefix       | The prefix of input fasta file partitions                                   |
+--------------------+-----------------------------------------------------------------------------+
| input postfix      | The postfix (file extension) of input fasta file partitions (default .fa)   |
+--------------------+-----------------------------------------------------------------------------+
| partition number   | The number of input fasta file partitions                                   |
+--------------------+-----------------------------------------------------------------------------+
| output folder      | The folder to store output blast result                                     |
+--------------------+-----------------------------------------------------------------------------+
| output prefix      | The prefix of output blast result                                           |
+--------------------+-----------------------------------------------------------------------------+

If Twister Blast is running correctly, it will print twister running
messages similar to the following:

::

    ./blastNew.sh 128 /N/dc/scratch/yangruan/fasta/cog/10000/400/ input_ .fa 400 /N/dc/scratch/yangruan/blast/result/cog/10k/eval_100_400p/ blastOut_ 
    time /N/u/yangruan/Quarry/workflow/ncbi-blast-2.2.23+/bin/blastp -db /N/dc/scratch/yangruan/blast/db/cog/10k/cog.10000 -evalue 100 -max_target_seqs 1000000 -num_alignments 1000000 -outfmt 6 -seg no
    -query
    -out
    JobID: BlastNewac4d15a9-0997-11e1-81b4-5b7f60de01d2
    Nov 7, 2011 11:24:43 PM org.apache.activemq.transport.failover.FailoverTransport doReconnect
    INFO: Successfully connected to tcp://149.165.229.100:61616
    0    [main] INFO  cgl.imr.client.TwisterDriver  - MapReduce computation termintated gracefully.
    Total Time of BLAST : 28.12Seconds
    2    [Thread-1] DEBUG cgl.imr.client.ShutdownHook  - Shutting down completed.

Finishing the Map-Reduce process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After finishing the Job, please use the command to kill the Map-Reduce
daemon and broker:

::

    $TWISTER_HOME/bin/stop_twister.sh

`‹ Using Twister on FutureGrid </manual/twister>`_ `up </manual/paas>`_
`Eucalyptus and Twister on FutureGrid
› </tutorials/eucalyptus-and-twister-futuregrid>`_

