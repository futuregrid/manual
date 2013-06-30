OpenStack Grizzly (Gregor)
===================


This manual page explains how to use OpenStack Grizzly on Sierra. It
explains how to login, create an instance of an image, upload/download
images, automate some initial setting and make a snapshot of instance.

From zero to get your first instance running
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. | Login to sierra.

   .. code:: code

       $ ssh username@sierra.futuregrid.org

#. | Create your novarc file with cloudmesh.

   .. code:: code

       $ module load cloudmesh
       $ cm-manage config sierra-openstack-grizzly

   | The cm-manage command will create a nova rc file at the default
   location ~/.futuregrid/novarc  To find out more about novarc files,
   please consult with the OpenStack manuals.
   |   

#. | Set your OpenStack environment valiables by reading your novarc
   file, and load novaclient

   .. code:: code

       $ source ~/.futuregrid/novarc
       $ module load novaclient

#. | Check if your nova client works by printing the image list and the
   flavor-list. If you can see the list, your account is fine and you
   are good to go to the next step. If you have a problem at this point,
   your account may have a problem. So please submit a support ticket on
   `our ticket system <https://portal.futuregrid.org/help>`__. Our staff
   will help you.

   .. code:: code

       $ nova image-list
       +--------------------------------------+-------------------------+--------+--------+
       | ID                                   | Name                    | Status | Server |
       +--------------------------------------+-------------------------+--------+--------+
       | 18c437e5-d65e-418f-a739-9604cef8ab33 | futuregrid/fedora-18    | ACTIVE |        |
       | 1a5fd55e-79b9-4dd5-ae9b-ea10ef3156e9 | futuregrid/ubuntu-12.04 | ACTIVE |        |
       +--------------------------------------+-------------------------+--------+--------+

   .. code:: code

       $ nova flavor-list
       +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+-------------+
       | ID | Name      | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public | extra_specs |
       +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+-------------+
       | 1  | m1.tiny   | 512       | 0    | 0         |      | 1     | 1.0         | True      | {}          |
       | 2  | m1.small  | 2048      | 20   | 0         |      | 1     | 1.0         | True      | {}          |
       | 3  | m1.medium | 4096      | 40   | 0         |      | 2     | 1.0         | True      | {}          |
       | 4  | m1.large  | 8192      | 80   | 0         |      | 4     | 1.0         | True      | {}          |
       | 5  | m1.xlarge | 16384     | 160  | 0         |      | 8     | 1.0         | True      | {}          |
       +----+-----------+-----------+------+-----------+------+-------+-------------+-----------+-------------+

#. | Create your ssh key. (\*$LOGNAME is your username on a Linux
   machine. So you can simply type your username instead of $LOGNAME, if
   you like.)

   .. code:: code

       $ nova keypair-add $LOGNAME-key > ~/.ssh/$LOGNAME-key
       $ chmod 600 ~/.ssh/$LOGNAME-key
       $ nova keypair-list
       +---------------+-------------------------------------------------+
       | Name          | Fingerprint                                     |
       +---------------+-------------------------------------------------+
       | <logname>-key | ab:a6:63:82:dd:08:d3:bc:c0:21:56:4c:e2:bb:22:ac |
       +---------------+-------------------------------------------------+
       Where Logname is your ligin name on sierra

   Note: Make sure you are not already having the key wiith that name in
   order to avoid overwriting it. Thus be extra careful to execute this
   step twice.

   | Often it is the case that you already have a key in your ~/.ssh
   directory that you may want to use. For example if you use rsa, your
   key will be located at ~/.ssh/id\_rsa.pub. If you like to find out
   more about normal Linux use key management, please consult with a ssh
   manual.
   |   

#. | Open ICMP and port 22 on default group.

   .. code:: code

       $ nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
       $ nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
       $ nova secgroup-list-rules default
       +-------------+-----------+---------+-----------+--------------+
       | IP Protocol | From Port | To Port | IP Range  | Source Group |
       +-------------+-----------+---------+-----------+--------------+
       | icmp        | -1        | -1      | 0.0.0.0/0 |              |
       | tcp         | 22        | 22      | 0.0.0.0/0 |              |
       +-------------+-----------+---------+-----------+--------------+

