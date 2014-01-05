**********************************************************************
Contributing to the Manual
**********************************************************************

It is very easy to contribute to the existing manual. All you need is
to e-mail us the changes. However, if you like it is also easy to set
up the manual generation fromework on your local machine as described
in a later section.

Organisation of the Manual in Git
----------------------------------

The FG manual has been developed by many different groups and we try
to provide a consistant set of manual pages as much as possible. The
manual is located in the directory::

  doc/source

Here you will find the many RST files contributed by the team members.
To simplify editing and to keep the number of conflicts during 
editing to a minimum it is naturally a good idea to have many such
files. However, all of them are integrated via the file::

  doc/source/index.rst

into a single manaul. Due to this organization it is also possible to
create custom manauls that may suport a particular class. For example
a class on big data may not be wanting to use MPI and thus a special
manual for such a class could be created. The nice thing is that the
teacher does not have to create additional information, but can just
use sphinx and a special index rst file to create a customized manual
of interest.

Please note that at this time we have also additional documented rst
files not yet included into the manual as they were not yet reviewed.

FAQ
----

* How to find the rst file?

  * Sometimes an editor may want to locate the name of the rst
    file. This is easy, just look in your browser, and see the usrl,
    the last filename with a .html ending gives your the rst file name,
    just replace html with rst

* Can I edit RST files in Word?

  * yes you can, but you must make sure that you do use the proper
    ascii charaters for quotes and other symbols that RST relies on.
 
* Can I edit RST files directly in a Web browser without word

  * Yes you can, you must have a git account for that and you can editd
    directly?

* I do not have a Git account how do I communicate errors?

  * Either Send us the url of the manual page with an error, copy the "before
    text", add a "changed to" text and e-mail it to us

  * Or, create a git clone and send us the patch. More information
    about this can be found in the git user manual on github.com

* Why use RST?

  * Previously pages of the FG manual were edited directly in drupal
    on our portal. However, editors were abusing our wysiwyg editor by
    pasting and copying text from thrird party edirors such as word
    into the drupal editor. Unfortunately, this lead to inconsistent
    formating and severe problems by editing documents. We also
    discovered issues at times when documents were edited by multiple
    editors at the same time. 

  * While using RST we avoid inconsistent formating.

  * While using git we use a much better tracking feature for parallel
    edits,

  * While using RST we have a nice search feature.

  * While using RST we can integrate autogenerate documentation form
    FutureGrid code we develop such as RAIN and cloudmesh.

* Why not use Word and skydrive?

  * Our team has rich experience with skydrive and Word. However word
    does not provide a publication framework for our manaul that is
    maintained by a highly distributed team. Although skydrive can be
    a help to share directories, we still have to enable the creation
    of a single consistemnt manaul. We also experienced issues with
    large groups on microsoft skydrive. As most contributions come
    from developers that have already accounts on github, they do not
    have to create new accounts on skydrive. Furthermore, not all
    developers have access to word. Howvere RST documents are editor
    independent. You can edit them with Word, emacs, vi, vim, or
    whtever other text editor you like. Thus the good news is if you like to use word to edit the
    documentation you can.

Publication of the Manual
--------------------------

The manual will be automatically upgraded once a change to git is
committed. However, this feture is currently disabled and will become
available in January of 2014 again.

The current method is to e-mail laszewski@gmail.com for an update
request while describing which files have been changed so a review can
tke place and the publication script can be invoked. We have not put
this script into the repository in order to avoid accidental changes.


**********************************************************************
Setting Up the Expert Developers Manual Editing Environment
**********************************************************************

Note that setting up the expert manual editing environment is optional
and does not have to be conducted at all in order to contribute or
allert us of errors in the manual. We suggest that you consult the
previous section for hints on how to send us errors or improvement
suggestions for the manual.

It is extremely easy to build the FG manual on your local
machine. Just a very limited number of python packages are
needed. However, we have decided to only document the way to install
it in pythons excellent virtualenv. Although it is possible to have an
even easier instal, we decided to stay with virtualenv as it will
protect your current environment from pagackes that you may not want
to have on your computer in your regular python environment.


Python
-------

Make sure you have python 2.7.2::

    $ python --version

Please note that we have not tried python version 3 for this.

Virtualenv
----------------------------------------------------------------------
Make sure the is no book directory in your home

Use virtual env::

    $ cd ~
    $ virtualenv MANUAL
    $ source MANUAL/bin/activate

In case you were to use another terminal (for example quit this one
and start a new one later), please remember to execute::

    $ source MANUAL/bin/activate


