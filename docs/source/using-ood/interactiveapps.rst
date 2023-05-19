.. _accessing_ood:

*****************************
Using OOD's Interactive Apps
*****************************

There are a number of applications that you can access and use through the OOD web portal.
When you select an application and click launch, the scheduler (Slurm) allocates a compute node with
a predetermined number of cores and amount of memory. The default time for running any of the
applications is one hour. It is recommended that you keep the default. If you ask for more than one
hour, you will need to wait for Slurm to allocate a resource that can run for your requested time,
which could take a long time to be allocated, depending on how busy the cluster is.

If you are attempting to run a job on one of the interactive apps on OOD that launches a graphical user interface (GUI), such as Maestro, you might get an error if your passwordless ssh is not set up
correctly. See :ref:`using_x11` for tips and troubleshooting information opening applications that use X11 forwarding.

Available Apps (November 2021)
================================
On the Interactive Apps tab, you can view the list of available interactive apps through the OOD web interface.

.. image:: /images/ood_apps_2021.jpg
  :alt: A list of interactive apps on OOD including FSL, Gaussian, IGV, KNIME, MATLAB, Maestro, MySQL, SAS, SPSS, STATA, Jupyter Notebook.

.. note::
   Some apps are reserved for specific research groups and are not for general access. If you get an access error when attempting to
   open an app, and you believe that you should have access to it, please email rchelp@northeastern.edu with your username,
   research group, the app you are trying to access, a screenshot of the error that you are getting, and we will
   look into the issue.

1. In a web browser, go to ood.discovery.neu.edu. If prompted, enter your myNortheastern username and password.

2. Select **Interactive Apps**, then select the application you want to use.

3. For most apps, keep the default options, and then click **Launch**. You might have to wait a
   minute or two for a compute node to be allocated with your requested time and resource.

4. If you selected Jupyter Notebook, click **Connect to Jupyter**.
   A Jupyter Notebook opens in a new tab on your browser.

.. tip::
  On the Jupyter Notebook Home tab, click **New**, then select the kernel you want to use, such as Python or R.
  Your selected kernel opens in a new tab on your browser. Click the **Running** tab to see a
  list of what Notebooks you already have running.
  If you already have a Notebook saved to your home directory, on the **Files** tab,
  click the name of the file to restart the Notebook in a new tab on your browser.

Working with JupyterLab Notebook
================================

One of the interactive apps on OOD is JupyterLab Notebook. You need to do some initial
setup in order to use this app effectively. This section will provide a walkthrough of setting up and using this app.
The general workflow is to first create a virtual python environment; ensure that Jupyter Notebook is installed in your virtual
environment; and then reference this environment when you start the JupyterLab Notebook OOD interactive app.

You can find the JupyterLab notebook on OOD by following these steps:

1. Go to https://ood.discovery.neu.edu/
2. Click on Interactive Apps
3. Select JupyterLab Notebook from the dropdown list


The OOD form for launching JupyterLab notebook looks like this:

.. image:: /images/jupyterlab_form.PNG

In the remainder of this section we will go over each of these fields.

Working Directory
------------------

This field contains the absolute file path to the directory from where the JupyterLab instance will be started. 
In the image above, the working directory is set to /home/k.joisher (By default the working directory is set to the home directory of the user).
On launching the JupyterLab instance with this working directory, we can see the contents of the home directory in the file explorer 

.. image:: /images/jupyterlab_workingdirectory.PNG

Partition
----------

This field contains the partition on which the JupyterLab session would run. Different partitions have different limits on the time, CPU and memory resources.
You can find more information about these partitions on the following link: https://rc-docs.northeastern.edu/en/latest/hardware/partitions.html .

If you want to use GPU for your JupyterLab session then select the gpu; or multigpu if you have access to that partition. Once you select either of these partitions, additional fields will be displayed on the form which ask for 
GPU type, CUDA version and number of gpus. You can find additional information about the various GPU types on the following page: https://rc-docs.northeastern.edu/en/latest/using-discovery/workingwithgpu.html .

.. image:: /images/jupyterlab_gpu.PNG


Computing resources (CPU, Time, Memory)
---------------------------------------

There are three fields on the form that allow you to configure the computational resources required for your JupyterLab sessions: CPU, Time and Memory. For GPU resources, refer the 'Partition' section above.
You can select up to 128 CPUs without GPU, and up to 12 CPUs with a GPU.
In the Time field, enter the number of hour(s) needed for the job. Minimum is one hour, maximum is 8 hours.
In the Memory (in Gb) field, enter the amount of memory you need for the job. Minimum is 2GB, maximum is 128GB.

Conda virtual environment
-------------------------

You can import python packages in your JupyterLab Notebook session by creating a conda virtual environment and activating that environment when starting a JupyterLab Notebook instance.
The fields in the image below are used to import a conda environment.

.. image:: /images/jupyterlab_conda.PNG

The steps below demonstrate A. how to create a virtual conda environment and B. launching JupyterLab session with the virtual conda environment:

A. Creating conda virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Connect to Discovery shell. You can use any one of the below 3 approaches to connect to Discovery:
	1. To connect using Windows, refer :ref:`connect_windows`
	2. To connect using Mac, refer :ref:`connect_mac`
	3. To connect using OOD, refer :ref:`access_ood`
	
2. Switch to a compute node from the login node before we create our custom conda environment. You can run the following command to switch to a compute node:
	``srun --partition=short --nodes=1 --cpus-per-task=1 --pty /bin/bash``

3. You can view the available anaconda modules by running the following command:
	``module avail anaconda``

4. Load the desired anaconda module from the above list by running the following command:
	``module load <anaconda_module_name>``
	
	For e.g. ``module load anaconda3/2022.05``

5. Create an anaconda environment by running the following command:
	``conda create -n <yourenvironmentname>``
	
	For e.g. ``conda create -n example_virtual_env``

6. Activate your environment by running the following command:
	``source activate <yourenvironmentname>``
	
	For e.g. ``source activate example_virtual_env``

7. Install Jupyterlab packages so that you can use your dependencies in Jupyterlab Notebook:
	``conda install -n example_virtual_env Jupyter``
	
	``conda install -n example_virtual_env jupyterlab``

8. Install the packages you want using the following command:
	``conda install -n <yourenvironmentname> <package>``
	
	For e.g. ``conda install -n example_virtual_env torch``


B. Launching JupyterLab Notebook session with the virtual conda environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Go to http://ood.discovery.neu.edu and login
- Click on Interactive Apps > Jupyterlab Notebook
- Fill in the form for the Jupyterlab Notebook session
- For the 'System-wide Conda Module:' field, select the anaconda module you loaded in step 4 of section A.
- Check the 'Custom Anaconda Environment (provide name only)' option
- Under the 'Name of Custom Conda Environment' field, enter the name of the environment you created in step 5 (for e.g. example_virtual_env)
- Click Launch

When your Jupyter Notebook is running and open, type ``conda list`` in a cell and run the cell to confirm that the environment is your custom conda environment (you should see this on the first line). This command will also list all
of your available packages.
