.. _using_spack:

**************
Using Spack
**************
We recommend that you try using `Spack <https://spack.io/>`_ to install software locally to your path. Spack is a tool that conveniently installs
software packages to your local path. Please refer to the `Spack documentation <https://spack.readthedocs.io/en/latest/index.html>`_  for the latest information about the `packages <https://spack.readthedocs.io/en/latest/package_list.html#package-list>`_ that Spack contains.
To use Spack, you first need to copy it to your /home directory, then have it in your local environment. Use the procedure below to get started with Spack on Discovery.

Getting started with Spack
==========================

1. Connect to Discovery.
2. Type ``git clone https://github.com/spack/spack.git``  to copy Spack to your /home directory.
3. Type ``srun --partition=short,lowpriority --pty --export=ALL -N 1 -n 28 --exclusive /bin/bash`` to allocate an interactive node. Spack will attempt to run ``make`` in parallel, so this ``srun`` request is for 28 cores on one node (-N 1 -n 28).
4. To have Spack in your local environment so you can use the Spack commands, type ``export SPACK_ROOT=/home/<yourusername>/spack``.
5. Then type ``. $SPACK_ROOT/share/spack/setup-env.sh``.
6. After you have the Spack commands in your path, type ``spack list`` to see all of the software that you can install with Spack.
7. Type ``spack info <software name>`` to see information about a specific software package, including options and dependencies. Make sure to note the options and/or dependencies that you want to add or not add before installing the software.
8. Type ``spack install <software name> +<any dependencies or options>`` to install a software package plus any dependencies or options. You can also specify ``-<any dependencies or options>``.You can list ``+`` or ``-`` different options and dependencies within the same line. Do not put a space between each option/dependency that you list.
9. Type ``spack find`` to view your installed software packages, or type ``spack find <software package name>`` to view information about a specific installed package.

When you have installed a software package, you can add it to the module system by typing:
``. $SPACK_ROOT/share/spack/setup-env.sh``

Installing LAMMPS with Spack example
=====================================
This section details how to install an application called LAMMPS with the KOKKOS and User-reaxc packages using Spack.
This example assumes that you do not have any previous versions of LAMMPS installed. If you
have any previous versions of LAMMPS, you must uninstall them before using this procedure. To see if you have any previous versions of LAMMPS, type
``spack find lammps``. If you do have a previous version, type ``spack uninstall --dependents lammps`` to uninstall LAMMPS. Then, you
can try the example procedure below. Note that the installation can take about two hours to complete. As part of the procedure, we recommend that you initiate a `screen session <https://www.gnu.org/software/screen/>`_
so that you can have the installation running as a separate process if you need to do other work on Discovery. If you decide to use screen, make note of the compute node number (compute node numbers start with c or d with four numbers, such as c0123)
to make it easier to check on the progress of the installation.

1. Install Spack by following steps 1 through 5 in the Getting started with Spack procedure above.
2. Type ``exit`` to exit from the compute node you requested in step 2 above.
3. Type the following to request a GPU node for 8 hours::

     srun --partition=gpu,lowpriority --nodes=1 --ntasks=14 --pty --export=All --gres=gpu:1 --mem=0 --time=08:00:00 /bin/bash

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
