Ansible Hosts
=============


Ansible Linux hosts
-------------------

Linux servers en computers in Ansible host-lijst

.. code-block::

   [linux]
   192.168.56.236
   192.168.56.237
   192.168.56.238

   [linux:vars]
   ansible_user=<username>
   anible_become_pass=<username>
   ansible_sudo_pass=<password>

Ansible Windows hosts
---------------------

Windows servers en computers in Ansible host-lijst

.. code-block::

   [windows]
   192.168.56.239

   [windows:vars]
   ansible_user=<username>
   ansible_password=<password>
   ansible_connection=ssh
   ansible_ssh_port=22
   ansible_shell_type=<cmd or powershell>

De variabele **ansible_shell_type** moet de DefaultShell weegeven die op de Windows-host is geconfigureerd. Stel in op **cmd** voor de standaardshell of stel in op **powershell** als de DefaultShell is gewijzigd in PowerShell. 