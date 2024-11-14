(transition)=
# Moving from Discovery to Explorer

This page highlights the major changes between Discovery and Explorer and provides a few recommendations for a smooth transition.

### New Login

You will want to update your commands to [connect to the cluster](../../connectingtocluster/index.html).

The [Open OnDemand](ood.explorer.northeastern.edu) website has also been updated and provides graphical interface to many applications (Jupyterlab, R, MATLAB etc).

### New Storage Directory

On Explorer our performant storage directory is called `/projects`. 

If you had a storage space for performant storage on Discovery you will want to change the paths in your scripts from `/work` to `/projects`.

### New Modules

All of the [modules](../../software/systemwide/modules.html) on Explorer are new. Some of the versions may have changed from the version you were using on Discovery. Thus, module load commands will need to be updated.

Modules should be loaded in sbatch scripts, or you can create an environment file (a text file with your module load commands) to source environemental parameters for interactive sessions. For example, if we saved several module load commands in a file called "env_file.sh". We could execute this file in an interactive session with the command "bash env_file.sh".

:::{important}
Any "module load" commands in your .bashrc that load Discovery modules may result in a "MODULE NOT FOUND" error in Explorer. Modules loaded in your .bashrc can also lead to conflicts in your environment.

We recommend removing all module load commands from your .bashrc
:::

### Software Compilied on Discovery

We recommend recompiling software on Explorer that was compilied on the Discovery cluster.

### Conda Environments

Conda environments that were built in Discovery may work in Explorer. A case where they may not work is if you had to load modules on Discovery to build and run your conda environment, and those same modules are not on the Explorer cluster (or their version has been updated). We recommend trying your conda environments on Explorer. If you run into error, try rebuilding the environment, or contact Research Computing by emailing [rchelp](rchelp@northeastern.edu)

Please see our documentation on [conda environements](../../software/packagemanagers/conda.html#conda) for more information.
