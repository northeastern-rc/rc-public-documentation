(using-mpi)=
# Using MPI

[Messaging Passing Interface (MPI)] is a standardized and portable message-passing system designed to function on a wide variety of parallel computing architectures. It provides a library of functions that enable a program to distribute a computational task across multiple nodes in a cluster.

There are multiple implementations of MPI including [OpenMPI] (Open Source Message Passing Interface), [MPICH], and [Intel MPI]. OpenMPI is a widely used MPI implementation in the HPC community and the one we will be working with through our documentation.

## Getting Started with MPI

To get started with MPI on a Slurm-based HPC cluster, you should have:
- Basic knowledge of Linux/Unix commands
- Familiarity with a programming language supported by MPI (e.g., C, C++, FORTRAN) if you are developing a program
- Understand how to load MPI module on the HPC
- Understand how to compile your source code and run the binaries (compiled languages) or to run the interpreted language with MPI

### MPI libraries on Discovery

There are many versions of OpenMPI, MVAPICH, and MPICH that are available on the HPC as modules compiled with different compilers and additional libraries and features. To see them, use the `module avail openmpi`, `module avail mpich`, and `module avail mvapich` respectively.

Use the `module show` command to view information about the compilers you need to use with these libraries and if they support InfiniBand (IB) or not. For example, `module show openmpi/4.1.0-zen2-gcc10.1`.

::::{dropdown} Output for `module show openmpi/4.1.0-zen2-gcc10.1`
:::{code} bash
/shared/centos7/modulefiles/openmpi/4.1.0-zen2-gcc10.1:

module-whatis	 Loads the executables, libraries and headers for OpenMPI v. 4.1.1. Built using Intel 2021 compilers on AMD EPYC architecture (zen2).

Please note - this MPI module supports communication through the HDR200 InfiniBand network by using the Mellanox (OFED 5.3) UCX (1.10.1) framework with cross platform unified API. To make sure InfiniBand is being used, make sure to compile and run your applications using this module only on AMD EPYC architectures (zen2).

To allocate the zen2 arch compute node, add the following flag to your SLURM command: --constraint=zen2
For more details:
https://rc-docs.northeastern.edu/en/latest/hardware/hardware_overview.html

To use the module, type:
module load gcc/10.1.0
module load openmpi/4.1.0-zen2-gcc10.1


conflict	 openmpi
prepend-path	 PATH /shared/centos7/openmpi/4.1.0-zen2-gcc10.1/bin
prepend-path	 MANPATH /shared/centos7/openmpi/4.1.0-zen2-gcc10.1/share/man
prepend-path	 LD_LIBRARY_PATH /shared/centos7/openmpi/4.1.0-zen2-gcc10.1/lib
prepend-path	 CPATH /shared/centos7/openmpi/4.1.0-zen2-gcc10.1/include
prepend-path	 LIBRARY_PATH /shared/centos7/openmpi/4.1.0-zen2-gcc10.1/lib
setenv		 OMPI_MCA_btl ^vader,tcp,openib,uct
:::
::::

## Running a MPI Program

The following is a basic slurm script for running an MPI program with annotations:

:::{code-block} bash
#!/bin/bash
#SBATCH --job-name=test_job         # Set the job name
#SBATCH --output=res_%j.out         # Set the output file name (%j expands to jobId)
#SBATCH --ntasks=4                  # Request 4 tasks
#SBATCH --time=01:00:00             # Request 1 hour runtime
#SBATCH --mem-per-cpu=2000          # Request 2000MB memory per CPU

module load openmpi/4.0.5           # Load the necessary module(s)
mpirun -n 4 ./your_program          # Run your MPI executable
:::

:::{note}
For MPI tasks, `--ntasks=X` is used, where `X` requests the number of cpu cores for tasks.
:::

This script specifies that it needs 4 tasks (i.e., CPU cores), a maximum of 10 minutes of runtime, and 2000MB of memory per CPU. It then loads the OpenMPI module and runs the MPI program using mpirun.

:::{tip}
Best practice for writing your sbatch script is including the versions of the modules you are loading to ensure you always have your expected environment on the HPC.
:::

## OpenMPI Tuning for Performance Optimization

OpenMPI provides a variety of environment variables that can be used to optimize the runtime characteristics of your MPI program for maximum performance. For instance, you can specify which network interfaces to use by setting the `OMPI_MCA_btl` variable:

:::{code-block} bash
export OMPI_MCA_btl=self,vader,tcp
:::

:::{tip}
You can also include or exclude certain network interfaces by setting the `OMPI_MCA_btl_tcp_if_include` or `OMPI_MCA_btl_tcp_if_exclude` variables.
:::

Also you can check if certain MPI modules already have certain `OMPI_MCA_btl` set by using the `module show` command and looking for the `setenv` options listed.

