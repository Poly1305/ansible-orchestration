Gebruikershandleiding SSH private- en public-key
================================================

.. note::
   Het Key paar moet aangemaakt worden op de lokale machine, vervolgens wordt de public key gekopieerd naar de remote computer/server.

.. note::
   Onderstaande handleiding werkt voor zowel Windows, Linux als macOS. 

Genereer private- en public-key paar
------------------------------------

1. Open de terminal of powershell
2. Voer de volgende syntax uit

.. code-block::

   ssh-keygen -t rsa -b 4096

3. Vul een wachtwoord in om de private- en public-key te beveiligen (optioneel)

4. De sleutels zullen worden opgeslagen in de **.ssh** folder

.. code-block::
    
   id_rsa
   id_rsa.pub

Kopieer de public key (handmatig)
---------------------------------
1. Maak de **.ssh** directory aan in de home folder van de huidige gebruiker op de remote computer/server
2. Kopieer de sleutel naar de remote computer/server met het de onderstaande syntax

.. code-block::

   scp ~/.ssh/id_rsa.pub <username>@<ip-adres>:/home/<username>/.ssh/uploaded_key.pub

3. Op de remote computer/server, schrijf de key naar het bestand authorized_keys om zo meer machines toe te kunnen voegen aan de remote computer/server

.. code-block::

   cat ~/.ssh/uploaded_key.pub >> ~/.ssh/authorized_keys

4. Zet de rechten goed voor de .ssh folder en de public keys (alleen voor Linux en macOS)

.. code-block::

   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/*

5. Controleer of je kunt verbindnen via de public key

.. code-block::

   ssh <username>@<ip-adres>

Kopieer de public key via SSH - automatisch (alleen voor Linux)
---------------------------------------------------------------
1. Voer onderstaande syntax uit om de public key te kopieeren naar de remote computer/server

.. code-block::
    
   ssh-copy-id <username>@<ip-adres>

2. Controleer de verbinding

.. code-block::

   ssh <username>@<ip-adres>

Uitzetten wachtwoord authenticatie Linux
----------------------------------------
1. Maak een backup van het bestand sshd_config

.. code-block::

   sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

2. Open **sshd_config** in de Nano texteditor

.. code-block::

   sudo nano /etc/ssh/sshd_config

3. Wijzig de onderstaande regel

.. code-block::

   PasswordAuthentication no

4. Herstart de SSH service

.. code-block::

   sudo service ssh restart
