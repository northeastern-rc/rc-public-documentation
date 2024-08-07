(cps-ood)=

# CPS Class Instructions

:::{important}
The following instructions will only work for CPS classes.
:::

These instructions describe the process of opening a CPS JupyterLab environment on the {term}`Open OnDemand (OOD)` on the cluster web portal and accessing class `/courses` folders.

:::{note}
Due to problems with launching OOD on **Safari**, we recommend using **Google Chrome**, **Mozilla Firefox** or **Microsoft Edge** browsers instead for best experience.
:::

## Open JupyterLab For Classes

:::{important}
The class instructor needs to fill in the: [Discovery Classroom Use Request] You will only be able to find your class resources if a request was already made.
:::

1. In a web browser, go to <http://ood.discovery.neu.edu>. Login with your NU credentials.

1. Under the **Courses** menu, select your Class Name (For example: **ALY6080 JupyterLab**).

1. Select the default options and click **Launch**. Wait until the session is successfully created and ready to be launched (turns green).

1. For more control of the session, modify **Time** for the session time (in hours), **Memory** to get more memory in GB, and the **Working Directory** where JupyterLab will launch.

    ::::{note}
    If **Working Directory** is left blank, the session will launch in the main class folder (in this example `/courses/ALY6080.202335/data`). Alternatively, start the session directly from your personal working directory by entering: `/courses/ALY6080.202335/students/[username]`, where `[username]` is your username on Discovery. The instructions below assume the field is left blank.
    :::{code}
    courses/
    └── ALY6080.202335
        ├── data
        ├── staff
        │   ├── doug
        │   ├── evelyn
        │   └── frank
        └── students
            │── alice
            │── bab
            └── cindy
    :::
    The above file tree represents the folder structure for the `ALY6080.202335` course.
    ::::

1. Click **Connect to Jupyter** to open JupyterLab. This will open a JupyterLab interface in another tab.

:::{caution}
Select **Cancel** when prompted with the **Build Recommended** option. The package jupyterlab-dash does not require a build, and will not work when build is enabled.
:::

## Access Class Directories

1. After you are connected to a CPS JupyterLab session on OOD, you can access any shared class directories and your private class directory.

1. You can navigate between the class folders using the left menu. The files in the shared class directory are read ony and the students do not have permissions to edit or remove the files. Your instructor may use the shared class directory to share files related to the classwork

1. Navigate to your personal class directory under: `/courses/[coursename.termcode]/students/<your username>`. Now you can create and edit Jupyter notebook files here.

1. Open a new Python notebook session from the Launcher menu by clicking the **Python 3 (ipykernel)**.

1. A new file will be created inside your directory called **Untitled.ipynb**. You can rename it by right-clicking on it and using the rename option.

1. This Python notebook has ready-to-use Python packages needed for your class.

:::{note}
**Permission Denied errors:**

Do not attempt to create, edit or write files that are outside your personal student directory. Most "Permission Denied" errors are due to directories or files having read-only access permissions.
:::