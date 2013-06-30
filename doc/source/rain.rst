**********************************************************************
RAIN
**********************************************************************

.. todo: just using the real manaual and possibly copy it via a fork
   into this one? Discuss with Gregor

FutureGrid image management defines the full lifecycle of the images
in FutureGrid. It involves the process of creating, customizing,
storing, sharing, and deploying images for different FutureGrid
environments. For information and instructions on managing your images
in FutureGrid, and the Rain environment, see the `Quickstart Guide <http://futuregrid.github.com/rain/quickstart.html>`__.


Generate and Register an OS Image on FutureGrid using the FG Shell
==================================================================

Below, we summarize the different steps needed to create a new image
and register it in a FutureGrid infrastructure. In this case, we will
register the image in OpenStack, but it can be registered in any other
FutureGrid infrastructure, such as Eucalyptus, Nimbus, or HPC. Detailed
information about these tools can be found
in  `http://futuregrid.github.com/rain/ <http://futuregrid.github.com/rain/>`__.

Request access
--------------

Submit a ticket to request
access `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__

Please use the subject: "Request to access FutureGrid Rain". Include
in the body "I would like to obtain access to FutureGrid Rain".

*Note: In future we may just create a checkbox for this request in the
help form.*
 

Once you have access, you can continue the tutorial. Typically, it will
take a business day for you to get added (a business day is 9am-5pm EST
Mon-Fri). 

Log into India
--------------

::

    $ ssh <username>@india.futuregrid.org
    $ module load futuregrid

Start the Shell
---------------

Execute the FG Shell. Please remember to replace <username> with your
portal user name. Then, you will be asked for a password (which is your
portal password)::

    $ fg-shell -u <username>

This command will change your shell and the prompt will be fg-rain>. If
your prompt is different, you need to execute "use rain".

Generate the Image
------------------

We are going to generate an Ubuntu 12.04 image. The -s parameter
allows you to specify the software you want to install in your image.
Currently, only the software available in the official repositories can
be installed::

    fg-rain> generate -o ubuntu -v 12.04 -a x86_64 -s wget, openmpi-bin

After a while, your image will be stored in the repository, and your
image ID will be printed.

Image Repository
----------------

We can consult the information of the image by executing the following
(please replace <imageid> with the ID that you got from the previous
command)::

    fg-rain> list * where imgId=<imageId>

Register Image
--------------

Next, we need to register that image in the infrastructure we want to
use. In this case, we will register the image in OpenStack (if you
followed the FG Openstack tutorial, your novarc will probably be in
~/openstack/novarc). This command will return an <ami-ID>, which is the
ID of the image in OpenStack::

    fg-rain> register -r <imageId> -s india -v ~/novarc

Once you have registered the image, you need to wait until it becames
available. To check the status of the image, you can execute the
following command::

    fg-rain> cloudlist -s india -v ~/novarc | grep <imageId>

The status is the second field. You may experience that this command
takes time to respond when the image is being uploaded (it is an
OpenStack issue).

Start Image
-----------

Once the image is in "available" status, we can proceed to start a VM
using the ami-ID that we got from the register command. In this case, we
are going in Interative mode, which means that we are going to get
logged into the VM once it is running::

    fg-rain> launch -i <ami-ID> -s india -v ~/novarc -I






FutureGrid Standalone Image Repository
======================================

The FutureGrid image repository is a standalone service that is not
tied to FutureGrid nor to any IaaS infrastructure. This image repository
offers a common interface that can distinguish image types for different
IaaS frameworks like Nimbus, Eucalyptus, and also bare-metal images.
This allows us in FG to include a diverse image set not only contributed
by the FG development team, but also by the user community that
generates such images and wishes to share them. The images can be
described with information about the software stack that is installed on
them including versions, libraries, and available services. This
information is maintained in the catalog and can be searched by users
and/or other FutureGrid services. Users looking for a specific image can
discover available images ﬁtting their needs, and ﬁnd their location in
the repository by using the catalog interface.

The repository supports different storage systems that allow you to
choose the most appropriate one for you. It includes MySQL, where the
image ﬁles are stored directly in the POSIX ﬁle system; MongoDB, where
both data and ﬁles are stored in the NoSQL database; the OpenStack
Object Store (Swift); and Cumulus from the Nimbus project. For the last
two cases, the data can be stored in either MySQL or in MongoDB. These
storage plugins not only increase the interoperability of the image
repository, but can also be used by the community as templates to create
their own plugins to support other storage systems.

Requirement
-----------

-  Python 2.6 or 2.7
-  LDAP server for user authentication

Software
--------

The software is open-source under an Apache 2 license. The image
repository can be found in github as part of our Image Management and
Rain
software  `https://github.com/futuregrid/rain <https://github.com/futuregrid/rain>`__ .

