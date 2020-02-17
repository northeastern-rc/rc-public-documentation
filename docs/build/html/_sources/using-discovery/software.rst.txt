********************
Installing Software
********************

Before requesting software or installing software locally to your path, you should always first
check to see if the software package that you need is already available through one of the preinstalled
modules on Discovery. The Research Computing team adds new modules regularly, so first use the ``module avail`` command
to view the most up to date list. See :ref:`using_module` for working with module.

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
2. Type ``git clone https://github.com/spack/spack.git`` to copy Spack to your /home directory.
3. Type ``srun -p short --pty --export=ALL -N 1 -n 28 --exclusive /bin/bash`` to allocate an interactive node. Spack will attempt to run ``make`` in parallel, so this ``srun`` request is for 28 cores on one node (-N 1 -n 28).
4. Type ``export SPACK_ROOT=/home/<yourusername>/spack`` to have Spack in your local environment so you can use the Spack commands.
5. Type ``spack list`` to see all of the software that you can install with Spack.
6. Type ``spack info <software name>`` to see information about a specific software package, including options and dependencies. Make sure to note the options and/or dependencies that you want to add or not add before installing the software.
7. Type ``spack install <software name> +<any dependencies or options>`` to install a software package plus any dependencies or options. You can also specify ``-<any dependencies or options>``.You can list ``+`` or ``-`` different options and dependencies within the same line. Do not put a space between each option/dependency that you list.


Using Make
==========

If you want to use ``make`` to add software locally to you path you must first download the
software package from its source (such as a webpage or Github), and you need to unpack it or unzip it, if it is archived/zipped.
Then, you must set the installation path to a directory where you have write access on Discovery, such as your home directory.
You can use ``./configure`` to do this, such as  ``./configure --prefix=/home/<yourusername>/software``
After you have set the install path, you need to compile the code using ``make`` and then install the software using ``make install``.
