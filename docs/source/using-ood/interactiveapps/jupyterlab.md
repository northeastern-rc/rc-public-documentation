(jupyterlab)=
# JupyterLab

JupyterLab Notebook is one of the interactive apps on OOD. This section will provide a walk through of setting up and using this app. The general workflow is to create a virtual Python environment, ensure that JupyterLab Notebook uses your virtual environment, and reference this environment when you start the JupyterLab Notebook OOD interactive app.

To find the JupyterLab Notebook on OOD, follow these steps:

1. Go to [Open On Demand].
1. Click on Interactive Apps.
1. Select JupyterLab Notebook from the drop-down list.

The OOD form for launching JupyterLab Notebook will appear.

:::{admonition} Conda virtual environment
You can import Python packages in your JupyterLab Notebook session by creating a conda virtual environment and activating that environment when starting a JupyterLab Notebook instance.

1. First, set up a virtual Python environment. See {ref}`creating-python` for how to set up a virtual Python environment on the HPC using the terminal.
1. Type `source activate <yourenvironmentname>` where `<yourenvironmentname>` is the name of your custom environment.
1. Type `conda install jupyterlab -y` to install JupyterLab in your environment.
:::

##  Using OOD to launch JupyterLab Notebook
1. Go to [Open On Demand].
1. Click **Interactive Apps**, then select **JupyterLab Notebook**.
1. Enter your **Working Directory** (e.g., `/home/<username>` or `/work/<project>`) that you want JupyterLab Notebook to launch in.
1. Select from the **Partition** drop-down menu the partition you want to use for your session. Refer to {ref}`partition-names` for the resource restrictions for the different partitions. If you need a GPU, select the `gpu` partition.
1. Select the compute node features for the job:
   - In the **Time** field, enter the number of hour(s) needed for the job.
   - Enter the memory you need for the job in the **Memory (in Gb)** field.
   - If you selected the `gpu` partition from the drop-down menu, select the GPU you would like to use and the version of CUDA that you would like to use for your session under the respective drop-down menus.

1. Select the Anaconda version you used to create your virtual Python environment in the **System-wide Conda Module** field.
1. Check the **Custom Anaconda Environment** box, and enter the name of your custom virtual Python environment in the **Name of Custom Conda Environment** field.
1. Click **Launch** to join the queue for a compute node. This might take a few minutes, depending on what you asked for.
1. When allocated a compute node, click **Connect to Jupyter**.

When your JupyterLab Notebook is running and open, type `conda list` in a cell and run the cell to confirm that the environment is your custom conda environment (you should see this on the first line). This command will also list all of your available packages.

:::{important}
We advise against using 'pip install' to install packages while in the JupyterLab Notebook. These installations are placed in your /home/username/.local directory, which will add to your /home quota. Additionaly, the presence of different packages in your .local can have a negative impact on the function of applications on the OOD. Please ensure all the packages you need are installed in a conda or virtual python environment.
:::
