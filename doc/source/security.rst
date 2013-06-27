Accessing FutureGrid resources via SSH
======================================

To properly view this manual page, please log into the FutureGrid portal
with your FutureGrid name.

To access the various FutureGrid resources, you need to provide a public
ssh key to FutureGrid. In this manual, we explain how to generate a ssh
key, upload it to the FutureGrid portal and log onto the resources. This
manual covers both UNIX and Windows Users.

Requirement for Windows Users
----------------------------------------------------------------------

Windows users need to have some special software to be able to use the
SSH commands. We recommend you use Cygwin (Linux-like environment for
Windows) because it will ease your experience with FutureGrid. We have
prepared a Cygwin version that is ready to use (If for some reason you
decide to download and install Cygwin from the official site, remember
that you need to install the ssh packages).

#. Download Cygwin from our
   Portal \ `https://portal.futuregrid.org/sites/default/files/cygwin.zip <https://portal.futuregrid.org/sites/default/files/cygwin.zip>`__.
#. Uncompress the file.
#. Execute the file the 'Windows Batch File' called Cygwin.bat
   |image21|
    
#. You may get a warning. Click in the Run button
   |image22|
     
#. You get a Linux-like terminal that will allow you to continue with
   this manual.
   |image23|
     

**NOTE**: When showing examples of commands, the $ symbol precedes the
actual command. So, the other lines are the output obtained after
executing the command.

Instructions for both Windows and Unix users
----------------------------------------------------------------------

Generate a SSH key
^^^^^^^^^^^^^^^^^^^^^^^

Use the tool ssh-keygen. This program is commonly available on most UNIX
systems (this includes Cygwin). It will ask you for the location and
name of the new key. It will also ask you for a passphrase, we
**STRONGLY RECOMMEND** that you use a passphrase. We have seem advise by
teachers and teachin assistants to not use passphrases: this is
**WRONG**. If you are not using a pasphrase and someone were to steal
your private key they have easily access to your account. We recommend
using the default location ~/.ssh/ and the default name id\_rsa. A
sample session::

    $ ssh-keygen

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/Javi/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/Javi/.ssh/id_rsa
    Your public key has been saved in /home/Javi/.ssh/id_rsa.pub.
    The key fingerprint is:
    90:46:9b:cf:09:16:94:17:df:43:f4:99:97:0d:42:4a Javi@Javi-PC
    The key's randomart image is::

    +--[ RSA 2048]----+
    |.+...Eo= .       |
    | ..=.o + o +o    |
    |O.  o o +.o      |
    | = .   . .       |
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
    +-----------------+

This command requires the interaction of the user.

1. The first question is::

    Enter file in which to save the key (/home/Javi/.ssh/id_rsa): 

We recommend you use the default. To do so, just press the enter key. In
case you already have a ssh key in your machine, you can skip this whole
section or use a different file name.

2. The second and third question is to protect your ssh key with a
passphrase. This password will protect your key because you need to type
it when you want to use it. Thus, you can either type a passphrase or
press enter to leave it without passphrase. To avoid security problems,
we DO recommend that chose a passphrase as discussed previously. Make
sure to not just type return for an empty passphrase::

    Enter passphrase (empty for no passphrase):

and::

    Enter same passphrase again:

 

Check your ssh key
^^^^^^^^^^^^^^^^^^^^^^

Once, you have generated your key, you should have them in the .ssh
directory::

    $ ls -l ~/.ssh

Copy the content of your public key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to copy the content of your public key to upload it to the
portal. A sample asumming that you used the default options during the
key generation::

    $ cat ~/.ssh/id_rsa.pub

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXJH2iG2FMHqC6T/U7uB8kt6KlRh4kUOjgw9sc4Uu+Uwe/EwD0wk6CBQMB+HKb9upvCRW/851UyRUagtlQexCRM2rMCi0VvhTVZhj61pTdhyl1t8hlkoL19JVnVBPP5kIN3wVyNAJjYBrAUNW4dXKXtmfkXp98T3OW4mxAtTH434MaT+QcPTcxims/hwsUeDAVKZY7UgZhEbiExxkejtnRBHTipi0W03W05TOUGRW7EuKf/4ftNVPilCO4DpfY44NFG1xPwHeimUk+t9h48pBQj16FrUCp0rS02Pj+4/9dNeS1kmNJu5ZYS8HVRhvuoTXuAY/UVcynEPUegkp+qYnR user@myemail.edu

