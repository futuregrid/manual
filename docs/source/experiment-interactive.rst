**********************************************************************
Interactive Experiment Management
**********************************************************************

One of the goals of FutureGrid is to allow you to easily execute
distributed experiments. This tutorial describes a few tools that we
provide to help you do this interactively from the command line.

The Host List Manager is a simple set of command line programs that
allow you to manage lists of hosts. The tool automatically gathers
information about hosts provisioned to you via Torque or Nimbus on
FutureGrid and you can also manually inform the tool about available
hosts (e.g. non-FutureGrid systems). You organize the hosts into sets
and the lists of hosts in each set can be provided to tools that execute
commands on many systems at once.

An example of such a parallel execution tool is
`TakTuk <http://taktuk.gforge.inria.fr/>`__. TakTuk executes commands
that you specify on sets of hosts and tries to optimize the amount of
time it takes to start these commands so that it is feasible to have
large host sets.

TakTuk and the Host List Manager have been installed on FutureGrid
login nodes.

Host List Manager
======================================================================

Host List Manager Setup
-----------------------

The Host List Manager is currently installed on the Alamo, Hotel,
India, and Sierra clusters. This tool requires two things from you so
that it can automatically discover the FutureGrid resources that are
provisioned to you. First, it needs access to your ssh key. This allows
the tool to ssh to FutureGrid login nodes and query Torque. For
interactive use, the recommended way to accomplish this is to use an
ssh-agent on your workstation and then forward authentication requests
to that agent.

On Windows, your favorite telnet/ssh program typically includes
running an ssh-agent as an option or has a plugin to do this. See the
documentation for your program on how to enable it. OS X users can use
the ssh-agent and ssh-add commands directly or convenience programs such
as `SSH Agent <http://www.phil.uu.nl/~xges/ssh/>`__. You can then enable
forwarding of authentication to your agent by logging in to Alamo with
the -A option to ssh::

    workstation$ ssh -A alamo.futuregrid.org

If you are a Linux user, you can again use ssh-agent and ssh-add, but
programs such as the Gnome Terminal will do this for you automatically.
You enable forwarding of authentication requests to your agent by sshing
to alamo using the -A option. You can test that you have your ssh-agent
setup correctly by sshing to alamo and then sshing to any other
FutureGrid login node. If you are not asked for a password, your
configuration is correct.

The Host List Manager also requires access to your Nimbus client
installation so that it can determine what Nimbus virtual machines have
been provisioned to you. You should therefore install and test the
Nimbus client in your account on Alamo using the instructions from the
`Nimbus Tutorial <https://portal.futuregrid.org/tutorials/nimbus>`__.
You may find it convenient to add the bin directory of the Nimbus client
install to your $PATH in one of your shell startup scripts (e.g.
$HOME/.profile).

Finally, before you begin to use the Host List Manager, it must be in
your environment. To do this, execute::

    alamo$ module load hostlists

Provisioning Hosts
------------------

The Host List Manager doesn't provision hosts for you so you need to do
this yourself. There are currently three ways to provision hosts that
are understood by the Host List Manager. The first method is to submit
jobs to Torque. These jobs don't need to do anything - they just claim
the nodes for you. You can therefore qsub a submit script such as the
one below::

    #!/bin/bash

    #PBS -N provision
    #PBS -l nodes=4:ppn=8
    #PBS -l walltime=04:00:00

    /bin/sleep 14400

Note that Torque will reclaim nodes allocated to your job when your
submit script ends. The script above therefore includes a sleep to avoid
that situation. See the Section :ref:`s-hpc` for more
information on how to use Torque.

The second provisioning method that the Host List Manager understands
is Nimbus. If you use the Nimbus cloud-client.sh to start virtual
machines, the Host List Manager will discover them. **Note that you must
use the Nimbus client install on the same system as the Host List
Manager and the Host List Manager must know about this Nimbus client
install.**\ This is required for the manager to correctly discover your
Nimbus virtual machines - Nimbus stores some information about your
provisioned virtual machines in the client directory.