Documentation
-------------

The documentation can be found
in  `http://futuregrid.github.com/rain/index.html <http://futuregrid.github.com/rain/index.html>`__.
Since this link provides information about all our tools, in this
section we collect the links that refer to the image repository.

User Manual
~~~~~~~~~~~

Information about the command-line interface is found
in  `http://futuregrid.github.com/rain/man-repo.html <http://futuregrid.github.com/rain/man-repo.html>`__.
If you are interested on using the shell, the manual is
in  `http://futuregrid.github.com/rain/man-shell.html <http://futuregrid.github.com/rain/man-shell.html>`__.

Installation
~~~~~~~~~~~~

You need to install the complete software, even if you only want to
use the image repository. This information is found
in  `http://futuregrid.github.com/rain/install.html <http://futuregrid.github.com/rain/install.html>`__.

Configuration
~~~~~~~~~~~~~

The configuration information can be found
in  `http://futuregrid.github.com/rain/configure\_futuregrid.html <http://futuregrid.github.com/rain/configure_futuregrid.html>`__.
You will be interested in:

-  Configuration
   files  `http://futuregrid.github.com/rain/configure\_futuregrid.html#configuration-files <http://futuregrid.github.com/rain/configure_futuregrid.html#configuration-files>`__
-  Setting up LDAP
   information  `http://futuregrid.github.com/rain/configure\_futuregrid.html#setting-up-ldap <http://futuregrid.github.com/rain/configure_futuregrid.html#setting-up-ldap>`__
-  Setting up the Image
   Repository  `http://futuregrid.github.com/rain/configure\_futuregrid.html#setting-up-the-image-repository <http://futuregrid.github.com/rain/configure_futuregrid.html#setting-up-the-image-repository>`__

Manual Image Customization
==========================

Sometimes users need to further customize their images by installing
their own software-software which may not be able to be installed with
the image generation tool. In this tutorial, we explain how users can
perform this customization in the images created with the FG image
generation tool. Detailed information about FG image management tools
can be found in
`http://futuregrid.github.com/rain/ <http://futuregrid.github.com/rain/>`__.

Logging into India
------------------

::

    $ ssh <username>@india.futuregrid.org 
    $ module load futuregrid

 
-

Requesting access
-----------------