In addition, OpenMPI lets you control the placement of processes on nodes, which can be critical for performance. The `--map-by` and `--bind-to` options dictate how processes are mapped to hardware resources and how they are bound to those resources, respectively.

Remember, optimizing for performance often requires a thorough understanding of your application, your hardware, and MPI.

## Troubleshooting and Debugging MPI Programs

Debugging MPI programs can be challenging due to their parallel nature. Fortunately, OpenMPI provides several tools and techniques to help with this.

One useful feature is verbose error reporting. To enable this, set the `OMPI_MCA_mpi_abort_print_stack` to `1`:

:::{code-block}
export OMPI_MCA_mpi_abort_print_stack=1
:::

If you have a parallel debugger such as TotalView or DDT, you can use it with OpenMPI using the `mpiexec` command with the `-tv` or `-debug` options, respectively.

Finally, remember to check your slurm job output files for any error messages or abnormal output. Sometimes, the issue may be with how you are running your job rather than with your MPI program itself.

## Benchmarking OpenMPI Performance

Benchmarking is a method used to measure the performance of a system or one of its components under different conditions. For MPI, benchmarks can be used to measure its communication and computation efficiency on different high-performance computing (HPC) systems. By comparing these benchmarks, you can identify potential bottlenecks and areas for improvement to optimize the performance of MPI.

### Tools for Benchmarking

There are several tools available for benchmarking MPI, including the following:

- **[HPC Challenge (HPCC)](https://hpcchallenge.org/hpcc/software/index.html):** This benchmark suite measures a range of metrics, including latency and bandwidth, as well as floating-point computation performance.
- **[Intel MPI Benchmarks (IMB)](https://github.com/intel/mpi-benchmarks):** A suite of benchmarks provided by Intel specifically for MPI. It includes a set of MPI-1 and MPI-2 function benchmarks and measures point-to-point communication, MPI data types, collective communication, and more.
- **[OSU Micro-Benchmarks (OSU-MB)](https://ulhpc-tutorials.readthedocs.io/en/latest/parallel/mpi/OSU_MicroBenchmarks/):** A lightweight set of benchmarks designed to measure latency, bandwidth, and other performance metrics for various MPI functions.

To use these tools, you generally need to download and compile them, and then run them using a slurm job script.

## Developing with MPI

### Hello world program
The fundamental concept in MPI is the communicator, which defines a group of processes that can send messages to each other. By default, all processes belong to the `MPI_COMM_WORLD` communicator. Here is a simple C++ program that using MPI:

:::{code-block} c++
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);

    // Get the number of processes
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    // Get the rank of the process
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    printf("Hello world from processor %d out of %d processors\n", world_rank, world_size);

    MPI_Finalize();
}
:::

In this code, `MPI_Init` initializes the MPI environment, `MPI_Comm_size` gets the number of processes, `MPI_Comm_rank` gets the rank (ID) of the process, and `MPI_Finalize` ends the MPI environment. In the C/C++ language, the `#include <mpi.h>` header file needs to be added to compile MPI code.

To understand how to run an MPI program, let us write a simple program that prints a `"Hello, World!"` message from each process.

First, create a file called `hello_world.c` in your preferred text editor and add the following code:

:::{code-block} c++
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    printf("Hello, World! I am process %d out of %d\n", world_rank, world_size);
    MPI_Finalize();
    return 0;
}
:::

This program initializes the MPI environment, gets the rank of the process, gets the total number of processes, and then prints a message. Finally, it finalizes the MPI environment.

Next, compile the program using the `mpicc` command, which is a wrapper for the C compiler that includes the OpenMPI libraries:

:::{code-block} bash
mpicc hello_world.c -o hello_world
:::

Where `-o` is the output flag, naming the executable `hello_world`. If omitted (i.e., `mpicc helloworld_c` would generate a compiled executable named `a.out` by default).

Finally, create a slurm job script to run the program:

:::{code-block} bash
#!/bin/bash
#SBATCH --job-name=hello_world
#SBATCH --output=result.txt
#SBATCH --ntasks=4
#SBATCH --time=10:00
#SBATCH --mem-per-cpu=2000

module load openmpi/4.0.5
mpirun -n 4 ./hello_world
:::

Submit this script to slurm with the `sbatch` command:

:::{code-block} bash
sbatch job_script.sh
:::

You should see output in the `result.txt` file that shows `"Hello, World!"` messages from each process.

### MPI Communication: Send and Receive Operations
MPI allows processes to communicate by sending and receiving messages. These messages can contain any type of data. Here is a simple example of using `MPI_Send` and `MPI_Recv` to send a number from one process to another:

