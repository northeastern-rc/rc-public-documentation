(accessing-ood)=

# OOD Interactive Apps

The OOD web portal provides a range of applications. Upon clicking *launch*, the Slurm scheduler assigns a compute node with a specified number of cores and memory. By default, applications run for one hour. If you require more than an hour, you may have to wait for Slurm to allocate resources for the duration of your request.
## Applications on OOD

:::{image} ../images/ood_apps_2023_06.png
---
alt: an image the OOD apps (06-2023).
scale: 40%
align: right
---
:::

The Open OnDemand interface offers several applications, which as of June 2023, include:
- JupyterLab
- RStudio (Rocker)
- Matlab
- Schrodinger (Maestro)
- Desktop
- Gaussian (Gaussview)
- KNIME
- Tensorboard
- SAS


These applications can be accessed from the OOD web interface's **Interactive Apps** dropdown menu.

Please note that specific applications in the **Interactive Apps** section, particularly those with graphical user interfaces (GUIs), may require X11 forwarding and the setup of passwordless SSH. For tips and troubleshooting information on X11 forwarding setup and usage, please refer to the [Using X11] section of our documentation.

Additionally, we offer a selection of modified standard applications intended to support specific coursework. These applications are under the **Courses** menu on the OOD web interface. Please note that these course-specific applications are only accessible to students enrolled in the respective courses.



:::{note}
Certain apps are reserved for specific research groups and are not publicly accessible, as indicated by the "Restricted" label next to the application name. If you receive an access error when attempting to open a restricted app, and you believe you should have access to it, please email <rchelp@northeastern.edu> with the following information: your username, research group, the app you are trying to access, and a screenshot of the error message. We will investigate and address the issue.
:::

1. Go to [Open On Demand] in a web browser. If prompted, enter your myNortheastern username and password.
1. Select **Interactive Apps**, then select the application you want to use.
1. Keep the default options for most apps, then click **Launch**. You might have to wait a minute or two for a compute node to be available for your requested time and resource.

## JupyterLab Notebook

JupyterLab Notebook is one of the interactive apps on OOD. This section will provide a walkthrough of setting up and using this app. The general workflow is to create a virtual Python environment, ensure that JupyterLab Notebook uses your virtual environment, and reference this environment when you start the JupyterLab Notebook OOD interactive app.

To find the JupyterLab Notebook on OOD, follow these steps:

1. Go to [Open On Demand].
1. Click on Interactive Apps.
1. Select JupyterLab Notebook from the dropdown list.

The OOD form for launching JupyterLab Notebook will appear.

:::{tip} Conda virtual environment
You can import Python packages in your JupyterLab Notebook session by creating a conda virtual environment and activating that environment when starting a JupyterLab Notebook instance.

1. First, set up a virtual Python environment. See {ref}`creating-python` for how to set up a virtual Python environment on the HPC using the terminal.
1. Type `source activate <yourenvironmentname>` where `<yourenvironmentname>` is the name of your custom environment.
1. Type `conda install jupyterlab -y` to install jupyterlab in your environment.
:::

###  Using OOD to launch JupyterLab Notebook
1. Go to [Open On Demand].
1. Click **Interactive Apps**, then select **JupyterLab Notebook**.
1. Enter your **Working Directory** (e.g., `/home/<username>` or `/work/<project>`) that you want JupyterLab Notebook to launch in.
1. Select from the **Partition** dropdown menu the partition you want to use for your session. Refer to {ref}`partition-names` for the resource restrictions for the different partitions. If you need a GPU, select the `gpu` partition.
1. Select the compute node features for the job:
   - In the **Time** field, enter the number of hour(s) needed for the job.
   - Enter the memory you need for the job in the **Memory (in Gb)** field.
   - If you selected the `gpu` partition from the dropdown menu, select the GPU you would like to use and the version of CUDA that you would like to use for your session under the respective dropdown menus.

1. Select the Anaconda version you used to create your virtual Python environment in the **System-wide Conda Module** field.
1. Check the **Custom Anaconda Environment** box, and enter the name of your custom virtual Python environment in the **Name of Custom Conda Environment** field.
1. Click **Launch** to join the queue for a compute node. This might take a few minutes, depending on your requested resources.
1. When you have been allocated a compute node, click **Connect to Jupyter**.

When your JupyterLab Notebook is running and open, type `conda list` in a cell and run the cell to confirm that the environment is your custom conda environment (you should see this on the first line). This command will also list all
of your available packages.

## Xfce Desktop (Beta)

This Open OnDemand application is a containerized desktop running on the HPC cluster. It has access to these tools/programs:

- Slurm (for running Slurm commands via the terminal in the desktop and interacting on compute nodes)
- Module command (for loading and running HPC-ready modules)
- File explorer (able to traverse and view files that you have access to on the HPC)
- Firefox web browser
- VLC media player
- Office Libre suite of applications (word processing, spreadsheets, presentation applications)

:::{note}
The desktop application is a Singularity container: a Singularity container cannot run inside. It will fail if a user tries to run a module or program that runs a container inside this application.
:::

[Open On Demand]: https://www.ood.discovery.neu.edu/
[Using X11]: https://rc-docs.northeastern.edu/en/latest/first_steps/connect_mac.html#using-x11
