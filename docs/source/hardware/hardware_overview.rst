.. _hardware_overview:

******************
Hardware overview
******************
The Discovery cluster provides you with access to over 24,000 CPU cores and over 200 GPUs. Discovery is connected
to the university network over 10 Gbps Ethernet (GbE) for high-speed data transfer.
Compute nodes are connected to each other with either 10 GbE or a high-performance HDR200 InfiniBand (IB) interconnect
running at 200 Gbps (with some nodes running HDR100 IB, if HDR200 IB is not supported on those nodes).

CPU nodes and their feature names
=================================
As of February 2021, all previous CPU node feature names were updated to human-friendly feature names following the
archspec microarchitecture specification (https://archspec.readthedocs.io/en/latest/index.html). **This update is only to the CPU node feature names.**
GPU node feature names remain unchanged at this time. Table 1 shows the new feature names and
their corresponding previous feature names. Note that the old feature names will be removed from use with your jobs as of March 3, 2021.
Make sure to update your scripts with the new feature names if you had used any of the old feature names previously.

**Table 1: CPU Nodes**

.. list-table::
  :widths: 30 10 5
  :header-rows: 1

  * - Previous Feature Name
    - Current Node Feature Name
    - Number of Nodes
  * - 4114CPU\@\2.20GHz
    - skylake_avx512
    - 48
  * - 6126\@\2.60GHz
    - skylake_avx512
    - 1
  * - 6130CPU\@\2.10GHz
    - skylake_avx512
    - 1
  * - 6148\@\2.40GHz
    - skylake_avx512
    - 3
  * - AMD-EPYC
    - zen2
    - 2
  * - AMD-EPYC-7302-16-Core-Processor
    - zen2
    - 1
  * - AMD-EPYC-7351-16-Core\@\2.40GHz
    - zen
    - 4
  * - AMD-EPYC-7402P-24-Core-Processor
    - zen2
    - 2
  * - AMD-EPYC-7452-32-Core-Processor
    - zen2
    - 55
  * - E5-2603v2\@\1.80GHz
    - ivybridge
    - 4
  * - E5-2650\@\2.00GHz
    - sandybridge
    - 23
  * - E5-2650v2\@\2.60GHz
    - ivybridge
    - 1
  * - E5-2650v3\@\2.30GHz
    - haswell
    - 4
  * - E5-2660v3\@\2.60GHz
    - haswell
    - 1
  * - E5-26700\@\2.60GHz
    - sandybridge
    - 4
  * - E5-2680v2\@\2.50GHz
    - haswell
    - 1
  * - E5-2680v2\@\2.80GHz
    - ivybridge
    - 93
  * - E5-2680v3\@\2.50GHz
    - haswell
    - 4
  * - E5-2680v3\@\2.80GHz
    - ivybridge
    - 1
  * - E5-2680v4\@\2.40GHz
    - broadwell
    - 526
  * - E5-2690v3\@\2.60GHz
    - haswell
    - 200
  * - E5-4640v2\@\2.20GHz
    - ivybridge
    - 1
  * - E7-4830v3\@\2.10GHz
    - haswell
    - 1
  * - E7-8867v3\@\2.50GHz
    - haswell
    - 1
  * - Gold6132\@\2.60GHz
    - skylake_avx512
    - 23
  * - Gold6140\@\2.60GHz
    - cascadelake
    - 1
  * - Gold6140CPU\@\2.30GHz
    - skylake_avx512
    - 2
  * - Platinum8160\@\2.10GHz
    - skylake_avx512
    - 2
  * - Platinum8276CPU\@\2.20GHz
    - cascadelake
    - 156
  * - XeonGold6132\@\2.60GHz
    - skylake_avx512
    - 3

If you are looking for information about GPUs, see :ref:`working_gpus`.

If you are looking for information about the partitions on Discovery, see :ref:`partition_names`.


Using the ``--constraint`` flag
================================
When using ``srun`` or ``sbatch``, you can specify specific hardware features as part of your job by using the ``--constraint=`` flag. Currently,
there are two supported options with the ``--constraint=`` flag: ``ib`` and ``micro-architecture``.
For example, if you want to only include nodes that are connected by InfiniBand (IB) with a job that needs to use multiple nodes, you can
specify ``--constraint=ib`` in your ``srun`` command or as a line in your ``sbatch`` script. Using a constraint can mean that you
will wait longer for your job to start, as the scheduler (Slurm) will need to find and allocate the appropriate hardware that you have
specified for your job. For more information about running jobs, see :ref:`using_slurm`.
