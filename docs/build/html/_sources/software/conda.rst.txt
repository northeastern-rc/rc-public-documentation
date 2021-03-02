.. _working_conda:

**************************************
Working with Conda/Miniconda/Anaconda
**************************************
`Conda <https://docs.conda.io/en/latest/>`_ is an open source environment and package manager. `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ is a free installer for Conda, Python,
and a few other useful packages. `Anaconda <https://docs.anaconda.com/anacondaorg/faq/>`_ is also a package manager that has a much larger number of packages that you can install.
A question that frequently comes up is "Should I use Anaconda or Miniconda?" The Conda documentation site has a topic that can help you to decide which package manager to use: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda.

.. _creating_python:

Creating a Conda virtual environment with Anaconda
===================================================

Using a locally installed Conda virtual environment is highly recommended so that you can install the specific packages that you need.
You can also have more than one environment with different packages for testing purposes. This procedure uses the Anaconda module already loaded on Discovery.

1. To check what version of Python you have installed, type ``which python``.
2. To load anaconda, type ``module load anaconda3/3.7``.
3. To create your environment, type ``conda create -n <yourenvironmentname> python=3.7 anaconda``, where <yourenvironmentname> is the name you want to give your environment. Tip: to see a list of all of your conda environments, type ``conda info -e``.
4. Follow the prompts to complete the Conda install.
5. To activate your Conda environment, type ``source activate <yourenvironmentname>``. Note that ``conda activate`` will not work on Discovery with this version.
6. To install a specific package, type ``conda install -n <yourenvironmentname> [package]``.
7. To deactivate the current, active Conda environment, type ``conda deactivate``.
8. To delete a Conda environment and all of its related packages, type ``conda remove -n <yourenvironmentname> --all``.

Working with a Miniconda environment
======================================
This procedure assumes that you have not installed Miniconda previously. If you need to update Miniconda, don't use the installation procedure. Use the
``conda update`` command. This procedure uses the Miniconda3 version with Python version 3.8 in step 2, although there are other versions you can install, such as
Miniconda3 with Python 3.7.

**To install Miniconda:**

1. If you are on a login node, move to a compute node by typing ``srun --partition=short --nodes=1 --cpus-per-task=1 --pty /bin/bash``.
2. Type ``wget --quiet https//repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`` to get the latest version of Miniconda.
3. Type ``sha256sum Miniconda3-latest-Linux-x86_64.sh`` to check the hash key of the package.
4. Type ``bash Miniconda3-latest-Linux-x86_64.sh`` to start the installation.
5. Press ``Enter`` to review the license agreement.
6. Type ``yes`` to agree to the license agreement.
7. Press ``Enter`` to accept the default installation location (your /home directory, e.g. /home/<yourusername>/miniconda3).
8. Type ``yes`` if asked to initialize Miniconda using conda init.
9. Type ``source miniconda3/bin/activate`` to activate the miniconda environment.

After installing and activating Miniconda, you can create a Conda environment. In the example below, the Conda envinronment is named "my-python38environment" and installs Python version 3.8.

1. After completing steps 1 through 9 in the previous procedure, type ``conda create --name my-python38environment python=3.8``.
2. Type ``y`` if asked to proceed with the installation.
3. Type ``conda activate my-python38environment`` to activate the environment.

To deactivate the environment, type ``conda deactivate``. You can type this command again to deactivate the Miniconda environment.
