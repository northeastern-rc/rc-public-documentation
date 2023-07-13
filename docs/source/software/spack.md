(using-spack)=

# Using Spack

Research Computing recommends using [Spack] to conveniently install software packages locally to your path. Please refer to the [Spack documentation] for the latest information about the [packages] that Spack contains. To use Spack, you first need to copy it to your `/home` directory or a `/work` directory, then you need to add it to your local environment.

:::{note}
Spack software installations are part of your research and should preferably be stored in your PI's `/work` directory.
:::

(getting-started-spack)=
## Install Spack

These instructions will demonstrate how to install Spack in your `/home` (*non-shared*) or `/work` (*shared*) directory and then how to add Spack to your local environment while on a compute node, so you have access to the Spack commands (steps 4-5).

::::::{tab-set}
:::::{tab-item} Non-shared

Copy Spack's Git repository to '$HOME'

::::{code-block} bash
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
::::

:::::
:::::{tab-item}	Shared

Copy Spack's Git repository to '/work' and modify directory permissions to give write access to the members of your PI's `/work`.

::::{code-block} bash
cd /work/<PI-Project-Dir>
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
chmod -R 775 spack/
::::

:::::
::::::

## Install a software using Spack 
 
1. Request a compute node interactively: `srun -p short --pty -N 1 -n 28 /bin/bash`. While building the software Spack will attempt to run `make` in parallel. Hence, you need to request a compute node with multiple cores. This `srun` request is for 28 cores on one node (`-N 1 -n 28`). 
1. Any module that is required for your software installation needs to be in your `$PATH` prior to adding Spack to your local environment. For example, to use a newer version of python for compatibility with Spack, type: `module load python/3.8.1`. 
1. Add Spack to your local environment so you can use the Spack commands. If Spack has been installed on `$HOME`: 
::::{code-block} bash
For Spack on $HOME
export SPACK_ROOT=/home/<yourusername>/spack
. $SPACK_ROOT/share/spack/setup-env.sh

For Spack on /work/<PI-Project-Dir>
export SPACK_ROOT=/work/<PI-Project-Dir>/spack
. $SPACK_ROOT/share/spack/setup-env.sh
::::

1. After you have the Spack commands in your environment, type `spack help` to ensure Spack is loaded in your environment and to see the commands you can use with Spack. You can also type `spack list` to see all the software that you can install with Spack, but note this command can take a few moments to populate the list.
1. To check your spack version: `spack --version` .
1. To see information about a specific software package, including options and dependencies: `spack info <software name>`. Make sure to note the options and/or dependencies that you want to add or not add before installing the software.
1. To install a software package plus any dependencies or options:
`spack install <software name> +<any dependencies or options>`;
you can specify `-<any dependencies or options>`. You can also list
`+` or `-` different options and dependencies within the same line. Do
not put a space between each option/dependency that you list.
1. To view information about your installed software packages: `spack find <software package name>` or `spack info <software package name>` . 
1. To Install a specific version of the software: `spack install <softwarename@version>`.

When you have installed a software package, you can add it to the module system by executing this command:
`. $SPACK_ROOT/share/spack/setup-env.sh`

## Installing LAMMPS with Spack example

This section details how to install the LAMMPS application with the KOKKOS and User-reaxc packages using Spack. This example assumes that you do not have any previous versions of LAMMPS installed. If you have any previous versions of LAMMPS, you must uninstall them before using this procedure. To see if you have any previous versions of LAMMPS, type `spack find lammps`. If you do have a previous version, you will need to uninstall LAMMPS by typing `spack uninstall --dependents lammps`. Then, you can try the example procedure below. Note that the installation can take about two hours to complete. As part of the procedure, we recommend that you initiate a [screen session] so that you can have the installation running as a separate process if you need to do other work on Discovery. If you decide to use screen, make note of the compute node number (compute node numbers start with c or d with four numbers, such as c0123) to make it easier to check on the progress of the installation.

If LAMMPS has a dependency on a specific `gcc` compiler, then do the following before starting the installation procedure. This will update the `compilers.yaml` file located in `$HOME/.spack/linux`.

1. `cd $HOME/.spack/linux/`
1. Open `compilers.yaml` and copy-paste a `compiler` entry at the end of the file. 
1. Edit 'spec' and 'path' to indicate the version of the gcc compiler that is required for installation. 

   ::::{code-block} bash
   For example:
        spec: gcc@=8.1.0
    	paths:
    	  cc: /shared/centos7/gcc/8.1.0/bin/gcc
     	  cxx: /shared/centos7/gcc/8.1.0/bin/g++
    	  f77: /shared/centos7/gcc/8.1.0/bin/gfortran
      	  fc: /shared/centos7/gcc/8.1.0/bin/gfortran
   ::::

1. The `compilers.yaml` file should now have the desired `gcc` version as its latest `compiler` entry.
1. Assuming that Spack has already been installed at a desired location. For installing gpu-supported LAMMPS, request a GPU node for 8 hours:

   :::{code-block} shell
   srun --partition=gpu --nodes=1 --ntasks=14 --pty --export=All --gres=gpu:1 --mem=0 --time=08:00:00 /bin/bash
   :::

1. Load a compatible cuda module: `module load cuda/10.2`

1. (Optional) Initiate a `tmux` session:

   1. Start a tmux session: `tmux`.
   1. List tmux sessions: `tmux ls` 
   1. Detach from tmux session: `Ctrl+b d`
   1. Attach to tmux session: `tmux attach-session -t 0` 
   1. Exit a tmux session: `Ctrl+d` 

1. Type:

   :::{code-block} shell
   spack install lammps +asphere +body +class2 +colloid +compress +coreshell +cuda \
   cuda_arch=70 +cuda_mps +dipole +granular +kokkos +kspace +manybody +mc +misc +molecule \
   +mpiio +peri +python +qeq +replica +rigid +shock +snap +spin +srd +user-reaxc +user-misc
   :::

1. Type `spack find LAMMPS` to view your installed software package.

1. Type `spack load lammps`.

[screen session]: https://www.gnu.org/software/screen/
[Spack]: https://spack.io/
[Spack documentation]: https://spack.readthedocs.io/en/latest/index.html
[packages]: https://spack.readthedocs.io/en/latest/package_list.html#package-list
