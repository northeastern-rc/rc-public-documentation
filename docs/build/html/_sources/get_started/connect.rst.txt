.. _intro_connect:

*************************
Connecting to Discovery
*************************

You connect to Discovery using a `secure shell <https://www.ssh.com/ssh/protocol/>`_ program and initiate an SSH session to
log into Discovery. Mac and Windows have slightly different procedures for connecting, as detailed below.

Mac
===
Mac computers come with a Secure Shell (SSH) program called `Terminal <https://support.apple.com/guide/terminal/welcome/mac>`_
that you use to connect to Discovery using SSH.

.. note::
   If you use Mac OS X version 10.8 or higher, and you use `XQuartz <https://www.xquartz.org/>`_ to do X11 forwarding, you should execute the following command in Terminal once before connecting to Discovery::

      defaults write org.macosforge.xquartz.X11 enable_iglx -bool true

**To connect to Discovery on a Mac:**

1. Open Terminal.

2. Type ``ssh <username>@login.discovery.neu.edu`` , where ``<username>`` is your Northeastern username. If you need to use X 11 forwarding, type ``ssh -Y <username>@login.discovery.neu.edu``.

3. Type your Northeastern password and press Enter.

You are now connected to Discovery at a login node.

Passwordless ssh
+++++++++++++++++
If you will be using x11 forwarding, you need to setup passwordless ssh to ensure that your application will launch without any issues. You also
need to make sure that your keys are added to the authorized.key file. This needs to be done anytime you regenerate your keys. If you're having
an issue with opening an application that uses x11 forwarding, such as Matlab or Schrodinger, and you recently regenerated your keys, make sure to
add your keys to the authorized.key file.

**To setup passwordless ssh**

1. Connect to Discovery.
2. Type ``ssh-keygen`` and then accept all of the defaults. This generates your public and private keys.
3. Type ``cd ~/.ssh ; cat id_rsa.pub >> authorized_keys``. This adds the contents of your public key file to a new line in the ~/.ssh/authorized_keys file

Windows
========
Before you can connect to Discovery on a Windows computer, you’ll need to download a terminal program,
such as MobaXterm or PuTTY. We recommend MobaXterm, as you can also use it for file transfer,
whereas with other SSH programs, you would need a separate file transfer program.

**To connect to Discovery with MobaXterm:**

1. Open MobaXterm.

2. Click **Session**, then click **SSH** as the connection type.

3. In **Remote Host**, type ``login.discovery.neu.edu``, make sure **Port** is set to 22, and click **OK**. If you don't add your Northeastern username, you will be prompted for it each time you log in.

4. At the prompt, type your Northeastern username and press Enter.

5. Type your Northeastern password and press Enter. Note that the cursor does not move as you type your password. This is expected behavior.

You are now connected to Discovery at a login node.

.. caution::

   Never launch a job from the login node.
   Jobs that are launched from the login node will be terminated.
   Move to a compute node before running any jobs.

Move to a compute node
======================

You should never launch any jobs from the login node ``[username@login-00~]``. Any job launched from the login node will be terminated. You can move to a compute node using the srun command or use the sbatch command to run a job on an interactive compute node.

- To move to a compute node, at the command prompt type ``srun --pty /bin/bash``

- See :ref:`batch_jobs` for information about using ``sbatch``.