Go ahead and select the ouptut, right click, and copy::

    $ cat ~/.ssh/id_rsa.pub

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXJH2iG2FMHqC6T/U7uB8kt6KlRh4kUOjgw9sc4Uu+Uwe/EwD0wk6CBQMB+HKb9upvCRW/851UyRUagtlQexCRM2rMCi0VvhTVZhj61pTdhyl1t8hlkoL19JVnVBPP5kIN3wVyNAJjYBrAUNW4dXKXtmfkXp98T3OW4mxAtTH434MaT+QcPTcxims/hwsUeDAVKZY7UgZhEbiExxkejtnRBHTipi0W03W05TOUGRW7EuKf/4ftNVPilCO4DpfY44NFG1xPwHeimUk+t9h48pBQj16FrUCp0rS02Pj+4/9dNeS1kmNJu5ZYS8HVRhvuoTXuAY/UVcynEPUegkp+qYnR Javi@Javi-PC

Upload the key to the FutureGrid Portal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on the button bellow to add your SSH key (Note: The quick link
button below only works if you are logged in before visiting this page.
Otherwise please make sure you login first and REFRESH this page.)
 |image24|

#. If you were logged into the Portal, this button redirects you to a
   page that includes a link Add a public key.
#. Otherwise, this button redirects you to the login page.

   #. Log into the portal
      |image25|
        
   #. Click in the "ssh key" button
      |image26|
        

#. Click in the "add a public key" link.
   |image27|
     
#. Paste your ssh key into the box marked Key.
   |image28|
     
#. Click the submit button.

-  **IMPORTANT**:

   -  Leave the Title field blank.
   -  Make sure that when you paste your key, it does not contain
      newlines or carriage returns that may have been introduced by
      incorrect pasting and copying. If so, please remove them.

At this point you are all set. However you will still need to wait till
all accounts have been set up to use the resources. Please, check your
email for further updates. You can also refresh this page and see if the
boxes in your account status information are all green. Than you can
continue.

Testing your ssh key
^^^^^^^^^^^^^^^^^^^^^^^

Test you key by logging onto India. India cluster gets the new ssh key
updated almost immediately. For other clusters like Hotel, it can take
around 10 minutes to update the ssh keys. If you are viewing this page
anonymously, please replace <USER> with your FutureGrid user name (the
one used to log into the Portal).

If you placed the ssh key in the default location::

    $ ssh -A gvonlasz@india.futuregrid.org

If you used a different path or name for your key::

    $ ssh -A -i <path to private key> gvonlasz@india.futuregrid.org 

The first time you ssh into a machine you will see a message like the
one shown in the picture. You have to type yes and press enter:


**Note**: the presence of the -A argument above is required for Nimbus
tutorials.

**Note 1**: If you are asked for a password when trying to ssh onto
Hotel, do **NOT** type any password. This means that your ssh key is not
updated yet. You need to wait a bit more.

Testing your ssh key on Hotel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After uploading your ssh key, it can take around 10 minutes to update
the ssh keys of Hotel. So, if you were able to log onto India, you have
set up properly your ssh key. So, after a while you will be able to log
onto Hotel.  If you are viewing this page anonymously, Please replace
<USER> with your FutureGrid user name (the one used to log into the
Portal).

If you placed the ssh key in the default location::

    $ ssh -A gvonlasz@hotel.futuregrid.org

If you used a different path or name for your key::

    $ ssh -A -i <path to private key> gvonlasz@hotel.futuregrid.org 

The first time you ssh into a machine you will see a message like this::

    The authenticity of host 'hotel.futuregrid.org (149.165.148.5)' can't be established.
    RSA key fingerprint is f8:96:15:b7:21:eb:64:92:6c:de:e0:79:f3:fb:86:dd.
    Are you sure you want to continue connecting (yes/no)? yes 

**Note**: the presence of the -A argument above is required for Nimbus
tutorials.

