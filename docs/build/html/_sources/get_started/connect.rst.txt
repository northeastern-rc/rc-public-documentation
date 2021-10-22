*************************
Connecting to Discovery
*************************
You connect to Discovery using a `secure shell <https://www.ssh.com/ssh/protocol/>`_ program to initiate an SSH session to
sign in to Discovery. Mac and Windows have slightly different procedures for connecting, as detailed below. If you usually launch software
from the command line that uses a graphical user interface (GUI), see :ref:`using_x11` for tips and troubleshooting information.

.. 2FA Authentication with DUO
.. ============================
.. When you connect to Discovery you are required to complete two-factor authentication (2FA) using the app Duo. All Northeastern staff, faculty, and students
.. should already have Duo, as it is used with many other online campus resources, such as Canvas and myNortheastern. To learn more about using Duo,
.. go to `Northeastern's 2FA informational website <https://get2fa.northeastern.edu/>`_.

Mac
===
Mac computers come with a Secure Shell (SSH) program called `Terminal <https://support.apple.com/guide/terminal/welcome/mac>`_
that you use to connect to Discovery using SSH. If you need to use software that uses a GUI, such as Matlab or Maestro, make sure to use the -Y option in the second step below (see :ref:`using_x11` for more tips and troubleshooting information).

.. note::
   If you use Mac OS X version 10.8 or higher, and you have `XQuartz <https://www.xquartz.org/>`_ running in the background to do X11 forwarding, you should execute the following command in Terminal once before connecting to Discovery:

   ``defaults write org.macosforge.xquartz.X11 enable_iglx -bool true``

   You should keep XQuartz running in the background. If you close and restart XQuartz, you will need to execute the above command again after restarting. Do not use the Terminal application from within XQuartz to sign in to Discovery. Use
   the default Terminal program that comes with your Mac (see Step 1 in the procedure below).

**To connect to Discovery on a Mac:**

1. Go to Finder > Applications > Utilities, and then double click Terminal.

2. At the prompt, type ``ssh <username>@login.discovery.neu.edu``, where ``<username>`` is your Northeastern username. If you need to use X11 forwarding, type ``ssh -Y <username>@login.discovery.neu.edu``.

3. Type your Northeastern password and press Enter.

You are now connected to Discovery at a login node.


Windows
========
Before you can connect to Discovery on a Windows computer, you’ll need to download a terminal program,
such as MobaXterm or PuTTY. We recommend MobaXterm, as you can also use it for file transfer,
whereas with other SSH programs, you would need a separate file transfer program.

**To connect to Discovery with MobaXterm:**

1. Open MobaXterm.

2. Click **Session**, then click **SSH** as the connection type.

3. In **Remote Host**, type ``login.discovery.neu.edu``, make sure **Port** is set to 22, and click **OK**.
   (OPTIONAL: You can type your Northeastern username and password on MobaXterm, and it will save that information every time you sign in. If you opt to do this, you will be connected to Discovery after you click OK.)

4. At the prompt, type your Northeastern username and press Enter.

5. Type your Northeastern password and press Enter. Note that the cursor does not move as you type your password. This is expected behavior.

You are now connected to Discovery at a login node.

.. _using_x11:

Using X11
==========
When you launch a software application that uses a graphical user interface (GUI) from the command line, this is completed through X11 forwarding. If you use MobaXterm on Windows, X11 forwarding
is turned on by default. If you use the Terminal program on Mac, you'll need to login using the -Y option (``ssh -Y <yourusername>@login.discovery.neu.edu``).

.. tip::
   If you used the -Y option to enable X11 forwarding on your Mac, you can test to see if it is working by typing ``xeyes``. This will run a small program that makes
   a pair of eyes appear to follow your cursor.

Passwordless ssh
+++++++++++++++++
You need to setup passwordless ssh to ensure that GUI-based applications will launch without any issues. You also
need to make sure that your keys are added to the authorized.key file. This needs to be done anytime you regenerate your keys. If you're having
an issue with opening an application that need X11 forwarding, such as MATLAB or Schrodinger, and you recently regenerated your keys, make sure to
add your keys to the authorized.key file.

.. note::
   Errors that you can see on both Mac and Windows when launching a GUI-based program include the following:

   ``Error: unable to open display localhost:19.0``

   ``Launch failed: non-zero return code``

  If you are getting these types of errors, follow the steps below to set up passwordless ssh. If you are on a Mac, complete all of the steps.
  If you are on Windows, sign in to Discovery using MobaXterm, then follow the procedure below starting at **step 9**.


**To setup passwordless ssh:**

1. On a Mac, open Terminal and type, ``cd ~/.ssh``. This moves you to the ssh folder on your local computer. **Note**: Make sure you're on your local computer for steps 1 through 4. If you are connected to Discovery, type ``exit`` to return to your local computer.
2. Type ``ssh-keygen -t rsa`` to generate two files: ``id_rsa`` and ``id_rsa.pub``.
3. Press ``Enter`` to all of the prompts (do not generate a passphrase).
4. Type ``ssh-copy-id -i ~/.ssh/id_rsa.pub <yourusername>@login.discovery.neu.edu`` to copy ``id_rsa.pub`` to your /home/.ssh folder on Discovery. Enter your NU password if prompted.
5. Connect to Discovery by typing ``ssh <yourusername>@login.discovery.neu.edu``.
6. Type ``cd ~/.ssh ; cat id_rsa.pub >> authorized_keys``. This moves you to your ssh folder and adds the contents of your public key file to a new line in the ~/.ssh/authorized_keys file.
7. Log out by typing ``exit``.
8. Connect to Discovery again by typing ``ssh <yourusername>@login.discovery.neu.edu``. **Note**: If you are using a Windows machine using MobaXterm, sign in to Discovery as usual, then complete steps 9 through 12 to complete the passwordless ssh setup.
9. Type ``cd ~/.ssh`` to move to your ssh folder.
10. Type ``ssh-keygen -t rsa`` to generate your key files.
11. Press ``Enter`` to all of the prompts (do not generate a passphrase). If prompted to overwrite a file, type ``Y``.
12. Type ``cat id_rsa.pub >> authorized_keys``. This adds the contents of your public key file to a new line in the ~/.ssh/authorized_keys file.

Next steps
===========
After you are connected, you can run jobs either in interactive mode with ``srun`` or submit a script using ``sbatch``. See :ref:`using_srun` and :ref:`using_sbatch` for more information.

To load and run software, see :ref:`software_overview`.
To find out more about the hardware and partitions on Discovery, see :ref:`hardware_overview` and :ref:`partition_names`.

To watch an introductory training video, go to `Northeastern's LinkedIn Learning page <https://www.linkedin.com/checkpoint/enterprise/login/74653650?pathWildcard=74653650&application=learning&redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Flearning%2Fcontent%2F1139340%3Fu%3D74653650>`_.
