Getting Started
===============

.. sidebar:: Page Contents

   .. contents::
      :local:

.. todo:: put the links to the sections here

In order for you to gain access to the FutureGrid resources, you need to
follow real simple steps:

#. Create a FutureGrid portal account
#. Create or join a project
#. Upload your SSH key
#. Explore our Manual

We will introduce these steps in more detail next.



Step 4: Explore the Documentation
---------------------------------

Once you have access to FutureGrid resources, a good place to start
learning about how to use FutureGrid are the tutorials, specifically the
following:

-  The `Manual <http://portal.futuregrid.org/manual>`__ for detailed
   information

Our manual will include a variety of topics that are of interest to our
users from many different user communities. It would be a disservice to
you to just list a view of them. Hence we provide you with a convenient
link to our table of contents. Please note that the manual also contains
links to our tutorials and our MOOC.

-  `Manual Table of
   Contents <https://portal.futuregrid.org/manual/toc>`__

It will be also easy for you to search for some topics in our search box
at the top of the Web page.




Training and Education
----------------------

FutureGrid provides training and educational materials through manuals
and tutorials.

FutureGrid leverages technologies contributed by its partners and by the
open-source community in the packaging, configuration, and deployment of
virtual clusters - including the plug-and-play, self-configuring Grid
appliance, the Nimbus science cloud middleware, the IPOP/GroupVPN
self-configuring virtual network, and the ViNe virtual network.

For links to the initial appliance-based FutureGrid tutorials, see the
FutureGrid `Education and Outreach
page <https://portal.futuregrid.org/outreach>`__. Additionally, for
video tutorials on the use of the appliances, see the `Grid appliance
YouTube
channel <http://www.youtube.com/acisp2p#p/c/D77781CEF51F72F3>`__.

 

`‹ Quickstart <https://portal.futuregrid.org/gettingstarted>`__

Guide to Using the FutureGrid Portal
====================================

Functions of the FutureGrid Portal
----------------------------------

 
The FutureGrid portal aims to:

#. Be the definite source for information about FutureGrid (manuals,
   papers, forums, FAQ, ...)
#. Allow management of your FG accounts (portal, services, and
   resources)
#. Allow management of your futuregrid projects
#. Allow management of FG experiments
#. Allow the dynamic provisioning via RAIN 

A FutureGrid User Dashboard 
----------------------------

After login, you will be redirected to a dashboard-like page (go to the
menu Accounts -> My Portal Account), where you will see the following:

#. A list of useful links, including links to profile, account, SSH key,
   and OpenID management information.
#. A projects summary section that lists the summarized information
   about projects that you are the owner of, that you manage, that you
   are member of, and that you support as a FutureGrid expert,
   respectively. Clicking the project title will bring you to the
   project detail info page. For those projects that you own or manage,
   an 'edit' link is also there so you can quickly update the project
   information.
#. A 'My Content' section where the content that you are responsible for
   maintaining (and/or that you have contributed) is listed. This gives
   a convenient view so you can easily go back to the content and update
   it.
#. A 'My Publications' section that lists your publications.

Update Project Information and Add Results
------------------------------------------

Another frequently used feature is the ability to update your project
information (e.g., add project members) and fill in results in the
'Project Results' section. You can do so only when you are either the
owner of the project or the project manager (if the owner has delegated
that to you). By following the links provided in the 'Dashboard'
section, you can review and edit the project information.

To add a user to your project as a member, the user must have a
FutureGrid portal account first. Then, while editing the project, you
can type a user's first name, and the suggestion feature will pop up
with the user's username to be added. If you have many members to add,
click the 'Add another item' in the 'Project Members' section to add
more. See also `this
FAQ <https://portal.futuregrid.org/how-can-i-add-people-project>`__.

