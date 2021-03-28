
Windows voorbereidingen
=======================

Voor het opzetten van de OpenSSH server op Windows kan gebruik worden gemaakt van het openssh-server. Het script voert de volgende handelingen uit:

* Installeer OpenSSH server
* Configureer de OpenSSH server
* Kopieer de public key van de master naar Windows

Link naar `OpenSSH Server Setup Script`_

Installeer OpenSSH server Windows
---------------------------------

1. Installeer OpenSSH server op Windows

.. code-block::

	Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

2. Start de OpenSSH server

.. code-block::

	Start-Service sshd

3. Controleer of de OpenSSH server is geinstalleerd

.. code-block::

	Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'

3. Start OpenSSH server automatisch bij het opstarten van Windows

.. code-block::

	Set-Service -Name sshd -StartupType 'Automatic'

4. Pas de Firewall aan voor OpenSSH server

.. code-block::

	New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22

Configureer de OpenSSH server
-----------------------------

1. Open het bestand C:\ProgramData\ssh\sshd_config met administrator privileges

2. Wijzig de regels in het bestand naar de onderstaande tekst

.. code-block::

   PubkeyAuthentication yes
   PasswordAuthentication no
   #Match Group administrators
       #AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys

3. Herstart de OpenSSH server

.. code-block::

   Restart-Service sshd


Voeg de Public key toe aan authorized_keys
------------------------------------------

1. Maak .ssh folder aan op de node (als deze nog niet bestaat)

.. code-block::

   New-item -Path $env:USERPROFILE -Name .ssh -ItemType Directory -force

2. Haal de Public key op bij de master

.. code-block::

	scp ~/.ssh/id_rsa.pub student@<ip-adres>:c:/users/<username>/.ssh/uploaded_key

3. Voeg de Public key toe aan het **authorized_keys** bestand

.. code-block::

	Get-Content $env:USERPROFILE\.ssh\uploaded_key | Out-File $env:USERPROFILE\.ssh\authorized_keys -Append -Encoding ascii


Controleer de SSH verbinding van Linux naar Windows
---------------------------------------------------

.. code-block::

   ssh <username>@<ip-adres>

.. External Links

.. _`OpenSSH Server Setup Script`: https://github.com/jebr/windows-scripts/tree/main/openssh-server