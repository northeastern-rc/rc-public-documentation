(cmake)=
# CMake

## CMake Example: Serial LAMMPS Build
:::{note}
This is a minimal example using the command line version of CMake to build LAMMPS with no customization.
::::
1. To allocate an interactive job on compute node type:
   ::::{code-block} bash
   srun -p short --pty -N 1 -n 28 /bin/bash
   ::::
1. Download the source code to LAMMPS:
   ::::{code-block} bash
   cd ~
   wget https://github.com/lammps/lammps/archive/refs/tags/stable_29Aug2024.tar.gz
   tar -xvf stable_29Aug2024.tar.gz 
   ::::
1. Load the following modules required for building LAMMPS:
   ::::{code-block} bash
   # module load gcc/11.4.1   # In case a different version of gcc is needed
   module load cmake/3.30.2
   ::::
1. For LAMMPS, you will need to create and use the build directory with the following command:
   ::::{code-block} bash
   cd lammps-stable_29Aug2024
   mkdir -p build
   cd build/
   ::::
1. Load the CMake module and use CMake to generate a build environment in a new directory.
   ::::{code-block} bash
   cmake -C ../cmake/presets/most.cmake ../cmake
   ::::
1. Next, you will work on the compilation and linking of all objects, libraries, and executables using the selected build tool.
   ::::{code-block} bash
   cmake --build .
   make install
   ::::
1. The `cmake --build` command will launch the compilation, which, if successful, will ultimately generate an executable `lmp`inside the`build`folder. Now you can start running LAMMPS using `./lmp`. To use the LAMMPS build, you will need to setup your environment so the binaries are in your PATH. This can be completed by including the following export statement in your sbatch script or have it as a script that you can source in your job script:
   ::::{code-block} bash
   #!/bin/bash
   #SBATCH -N 1
   #SBATCH -n 1
   #SBATCH -p short

   # module load gcc/11.4.1  # In case a different version of gcc is needed

   export PATH=/home/$USER/lammps-stable_29Aug2024/build:$PATH

   cd ~
   lmp -in /home/$USER/lammps-stable_29Aug2024/examples/melt/in.melt
   ::::

   or create the following script in your `$HOME` called `lammps_env.sh`

   ::::{code-block} bash
   #!/bin/bash
   # module load gcc/11.1.0 # In case a different version of gcc is needed

   export PATH=/home/$USER/lammps-stable_29Aug2024/build:$PATH
   ::::

   and modify your sbatch job script to source this environment file that will setup your environment for your job:

   ::::{code-block} bash
   #!/bin/bash
   #SBATCH -N 1
   #SBATCH -n 1
   #SBATCH -p short
   
   source /home/$USER/lammps_env.sh

   cd ~
   lmp -in /home/$USER/lammps-stable_29Aug2024/examples/melt/in.melt
   ::::

(cmake-lammps-example)=
## CMake Example: Parallel LAMMPS Build
:::{seealso}
{ref}`make-lammps-example`
:::
The following instructions to build LAMMPS using cmake.
1. Running LAMMPS in parallel is possible using a domain decomposition parallelization. In order to build the MPI version, first allocate an interactive job on compute node by typing:
   ::::{code-block} bash
   srun -N 1 -p short -n 28 --constraint=ib --pty /bin/bash
   ::::
1. Download the source code to LAMMPS:
   ::::{code-block} bash
   cd ~
   wget https://github.com/lammps/lammps/archive/refs/tags/stable_29Aug2024.tar.gz
   tar -xvf stable_29Aug2024.tar.gz 
   ::::
1. Load the required modules required for building LAMMPS:
   ::::{code-block} bash
   # module load gcc/11.1.0  # In case a different version of gcc is needed
   module OpenMPI/4.1.6
   module load cmake/3.30.2
   ::::
1. For LAMMPS, you will need to create and use the build directory with the following command:
   ::::{code-block} bash
   cd lammps-stable_29Aug2024
   mkdir -p build
   cd build/
   ::::
1. In the build directory, run the following commands with `DBUILD_MPI=yes`  to build the MPI version :
   ::::{code-block} bash
   cmake -C ../cmake/presets/most.cmake ../cmake -DBUILD_MPI=yes
   cmake --build .
   make install
   ::::
1. The instructions above will create a `lmp` inside the `build` directory that is MPI compliant. To use the LAMMPS build,
   you will need to setup your environment so the binaries are in your PATH. This can be completed by including the following export statement in your sbatch script or have it as a script that you can source in your job script:
   ::::{code-block} bash
   #!/bin/bash
   #SBATCH -N 1
   #SBATCH -n 8
   #SBATCH -p short

   # module load gcc/11.1.0  # In case a different version of gcc is needed/available
   module openmpi/OpenMPI/4.1.6

   export PATH=/home/$USER/lammps-stable_29Aug2024/build:$PATH

   cd ~
   mpirun -n 8 lmp_mpi -in /home/$USER/lammps-stable_29Aug2024/examples/melt/in.melt
   ::::

   or create the following script in your `$HOME` called `lammps_env.sh`

   ::::{code-block} bash
   #!/bin/bash
   # module load gcc/11.1.0 # In case a different version of gcc is needed
   module OpenMPI/4.1.6

   export PATH=/home/$USER/lammps-stable_29Aug2024/build:$PATH
   ::::

   and modify your sbatch job script to source this environment file that will setup your environment for your job:

   ::::{code-block} bash
   #!/bin/bash
   #SBATCH -N 1
   #SBATCH -n 8
   #SBATCH -p short
   
   source /home/$USER/lammps_env.sh

   cd ~
   mpirun -n 8 lmp_mpi -in /home/$USER/lammps-stable_29Aug2024/examples/melt/in.melt
   ::::

:::{note}
When compiled with MPI, the binaries expect `mpirun` or `mpiexec` with the number of tasks to run.
:::
Now, you can start running LAMMPS using `mpirun -n 1 ./lmp -h`.
