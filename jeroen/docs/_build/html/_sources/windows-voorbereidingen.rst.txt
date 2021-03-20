
Windows voorbereidingen
=======================

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

Voeg de Public key toe aan authorized_keys
------------------------------------------

1. Maak .ssh folder aan op de node (als deze nog niet bestaat)

2. Kopieer de Public key naar de node

.. code-block::

	scp ~/.ssh/id_rsa.pub <username>@<ip-adres>:/c:/users/<username>/.ssh/uploaded_key.pub

3. Voeg de Public key toe aan het **authorized_keys** bestand

.. code-block::

	cat .ssh/uploaded_key.pub >> .ssh/authorized_keys