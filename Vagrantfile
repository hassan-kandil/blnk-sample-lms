# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

$script = <<SCRIPT
echo "running script in the VM"
echo "Distro packages update"
sudo apt-get update
echo "Installing git"
sudo apt-get install -y git
SCRIPT

Vagrant.configure("2") do |config|

  
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_check_update = false
  config.vm.network "private_network", ip: "192.168.111.223"

  config.vm.define "LMSServerEnviron"
    
  # PostgreSQL
  config.vm.network "forwarded_port", guest: 5431, host: 5431
  config.vm.network "forwarded_port", guest: 8080, host: 8081

  
  # Apps
  (8000..8050).each do |port|
    config.vm.network "forwarded_port", guest: "#{port}", host: "#{port}"
  end
  
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.name = "LMSServerEnviron"
  end

  config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", :mount_options => ["dmode=777","fmode=777"]
  config.vm.provision "shell", inline: $script
  
  config.vm.provision :docker
  config.vm.provision :docker_compose


end