For updating your project results, there is a 'Project Results' section
with a 'Results' window that supports WYSIWYG editing. It supports
simple formatted text, embedded images, etc. For text, you can edit
directly in the window, or copy the content you developed in your
favorite editor and paste the content in the edit window. In the case of
images, you'll need to upload the image to the server first, and then
insert it to the window, or alternatively refer to an external URL for
an image hosted somewhere else.

For more detailed info on how to include an image, please see `this
FAQ <https://portal.futuregrid.org/how-upload-andor-include-image-while-creating-pagenews-etc>`__.

Contribute to the FutureGrid Community
--------------------------------------

The FutureGrid portal also provides its users a place where they can
contribute to the community by sharing their ideas, research topics, FG
experience, etc.; in this way people can learn from you, and also you
can learn from others. Emphasizing user participation and
collaboration is one of the main goals shaping the portal to its current
state.

You can contribute by `creating a 'Community
Page' <https://portal.futuregrid.org/node/add/page-community>`__. You
can find the link in the left side navigation block, under the 'Create
content' menu. After entering the edit page, you'll see a 'Title' text
box, where you put the content/article title, and a 'Body' window where
you put the content. Once again, it supports formatted text and embedded
images, etc.

You can cite FutureGrid references also, by enclosing a citekey within
the 'bib' tag as stated under the editor window (NOTE: Please use '[]'
instead of '<>'), where CITEKEY could be found in the `biblio
page <https://portal.futuregrid.org/biblio>`__ (the content within but
not including the '[ ]').

An example of a user contributed page can be found
`here <https://portal.futuregrid.org/contrib/testexample-page-user-contributed-page>`__.

File Upload and Attachment to a Page
------------------------------------

Please see `this
FAQ <https://portal.futuregrid.org/faq/how-uploadattach-file-page>`__
for instructions on file upload.




Alamo
=====

Alamo is a 96 node Dell cluster running 2.66 GHz Intel Xeon X5550
processors.  The OS is CentOS 5.8 and 6.3.  It runs Torque and Moab for
scheduling.  Alamo has a QDR IB interconnect and 15 TB of attached disk
storage.   Alamo is partitioned into different resources for Nimbus and
HPC.  See the Alamo hardware page for more
detail: `https://portal.futuregrid.org/hardware/alamo <https://portal.futuregrid.org/hardware/alamo>`__
.

**Nimbus partition -** see nimbus
documentation: `https://portal.futuregrid.org/tutorials/nimbus <https://portal.futuregrid.org/tutorials/nimbus>`__

**HPC partition**

Max cores 584.  Submit
`ticket <http://%20https://portal.futuregrid.org/help>`__ if you need to
run larger than the 320 limit per user. 

Available queues: 
   short - 24 hours runtime limit
   long - 72 hours runtime limit

After registering your .ssh key on the portal, go to
`https://portal.futuregrid.org/manual/access <https://portal.futuregrid.org/manual/access>`__
.

If you key has been uploaded, you can ssh to the login node using the
following command. 
**Note**: If you are prompted for a password, your account has not
been set up correctly or the .ssh key has not been propagated. 

  ssh alamo.futuregrid.org

To submit a test job use the qsub command.

ex.  qsub -N job\_name -l nodes=1 -q short  job\_script

-  qstat - show current jobs in the queue with status
-  showq - show current running and queued jobs and job id
-  checkjob -v <jobid>   - more detailed information about your job

Applications are available via modules.  To see a list of available
applications:
  module avail

File systems:
   /home   - Quota enforced home directory, backed up nightly.
   /N/work - 6.3 TB work directory, not backed up. NFS mounted from
login node. 
   /N/images - 11 TB directory for system images, not backed up. NFS
mounted from login node.

Administrator: David Gignac
For issues or questions please
use `https://tickets.futuregrid.org <https://tickets.futuregrid.org>`__
. You can conveniently submit a ticket
via `https://portal.futuregrid.org/help <https://portal.futuregrid.org/help>`__.
To look at your previously submitted tickets you can
use `https://portal.futuregrid.org/tickets <https://portal.futuregrid.org/tickets>`__
.

  