The third provisioning method that the Host List Manager understands
is manual provisioning. This simply means provisioning hosts via some
other mechanism (e.g. submitting a job to a non-FutureGrid cluster,
requesting a virtual machine on a non-FutureGrid cloud, or even
including servers from your project) and manually informing the Host
List Manager about them.

Managing Host Lists
-------------------

The first command to run is hupdate. This command updates your local
cache of information about hosts that FutureGrid has provisioned to you
and since this is the first hostlists command that you've executed, it
will setup your local configuration (in $HOME/.hostlists). If this
command works successfully, it will produce no output. However, there
are a few problems that can occur:

-  If the output includes "Password:", then your ssh key is not setup
   correctly. Please see the Setup section above.
-  If you see the error "Didn't find your Nimbus client directory" and
   you have installed the Nimbus, the rest of the error message gives
   you two options on how to resolve this problem: Either add the bin
   directory of your Nimbus client to $PATH or add the path to your
   Nimbus client directory to the nimbus section in your
   $HOME/.hostlists/manager.cfg file.

One note is that you do not typically need to execute hupdate. The
other programs that make up this tool will invoke hupdate if the local
cache of information has not been updated recently. However, you may
want to run hupdate yourself to force an update in some situations (e.g.
when you know that resources have just been provisioned to you) rather
than to wait for the next automatic execution.

The primary command for examining the hosts that are available to you
is hshow. The basic command provides a summary of the hosts available,
one per line::

    alamo$ hshow
    ---------------------------------------------------------------
    |         Host Name          |     Available Until     | Tags |
    ---------------------------------------------------------------
    |  c037.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |      |
    |  c070.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |      |
    |  c033.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |      |
    |  c026.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |      |
    | i58r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT |      |
    | i57r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT |      |
    | i56r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT |      |
    | i55r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT |      |
    ---------------------------------------------------------------

The long (-l) output provides additional information.

You can manually manage hosts using the hmanage command. This command
can be used to add (-a), modify (-m), and remove (-r) hosts to your
local cache. The main use for this command is to manage non-FutureGrid
systems in your host lists. For example, to add a host that is running a
service that you have access to for 2 hours for stress testing::

    alamo$ hmanage -a -b 2011-06-30T13:30:00 -d 02:00:00 -n info2.dyn.teragrid.org

These hosts will appear in the output of hshow::

    alamo$ hshow
    ---------------------------------------------------------------
    |         Host Name          |     Available Until     | Tags |
    ---------------------------------------------------------------
    |  c037.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |      |
    |  c070.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |      |
    |  c033.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |      |
    |  c026.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |      |
    | i58r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT |      |
    | i57r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT |      |
    | i56r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT |      |
    | i55r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT |      |
    |     info2.dyn.teragrid.org | 2011-06-30T15:30:00 CDT |      |
    ---------------------------------------------------------------

The hmanage command is also used with the "-m -u USER" options to set
alternative user names to use on hosts discovered by hupdate (for
example, to set the username to use on a virtual machine). Note that for
automatically discovered hosts, you can only use hmanage to change the
username to be used on that host.

The command that you will use to organize hosts into groups is htag.
This command allows you to associate zero or more tags with each host.
The Host List Manager generates a host list for each tag. htag can be
used to add (-a), remove (-r), or modify (-m) the tags associated with
one or more hosts. For example, you can tag one system as the server,
and the other systems as clients::

    alamo$ htag -a -t server -n info2.dyn.teragrid.org
    alamo$ htag -a -t client -n "\S+.futuregrid.org"


Note that the htag command allows you to specify hosts with exact
names or with Python-style regular expressions. You can also associate
more than one tag per host::

    alamo$ htag -a -t client-texas -n "\S+.alamo.futuregrid.org"
    alamo$ htag -a -t client-indiana -n "\S+.iu.futuregrid.org"


