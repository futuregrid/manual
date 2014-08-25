.. raw:: html

   <div id="page-wrapper">

.. raw:: html

   <div id="page">

.. raw:: html

   <div id="header">

.. raw:: html

   <div class="section clearfix">

|Home|

.. raw:: html

   <div id="top-menu">

.. raw:: html

   <div id="session">

.. raw:: html

   <div class="region region-session">

.. raw:: html

   <div id="block-menu-menu-user"
   class="block block-menu first last region-odd odd region-count-1 count-7">

.. raw:: html

   <div class="content">

-  `Log in </user/login>`__
-  `Register </user/register>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="search-box">

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="region region-header">

.. raw:: html

   <div id="block-menu-menu-social-network"
   class="block block-menu first last region-odd even region-count-1 count-2">

.. raw:: html

   <div class="content">

-  `Blogger <http://futuregridtestbed.blogspot.com/>`__
-  `Facebook <https://www.facebook.com/pages/FutureGrid/334463263254672>`__
-  `Google <https://plus.google.com/100917243498949712032/posts>`__
-  `Twitter <https://twitter.com/#!/futuregrid>`__
-  `RSS </rss>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="main-wrapper">

.. raw:: html

   <div id="main" class="clearfix with-navigation">

.. raw:: html

   <div id="content" class="column">

.. raw:: html

   <div class="section">

.. raw:: html

   <div class="tabs">

-  `View </tutorials/ga3>`__
-  `What links here </node/677/backlinks>`__

.. raw:: html

   </div>

.. raw:: html

   <div id="content-area">

.. raw:: html

   <div id="node-677" class="node-type-page clearfix">

.. raw:: html

   <div class="content">

 

This is a short tutorial describing how to build an educational virtual
cluster appliance starting from an Ubuntu 10.04 image. A more detailed
description is given at \ `Testing Grid
Appliance <http://www.grid-appliance.org/wiki/index.php/TestingGridAppliance>`__.

 

#. Deploy an Ubuntu 10.04 appliance locally. You can download an Ubuntu
   9.10 VMware appliance \ `here <http://vmplanet.net/node/105>`__, or
   create an instance on FutureGrid of an Ubuntu 10.04 VM.
     
#. Sudo to root and install the grid-appliance baseline package as
   follows:

   #. apt-get install wget
   #. echo "deb http://www.grid-appliance.org/files/packages/deb/ lucid
      contrib" >> /etc/apt/sources.list
   #. wget http://www.grid-appliance.org/files/packages/deb/repo.key
   #. apt-key add repo.key
   #. apt-get update
   #. apt-get install grid-appliance-base
        

#. To configure the appliance to connect to a GroupVPN, use one of the
   following two options:

   #. To use a default GroupVPN and connect to a public pool hosted at
      UF, simply install the package apt-get-install
      grid-appliance-public-pool.
   #. To use our defined Group:

      #. Create a GroupVPN and GroupAppliance
         at \ `http://grid-appliance.org <http://grid-appliance.org/>`__ .
         For an example, see \ `Deploying independent appliance
         pools <http://www.grid-appliance.org/index.php?option=com_content&view=article&id=79&Itemid=76>`__.
      #. In the GroupAppliance interface, download and extract the
         floppy configuration file for a client (floppy.img) and place
         it in/opt/grid\_appliance/etc/floppy.img .
      #. /etc/init.d/grid\_appliance.sh restart 
           

#. Within a few seconds, your appliance should obtain a virtual IP
   address on the virtual network interface tapipop. Once it does, wait
   a few seconds and type condor\_status to check the status of other
   nodes in the pool; you may need to retry a couple of times until
   connected.

.. raw:: html

   </div>

-  `Login </user/login?destination=comment%2Freply%2F677%23comment-form>`__
   or
   `register </user/register?destination=comment%2Freply%2F677%23comment-form>`__
   to post comments

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="navigation">

.. raw:: html

   <div class="section clearfix">

.. raw:: html

   <div class="region region-navigation">

.. raw:: html

   <div id="block-menu-menu-website"
   class="block block-menu first last region-odd odd region-count-1 count-1">

.. raw:: html

   <div class="content">

-  `About </about>`__

   -  `Overview <https://portal.futuregrid.org/about>`__
   -  `Status </status>`__
   -  `News </news>`__
   -  `Documents </documents>`__

      -  `Manuals </manual-old>`__
      -  `Tutorials </tutorials>`__
      -  `Presentations </documents/presentations>`__
      -  `Publications </documents/publications>`__
      -  `Reports </reports>`__

   -  `Sponsors </sponsors>`__
   -  `Staff </staff>`__
   -  `Contact </contact>`__

-  `Support </manual/help-and-support>`__

   -  `Getting Started </manual/gettingstarted>`__
   -  `Accessing FutureGrid </manual/access>`__
   -  `User Manual </manual-old>`__

      -  `Table of Contents </manual/toc>`__

   -  `FAQ </faq>`__

      -  `All Entries <https://portal.futuregrid.org/faq>`__
      -  `Ask a
         Question <https://portal.futuregrid.org/node/add/faq?ask=TRUE>`__

   -  `Tutorials </tutorials>`__

      -  `Summer School <https://portal.futuregrid.org/projects/241>`__

         -  `tumblr <http://sciencecloudsummer2012.tumblr.com/schedule>`__
         -  `Project
            Page <https://portal.futuregrid.org/projects/241>`__
         -  `Forum <https://portal.futuregrid.org/forums/fg-class-and-tutorial-forums/summer-school-2012>`__
         -  `Account
            Creation <https://portal.futuregrid.org/projects/241/register>`__
         -  `Next
            Steps <https://portal.futuregrid.org/projects/241/next>`__
         -  `Participants <https://portal.futuregrid.org/projects/241/participants>`__

   -  `Using IaaS Clouds </using/clouds>`__
   -  `Using Map/Reduce </using/mapreduce>`__
   -  `Forums <https://portal.futuregrid.org/forum>`__
   -  `Outreach <https://portal.futuregrid.org/outreach>`__
   -  `My tickets </tickets>`__
   -  `Submit a ticket </help>`__