#. | Boot an instance.

   .. code:: code

       $ nova boot --flavor m1.small \
                   --image "futuregrid/ubuntu-12.04" \
                   --key_name $LOGNAME-key $LOGNAME-001
       +-----------------------------+--------------------------------------+
       | Property                    | Value                                |
       +-----------------------------+--------------------------------------+
       | status                      | BUILD                                |
       | updated                     | 2013-05-15T20:32:03Z                 |
       | OS-EXT-STS:task_state       | scheduling                           |
       | key_name                    | mystackkey                           |
       | image                       | futuregrid/ubuntu-12.04              |
       | hostId                      |                                      |
       | OS-EXT-STS:vm_state         | building                             |
       | flavor                      | m1.small                             |
       | id                          | e15ad5b6-c3f0-4c07-996c-3bbe709a63b7 |
       | security_groups             | [{u'name': u'default'}]              |
       | user_id                     | 3bd2d773911c4502982e5c2cd81437f7     |
       | name                        | vm001                                |
       | adminPass                   | KgiKjek99dgk                         |
       | tenant_id                   | b7ea98db7b3449b184b58d28e80c7541     |
       | created                     | 2013-05-15T20:32:03Z                 |
       | OS-DCF:diskConfig           | MANUAL                               |
       | metadata                    | {}                                   |
       | accessIPv4                  |                                      |
       | accessIPv6                  |                                      |
       | progress                    | 0                                    |
       | OS-EXT-STS:power_state      | 0                                    |
       | OS-EXT-AZ:availability_zone | None                                 |
       | config_drive                |                                      |
       +-----------------------------+--------------------------------------+

#. | Check if your instance is active. If the status changed from BUILD
   to ACTIVE, you should be able to login.

   .. code:: code

       $ nova list
       +--------------------------------------+---------------+--------+---------------------+
       | ID                                   | Name          | Status | Networks            |
       +--------------------------------------+---------------+--------+---------------------+
       | e15ad5b6-c3f0-4c07-996c-3bbe709a63b7 | <logname>-001 | ACTIVE | private=10.35.23.18 |
       +--------------------------------------+---------------+--------+---------------------+

       $ ssh -l ubuntu -i ~/.ssh/$LOGNAME-key 10.35.23.18
       ubuntu@<logname>-001:~$

#. | If you see this error, you need to delete the offending host key
   from .ssh/known\_hosts

   .. code:: code

       Add correct host key in /home/username/.ssh/known_hosts to get rid of this message.
       Offending key in /home/peter/.ssh/known_hosts:3

#. | But you can simply disable ssh host key checking by adding these
   lines on .ssh/config . The .ssh/config doesn't exist as default so
   create the file and put these lines.

   .. code:: code

       Host 10.35.23.* 198.202.120.*
        StrictHostKeyChecking no
        UserKnownHostsFile=/dev/null

Use Block Storage
~~~~~~~~~~~~~~~~~

#. | You can create a block storage(which is similar to Amazon EBS).
   Creating a 5G volume is like this:

   .. code:: code

       $ nova volume-create 5
       $ nova volume-list
       +--------------------------------------+-----------+--------------+------+-------------+-------------+
       | ID                                   | Status    | Display Name | Size | Volume Type | Attached to |
       +--------------------------------------+-----------+--------------+------+-------------+-------------+
       | 6d0d8285-xxxx-xxxx-xxxx-xxxxxxxxxxxx | available | None         |  5   | None        |             |
       +--------------------------------------+-----------+--------------+------+-------------+-------------+

#. | Attach the volume to your instance as "/dev/vdb" with this:

   .. code:: code

       $ nova volume-attach $LOGNAME-001 6d0d8285-xxxx-xxxx-xxxx-xxxxxxxxxxxx "/dev/vdb"

