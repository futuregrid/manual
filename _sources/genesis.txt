**********************************************************************
Genesis II 
**********************************************************************

Author: University of Virginia
Version: 1.0
Last Revision: 2011-11-02

Introduction
=============

`GenesisII <http://www.genesis2.virginia.edu/wiki>`__ compute endpoints
are currently deployed on three FutureGrid HPC resources: XRay, Sierra
and India.  Additional endpoints are planned for Hotel and Alamo in the
near future.  This tutorial explains:

-  How to connect to these GenesisII endpoints from other grid
   middleware platforms;
-  How to download GenesisII client software and use the UVa Corss
   Campus Grid (XCG) which includes the FutureGrid endpoints.

What is GenesisII
=================

GenesisII is a Grid middleware system. Listed below are the key
principles/features of the GenesisII design. More information about
GenesisII can be found `here <http://www.genesis2.virginia.edu/wiki>`__.

-  Open source.

-  Standards-based. GenesisII follows grid standards from the Open Grid
   Forum (OGF), W3C, and OASIS, including many from the Open Grid
   Services Architecture (OGSA) and the Web Services Resource Framework
   (WSRF).  In particular, GenesisII adheres to parts or all of OGSA
   Basic Execution Service (BES), Resource Naming Service (RNS), OGSA
   ByteIO, WS-Security, WS-Naming, WS-Trust, and Job Submission
   Description Language (JSDL).

-  Open and extensible realized with a modern Service- Oriented
   Architecture (SOA), which allows to easily replace particular
   components with others.

-  Interoperable with other Grid technologies to enable a coupling of
   Grid infrastructures or the users needs

-  End user focused. Whenever possible GenesisII was designed to use
   concepts already familiar to users (such as hierarchical directory
   structures) and to provide easy to use commands and GUIs to simplify
   the user's experience.  GenesisII provides a number of commands based
   on familiar UNIX tools and provides GUIs for to browse the grid
   directory structure, monitor jobs, create JSDL job descriptions, etc.

-  Strong security mechanisms built in from the ground up.  Flexible
   access control for all grid resources.  Support for X.509
   certificates and username/password (based on WS-Security and OGF
   Basic Security Profile).  Support for virtual organizations via
   user-defined groups.

-  Quick and simple to install and configure.

-  Client and server software supported on a number of platforms
   (Windows XP, Linux, and MacOS).  Support for various batch systems
   such as PBS, Sun Grid Engine, etc.

-  Implemented in Java to achieve platform independence.

Connecting to the GenesisII BES Endpoints
=========================================

To date, three GenesisII BES endpoints have been deployed on FutureGrid
for interoperability testing as well as grid client usage. Endpoints are
located on Sierra, India, and Alamo. This section contains the
information needed for other grid middleware platforms to connect to the
GenesisII BES endpoints.

Supported Data Staging Protocols
----------------------

Each of the GenesisII endpoints supports a number of protocols for
staging data into and out of jobs as supported by the JSDL
specification's Data Staging elements.  The following are the protocols
currently supported by the GenesisII endpoints:


Stage in:
~~~~~~~~~

-  HTTP
-  RNS/ByteIO
-  ftp
-  scp
-  sftp

Stage out:
~~~~~~~~~~

-  mailto
-  RNS/ByteIO
-  ftp
-  scp
-  sftp

\*\* NOTE: ftp, scp, sftp is supported as per the HPC FSE standard and
only for the username/password security token version.

Endpoint Connection Information 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

India
-------------------------------

-  **Endpoint EPR**: `click
   here <https://portal.futuregrid.org/sites/default/files/india-epr-Nov-01-2011.txt>`__

-  **Security**: configured for username/password authentication;
   `Email <mailto:uvacse@virginia.edu>`__ for username token and CA
   cert.

-  **OS**: Red Hat Enterprise Linux Server release 5.7

-  **Arch**: x86\_64

-  **Cores**: Approximately 400. Jobs submitted to HPC (i.e. batch)
   queue via PBS
     
-  **Grid Path**:
   /bes-containers/FutureGrid/IU/pbs-long.from-daemon.india.futuregrid.org

Sierra
----------------------------------------------------------------------

-  **Endpoint EPR**: `click
   here <https://portal.futuregrid.org/sites/default/files/sierra-epr-Mar-22-2012_0.txt>`__

-  **Security**: configured for username/password authentication;
   `Email <mailto:uvacse@virginia.edu>`__ for username token and CA
   cert.

-  **OS**: Red Hat Enterprise Linux Server release 6.1

-  **Arch**: x86\_64

-  **Cores**: Approximately 300. Jobs submitted to HPC (i.e. batch)
   queue via PBS
     
-  **Grid Path**:
   /bes-containers/FutureGrid/SDSC/pbs-long.from-daemon.sierra.futuregrid.org

Alamo
~~~~~

-  **Endpoint EPR**: `click
   here <https://portal.futuregrid.org/sites/default/files/alamo-epr-Mar-22-2012_0.txt>`__

