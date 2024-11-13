(transition)=
# Moving from Discovery to the Explorer Cluster

This page highlights the major changes between Discovery and Explorer and provides a few recommendations for a smooth transition.

## New Logins

You will want to update your commands to ssh in, as well as login in via the Open OnDemand website.

## New Storage Directory Name

On Explorer our performant storage directory is called `/projects`. If you had a storage space for performant storage on Discovery you will want to change the paths in your scripts from `/work` to `/projects`.

## New Modules

All of the modules on Explorer are new. Some of the versions may have changed from the version you were using on Discovery. Thus, module load commands will need to be updated.

:::{important}
Any "module load" commands in your .bashrc that load Discovery modules may result in a "MODULE NOT FOUND" error in Explorer. Modules loaded in your .bashrc can also lead to conflicts in your environment.

We recommend removing all module load commands from your .bashrc

Modules should be loaded in sbatch scripts, or you can create an environment file (a text file with your module load commands) to source environemntal parameters for interactive sessions. In an interactive session this can be executed via the command "bash file_name.sh"
:::

## New Partitions
