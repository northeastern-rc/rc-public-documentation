.. _software_overview:

******************
Software overview
******************
Discovery offers you many options for working with software. Two of the easiest and most convenient ways are
using the ``module`` command on the command line and using the interactive apps on Open onDemand (OOD), Discovery's web portal.
If you need a specific software package, first check to see if it is already available through one of the preinstalled
modules on Discovery. The Research Computing team adds new modules regularly, so use the ``module avail`` command
to view the most up to date list. You can also try using Spack, a software package manager available on Discovery. Spack has over 5000 packages that
you can install.

See :ref:`using_module` for more information about working with module.

See :ref:`accessing_ood` for more information about OOD.

See :ref:`using_spack` for more information about Spack.

You can also use Conda, Miniconda, and Anaconda to manage software packages. See :ref:`working_conda` for more information.

Using Make
==========
If you want to use ``make`` to add software locally to you path you must first download the
software package from its source (such as a webpage or Github), and you need to unpack it or unzip it, if it is archived/zipped.
Then, you must set the installation path to a directory where you have write access on Discovery, such as your home directory.
You can use ``./configure`` to do this, such as  ``./configure --prefix=/home/<yourusername>/software``
After you have set the install path, you need to compile the code using ``make`` and then install the software using ``make install``.

Requesting Software Installation Assistance
============================================
If the software that you need is not a module on Discovery, cannot be installed through Spack, or is not available through another way of
self-installation (such as using ``make``), you can submit a `ServiceNow
software request ticket <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=777c510bdbebd340a37cd206ca9619b0>`_.
Be aware that there might be packages that cannot be installed on Discovery due
to incompatibility with the hardware on Discovery.