Submit a ticket to request
access  `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__

Obtaining the image
-------------------

You can get your image from our repository, or generate a new one.

Getting an image from the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ fg-repo -u <username> -g <imageId>

Generating a new image
~~~~~~~~~~~~~~~~~~~~~~

We are going to generate an Ubuntu image. Since we want to modify the
image, we have specified the -g parameter to retrieve the image after it
is generated. By default, it is uploaded to the image repository::

    $ fg-generate -u jdiaz -o ubuntu -v 12.04 -a x86_64 -s wget, openmpi-bin -g

In both cases, we will obtain a tgz file that contains the image file
(.img) and a manifest (.manifest.xml). For example, our image could be
in */N/u/<username>/123123123.tgz* .

Customizing the image
---------------------

To continue with the rest of the tutorial, we need a UNIX machine
where we have root privileges.

Assuming that we are in a UNIX machine with root privileges:

1. Retrieve the image from India::

    $ scp <username>@india.futuregrid.org:/N/u/<username/123123123.tgz .

2. Decompress the image::

    $ tar vxfz 123123123.tgz

    jdiaz859434.img
    jdiaz859434.manifest.xml

3. Mount the image. This will mount the image file into a directory.
In this way, we will have access to the OS files that are inside the
image::

    $ mkdir image
    $ sudo mount -o loop jdiaz859434.img image

Copy your software into the image directory (if needed). In this case,
I am going to copy a software directory to the tmp directory of the
image::

    $ cp -r /home/javi/mysoftware image/tmp

*Chroot* into the image. This changes the root of the OS to the one of
the image. In this way, evey operation we execute will have effect only
inside the image. After executing this command, you will be the root
users inside the image::

    $ sudo chroot image

Now you can install whatever software you need. You can also use
*yum/apt* to install packages from the software repository. Remember
that they will be installed inside the image. As example, here I install
tomcat with *apt* and compile my software with *make*::

    # apt-get install tomcat6
    # cd /tmp/mysoftware
    # make && make install

You can also configure the OS of image to start services during the
boot time. The easiest way to do that is by modifying
the\ */etc/rc.local*\ file.

Once you have finished customizing your image, you need to exit from
the *chroot* command, unmount the image, and compress it again::

    # exit
    $ sudo umount image
    $ tar vxfz mynewimage.tgz jdiaz859434.img jdiaz859434.manifest.xml

Transfer the image back to India
--------------------------------

::

    $ scp mynewimage.tgz <username>@india.futuregrid.org:/N/u/<username>/

Log into India
--------------

::

    $ ssh <username>@india.futuregrid.org 
    $ module load futuregrid

Upload the image to the repository
----------------------------------

We upload the image to the repository so we can reuse it and share it
with other users. When uploading the image, you can specify some
metadata to describe the properties of the image::

    $ fg-repo -p mynewimage.tgz "os=Ubuntu12 & arch=x86_64 & description=My new customized image & tag=tomcat, openmpi"

This command will provide you the ID your image has in the repository.
This ID is needed for the next step.

Register your image in different infrastructures
------------------------------------------------

You now have your image ready to be registered in the different
FutureGrid infrastructures. To use OpenStack
(`tutorial <https://portal.futuregrid.org/tutorials/openstack>`__) and
Eucalyptus
(`tutorial <https://portal.futuregrid.org/tutorials/eucalyptus3>`__),
you need to indicate the location of you novarc and eucarc file.

Register the image in Openstack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ fg-register -u <username> -r <imageID> -s india -v ~/novarc

Register the image in Eucalyptus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ fg-register -u <username> -r <imageID> -e india -v ~/eucarc

Register the image in HPC
~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ fg-register -u <username> -r <imageID> -x india


Each command will provide you with the ami-ID that your image has in
the specified infrastructure.

Using your Registered Image
---------------------------

.. todo:: fix the links in this section

OpenStack (more info in  `https://portal.futuregrid.org/tutorials/openstack <https://portal.futuregrid.org/tutorials/openstack>`__)::

    source novarc
    euca-run-instance -k <keyname> <ami-ID>

Eucalyptus (more info in  `https://portal.futuregrid.org/tutorials/eucalyptus3 <https://portal.futuregrid.org/tutorials/eucalyptus3>`__)::

    source eucarc
    euca-run-instance -k <keyname> <ami-ID>

HPC (more info in  `https://portal.futuregrid.org/tutorials/hpc <https://portal.futuregrid.org/tutorials/hpc>`__):

Provision a machine with our image and go into Interactive mode (you
are logged into the machine)::

    qsub -l os=<ami-ID> -I

Provision two machines with our image and execute an script::

    qsub -l os=<ami-ID> -l nodes=2:ppn=8 myscript.sh




RAIN Manual Pages
=================

FutureGrid provides a number of manual pages, listed below.

