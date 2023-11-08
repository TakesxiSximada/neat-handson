Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.provider :virtualbox do |vb|
    vb.gui = true
  end

  config.vm.provision :shell do |shell|
    shell.privileged = true
    shell.path = "provision.sh"
    shell.reboot = true
  end
end
