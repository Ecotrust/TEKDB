#!/bin/bash
/usr/bin/apt-get update
/usr/bin/apt-get upgrade
/usr/bin/apt-get install python3-venv python3-dev python3-pip -y

echo `pwd`
chmod +x /vagrant/scripts/vagrant_provision_ubuntu.sh
su -c "/vagrant/scripts/vagrant_provision_ubuntu.sh" ubuntu
