(cps-ood)=

# CPS class-specific instructions

:::{Caution}
**Note - the following instructions will only work for CPS classes.**
:::

These instructions describe the process of opening a CPS JupyterLab environment on the Open OnDemand (OOD) Discovery web portal and accessing class work directories.

:::{note}
Due to problems with launching OOD on **Safari**, we recommend using **Google Chrome**, **Mozilla Firefox** or **Microsoft Edge** browsers instead for best experience.
:::

## Open the CPS JupyterLab environment

:::{important}
The class instructor needs to fill in the: [Discovery Classroom Use Request](https://bit.ly/NURC-Classroom) You will only be able to find your class resources if a request was already made.
:::

In a web browser, go to <http://ood.discovery.neu.edu>. Login with your NU credentials.

Under the **Courses** menu, select your Class Name (For example: **ALY3070 JupyterLab**):

```{image} /images/cps-ood-menu.png
:alt: A menu dropdown list of classes, with a CPS ALY3070 class highlighted.
:width: 400
```

Select the default options and click **Launch**. Wait until the session is successfully created and ready to be launched (turns green).

```{image} /images/cps-ood-jupyterform.png
:alt: A form of the cps jupyterlab options.
:width: 400
```

For more control of the session, modify **Time** for the session time (in hours), **Memory** to get more memory in GB, and the **Working Directory** where JupyterLab will launch.

:::{note}
If **Working Directory** is left blank, the session will launch in the main class folder (in this example `/work/cps/ALY3070`). Alternatively, start the session directly from your personal working directory by entering: `/work/cps/ALY3070/students/[username]`, where `[username]` is your username on Discovery. The instructions below assume the field is left blank.
:::

Click **Connect to Jupyter** to open JupyterLab:

```{image} /images/cps-ood-jupyterlab-start-session.png
:alt: session created view.
:width: 400
```

This will open a JupyterLab interface in another tab.

Select **Cancel** when prompted with the **Build Recommended** option:

```{image} /images/cps-ood-build-window.png
:alt: build window view.
:width: 400
```

The package jupyterlab-dash does not require a build, and will not work when build is enabled.

## Access CPS class directories

After you are connected to a CPS JupyterLab session on OOD, you can access any shared class directories and your private class directory.

You can navigate between the class folders using the left menu. Your instructor may share files in this directory:

```{image} /images/cps-ood-jupyterlab-folders-view.png
:alt: show files.
:width: 400
```

For instance, file **Example.ipynb** can be viewed using Python Jupyter Notebook (but not edited or removed).

Navigate to the **students** directory, where you will see another directory under your username:

```{image} /images/cps-ood-jupyterlab-students-folder.png
:alt: show students folder.
:width: 400
```

Enter your personal class directory (here, username `mariana.levi` is shown):

```{image} /images/cps-ood-jupyterlab-username-folder.png
:alt: show inside username folder.
:width: 400
```

Now you can create and edit Jupyter Notebook files.

Open a new Python Notebook session from the Launcher menu by clicking the **Python 3 (ipykernel)**:

```{image} /images/cps-ood-jupyterlab-ipykernel-launcher.png
:alt: show inside ipykernel.
:width: 400
```

A new file will be created inside your directory called **Untitled.ipynb**. You can rename it by right-clicking on it and using the Rename option:

```{image} /images/cps-ood-jupyterlab-ipykernel.png
:alt: show inside ipykernel.
:width: 400
```

This Python notebook has ready-to-use Python packages needed for your class.

:::{note}
**Permission Denied errors:**
Do not attempt to create, edit or write files that are outside of your personal student directory. Most "Permission Denied" errors are due to directories or files having read-only access permissions.
:::

## Submit CPS class assignments

:::{important}
Due to the write-only access permissions on the **assignments** directory, it is required to use the command line interface (Linux Terminal) to submit assignments. **Using other methods, such as the JupyterLab interface or OOD File Explorer, currently does not work**.
:::

To submit your assignment (for example, named: **Assignment1.ipynb**) to the **assignments** directory, open the JuypterLab New Launcher by clicking the **File** top menu option, and then selecting **New Launcher**:

```{image} /images/cps-ood-jupyterlab-new-launcher.png
:alt: open new launcher.
:width: 400
```

Click on the **Terminal** option under **Other** to open a Linux terminal:

```{image} /images/cps-ood-jupyterlab-open-terminal.png
:alt: open terminal.
:width: 400
```

Navigate to your personal directory by typing the following command (change the class name from `ALY3070` to your class name accordingly):

```
cd /work/cps/ALY3070/students/$USER
```

Where `$USER` is a saved shell variable for your username. You can optionally also replace it with your username.

Check that your assignment file is visible in the command line by typing `ls`. Then, Copy the assignment file to the **assignments** directory with this command (replace **Assignment1.ipynb** with your file name):

```
cp Assignment1.ipynb ../../assignments
```

To remove an existing assignment, type (replace **Assignment1.ipynb** with your file name):

```
rm ../../assignments/Assignment1.ipynb
```

Close the Terminal tab when done.

```{image} /images/cps-ood-commandline.png
:alt: commandline commands.
:width: 400
```
