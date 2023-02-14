*****************************************
Message Passing Interface (MPI) Overview
*****************************************
`Message Passing Interface (MPI) <https://www.mpi-forum.org>`_ is a standard for writing message-passing programs. MPI itself is not a
language. It defines a library interface, aimed at establishing a practical and easy-to-use standard for message passing.
There are several implementations of MPI, such as  `Open MPI <https://www.open-mpi.org/>`_ and  `MVAPICH <http://mvapich.cse.ohio-state.edu/>`_.

MPI libraries on Discovery
================================
These are the current versions of Open MPI, MVAPICH, and `MPICH <https://www.mpich.org/>`_ that are available on Discovery as modules.

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

Use the ``module show`` command to view information about the compilers you need to use with these libraries and if
they support InfiniBand (IB) or not. For example, ``module show openmpi/4.1.0-zen2-gcc10.1``.

The above examples are just for illustration purposes and may vary depending on the implementation
and system configuration. If you need assistance with using MPI libraries on Discovery, you can reach out to the
support team at `Email RC`_ or `Schedule Consultation`_ with one of our team members.

.. _Schedule Consultation: <https://rc.northeastern.edu/support/consulting/>
.. _Email RC: rchelp@northeastern.edu