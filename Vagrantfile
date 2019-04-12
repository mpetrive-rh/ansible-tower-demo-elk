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
      vb.memory = 8192
      vb.cpus = 2
   end
    config.vm.hostname = "elk"
    config.vm.network :private_network, ip: "172.16.2.10"

    config.vm.network :forwarded_port,
      guest: 5601,
      host: 5601,
      host_ip: "192.168.1.100"

    config.vm.network :forwarded_port,
      guest: 9200,
      host: 9200,
      host_ip: "192.168.1.100"
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

    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "site.yml"
      ansible.limit = "all"
      ansible.become = true
      ansible.groups = {
        "elkvm" => ["elk"],
        "openldapvm" => ["openldap"],
        "towervm" => ["tower"],
        "demovm" => ["demovm1", "demovm2", "demovm3", "demovm4"]
      }
      #ansible.galaxy_role_file = "requirements.yml"
    end

    config.vm.network :forwarded_port,
      guest: 443,
      host: 4443,
      host_ip: "192.168.1.100"

  end


  (1..1).each do |i|
#  (1..4).each do |i|
    cluster.vm.define "demovm#{i}" do |config|
      config.vm.box = "centos/7"
      config.ssh.insert_key = false
      config.vm.provider :libvirt do |v|
        v.memory = 512
      end
      config.vm.hostname = "demovm#{i}"
      config.vm.network :private_network, ip: "172.16.2.1#{i}"
    end
  end

end
