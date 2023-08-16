(software-overview)=
# Software Overview
```{toctree}
:hidden:
:maxdepth: 3

modules
mpi
r
spack
matlab
conda
makefile
cmake
```
## System-Wide Software
::::{grid} 2

:::{grid-item-card} {ref}`using-module`
For more information about working with module.
:::
:::{grid-item-card} {ref}`accessing-ood`
For more information about OOD.
:::
::::

Discovery offers you many options for working with software. Two of the easiest and most convenient ways are using the `module` command on the command line and using the interactive apps on Open OnDemand (OOD), Discovery's web portal.

::::{sidebar}
:::{seealso}
{ref}`using-module`.
:::
::::

If you need a specific software package, first check to see if it is already available through one of the preinstalled modules on Discovery. The Research Computing team adds new modules regularly, so use the `module avail` command to view the most up-to-date list.

## Getting Started Scientific Software Applications
Research Computing has provides [scripts] to assist you in getting started with different scientific software packages on discovery. Although these scripts may not have all the solutions, they aim to provide users with a starting point to grasp the syntax and procedures used in various applications.

::::{grid} 3
:::{grid-item-card} [MATLAB]
:::
:::{grid-item-card} [Multiprocessing]
:::
:::{grid-item-card} [Schrodinger]
:::
::::

The collection of scripts is continuously growing and the team welcomes any contributions to the [project].

## Package Managers
Package managers allows you to build specific environments.

::::{grid} 2
:::{grid-item-card} {ref}`conda`
Manage software packages with Anaconda or Miniconda.
:::
:::{grid-item-card} {ref}`spack`
Has over 5,000 packages that you can install.
:::
::::


## Installing Your Own Software

::::{grid} 2
:::{grid-item-card} {ref}`make`
For more information about working with module.
:::
:::{grid-item-card} {ref}`cmake`
For more information about OOD.
:::
::::

## Requesting Software Installation Assistance
If the software you need is not a module on the cluster, cannot be installed via Spack, and is not available through another way of self-installation (e.g., `make`), please submit a [ServiceNow software request ticket].

:::{note}
Some packages might not be able to be installed on the cluster due to hardware incompatibility issues.
:::


[Matlab]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/MATLAB
[Multiprocessing]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/Multiprocessing
[project]: https://github.com/northeastern-rc/discovery-example-scripts
[Schrodinger]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/Schrodinger
[scripts]: https://github.com/northeastern-rc/discovery-example-scripts
[servicenow software request ticket]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=777c510bdbebd340a37cd206ca9619b0
