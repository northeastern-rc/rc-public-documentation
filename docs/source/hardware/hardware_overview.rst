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