-  **Security**: configured for username/password authentication;
   `Email <mailto:uvacse@virginia.edu>`__ for username token and CA
   cert.

-  **OS**: CentOS release 5.6

-  **Arch**: x86\_64

-  **Cores**: Approximately 200. Jobs submitted to HPC (i.e. batch)
   queue via PBS
     
-  **Grid Path**: /bes-containers/FutureGrid/TACC/pbs-long.from-alamo1

Hotel
~~~~~

-  **Endpoint EPR**: `click
   here <https://portal.futuregrid.org/sites/default/files/hotel-epr-Apr-24-2012.txt>`__

-  **Security**: `Email <mailto:uvacse@virginia.edu>`__ for
   username/password authentication token and CA cert.

-  **OS**: Red Hat Enterprise Linux Server release 5.8 (Tikanga)

-  **Arch**: x86\_64
     
-  **Cores**: Approximately 300. Jobs submitted to HPC (i.e. batch)
   queue via PBS
     
-  **Grid Path**:
   /bes-containers/FutureGrid/UC/pbs-long.from-hotel1.futuregrid.org

Using the Futuregrid GenesisII Endpoints as a Client
====================================================

There are two ways a client can use the GenesisII endpoints deployed
within Futuregrid: using a standards-compliant non-GenesisII middleware
client or using the GenesisII client.

Non-GenesisIIUsing a Standards-Compliant Client
-----------------------------------------------

If you wish to use a standards-based middleware client, you may be
able to use that client to access the GenesisII BES endpoints within
Futuregrid.  The first step is to determine whether the grid client
software you wish to use is properly compliant with the GenesisII BES
implementation.  GenesisII BES endpoints have been tested for
interoperability against several grid software systems.  You will need
to contact the developer/vendor of your system to determine if their
software is compatible with GenesisII.  Depending on your system works,
you will either need to contact your grid system administrator to have
him/her add the Futuregrid GenesisII BES endpoints or you will need to
provide a reference to the endpoints to the client tooling.  In either
case, the information you or your grid administrator needs is included
in the section above (`Connecting to the GenesisII BES
Endpoints <#Connecting%20To%20GenesisII%20BES%20Endpoints>`__).


Using The GenesisII Client
--------------------------

GenesisII has a rich client package available for Windows, MacOS and
LINUX platforms that includes UNIX-style command line tools as well as
several graphical user interface tools.  The University of Virginia
maintains a grid called the Cross Campus Grid (XCG) that already
includes the FurtureGrid GenesisII BES endpoints in it - already
configured and ready to go.  To get started, the first step is to
download and install the GenesisII/XCG installation package.

Acquiring GenesisII Client Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GenesisII/XCG installers are available at
`http://www.cs.virginia.edu/~vcgr/wiki/index.php/Genesis\_II\_Downloads <http://www.genesis2.virginia.edu/wiki/Main/Downloads>`__.
Choose the platform that matches the machine/OS where you will be
running your client and click the corresponding "Download" link to
download the installer.

Linux
^^^^^

The Linux installer is a shell script named XCG-Installer.sh encoded
with the entire GenesisII package inside.  Simply execute the shell
script (./XCG-Installer in proper directory) to begin installation. 
Follow the steps here in answering the installation questions.


Windows
^^^^^^^

The Windows installer is an executable named XCG-Installer.exe. 
Simply run it like any other executable (e.g. double-clicking) and
follow the steps here in answering the installation questions.

Note that currently, the GenesisII software is only tested for
Windows XP.  However, our early experience with Windows 7 (and Vista)
indicates that the client installation will work fine as long as you
install GenesisII in a folder that does not have special security
meaning to Windows (such as your Documents and Settings directory or
C:\\).

MacOS
^^^^^

The MacOS installer is a dmg file named XCG-Installer.dmg encoded with
the entire GenesisII package inside.  Simply execute the dmg file (e.g.
by double clicking) to begin installation.  Follow the steps here in
answering the installation questions.


Installing the GenesisII/XCG Client Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The installation process requires answering a few questions about
license agreement and configuration options.

-  **Agree to license terms**.  The GenesisII license follows the Apache
   License model.  For command line versions, this may require hitting
   enter a number of time to scroll the license text on the screen.
-  **Select the directory for the installation**.  In most cases the
   default is sufficient, though you can feel free to change it.  As
   noted earlier, Windows Vista and 7 users should choose a directory
   that is not given special protection from those operating systems. 
   For example, the default C:\\Program Files is given special treatment
   and blocks writes made there by the software.  This causes GenesisII
   problems because GenesisII has a patch mechanism built which needs to
   overwrite package files in the installation directory.  For Windows
   7/Vista, we recommend a directory within your user folder.
-  **Client v Full Container Install.**  The entire GenesisII software
   package is included in the installer.  This includes both client-side
   command line tools and GUIs as well as server-side programs for
   installing grid servers.  We recommend installing the client only
   version.  Select XCG Client Install option.  
