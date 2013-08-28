.. _s-hadoop:

**********************************************************************
Using Hadoop in FutureGrid
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

We have various platforms that support Hadoop on FutureGrid. MyHadoop is probably the easiest solution offered for you. It provides the advantage that it is integrated into the queuing system and allows hadoop jobs to be run as batch job. This is of especial interest for classes that may run quickly out of resources if every students wants to run their hadoop application at the same time.

.. _s-myhadoop:


**********************************************************************
Running Hadoop as a Batch Job using MyHadoop
**********************************************************************

|Hadoop-logo|

MapReduce is a programming model developed by Google. Their
definition of MapReduce is as follows:  "MapReduce is a programming
model and an associated implementation for processing and generating
large data sets. Users specify a map function that processes a key/value
pair to generate a set of intermediate key/value pairs, and a reduce
function that merges all intermediate values associated with the same
intermediate key."  For more information about MapReduce, please see the
Google paper `here <http://labs.google.com/papers/mapreduce.html>`__.

The `Apache Hadoop Project <http://hadoop.apache.org>`__ provides an
open source implementation of MapReduce and HDFS (Hadoop Distributed
File System).   

This tutorial illustrates how to run Apache Hadoop thru the batch
systems on FutureGrid using the MyHadoop tool.  

myHadoop on FutureGrid
====================

`MyHadoop <http://sourceforge.net/projects/myhadoop/>`__ is a set of
scripts that configure and instantiate Hadoop as a batch job. 

myHadoop 0.20.2 is currently installed on Alamo, Hotel, India, and Sierra
FutureGrid systems. 


Running myHadoop on FutureGrid
----------------------------------------------------------------------

To run the example, use the following steps.

#. Log into a FutureGrid system that has myHadoop available.  In this
   tutorial, we are executing from the Hotel machine::

       $ ssh portalname@india.futuregrid.org
       This machine accepts SSH public key and One Time Password (OTP) logins only.
       If you do not have a public key set up, you will be prompted for a password.
       This is *not* your FutureGrid password, but the One Time Password generated from your
       OTP token.  Do not type your FutureGrid password, it will not work.  If you do not
       have a token or public key, you will not be able to login.
       The portalname is your account name that allows you to log into
       the FutureGrid portal..

#. Load the myHadoop module.  On some FutureGrid systems, you may also
   need to load the "torque" module as well if qstat is not already in
   your environment::

       $ module load myhadoop
       SUN Java JDK version 1.6.0 (x86_64 architecture) loaded
       Apache Hadoop Common version 0.20.203.0 loaded
       myHadoop version 0.2a loaded

#. To run the example now, skip to step 9.  Otherwise, view the
   pbs-example.sh script located in $MY_HADOOP_HOME/pbs-example.sh.
   At the top of the file, you will see standard batch directives
   indicating which queue to run the Hadoop job, how many nodes, etc::

       #PBS -q batch
       #PBS -N hadoop_job
       #PBS -l nodes=4:ppn=8
       #PBS -o hadoop_run.out
       #PBS -e hadoop_run.err
       #PBS -V

#. Next, there is a line to load Java via modules under the above lines::

       module add java

#. In the example script, a temporary directory to store Hadoop
   configuration files is specified as ${HOME}/myHadoop-config (although
   any globally accessible place is fine)::

       #### Set this to the directory where Hadoop configs should be generated
       # Don't change the name of this variable (HADOOP_CONF_DIR) as it is
       # required by Hadoop - all config files will be picked up from here
       #
       # Make sure that this is accessible to all nodes
       export HADOOP_CONF_DIR="${HOME}/myHadoop-config"

#. The pbs-example.sh script runs the "wordcount" program from
   the hadoop-0.20.2-examples.jar.  There is sample text data from the
   `Project Gutenberg website <http://www.gutenberg.org/>`__ located a
   $MY_HADOOP_HOME/gutenberg::

       $ ls $MY_HADOOP_HOME/gutenberg
       1342.txt.utf8

