

Ansible voorbereidingen
=======================


Installeren van Ansible (Ubuntu server)
---------------------------------------

1. Voer de volgende commando's uit om Ansible te installeren

.. code-block::
	
	sudo apt update

.. code-block::

	sudo apt install software-properties-common

.. code-block::

	sudo apt-add-repository --yes --update ppa:ansible/ansible

.. code-block::
	
	sudo apt install ansible

Aanmaken van de private- en public-key
--------------------------------------

Verbindingen van Ansible met de nodes gaat op basis van SSH. Een goede gewoonte is om gebruik te maken van private- en public-key. Een uitleg hierover is hier te vinden:

* :doc:`ssh-private-public-key`

Configureren Ansible Hosts
--------------------------

De configuratie van de Ansible hosts worden gedaan in het bestand **/etc/ansible/hosts**

* :doc:`ansible-hosts`

Configuaratie Ansible
---------------------

* `Ansible configuratie`_

Eenvoudige test werking Ansible
-------------------------------

.. code-block::

	ansible -m ping linux

Response:

.. code-block::

	192.168.56.236 | SUCCESS => { 
	"ansible_facts": { 
	"discovered_interpreter_python": "/usr/bin/python3" 
	}, 
	"changed": false, 
	"ping": "pong" 
	} 
	192.168.56.238 | SUCCESS => { 
	"ansible_facts": { 
	"discovered_interpreter_python": "/usr/bin/python3" 
	}, 
	"changed": false, 
	"ping": "pong" 
	} 
	192.168.56.237 | SUCCESS => { 
	"ansible_facts": { 
	"discovered_interpreter_python": "/usr/bin/python3" 
	}, 
	"changed": false, 
	"ping": "pong" 
	} 

.. External links

.. _`Ansible configuratie`: https://raw.githubusercontent.com/Poly1305/ansible-orchestration/master/jeroen/ansible-config/ansible.cfg?token=AB26NX7P6XIEUJULLQFSKV3AL46OE