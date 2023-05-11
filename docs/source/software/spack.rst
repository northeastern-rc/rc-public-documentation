.. _using_spack:

**************
Using Spack
**************
Research Computing recommends using `Spack <https://spack.io/>`_ to conveniently install software packages locally to your path.  Please refer to the `Spack documentation <https://spack.readthedocs.io/en/latest/index.html>`_  for the latest information about the `packages <https://spack.readthedocs.io/en/latest/package_list.html#package-list>`_ that Spack contains.
To use Spack, you first need to copy it to your /home directory or a /work directory, then have it in your local environment.

Getting started with Spack
==========================
These instructions will demonstrate how to install Spack in your local /home directory (step 2) and then how to add Spack to your local environment while on a compute node so you have access to the Spack commands (steps 4-5).

1. Connect to Discovery via ssh.
2. From the terminal, type ``git clone -c feature.manyFiles=true https://github.com/spack/spack.git`` to copy Spack to your /home directory.
3. Type ``srun -p short --pty -N 1 -n 28 /bin/bash`` to allocate an interactive job on a compute node. Spack will attempt to run ``make`` in parallel when it builds the software you choose to install, so this ``srun`` request is for 28 cores on one node (-N 1 -n 28).
To use Spack, it needs to add it to your local environment on the compute node, which is why this is completed after step 3.
4. To use a newer version of python for compatibility with Spack, type: ``module load python/3.8.1``.
5. To add Spack in your local environment so you can use the Spack commands, type ``export SPACK_ROOT=/home/<yourusername>/spack``.
6. Next, type ``. $SPACK_ROOT/share/spack/setup-env.sh``.
7. After you have the Spack commands in your environment, type ``spack help`` to ensure Spack is loaded in your environemnt and to see the commands you can use with Spack. You can also type ``spack list`` to see all of the software that you can install with Spack, but note this command can take some time to populate the list.
8. To see information about a specific software package, including options and dependencies, type ``spack info <software name>``. Make sure to note the options and/or dependencies that you want to add or not add before installing the software.
9. To install a software package plus any dependencies or options, type ``spack install <software name> +<any dependencies or options>``; you can specify ``-<any dependencies or options>``. You can also list ``+`` or ``-`` different options and dependencies within the same line. Do not put a space between each option/dependency that you list.
10.  To view your installed software packages, type ``spack find``. If you want to view information about a specific installed package, type ``spack find <software package name>``.

When you have installed a software package, you can add it to the module system by typing:
``. $SPACK_ROOT/share/spack/setup-env.sh``

.. note::

   Spack can be installed in a /work directory, which enables members of the /work directory to use the programs that are installed with Spack in that directory.

Installing LAMMPS with Spack example
=====================================
This section details how to install the LAMMPS application with the KOKKOS and User-reaxc packages using Spack.
This example assumes that you do not have any previous versions of LAMMPS installed. If you
have any previous versions of LAMMPS, you must uninstall them before using this procedure. To see if you have any previous versions of LAMMPS, type
``spack find lammps``. If you do have a previous version, you will need to unistal LAMMPS by typing ``spack uninstall --dependents lammps``. Then, you
can try the example procedure below. Note that the installation can take about two hours to complete. As part of the procedure, we recommend that you initiate a `screen session <https://www.gnu.org/software/screen/>`_
so that you can have the installation running as a separate process if you need to do other work on Discovery. If you decide to use screen, make note of the compute node number (compute node numbers start with c or d with four numbers, such as c0123)
to make it easier to check on the progress of the installation.

1. Install Spack by following steps 1 through 5 in the Getting started with Spack procedure above.
2. Type ``exit`` to exit from the compute node you requested in step 2 above.
3. Type the following to request a GPU node for 8 hours::

     srun --partition=gpu --nodes=1 --ntasks=14 --pty --export=All --gres=gpu:1 --mem=0 --time=08:00:00 /bin/bash

4. (Optional) Initiate a ``screen`` session:

   a. Type ``screen -S lammps-install`` to create a screen session.
   b. Type ``screen -ls`` to check to see if the session was created (you'll see it listed if it was successfully created).
   c. Type ``screen -rd lammps-install`` to enter that screen session.
   d. Type ``echo $STY`` to check that you are in the screen session.
   e. Type ``CTRL+A+D`` to exit the screen.

5. Type::

     spack install lammps +asphere +body +class2 +colloid +compress +coreshell +cuda cuda_arch=70 +cuda_mps +dipole +granular +kokkos +kspace +manybody +mc +misc +molecule +mpiio +peri +python +qeq +replica +rigid +shock +snap +spin +srd +user-reaxc +user-misc

6. Type ``spack find LAMMPS`` to view your installed software package.
7. Type ``spack load lammps``.
