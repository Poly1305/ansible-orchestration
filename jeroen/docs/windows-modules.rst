
Windows modules
===============

Module Windows Features
-----------------------
`win_feature`_

Voorbeeld Playbook
~~~~~~~~~~~~~~~~~~

.. code-block::

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
`win_reboot`_

Voorbeeld van herstarten na installeren rol/feature (In Playbook)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

	- name: Herstart server wanneer dit nodig is voor het installeren van de rol/feature
	  win_reboot:
	  when: win_feature.reboot_required  


Voorbeeld van herstarten na een bepaalde tijd (Playbook)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

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
`win_ping`_ 

Voorbeeld van win_ping in Ansible syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

	ansible -m win_ping <hosts>


Voorbeeld van win_ping in Playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block::

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
`win_domain_controller`_


.. External links

.. _`win_feature`: https://docs.ansible.com/ansible/2.8/modules/win_feature_module.html

.. _`win_reboot`: https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_reboot_module.html

.. _`win_ping`: https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html

.. _`win_domain_controller`: https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_domain_controller_module.html