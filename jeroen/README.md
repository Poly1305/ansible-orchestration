# Modules


## Windows Features
[Ansible win_feature](https://docs.ansible.com/ansible/2.8/modules/win_feature_module.html)

### Voorbeeld YAML
'''
---
- name: install-hyperv
  hosts: windows
  remote_user: <username>
  become: yes
  become_user: <username>
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
'''

## Windows Reboot
[Ansible module win_reboot](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_reboot_module.html)

### Voorbeeld van herstarten na installeren rol/feature (In PLaybook)

'''
- name: Herstart server wanneer dit nodig is voor het installeren van de rol/feature
  win_reboot:
  when: win_feature.reboot_required  
'''

### Voorbeeld van herstarten na een bepaalde tijd (Playbook)

'''
---
- name: rebootwindows
  hosts: windows
  remote_user: <username>
  become: yes
  become_user: <username>
  become_method: runas
  gather_facts: no
  tasks:
    - name: Herstart Windows
      win_reboot:
        reboot_timeout: 3
'''