(using-conda)=

# Using Conda

[Conda]is an open source environment and package manager. [Miniconda] is a free installer for Conda, Python,
and comes with a few other packages. [Anaconda] is also a package manager that has a much larger number of packages pre-installed.

A question that frequently comes up is "[Should I use Anaconda or Miniconda?]"

:::{note}
It is not recommended to build your Miniconda and Conda virtual environments inside your /home directory due to its limited space quota (see [Storage Accessible on Discovery]). Use the /work file system instead. If your group needs access to /work, the group PI can request it using: [New Storage Space request].
:::

(creating-python)=

## Creating a Conda virtual environment with Anaconda

Using a locally installed Conda virtual environment is highly recommended so that you can install the specific packages that you need.
You can also have more than one environment with different packages for different research projects or for testing purposes. This procedure uses the Anaconda module already available on Discovery.

1. If you are on a login node, move to a compute node by typing `srun --partition=short --nodes=1 --cpus-per-task=1 --pty /bin/bash`. In the above example, we request for 1 node with 1 cpu core, but you can request for additional resources as per your requirements.
1. To load anaconda, type `module load anaconda3/2022.05`.
1. To create your environment, type `conda create --prefix=/work/groupname/username/<yourenvironmentname> python=3.11 anaconda`, where \<yourenvironmentname> is the name you want to give your environment. Tip: to see a list of all of your conda environments, type `conda info -e`. 
1. Follow the prompts to complete the Conda install.
1. To activate your Conda environment, type `source activate <yourenvironmentname>/`. You can also use `conda activate `, though you may have to initilize conda first with `conda init `. Note, when using the `--prefix` to create your environment you will need to have a forward slash when activating the environment. If you are trying to activate your environment from a location other than the '--prefix' directory location you will have to run 'source activate' with the whole path i.e., `source activate /work/groupname/username/<yourenvironmentname>`.
1. You will notice that once your conda environment is activated your command line prompt has been modified with the full path of the environment, e.g., `(/work/groupname/username/newconda2) [username@c2001 dirname]$`. To You can clear this up by running the command: ``conda config --set env_prompt '({name}) '`` which will modify your .condarc file to only show the active envrionments name and not its full path: (newconda2) [username@c2000 dirname]$
1. With your Conda environment activated you can install a specific package with `conda install [package]`.
1. To deactivate the current, active Conda environment, type `conda deactivate`.
1. To delete a Conda environment and all of its related packages, type `conda remove -n <yourenvironmentname> --all`.

(mini-conda)=

## Working with a Miniconda environment

This procedure assumes that you have not installed Miniconda previously. If you need to update Miniconda, don't use the installation procedure. Use the
`conda update` command. This procedure uses the Miniconda3 version with Python version 3.8 in step 2, although there are other versions you can install, such as
Miniconda3 with Python 3.7.

**To install Miniconda:**

1. If you are on a login node, move to a compute node by typing `srun --partition=short --nodes=1 --cpus-per-task=1 --pty /bin/bash`.
1. Type `wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh` to get the latest version of Miniconda.
1. Type `sha256sum Miniconda3-latest-Linux-x86_64.sh` to check the hash key of the package.
1. Type `bash Miniconda3-latest-Linux-x86_64.sh -b -p <dir>` to start the installation, where `<dir>` should be replaced with the full path to your desired installation directory. For example, set it to `/work/<mygroup>/<mydirectory>/miniconda3` (recommended).
1. Type `source <dir>/bin/activate` to activate the miniconda environment.
1. Another recommended step is to update your Conda version (possible only when using conda you own): `conda update conda -y`

After installing, activating and updating Miniconda, you can create a new virtual Conda environment. In the example below, the Conda envinronment is named "my-python38environment" and installs Python version 3.8.

1. After completing steps 1 through 6 in the previous procedure, type `conda create --name my-python38environment python=3.8`.
1. Type `y` if asked to proceed with the installation.
1. Type `conda activate my-python38environment` to activate the environment.

To deactivate the environment, type `conda deactivate`. You can type this command again to deactivate the Miniconda environment.

## Conda best practices

1. Your .conda directory may get very large if you install multiple packages and create many virtual Conda environments. Make sure to clean the Conda cache and clean unused packages with: `conda clean --all`.
1. Clean unused Conda environments by first listing the environments with: `conda env list` , and then removing unused ones: `conda env remove --name <yourenvironmentname>`.
1. You can build Conda environments in different locations to save space on your home directory (see [Storage Accessible on Discovery](../storage/discovery_storage.md)). You can use the `--prefix` flag when building your environment. For example: `conda create myenv --prefix=/work/<mygroup>/<mydirectory>`.


[anaconda]: https://docs.anaconda.com
[conda]: https://docs.conda.io/en/latest/ 
[miniconda]: https://docs.conda.io/en/latest/miniconda.html 
[should i use anaconda or miniconda]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda
[Storage Accessible on Discovery]:../storage/discovery_storage.md
[New Storage Space request]:https://bit.ly/NURC-NewStorage .
