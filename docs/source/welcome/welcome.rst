********
Welcome
********
Use this online documentation to help get you started with using the Discovery cluster system.
This help system contains information and instructions on getting an account, connecting to the system,
loading modules, running jobs, and storing data. If you are not familiar with high performance computing,
you should take our training courses before working on the system. You can find information about the training and
services that the Research Computing team provides at our website: http://www.rc.northeastern.edu.

This is a beta version of the help system, and updates and changes will continue to be pushed to
this help system during the Fall 2019 semester.

We want your feedback! If you have any comments or suggestions, email us at rchelp@northeastern.edu
and specify Documentation Request in the subject line.

What is Discovery
=================
Discovery is a high performance computing (HPC) resource for the Northeastern University research community.
The Discovery cluster is located in the Massachusetts Green High Performance Computing Center (https://www.mghpcc.org/)
in Holyoke, MA. MGHPCC is a 90,000 square foot, 15 megawatt research computing and data center facility that
houses computing resources for five institutions:  Northeastern, BU, Harvard, MIT, and UMass.

Linux
=====
Discovery is a Linux-based cluster. You should have some knowledge of Linux before attempting to use Discovery.
The Research Computing group offers training sessions on Linux, as well as training on using Discovery and
other topics related to the high performance computing environment.
See the Research Computing website http://rc.northeastern.edu for more information on our training and services.
You can also find information on how to use Linux on sites such as Code Academy.

Hardware overview
=================
The Discovery cluster consists of a combination of the following CPUs and GPUs:

* 2.4 GHz Intel E5-2680 v4 CPUs
* 2.1 GHz Intel Xeon Platinum 8176 CPUs
* a selection of NVIDIA K80, P100, V100, and T4 GPUs

This system provides you with access to over 20,000 CPU cores and over 200 GPUs. Discovery is connected
to the university network over 10 Gbps Ethernet (GbE) for high-speed data transfer, and Discovery
provides 3 PB of available storage on a high-performance GPFS parallel filesystem.
Compute nodes are connected with either 10 GbE or a high-performance HDR100 InfiniBand (IB) interconnect
running at 100 Gbps, supporting all types and scales of computational workloads.
Full HDR IB connections (200 Gbps) are also available, if needed.

Partitions
++++++++++
The Discovery cluster is sectioned into partitions. Discovery offers several
computing partitions. The two main partitions are general and gpu.
Each partition consists of several processor architectures and different compute node count.
There are also partitions that are reserved for individual faculty members.
Two partitions, fullnode and multigpu, are accessible only after application approval
(details can be found in: https://rc.northeastern.edu/policy/).

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Nodes
     - CPUs
     - GPUs
   * - general
     - 316
     - 6828
     - 0
   * - gpu
     - 48
     - 896
     - 48
   * - test
     - 2
     - 40
     - 0
   * - interactive
     - 2
     - 40
     - 0
   * - infinband
     - 64
     - 1024
     - 0
   * - multigpu
     - 24
     - 688
     - 120
   * - fullnode
     - 408
     - 11424
     - 0


You can view all of the partitions by using the Slurm command ``sinfo``.
For more information about Slurm, see :ref:`using_slurm`.

Software overview
=================
Discovery has a number of software applications that are free for you to use.
You can find and load the currently available software on Discovery using the ``module avail`` command.
See the section Using Module for more information.
