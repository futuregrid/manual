.. _s-hpss:

**********************************************************************
HPSS
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:

**Note**: FutureGrid does not provide an HPSS server. The HSI is used to
access IU's HPSS service from INDIA. This is available only for IU
faculty, staff, and students.

Through the `SDA <http://rc.uits.iu.edu/storage/sda>`__ (formerly known
as MDSS) service, IU provides distributed storage service to faculty,
staff, and graduate students. The
`HSI <http://rc.uits.iu.edu/storage/hsi>`__ (Hierarchical Storage
Interface) client is available in INDIA. To use the HSI client:

-  First, activate your SDA account. Detailed instructions are available
   at IU's `MDSS Service Starter
   Kit <http://rc.uits.iu.edu/storage/mdss-starter-kit>`__ page.
-  Then, from INDIA, load the HSI module as follows::

    $ module load hsi
    hsi version 3.5.3 loaded

-  Connect to the SDA::

    $ hsi -A combo
    Principal: your_iu_userid                                
    [youriuid]Password:                                
    Username: your_iu_userid  UID: 1122636  Acct: 1122636(1122636) Copies: 1 Firewall: off [hsi.3.5.3 Fri Nov 20 10:01:25 EST 2009]
    ?

**Note:**\ Your Principal is your IU Network ID, and your password is
the IU passphrase.

-  Enable firewall mode; otherwise, you will receive this error::

       put: Error -5 on transfer::

    ? firewall -on
    A: firewall mode set ON, I/O mode set to extended (parallel=off), autoscheduling currently set to OFF

-  List local folder::

     ? lls
    testfile.txt

-  List the current directory in HPSS::

    ? pwd
    pwd0: /hpss/pathtoyouriuusername

-  For transferring files (*put* and *get*), search the `IU Knowledge
   Base <http://kb.iu.edu/?search=hsi>`__.
   `‹ Storage </storage>`__ `up </storage>`__ 
