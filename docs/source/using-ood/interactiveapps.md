(accessing-ood)=

# OOD Interactive Apps

There are a number of applications that you can access and use through the OOD web portal. When you select an application and click launch, the scheduler (Slurm) allocates a compute node with a predetermined number of cores and amount of memory. The default time for running any of the applications is one hour. It is recommended that you keep the default. If you ask for more than one hour, you will need to wait for Slurm to allocate a resource that can run for your requested time, which could take a long time to be allocated, depending on how busy the cluster is.

If you are attempting to run a job on one of the interactive apps on OOD that launches a graphical user interface (GUI), such as Maestro, you might get an error if your passwordless ssh is not set up correctly. See {ref}`using-x11` for tips and troubleshooting information opening applications that use X11 forwarding.

## Available Apps (June 2023)

On the Interactive Apps tab, you can view the list of available interactive apps through the OOD web interface.

:::{image} ../images/ood_apps_2023_06.png
---
alt: an image the OOD apps (06-2023).
scale: 30%
align: right
---
:::

:::{note}
Some apps are reserved for specific research groups and are not for general access, denoted by Restricted next to application name. If you get an access error when attempting to open an app, and you believe that you should have access to it, please email <rchelp@northeastern.edu> with your username, research group, the app you are trying to access, a screenshot of the error that you are getting, and we will look into the issue.
:::

1. In a web browser, go to [Open On Demand]. If prompted, enter your myNortheastern username and password.
1. Select **Interactive Apps**, then select the application you want to use.
1. For most apps, keep the default options, and then click **Launch**. You might have to wait a
   minute or two for a compute node to be allocated with your requested time and resource.

## Jupyter Notebook

One of the interactive apps on OOD is JupyterLab Notebook. You need to do some initial setup in order to use this app effectively. This section will provide a walkthrough of setting up and using this app. The general workflow is to first create a virtual python environment, ensure that JupyterLab Notebook is installed in your virtual environment, and then reference this environment when you start the JupyterLab Notebook OOD interactive app.

You can find the JupyterLab notebook on OOD by following these steps:
1. Go to [Open On Demand]
1. Click on Interactive Apps
1. Select JupyterLab Notebook from the dropdown list

The OOD form for lauching JupyterLab Notebook will appear.

### Conda virtual environment

You can import python packages in your JupyterLab Notebook session by creating a conda virtual environment and activating that environment when starting a JupyterLab Notebook instance.

1. First set up a virtual python environment. See {ref}`creating-python` for how to set up a virtual python environment on the HPC using the terminal.
1. Type `source activate <yourenvironmentname>` where `<yourenvironmentname>` is the name of your custom environment.
1. Type `conda install jupyterlab -y` to install jupyterlab in your environment.

###  Using OOD to launch Jupyter Notebook
1. Go to [Open On Demand].
1. Click **Interactive Apps**, then select **JupyterLab Notebook**.
1. Enter your **Working Directory** (as examples `/home/<username>` or `/work/<project>`) that you want JupyterLab Notebook to launch in.
1. Select from the **Partition** dropdown menu the partition you want to use for your session. Refer to {ref}`partition-names` for the resource restrictions for the different partitions. If you need a GPU, select the `gpu` partition.
1. Select the compute node features for the job:
   - In the **Time** field, enter the number of hour(s) needed for the job.
   - In the **Memory (in Gb)** field, enter the amount of memory you need for the job.
   - If you selected the `gpu` partition from the dropdown menu, select the GPU you would like to use and the version of CUDA that you would like to use for your session under the respective dropdown menus.
1. Select the Anaconda version that you used to create your virtual python environment in the **System-wide Conda Module** field.
1. Check **Custom Anaconda Environment** box, and enter the name of your custom virtual python environment in the **Name of Custom Conda Environment** field.
1. Click **Launch**. This will put you in the queue for a compute node. Note that this might take a few minutes, depending on the resources you requested.
1. When you have been allocated a compute node, click **Connect to Jupyter**.

When your Jupyter Notebook is running and open, type `conda list` in a cell and run the cell to confirm that the environment is your custom conda environment (you should see this on the first line). This command will also list all
of your available packages.

## Xfce Desktop (Beta)

This Open OnDemand application is a containerized desktop running on the HPC cluster. It has access to these tools/programs:

- Slurm (for running Slurm commands via the terminal in the desktop and interacting on compute nodes)
- Module command (for loading and running HPC ready modules)
- File explorer (able to traverse and view files that you have access to on the HPC)
- Firefox web browser
- VLC media player
- Office Libre suite of applications (work processing, spreadsheets, presentation applications)

:::{note}
The desktop application is itself a Singularity container and has not been set up to run a Singularity container inside of it. If a user is trying to run a module or program that itself runs a container while inside of this application it will fail.
:::

[Open On Demand]: https://www.ood.discovery.neu.edu/
