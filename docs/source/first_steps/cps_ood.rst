.. _access_ood:

******************************
JupyterLab for your CPS class
******************************
These instructions describe the process of opening a CPS JupyterLab environment on the Open OnDemand (OOD) Discovery web portal and accessing class work directories.


Step 1 - access your CPS Class JupyterLab environment
=====================================================
 1. Ensure with your class instructor that a `Discovery Classroom Use Request <https://bit.ly/NURC-Classroom>`_ was requested by the instructor. You will only be able to find your class resources if a request was made. 
 2. In a web browser, go to http://ood.discovery.neu.edu. Login with your NU credentials (follow (see more information here:ref:`connect_ood`).

.. note::
   Due to several reports about problems using the Safari browser on OOD, it is recommended to use Google Chrome, Mozilla Firefox or Microsoft Edge browsers for best experience. Use any modern browser that supports ECMAScript 2016 (see: `OnDemand Documentation <https://osc.github.io/ood-documentation/latest/requirements.html#browser-requirements>`_).  
 
 3. Under the **Courses** menu, select your Class Name. For example **ALY3070 JupyterLab**:

.. image:: /images/cps-ood-menu.png
 :alt: A menu dropdown list of classes, with a CPS ALY3070 class highlighted.

 4. Select the default options and click **Launch**.
.. image:: /images/cps-ood-jupyterform.png
 :alt: A form of the cps jupyterlab options.

.. note::
   You can have more control of the session by changing the **Time** field to more than 1 hour, the **Memory** field (to get more memory in GB), and the **Working Directory** where JupyterLab launches. By default, the session will launch in the main class folder (in this example `/work/cps/ALY3070`) shared with all class students. This folder has read-only permissions. Additionally, each student has access to a personal working directory under: `/work/cps/ALY3070/students/[username]`, where `[username]` is the student username on Discovery. 

 5. Once the session has been successfully created, wait until the session window starts (turns to green), and then click **Connect to Jupyter**. This will open a new tab with the JupyterLab interface. 
.. image:: /images/cps-ood-jupyterlab-start-session.png
 :alt: session created view. 

 6. Select **Cancel** when prompted with the **Build Recommended** option. Package jupyterlab-dash does not require a build, and currently doesn't work with it enabled.

.. image:: /images/cps-ood-build-window.png
 :alt: build window view.

Step 2 - access your class directories
=======================================
After you are connected to a CPS JupyterLab session on OOD, you can access any shared class directories and your private class directory.

1. You can navigate between the class folders using the left menu. Your instructor may share files in this directory, or within another directory as instructed in your class. For instance, file **Example.ipynb** can be viewed using Python Jupyter Notebook, but cannot be edited.

.. image:: /images/cps-ood-jupyterlab-folders-view.png
 :alt: show files.

2. Navigate to the **students** directory, where you will see another directory under your username. This is your personal class directory, where you can create and edit files. Navigate inside this directory.

.. image:: /images/cps-ood-jupyterlab-students-folder.png
 :alt: show students folder.

.. image:: /images/cps-ood-jupyterlab-username-folder.png
 :alt: show inside username folder.

3. Open a new Python Notebook session by clicking the **Python 3 (ipykernel)**. You will see that a new file has been created inside your directory called **Untitled.ipynb**. You can now work within this directory and remane the files (right click->Rename).

.. image:: /images/cps-ood-jupyterlab-ipykernel.png
 :alt: show inside ipykernel.

.. note:: 
  Do not attempt to edit/write into files outside your personal directory. Other directories (besides `assignments`) have read-only access permissions.  

Step 3 - submit class assignments
=================================
Once you're ready to submit your assignment Jupyter Notebook file, you'll need to use the command line option to copy it over to the **assignments** directory. This is due to the write-only access permissions on that directory, which prevents JupyterLab form copying it via its interface.

1. Suppose you have a file inside your personal class directory called **Assignment1.ipynb**. To copy it over to the **assignments** directory, open the JuypterLab New Launcher by clicking the **File** top menu option, and then selecting **New Launcher**.

.. image:: /images/cps-ood-jupyterlab-new-launcher.png
 :alt: open new launcher.

2. Click on the **Terminal** option under **Other** to open a Linux terminal.

.. image:: /images/cps-ood-jupyterlab-open-terminal.png
 :alt: open terminal.

3. Navigate to your personal directory by typing the following command (change the class name from `ALY3070` to your class name accordingly):

  `cd /work/cps/ALY3070/students/$USER`

Where `$USER` is a saved shell variable for your username. You can optionally also replace it with your username.

.. image:: /images/cps-ood-jupyterlab-cd-student-dir.png
 :alt: cd to the student dir.

4. Check that your assignment file is visible in the command line by typing:

  `ls`

.. image:: /images/cps-ood-jupyterlab-ls-student-dir.png
 :alt: ls the student dir.

5. Copy the assignment file to the **assignments** directory with this command (replace the file name with your own file name):

  `cp Assignment1.ipynb ../../assignments`

.. image:: /images/cps-ood-jupyterlab-cp-student-assignment.png
 :alt: copy student assignment.

6. Navigate to the **assignments** directory on the folder navigator on your left menu and check if your assignment is there.

.. image:: /images/cps-ood-jupyterlab-check-assignments.png
 :alt: check student assignments.

You may also remove your file if you need to by typing this command (replace the file name with your own file name):

`rm ../../assignments/Assignment1.ipynb`

7. Close the Terminal tab when done.
