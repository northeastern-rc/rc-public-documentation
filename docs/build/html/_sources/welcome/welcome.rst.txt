********
Welcome
********
Welcome to the official online help system for Northeastern University's Research Computing team!
This documentation will help get you started with using Northeastern's Discovery cluster system.
This help system contains the most up-to-date information and instructions on getting an account, connecting to the system,
loading modules, running jobs, and storing data. If you are not familiar with high performance computing,
you should take our training courses before working on the system. You can find information about the training and
services that the Research Computing team provides at our website: http://www.rc.northeastern.edu.

This is help system is update frequently to reflect the latest information about Discovery, as well
as to add new topics to help you with your research. Check back often to view our updates.

We want your feedback! If you have any comments or suggestions for topics you'd like
to see covered in this documentation, submit a `documentation ServiceNow ticket <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=c58d8492dbb08090a37cd206ca9619b6>`_.

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
The Discovery cluster provides you with access to over 24,000 CPU cores and over 200 GPUs. Discovery is connected
to the university network over 10 Gbps Ethernet (GbE) for high-speed data transfer, and Discovery
provides 3 PB of available storage on a high-performance GPFS parallel filesystem.
Compute nodes are connected with either 10 GbE or a high-performance HDR100 InfiniBand (IB) interconnect
running at 100 Gbps, supporting all types and scales of computational workloads.
Full HDR IB connections (200 Gbps) are also available, if needed.
See the tables below for details on CPUs and GPUs that are available on Discovery.

.. list-table::
  :widths: 40 10 10 10 10
  :header-rows: 1

  * - CPU Type
    - Cores per Node
    - Number of Nodes
    - Total Cores
    - RAM per node
  * - E5-2680v2\@\2.8 GHz
    - 20
    - 76
    - 1520
    - 64GB
  * - E5-2690v3\@\2.6 GHz
    - 24
    - 184
    - 4416
    - 128GB
  * - E5-2680v4\@\2.4 GHz
    - 28
    - 408
    - 11424
    - 256GB
  * - Platinum 8276\@\2.2 GHz
    - 56
    - 128
    - 7168
    - 192GB

.. list-table::
  :widths: 40 40 40
  :header-rows: 1

  * - GPU Type
    - Number of nodes/GPUs
    - CPU Type
  * - k20m
    - 23 nodes with 1 GPU each
    - E5-2650\@\2.00GHz
  * - k40m
    - 16 nodes with 1 GPU each
    - E5-2690v3\@\2.60GHz
  * - k80
    - 8 nodes with 8 GPUs each
    - E5-2680v4\@\2.40GHz
  * - p100
    - 12 nodes with 4 GPUs each
    - E5-2680v4\@\2.40GHz
  * - v100
    - 4 nodes with 2 GPUs each
    - AMD EPYC 7351\@\2.60GHz
  * - v100-sxm2
    - 24 nodes with 4 GPUs each
    - Intel Gold 6132\@\2.60Ghz


.. _partition_names:

Partitions
==========
:sub:`Updated April 3, 2020`

.. note::
   As of February 2020, the partition names were updated. You should refer to the table below for
   the most current partition names to use with your submission scripts.

The Discovery cluster is sectioned into virtual partitions. The partitions available for general use
are debug, express, short, and gpu. Each partition consists of several processor architectures and different compute node counts.
There are also partitions that are reserved for individual faculty members.
Three partitions, long, large, and multigpu, are accessible only after application approval
For more information see :ref:`partition_access` and the RC website: https://rc.northeastern.edu/policy/.

.. note::
   In the following table, the Running Jobs Per User/Per Research Group. RAM limit is per user, across all jobs.

.. list-table::
   :widths: 20 20 20 20 30 20 20
   :header-rows: 1

   * - Name
     - Requires approval?
     - Time limit (default/max)
     - Running jobs
     - Submitted jobs
     - Core limit
     - RAM limit
   * - debug
     - No
     - 20 minutes/20 minutes
     - 10/25
     - 5000
     - 128
     - 256GB
   * - express
     - No
     - 30 minutes/60 minutes
     - 50/250
     - 5000
     - 2048
     - 25TB
   * - short
     - No
     - 4 hours/24 Hours
     - 50/500
     - 5000
     - 1024
     - 25TB
   * - long
     - **Yes**
     - 1 day/5 Days
     - 25/250
     - 1000 per user/5000 per group
     - 1024
     - 25TB
   * - large
     - **Yes**
     - 6 hours/6 Hours
     - 100/100
     - 1000 per user/5000 per group
     - N/A
     - N/A

.. list-table::
   :widths: 20 20 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Requires approval?
     - Time limit (default/max)
     - Running jobs
     - Submitted jobs
     - GPU per job limit
     - GPU per user limit
   * - gpu
     - No
     - 4 hours/8 Hours
     - 25/250
     - 50/100
     - 1
     - 8
   * - multigpu
     - **Yes**
     - 4 hours/24 Hours
     - 25/100
     - 50/100
     - 12
     - 12

You can view all of the partitions by using the Slurm command ``sinfo -a``. To specify a partition in
your job submission script, use the option ``--partition=<partition name>``.
For more information about Slurm, see :ref:`using_slurm`.

.. _partition_access:

Partition Access Request
==========================

If you need access to the large, long, or multigpu partition, you need to submit a `ServiceNow ticket <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7>`_.
Access is not automatically granted. You will need to provide details and test results that demonstrate your need for access for these partitions.
If you need temporary access to multigpu to perform testing before applying for permanent access,
you should also submit a `ServiceNow ticket <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7>`_. All requests are evaluated by members of the RC team,
and multigpu requests are also evaluated by two faculty members.

Software overview
=================
Discovery has a number of software applications that are available for you to load and use using a module system.
Before requesting software or installing software locally to your path, you should always check the available
software modules on Discovery by using the ``module avail`` command. See :ref:`using_module` for more information.