Create a github local directory with the manual
----------------------------------------------------------------------
We assume you will install your local copy of the manual in
~/github/manual. If you do not want to use the github dir, please use
another directory name you like::

    $ mkdir -p ~/github
    $ cd ~/github
    $ git clone https://github.com/futuregrid/manual.git

Install the Requirements
----------------------------------------------------------------------
To build this book make sure you install the following module::

    $ cd manual
    $ pip install -r requirements.txt

This may take a while, so be patient.

The files will be in::

   ./doc/source 

and have an rst ending. They use
restructured text. For more info on rst see:

* http://sphinx-doc.org/rest.html



All-in-one setup script
--------------------

Execute the following script only with care. Maybe its best if you
copy one line at a time as documented earlier to avoid problems::

    cd ~
    virtualenv MANUAL
    source MANUAL/bin/activate
    mkdir -p ~/github
    cd ~/github
    git clone https://github.com/futuregrid/manual.git
    cd manual
    pip install -r requirements.txt



Watchdog
-------------

This tool is optional and can be skipped for those just doing a
regular install.

You may be interested in using watchdog when you are in the process of
editing a page. Upon chnage it will update the changed html output
into the browser. For example, assume you edit the page
openstack.rst. If you are running in another window::

   make watchdog FILE=openstack

For more details, please see the Makefile.

Transfering a page from the portal to RST
----------------------------------------------------------------------

Assume you like to transfer a page from the portal to rst. This can
actually be done quite easily using a program called pandoc. First get
the page and rename it to a page with html::

    $ wget https://portal.futuregrid.org/contrib/simple-vine-tutorial
    $ mv simple-vine-tutorial simple-vine-tutorial.html
    $ pandoc simple-vine-tutorial.html -o simple-vine-tutorial.rst

Than edit the page and remove the code related to the menues so only
the bare code stays:

* typically everything before **What links here** can be ignored.
* typically everything after the words  **Your rating** and the rest
   of the page can  be ignored.

Creating the pages locally
---------------------

To create the pages locally simply go in the manual folder and saay
make::

    $ cd ~/github/manual
    $ make

Your index file will be in::

     $ firefox ./doc/build/html/index.html

On Osx you can simply say::

     $ make view
..
    Autorun 
    .. hint:: PLEASE SKIP THIS SECTION, WE ARE NOT USING AUTORUN
    Autoran can be found at:
    * https://bitbucket.org/birkenfeld/sphinx-contrib/src/c54749e503872d3f7a00c0561a115000dcc83565/autorun?at=default
    To installit you need to do the following::
	$ cd ~
	$ hg clone http://bitbucket.org/birkenfeld/sphinx-contrib/
	$ cd sphinx-contrib/autorun
	$ python setup.py install

Publishing the pages
-----------------------

The pages can be published to github with::

    make gh-pages



Jira 
----------------------------------------------------------------------

References to jira can be made with the tag::

  :jira:`this issue <FG-1418>`

It will result in an outpus such as

:jira:`this issue <FG-1418>`

To just refer to a text with the number use::

   :jira:`FG-1418`

and you will get 

:jira:`FG-1418`

It uses the extension http://sphinx-doc.org/latest/ext/extlinks.html
and the tags must be specified in the conf.py file.

Portal link
----------------------------------------------------------------------

to simplify access to a portal url you can use::

    :portal:`my/ssh-keys`

and it will return

:portal:`my/ssh-keys`

It uses the extension http://sphinx-doc.org/latest/ext/extlinks.html
and the tags must be specified in the conf.py file.

Screencast recording tips
---------------------------

OSX 
~~~~

Install OmniDazzle from:

* http://www.omnigroup.com/products/omnidazzle/


Hide the icons on OSX desktop::

   $ defaults write com.apple.finder CreateDesktop -bool false
   $ killall Finder

Show the icons on OSX desktop::

   $ defaults write com.apple.finder CreateDesktop -bool true
   $ killall Finder

Changing the prompt
~~~~~~~~~~~~~~~~~~~

To change the prompt you can do something like::

    $ PS1="$ "

Recording of typed in commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simply use::

    $ script file.log

Setup quicktime sound recording
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start up quicktime you will see the following window:

|i-quicktime-1|

Click on the little arrow on the right and you will see

|i-quicktime-2|

Checkon the microphone you like to activate. This is  most likely the 
*Build-in-Input: Internal microphone*. Also click on *Show mouse click
in Recording*:

|i-quicktime-3|

Then start regording. Be careful that you wait in the rcordng till you
see a little timer on the left quicktime needs a bit of startup time
when recording sound and images.

.. |i-quicktime-1| image:: /images/quicktime-1.png
.. |i-quicktime-2| image:: /images/quicktime-2.png
.. |i-quicktime-3| image:: /images/quicktime-3.png
