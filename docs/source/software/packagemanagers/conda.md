::::{sidebar}
:::{seealso}
[Should I use Anaconda or Miniconda]?
:::
::::
(conda)=
# Conda
[Conda] is an open-source environment and package manager. [Miniconda] is a free installer for Conda and Python and comes with a few other packages. [Anaconda] is also a package manager that has a much larger number of packages pre-installed.

## Managing Conda Environments

(creating-python)=
### Creating Environments

:::::{note}
We recommend avoiding building Conda environments in your `/home`, for its space quota. Instead, Use `/project`, which can be requested by PIs for groups in need of space `/project`.
:::{seealso}
{ref}`Learn about storage options <data-storage>` and [Submit New Storage Space request].
:::

:::::


Installing local virtual environment using Conda is recommended on the cluster. You can have multiple environments with different packages for each, which allows project's environments to be independent of others. You only have to load the `anaconda3` module.

From the login node, log-in to a compute node.

:::{code-block} bash
---
caption: |
    Request one node on the `short` partition with 1 CPU core. Then, load the `anaconda3/2022.05` module.
linenos: true
---

srun --partition=short --nodes=1 --cpus-per-task=1 --pty /bin/bash
module load anaconda3/2024.06
:::

To create a new Conda environment where `<environment-name>` is the path and name. You can see a list of your existing environments with `conda env list`.

:::{code} bash
conda create --prefix=/<path>/<environment-name> python=3.11 anaconda
:::

::::{attention}
Do NOT automatically initialize conda on startup, as it sometimes interferes with other environments on the HPC. If you have previously set conda to initialize on startup, remove the conda initialization script from the `.bashrc` file. See {ref}`conda-and-bashrc` for more details.
::::

Follow the prompts to complete the Conda install, then activate the environment.

:::{code} bash
source activate /<path>/<environment-name>
:::

Your command line prompt will then include the path and name of environment.

:::{code} bash
(/<path>/<environment-name>) [<username>@c2001 dirname]$
:::

::::{tip}
The `conda config --set env_prompt '({name}) '` command modifies your `.condarc` to show only the environment, which displays as follows:
:::{code} bash
(<environment-name>) [<username>@c2000 dirname]$
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

### Listing Environments
You can view the environments you've created in your home directory by using the following command
:::{code} bash
conda env list
:::

:::{code} bash
# conda environments:
#
MlGenomics               $HOME/.conda/envs/MlGenomics
base                     $HOME/miniconda3
:::

To list the software packages within a specific environment, use
:::{code} bash
conda list --name env_name
:::

If you've created an environment in a different location, you can still list its packages using:
:::{code} bash
conda list --prefix /path/to/env
:::

### Exporting Environment
For ensuring reproducibility, it's recommended to export a list of all packages and versions in an environment to an environment file. This file can then be used to recreate the exact environment on another system or by another user. It also serves as a record of the software environment used for your analysis.

### Removing Environments
When you need to remove an environment located in your home directory, execute:
:::{code} bash
conda env remove --name env_name
:::

For environments located elsewhere, you can remove them using:
:::{code} bash
rm -rf /path/to/env
:::

### Clean Conda Environment
To remove packages that are no longer used by any environment and any downloaded tarballs stored in the conda package cache, run:
:::{code} bash
conda clean --all
:::

By following these guidelines, you can efficiently manage your Conda environments and packages, ensuring reproducibility and a clean system.

(mini-conda)=

## Using Miniconda

This procedure assumes that you have not installed Miniconda. If you need to update Miniconda, do not follow the installation procedure. Use `conda update`. This procedure uses the Miniconda3 version with Python version 3.8 in step 2, although there are other versions you can install (e.g., 3.9 or 3.11).

### Installing Miniconda

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
Where `<dir>` is the full path to your desired installation directory (e.g., `/work/mygroup/miniconda3`).


Activate the base Miniconda environment
:::{code} bash
source <dir>/bin/activate
:::

You can now create a new environment with this command where we are using python version 3.8:

:::{code-block} bash
conda create --name my-py38env python=3.8
:::

Type `y` if asked to proceed with the installation.

Now you can activate your new environment

:::{code} bash
conda activate my-py38env
:::

To deactivate the environment, type `conda deactivate`. You can type this command again to deactivate the base Miniconda environment.

(conda-and-bashrc)=
## Conda and `.bashrc`

In addition to editing your `.bashrc` file as outlined in the example above, programs you install can also modify your `.bashrc` file. For example, if you follow the procedure outlined in {ref}`mini-conda`, there may be a section added to your `.bashrc` file (if you didn't use the `-b` batch option) that automatically loads your conda environment every time you sign in to Explorer. See the figure below for an example of this:

:::{code} bash
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/$USER/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/$USER/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/$USER/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/$USER/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
:::

You should not modify this section in the `.bashrc` file directly. If it was changed, remove this section manually using a file editor.

:::{caution}
We recommend removing the conda initialization section from your `.bashrc` as it may interfere with the correct startup environment when using Open OnDemand apps. You should always load your Conda environment after your job has already started.
:::

If you need help with your `.bashrc` file or would like it restored to its default, reach out to the RC team at <mailto:rchelp@northeastern.edu>, and we can provide you with
a new default `.bashrc` file and help troubleshoot issues with the file.

## Conda Best Practices
:::{seealso}
Best practices for home storage: {ref}`cleaning-conda`.
:::

1. Your `~/.conda` may get very large if you install multiple packages and create many virtual Conda environments. Make sure to clean the Conda cache and clean unused packages with: `conda clean --all`.
1. Clean unused Conda environments by first listing the environments with: `conda env list` , and then removing unused ones: `conda env remove --name <environment-name>`.
1. You can build Conda environments in different locations to save space on your home directory (see {ref}`data-storage`). You can use the `--prefix` flag when building your environment. For example: `conda create myenv --prefix=/work/<mygroup>/<mydirectory>`.
1. Another recommended step is to update your Conda version (possible only when using Miniconda): `conda update conda -y`


[anaconda]: https://docs.anaconda.com
[conda]: https://docs.conda.io/en/latest/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Should I use Anaconda or Miniconda]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda
[Submit New Storage Space request]: https://bit.ly/NURC-NewStorage