IaaS - Infrastructure as a Service
==================================

This chapter contains information in regards to Infrastructure as a
Service offerings on FutureGrid

Using IaaS Clouds on FutureGrid
===============================

Infrastructure-as-a-Service (IaaS) cloud computing encompasses
techniques that have driven major recent advances in information
technology supporting elastic, on-demand, "pay as you go" computing as a
service. Key technologies behind IaaS cloud computing are resource
virtualization, as well as cloud middleware that enables the management
of clusters of virtualized resources through service interfaces. 

The FutureGrid testbed provides capabilities that allow users to
experiment with open-source cloud middleware and virtualization
platforms, and there are different ways you may want to use these
platforms in the testbed. This page guides you in selecting from
FutureGrid capabilities best suited to your goals, and provides links to
respective tutorials:







Management Services
===================

FutureGrid contains a number of interresting management services. This
includes image management services to deploy and provision images onto
bare metal or virtualized machines as well as experiment management that
allows the creation of easy to use workflows to run repeatable
experiments on FutureGrid. These services are curently under development
and you are welcome to join the development teams by contacting
`laszewski@gmail.com <mailto:laszewski@gmail.com>`__


Commandline clients
==================================================================

Install the nova client::

   pip install -e git+https://github.com/openstack/python-novaclient.git#egg=python-novaclient

Get your novarc file::

   todo

Source your .novarc file::

   $ source ~/.futuregrid/novarc

No the first nova command::

   $ nova list 


.. |image0| image:: https://portal.futuregrid.org/sites/default/files/u30/fg-logo-md.gif
.. |image4| image:: https://portal.futuregrid.org/sites/default/files/resize/images/FutureGrid_iDataPlex_Cray_IU-sm-640x425.jpg
.. |image5| image:: https://portal.futuregrid.org/sites/default/files/resize/images/Cray_XT5m_Front_closed-small-427x640.jpg
.. |image6| image:: https://portal.futuregrid.org/sites/default/files/images/FutureGrid%20Logocal%20v3.png
.. |image7| image:: https://portal.futuregrid.org/sites/default/files/resize/images/Juniper%20EX8208-140x184.png
.. |image8| image:: https://portal.futuregrid.org/sites/default/files/u23/futuregrid-physical.png
.. |image9| image:: https://portal.futuregrid.org/sites/default/files/u23/futuregrid-topology.png
.. |image10| image:: https://portal.futuregrid.org/sites/default/files/images/Spirent%20XGEM.png
.. |image11| image:: https://portal.futuregrid.org/sites/default/files/images/FutureGrid%20Logocal%20v3.png
.. |image12| image:: https://portal.futuregrid.org/sites/default/files/images/status_incapart.PNG
   :target: http://inca.futuregrid.org:8080/inca/jsp/partitionTable.jsp
.. |image13| image:: https://portal.futuregrid.org/sites/default/files/ScreenSnapz.jpg
   :target: http://inca.futuregrid.org:8080/inca/jsp/status.jsp?queryNames=Health&xsl=table.xsl&resourceIds=FutureGrid
.. |image14| image:: https://portal.futuregrid.org/sites/default/files/ganglia.png
   :target: http://ganglia.futuregrid.org
.. |image15| image:: https://portal.futuregrid.org/sites/default/files/images/large_status_nocmap.PNG
   :target: http://noc.futuregrid.org
.. |image16| image:: https://portal.futuregrid.org/sites/default/files/u23/Screen%20shot%202011-01-14%20at%207.48.06%20PM.png
   :target: http://inca.futuregrid.org
.. |image17| image:: https://portal.futuregrid.org/sites/default/files/u23/Screen%20shot%202011-04-07%20at%203.23.05%20PM.png
   :target: https://portal.futuregrid.org/monitoring/cloud
