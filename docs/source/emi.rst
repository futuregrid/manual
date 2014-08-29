


EMI Unicore Tutorial
====================

What is EMI?
------------

`European Middleware Initiative <http://www.eu-emi.eu/>`__ (EMI) is a
software platform for high performance distributed computing.

It is at the core of grid middleware distributions used by scientific
research communities and distributed computing infrastructures all over
the world including WLCG--the Worldwide LHC Computing Grid--which
supports, for example, the search for the Higgs boson and new types of
matter searches of the physicists at LHC, together with other large
scientific challenges in astronomy, biology, computational chemistry and
other sciences.

Being a close collaboration among well-established grid middleware
providers and other specialized software providers, EMI proposes itself
as a leading platform for scientific grid computing and looks at
expanding outside of its natural environment.

EMI on FutureGrid
-----------------

EMI have created a number of Virtual Appliances which run on FutureGrid.
This tutorial describes how to use the the EMI UNICORE server tools.
Users can connect an EMI user interface node to the UNICORE instance
running on the VM in order to submit jobs, monitor them and retrieve
results.

The emi-unicore virtual appliance is available on the following
resources

-  Sierra
-  Hotel
-  Foxtrot

Launching the UNICORE appliance
-------------------------------

To launch the emi-unicore VM you must use the Nimbus cloud-client tool.
For instructions on how to install and configure Nimbus please see
the \ `Nimbus
tutorial <https://portal.futuregrid.org/tutorials/nimbus>`__.

Once you have a working Nimbus client you can search for the emi-unicore
appliance using the following command

::

    $ bin/cloud-client.sh --list

You should see a the emi-unicore appliance in the list. To instantiate
an emi-unicore appliance use the following command

::

    $ bin/cloud-client.sh --run --name <VM appliance name> --hours <number of hours>

For example, if the emi-unicore appliance is called
emi1-unicore-centos-5.3-x64-p1.gz and you want to run it for three
hours, use the following command

::

    $ bin/cloud-client.sh --run --name emi1-unicore-centos-5.3-x64-p1.gz --hours 3

Once the VM is running you should have a working UNICORE server. You can
log in as root using your ssh key and test the UNICORE services with the
command

::

    $ unicore-unicorex-status.sh

Using your UNICORE Server
-------------------------

The emi-unicore appliance contains the UNICORE server packages. In order
to submit jobs to this server you must have access to a user interface
machine with the emi-ui package installed.

This can be an external machine, or another VM, but it must run
Scientific Linux versions 5 or 6.

The emi-ui package can be obtained from the \ `EMI
repository <http://emisoft.web.cern.ch/emisoft/index.html>`__. EMI
packages are signed with the EMI GPG key, which can be obtained
from \ `http://emisoft.web.cern.ch/emisoft/dist/EMI/2/RPM-GPG-KEY-emi <http://emisoft.web.cern.ch/emisoft/dist/EMI/2/RPM-GPG-KEY-emi>`__.
Download the key and run rpm --import <keyfilename> in order to allow
packages signed with this key to be verified.

First configure the repository by installing the relevant yum repository
file:

-  `SL5 <http://emisoft.web.cern.ch/emisoft/dist/EMI/2/sl5/x86_64/base/emi-release-2.0.0-1.sl5.noarch.rpm>`__
-  `SL6 <http://emisoft.web.cern.ch/emisoft/dist/EMI/2/sl6/x86_64/base/emi-release-2.0.0-1.sl6.noarch.rpm>`__

You should now be able to install packages from the EMI repository. To
install the emi-ui type

::

    $ yum install emi-ui

To configure your emi user interface to use the UNICORE server running
in your emi-unicore virtual appliance you must edit the file
.ucc/preferences. If this file does not exist first run the command ucc
to create it.

Set the registry line to the uri of the EMI UNICORE instance, you will
need to ensure that the hostname matches that of the emi-unicore VM
which you previously instantiated. The hostname was given in the output
of the Nimbus cloud-client.sh --run command. For example, if your
UNICORE appliance was instantiated on host vm-7.sdsc.futuregrid.org then
you would set the registry line as follows in the .ucc/preferences file:

::

    registry=https://vm-7.sdsc.futuregrid.org:8080/DEFAULT-SITE/services/Registry?res=default_registry

You will also need to configure the UNICORE authentication. Your UNICORE
server is configured to allow access to the UNICORE "demo user". You can
find the keystore for this
user \ `here <http://www.eu-emi.eu/documents/10147/45270/user-keystore.jks>`__,
download it and put it in the .ucc/certs/ directory. Next set the
following parameters in the .ucc/preferences file:

::

    keystore=certs/user-keystore.jks password=the!user

You are now ready to begin using your EMI UNICORE installation. To test
it use the command

::

    $ ucc connect

Querying Resources on EMI UNICORE
---------------------------------

Before you run any jobs, you should investigate what resources are
available. You can query the UNICORE server using the following commands

::

    $ ucc list-sites $ ucc list-storages $ ucc list-applications

The first two commands will tell you about the computing and storage
resources available to you. The last command tells you the supported
applications which you are permitted to use. If you look in more detail
at output of the list-applications command you will see that it provides
a list of common applications along with their version number.

::

    $ ucc list-applications Applications on target system <DEFAULT-SITE> Korn shell Version M 1993-12-28 q C shell 6.14.00 Bash shell 3.1.16 POVRay 3.5 Python Script 2.4.2 Perl 5.8.8 Date 1.0 Custom executable 1.0

When you submit a job to a UNICORE server, you must specify which of
these applications the job will use. You can also upload data files or
scripts for execution by any of these commands. The details of which
application to use and any input and output files must be stored in a
job description file which is submitted to UNICORE for execution.

