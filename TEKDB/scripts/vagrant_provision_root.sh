#!/bin/bash

UBUNTU_VER=$1
GEOS_VER=$2
POSTGRES_VERSION=$3

/bin/echo "deb http://apt.postgresql.org/pub/repos/apt $UBUNTU_VER-pgdg main" >> /etc/apt/sources.list
/usr/bin/wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -

/usr/bin/apt-get update
/usr/bin/apt-get upgrade

/usr/bin/apt-get install python3-venv python3-dev python3-pip -y

/usr/bin/apt-get install postgresql-9.5-postgis-2.2 postgresql-contrib-9.5 -y

#install Proj.4
cd /tmp
/usr/bin/wget http://download.osgeo.org/proj/proj-4.9.1.tar.gz
/usr/bin/wget http://download.osgeo.org/proj/proj-datumgrid-1.5.tar.gz
/bin/tar xzf /tmp/proj-4.9.1.tar.gz
cd /tmp/proj-4.9.1/nad
/bin/tar xzf /tmp/proj-datumgrid-1.5.tar.gz
cd /tmp/proj-4.9.1
/tmp/proj-4.9.1/configure
/usr/bin/make
/usr/bin/make install

# /usr/bin/apt-get install pgadmin3 -y   # Do we really need this?
/usr/bin/apt-get install binutils libgeos-$GEOS_VER libproj-dev gdal-bin python-gdal -y
sed -i 's/local   all             postgres                                peer/local   all             postgres                                trust/' /etc/postgresql/$POSTGRES_VERSION/main/pg_hba.conf
/usr/sbin/service postgresql restart

# echo `pwd`
chmod +x /vagrant/scripts/vagrant_provision_ubuntu.sh
su -c "/vagrant/scripts/vagrant_provision_ubuntu.sh" ubuntu