And these tags are visible in the output of hshow::

    alamo$ hshow
    --------------------------------------------------------------------------------
    |         Host Name          |     Available Until     |          Tags         |
    --------------------------------------------------------------------------------
    |  c037.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |   client client-texas |
    |  c070.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |   client client-texas |
    |  c033.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |   client client-texas |
    |  c026.alamo.futuregrid.org | 2011-06-30T18:38:17 CDT |   client client-texas |
    | i58r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT | client client-indiana |
    | i57r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT | client client-indiana |
    | i56r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT | client client-indiana |
    | i55r.idp.iu.futuregrid.org | 2011-06-30T18:42:44 CDT | client client-indiana |
    |     info2.dyn.teragrid.org | 2011-06-30T15:30:00 CDT |    n            server |
    --------------------------------------------------------------------------------

TakTuk
======================================================================

Running Experiments with TakTuk
-------------------------------

It is very easy for you to setup TakTuk for your use on FutureGrid.
You simply need to load the taktuk module::

    alamo$ module load taktuk

You can then use TakTuk with the hosts that you have provisioned and
organized with the Host List Manager. An example TakTuk command is::

    alamo$ taktuk -s -f `hlist -f client` broadcast exec { hostname }
    c037.alamo.futuregrid.org-1: hostname (14062): output > c037
    c070.alamo.futuregrid.org-2: hostname (6167): output > c070
    c033.alamo.futuregrid.org-3: hostname (14662): output > c033
    c026.alamo.futuregrid.org-4: hostname (12788): output > c026
    c037.alamo.futuregrid.org-1: hostname (14062): status > Exited with status 0
    c033.alamo.futuregrid.org-3: hostname (14662): status > Exited with status 0
    c026.alamo.futuregrid.org-4: hostname (12788): status > Exited with status 0
    c070.alamo.futuregrid.org-2: hostname (6167): status > Exited with status 0
    i57r.idp.iu.futuregrid.org-6: hostname (19868): output > i57
    i58r.idp.iu.futuregrid.org-5: hostname (16148): output > i58
    i56r.idp.iu.futuregrid.org-7: hostname (27979): output > i56
    i55r.idp.iu.futuregrid.org-8: hostname (8500): output > i55
    i57r.idp.iu.futuregrid.org-6: hostname (19868): status > Exited with status 0
    i56r.idp.iu.futuregrid.org-7: hostname (27979): status > Exited with status 0
    i58r.idp.iu.futuregrid.org-5: hostname (16148): status > Exited with status 0
    i55r.idp.iu.futuregrid.org-8: hostname (8500): status > Exited with status 0

There command above passed a number of arguments to taktuk. The -s
flag tells TakTuk to self-propagate. That is, don't assume that TakTuk
is installed on the remote hosts. This flag slows TakTuk down since it
causes TakTuk to copy some of its code out to the hosts, but this
overhead isn't significant for smaller numbers of hosts. If you wish to
avoid using this flag, you can ensure that taktuk is in your path on the
hosts (for example, by loading the taktuk module in your .profile file
on the hosts).

Taktuk allows you to specify a hosts file with one host per line
using the -f flag. The Host List Manager generates these files in your
$HOME/.hostlists directory, but you can easily get the name of the host
list file for a tag using hlist -f <tag>. The taktuk command above has
the hlist command in back ticks, so the hlist command is run and the
output is used as an argument to taktuk.

The final arguments to the command are a request to broadcast the
execution of a command and that the command to execute is hostname. The
output from taktuk is displayed on your screen as well as the exit code
of the remote commands. This example was quite simple, but should give
you an idea of how you can use TakTuk for running experiments. A more
complex example would be for you to use TakTuk to start a monitoring
program on the host tagged server and start programs that stress test
the server on the hosts tagged client. You might also move configuration
files to the client systems with a command such as::

    alamo$ taktuk -s -f `hlist -f client` broadcast put { stress.cfg } { /scratch/myexperiment/stress.cfg }

