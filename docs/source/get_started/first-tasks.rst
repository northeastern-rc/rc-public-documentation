************
First Tasks
************
.. _getting_access:

Getting Access
==============
You must first have an account before you can access Discovery. You request an account through ServiceNow. You will need a Northeastern username and password to access ServiceNow. If you are new to the university or a visiting researcher, work with your sponsor to get an Northeastern username and password.

**To request an account, follow these steps:**

1. Go to `ServiceNow <https://northeastern.service-now.com/research?id=nurc_category>`_.

2. Fill out the form, check the acknowledgement box, and click Submit.

Your request can take up to 24 hours to process. You will receive a confirmation email when your access has been granted.
After you have access, if you are not familiar with using Discovery, high performance computing, or Linux, you should take one of our training courses.
See the `Research Computing website <https://rc.northeastern.edu/support/training/>`_ for more information on our training and services.

Connecting to Discovery
=======================
You connect to Discovery using a `secure shell <https://www.ssh.com/ssh/protocol/>`_ program and initiate an SSH session to
log into Discovery.

Mac
~~~~
Mac computers come with a Secure Shell (SSH) program called `Terminal <https://support.apple.com/guide/terminal/welcome/mac>`_
that you use to connect to Discovery using SSH.

**To connect to Discovery on a Mac:**

1. Open Terminal.

2. Type ``ssh <username>@login.discovery.neu.edu`` , where ``<username>`` is your Northeastern username.

3. Type your Northeastern password and press Enter.

You are now connected to Discovery at a login node.

.. caution::

   Never launch a job from the login node.
   Jobs that are launched from the login node will be terminated.
   Move to a compute node before running any jobs.

Windows
~~~~~~~
Before you can connect to Discovery on a Windows computer, you’ll need to download a terminal program,
such as MobaXterm or PuTTY. We recommend MobaXterm, as you can also use it for file transfer,
whereas with other SSH programs, you would need a separate file transfer program.

**To connect to Discovery with MobaXterm:**

1. Open MobaXterm.

2. Click **Session**, then click **SSH** as the connection type.

3. In **Remote Host**, type ``login.discovery.neu.edu``, make sure **Port** is set to 22, and click **OK**. You do not need to enter a username.

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

- See :ref:`submitting_jobs` for information about using ``sbatch``.
