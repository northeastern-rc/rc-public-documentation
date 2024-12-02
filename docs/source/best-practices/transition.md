(transition)=
# Quick Start to Explorer

This page highlights the major changes between Discovery and Explorer and provides a few recommendations for a smooth transition.

### New Login

You will want to update your commands to [connect to the cluster](../connectingtocluster/index.md).

The [Open OnDemand](https://ood.explorer.northeastern.edu) website has also been updated and provides graphical interface to many applications (Jupyterlab, R, MATLAB etc).

### New Storage Directory

All of your data that was in Discovery will be in Explorer.

On Explorer our performant storage directory is called `/projects`. 

If you had a storage space for performant storage on Discovery you will want to change the paths in your scripts from `/work` to `/projects`. If you would like a new directory in /projects please [request one](https://bit.ly/NURC-NewStorage).

### Courses Directory

If you are teaching in the Spring 2025 term, you will only be able to access your course materials (i.e., `/courses` directory and OOD applications) from Explorer. 

If you get a "Permission Denied" error when trying to `cd` or otherwise access your space in `/courses` please check that you are logged in to Explorer, and please select "Restart Web Server" from the `?` icon.

### New Software

There is a lot of new software on Explorer. Please see what we offer as a [module](../software/systemwide/modules.md) and as a [container image](../containers/index.md). If you don't see software that you would like to use on the Explorer cluster, please fill out a [software request form](https://bit.ly/NURC-StorageExtension).

#### Modules

All of the [modules](../software/systemwide/modules.md) on Explorer are new. Some of the versions may have changed from the version you were using on Discovery. Thus, module load commands will need to be updated.

Modules should be loaded in sbatch scripts.

For interactive sessions using `srun`, you can create an environment file (a text file with your module load commands) to source environmental parameters for interactive sessions. For example, if we saved several module load commands in a file called "env_file.sh". We could execute this file in an interactive session with the command "bash env_file.sh".

:::{important}
Any "module load" commands in your .bashrc that load Discovery modules may result in a "MODULE NOT FOUND" error in Explorer. Modules loaded in your .bashrc can also lead to conflicts in your environment.

We recommend removing all module load commands from your .bashrc
:::

#### Container Images

[Apptainer](../containers/apptainer.md) is the container run-time engine on Explorer and is installed system-wide (i.e., there is no module for apptainer).

We have many newly added container images at `/shared/container_repository/explorer/`

If you had an image that was pulled to Discovery using `Singularity` it should still work as expected on Explorer, though there may be some exceptions. One of the advantages of container images, is their portability.

### Software Compilied on Discovery

We recommend recompiling software on Explorer that was compilied on the Discovery cluster. If you need assistance please reach out to the Research Computing Team by emailing rchelp@northeastern.edu.

### Conda Environments

Conda environments that were built in Discovery may work in Explorer. A case where they may not work is if you had to load modules on Discovery to build and run your conda environment, and those same modules are not on the Explorer cluster (or their version has been updated). We recommend trying your conda environments on Explorer. If you run into error, try rebuilding the environment, or contact Research Computing by emailing rchelp@northeastern.edu

Please see our documentation on [conda environements](../software/packagemanagers/conda.md#conda) for more information.
