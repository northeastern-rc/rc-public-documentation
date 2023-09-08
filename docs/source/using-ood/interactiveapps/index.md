(interactive-ood-apps)=
# Interactive Open OnDemand Applications
```{toctree}
:hidden:
desktopood
fileexplore
jupyterlab
stataood
```

::::{grid} 3

:::{grid-item-card} {ref}`desktop-app`
:::
:::{grid-item-card} {ref}`file-explorer`
:::
:::{grid-item-card} {ref}`jupyterlab`
:::
::::



The OOD web portal provides a range of applications. Upon clicking *launch*, the Slurm scheduler assigns a compute node with a specified number of cores and memory. By default, applications run for one hour. If you require more than an hour, you may have to wait for Slurm to allocate resources for the duration of your request.
## Applications on OOD

:::{image} ../../images/ood_apps_2023_06.png
---
alt: an image of the OOD apps (06-2023).
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
- Gaussian (GaussView)
- KNIME
- TensorBoard
- SAS

These applications can be accessed from the OOD web interface's **Interactive Apps** drop-down menu.

:::{note}
Specific applications in the **Interactive Apps** section, particularly those with graphical user interfaces (GUIs), may require X11 forwarding and the setup of passwordless SSH. For tips and troubleshooting information on X11 forwarding setup and usage, please look at the [Using X11] section of our documentation.
:::

Additionally, we offer a selection of modified standard applications intended to support specific coursework. These applications are under the **Courses** menu on the OOD web interface. Please note that these course-specific applications are only accessible to students enrolled in the respective courses.

:::{note}
Certain apps are reserved for specific research groups and are not publicly accessible, as indicated by the "Restricted" label next to the application name. If you receive an access error when attempting to open a restricted app, and you believe you should have access to it, please email <rchelp@northeastern.edu> with the following information: your username, research group, the app you are trying to access, and a screenshot of the error message. We will investigate and address the issue.
:::

1. Go to [Open On Demand] in a web browser. If prompted, enter your MyNortheastern username and password.
1. Select **Interactive Apps**, then select the application you want to use.
1. Keep the default options for most apps, then click **Launch**. You might have to wait a minute or two for a compute node to be available for your requested time and resource.