-  **Shortcuts/Start Menu options.**  For Windows users, you can select
   whether to create a shortcut for all users (default yes), create a
   start menu item for GenesisII (default: yes) and pick a name for the
   start menu folder (default: GenesisII).  The defaults are
   recommended, but you can change if you like.  For Linux and MacOS,
   you can choose whether to create shortcuts in the standard binary
   directory (Linux: /usr/bin; MacOS: /Applications/?).  Unless you are
   installing with root privileges, we recommend choosing "No" to this
   question.

That's it.  Since the installer is specific to the UVA Cross Campus
Grid, you not only have GenesisII successfully installed, but you have
also configured your system to connect to the XCG.


Getting Started
---------------

To get started using the XCG, you will need an XCG account - which is
**not** the same as your local machine account or your FutureGrid
resource account. To request an XCG account, fill out the XCG user
application form located at
`http://www.cs.virginia.edu/~vcgr/userrequest <https://www.cs.virginia.edu/~vcgr/userrequest/>`__.

Once you have an account and have the appropriate GenesisII software
installed, you are ready to start a GenesisII grid shell and login.

Start Grid Shell
~~~~~~~~~~~~~~~~

To start a grid shell start the "grid" executable from the installation
directory.

Windows
^^^^^^^

Double click the "grid" file in the installation directory;
or
Open a Windows command line window, cd to the installation directory,
and enter the grid.exe command.

Linux or MacOS
^^^^^^^^^^^^^^

If you have a Window manager running, double click on the grid binary
in the installation directory
or
Open a shell, cd to the installation directory and enter the grid
command

.. code:: _fck_mw_lspace

     $> cd <installation directory>
     $> grid

**LogIn**
Once you have a grid shell open, you need to be logged into your XCG
grid account in order to perform most useful commands. First check to
see if you are already logged in - the "whoami" command prints out your
current credentials. If you are not logged in, it should look like this
(the Client Tool Identity is an automatically generated certificate used
by GenesisII client commands and does not carry any authentication
information):

.. code:: _fck_mw_lspace

     $XCG> whoami
     Client Tool Identity:
        "Client Cert EFC05BB7-295A-B313-E0E0-95A8CE61EB68"
     $XCG>

To login, use the "login" command.  The syntax is "login
--username=<grid user name>".  After running this command, a popup
window will prompt you for your password

.. code:: _fck_mw_lspace

     $XCG> login --username=jfk3w
     $XCG> whoami
     Client Tool Identity:
        "Client Cert EFC05BB7-295A-B313-E0E0-95A8CE61EB68"
     "jfk3w" -> "Client Cert EFC05BB7-295A-B313-E0E0-95A8CE61EB68"
     "uva-idp-group.2010" -> "Client Cert EFC05BB7-295A-B313-E0E0-95A8CE61EB68" 
     $XCG> 

The output from the post-login whoami command indicates that I have 2
new certificates - one that asserts that I am user jfk3w, and another
that asserts that I have the permissions of the group
"uva-idp-group.2010".  The XCG uses the uva-idp-group.2010 to set
permissions for all approved XCG users.  Your membership in this group
is done by XCG administrators when you account is created.  If you later
create new groups or are added to other existing groups, your login will
automatically acquire the extra credentials to assert that you are a
member of that group (assuming the group allows you access).

Running Jobs
~~~~~~~~~~~~

To learn how the basics about executing and monitoring jobs using
GenesisII and the XCG, please refer to `XCG
Tutorial <https://portal.futuregrid.org/sites/default/files/XCG%20Tutorial.pdf>`__
document.

Getting Help
------------

To get help using the XCG send email to the UVA Computational Science
and Engineering (UVACSE) group at uvacse@virginia.edu.  You can also use
the `GenesisII web
site <http://www.genesis2.virginia.edu/wiki/Main/HomePage>`__ and the
`XCG web
site <http://www.cs.virginia.edu/~xcgshare/wiki/index.php/Homepage>`__
to look at further documentation and FAQs

+-------------------------------------------------------------------------------------------------------------------+-----------+
| Endpoints                                                                                                        | Size      |
+===================================================================================================================+===========+
| `india-epr-Nov-01-2011.txt <https://portal.futuregrid.org/sites/default/files/india-epr-Nov-01-2011.txt>`__       | 7.8 KB    |
+-------------------------------------------------------------------------------------------------------------------+-----------+
| `sierra-epr-Mar-22-2012.txt <https://portal.futuregrid.org/sites/default/files/sierra-epr-Mar-22-2012_0.txt>`__   | 7.8 KB    |
+-------------------------------------------------------------------------------------------------------------------+-----------+
| `alamo-epr-Mar-22-2012.txt <https://portal.futuregrid.org/sites/default/files/alamo-epr-Mar-22-2012_0.txt>`__     | 7.82 KB   |
+-------------------------------------------------------------------------------------------------------------------+-----------+
| `hotel-epr-Apr-24-2012.txt <https://portal.futuregrid.org/sites/default/files/hotel-epr-Apr-24-2012.txt>`__       | 7.86 KB   |
+-------------------------------------------------------------------------------------------------------------------+-----------+