.. |image18| image:: https://portal.futuregrid.org/sites/default/files/screenshot-for-status-small.png
   :target: https://portal.futuregrid.org/metrics
.. |image19| image:: https://portal.futuregrid.org/sites/default/files/fg-sys-sw-ver.PNG
   :target: http://inca.futuregrid.org:8080/inca/HTML/rest/HPC/FutureGrid
.. |image20| image:: https://portal.futuregrid.org/sites/default/files/u15/nimbus-usage.png
   :target: http://inca.futuregrid.org/nimbus-stats


.. |image31| image:: https://portal.futuregrid.org/sites/default/files/images/open_file.png
.. |image32| image:: https://portal.futuregrid.org/sites/default/files/images/cancel_loading_resize.png
.. |image33| image:: https://portal.futuregrid.org/sites/default/files/images/Startup.png
.. |image34| image:: https://portal.futuregrid.org/sites/default/files/images/Display_arranging_a.png
.. |image35| image:: https://portal.futuregrid.org/sites/default/files/images/Display_arranging_b.png
.. |image36| image:: https://portal.futuregrid.org/sites/default/files/images/Custom_arrangement.png
.. |image37| image:: https://portal.futuregrid.org/sites/default/files/images/close_display.png
.. |image38| image:: https://portal.futuregrid.org/sites/default/files/images/Undocking_1.png
.. |image39| image:: https://portal.futuregrid.org/sites/default/files/images/Undocking_2.png
.. |image40| image:: https://portal.futuregrid.org/sites/default/files/images/Resize_labels.png
.. |image41| image:: https://portal.futuregrid.org/sites/default/files/images/Zooming.png
.. |image42| image:: https://portal.futuregrid.org/sites/default/files/images/Zoom_toolbar.png
.. |image43| image:: https://portal.futuregrid.org/sites/default/files/images/icon_master_tl.png
.. |image44| image:: https://portal.futuregrid.org/sites/default/files/images/icon_process_tl.png
.. |image45| image:: https://portal.futuregrid.org/sites/default/files/images/icon_counter_tl.png
.. |image46| image:: https://portal.futuregrid.org/sites/default/files/images/icon_radar.png
.. |image47| image:: https://portal.futuregrid.org/sites/default/files/images/icon_function_summ.png
.. |image48| image:: https://portal.futuregrid.org/sites/default/files/images/icon_message_summ.png
.. |image49| image:: https://portal.futuregrid.org/sites/default/files/images/icon_process_summ.png
.. |image50| image:: https://portal.futuregrid.org/sites/default/files/images/icon_matrix.png
.. |image51| image:: https://portal.futuregrid.org/sites/default/files/images/icon_calltree.png
.. |image52| image:: https://portal.futuregrid.org/sites/default/files/images/icon_legend.png
.. |image53| image:: https://portal.futuregrid.org/sites/default/files/images/icon_context.png
.. |image54| image:: https://portal.futuregrid.org/sites/default/files/images/icon_marker.png
.. |image55| image:: https://portal.futuregrid.org/sites/default/files/images/Master_timeline.png
.. |image56| image:: https://portal.futuregrid.org/sites/default/files/images/Process_timeline.png
.. |image57| image:: https://portal.futuregrid.org/sites/default/files/images/collectives.png
.. |image58| image:: https://portal.futuregrid.org/sites/default/files/images/burst.png
.. |image59| image:: https://portal.futuregrid.org/sites/default/files/images/marker-multiple.png
.. |image60| image:: https://portal.futuregrid.org/sites/default/files/images/marker-template.png
.. |image61| image:: https://portal.futuregrid.org/sites/default/files/images/io-multiple.png
.. |image62| image:: https://portal.futuregrid.org/sites/default/files/images/io-single.png
.. |image63| image:: https://portal.futuregrid.org/sites/default/files/images/io-single-selected.png
.. |image64| image:: https://portal.futuregrid.org/sites/default/files/images/Counter_data_timeline.png
.. |image65| image:: https://portal.futuregrid.org/sites/default/files/images/performance_radar_find_function.png
.. |image66| image:: https://portal.futuregrid.org/sites/default/files/images/performance_radar_set_counter.png
.. |image67| image:: https://portal.futuregrid.org/sites/default/files/images/Call_tree.png
.. |image68| image:: https://portal.futuregrid.org/sites/default/files/images/Function_summary.png
.. |image69| image:: https://portal.futuregrid.org/sites/default/files/images/Process_summary.png
.. |image70| image:: https://portal.futuregrid.org/sites/default/files/images/Messagesummary.png
.. |image71| image:: https://portal.futuregrid.org/sites/default/files/images/Communication_matrix_view.png
.. |image72| image:: https://portal.futuregrid.org/sites/default/files/images/Function_legend.png
.. |image73| image:: https://portal.futuregrid.org/sites/default/files/images/Marker_view.png
.. |image74| image:: https://portal.futuregrid.org/sites/default/files/images/Context_view.png
.. |image75| image:: https://portal.futuregrid.org/sites/default/files/images/context_compare.png
.. |image76| image:: https://portal.futuregrid.org/sites/default/files/images/process_filter.png
.. |image77| image:: https://portal.futuregrid.org/sites/default/files/images/pref_general.png
.. |image78| image:: https://portal.futuregrid.org/sites/default/files/images/pref_appearance.png
.. |image88| image:: https://portal.futuregrid.org/sites/default/files/resize/euca_fg_login-290x240.png
.. |image89| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/Screen%20Shot%202013-03-06%20at%2012.47.32%20PM-201x200.png
   :target: http://futuregrid.github.com/rain/
