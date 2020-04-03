.. _installing_software:

********************
Installing Software
********************

Before requesting software or installing software locally to your path, you should always first
check to see if the software package that you need is already available through one of the preinstalled
modules on Discovery. The Research Computing team adds new modules regularly, so first use the ``module avail`` command
to view the most up to date list. See :ref:`using_module` for more information about working with module.

Requesting Software Installation
=================================

If you have a software request or need help with installing a software package, please submit a `ServiceNow
software request ticket <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=777c510bdbebd340a37cd206ca9619b0>`_. Be aware that there might be packages that cannot be installed on Discovery due
to incompatibility with the hardware on Discovery.

Using Spack
===========

We recommend that you try using `Spack <https://spack.io/>`_ to install software locally to your path. Spack is a tool that conveniently installs
software packages to your local path. Please refer to the Spack documentation for the latest information on using Spack.

1. Connect to Discovery.
2. Type ``git clone https://github.com/spack/spack.git``  to copy Spack to your /home directory.
3. Type ``srun -p short --pty --export=ALL -N 1 -n 28 --exclusive /bin/bash`` to allocate an interactive node. Spack will attempt to run ``make`` in parallel, so this ``srun`` request is for 28 cores on one node (-N 1 -n 28).
4. To have Spack in your local environment so you can use the Spack commands, type ``export SPACK_ROOT=/home/<yourusername>/spack``.
5. Then type ``. $SPACK_ROOT/share/spack/setup-env.sh``.
6. After you have the Spack commands in your path, type ``spack list`` to see all of the software that you can install with Spack.
7. Type ``spack info <software name>`` to see information about a specific software package, including options and dependencies. Make sure to note the options and/or dependencies that you want to add or not add before installing the software.
8. Type ``spack install <software name> +<any dependencies or options>`` to install a software package plus any dependencies or options. You can also specify ``-<any dependencies or options>``.You can list ``+`` or ``-`` different options and dependencies within the same line. Do not put a space between each option/dependency that you list.


Using Make
==========

If you want to use ``make`` to add software locally to you path you must first download the
software package from its source (such as a webpage or Github), and you need to unpack it or unzip it, if it is archived/zipped.
Then, you must set the installation path to a directory where you have write access on Discovery, such as your home directory.
You can use ``./configure`` to do this, such as  ``./configure --prefix=/home/<yourusername>/software``
After you have set the install path, you need to compile the code using ``make`` and then install the software using ``make install``.

Creating a Python Environment
==============================

Using a locally installed conda virtual environment is highly recommended so that you can install the specific packages that you need.
You can also have more than one environment with different packages for testing purposes.

1. To check what version of Python you have installed, type ``which python``.
2. To load anaconda, type ``module load anaconda3/3.7``.
3. To create your environment, type ``conda create -n <yourenvironmentname> python3.7 anaconda``, where <yourenvironmentname> is the name you want to give your environment. Tip: to see a list of all of your conda environments, type ``conda info -e``.
4. Follow the prompts to complete the conda install.
5. To activate your conda environment, type ``source activate <yourenvironmentname>``. Note that ``conda activate`` will not work on Discovery.
6. To install a specific package, type ``conda install -n <yourenvironmentname> [package]``.
7. To deactivate the current, active conda environment, type ``conda deactivate``.
8. To delete a conda environment and all of its related packages, type ``conda remove -n <yourenvironmentname> --all``.

Installing Matlab toolboxes
===========================

Use the following procedure if you need to install a Matlab toolbox:

1. Download the toolbox from its source website.
2. Connect to Discovery.
3. Create a directory in your /home directory. We recommend creating a directory called ``matlab``::

    mkdir /home/<username>/matlab  #where <username> is your username

4. Go to the directory you just created::

    cd /home/<username>/matlab

5. Unzip the toolbox file::

    unzip <toolboxname>

6. Load Matlab::

    module load matlab

7. Start Matlab::

    matlab

8. Add the toolbox to your PATH::

    addpath('/home/<username>/matlab/<toolbox>') #where <toolbox> is the name of the toolbox you just unzipped

9. If this is a toolbox you want to use more than once, you should save it to your path::

    savepath()

10. You can now use the toolbox within Matlab. When you are done, type ``quit``.