#. | Login to your instance, make filesystem and mount it on some
   directory. Here's an example, mounting on /mnt

   .. code:: code

       $ ssh -l ubuntu -i ~/.ssh/$LOGNAME-key 10.35.23.18
       ubuntu@<logname>-001:~$ sudo su -
       root@<logname>-001:~# mkfs.ext4 /dev/vdb
       root@<logname>-001:~# mount /dev/vdb /mnt
       root@<logname>-001:~# df -h
       Filesystem      Size  Used Avail Use% Mounted on
       /dev/vda1        20G  2.1G   17G  11% /
       none            4.0K     0  4.0K   0% /sys/fs/cgroup
       udev            998M  8.0K  998M   1% /dev
       tmpfs           201M  236K  201M   1% /run
       none            5.0M     0  5.0M   0% /run/lock
       none           1002M     0 1002M   0% /run/shm
       none            100M     0  100M   0% /run/user
       /dev/vdb        4.8G   23M  4.2G   1% /mnt

#. | When you want to detach it, unmount /mnt first, go back to sierra's
   login node and execute volume-detach:

   .. code:: code

       root@<logname>-001:~# umount /mnt
       root@<logname>-001:~# exit
       ubuntu@<logname>-001:~$ exit
       $ nova volume-detach $LOGNAME-001 6d0d8285-xxxx-xxxx-xxxx-xxxxxxxxxxxx

Set up external access to your instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For making it possible to access your instance from external, you need
to create an external IP address and add it on your instance.

#. | Create an external ip address with 

   .. code:: code

       $ nova floating-ip-create
       +-----------------+-------------+----------+------+
       | Ip              | Instance Id | Fixed Ip | Pool |
       +-----------------+-------------+----------+------+
       | 198.202.120.193 | None        | None     | nova |
       +-----------------+-------------+----------+------+

#. | And then, put it on your instance with 

   .. code:: code

       $ nova add-floating-ip $LOGNAME-001 198.202.120.193
       $ nova floating-ip-list
       +-----------------+--------------------------------------+-------------+------+
       | Ip              | Instance Id                          | Fixed Ip    | Pool |
       +-----------------+--------------------------------------+-------------+------+
       | 198.202.120.193 | c0bd849a-221a-4e53-bf7b-7097541a9bcc | 10.35.23.20 | nova |
       +-----------------+--------------------------------------+-------------+------+

   Now you should be able to ping and ssh from external.

Make a snapshot of an instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: Please use your login name as a prefix followed by a /. If you
create an image for a particular project, please use the projectname. In
many cases the projectname is preferable in case multiple users share
the same images

#. | After you have worked on your instance, you will want to create a
   snapshot of your instance. You can do it with 

   .. code:: code

       $ nova image-create $LOGNAME-001 $LOGNAME/custom-ubuntu-01
       $ nova image-list
       +--------------------------------------+----------------------------+--------+--------------------------------------+
       | ID                                   | Name                       | Status | Server                               |
       +--------------------------------------+----------------------------+--------+--------------------------------------+
       | 18c437e5-d65e-418f-a739-9604cef8ab33 | futuregrid/fedora-18       | ACTIVE |                                      |
       | 1a5fd55e-79b9-4dd5-ae9b-ea10ef3156e9 | futuregrid/ubuntu-12.04    | ACTIVE |                                      |
       | f43375b4-44d3-4350-a9a8-a73f35589344 | <logname>/custom-ubuntu-01 | ACTIVE | c0bd849a-221a-4e53-bf7b-7097541a9bcc |
       +--------------------------------------+----------------------------+--------+--------------------------------------+

#. | If you want to download your customized image, you can do it with
   this;

   .. code:: code

       $ glance image-download --file "custome-ubuntu-01.img" "$LOGNAME/custom-ubuntu-01"
               

Automate some initial configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may want to install some packages into the iamge,  enable root,  and
add ssh authorized\_keys. With the OpenStack cloud-init such steps can
be simplified.

#. | Create a file(mycloudinit.txt) containing these lines:

   .. code:: code

       #cloud-config

       # Enable root login.
       disable_root: false
       # Install packages.
       packages:
        - apt-show-versions
        - wget
        - build-essential
       # Add some more ssh public keys.
       ssh_authorized_keys:
        - ssh-rsa AAAfkdfeiekf....fES7060rb myuser@s1
        - ssh-rsa AAAAAAkgeig78...skdfjeigi myuser@myhost

