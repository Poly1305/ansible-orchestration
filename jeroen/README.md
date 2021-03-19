# Inhoudsopgave

* [Ansible voorbereidingen](#ansible-voorbereidingen)
* [Linux voorbereidingen](#linux-voorbereidingen)
* [Windows voorbereidingen](#windows-voorbereidingen)
  * [Installeer OpenSSH server](#installeer-openssh-server)
  * [Voeg de Public key toe aan authorized_keys](#voeg-de-public-key-toe-aan-authorized_keys)
* [Ansible Modules](#modules)
  * [win_feature](#windows-features)
  * [win_reboot](#windows-reboot)
  * [win_ping](#windows-ping)
  * [win_domain_controller](#windows-domain-controller)
* [Ansible hosts](https://github.com/Poly1305/ansible-orchestration/blob/master/jeroen/ansible-config/hosts)
* [Ansible config](https://github.com/Poly1305/ansible-orchestration/blob/master/jeroen/ansible-config/ansible.cfg)


# Linux Voorbereidingen

## Installeer OpenSSH server

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

## Voeg de gebruiker toe aan de groep zonder sudo
Voor het uitvoeren van een Playbook zijn vaak administrator rechten nodig op de node. Omdat het niet verstandig is om een wachtwoord op te nemen in de Playbook (deze wordt namelijk gedeeld via GitHub) moet de groep van de gebruiker of de gebruiker zo ingesteld worden dat er geen wachtwoord nodig is voor het uitvoern van een sudo commando. Via de volgende stappen is dit in te stellen voor een groep of afzonderlijke gebruiker. Het bestand wat aangepast gaat worden is terug te vinden op **/etc/sudoers**.

### Gebruiker sudo zonder wachtwoord

1. Open het bestand /etc/sudoers

```sudo visudo```

2. Voeg de volgende regel toe aan het bestand

```
%<naam van de groep> ALL=ALL(ALL:ALL) NOPASSWD:ALL

```

3. Voor gebruikers in de ingevoerde groep is het niet meer nodig om het wachtwoord op te geven bij het uitvoeren van het **sudo** commando


### Groep sudo zonder wachtwoord

1. Open het bestand /etc/sudoers

```sudo visudo```

2. Voeg de volgende regel toe aan het bestand

```
<gebruikersnaam> ALL=ALL(ALL:ALL) NOPASSWD:ALL
```

3. Voor de ingevoerde gebruiker is het niet meer nodig om het wachtwoord op te geven bij het uitvoeren van het **sudo** commando


# Windows voorbereidingen

## Installeer OpenSSH server

1. Installeer OpenSSH server op Windows

```Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0```

2. Start de OpenSSH server

```Start-Service sshd```

3. Controleer of de OpenSSH server is geinstalleerd

```Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'```

## Voeg de Public key toe aan authorized_keys

1. Maak .ssh folder aan op de node (als deze nog niet bestaat)

2. Kopieer de Public key naar de node

```scp ~/.ssh/id_rsa.pub <username>@<ip-adres>:/c:/users/<username>/.ssh/uploaded_key.pub```

3. Voeg de Public key toe aan het **authorized_keys** bestand

```cat .ssh/uploaded_key.pub >> .ssh/authorized_keys```


# Modules

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