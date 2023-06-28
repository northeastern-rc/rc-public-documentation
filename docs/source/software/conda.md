(using-conda)=

# Using Conda

[Conda] is an open source environment and package manager. [Miniconda] is a free installer for Conda, Python, and comes with a few other packages. [Anaconda] is also a package manager that has a much larger number of packages pre-installed.

A question that frequently comes up is "[Should I use Anaconda or Miniconda]?"

:::{note}
It is not recommended to build your Miniconda and Conda virtual environments inside your /home directory due to its limited space quota (see [Storage Accessible on Discovery]). Use the /work file system instead. If your group needs access to /work, the group PI can request it using: [New Storage Space request].
:::

(creating-python)=

## Creating an Environment

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

## Conda Best Practices
:::{seealso}
Best practices for home storage: {ref}`cleaning-conda`.
:::

1. Your `~/.conda` may get very large if you install multiple packages and create many virtual Conda environments. Make sure to clean the Conda cache and clean unused packages with: `conda clean --all`.
1. Clean unused Conda environments by first listing the environments with: `conda env list` , and then removing unused ones: `conda env remove --name <environment-name>`.
1. You can build Conda environments in different locations to save space on your home directory (see [Storage Accessible on Discovery]). You can use the `--prefix` flag when building your environment. For example: `conda create myenv --prefix=/work/<mygroup>/<mydirectory>`.
1. Another recommended step is to update your Conda version (possible only when using Miniconda): `conda update conda -y`


[anaconda]: https://docs.anaconda.com
[conda]: https://docs.conda.io/en/latest/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[Should I use Anaconda or Miniconda]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda
[Storage Accessible on Discovery]: ../storage/discovery_storage.md
[New Storage Space request]: https://bit.ly/NURC-NewStorage
