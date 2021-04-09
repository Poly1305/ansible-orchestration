
Windows modules
===============

Module Windows Features
-----------------------
Ansible documentatie: `win_feature <https://docs.ansible.com/ansible/2.8/modules/win_feature_module.html>`_

Voorbeeld Playbook
~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

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


Module Windows Reboot
---------------------
Ansible documentatie: `win_reboot <https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_reboot_module.html>`_

Voorbeeld van herstarten na installeren rol/feature (In Playbook)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: yaml

	- name: Herstart server wanneer dit nodig is voor het installeren van de rol/feature
	  win_reboot:
	  when: win_feature.reboot_required  


Voorbeeld van herstarten na een bepaalde tijd (Playbook)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: yaml

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


Module Windows Ping
-------------------
Ansible documentatie: `win_ping <https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html>`_ 

Voorbeeld van win_ping in Ansible syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

	ansible -m win_ping <hosts>


Voorbeeld van win_ping in Playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: yaml

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


Module Windows Domain Controller
--------------------------------
Ansible documentatie: `win_domain <https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_domain_module.html>`_

Met de module win_domain kan een nieuw domein worden aangemaakt met een nieuw forest.


Voorbeeld van win_domain_controller in Playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    - name: setup-adds
      hosts: windows
      remote_user: <gebruikersnaam>
      become: yes
      become_user: <gebruikersnaam>
      become_method: runas
      gather_facts: no
      tasks:
        - name: Maak een nieuw domein met een nieuw forest
          win_domain:
            dns_domain_name: <domeinnaam>.local
            domain_netbios_name: <naam>
            safe_mode_password: <password>
          register: domain_result

    - name: Start netlogon service
      win_service:
        name: netlogon
        state: started

    - name: Herstart server wanneer dit nodig is voor het installeren van de rol/feature
      win_reboot:
      when: domain_result.reboot_required 


Module Windows DNS-client
-------------------------
Ansible documentatie: `win_dns_client <https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_dns_client_module.html>`_

Met de module win_dns_client kan de DNS ingesteld worden op een server. Bij het aanmaken van een nieuwe domein of het toevoegen van een computer aan een bestaand domein, moet de DNS ingesteld worden op het adres van de ADDS/DNS server. In geval van de ADDS/DNS server zelf, wordt deze ingesteld op localhost (127.0.0.1)


Voorbeel van win_dns_client in Playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    - name: setup-dns-address
      hosts: windows
      remote_user: <gerbuikersnaam>
      become: yes 
      become_user: <gebruikersnaam>
      become_method: runas
      gather_facts: no
      tasks:
        - name: Stel DNS in op localhost en Cloudflare
          win_dns_client:
            adapter_names: 'Ethernet1'
            ipv4_addresses:
            - 127.0.0.1
            - 1.1.1.1
            log_path: c:\dns_log.txt


Module Windows Service
----------------------
Ansible documentatie: `win_service <https://docs.ansible.com/ansible/2.9/modules/win_service_module.html#win-service-module>`_

Met de module win_service kan een service beheerd worden.

Voorbeeld van gebruik win_service in een Playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    - name: Start netlogon service
      win_service:
        name: netlogon
        state: started


Overzicht alle Ansible Windows modules
--------------------------------------

Overzicht van alle Ansible `Windows modules <https://docs.ansible.com/ansible/2.9/modules/list_of_windows_modules.html>`_