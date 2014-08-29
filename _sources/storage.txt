
.. _s-storage:

Storage Services
======================================================================

.. todo:: this section doe snot work at all for me as I can not log in. It does not explain how I get an account to login.

Using Indiana Universities Storage Services from FutureGrid
----------------------------------------------------------------------

FutureGrid does not provide an HPSS server. However, if you have an IU
account (available only for IU faculty, staff, and students), you can
use the following services from india:

* `SDA <http://rc.uits.iu.edu/storage/sda>`__ service
* `HSI <http://rc.uits.iu.edu/storage/hsi>`__, the Hierarchical Storage
Interface client is available in india. 

To use the HSI client on india:

-  First, activate your SDA account as descreibed in the `MDSS Service Starter
   Kit <http://rc.uits.iu.edu/storage/mdss-starter-kit>`__ documentation.
-  Then, from india, load the HSI module as follows::

    $ module load hsi
    hsi version 3.5.3 loaded

-  Connect to the SDA::

    $ hsi -A combo
    Principal: your_iu_userid                                
    [youriuid]Password:                                
    Username: your_iu_userid  UID: 1122636  Acct: 1122636(1122636) Copies: 1 Firewall: off [hsi.3.5.3 Fri Nov 20 10:01:25 EST 2009]
    ?

Your principal is your IU Network ID, and your password is
the IU passphrase.

-  Enable firewall mode; otherwise, you will receive this error::

    put: Error -5 on transfer

    ? firewall -on
    A: firewall mode set ON, I/O mode s<et to extended (parallel=off), autoscheduling currently set to OFF

-  List local folder::

     ? lls
     testfile.txt

-  List the current directory in HPSS::

    ? pwd
    pwd0: /hpss/pathtoyouriuusername

-  For transferring files (*put* and *get*), search the `IU Knowledge
   Base <http://kb.iu.edu/?search=hsi>`__.


