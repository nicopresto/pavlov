from fabric.api import *

#env.hosts = ['']
#env.user  = ''

def remote_info():
    run('uname -a')

def local_info():
    local('uname -a')

def update_repos():
    run("sudo apt-get update && sudo apt-get -y upgrade")

def install_core():
#    run("sudo apt-get install openssh-server") # do this manually or on build
    run("sudo apt-get -y install build-essential")
    run("sudo apt-get -y install python-setuptools python-dev")
    run("sudo easy_install pip")
    # ?python-software-properties

def install_editors():
    #note this brings the whole texlive environment ... avoid?
    run("sudo apt-get -y install emacs g++ cmake doxygen git diff colordiff patch meld")
    
def install_web2py():
    run("wget http://www.web2py.com/examples/static/web2py_src.zip")
    run("unzip web2py_src.zip")

#def add_repos():
   # local("sudo add-apt-repository ppa:ubuntugis/ppa") # out of date

def install_reqs():
    run("sudo apt-get -y install libpq-dev autoconf libtool gettext libxml2-dev proj subversion xsltproc libjson0 libjson0-dev libreadline-gplv2-dev")   

# REPO
def install_gis():
    # build gdal from source
    run("sudo apt-get install libgeos-3.2.2 gdal-bin libproj-dev qgis")

def clean():
    run("sudo apt-get autoremove")
    run("sudo apt-get clean")

def basic():
    update_repos()
    install_core()
    install_editors()
    install_web2py()
    install_pg()
    clean()

def build_gis():
    install_gis()

def build_databases():
    run("sudo apt-get install mongodb")
    run("sudo pip install pymongo")
    run("sudo apt-get install postgresql")

def build_stats():
    run("sudo apt-get install r-base")

def configure_python():
    run("sudo pip install ipython")
    run("sudo pip install tornado")
    run("sudo apt-get install uuid-dev")
    run("sudo apt-get install libfreetype6-dev")
    run("wget http://download.zeromq.org/zeromq-2.2.0.tar.gz  && tar xvfz zeromq-2.2.0.tar.gz")
    run("cd zeromq-2.2.0 && ./configure && make && sudo make install")
    run("sudo apt-get install pyzmq")
