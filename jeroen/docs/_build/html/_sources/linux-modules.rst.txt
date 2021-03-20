
Linux modules
=============

.. _module_docker_container:

Docker Container
----------------

Module `docker_container`_

Voorbeeld Playbook (Watchtower)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

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

Docker Network
--------------

Module `docker_network`_

Voorbeeld Playbook
~~~~~~~~~~~~~~~~~~

Maak het **web** netwerk aan voor gebruik in de :ref:`module_docker_container` module

.. code-block::

	# Create web network
	- name: create web network
	    docker_network:
	      name: web      


.. _`docker_container`: https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html

.. _`docker_network`: https://docs.ansible.com/ansible/2.3/docker_network_module.html