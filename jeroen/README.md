
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