(package-manager)=
# Package Managers

## Conda

[Conda] is an open source environment and package manager. [Miniconda] is a free installer for Conda, Python, and comes with a few other packages. [Anaconda] is also a package manager that has a much larger number of packages pre-installed.

A question that frequently comes up is "[Should I use Anaconda or Miniconda]?"

:::{note}
It is not recommended to build your Miniconda and Conda virtual environments inside your /home directory due to its limited space quota (see [Storage Accessible on Discovery]). Use the /work file system instead. If your group needs access to /work, the group PI can request it using: [New Storage Space request].
:::

(creating-python)=

### Creating an Environment

Using a locally installed Conda virtual environment is highly recommended so that you can install the specific packages that you need. You can also have more than one environment with different packages for different research projects or for testing purposes. This procedure uses the Anaconda module already available on Discovery.

If you are on a login node, move to a compute node by typing:

:::{code-block} bash
---
caption: |
    Requesting 1 node with 1 cpu core and load anaconda.
---

srun --partition=short --nodes=1 --cpus-per-task=1 --pty /bin/bash
module load anaconda3/2022.05
:::

To create a new Conda environment where `<environment-name>` is the path and name. You can see a list of your existing environments with `conda env list`.

:::{code} bash
conda create --prefix=/<path>/<environment-name> python=3.11 anaconda
:::

Follow the prompts to complete the Conda install, then activate the environment.

:::{code} bash
source activate /<path>/<environment-name>
:::

Your command line prompt will then include the path and name of environment.

:::{code} bash
(/<path>/<environment-name>) [username@c2001 dirname]$
:::

::::{tip}
``conda config --set env_prompt '({name}) '`` modifies your `.condarc` to only show the environments name as such:
:::{code} bash
(<environment-name>) [username@c2000 dirname]$
:::
::::

With your Conda environment activated you can install a specific package with

:::{code} bash
conda install [packagename]
:::

To deactivate the current active Conda environment
:::{code} bash
conda deactivate
:::

To delete a Conda environment and all of its related packages, run:
:::{code} bash
conda remove -n yourenvironmentname --all
:::

(mini-conda)=

### Using Miniconda

This procedure assumes that you have not installed Miniconda. If you need to update Miniconda, do not follow the installation procedure. Use `conda update`. This procedure uses the Miniconda3 version with Python version 3.8 in step 2, although there are other versions you can install (e.g., 3.9 or 3.11).

#### Installing Miniconda

::::{attention}
Make sure to log on to a compute node.
:::{code} bash
srun --partition=short --nodes=1 --cpus-per-task=1 --pty /bin/bash
:::
::::

Download Miniconda, check the hash key, and install as follows:

:::{code} bash
wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sha256sum Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p <dir>
:::
Where `<dir>` is the full path to your desired installation directory (e.g., `/work/mygroup/mydirectory/miniconda3`).


Activate the base Miniconda environment
:::{code} bash
source <dir>/bin/activate
:::

You can now create a new environment with this command where we're using python version 3.8:

:::{code-block} bash 
conda create --name my-py38env python=3.8
:::

Type `y` if asked to proceed with the installation.

Now you can activate your new environment

:::{code} bash
conda activate my-py38env
:::

To deactivate the environment, type `conda deactivate`. You can type this command again to deactivate the base Miniconda environment.

### Conda Best Practices
:::{seealso}
Best practices for home storage: {ref}`cleaning-conda`.
:::

1. Your `~/.conda` may get very large if you install multiple packages and create many virtual Conda environments. Make sure to clean the Conda cache and clean unused packages with: `conda clean --all`.
1. Clean unused Conda environments by first listing the environments with: `conda env list` , and then removing unused ones: `conda env remove --name <environment-name>`.
1. You can build Conda environments in different locations to save space on your home directory (see [Storage Accessible on Discovery]). You can use the `--prefix` flag when building your environment. For example: `conda create myenv --prefix=/work/<mygroup>/<mydirectory>`.
1. Another recommended step is to update your Conda version (possible only when using Miniconda): `conda update conda -y`

## Spack

Research Computing recommends using [Spack] to conveniently install software packages locally to your path. Please refer to the [Spack documentation] for the latest information about the [packages] that Spack contains. To use Spack, you first need to copy it to your `/home` directory or a `/work` directory, then you need to add it to your local environment.

:::{note}
Spack software installations are part of your research and should preferably be stored in your PI's `/work` directory.
:::

(getting-started-spack)=
### Install Spack

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

### Install a software using Spack 
 
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

### Installing LAMMPS with Spack example

This section details how to install the LAMMPS application with the
KOKKOS and User-reaxc packages using Spack. This example assumes that
you do not have any previous versions of LAMMPS installed. If you have
any previous versions of LAMMPS, you must uninstall them before using
this procedure. To see if you have any previous versions of LAMMPS,
type `spack find lammps`. If you do have a previous version, you will
need to uninstall LAMMPS by typing `spack uninstall --dependents
lammps`. Then, you can follow the instructions below. Note that the
installation can take about two hours to complete. As part of the
procedure, we recommend that you initiate a [tmux session] so that
you can have the installation running as a separate process if you
need to do other work on Discovery. If you decide to use tmux, make
note of the compute node number (compute node numbers start with c or
d with four numbers, such as c0123) to make it easier to check on the
progress of the installation.

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
   srun --partition=gpu --nodes=1 --ntasks=14 --pty --gres=gpu:1 --mem=16GB --time=08:00:00 /bin/bash
   :::

1. Load compatible cuda, gcc, and python modules and activate Spack from the installed location.

   ::::{code-block} bash
    module load cuda/10.2 gcc/8.1.0 python/3.8.1
    export SPACK_ROOT=/work/<PI-Project-Dir>/spack
    . $SPACK_ROOT/share/spack/setup-env.sh
   :::: 

1. (Optional) Initiate a `tmux` session:

   - Start a tmux session: `tmux`.
   - List tmux sessions: `tmux ls` 
   - Detach from tmux session: `Ctrl+b d`
   - Attach to tmux session: `tmux attach-session -t 0` 
   - Exit a tmux session: `Ctrl+d` 

1. Type:

   :::{code-block} shell
   spack install lammps +asphere +body +class2 +colloid +compress +coreshell +cuda \
   cuda_arch=70 +cuda_mps +dipole +granular +kokkos +kspace +manybody +mc +misc +molecule \
   +mpiio +peri +python +qeq +replica +rigid +shock +snap +spin +srd +user-reaxc +user-misc
   :::

1. Type `spack find LAMMPS` to view your installed software package.

1. Type `spack load lammps`.

[anaconda]: https://docs.anaconda.com
[conda]: https://docs.conda.io/en/latest/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Should I use Anaconda or Miniconda]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda
[Spack]: https://spack.io/
[Spack documentation]: https://spack.readthedocs.io/en/latest/index.html
[Storage Accessible on Discovery]: ../datamanagement/discovery_storage.md
[New Storage Space request]: https://bit.ly/NURC-NewStorage
[packages]: https://spack.readthedocs.io/en/latest/package_list.html#package-list
[tmux session]: https://alta3.com/posters/tmux.pdf