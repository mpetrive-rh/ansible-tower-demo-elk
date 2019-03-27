# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |cluster|

#  cluster.vm.define "ldapvm" do |config|
#    config.vm.box = "centos/7"
#    config.ssh.insert_key = false
#    config.vm.provider :libvirt do |vb|
#      vb.memory = 512
#    end
#    config.vm.hostname = "ldapvm"
#    config.vm.network :private_network, ip: "172.16.2.9"
#  end
  
  cluster.vm.define "elk" do |config|
    config.vm.box = "centos/7"
    config.ssh.insert_key = false
    config.vm.provider :libvirt do |vb|
      vb.memory = 4096
      vb.cpus = 2
   end
    config.vm.hostname = "elk"
    config.vm.network :private_network, ip: "172.16.2.10"
  end
 
  cluster.vm.define "tower" do |config|
    config.vm.box = "centos/7"
    config.ssh.insert_key = false
    config.vm.provider :libvirt do |vb|
      vb.memory = 4096
      vb.cpus = 2
    end
    config.vm.hostname = "tower"
    config.vm.network :private_network, ip: "172.16.2.42"
  end

  cluster.vm.define "demovm1" do |config|
    config.vm.box = "centos/7"
    config.ssh.insert_key = false
    config.vm.provider :libvirt do |vb|
      vb.memory = 512
    end
    config.vm.hostname = "demovm1"
    config.vm.network :private_network, ip: "172.16.2.5"
  end

#  cluster.vm.define "demovm2" do |config|
#    config.vm.box = "centos/7"
#    config.ssh.insert_key = false
#    config.vm.provider :libvirt do |vb|
#      vb.memory = 512
#    end
#    config.vm.hostname = "demovm2"
#    config.vm.network :private_network, ip: "172.16.2.6"
#  end

#  cluster.vm.define "demovm3" do |config|
#    config.vm.box = "centos/7"
#    config.ssh.insert_key = false
#    config.vm.provider :libvirt do |vb|
#      vb.memory = 512
#    end
#    config.vm.hostname = "demovm3"
#    config.vm.network :private_network, ip: "172.16.2.7"
#   end

#  cluster.vm.define "demovm4" do |config|
#    config.vm.box = "centos/7"
#    config.ssh.insert_key = false
#    config.vm.provider :libvirt do |vb|
#      vb.memory = 512
#    end
#    config.vm.hostname = "demovm4"
#    config.vm.network :private_network, ip: "172.16.2.8"
#  end

  cluster.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
    ansible.groups = {
      "elk" => ["elk"],
      "tower" => ["tower"],
      "demovm" => ["demovm1", "demovm2", "demovm3", "demovm4"]
    }
    ansible.galaxy_role_file = "requirements.yml"
  end

end
