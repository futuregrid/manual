.. _s-vine:

ViNe
========================

ViNe is available to FutureGrid users on the foxtrot and sierra
clusters, and can be deployed in any cloud on virtual machines (requires
overlay network knowledge).

Overview:
    ViNe is a project developed at University of Florida that
    implements routing and other communication mechanisms needed to
    deploy a user-level virtual network. ViNe is particularly
    appealing for cloud computing because it allows the establishment
    of wide-area virtual networks supporting symmetric communication
    among public and private network resources (even when they are
    behind firewalls), does not require changes to either the physical
    network or the OS of machines, and has low virtualization
    overheads. ViNe can provide communication among FutureGrid and
    external resources (including those with private IP addresses)
    without the need to reconfigure the (FutureGrid) physical network
    infrastructure.

Prerequisites:
    In order for a host to participate in ViNe overlays, users need
    root privilege to adjust operating system routing
    tables. Currently, users can get root privilege on the virtual
    machines (VMs) started on FG clouds. ViNe routers are available on
    foxtrot and sierra, and VMs started through Nimbus can be
    configured to participate on ViNe overlays.

Setup:
    All VMs must be members of ViNe overlays, independently wether
    they are on public or private networks. In order to enable the
    ViNe communication, the following command needs to be executed on
    participating VMs::

        wget -P /tmp -N http://www.acis.ufl.edu/vine/enablevine.php
        . /tmp/enablevine.sh

Tutorial:
    A step-by-step tutorial on connecting VMs to ViNe overlays can be
    found in the section :ref:`s-vine-overlay`.


