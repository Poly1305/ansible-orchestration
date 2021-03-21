
Linux modules
=============

.. _module_docker_container:

Module Docker Container
-----------------------
Ansible documentatie: `docker_container`_

Voorbeeld Playbook (Watchtower)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

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

Module Docker Network
---------------------
Ansible documentatie: `docker_network`_

Voorbeeld Playbook
~~~~~~~~~~~~~~~~~~

Maak het **web** netwerk aan voor gebruik in de :ref:`module_docker_container` module

.. code-block::

  # Create web network
  - name: create web network
    docker_network:
      name: web      

Module File
-----------
Ansible documentatie: `file`_

Voorbeeld Playbook
~~~~~~~~~~~~~~~~~~
Maak een aantal folders aan

.. code-block::

  - name: create necessary folders
    file:
      path: "{{ item }}"
      owner: user
      group: sudo
      mode: 0755
      state: directory
    with_items:
      - /home/user/docker
      - /home/user/docker/portainer
      - /home/user/docker/portainer/data
      - /home/user/docker/watchtower

Module APT
----------
Ansible documentatie: `apt`_

Voorbeelden
~~~~~~~~~~~

Update repositories

.. code-block::
	
  - name: update repositories
    apt:
      update_cache: yes

Installeer software packages

.. code-block::

  - name: install packages
    apt:
      pkg:
        - apt-transport-https
        - ca-certificates
        - curl
        - software-properties-common

Installeer software

.. code-block::
	
  - name: update repositories and install docker
    apt:
      update_cache: yes
      name: docker-ce
      state: latest


Module Command
--------------
Ansible documentatie: `command`_

Voorbeelden
~~~~~~~~~~~

Toevoegen van een gebruiker aan een groep

.. code-block::
	
  - name: add user <username> to docker group
    command: usermod -aG docker <username>

Starten van een service

.. code-block::

  - name: auto start docker service
    command: systemctl enable --now docker.service


Module Get URL
--------------
Ansible documentatie: `get_url`_

De module get_url is het Ansible alternatief voor het curl commando in Linux.

Voorbeeld in Playbook
~~~~~~~~~~~~~~~~~~~~~

.. code-block::

  - name: get new bash rc from github
    get_url:
      url: https://<url>
      dest: /path/to/destination/file

Module Copy
-----------
Ansible documentatie: `copy`_

Met de copy module kan een bestand of tekst gekopieerd worden naar een bestand.


Voorbeeld van bestand kopieëren in Playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

  - name: Kopieer bestand en stel eigenaar en rechten in
    copy:
      src: /path/to/file.txt
      dest: /path/to/dest/file.txt
      owner: <gebruikersnaam>
      group: <groepsnaam>
      mode: '0755'

Voorbeeld van bestand kopieëren en backup maken van oude betand
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

  - name: Kopieer bestand en stel eigenaar en rechten in
    copy:
      src: /path/to/file.txt
      dest: /path/to/dest/file.txt
      owner: <gebruikersnaam>
      group: <groepsnaam>
      backup: yes

Voorbeeld van tekst in een bestand kopieëren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Bijkomend voordeel, als het bestand niet bestaat zal deze aangemaakt worden

.. code-block::

   - name: Kopieer tekst in een bestand
     copy:
       dest: /path/to/file.txt
       content: |
         regel 1
         regel 2


Module Line in File
-------------------
Ansible documentatie: `lineinfile`_

Met de module lineinfile kan tekst aangepast worden van een bestand.


Voorbeeld teskt toevoegen aan het einde van een bestand
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::
   - name: Voeg tekst toe aan het einde van een bestand
     lineinfile:
       dest: "/path/to/file.txt"
       insertafter: ""
       line: "de nieuwe tekst"
       state: present
       backup: yes


Voorbeeld bestaande tekst aanpassen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    - name: wijzig tekst
      lineinfile:
        dest: "/path/to/file.txt"
        regexp: "^Tekst"
        line: "Nieuwe tekst"


Voorbeeld tekst toevoegen meerdere regels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    - name: wijzig tekst
      lineinfile:
        dest: "/path/to/file.txt"
        insertbefore "^tekst"
        line: |
          Regel 1
          Regel 2
          Regel 3


Module Service
--------------
Ansible Documentatie: `service`_


Voorbeeld herstarten service in Playbook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   - name: herstarten service
     service:
       name: <servicenaam>
       state: restarted




.. External links

.. _`docker_container`: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

.. _`docker_network`: https://docs.ansible.com/ansible/2.3/docker_network_module.html

.. _`file`: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html

.. _`apt`: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html

.. _`command`: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/command_module.html

.. _`get_url`: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/get_url_module.html

.. _`copy`: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html

.. _`lineinfile`: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/lineinfile_module.html

.. _`service`: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html