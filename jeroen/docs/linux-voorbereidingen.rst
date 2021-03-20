
Linux voorbereidingen
=====================


Installeer OpenSSH server Linux
-------------------------------

1. Installeer Open SSH server op Linux

.. code-block::

   sudo apt install openssh-server

2. Start OpenSSH server

.. code-block::

   sudo systemctl start sshd.service

3. Controleer of de OpenSSH server actief is

.. code-block::

   sudo systemctl is-enabled sshd.service

Voeg de Public key toe aan authorized_keys
------------------------------------------

1. Maak .ssh folder aan op de node (als deze nog niet bestaat)

2. Kopieer de Public key naar de node

.. code-block::

   scp ~/.ssh/id_rsa.pub <username>@<ip-adres>:/home/<username>/.ssh/uploaded_key.pub

3. Voeg de Public key toe aan het **authorized_keys** bestand

.. code-block::

   cat ~/.ssh/uploaded_key.pub >> ~/.ssh/authorized_keys

Uitvoeren sudo zonder wachtwoord
--------------------------------
Voor het uitvoeren van een Playbook zijn vaak administrator rechten nodig op de node. Omdat het niet verstandig is om een wachtwoord op te nemen in de Playbook (deze wordt namelijk gedeeld via GitHub) moet de groep van de gebruiker of de gebruiker zo ingesteld worden dat er geen wachtwoord nodig is voor het uitvoeren van een sudo commando. Via de volgende stappen is dit in te stellen voor een groep of afzonderlijke gebruiker. Het bestand wat aangepast gaat worden is terug te vinden op **/etc/sudoers**.

Groep sudo zonder wachtwoord
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open het bestand /etc/sudoers

.. code-block::

   sudo visudo

2. Voeg de volgende regel toe aan het bestand

.. code-block::

   %<naam van de groep> ALL=ALL(ALL:ALL) NOPASSWD:ALL

3. Voor gebruikers in de ingevoerde groep is het niet meer nodig om het wachtwoord op te geven bij het uitvoeren van het **sudo** commando


Gebruiker sudo zonder wachtwoord
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open het bestand /etc/sudoers

.. code-block::

   sudo visudo

2. Voeg de volgende regel toe aan het bestand

.. code-block::

   <gebruikersnaam> ALL=ALL(ALL:ALL) NOPASSWD:ALL

3. Voor de ingevoerde gebruiker is het niet meer nodig om het wachtwoord op te geven bij het uitvoeren van het **sudo** commando