**Note 1**: If you are asked for a password when trying to ssh onto
Hotel, do \ **NOT** type any password. This means that your ssh key is
not updated yet. You need to wait a bit more.

Generating SSH Keys for FutureGrid Access
=========================================



Key Generation
==============

To gain access to FutureGrid Resources including HPC and Nimbus
services, you need to provide a public key to FutureGrid. We recommend
that you are familiar with public keys and have the understanding that
we do REQUIRE passphrase protected keys. To generate and send such a
key, please follow the following steps. To find more out about open
ssh you can also go to 

-  `http://openssh.com/manual.html <http://openssh.com/manual.html>`__

Other good resources include 

-  http://help.github.com/key-setup-redirect
-  http://help.github.com/working-with-key-passphrases/
-  http://www.dribin.org/dave/blog/archives/2007/11/28/ssh\_agent\_leopard/

Generate Public/Private Key Pair
---------------------------------------------

First, you have to generate a key. You do this as follows:

-  Step 1: use the command “ssh-keygen -t rsa -C <your-e-mail>” to
   generate the key
-  Step 2: specifiy the KeyPair location and name. We recommend that you
   use the default location if you do not yet have another key there.
   e.g. /home/username/.ssh/id\_rsa
-  Step 3: type user defined passphrase when asking passphrase for the
   key

Example::

    ssh-keygen -t rsa -C johndoe@indiana.edu

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/johndoe/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/johndoe/.ssh/id_rsa.
    Your public key has been saved in /home/johndoe/.ssh/id_rsa.pub.
    The key fingerprint is:
    34:87:67:ea:c2:49:ee:c2:81:d2:10:84:b1:3e:05:59 johndoe@indiana.edu


List the result
----------------------------

You can find your key under the key location. As we user the .ssh
directory it will be located there::

    $ls -lisa ~/.ssh
    -rw-------  1 johndoe johndoe        1743 2011-02-10 09:44 id_rsa
    -rw-r--r--  1 johndoe johndoe         399 2011-02-10 09:44 id_rsa.pub

 


Add or Replace Passphrase for an Already Generated Key
-------------------------------------------------------------------

In case you need to change your change passphrase, you can simply run
“ssh-keygen -p” command. Then specify the location of your current key,
and input (old and) new passphrases. There is no need to re-generate
keys::

    ssh-keygen -p

    Enter file in which the key is (/home/johndoe/.ssh/id_rsa):
    Enter old passphrase:
    Key has comment '/home/johndoe/.ssh/id_rsa'
    Enter new passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved with the new passphrase.  

 

Capture the Public Key for FutureGrid
-------------------------------------------------

Use a text editor to open the “id\_rsa.pub”. Copy the **entire**
contents of this file into the ssh key field as part of your profile
information. You can now add this key to your keys at the following
page:

Key Management
-----------------

This is a future section that will include material about how to use
ssh-add and keychain. You can find instructions on them via the
github link that we provided above. However, we are not github ;-)

Resetting the SSH key
------------------------

Please follow the instructions given at 

-  `https://portal.futuregrid.org/how-do-i-reset-my-ssh-key <https://portal.futuregrid.org/how-do-i-reset-my-ssh-key>`__



.. |image21| image:: https://portal.futuregrid.org/sites/default/files/u30/cygwim1.png
.. |image22| image:: https://portal.futuregrid.org/sites/default/files/u30/cygwin2.png
.. |image23| image:: https://portal.futuregrid.org/sites/default/files/u30/cygwinfirst.png
.. |image24| image:: https://portal.futuregrid.org/sites/default/files/u23/register-sshkey.png
   :target: https://portal.futuregrid.org/user/23/ssh-keys
.. |image25| image:: https://portal.futuregrid.org/sites/default/files/u30/portalLogin_0.png
.. |image26| image:: https://portal.futuregrid.org/sites/default/files/u30/portalsshkey.png
.. |image27| image:: https://portal.futuregrid.org/sites/default/files/u30/portalclikaddkey_0.png
.. |image28| image:: https://portal.futuregrid.org/sites/default/files/u30/portalkeypaste_0.png