Runing a job and the job description file
-----------------------------------------

Let's get started with a very simple example. Create a file on your user
interface machine called date.u with the follwoing content:

::

    # simple job: run Date { ApplicationName: Date, ApplicationVersion: 1.0, }

This file tells UNICORE to execute the application Date version 1.0.

To submit this job we use the command 

::

    $ ucc run date.u -v

In the output from this command you should see a line specifying where
the output file was downloaded to, for example:

::

    [ucc run] Downloading remote file 'https://vm-7.sdsc.futuregrid.org:8080/DEFAULT-SITE/services/StorageManagement?res=f884b431-4660-4b7a-b91c-260b647604db#//stdout' -> /root/./205d109d-42a6-4cea-8cd3-c85ecc201e4d/stdout

This line indicates that the standard output of your job has been
downloaded to the file
/root/./205d109d-42a6-4cea-8cd3-c85ecc201e4d/stdout

You can view your job's output by typing

::

    $ cat /root/./205d109d-42a6-4cea-8cd3-c85ecc201e4d/stdout Thu Jul 12 10:32:29 EDT 2012

Congratulations, you have now succesfully run your first EMI UNICORE
grid job! Of course, this was a very simple job, so next we will go on
to look at how you can submit your own data and scripts for execution by
UNICORE.

Running your own scripts
------------------------

The job that you ran above didn't require any input or output files, and
used a native command on the server that does not require any input.
This is not the case with most useful jobs.

If you want to run your own script you will need to upload the script to
the UNICORE storage device and specify it in the job description file to
tell UNICORE which of your input files to pass to the interpreter.

Let's start with a simple bash script. The emi-unicore appliance comes
with a version of the Bash shell, run ucc list-appliances to check the
version number.

Next create a job description file to run this application, for example:

::

    # a job to run a bash script { ApplicationName: Bash shell, ApplicationVersion: 3.1.16, }

Create a script that you want to run and copy it to the UI machine. A
"Hello world" example is given below.

::

    echo "Hello World!" > output.txt

This script should be set as the Source in your job description file as
follows

::

    Environment: [ "SOURCE=remoteScript.sh", ],

Next you must tell ucc to upload the script with your job, and to
download the output file using the Imports and Exports 

::

    Imports: [ { From: "./script.sh", To: "remoteScript.sh" }, ], Exports: [ { From: "output.txt", To:"./output.txt" }, ]

Your full job description file will now look something like this

::

    # a job to run a bash script { ApplicationName: Bash shell, ApplicationVersion: 3.1.16,  Environment: [ "SOURCE=remoteScript.sh", ],  Imports: [ { From: "./script.sh", To: "remoteScript.sh" }, ], Exports: [ { From: "output.txt", To:"./output.txt" }, ] }

Now run this job with the ucc run command. You can do the same with
Perl, Python or other scripting languages. Use ucc list-applications to
see a full list of available scripting languages.

Handling Data
-------------

If you have data files that you want to use with multiple jobs it can be
inefficient to stage them in with each job. In this case it may be
useful to copy the files to the UNICORE storage in advance. You can do
this using the ucc command line tool. Once done, your job can tell
UNICORE to copy the files to your local directory by specifying them in
your job description file.

To copy a file to a storage element first list the available storages:

::

    $ ucc list-storages Home https://vm-143.uc.futuregrid.org:8080/DEFAULT-SITE/services/StorageManagement?res=demo-Home

This tells you that your Home directory is available addressable via
this URI. You can use this URI to access your Home directory as follows

::

    $ ucc ls https://vm-143.uc.futuregrid.org:8080/DEFAULT-SITE/services/StorageManagement?res=demo-Home

::

    $ ucc put-file -s localfile.data -t https://vm-143.uc.futuregrid.org:8080/DEFAULT-SITE/services/StorageManagement?res=demo-Home#/remotefile.data

Note that the -s parameter for ucc put-file specifies the source file
while -t specifies the target file.

Using the full URI is sometimes inconvenient, so you can use a shorter,
more intuitive format. This is also a URI, but you need to know only the
site (target system) name, and the storage or job id. For example

::

    unicore6://DEFAULT-SITE/Home/file

will resolve the "Home" storage at the target system named
"DEFAULT-SITE".

::

    $ ucc put-file -s localfile.data -t u6://DEFAULT-SITE/Home/testdata  $ ucc get-file -s u6://DEFAULT-SITE/Home/testdata -t newlocalfile.data

Remember that you will need to copy the file to the local working
directory as part of your job in order to use it. To do this, include it
in the job description file as an import as follows:

::

    { From: "u6://DEFAULT-SITE/Home/testdata", To: "testdata"}

You can also refer to a job Uspace (the job's working directory) on a
given site. For this, you will need the unique ID of that job, which you
can get for example using the 'list-jobs' command. For example,

::

    unicore6://DEFAULT-SITE/1f3bc2e2-d814-406e-811d-e533f8f7a93b/outfile

refers to the file "outfile" in the working directory of the given job
on the "DEFAULT-SITE" target system. This may be useful for checking the
content of files during the job's execution, allowing you to steer the
analysis on the basis of partial results.

Resources
---------

In the Resources section of the .u script user can specify resources to
run the job on the remote system. The section may look as follows:

::

    Resources: { Memory: 128000000, Nodes: 1, CPUs: 8 , }

Running job on a set of files
-----------------------------

To run UNICORE on a set of files user can put jobs descriptions in one
directory (e.g. indir/) and use batch command: batch. -i argument
indicate source directory (with .u scripts), -o - directory for output
files:

::

    $ ucc batch -i indir -o outdir

 

Average: Select ratingPoorOkayGoodGreatAwesome

No votes yet
