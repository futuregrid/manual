**********************************************************************
PAPI
**********************************************************************

.. figure:: images/icl_footer.png
   :align: right

   PAPI

`PAPI <http://icl.cs.utk.edu/papi/overview/index.html>`__ is an acronym
for \ **P**\ erformance \ **A**\ pplication \ **P**\ rogramming \ **I**\ nterface.
The PAPI Project is being developed at the Computer Science Department
of the \ `University of Tennessee’s Innovative Computing
Laboratory <http://icl.cs.utk.edu/>`__. This project was created to
design, standardize, and implement a portable and efficient API
(Application Programming Interface) to access the hardware performance
counters found on most modern microprocessors.  For more information,
please see the user guides listed below.  `Read more
... <http://icl.cs.utk.edu/projects/papi/wiki/User_Guide>`__

Availability
================

PAPI 4.2.0 is available on the Bravo machine and PAPI version 3.6.2.2 is
available on the Xray machine. To load PAPI on Bravo, 'module add papi'
as below::

     $ module add papi
         papi version 4.2.0 loaded

     $ env | grep papi

       MANPATH=/opt/papi-4.2.0/man:/usr/share/man
       LD_LIBRARY_PATH=/opt/papi-4.2.0/lib:/N/u/inca/openssl/lib:
       PATH=/opt/papi-4.2.0/bin:...
       PAPI_ROOT=/opt/papi-4.2.0``

To load PAPI on Xray, type 'module add xt-papi' as below::

     $ module add xt-papi
     $ env | grep PAPI

       PAPI_POST_LINK_OPTS= -L/opt/xt-tools/papi/3.6.2.2/lib -lpapi -lpfm
       PAPI_VERSION=3.6.2.2
       PAPI_INCLUDE_OPTS= -I/opt/xt-tools/papi/3.6.2.2/include``

Our plans are to make PAPI 4.2.0 available on Alamo, India, Sierra, and
Hotel when the machines are upgraded to Redhat 6.

References
===============

-  `User Guide <http://icl.cs.utk.edu/projects/papi/wiki/User_Guide>`__

