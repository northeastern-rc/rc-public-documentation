.. _access_ood:

******************************
JupyterLab for your CPS class
******************************
These instructions describe the process of opening a CPS JupyterLab environment on the Open OnDemand (OOD) Discovery web portal and accessing class work directories.

.. note::
   Due to several reports about problems using the Safari browser on OOD, it is recommended to use Google Chrome, Mozilla Firefox or Microsoft Edge browsers for best experience. Use any modern browser that supports ECMAScript 2016 (see: `OnDemand Documentation <https://osc.github.io/ood-documentation/latest/requirements.html#browser-requirements>`_).  

Step 1 - access your CPS Class JupyterLab environment
=====================================================
 1. Ensure with your class instructor that a `Discovery Classroom Use Request <https://bit.ly/NURC-Classroom>`_ was requested by the instructor. You will only be able to find your class resources if a request was made. 

 2. In a web browser, go to http://ood.discovery.neu.edu. Login with your NU credentials (follow (see more information here :ref:`connect_ood`).

 3. Under the **Courses** menu, select your Class Name.

.. image:: /images/cps-ood-menu.png
 :width: 400
 :alt: A menu dropdown list of classes, with a CPS ALY3070 class highlighted.

For example: **ALY3070 JupyterLab**.

 4. Select the default options and click **Launch**.

.. image:: /images/cps-ood-jupyterform.png
 :width: 400
 :alt: A form of the cps jupyterlab options.

For more control of the session, modify **Time** for the session time (in hours), **Memory** to get more memory in GB, and the **Working Directory** where JupyterLab launches.

.. note::
   If **Working Directory** left blank, the session will launch in the main class folder (in this example `/work/cps/ALY3070`). This folder has read-only permissions. Additionally, each student has access to a personal working directory (read+write) under: `/work/cps/ALY3070/students/[username]`, where `[username]` is the student username on Discovery. 

Wait until the session is successfully created and started (turns green).

 5. Click **Connect to Jupyter** to open JupyterLab.
 
.. image:: /images/cps-ood-jupyterlab-start-session.png
 :width: 400
 :alt: session created view. 

This will open a JupyterLab interface in another tab.

 6. Select **Cancel** when prompted with the **Build Recommended** option. 

.. image:: /images/cps-ood-build-window.png
 :width: 400
 :alt: build window view.

The package jupyterlab-dash does not require a build, and will not work when build is enabled.

Step 2 - access your class directories
=======================================
After you are connected to a CPS JupyterLab session on OOD, you can access any shared class directories and your private class directory.

1. You can navigate between the class folders using the left menu. Your instructor may share files in this directory.

.. image:: /images/cps-ood-jupyterlab-folders-view.png
 :width: 400
 :alt: show files.

For instance, file **Example.ipynb** can be viewed using Python Jupyter Notebook (but not edited or removed).

2. Navigate to the **students** directory, where you will see another directory under your username.

.. image:: /images/cps-ood-jupyterlab-students-folder.png
 :width: 400
 :alt: show students folder.

Enter your personal class directory.

.. image:: /images/cps-ood-jupyterlab-username-folder.png
 :width: 400
 :alt: show inside username folder.

Here you can create and edit files. 

3. Open a new Python Notebook session from the Launcher menu by clicking the **Python 3 (ipykernel)**. 

.. image:: /images/cps-ood-jupyterlab-ipykernel-launcher.png
 :width: 400
 :alt: show inside ipykernel.

A new file will be created inside your directory called **Untitled.ipynb**. You can rename it by right-click + Rename option. 

.. image:: /images/cps-ood-jupyterlab-ipykernel.png
 :width: 400
 :alt: show inside ipykernel.

This Python notebook has ready-to-use Python packages needed for your class.

.. note:: 
  **Permission Denied errors**
  Do not attempt to create, edit or write files that are outside of your personal student directory. Most "Permission Denied" errors are due to directories or files having read-only access permissions. 

Step 3 - submit class assignments
=================================
Due to the write-only access permissions on the **assignments** directory, it is required to use the command line interface to submit assignments. Copying the assignment file using the folder navigator menu will not work.

1. To submit your assignment (for example, named: **Assignment1.ipynb**) to the **assignments** directory, open the JuypterLab New Launcher by clicking the **File** top menu option, and then selecting **New Launcher**.

.. image:: /images/cps-ood-jupyterlab-new-launcher.png
 :width: 400
 :alt: open new launcher.

2. Click on the **Terminal** option under **Other** to open a Linux terminal.

.. image:: /images/cps-ood-jupyterlab-open-terminal.png
 :width: 400
 :alt: open terminal.

3. Navigate to your personal directory by typing the following command (change the class name from ``ALY3070`` to your class name accordingly) ::

  cd /work/cps/ALY3070/students/$USER

Where ``$USER`` is a saved shell variable for your username. You can optionally also replace it with your username.

4. Check that your assignment file is visible in the command line by typing ::

  ls

5. Copy the assignment file to the **assignments** directory with this command (replace **Assignment1.ipynb** with your file name) ::

  cp Assignment1.ipynb ../../assignments

To remove an existing assignment, type (replace **Assignment1.ipynb** with your file name) ::

  rm ../../assignments/Assignment1.ipynb

.. image:: /images/cps-ood-commandline.png
 :width: 400
 :alt: commandline commands.

6. Close the Terminal tab when done.
