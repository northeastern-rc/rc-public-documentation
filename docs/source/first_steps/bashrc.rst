.. _bashrc:

*******************************
Shell environment on Discovery
*******************************

The Discovery Shell environment and .bashrc
+++++++++++++++++++++++++++++++++++++++++++

Discovery uses a Linux-based Operating System (CentOS) that uses the Shell to interface with the user. Bash (Bourne Again SHell) is one of the most popular Shell implementations whichn is the default shell on Discovery.  

The Shell script .bashrc is used by Bash to initialize your Shell environment. For example, it can be used to define shell environemnt variables (such as `PATH`) or aliases and load modules.
Your .bashrc file lives in your /home directory. You can make changes to it with a text editor like `nano <https://www.nano-editor.org/>`_.
Adding sections to your .bashrc file, such as adding modules to load when you sign in or assigning aliases for commands that you use frequently, can be time savers for your workflows.

.. caution:: Making edits to your .bashrc file can result in issues, such as not able to launch an app or not able to execute commands. Incorrect changes to your `PATH` variable may result in the inavibility to use basic Shell commands.  
             Before making changes to your .bashrc file, make a backup of the default .bashrc file so you can restore it if necessary.
             If you need help with editing your .bashrc file, reach out to rchelp@northeastern.edu or `schedule a consultation with
             a staff member <https://outlook.office365.com/owa/calendar/ResearchComputing2@northeastern.onmicrosoft.com/bookings/>`_
             who can help suggest edits and troubleshoot any issues you might be having.


About your .bashrc file
+++++++++++++++++++++++
You have a default .bashrc file in your home directory when your account is created. See the figure below for an example of a default .bashrc file.

.. image:: /images/catbashrc.jpg

.. important::
  We recommend to keep .bashrc unchanged when using Discovery. You can source environment Shell scripts or load modules directly inside your jobs instead. This apprach can prevent potential runtime errors from loading incompatible modules, setting environment variables incorrectly, or from mixing multiple software environments. 

Conda and .bashrc
++++++++++++++++++

In addition to editing your .bashrc file as outlined in the example above, programs that you install can also modify your .bashrc file. For example, if you
follow the procedure outlined in :ref:`mini_conda`, there will be a section added to your .bashrc file that automatically loads your conda environment every time you sign in to Discovery. See the figure below for an example of this:

.. image:: /images/minicondabashrc.jpg

You should not modify this section in the .bashrc file directly. If it was change, remove this section manually using a file editor.

.. caution:: We recommend removing the conda initialize section from your .bashrc as it may interfere with the correct startup environment when using Open OnDemand apps. You should always load your Conda environment after your job already started.

If you need help with your .bashrc file or would like it restored to its default, reach out to the RC team at rchelp@northeastern.edu, and we can provide you with
a new, default .bashrc file and/or help troubleshoot issues with the file.

Editing your .bashrc file
=========================
The basic workflow for editing your .bashrc file is to sign in to Discovery, go to your /home directory,
open the file in a text editor on the command line, make your edits, save the file, sign out of Discovery, then sign back in again.
Your changes will take effect when you have signed back in again.

Example procedure for editing your .bashrc file:

1. Sign in to Discovery.
2. (Optional) Type PWD to make sure you are in your /home directory.
3. (Optional) Type ``ls -a`` to view the contents of your /home directory, including hidden files. Your .bashrc file is a hidden file (hidden files are preceded by a ``.`` ). Using the ``-a`` option with ``ls`` displays hidden files.
4. (Recommended) Type ``cp .bashrc .bashrc-default`` to make a copy of your .bashrc file called ``.bashrc-default``.
5. Type ``nano .bashrc`` to open your .bashrc file in the nano text editor.
6. Type the edits that you want to make to your file. In this example, an alias was added to create a shortcut to the user's /scratch space.

   .. image:: /images/nanobashrc.png

7. Save the file and exit the editor.
8. Sign out of Discovery and sign back in for the changes to take effect.
