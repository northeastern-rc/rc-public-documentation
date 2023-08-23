(cmake)=
# CMake

## CMake Example: Serial LAMMPS Build
:::{note}
This is a minimal example using the command line version of CMake to build LAMMPS with no add-on packages enabled and no customization.
::::
1. To allocate an interactive job on compute node type:
   ::::{code-block} bash
   srun -p short --pty -N 1 -n 28 /bin/bash
   ::::
1. For LAMMPS, you will need to create and use the build directory with the following command:
   ::::{code-block} bash
   mkdir build
   cd build/
   ::::
1. Load the CMake module and use CMake to generate a build environment in a new directory.
   ::::{code-block} bash
   module load cmake/3.23.2
   cmake ../cmake
   ::::
1. Next, you will work on the compilation and linking of all objects, libraries, and executables using the selected build tool.
   ::::{code-block} bash
   cmake --build .
   make install
   ::::
1. The `cmake --build` command will launch the compilation, which, if successful, will ultimately generate an executable `lmp`inside the`build`folder. Now you can start running LAMMPS using `./lmp`.

(cmake-lammps-example)=
## CMake Example: Parallel LAMMPS Build
:::{seealso}
{ref}`make-lammps-example`
:::
The following instructions to build LAMMPS using cmake.
1. Running LAMMPS in parallel is possible using a domain decomposition parallelization. In order to build the MPI version, first allocate an interactive job on compute node by typing:
   ::::{code-block} bash
   srun -N 1 -n 28 --constraint=ib --pty /bin/bash
   ::::
1. Load the required modules required for building LAMMPS:
   ::::{code-block} bash
   module load openmpi/4.0.5
   module load cmake/3.23.2
   ::::
1. For LAMMPS, you will need to create and use the build directory with the following command:
   ::::{code-block} bash
   mkdir build
   cd build/
   ::::
1. In the build directory, run the following commands with `DBUILD_MPI=yes`  to build the MPI version :
   ::::{code-block} bash
   cmake ../cmake -DBUILD_MPI=yes
   cmake --build .
   make install
   ::::

The instructions above will create a `lmp` inside the `build` directory.

:::{note}
When compiled with MPI, the binaries expect `mpirun` or `mpiexec` with the number of tasks to run.
:::
Now, you can start running LAMMPS using `mpirun -n 1 ./lmp -h`.
