(using-module)=

# Using Module

::::{sidebar}
:::{note}
Some modules conflict, resulting in the software behaving differently than expected. Also, if there are multiple software versions and you load more than one version of the software, only the latest version will be used. Use `module list` to view the modules loaded into your path.
:::
::::

The 'modules' tool is widely used for managing application environments on High-Performance Computing (HPC) systems. This page will provide an overview of 'modules', instructions on using them, best practices, use cases, and more.

The module system on the cluster includes many commonly used scientific software packages that you can load into your path when you need them and unload when you no longer need them. In essence, 'modules' handle environment variables like `PATH` and `LD_LIBRARY_PATH` to avoid conflicts between software applications.

Use the `module avail` command to show a list of the most currently available software on the cluster.

:::{tip}
The `which <target>` prints the path of executable `<target>` in your path (e.g., `which python` prints the `python` that will execute if called).
:::

## Module commands

The following are common module commands helpful in interacting with software packages on the cluster.

:::{list-table} List of common module commands, where `<module>` is the name of the target module.
---
header-rows: 1
widths: 23 40
---
* - Module Command
  - Function
* - `module avail`
  - Displays a list of all available modules.
* - `module list`
  - Shows a list of currently loaded modules.
* - `module show <module>`
  - {ref}`View the details of a software package.<module-show-example>`
* - `module load <module>`
  - Loads a specific module.
* - `module unload <module>`
  - Unloads a specific module.
* - `module purge`
  - Unloads all loaded modules.
* - `module swap <module1> <module2>`
  - Replaces `module1` with `module2`.
:::

:::{caution}
`module purge` unloads all modules from your environment. This module sets the HTTP proxy needed to access the internet from nodes. If you accidentally purge this module, it automatically reloads by logging out and then back in. You can also load it manually `module load`.
:::

(module-show-example)=
## Module show example

Before loading a module, type `module show <name of module>` to see if there are any dependencies or commands that you need to execute
before loading the module. Sometimes, a module might depend on loading other modules to work as expected. While modules are convenient for loading software on the cluster, scientific software can come with many packages and dependencies. In addition to the module, you will need to look over other ways to load the cluster's software.

:::{seealso}
{ref}`software-overview` for installing software on the cluster.
:::

Here is an example of using `module show` to show details for the Amber software package.

:::{code} bash
$ module show amber
:::
:::{code-block} text
---
caption: Command-line output.
---
/shared/centos7/modulefiles/amber/18-mpi:

module-whatis     loads the modules environment for Amber 18 MPI parallel executable
                  on CPU nodes.

Please load the following modules:
module load openmpi/3.1.2
module load amber/18-mpi
module load python/2.7.15

setenv            AMBER_HOME /shared/centos7/amber/amber18-cpu
prepend-path      PYTHONPATH /shared/centos7/amber/amber18-cpu/lib/python2.7/site-packages
prepend-path      PATH /shared/centos7/amber/amber18-cpu/bin
prepend-path      LD_LIBRARY_PATH /shared/centos7/amber/amber18-cpu/lib
prepend-path      C_INCLUDE_PATH /shared/centos7/amber/amber18-cpu/include
prepend-path      CPLUS_INCLUDE_PATH /shared/centos7/amber/amber18-cpu/include
:::

## Module load and unload example

The software module `stata/15` was loaded and unloaded in the following code snippet. After each, `module list` displays loaded modules showing whether or not STATA was loaded.

:::::{grid}
::::{grid-item}
:::{code-block} bash
---
emphasize-lines: 3,4
caption: Loading Stata version 15.
---
$ module load stata/15
$ module list
Currently Loaded Modulefiles:
1) explorer/1.0     2) stata/15
:::
::::
::::{grid-item}
:::{code-block} bash
---
emphasize-lines: 3,4
caption: Unloading Stata version 15.
---
$ module unload stata/15
$ module list
Currently Loaded Modulefiles:
1) explorer/1.0
:::
::::
:::::

## Launching applications via X11 Forwarding

If you are attempting to open a GUI-based software application that  uses X11 forwarding to display, such as MATLAB or Maestro, and you get an error such as `Error: unable to open display localhost:19.0`, this is most likely due to an issue with passwordless SSH. See {ref}`connect-to-cluster` for tips and troubleshooting information opening applications that use X11 forwarding.

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