and move performance results back from the clients and server with
commands such as::

    alamo$ taktuk -s -f `hlist -f client` broadcast get { /scratch/myexperiment/results.txt} { results.\$host }

Host List Manager Commands
--------------------------

The arguments to each command can be viewed by running the command with
the -h option.

hupdate
~~~~~~~

The hupdate command is used to force an update of the locally cached
information. This update is done by querying Torque and Nimbus services
around FutureGrid::

    Usage: hupdate [options]

    Options:
      -h, --help          show this help message and exit
      -p, --provisioning  only update information about hosts provisioned to you
      -l, --hostlists     only update host lists (default is to update both)

hmanage
~~~~~~~

The hmanage command is used to manually manage hosts. This is useful if
you want to include non-FutureGrid hosts in your experiments. Hosts
discovered via update cannot be manually managed except the username to
use on the host can be set via the '-m -u USER' options. This is
particularly helpful when you are using virtual machines where you often
want to log in as a different user (e.g. root)::

    Usage: hmanage [options]

    Options:
      -h, --help            show this help message and exit
      -a, --add             add one or more manually managed hosts
      -r, --remove          remove one or more manually managed hosts
      -m, --modify          modify the properties of one or more manually managed
                            hosts
      -b BEGIN, --begin=BEGIN
                            The date/time the host became available. Optional and
                            only used with -a or -m. Format is yyyy-mm-ddThh:mm:ss
                            in local time.
      -d DURATION, --duration=DURATION
                            The duration the host will be available. Optional and
                            only used with -a or -m. Format is hh:mm:ss.
      -u USER, --username=USER
                            The username to use on the host.
      -n HOST, --hostname=HOST
                            a host name (option can appear one or more times)

hshow
~~~~~

This command provides information about the hosts available to you.
This includes hosts found automatically or entered manually::

    Usage: hshow [options]

    Options:
      -h, --help            show this help message and exit
      -s, --short           provide short output (default)
      -l, --long            only update host lists (default is to update both)
      -n HOST, --hostname=HOST
                            an exact host name or a regular expression (option can
                            appear one or more times)
      -t TAG, --tag=TAG     an exact tag name or a regular (option can appear one
                            or more times)

htag
~~~~

The htag program is used to add, remove, or set tags on one or more
hosts. You must specify one of add (-a), remove (-r), or set (-s)::

    Usage: htag [options]

    Options:
      -h, --help            show this help message and exit
      -a, --add             add tag(s) to host(s)
      -r, --remove          remove tag(s) from host(s)
      -s, --set             set tag(s) for host(s)
      -n HOST, --hostname=HOST
                            an exact host name or a regular expression (option can
                            appear one or more times)
      -t TAG, --tag=TAG     a tag name (option can appear one or more times)

hlist
~~~~~

This program is used to output a host list. The host list can be
output as either the name of the file containing the host names (one per
line) or a space separated lists of host names to stdout. If a host has
a username associated with it, it is output as user@host::

    Usage: hlist [options] <tag>

    Options:
      -h, --help      show this help message and exit
      -f, --filename  output path to file containing the hosts associated with the
                      tag
      -o, --stdout    output hosts associated with the tag

htaktuk
~~~~~~~

A convenience wrapper around the taktuk command that will run hupdate if
it has not been run recently. It expects the taktuk program to be in
your $PATH. All arguments are passed to taktuk.

TakTuk Commands
---------------

TakTuk only provides one command, named taktuk.The full set of options
that can be provided to this command are documented on the `taktuk man
page <http://taktuk.gforge.inria.fr/taktuk.html>`__. There is additional
information linked from the `TakTuk documentation
page <http://taktuk.gforge.inria.fr/documentation.html>`__, including
the `TakTuk User
Guide <http://taktuk.gforge.inria.fr/Documents/TakTuk_UserGuide.pdf>`__.


