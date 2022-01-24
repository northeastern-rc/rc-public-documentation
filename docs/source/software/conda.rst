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
2. To load anaconda, type ``module load anaconda3/2022.01``.
3. To create your environment, type ``conda create -n <yourenvironmentname> python=3.7 anaconda``, where <yourenvironmentname> is the name you want to give your environment. Tip: to see a list of all of your conda environments, type ``conda info -e``. To save space, also use the ``--prefix=/work/<mygroup>/<mydirectory>`` flag to build in your work directory.
4. Follow the prompts to complete the Conda install.
5. To activate your Conda environment, type ``source activate <yourenvironmentname>``. Note that ``conda activate`` will not work on Discovery with this version.
6. To install a specific package, type ``conda install -n <yourenvironmentname> [package]``.
7. To deactivate the current, active Conda environment, type ``conda deactivate``.
8. To delete a Conda environment and all of its related packages, type ``conda remove -n <yourenvironmentname> --all``.

.. _mini_conda:

Working with a Miniconda environment
======================================
This procedure assumes that you have not installed Miniconda previously. If you need to update Miniconda, don't use the installation procedure. Use the
``conda update`` command. This procedure uses the Miniconda3 version with Python version 3.8 in step 2, although there are other versions you can install, such as
Miniconda3 with Python 3.7.

**To install Miniconda:**

1. If you are on a login node, move to a compute node by typing ``srun --partition=short --nodes=1 --cpus-per-task=1 --pty /bin/bash``.
2. Type ``wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`` to get the latest version of Miniconda.
3. Type ``sha256sum Miniconda3-latest-Linux-x86_64.sh`` to check the hash key of the package.
4. Type ``bash Miniconda3-latest-Linux-x86_64.sh -b -p <dir>`` to start the installation, where ``<dir>`` should be replaced with the full path to your desired installation directory. For example, set it to ``/work/<mygroup>/<mydirectory>/miniconda3`` (recommended).
5. Type ``source <dir>/bin/activate`` to activate the miniconda environment.
6. Another recommended step is to update your Conda version (possible only when using conda you own): ``conda update conda -y``

After installing, activating and updating Miniconda, you can create a new virtual Conda environment. In the example below, the Conda envinronment is named "my-python38environment" and installs Python version 3.8.

1. After completing steps 1 through 6 in the previous procedure, type ``conda create --name my-python38environment python=3.8``.
2. Type ``y`` if asked to proceed with the installation.
3. Type ``conda activate my-python38environment`` to activate the environment.

To deactivate the environment, type ``conda deactivate``. You can type this command again to deactivate the Miniconda environment.

Conda best practices
====================

1. Your .conda directory may get very large if you install multiple packages and create many virtual Conda environments. Make sure to clean the Conda cache and clean unused packages with: ``conda clean --all``.
2. Clean unused Conda environments by first listing the environments with: ``conda env list`` , and then removing unused ones: ``conda env remove --name <yourenvironmentname>``.
3. You can build Conda environments in different locations to save space on your home directory (see :ref:`discovery_storage`). You can use the ``--prefix`` flag when building your environment. For example: ``conda create myenv --prefix=/work/<mygroup>/<mydirectory>``.

.. note::
  It is not recommended to build your Miniconda and virtual Conda environments inside your /home directory due to its limited space qouta and lower performance of the file system (see :ref:`discovery_storage`). If your group does not have access to /work, the group PI can request it using the `New Storage Space request <https://bit.ly/NURC-NewStorage>`_ .
