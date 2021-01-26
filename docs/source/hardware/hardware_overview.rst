.. _hardware_overview:

******************
Hardware overview
******************
The Discovery cluster provides you with access to over 24,000 CPU cores and over 200 GPUs. Discovery is connected
to the university network over 10 Gbps Ethernet (GbE) for high-speed data transfer, and Discovery
provides 3 PB of available storage on a high-performance GPFS parallel filesystem.
Compute nodes are connected with either 10 GbE or a high-performance HDR100 InfiniBand (IB) interconnect
running at 100 Gbps, supporting all types and scales of computational workloads.
Full HDR IB connections (200 Gbps) are also available, if needed.
See the tables below for details on CPUs and GPUs that are available on Discovery. See :ref:`partition_names` for more information about the partitions on Discovery.

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
  :widths: 40 40 40 40
  :header-rows: 1

  * - GPU Type
    - Number of nodes/GPUs
    - CPU Type
    - RAM per node
  * - k20m
    - 23 nodes with 1 GPU each
    - E5-2650\@\2.00GHz
    - 128GB
  * - k40m
    - 16 nodes with 1 GPU each
    - E5-2690v3\@\2.60GHz
    - 128GB
  * - k80
    - 8 nodes with 8 GPUs each
    - E5-2680v4\@\2.40GHz
    - 512GB
  * - p100
    - 12 nodes with 4 GPUs each
    - E5-2680v4\@\2.40GHz
    - 512GB
  * - v100-pcie
    - 4 nodes with 2 GPUs each
    - AMD EPYC 7351\@\2.60GHz
    - 480GB
  * - v100-sxm2
    - 24 nodes with 4 GPUs each
    - Intel Gold 6132\@\2.60Ghz
    - 187GB

See :ref:`working_gpus` for more information on using GPUs with your jobs.

Using the ``--constraint`` flag
================================
When using ``srun`` or ``sbatch``, you can specify specific hardware features as part of your job by using the ``--constraint=`` flag.
For example, if you want to only include nodes that are connected by InfiniBand (IB) with a job that needs to use multiple nodes, you can
specify ``--constraint=ib`` in your ``srun`` command or as a line in your ``sbatch`` script. Using a constraint can mean that you
will wait longer for your job to start, as the scheduler (Slurm) will need to find and allocate the appropriate hardware that you have
specified for your job. For more information about running jobs, see :ref:`using_slurm`.

Updated node feature names (February 2021)
+++++++++++++++++++++++++++++++++++++++++++
As of February 2021, all previous node feature names will be updated to human-friendly feature names following the
archspec microarchitecture specification (https://archspec.readthedocs.io/en/latest/index.html). The following table shows the new feature names and
their corresponding previous feature names. Note that the previous feature names will be removed from use with your jobs as of February 2021.
You should update your scripts accordingly in order to continue to use these features with your scripts.

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
