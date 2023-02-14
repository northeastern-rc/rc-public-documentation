*****************************************
Message Passing Interface (MPI) Overview
*****************************************
`Message Passing Interface (MPI) <https://www.mpi-forum.org>`_ is a standard for writing message-passing programs. MPI itself is not a language. Instead, it defines a library interface to establish a practical, easy-to-use standard for message passing. There are several implementations of MPI, such as `Open MPI <https://www.open-mpi.org/>`_ and `MVAPICH <http://mvapich.cse.ohio-state.edu/>`_.

MPI libraries on Discovery
================================
The current versions of Open MPI, MVAPICH, and `MPICH <https://www.mpich.org/>`_ are available on Discovery as modules.
::
   openmpi/4.1.0-zen2-gcc10.1
   openmpi/4.1.0-amd-intel2021
   openmpi/4.0.5-skylake-gcc7.3
   openmpi/4.1.0-gcc10.1-cuda11.2
   openmpi/4.0.4-amd-intel2020u2
   openmpi/4.0.5
   openmpi/4.0.5-skylake-gcc10.1
   openmpi/4.0.3-cuda
   mpich/3.3.2-skylake-gcc7.3
   mvapich2/2.3.4-intel2020

Use the ``module show`` command to view information about the compilers you need to use with these libraries and whether they support InfiniBand (IB).

For example,
::
   module show openmpi/4.1.0-zen2-gcc10.1

Using MPI
=============

Compiling
------------

To compile an MPI program, you can use the MPI compiler wrapper ``mpicc``. The MPI compiler wrapper automatically sets the necessary compiler flags and libraries to build an MPI program.

Here is an example of how to compile an MPI program using ``mpicc``::

   mpicc -o my_mpi_program my_mpi_program.c

In this example, ``my_mpi_program.c`` is the source code file for the MPI program; ``my_mpi_program`` is the generated executable. The ``-o`` option specifies the name of the output file.

Once compiled, you can run it using ``mpirun``. The ``mpirun`` command launches MPI programs on a parallel environment.

Here is an example of how to run an MPI program using ``mpirun``::

   mpirun -np 4 ./my_mpi_program

where ``-np 4`` specifies the number of processes to launch, and ``./my_mpi_program`` is the name of the executable file.

.. note::
   ℹ️ The exact syntax and options for ``mpicc`` and ``mpirun`` may vary depending on your MPI implementation you are
   using. Therefore, we recommend consulting the documentation for your MPI implementation for more information on compiling and running MPI programs.

Examples
-----------------
Here are several examples of how to use MPI on Discovery:

Loading the MPI Library::

   module load openmpi/4.1.0-zen2-gcc10.1

Compiling an MPI Program::

   mpicc -o my_mpi_program my_mpi_program.c

Running an MPI Program::

   mpirun -np 4 ./my_mpi_program

Checking the Information about MPI Library::

   module show openmpi/4.1.0-zen2-gcc10.1

Using a Different MPI Library::

   unload openmpi/4.1.0-zen2-gcc10.1
   module load mvapich2/2.3.4-intel2020

Sample Code Snippets
--------------------
Here are a few code examples using MPI.

.. note::
   ℹ️ MPI programs often require careful design and implementation to achieve good performance and scalability.
   Good MPI programming practices include:
      - Avoiding communication and computation overlap.
      - Reducing the amount of communication.
      - Using appropriate collective communication operations.


**Broadcasting a Message**

In this example, the MPI function MPI_Comm_rank is used to determine the rank of the process, and MPI_Comm_size is used to determine the size of the communicator MPI_COMM_WORLD. The MPI_Bcast function is used to broadcast the value 42 from process rank 0 to all other processes.

.. code-block:: cpp

   int rank, size;
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);

   int message = 0;
   if (rank == 0) {
     message = 42;
   }

   MPI_Bcast(&message, 1, MPI_INT, 0, MPI_COMM_WORLD);

**Sending and Receiving Messages**

In this example, process rank 0 sends the value 42 to process rank 1 using the MPI_Send function, and process rank 1 receives the message using the MPI_Recv function.

.. code-block:: bash

   int rank, size;
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);

   int message;
   if (rank == 0) {
     message = 42;
     MPI_Send(&message, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
   } else if (rank == 1) {
     MPI_Recv(&message, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
   }


**Scattering and Gathering Data**

In this example, the MPI_Scatter function is used to distribute the data from process rank 0 to all other processes, and the MPI_Gather function is used to gather the results back to process rank 0. Each process multiplies its portion of the data by 2, and the results are gathered back to process rank 0 for further processing.

.. code-block:: bash

   int rank, size;
   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
   MPI_Comm_size(MPI_COMM_WORLD, &size);

   const int count = 6;
   int data[count];
   int result[count];
   if (rank == 0) {
     for (int i = 0; i < count; i++) {
       data[i] = i;
     }
   }

   MPI_Scatter(data, count / size, MPI_INT, result, count / size, MPI_INT, 0, MPI_COMM_WORLD);

   for (int i = 0; i < count / size; i++) {
     result[i] *= 2;
   }

   MPI_Gather(result, count / size, MPI_INT, data, count / size, MPI_INT, 0, MPI_COMM_WORLD);

These are just a few examples of what you can do with MPI. Many other MPI functions can perform various parallel operations, such as reducing data, performing parallel I/O, and synchronizing processes. With MPI, you can write parallel programs that run efficiently across numerous systems, ranging from small clusters to large supercomputers.

----------

The above examples are just for illustration purposes and may vary depending on the implementation and system configuration. If you need assistance with using MPI libraries on Discovery, you can reach out to the support team at `Email RC`_ or `Schedule Consultation`_ with one of our team members.

.. _Schedule Consultation: <https://rc.northeastern.edu/support/consulting/>
.. _Email RC: rchelp@northeastern.edu