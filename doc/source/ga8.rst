
GA8: Running Condor Tasks on a Grid Appliance


Summary:
~~~~~~~~

This tutorial provides step-by-step instructions on how to deploy a Grid
Appliance configured withÂ Condor, an open-source job scheduler. The Grid
Appliance can be used as a basis for running a variety of educational,
training and outreach activities.

Prerequisites:
~~~~~~~~~~~~~~

-  To follow this tutorial, it is a pre-requisite that you have gone
   through one of the core Grid appliance tutorials:

   -  `Running the Grid Appliance on your
      desktop <https://portal.futuregrid.org/tutorials/ga1>`__
   -  `Running the Grid Appliance on
      FutureGrid <http://portal.futuregrid.org/tutorials/ga9>`__

Set Up and SubmitÂ a Condor Job
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Once you are logged in through ssh into the Grid appliance, change
   your user to "griduser", change your directory, and compile a simple
   program which estimates the value of "pi" using a Monte Carlo method:

.. code:: rteindent2

    su griduser
    cd 
    cd examples/montepi
    gcc montepi.c -o montepi -lm -m32

-  Inspect the "submit\_montepi\_vanilla" file - this file sets Condor
   up to submit two batches of 50 tasks, each of wihch runs one Monte
   Carlo task. Chech the status of the Condor pool (which shows nodes
   are connected, available for running tasks, busy, etc) with the
   "condor\_status" command. Then use the "submit\_montepi\_vanilla"
   file to submit your job:

.. code:: rteindent2

    more submit_montepi_vanilla
    condor_status
    condor_submit submit_montepi_vanilla

-  Monitor the progress of your jobs with the "condor\_q" command, which
   shows the status of your job queue. You can also check the status of
   the Condor pool with "condor\_status" to see which resources become
   busy. Once the Monte Carlo tasks complete and there are no jobs in
   the queue, check the various results that have been obtained from the
   different tasks with the "grep" command:

.. code:: rteindent2

    condor_q
    grep -i pi *.out