:::{code-block} c++
#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    int number;
    if (world_rank == 0) {
        number = -1;
        MPI_Send(&number, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    } else if (world_rank == 1) {
        MPI_Recv(&number, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Process 1 received number %d from process 0\n", number);
    }

    MPI_Finalize();
}
:::

### MPI Monte Carlo

A key aspect of using OpenMPI is the ability to implement parallel algorithms, which can significantly speed up computation. Here is an example of a parallel version of the Monte Carlo method for estimating the number $\pi$:

:::{code-block} c++
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv) {
    MPI_Init(NULL, NULL);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    srand(time(NULL) * world_rank); // Ensure random numbers on all processes

    int local_count = 0;
    int global_count = 0;
    int flip = 1 << 24;
    double x, y, z;

    // Calculate hits within circle locally
    for (int i = 0; i < flip; i++) {
        x = (double)rand() / (double)RAND_MAX;
        y = (double)rand() / (double)RAND_MAX;
        z = sqrt((x*x) + (y*y));
        if (z <= 1.0) {
            local_count++;
        }
    }

    // Combine all local sums into the global sum
    MPI_Reduce(&local_count, &global_count, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    // Process 0 calculates pi and prints the result
    if (world_rank == 0) {
        double pi = ((double)global_count / (double)(flip * world_rank)) * 4.0;
        printf("The estimated value of pi is %f\n", pi);
    }

    MPI_Finalize();
}
:::

In this code, each process performs its own Monte Carlo simulation and then combines its results with those from other processes using the `MPI_Reduce` function.

### Using OpenMPI with Python's mpi4py

mpi4py is a Python package that provides bindings to the MPI standard. It allows Python programs to take advantage of the distributed memory model and scale across multiple nodes of a high performance computing cluster, just like MPI.

The mpi4py package has been designed to be as close as possible to the MPI standard, providing Python developers with a familiar and straightforward interface to MPI.

In this program, `process 0` sends the number `-1` to `process 1`, which receives it and prints it.

To install mpi4py inside of a conda environment:

:::{code-block} bash
srun -n 4 --pty /bin/bash
module load anaconda3/2022.05
mkdir -p /path/to/mpi4py_env
conda create --prefix=/path/to/mpi4py_env -y
source activate /path/to/mpi4py_env
conda install -c conda-forge mpi4py
:::

In your preferred text editor, write a file `hello.py` that contains the following:

:::{code-block}
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    print('Hello from the master process')
else:
    print(f'Hello from process {rank}')
:::

This program gets the communicator for the current process, obtains the rank of the process, and then prints a message. If the rank is 0, the process is the master, otherwise, it is a worker.

You can run this program using the `mpirun` command:

:::{code-block} bash
srun -n 4 --pty /bin/bash
mpirun -np 4 python hello_world.py
:::

This will run the program on 4 processes.

Just like in MPI, mpi4py allows you to perform point-to-point communication using the `send` and `recv` methods, and collective communication using methods like `bcast` (broadcast), `gather`, and `reduce`.

Here is an example of point-to-point communication:

:::{code-block} python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 1, 'b': 2, 'c': 3}
    comm.send(data, dest=1)
else:
    data = comm.recv(source=0)
    print(f'Received data {data} at process {rank}')
:::

In this program, the master process sends a dictionary to a specific process and that process receives the dictionary.

:::{note}
Anything greater than rank 2 will make this program hang.
:::

### Writing Efficient MPI Code

Efficiency and scalability are crucial when writing MPI code. Here are some tips to follow:

- **Overlap Computation and Communication:** Whenever possible, organize your code so that computation can occur while communication is ongoing. This will reduce the waiting time for communication to complete.
- **Minimize Communication:** Communication is often the bottleneck in parallel programs. Therefore, design your algorithms to minimize the amount of data that needs to be sent between processes.
- **Use Collective Operations:** MPI provides collective operations like `MPI_Bcast` and `MPI_Reduce`. These operations are often optimized for the underlying hardware and should be used whenever possible.
- **Use Non-Blocking Operations:** MPI also provides non-blocking versions of its send and receive functions. These functions (`MPI_Isend` and `MPI_Irecv`) return immediately, allowing the program to continue executing while communication is happening in the background.

## Getting Help with MPI

For assistance with getting started with using MPI or troubleshooting using MPI libraries on Discovery, reach out to us at <rchelp@northeastern.edu> or [schedule a consultation] with one of our team members.

[Intel MPI]: https://www.intel.com/content/www/us/en/developer/tools/oneapi/mpi-library.html
[Messaging Passing Interface (MPI)]: https://www.mpi-forum.org
[MPICH]: https://www.mpich.org/
[OpenMPI]: https://www.open-mpi.org/
[schedule a consultation]: https://rc.northeastern.edu/support/consulting/