.. |image90| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/Screen%20Shot%202013-03-06%20at%2012.51.48%20PM-200x200.png
   :target: http://futuregrid.github.com/rain/quickstart.html
.. |image91| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/Screen%20Shot%202013-03-06%20at%2012.47.32%20PM-201x200.png
   :target: http://futuregrid.github.com/rain/
.. |image92| image:: https://portal.futuregrid.org/sites/default/files/resize/u23/Screen%20Shot%202013-03-06%20at%2012.51.48%20PM-200x200.png
   :target: http://futuregrid.github.com/rain/quickstart.html
.. |:!:| image:: http://www.opennebula.org/lib/images/smileys/icon_exclaim.gif
.. |image94| image:: https://portal.futuregrid.orghttps://portal.futuregrid.org/sites/default/files/resize/myHadoop-300x70.png
.. |Hadoop logo| image:: http://hadoop.apache.org/images/hadoop-logo.jpg
.. |image96| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image97| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image98| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image99| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image100| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image101| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image102| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image103| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image104| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image105| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image106| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image107| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image108| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image109| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image110| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image111| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image112| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image113| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image114| image:: http://www.iterativemapreduce.org/images/imrmodel.png
.. |image115| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image116| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image117| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image118| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image119| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image120| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image121| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image122| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image123| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image124| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image125| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image126| image:: http://www.iterativemapreduce.org/images/bullet.GIF
.. |image127| image:: https://portal.futuregrid.orghttps://portal.futuregrid.org/sites/default/files/u192/start_twister.jpg
.. |image128| image:: https://portal.futuregrid.orghttps://portal.futuregrid.org/sites/default/files/resize/u192/twister_kmeans-906x257.jpg
.. |Cloud site sample layouts.| image:: https://pegasus.isi.edu/wms/docs/4.0/images/fg-pwms-prefio.3.png
.. |image130| image:: https://portal.futuregrid.org/sites/default/files/u30/fg-logo-md.gif
.. |image132| image:: https://portal.futuregrid.org/sites/default/files/u23/summerschool2012.png
   :target: https://portal.futuregrid.org/projects/241
