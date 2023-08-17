(using-module)=

# Using Module

The module system on the cluster includes many commonly used scientific software packages
that you can load in your path when you need it and unload it when you no longer need it.

Use the `module avail` command to show a list of the most currently available software on the cluster.

:::{note}
Some modules might conflict with each other, resulting in the software not behaving as expected.
Also, if there are multiple versions of software, and you load more than one version of the software,
only the latest version will be used. Use `module list` to view the modules you currently have loaded in your path.
:::

:::{tip}
Use the `which` command to display which version of a software package you have in your path.
For example, `which python` will display the version of python that you have in your path.
:::

## Module commands

The following are common module commands that are useful for interacting with software packages on the cluster.

:::{list-table} List of common module commands, where `<module>` is the name of the target module.
---
header-rows: 1
---
* - Module Command
  - Function
* - ``module avail``
  - View a list of all the available software packages on the cluster that you can load
* - ``module list``
  - Displays a list of the software packages currently loaded in your path
* - ``module show <module>``
  - View the details of a software package (see the section "Module Show" below for more information)
* - ``module load <module>``
  - Load a software package into your environment
* - ``module unload <module>``
  - Remove a single software package from your environment
* - ``module purge``
  - Removes all the loaded software packages from your environment.
:::

:::{caution}
Using `module purge` will purge all modules from your environment, including the default module `discovery/2019-02-21`.
This module contains the http proxy needed for nodes to have internet access.
If you accidentally purge this module, it will be automatically reloaded the next time you log out and
log back in again. You can also load it manually if you have purged it by using the `module load` command.
:::

## Module show example

Before loading a module, type `module show <name of module>` to see if there are any dependencies or commands that you need to execute
before loading the module. In some cases, a module might depend on having other modules loaded to work as expected. While modules are a convenient way of loading software to use on the cluster, scientific software can come with many packages and dependencies. In addition to module, you should review other ways of loading software on the cluster. See {ref}`software-overview` for more information on different ways you can install software on the cluster. The figure below shows an example of `module show` with the software package called amber.

![Alt text](../images/moduleshow.jpg)

## Module load and unload example

In the figure below, the software module stata/15 was loaded and then unloaded. After loading and unloading, module list was used
to check that the STATA was loaded and unloaded.

![Alt text](../images/moduleload.jpg)

## Using software applications with X11 Forwarding

If you are attempting to open a GUI-based software application that  uses X11 forwarding to display, such as MATLAB or Maestro, and
you get an error such as `Error: unable to open display localhost:19.0`, this is most likely due to an issue with passwordless SSH.
See {ref}`connect-to-cluster` for tips and troubleshooting information opening applications that use X11 forwarding.

## Installing Your Own Module
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
