(using-spack)=

# Using Spack

Research Computing recommends using [Spack] to conveniently install software packages locally to your path. Please refer to the [Spack documentation] for the latest information about the [packages] that Spack contains. To use Spack, you first need to copy it to your `/home` directory or a `/work` directory, then you need to add it to your local environment.

:::{note}
Spack software installations are part of your research and should preferably be stored in your PI's `/work` directory.
:::

(getting-started-spack)=
## Getting started with Spack

These instructions will demonstrate how to install Spack in your local `/home` directory (step 2) and then how to add Spack to your local environment while on a compute node, so you have access to the Spack commands (steps 4-5).

1. Connect to Discovery via ssh ({ref}`connect-mac` or {ref}`connect-windows`).
1. From the terminal, type `git clone -c feature.manyFiles=true https://github.com/spack/spack.git` to copy Spack to your `/home`.
1. Type `srun -p short --pty -N 1 -n 28 /bin/bash` to allocate an interactive job on a compute node. Spack will attempt to run `make` in parallel when Spack builds the software you choose to install, so this `srun` request is for 28 cores on one node (`-N 1 -n 28`). To use Spack, it needs to be added to your local environment on the compute node, which is why this is completed after step 3.
1. To use a newer version of python for compatibility with Spack, type: `module load python/3.8.1`.
1. To add Spack in your local environment so you can use the Spack commands, type `export SPACK_ROOT=/home/<yourusername>/spack`.
1. Next, type `. $SPACK_ROOT/share/spack/setup-env.sh`.
1. After you have the Spack commands in your environment, type `spack help` to ensure Spack is loaded in your environment and to see the commands you can use with Spack. You can also type `spack list` to see all the software that you can install with Spack, but note this command can take a few moments to populate the list.
1. To check your spack version, type `spack --version` .
1. To see information about a specific software package, including options and dependencies, type `spack info <software name>`. Make sure to note the options and/or dependencies that you want to add or not add before installing the software.
1. To install a software package plus any dependencies or options, type `spack install <software name> +<any dependencies or options>`; you can specify `-<any dependencies or options>`. You can also list `+` or `-` different options and dependencies within the same line. Do not put a space between each option/dependency that you list.
1. To view your installed software packages, type `spack find`. If you want to view information about a specific installed package, type `spack find <software package name>` or `spack info <software package name>`.
1. Install a specific version of the software using the command: `spack install <softwarename@version>`.

When you have installed a software package, you can add it to the module system by executing this command:
`. $SPACK_ROOT/share/spack/setup-env.sh`

:::{note}
Spack can be installed in a `/work`, which enables members of the `/work` to use the programs that are installed with Spack in that directory.
:::

## Installing LAMMPS with Spack example

This section details how to install the LAMMPS application with the KOKKOS and User-reaxc packages using Spack. This example assumes that you do not have any previous versions of LAMMPS installed. If you have any previous versions of LAMMPS, you must uninstall them before using this procedure. To see if you have any previous versions of LAMMPS, type `spack find lammps`. If you do have a previous version, you will need to uninstall LAMMPS by typing `spack uninstall --dependents lammps`. Then, you can try the example procedure below. Note that the installation can take about two hours to complete. As part of the procedure, we recommend that you initiate a [screen session] so that you can have the installation running as a separate process if you need to do other work on Discovery. If you decide to use screen, make note of the compute node number (compute node numbers start with c or d with four numbers, such as c0123) to make it easier to check on the progress of the installation.

If LAMMPS has a dependency on a specific `gcc` compiler, then do the following before starting the installation procedure. This will update the `compilers.yaml` file located in `$HOME/.spack/linux`.

1. `rm -r $HOME/.spack`
1. `module load gcc/<desired-version>`
1. `spack info lammps`

Check if `compilers.yaml` has been created in `$HOME/.spack/linux` with your desired `gcc` version as the latest (or the only) entry in that file. 

1. Install Spack by following steps 1 through 5 in the {ref}`getting-started-spack` procedure above.

1. Type `exit` to exit from the compute node you requested in step 2 above.

1. Type the following to request a GPU node for 8 hours:

   :::{code-block} shell
   srun --partition=gpu --nodes=1 --ntasks=14 --pty --export=All --gres=gpu:1 --mem=0 --time=08:00:00 /bin/bash
   :::

1. Load a compatible cuda module: `module load cuda/10.2`

1. (Optional) Initiate a `screen` session:

   1. Type `screen -S lammps-install` to create a screen session.
   1. Type `screen -ls` to check to see if the session was created (you'll see it listed if it was successfully created).
   1. Type `screen -rd lammps-install` to enter that screen session.
   1. Type `echo $STY` to check that you are in the screen session.
   1. Type `CTRL+A+D` to exit the screen.

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
