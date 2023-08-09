(software-overview)=

# Software Overview
Discovery offers you many options for working with software. Two of the easiest and most convenient ways are using the `module` command on the command line and using the interactive apps on Open OnDemand (OOD), Discovery's web portal.

::::{sidebar}
:::{seealso}
{ref}`using-module`.
:::
::::

If you need a specific software package, first check to see if it is already available through one of the preinstalled modules on Discovery. The Research Computing team adds new modules regularly, so use the `module avail` command to view the most up-to-date list. You can also try using Spack, a software package manager available on Discovery. Spack has over 5,000 packages that
you can install.

::::{grid} 3

:::{grid-item-card} {ref}`using-module`
For more information about working with module.
:::
:::{grid-item-card} {ref}`accessing-ood`
For more information about OOD.
:::
:::{grid-item-card} {ref}`using-spack`
For more information about Spack.
:::
::::

You can also use Conda, Miniconda, and Anaconda to manage software packages. See {ref}`using-conda` for more information.

## Getting Started Scientific Software Applications
The Research Computing team has created a collection of [scripts] to assist you in getting started with different scientific software packages on discovery. Although these scripts may not have all the solutions, they aim to provide users with a starting point to grasp the syntax and procedures used in various applications.

- [Matlab]
- [Multiprocessing]
- [Schrodinger]

The collection of scripts is continuously growing and the team welcomes any contributions to the [project].

## Requesting Software Installation Assistance
If the software that you need is not a module on Discovery, cannot be installed through Spack, or is not available through another way of
self-installation (such as using `make`), you can submit a [ServiceNow software request ticket].
Be aware that there might be packages that cannot be installed on Discovery due
to incompatibility with the hardware on Discovery.

[Matlab]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/MATLAB
[Multiprocessing]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/Multiprocessing
[project]: https://github.com/northeastern-rc/discovery-example-scripts
[Schrodinger]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/Schrodinger
[scripts]: https://github.com/northeastern-rc/discovery-example-scripts
[servicenow software request ticket]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=777c510bdbebd340a37cd206ca9619b0
