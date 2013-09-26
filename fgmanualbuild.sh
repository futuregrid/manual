#!/bin/sh
#essential system packages/libraries required
sudo apt-get install g++ python-dev python-pip python-virtualenv git libfreetype6-dev libpng-dev mercurial make
# has to activate virtuan env first
cd ~
virtualenv MANUAL
. ./MANUAL/bin/activate
#manually install sphinxcontrib-autorun
mkdir -p ~/hg
cd ~/hg
hg clone http://bitbucket.org/birkenfeld/sphinx-contrib/
cd sphinx-contrib/autorun
python setup.py install
#get the doc source from github
mkdir -p ~/github
cd ~/github
git clone https://github.com/futuregrid/manual.git
#setting up essential python libraries
cd manual
pip install -r requirements_pre.txt
easy_install -U distribute
pip install -r requirements.txt
pip uninstall PIL