#. | Boot your instance with --user-data mycloudinit.txt like this:

   .. code:: code

       $ nova boot --flavor m1.small \
                   --image "futuregrid/ubuntu-12.04" \
                   --key_name $LOGNAME-key \
                   --user-data mycloudinit.txt $LOGNAME-002

   You should be able to login to <logname>-002 as root, and the added
   packages are installed.

Get the latest version of Ubuntu Cloud Image and upload it to the OpenStack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. | Several versions of Ubuntu cloud images are available on
   `http://cloud-images.ubuntu.com/ <http://cloud-images.ubuntu.com/>`__
   . Choose the version you want and download the file name with
   \*\*\*\*\*\*-cloudimg-amd64-disk1.img. For example, downloading
   Ubuntu-13.04(Raring Ringtail)is like this:

   .. code:: code

       $ wget http://cloud-images.ubuntu.com/raring/current/raring-server-cloudimg-amd...

#. | Upload it with glance client like this:

   .. code:: code

       $ glance image-create \
              --name $LOGNAME/myimages/ubuntu-13.04 \
              --disk-format qcow2 \
              --container-format bare \
              --file raring-server-cloudimg-amd64-disk1.img

   Now your new image is listed on ``nova image-list``\ and will be
   available when the status become "ACTIVE".

Delete your instance
~~~~~~~~~~~~~~~~~~~~

#. | You can delete your instance with 

   .. code:: code

       $ nova delete $LOGNAME-002

   Please do not forgetto also delete your 001 vm if you no longer need
   it

    

How to change your password
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. | Sometimes, users accidentally send password to a corablator/support
   for debugging, and then regret. When you put yourself in the
   situation by mistake, don't worry. Just use keystone client and reset
   your password with

   .. code:: code

       $ keystone password-update

   \* Remember, you will also need to change it in your novarc. This can
   be achieved by either editing your novarc file directly, or by
   editing the file ~/.futuregrid/cloudmesh.yaml annd recreating your
   novarc file.

Things to do when you need Euca2ools or EC2 interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even though the nova client and protocols will provide you with more
advanced features, some users still want to access OpenStack with EC2
compatible tools. One such tool are the euca2tools. We explain briefly
how you can access them.

#. | Create a directory for putting eucarc, and create pk.pem, cert.pem
   and cacert.pem.

   .. code:: code

       mkdir ~/eucacreds
       cd ~/eucacreds
       nova x509-create-cert
       nova x509-get-root-cert
       ls -la

#. | Create EC2\_ACCESS\_KEY and EC2\_SECRET\_KEY.

   .. code:: code

       keystone ec2-credentials-create

#. | Create eucarc file and put your EC2\_ACCESS\_KEY and
   EC2\_SECRET\_KEY like this:

   .. code:: code

       export EC2_ACCESS_KEY="Your EC2_ACCESS_KEY"
       export EC2_SECRET_KEY="Your EC2_SECRET_KEY"
       export EC2_URL="http://s77r.idp.sdsc.futuregrid.org:8773/services/Cloud"
       export S3_URL="http://s77r.idp.sdsc.futuregrid.org:3333"
       export EC2_PRIVATE_KEY=${NOVA_KEY_DIR}/pk.pem
       export EC2_CERT=${NOVA_KEY_DIR}/cert.pem
       export NOVA_CERT=${NOVA_KEY_DIR}/cacert.pem
       export EUCALYPTUS_CERT=${NOVA_CERT}
       alias ec2-bundle-image="ec2-bundle-image --cert ${EC2_CERT} --privatekey ${EC2_PRIVATE_KEY} --user 42 --ec2cert ${NOVA_CERT}"
       alias ec2-upload-bundle="ec2-upload-bundle -a ${EC2_ACCESS_KEY} -s ${EC2_SECRET_KEY} --url ${S3_URL} --ec2cert ${NOVA_CERT}"

#. | Confirm if euca2ools works fine.

   .. code:: code

       module load euca2ools
       source ~/eucacreds/eucarc
       euca-describe-images
       euca-describe-instances

