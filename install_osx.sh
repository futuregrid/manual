#!/bin/bash
#essential system packages/libraries required

ENV="ENV"
PWD=`pwd`

install_ubuntu_packages() {
    sudo apt-get install g++ 
    sudo apt-get python-dev python-pip python-virtualenv 
    sudo apt-get git 
    sudo apt-get libfreetype6-dev libpng-dev mercurial make
}

# has to activate virtuan env first
install_virtualenv(){
    cd ~
    virtualenv $ENV
    source ./$ENV/bin/activate   
}

#manually install sphinxcontrib-autorun
install_autorun(){
    mkdir -p /tmp/hg
    cd /tmp/hg
    hg clone http://bitbucket.org/birkenfeld/sphinx-contrib/
    cd sphinx-contrib/autorun
    python setup.py install
}

#get the doc source from github
install_manual_source(){
    mkdir -p ~/github
    cd ~/github
    git clone https://github.com/futuregrid/manual.git
}


#setting up essential python libraries
install_requirements(){
    pip install numpy
    pip install -r requirements_pre.txt
    #easy_install -U distribute
    pip install -r requirements.txt
    #pip uninstall PIL
}

#install_ubuntu_packages

git pull
#install_virtualenv
install_autorun
#install_manual_source
#install_requirements