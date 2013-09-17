Upgrading Nimbus On FG clusters
===============================

.. sidebar:: Page Contents

   .. contents::
      :local:

Disclaimer
----------

This document provides guidelines on how to upgrade Nimbus on
FutureGrid sites.  It is not a definitive guide to upgrading Nimbus
anywhere.  An admin's own skills and intuition should be in full force
while following this guide.  This page should be considered little more
than the notes from one effective upgrade from 2.7 to 2.8.

Upgrading Workspace Service and Cumulus
---------------------------------------

First create a source directory and download the latest Nimbus release
from
`http://www.nimbusproject.org/downloads/ <http://www.nimbusproject.org/downloads/>`__,
and untar the distributions:

::

    mkdir ~/src
    wget http://www.nimbusproject.org/downloads/nimbus-iaas-2.8-src.tar.gz
    tar -xzf nimbus-iaas-2.8-src.tar.gz
    wget http://www.nimbusproject.org/downloads/nimbus-iaas-controls-2.8.tar.gz
    tar -zxf nimbus-iaas-controls-2.8.tar.gz

For convenience set the following variables:

::

    export OLD_NIMBUS=<path to old nimbus install>
    export NEW_NIMBUS=<path to new nimbus install>

Make sure that the old install is not running:

::

    $OLD_NIMBUS/bin/nimbusctl stop

Install the new Nimbus. If you are on an old distribution such as CentOS
5, you might need to set the OLD\_OPENSSL\_VERSION environment variable.
If you run into Java OOM issues, export the following variable: export
ANT\_OPTS=-Xmx1024M. When asked any questions just hit enter:

::

    ./install $NEW_NIMBUS

Run the following commands to transfer over the env. **\*NOTE\*** please
check that you are ok with these commands first, do not blindly copy and
paste them. ***These commands DELETE things!***

::

    rm -rf $NEW_NIMBUS/var/ca
    rm $NEW_NIMBUS/var/hostcert.pem
    rm $NEW_NIMBUS/var/hostkey.pem
    rm $NEW_NIMBUS/var/keystore.jks

    cp $OLD_NIMBUS/nimbus-setup.conf $NEW_NIMBUS/nimbus-setup.conf

    export PREVIOUS_NIMBUS_HOME_VALIDATED=$OLD_NIMBUS
    $NEW_NIMBUS/bin/nimbus-configure --conf $NEW_NIMBUS/nimbus-setup.conf  --import-cumulusdb
    $NEW_NIMBUS/bin/nimbus-configure --conf $NEW_NIMBUS/nimbus-setup.conf --import-prev

    cp $OLD_NIMBUS/services/etc/nimbus/workspace-service/metadata.conf $NEW_NIMBUS/services/etc/nimbus/workspace-service/metadata.conf

Import SSH keys from the Elastic interface:

::

    sqlite3 $OLD_NIMBUS/services/var/nimbus/elastic.db
    sqlite> .output /N/u/nimbus/ssh_keypairs
    sqlite> .dump ssh_keypairs
    sqlite> .quit

    sqlite3 $NEW_NIMBUS/services/var/nimbus/elastic.db
    sqlite> .read /N/u/nimbus/ssh_keypairs
    sqlite> .quit

Manually check the remaining differences in the configuration files. 
The differences will be very site dependent so put on your thinking
cap.  The following script will diff out all the conf files.  Go through
the output and make sure you merge over all the needed changes for your
site

::

    cd $OLD_NIMBUS
    confs=`find . -name '*.conf'`
    for c in $confs
    do
        diff -q -u $OLD_NIMBUS/$c $NEW_NIMBUS/$c

::

    done

Now verify that services/etc/nimbus-context-broker/jndi-config.xml has
the right caCertPath and caKeyPath (in almost every case it will not
have the right values).
Also verify that services/etc/globus\_wsrf\_core/server-config.wsdd
has the right logicalHost.
Also verify the customizations
in services/etc/nimbus/workspace-service/other/authz-callout-ACTIVE.xml
are still enabled (for example cp propagation).

Also check $NEW\_NIMBUS/cumulus/etc/cumulus.ini for the backend
data\_dir if you are using type 'posix' (which you likely are).
And check
$NEW\_NIMBUS/services/etc/nimbus/workspace-service/cumulus.conf for the
cumulus.authz.db and cumulus.repo.dir settings.

Now you must load up the new Nimbus install with the backends from
the old install.  The following python script can help with that task. 
Simply give it two arguments: $OLD\_NIMBUS $NEW\_NIMBUS


`https://raw.github.com/nimbusproject/nimbus/master/docs/src/admin/reload.py <https://raw.github.com/nimbusproject/nimbus/master/docs/src/admin/reload.py>`__

Upgrading Workspace Control
---------------------------

Set up the workspace control nodes by doing the following:

#. Move the old install from /opt/nimbus to /opt/nimbus2.7
#. Create the directory /opt/nimbus2.8 and have it owned by the nimbus
   user and group
#. Create a symlink from /opt/nimbus to /opt/nimbus2.8

Now copy the old working workspace control code from a working VMM
node to the source directory:

::

    scp -r working_node:/opt/nimbus2.7 ~/src/

Just like in the above step, run the following diff script to find
configuration differences, give it the full path to nimbus2.7 as the
first argument and the full path to the new distribution at the second:

::

    cd $1
    confs=`find . -name '*.conf'`
    for c in $confs
    do
        diff -u $1/$c $2/$c

::

    done

Merge all of the differences.  Check out the following files and merge
the differences:

libexec/workspace-control/mount-alter.sh
lantorrent/etc/\*
etc/workspace-control/libvirt\_template.xml

Make sure that everything in nimbus2.7/var/workspace-control/kernels
is also in
nimbus-iaas-controls-2.8/workspace-control/var/workspace-control/kernels

scp everything under nimbus-iaas-controls-2.8/workspace-control to
all VMM nodes:/opt/nimbus/
