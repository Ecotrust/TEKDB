# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/focal64"
  # config.vm.box_check_update = true

  config.vm.network "forwarded_port", guest:8000, host:8000
  config.vm.network "forwarded_port", guest:8080, host:8080
  config.vm.network "forwarded_port", guest:5432, host:65432

  config.ssh.insert_key = true
  config.ssh.forward_agent = true

  config.vm.synced_folder "./", "/usr/local/apps/TEKDB"
  #
  # config.vm.provision "shell" do |s|
  #   s.path = "scripts/vagrant_provision_root.sh"
  #   s.args = ['focal', '3.8.0', '12', '3']
  #   s.privileged = "true"
  # end

end
