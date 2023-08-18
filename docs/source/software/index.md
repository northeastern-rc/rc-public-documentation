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
:::{grid-item-card} {ref}`interactive-ood`
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

## Requesting Software Installation Assistance
If the software you need is not a module on the cluster, cannot be installed via Spack, and is not available through another way of self-installation (e.g., `make`), please submit a [ServiceNow software request ticket].

:::{note}
Some packages might not be able to be installed on the cluster due to hardware incompatibility issues.
:::


## Installing Your Own Software

::::{grid} 2
:::{grid-item-card} {ref}`make`
For more information about working with module.
:::
:::{grid-item-card} {ref}`cmake`
For more information about OOD.
:::
::::

(installing-your-own-module)=
### Installing Your Own Module
In addition to the pre-installed software on our HPC cluster, users may need to install their software. This section outlines the general steps for doing so.

1. Check If the Software Is Already Installed

Before installing new software, check if it's already installed by using the `module avail` command:

:::{code} bash
module avail
:::

This command lists all the available modules (i.e., software) on the system.

2. Choose the Appropriate Location for Installation

Users should install their software in their home directory or a designated project directory to avoid permission issues. For example:

:::{code} bash
cd /home/<username>/software
:::

Replace `<username>` with your username.

3. Download the Software

Download the software package using `wget` or `curl`, for example:

:::{code} bash
wget http://example.com/software.tar.gz
:::

Ensure to replace `http://example.com/software.tar.gz` with the actual URL of the software package.

4. Extract the Software

Most software packages are distributed as compressed files that must be extracted.

:::{code} bash
tar -xvzf software.tar.gz
:::

Replace `software.tar.gz` with the actual filename of the software package.

5. Install the Software

Installation steps can vary widely between different programs. Many use the `configure`, `make`, `make install` steps, like this:

:::{code} bash
cd software_directory   # Replace with actual directory
./configure --prefix=/home/<username>/software
make
make install
:::

Replace `<username>` with your username and `software_directory` with the actual directory of the software.

:::{note}
Always read the software's installation instructions, as steps may vary.
:::

6. Test the Software

After installation, it's important to test the software to ensure it works correctly. Most software packages include a set of test cases for this purpose. Refer to the software's documentation for how to run these tests.

:::{figure} ../_static/image/build-diagram.png

A workflow of software installation (replace with our own).
:::

7. Make the Software Available via Modules

For ease of use, consider creating a module file for the software. Here's an example of a basic module file for software installed in `/home/<username>/software`:

:::{code} bash
#%Module
set root /home/<username>/software
prepend-path PATH $root/bin
prepend-path LD_LIBRARY_PATH $root/lib
:::

Replace `<username>` with your username.

::{table} Common Software Installation Commands**

| Command      | Description                           |
|--------------|---------------------------------------|
| module avail | List all available modules            |
| cd           | Change the current directory          |
| wget or curl | Download files                        |
| tar          | Extract files from a tarball          |
| ./configure  | Configure the software for the system |
| make         | Compile the software                  |
| make install | Install the software                  |
:::

Following these steps, users should be able to install most software packages on their own. However, always refer to the specific software's documentation, as steps can vary. If you run into issues or need help, please contact support.


[Matlab]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/MATLAB
[Multiprocessing]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/Multiprocessing
[project]: https://github.com/northeastern-rc/discovery-example-scripts
[Schrodinger]: https://github.com/northeastern-rc/discovery-example-scripts/tree/main/Schrodinger
[scripts]: https://github.com/northeastern-rc/discovery-example-scripts
[servicenow software request ticket]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=777c510bdbebd340a37cd206ca9619b0