(For Rain, our up-to-date documentation of rain can be found at
`https://portal.futuregrid.org/doc/rain/index.html <https://portal.futuregrid.org/doc/rain/index.html>`__
and\ `http://futuregrid.github.com/rain/index.html <http://futuregrid.github.com/rain/index.html>`__
.

- `fg-repo <http://futuregrid.github.com/rain/man-repo.html>`__
- `fg-rain <http://futuregrid.github.com/rain/man-rain.html>`__
- `fg-generate <http://futuregrid.github.com/rain/man-generate.html>`__
- `fg-register <http://futuregrid.github.com/rain/man-register.html>`__
- `fg-shell <http://futuregrid.github.com/rain/man-shell.html>`__

fg-portal-manage
-----------------
The tool is for admin purpose only. An admin person or an system script
can call this to get user/project information from the portal::

    fg-portal-manage 
     -h, --help            show this help message and exit
     -n NAME, --name=NAME  querying by name
     -m MAIL, --mail=MAIL  querying by email
     -i UID, --uid=UID     querying by portal uid
     -u USERNAME, --username=USERNAME
                           querying by portal username
     -k, --attrib          specifying attrib(s) to be displayed, inlcuding:
                           firstname, lastname, email, phone, organization,
                           institution_name, citizenship, sshkey, projectall,
                           project
     -l, --ldif            output ldif format of user info(no dn). If provided
                           all attributes will be included in the output
                           disregarding the setting from -k
     -v, --vetted          Show only those vetted users. If omitted all users
                           that meet the creteria will be shown
     -w, --waiting         Show the waiting list in which a user is eligible to
                           get an LDAP account
     -y, --withsshkey      A sub-option for -w, which shows the waiting list, but
                           only for those who have submitted a sshkey
     -p, --project         Get list of project in table view
     -s STATUS, --status=STATUS
                           A sub-option for -p, which specifies project status
                           that would like to be retrieved. Try pending,
                           approved, completed, denied
     -1, --pidonly         A sub-option for -p which prints out only the project



DESCRIPTION
^^^^^^^^^^^^

FutureGrid account admin tool queries user profile info from the portal
and also checks status against the ldap.

To run the script, python 2.7 is needed (if trying on lower version, try
to install the argparse module; it may also work), as well as the
mysqldb module. Depending on the os distribution, the installation could
be different. E.g., in ubuntu, it's simply: apt-get install
python-mysqldb .

The futuregrid.cfg file needs to be put into the same directory as the
script, and the dummy config values need to be replaced with those real
ones. (Whoever has access to the portal server should have knowledge on
this. We will not distribute this to anymore other than the portal admin
and sys admin.)



EXAMPLES
^^^^^^^^^^^^

.. todo:: fix this command

Run this to get the help info::

    ./fg-portal-manage.py -h

This will give a table viewed info of user with uid 3::

    ./fg-portal-manage.py -i 3

However, the following::

    ./fg-portal-manage.py -i 3 -l

will print the long quasi-ldif formatted info.

Other command::

    -u for username; -n for realname(first or last); as well as -m for email does similar thing

:: 

    ./fg-portal-manage.py -l

-will simply print out all users in the portal in the ldif-like format.

::

    ./fg-portal-manage.py -l -v

-will print out a similar list but only for (all) those vetted users,
i.e., approved users with an active project.

::
    ./fg-portal-manage.py -w

-prints out all users who have approved portal account and are members
of an active project(s) (i.e., vetted users), but don't have an LDAP
account yet.

::

    ./fg-portal-manage.py -l -w

-the same as -w but in long quasi-ldif format.

::

    ./fg-portal-manage.py -w -y

-the same as -w, but prints out only those who have submitted a sshkey.

::

    ./fg-portal-manage.py -p

-lists all FG projects registered in the portal, in the format of:

::

    pid: title|project lead|project manager|status|[members list]

-project lead/manager and members are represented by the portaluid.

::

    ./fg-portal-manage.py -p -s approved

-prints a list of projects but only those in 'approved' status. Other
valid statuses are: pending, completed, denied.

::

    ./fg-portal-manage.py -p -s completed -1(number '1')

-prints a list of completed projects but only display the projectids.
 
