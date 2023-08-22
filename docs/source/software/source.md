(from-source)=

# Software Installation from Source

Software packages that are not available as Modules or cannot be installed using Spack can be installed from source. We recommend that you follow the official instructions depending on the software type such as README or INSTALLATION files for instructions to install any software.

:::{note}
Software installations are part of your research and should preferably be stored in your PI's `/work` directory.
:::

Download the software package from its source (such as a webpage or GitHub) using one of the following options:

1. To download the software and store in it a zip file, use the curl command `curl --output <dirName.tar.gz> <sourceCodeLink>`.
To unzip your file, use the following command: `tar -zxf <dirName.tar.gz>`

2. To clone it from GitHub, run the following command `git clone -b release <sourceCodeLink> <dirName>`.

3. LAMMPS Example:
`git clone -b release https://github.com/lammps/lammps.git mylammps`

# Using LAMMPS as an example

## Serial LAMMPS Build

1. Type `srun -p short --pty -N 1 -n 28 /bin/bash` to allocate an interactive job on compute node.
2. For LAMMPS, you will need to create and use the build directory with the following command:

   ::::{code-block} bash
   mkdir build
   cd build/
   ::::

3. Load the CMake module and use CMake to generate a build environment in a new directory.

   ::::{code-block} bash
   module load cmake/3.23.2
   cmake ../cmake
   ::::

4. Next, you will work on the compilation and linking of all objects, libraries, and executables using the selected build tool.

   ::::{code-block} bash
   cmake --build .
   make install
   ::::

   Please note, this is a minimal example using the command line version of CMake to build LAMMPS with no add-on packages enabled and no customization.

5. The `cmake --build` command will launch the compilation, which, if successful, will ultimately generate an executable `lmp`inside the`build`folder. Now you can start running LAMMPS using `./lmp`.

## Parallel LAMMPS Build

1. Running LAMMPS in parallel is possible using a domain decomposition parallelization. In order to build the MPI version, Type `srun -N 1 -n 28 --constraint=ib --pty /bin/bash` to allocate an interactive job on compute node.

2. Load the required modules required for building LAMMPS:

   ::::{code-block} bash
   module load openmpi/4.0.5
   module load cmake/3.23.2
   ::::

3. For LAMMPS, you will need to create and use the build directory with the following command:

   ::::{code-block} bash
   mkdir build
   cd build/
   ::::

4. In the build directory, run the following commands with `DBUILD_MPI=yes`  to build the MPI version :

   ::::{code-block} bash
   cmake ../cmake -DBUILD_MPI=yes
   cmake --build .
   make install
   ::::

The above will generate `lmp` inside the `build` folder. Please note, when compiled with MPI, the binaries are expecting to be started with mpirun or mpiexec with the number of tasks it wants to run on. So now you can start running LAMMPS using `mpirun -n 1 ./lmp -h`.

## LAMMPS Build Using make

LAMMPS can also be built using make; use the following instructions to build LAMMPS using make:

1. Type `srun -N 1 -n 28 --constraint=ib --pty /bin/bash` to allocate an interactive job on compute node.

2. Load the following modules required for building LAMMPS:
   ::::{code-block} bash
   module load openmpi/4.0.5
   module load python/3.6.6
   module load gcc/9.2.0
   ::::

3. Change the directory to the `src` directory using the command `cd /path/to/mylammps/src`

4. Use the following command to build serial version or the MPI version of LAMMPS depending on the requirement. This will generate `lmp_serial` binary for a serial build and `lmp_mpi` for an MPI build.
   ::::{code-block} bash
   make serial
   make mpi
   ::::

Now you can start running the program, using `./lmp_serial` or `mpirun -n 1 ./lmp_mpi -h`

:::{note}
Please note that there were no configure options and the information is stored within the makefiles `mylammps/MAKE` in the `make.serial` and `make.mpi` files.
:::

   
