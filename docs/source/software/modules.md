(using-module)=

# Using Module
The 'modules' tool is widely used for managing application environments on High-Performance Computing (HPC) systems. This page will provide an overview of 'modules', instructions on using them, best practices, use cases, and more.

The module system on the cluster includes many commonly used scientific software packages that you can load in your path when you need it and unload it when you no longer need it. In essence, 'modules' handles environment variables like `PATH` and `LD_LIBRARY_PATH` to avoid conflicts between different software applications.

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
* - `module avail`
  - Displays a list of all available modules.
* - `module list`
  - Shows a list of currently loaded modules.
* - `module show <module>`
  - View the details of a software package (see the section "Module Show" below for more information)
* - `module load <module>`
  - Loads a specific module.
* - `module unload <module>`
  - Unloads a specific module.
* - `module purge`
  - Removes all the loaded software packages from your environment.
* - `module swap <module1> <module2>`
  - Replaces `module1` with `module2`.
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

## Advanced Module Usage

Explain how to use modules in job scripts or interactive sessions, using module save and module restore to manage module collections and other advanced topics.

## Creating Module Files

:::{seealso}
{ref}`installing-your-own-module`.
:::

## Best Practices Using Modules

- Only load the modules you need: Unnecessary modules can cause conflicts.
- Know module hierarchies: Some modules might only become available after loading another module.
- Always load a specific module version: This avoids problems if the default version changes.

## Common Issues and Troubleshooting Modules

Cover common issues users might face while using 'modules', like conflicts, missing modules, or unexpected behavior, and provide troubleshooting tips.

## Use-Cases for Modules

Provide several examples of how to use 'modules' for various use cases. This could include:

- Loading modules for a specific software stack for a project.
- Swapping compiler modules to test code compatibility.
- Using module collections to switch between different project environments easily.
