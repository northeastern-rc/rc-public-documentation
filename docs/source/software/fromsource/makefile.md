(make)=
# Make
:::{important}
Be sure to refer to the installation instructions provided with software being installed. If the software requires additional dependencies not installed on the system, they might need to installed and added to your `PATH` similarly.
:::

If you want to use `make` to add software locally to your path, you must first download the software package from its source (e.g., its webpage or GitHub) and unpack it or unzip it if need be. Then, you must set the installation path to a directory with write access on the cluster, such as your home directory or your `/projects`.

:::{note}
You can use `./configure` to specify the installation path (e.g., `./configure --prefix=${HOME}/software`).
:::

After setting the installation path, compile the code via `make` and then install the software using `make install`.

## Makefile Example: Installing FFTW Library

Even without root access, you can install software system-wide by installing it in your home directory. Let us continue with the FFTW library as an example.

1. Download the FFTW tarball. Here, we download version 3.3.9:
    :::{code} bash
    cd ~
    wget http://www.fftw.org/fftw-3.3.9.tar.gz
    :::

1. Extract the tarball:
    :::{code} bash
    tar xzf fftw-3.3.9.tar.gz
    :::

1. Move into the directory:

    :::{code} bash
    cd fftw-3.3.9
    :::

1. Configure the build process, specifying the prefix as a location in your home directory. This location is where the library will be installed. Note that the specified directory should be in your `PATH` to ensure system-wide accessibility.
    :::{code} bash
    ./configure --prefix=$HOME/fftw
    :::

1. Compile the software:
    :::{code} bash
    make -j 8
    :::

1. Instead of the default `make install`, which typically requires root access for system-wide installation, you can `make install` with the prefix configuration to install the software in your home directory.
    :::{code} bash
    make install
    :::

The FFTW library should now be installed in the `fftw` directory in your home directory.

:::::{important}
Include the location of the software in your `PATH` to access directly. This can be done by adding the following line to your `~/.bashrc`:

::::{code} bash
export PATH=$HOME/fftw/bin:$PATH
::::

This puts the program in your path so that the system can find the FFTW library binaries when called.

::::{note}
You need to source your profile or restart your shell for these changes to take effect, which is done as follows:

:::{code} bash
source ~/.bashrc
:::
::::
:::::

(make-lammps-example)=
## Makefile Example: Installing LAMMPS
:::{seealso}
{ref}`cmake-lammps-example`
:::
:::{note}
There are no configure options used and the information is stored within the makefiles `mylammps/MAKE` in the `make.serial` and `make.mpi` files.
:::
:::
The following instructions to build LAMMPS using make.
1. To allocate an interactive job on compute node type:
   ::::{code-block} bash
   srun -N 1 -p short -n 28 --constraint=ib --pty /bin/bash
   ::::
1. Load the following modules required for building LAMMPS:
   ::::{code-block} bash
   module load OpenMPI/4.1.6
   # module load python/3.9.18  # In case a different version of python is needed and available
   # module load gcc/11.4.1     # In case a different version of gcc is needed and available
   ::::
1. Change the directory to the `src` directory using the command `cd /path/to/mylammps/src`
1. Use the following command to build serial version or the MPI version of LAMMPS depending on the requirement. This will generate `lmp_serial` binary for a serial build and `lmp_mpi` for an MPI build.
   ::::{code-block} bash
   make serial
   make mpi
   ::::

Now you can start running the program, using `./lmp_serial` or `mpirun -n 1 ./lmp_mpi -h`.