-  `Community </community>`__

   -  `Can I Help? </contrib/can-i-help>`__
   -  `Forum </forum>`__
   -  `Add a Community
      Page <https://portal.futuregrid.org/node/add/page-community>`__
   -  `Educational Materials </community_edu_materials>`__
   -  `MOOCs </massive-open-online-courses-moocs-futuregrid>`__
   -  `Multimedia Gallery </gallery/science-cloud-summer-school>`__
   -  `Virtual Appliances </community/appliances>`__

-  `Projects </projects/overview>`__

   -  `Project Lists </projects/all>`__

      -  `All Projects </projects/all>`__
      -  `Course Projects </projects/keywords/course>`__
      -  `XSEDE Projects </projects-xsede>`__

   -  `Project Keywords </projects/keywords>`__
   -  `Statistics <https://portal.futuregrid.org/projects-statistics>`__
   -  `Results </projects/list/results>`__

      -  `How to Report Results? </faq/how-do-i-report-results>`__
      -  `How to Close a
         Project? <https://portal.futuregrid.org/faq/how-do-i-close-project>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="page-bottom">

.. raw:: html

   <div class="region region-page-bottom">

.. raw:: html

   <div id="block-menu_block-1"
   class="block block-menu_block first region-odd odd region-count-1 count-3">

`About </about>`__
------------------

.. raw:: html

   <div class="content">

.. raw:: html

   <div
   class="menu_block_wrapper menu-block-1 menu-name-menu-website parent-mlid-2705 menu-level-1">

-  `Overview <https://portal.futuregrid.org/about>`__
-  `Status </status>`__
-  `News </news>`__
-  `Documents </documents>`__
-  `Sponsors </sponsors>`__
-  `Staff </staff>`__
-  `Contact </contact>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="block-menu_block-3"
   class="block block-menu_block region-even even region-count-2 count-4">

`Support </manual/help-and-support>`__
--------------------------------------

.. raw:: html

   <div class="content">

.. raw:: html

   <div
   class="menu_block_wrapper menu-block-3 menu-name-menu-website parent-mlid-2051 menu-level-1">

-  `Getting Started </manual/gettingstarted>`__
-  `Accessing FutureGrid </manual/access>`__
-  `User Manual </manual-old>`__
-  `FAQ </faq>`__
-  `Tutorials </tutorials>`__
-  `Using IaaS Clouds </using/clouds>`__
-  `Using Map/Reduce </using/mapreduce>`__
-  `Forums <https://portal.futuregrid.org/forum>`__
-  `Outreach <https://portal.futuregrid.org/outreach>`__
-  `My tickets </tickets>`__
-  `Submit a ticket </help>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="block-menu_block-4"
   class="block block-menu_block region-odd odd region-count-3 count-5">

`Community </community>`__
--------------------------

.. raw:: html

   <div class="content">

.. raw:: html

   <div
   class="menu_block_wrapper menu-block-4 menu-name-menu-website parent-mlid-13995 menu-level-1">

-  `Can I Help? </contrib/can-i-help>`__
-  `Forum </forum>`__
-  `Add a Community
   Page <https://portal.futuregrid.org/node/add/page-community>`__
-  `Educational Materials </community_edu_materials>`__
-  `MOOCs </massive-open-online-courses-moocs-futuregrid>`__
-  `Multimedia Gallery </gallery/science-cloud-summer-school>`__
-  `Virtual Appliances </community/appliances>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="block-menu_block-5"
   class="block block-menu_block last region-even even region-count-4 count-6">

`Projects </projects/overview>`__
---------------------------------

.. raw:: html

   <div class="content">

.. raw:: html

   <div
   class="menu_block_wrapper menu-block-5 menu-name-menu-website parent-mlid-1295 menu-level-1">

-  `Project Lists </projects/all>`__
-  `Project Keywords </projects/keywords>`__
-  `Statistics <https://portal.futuregrid.org/projects-statistics>`__
-  `Results </projects/list/results>`__

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div id="footer">

.. raw:: html

   <div class="section">

.. raw:: html

   <div id="footer-message">

|image1|\ The FutureGrid project is funded by the National Science
Foundation (NSF) and is led by `Indiana
University <http://www.iub.edu/>`__ with `University of
Chicago <http://www.uchicago.edu/index.shtml>`__, `University of
Florida <http://www.ufl.edu/>`__, `San Diego Supercomputing
Center <http://www.sdsc.edu/>`__, `Texas Advanced Computing
Center <http://www.tacc.utexas.edu/>`__, `University of
Virginia <http://www.virginia.edu/>`__, `University of
Tennessee <http://www.utk.edu/>`__, `University of Southern
California <http://www3.isi.edu/home>`__,
`Dresden <http://tu-dresden.de>`__, `Purdue
University <http://www.purdue.edu/>`__, and `Grid
5000 <https://www.grid5000.fr/mediawiki/index.php/Grid5000:Home>`__ as
partner sites. This material is based upon work supported in part by the
National Science Foundation under Grant No. 0910812.
 |image2|\ Futuregrid is a resource provider for
`XSEDE <https://www.xsede.org/>`__.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </div>

.. |Home| image:: /sites/all/themes/fgtheme/logo.png
   :target: /
.. |image1| image:: /sites/default/files/images/nsf-logo.png
   :target: http://www.tacc.utexas.edu/
.. |image2| image:: /sites/default/files/u876/xsede-logo.png
