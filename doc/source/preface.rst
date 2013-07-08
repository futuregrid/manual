**********************************************************************
Preface
**********************************************************************

.. sidebar:: Page Contents

   .. contents::
      :local:
 
FutureGrid is a project led by Indiana University and funded by the
National Science Foundation (NSF) to develop a high-performance grid
test bed that will allow scientists to collaboratively develop and
test innovative approaches to parallel, grid, and cloud computing.
FutureGrid will provide the infrastructure to researchers that allows
them to perform their own computational experiments using distributed
systems. The goal is to make it easier for scientists to conduct such
experiments in a transparent manner.

FutureGrid users will be able to deploy their own hardware and software
configurations on a public/private cloud, and run their experiments.
They will be able to save their configurations and execute their
experiments using the provided tools. The FutureGrid test bed is
composed of a high-speed network connecting distributed clusters of high
performance computers. FutureGrid will employ virtualization technology
that will allow the test bed to support a wide range of operating
systems.

The NSF awarded $10.1 million to enable joint development of
FutureGrid through a partnership of Indiana University, Purdue
University, University of California - San Diego, University of
Chicago/Argonne National Labs, University of Florida, University of
Southern California, University of Texas, and the Center for Information
Services and High Performance Computing at Technische Universität
Dresden. The principal investigator is Dr. Geoffrey C. Fox, Director of
the `Digital Science Center <http://pti.iu.edu/dsc>`__ at the
IU `Pervasive Technology Institute <http://pti.iu.edu/>`__.
 

.. _my-how-to-cite:

Citation for Publications
==========================

If you use FutureGrid [1]_, we ask you to include the following
reference in your papers.  

.. [1]   Fox, G., G. von Laszewski, J. Diaz, K. Keahey, J. Fortes, R.
   Figueiredo, S. Smallen, W. Smith, and A. Grimshaw, "FutureGrid - a  reconfigurable testbed for Cloud, HPC and Grid Computing",
   Contemporary High Performance Computing: From Petascale toward
   Exascale, April, 2013. Editor J. Vetter.    :portal:`[pdf]
   <sites/default/files/vonLaszewski-fg-bookchapter.pdf>`
   Contemporary High Performance Computing: From Petascale toward
   Exascale, April, 2013. 

Please also include the following sentence in your Acknowledgement
section [2]_:

.. [2]  This material is based upon work supported in part by the 
  National Science Foundation under Grant No. 0910812.


Acknowledgement
==========================================================

The FutureGrid project is funded by the National Science Foundation
(NSF) and is led by `Indiana
University <http://www.iub.edu/>`__ with `University of
Chicago <http://www.uchicago.edu/index.shtml>`__, `University of
Florida <http://www.ufl.edu/>`__, `San Diego Supercomputing
Center <http://www.sdsc.edu/>`__, `Texas Advanced Computing
Center <http://www.tacc.utexas.edu/>`__, `University of
Virginia <http://www.virginia.edu/>`__, `University of
Tennessee <http://www.utk.edu/>`__, `University of Southern
California <http://www3.isi.edu/home>`__, `Dresden <http://tu-dresden.de/>`__, `Purdue
University <http://www.purdue.edu/>`__, and `Grid
5000 <https://www.grid5000.fr/mediawiki/index.php/Grid5000:Home>`__ as
partner sites. This material is based upon work supported in part by the
National Science Foundation under Grant No. 0910812.

Sponsors
======
The current
sponsors of FutureGrid include:


.. csv-table:: 
   :header: "Logo", "Sponsor"
   :widths: 15, 80

   |image1|, "National Sciens Foundation"
   |image2|, "Lilly Endowment"
   |image3|, "Indiana University Pervasive Technology Institute"

    

About this Manual
======================================================================

This manual is the primary location of  information about FutureGrid
software and services. All FG team members update this manual
regularly. We would also like to **ask the community to help**. If
you would enjoy contributing sections and chapters as part of your
community activities, please contact Gregor
at `laszewski@gmail.com <mailto:laszewski@gmail.com>`__. We welcome
additional contributors and editors to this manual.

Enjoy using and expanding the FutureGrid User Manual!

Gregor von Laszewski


.. |image1| image:: https://portal.futuregrid.org/sites/default/files/u30/nsf.jpg
.. |image2| image:: https://portal.futuregrid.org/sites/default/files/images/lilly_endowment.jpg
.. |image3| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/iu-logo-50x64.jpeg

.. conventions::

Conventions
============

.. role:: rubric

.. highlight:: bash

$
    When showing examples of commands, the $ symbol precedes the
    actual command. So, the other lines are the output obtained after
    executing the command. An example invoking the ls command
    follows::

       $ ls

portalname:
    In some examples we refer to your portal name as |portalname|

localname: 
    In some examples we refer to your local computers name as
    |localname|. Your portal name and your local name may be
    different.

Menu selections:
    :menuselection:`Start --> Programs`

Man page:
    :manpage:`ls(1)`

.. role:: rubric

.. |portalname| replace:: **portalname** :rubric:`red`

.. |localname| replace:: **localname**