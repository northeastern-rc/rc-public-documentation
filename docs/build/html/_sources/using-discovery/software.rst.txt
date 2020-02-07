********************
Installing Software
********************

Before requesting software or installing software locally to your path, you should always first
check to see if the software package that you need is already available through one of the preinstalled
modules on Discovery. The Research Computing team adds new modules regularly, so first use the ``module avail`` command
to view the most up to date list. See :ref:`using_module` for working with module.

If you have a software request or need help with installing a software package, please submit a ServiceNow
software request ticket. Be aware that there might be packages that cannot be installed on Discovery due
to incompatibility with the hardware on Discovery.

We recommend that you try using Spack https://spack.io/ to install software locally to your path. Spack is a tool that conveniently installs
software packages to your local path. Please refer to the Spack documentation for the latest information on using Spack.

If you want to use ``make`` to add software locally to you path you must first download the
software package from its source (such as a webpage or Github), and you need to unpack it or unzip it, if it is archived/zipped.
Then, you must set the installation path to a directory where you have write access on Discovery, such as your home directory.
You can use ``./configure`` to do this, such as  ``./configure --prefix=/home/<yourusername>/software``
After you have set the install path, you need to compile the code using ``make`` and then install the software using ``make install``.
