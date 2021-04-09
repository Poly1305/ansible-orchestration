Ansible Opties
==============
.. [name]

De naam van een play of van een task

.. [hosts]

De hosts waarop het playbook wordt uitgevoerd

.. [remote_user]

De gebruiker waarmee verbinding wordt gemaakt

.. [become]

Het verkrijgen van administrator provileges om taken uit te kunnen voeren

.. [become_user]

De gebruiker waarmee administrator privileges verkregen worden

.. [become_method]

De methode die gebruikt wordt voor het instellen van de manier waarop de administrator privileges
moeten worden verkregen. Voor Windows is dat ``runas`` en voor Linux is dat ``sudo`` of ``su``

.. [vars_files]

Onder deze optie kunnen bestanden met variablen worden gekoppeld.

.. [include_vars]

Een andere manier om variablen toe te voegen aan een playbook. Zie voorbeeld over het gebruik van deze manier voor het gebruiken van variabelen in een playbook.

.. [gather_facts]

Verzamel informatie en koppel deze aan variablen die gebruikt kunnen worden in het playbook. 
Meer over gather_facts variablen zijn `hier <https://linuxhandbook.com/ansible-variables-facts-registers/>`_ terug te vinden.


Voorbeeld gebruik van Ansible opties met vars_file
--------------------------------------------------

.. code-block:: yaml

   - name: play-name
     hosts: "{{ host }}"
     remote_user: "{{ user }}"
     become: yes
     become_user: "{{ user }}"
     become_method: runas
     gather_facts: yes
     vars_files:
       - vars-playbook.yml
     tasks:
       - name: Uit te voeren taak
       ansible_module:
         module_optie_1: "{{ optie1 }}"
         module_optie_2: "{{ optie2 }}"
         module_optie_3: "{{ optie3 }}"

Voorbeeld include_vars
----------------------

.. code-block:: yaml

   - name: play-name
     hosts: "{{ host }}"
     remote_user: "{{ user }}"
     gather_facts: yes
     tasks:
       - name: Definieer vars bestand 1
         include_vars:
           file: vars-playbook.yml
           name: var
       - name: Uit te voeren taak
         ansible_module:
           module_optie_1: "{{ var.optie1 }}"
           module_optie_2: "{{ var.optie2 }}"
           module_optie_3: "{{ var.optie3 }}"