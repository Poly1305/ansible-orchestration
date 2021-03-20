# Inhoudsopgave

* [Ansible voorbereidingen](#ansible-voorbereidingen)
* [Linux voorbereidingen](#linux-voorbereidingen)
  * [Installeer OpenSSH server](#installeer-openssh-server-linux)
  * [Voeg de Public key toe aan authorized_keys](#voeg-de-public-key-toe-aan-authorized_keys)
  * [Uitvoeren sudo zonder wachtwoord](#uitvoeren-sudo-zonder-wachtwoord)
    * [Groep sudo zonder wachtwoord](#groep-sudo-zonder-wachtwoord)
    * [Gebruiker sudo zonder wachtwoord](#gebruiker-sudo-zonder-wachtwoord)
* [Windows voorbereidingen](#windows-voorbereidingen)
  * [Installeer OpenSSH server](#installeer-openssh-server-windows)
  * [Voeg de Public key toe aan authorized_keys](#voeg-de-public-key-toe-aan-authorized_keys)
* [Ansible Linux Modules](#linux-modules)
  * [docker_container](#docker-container)
  * [docker_network](#docker-network)
* [Ansible Windows Modules](#windows-modules)
  * [win_feature](#windows-features)
  * [win_reboot](#windows-reboot)
  * [win_ping](#windows-ping)
  * [win_domain_controller](#windows-domain-controller)
* [Ansible Hosts](#ansible-hosts)
  * [Ansible Linux Hosts](#ansible-linux-hosts)
  * [Ansible Windows Hosts](#ansible-windows-hosts)
* [Ansible config](https://github.com/Poly1305/ansible-orchestration/blob/master/jeroen/ansible-config/ansible.cfg)
* [Ansible Playbooks](https://github.com/Poly1305/ansible-orchestration/tree/master/jeroen/playbooks)


# Linux Voorbereidingen

## Installeer OpenSSH server Linux

1. Installeer Open SSH server op Linux

```sudo apt install openssh-server```

2. Start OpenSSH server

```sudo systemctl start sshd.service```

3. Controleer of de OpenSSH server actief is

```sudo systemctl is-enabled sshd.service```

## Voeg de Public key toe aan authorized_keys

1. Maak .ssh folder aan op de node (als deze nog niet bestaat)

2. Kopieer de Public key naar de node

```scp ~/.ssh/id_rsa.pub <username>@<ip-adres>:/home/<username>/.ssh/uploaded_key.pub```

3. Voeg de Public key toe aan het **authorized_keys** bestand

```cat ~/.ssh/uploaded_key.pub >> ~/.ssh/authorized_keys```

## Uitvoeren sudo zonder wachtwoord
Voor het uitvoeren van een Playbook zijn vaak administrator rechten nodig op de node. Omdat het niet verstandig is om een wachtwoord op te nemen in de Playbook (deze wordt namelijk gedeeld via GitHub) moet de groep van de gebruiker of de gebruiker zo ingesteld worden dat er geen wachtwoord nodig is voor het uitvoeren van een sudo commando. Via de volgende stappen is dit in te stellen voor een groep of afzonderlijke gebruiker. Het bestand wat aangepast gaat worden is terug te vinden op **/etc/sudoers**.

### Groep sudo zonder wachtwoord

1. Open het bestand /etc/sudoers

```sudo visudo```

2. Voeg de volgende regel toe aan het bestand

```
%<naam van de groep> ALL=ALL(ALL:ALL) NOPASSWD:ALL
```

3. Voor gebruikers in de ingevoerde groep is het niet meer nodig om het wachtwoord op te geven bij het uitvoeren van het **sudo** commando


### Gebruiker sudo zonder wachtwoord

1. Open het bestand /etc/sudoers

```sudo visudo```

2. Voeg de volgende regel toe aan het bestand

```
<gebruikersnaam> ALL=ALL(ALL:ALL) NOPASSWD:ALL
```

3. Voor de ingevoerde gebruiker is het niet meer nodig om het wachtwoord op te geven bij het uitvoeren van het **sudo** commando


# Windows voorbereidingen

## Installeer OpenSSH server Windows

1. Installeer OpenSSH server op Windows

```Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0```

2. Start de OpenSSH server

```Start-Service sshd```

3. Controleer of de OpenSSH server is geinstalleerd

```Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'```

3. Start OpenSSH server automatisch bij het opstarten van Windows

```Set-Service -Name sshd -StartupType 'Automatic'```

4. Pas de Firewall aan voor OpenSSH server

```New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22```

## Voeg de Public key toe aan authorized_keys

1. Maak .ssh folder aan op de node (als deze nog niet bestaat)

2. Kopieer de Public key naar de node

```scp ~/.ssh/id_rsa.pub <username>@<ip-adres>:/c:/users/<username>/.ssh/uploaded_key.pub```

3. Voeg de Public key toe aan het **authorized_keys** bestand

```cat .ssh/uploaded_key.pub >> .ssh/authorized_keys```

# Ansible Linux Modules

## Docker Container
[Module docker_container](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html)

### Voorbeeld Playbook (Watchtower)
```
# Watchtower
- name: laungh watchtower container
    docker_container:
      name: watchtower
      image: containrrr/watchtower:latest
      restart_policy: unless-stopped
      detach: yes
      state: started
#     state: absent
      purge_networks: yes
      networks_cli_compatible: yes
      volumes:
        - /var/run/docker.sock:/var/run/docker.sock
      env:
        TZ: "Europe/Amsterdam"
        WATCHTOWER_POLL_INTERVAL: "3600"
        WATCHTOWER_INCLUDE_STOPPED: "true"
        WATCHTOWER_DEBUG: "true"
        WATCHTOWER_CLEANUP: "true"
        WATCHTOWER_NOTIFICATIONS: "shoutrrr"
        WATCHTOWER_NOTIFICATION_URL: "telegram://<bot-token>@<bot-username>?channels=@<channel-name>"
        WATCHTOWER_MONITOR_ONLY: "true"
        WATCHTOWER_REVIVE_STOPPED: "true"
      networks:
        - name: web
```

## Docker Network
[Module docker_network]https://docs.ansible.com/ansible/2.3/docker_network_module.html

### Voorbeeld Playbook

Maak het **web** netwerk aan voor gebruik in de [docker_container module](#docker-container)
```
# Create web network
- name: create web network
    docker_network:
      name: web      

```

# Ansible Windows Modules

## Windows Features
[Module win_feature](https://docs.ansible.com/ansible/2.8/modules/win_feature_module.html)

### Voorbeeld Playbook
```
---
- name: install-hyperv
  hosts: windows
  remote_user: <gebruikersnaam>
  become: yes
  become_user: <gebruikersnaam>
  become_method: runas
  gather_facts: no
  tasks:
    - name: Installeer Hyper-V
      win_feature:
        name: Hyper-V
        state: present
        include_sub_features: yes
        include_management_tools: yes
      register: win_feature
```

## Windows Reboot
[Module win_reboot](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_reboot_module.html)

### Voorbeeld van herstarten na installeren rol/feature (In Playbook)

```
- name: Herstart server wanneer dit nodig is voor het installeren van de rol/feature
  win_reboot:
  when: win_feature.reboot_required  
```

### Voorbeeld van herstarten na een bepaalde tijd (Playbook)

```
---
- name: rebootwindows
  hosts: windows
  remote_user: <gebruikersnaam>
  become: yes
  become_user: <gebruikersnaam>
  become_method: runas
  gather_facts: no
  tasks:
    - name: Herstart Windows
      win_reboot:
        reboot_timeout: 3
```

## Windows Ping
[Module win_ping](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html)

### Voorbeeld van win_ping in Ansible syntax
```ansible -m win_ping <hosts>```


### Voorbeeld van win_ping in Playbook
```
---
- name: ping-windows
  hosts: windows
  remote_user: <gebruikersnaam>
  become: yes
  become_user: <gebruikersnaam>
  become_method: runas
  gather_facts: yes
  tasks:
    - win_ping:  
```

## Windows Domain Controller
[Module win_domain_controller](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_domain_controller_module.html)


# Ansible Hosts

## Ansible Linux hosts

Linux servers en computers in Ansible host-lijst

```
[linux]
192.168.56.236
192.168.56.237
192.168.56.238

[linux:vars]
ansible_user=<username>
```

## Ansible Windows hosts

Windows servers en computers in Ansible host-lijst

```
[windows]
192.168.56.239

[windows:vars]
ansible_user=<username>
ansible_password=<password>
ansible_connection=ssh
ansible_ssh_port=22
ansible_shell_type=<cmd or powershell>
```

De variabele **ansible_shell_type** moet de DefaultShell weegeven die op de Windows-host is geconfigureerd. Stel in op **cmd** voor de standaardshell of stel in op **powershell** als de DefaultShell is gewijzigd in PowerShell. 