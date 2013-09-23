
VIRTUALENV="ENV"

def setup_virtualenv():
    local("cd ~; virtualenv {0}".format{VIRTUALENV})
    local("source ~/{0}/bin/activate".format{VIRTUALENV})

def setup_sphinx_autorun():
    local ("mkdir -p /tml/hg")
    local("cd /tmp/hg; hg clone http://bitbucket.org/birkenfeld/sphinx-contrib/")
    local("cd /tmp/hg/sphinx-contrib/autorun; python setup.py install")

def download_manual():
    local("mkdir -p ~/github")
    local("cd ~/github; git clone https://github.com/futuregrid/manual.git")

def requirements():
    local ("cd manual; pip install -r requirements_pre.txt")
    local ("easy_install -U distribute")
    local ("pip install -r requirements.txt")
    local ("pip uninstall PIL")

def ubuntu():
    local("sudo apt-get install g++ python-dev python-pip python-virtualenv git libfreetype6-dev libpng-dev mercurial make")

    setup_virtualenv()
    setup_sphinx_autorun()
    download_manual()
    requirements()

def osx()
    setup_virtualenv()
    setup_sphinx_autorun()
    download_manual()
    requirements()