#. The following lines create a Data directory in HDFS (directory
   specified in $MY_HADOOP_HOME/bin/setenv.sh), copies over the
   gutenberg data, executes the Hadoop job, and then copies the output
   back your ${HOME}/Hadoop-Outputs directory. ::

       #### Run your jobs here
       echo "Run some test Hadoop jobs"
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -mkdir Data
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -copyFromLocal $MY_HADOOP_HOME/gutenberg Data
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -ls Data/gutenberg
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR jar $HADOOP_HOME/hadoop-0.20.2-examples.jar wordcount Data/gutenberg Outputs
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -ls Outputs
       $HADOOP_HOME/bin/hadoop --config $HADOOP_CONF_DIR dfs -copyToLocal Outputs ${HOME}/Hadoop-Outputs

#. Now submit the pbs-example.sh script to Hotel::

       $ qsub $MY_HADOOP_HOME/pbs-example.sh 
       40256.svc.uc.futuregrid.org

#. The job will take about 5 minutes to complete.  To monitor its
   status, type 'qstat'.  The "R" means the job is running::

       $ qstat
       Job id                    Name             User            Time Use S Queue
       ------------------------- ---------------- --------------- -------- - -----
       40256.svc                  hadoop_job       gvonlasz               0 R batch                  

#. When it is done, the status of the job will be "C" meaning the job
   has completed (or it will no longer be displayed in qstat output).
   You should see a new hadoop_run.out file and an "Hadoop-Outputs"
   directory ::

       $ qstat
       Job id                    Name             User            Time Use S Queue
       ------------------------- ---------------- --------------- -------- - -----
       40256.svc                  hadoop_job       gvonlasz       00:00:05 C batch                   
       $ ls
       Hadoop-Outputs hadoop_run.out

#. View results of the word count operation::

       $ head Hadoop-Outputs/part-r-00000  
       "'After    1
       "'My   1
       "'Tis  2
       "A 12
       "About 2
       "Ah!   2
       "Ah!" 1
       "Ah,   1
       "All   2
       "All!  1

Now to run you own custom Hadoop job, make a copy of the
$MY_HADOOP_HOME/pbs-example.sh script and modify the lines described
in Step 7.

Persistent Mode
----------------------------------------------------------------------

The above example copies input to local HDFS scratch space you specified
in $MY_HADOOP_HOME/bin/setenv.sh, runs MapReduce, and copies output
from HDFS back to your home directory.  This is called non-persistent
mode and is good for small amounts of data.  Alternatively, you can run
in persistent mode which is good if you have access to a parallel file
system or have a large amount of data that will not fit in scratch
space.  To enable persistent mode, follow the directions in
pbs-example.sh.


Customizing Hadoop Settings
----------------------------------------------------------------------

To modify any of the Hadoop settings
like maximum_number_of_map_task, maximum_number_of_reduce_task,
etc., make you own copy of myHadoop and customize the settings
accordingly.  For example:

#. Copy the $MY_HADOOP_HOME directory to your home directory::

       $ cp -r $MY_HADOOP_HOME $HOME/myHadoop

#. Then edit $HOME/myHadoop/pbs-example.sh and on line 16, replace it
   with::

       . ${HOME}/myHadoop/bin/setenv.sh

#. Similarly edit $HOME/myHadoop/bin/setenv.sh and on line 4, replace it
   with::

       export MY_HADOOP_HOME=$HOME/myHadoop

#. Customize the settings in the Hadoop files as needed in
   $HOME/myHadoop/etc

#. Submit your copy of pbs-example.sh::

       $ qsub $HOME/myHadoop/pbs-example.sh

Using a Different Installation of Hadoop
----------------------------------------------------------------------

If you would like to use a different version of my Hadoop or have
customized the Hadoop code in some way, you can specify a different
installation of Hadoop by redefining the HADOOP_HOME variable after
$MY_HADOOP_HOME/bin/setenv.sh is called within your own copy of
pbs-example.sh::

    ### Run the myHadoop environment script to set the appropriate variables
    #
    # Note: ensure that the variables are set correctly in bin/setenv.sh
    . /opt/myHadoop/bin/setenv.sh
    export HADOOP_HOME=${HOME}/my-custom-hadoop

More Information
----------------------------------------------------------------------

For more information about how myHadoop works, please see the
documentation in $MY_HADOOP_HOME/docs/myHadoop.pdf 

Gregor: naturally we should place a real http link. make sure this happens. for example, upload myHadoop to portal and use that link


.. |Hadoop-logo| image:: images/hadoop-logo.jpg
