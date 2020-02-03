********
Welcome
********
Use this online documentation to help get you started with using the Discovery cluster system.
This help system contains information and instructions on getting an account, connecting to the system,
loading modules, running jobs, and storing data. If you are not familiar with high performance computing,
you should take our training courses before working on the system. You can find information about the training and
services that the Research Computing team provides at our website: http://www.rc.northeastern.edu.

This is a beta version of the help system, and updates and changes will continue to be pushed to
this help system during the Spring 2020 semester.

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
The Discovery cluster provides you with access to over 20,000 CPU cores and over 200 GPUs. Discovery is connected
to the university network over 10 Gbps Ethernet (GbE) for high-speed data transfer, and Discovery
provides 3 PB of available storage on a high-performance GPFS parallel filesystem.
Compute nodes are connected with either 10 GbE or a high-performance HDR100 InfiniBand (IB) interconnect
running at 100 Gbps, supporting all types and scales of computational workloads.
Full HDR IB connections (200 Gbps) are also available, if needed.
See the table below for details on CPU types, cores per node, and number of cores.

.. list-table::
  :widths: 40 10 10 10
  :header-rows: 1

  * - CPU Type
    - Cores per Node
    - Number of Nodes
    - Total Cores
  * - E5-2680v2@2.8 GHz
    - 20
    - 76
    - 1520
  * - E5-2690v3@2.6 GHz
    - 24
    - 184
    - 4416
  * - E5-2680v4@2.4 GHz
    - 28
    - 408
    - 11424
  * - Platinum 8276@2.2 GHz
    - 56
    - 128
    - 7168

.. _partition_names:

Partitions
++++++++++

.. note::
   As of January 2020, the partition names were updated. You should refer to the table below for
   the most current partition names to use with your submission scripts.

The Discovery cluster is sectioned into partitions. Discovery has several
computing partitions for different computing needs. The partitions available for general use
are debug, express, short, and gpu.
Each partition consists of several processor architectures and different compute node counts.
There are also partitions that are reserved for individual faculty members.
Three partitions, long, large, and multigpu, are accessible only after application approval
(details and application forms can be found on the RC website: https://rc.northeastern.edu/policy/).
NOTE: In the following table, the Running Jobs and Submitted Jobs numbers are Per User/Per Research Group.

.. list-table::
   :widths: 20 20 10 20 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Requires Approval?
     - Time limit
     - Running Jobs
     - Submitted Jobs
     - Core Limit
     - RAM Limit
     - GPU per job Limit
     - GPU per user Limit
   * - debug
     - No
     - 20 minutes
     - 10/25
     - 25/100
     - 128
     - 256GB
     - N/A
     - N/A
   * - express
     - No
     - 60 minutes
     - 50/250
     - 250/100
     - 2048
     - 25TB
     - N/A
     - N/A
   * - short
     - No
     - 24 Hours
     - 50/500
     - 100/100
     - 1024
     - 25TB
     - N/A
     - N/A
   * - gpu
     - No
     - 8 Hours
     - 25/250
     - 50/100
     - N/A
     - N/A
     - 1
     - 8
   * - long
     - **Yes**
     - 5 Days
     - 25/250
     - 50/500
     - 1024
     - 25TB
     - N/A
     - N/A
   * - multigpu
     - **Yes**
     - 24 Hours
     - 25/100
     - 50/100
     - N/A
     - N/A
     - 8
     - 8
   * - large
     - **Yes**
     - 6 Hours
     - 100/100
     - 100/1000
     - N/A
     - N/A
     - N/A
     - N/A


You can view all of the partitions by using the Slurm command ``sinfo -a``. To specify a partition in
your job submission script, use the option ``--partition=<partition name>``.
For more information about Slurm, see :ref:`using_slurm`.

Software overview
=================
Discovery has a number of software applications that are available for you to load and use using a module system.
Before requesting software or installing software locally to your Path, you should always check the available
software modules on Discovery by using the ``module avail`` command. See :ref:`using_module` for more information.
