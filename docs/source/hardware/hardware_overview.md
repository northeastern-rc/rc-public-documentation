(hardware-overview)=

# Hardware Overview

The computing cluster provides access to over 1,024 {term}`CPU <Central Processing Unit (CPU)>` nodes, 50,000 CPU cores, and over 200 GPUs and is connected to the university network over 10 Gbps Ethernet (GbE) for high-speed data transfer. Compute nodes are wired with 10 GbE or a high-performance HDR200 {term}`InfiniBand (IB)` interconnect running at 200 Gbps (with some nodes running HDR100 IB if the HDR200 IB is not supported).

## CPU nodes

Table 1 below shows the feature names, number of nodes by partition type (public and private), and the RAM memory range per node. The feature name follows archspec microarchitecture [specification](https://archspec.readthedocs.io/en/latest/index.html).

:::{list-table}
---
header-rows: 1
---
* - Feature Name
  - Number of Nodes - public, private
  - RAM memory per node
* - skylake
  - 0, 170
  - 186 - 3094 GB
* - zen2
  - 40, 292
  - 256 - 2000 GB
* - zen
  - 40, 300
  - 256 - 2000 GB
* - ivybridge
  - 64, 130
  - 31 - 1031 GB
* - sandybridge
  - 8, 0
  - 384 GB
* - haswell
  - 230, 62
  - 109 - 1031 GB
* - broadwell
  - 756, 226
  - 128 - 515 GB
* - cascadelake
  - 260, 88
  - 186 - 3094 GB
:::

If you are looking for information about GPUs, see {ref}`working-gpus`.

If you are interested in more information about the different partitions on Discovery, including the number of nodes per partition, running time limits, job submission limits, and RAM limits, see {ref}`partition-names`.

## Using the `--constraint` flag

When using `srun` or `sbatch`, you can specify hardware features as part of your job by using the `--constraint=` flag. This may be particularly useful when benchmarking, optimizing, or if you are using code that was compiled on a certain micro-architecture. Currently, you can use the `--constraint=` flag to restrict your job to a specific feature name (e.g., `haswell`, `ivybridge`) or you can use the flag: `ib` to only include nodes that are connected by InfiniBand (IB) with a job that needs to use multiple nodes.

A few examples using `srun`:

:::{code-block} bash
---
linenos: true
---
     srun --constraint=haswell --pty /bin/bash
     srun --constraint=ivybridge --pty /bin/bash
     srun --constraint=ib --pty /bin/bash
     srun --constraint="[ivybridge|zen2]" --pty /bin/bash #this uses the OR operator | to select either an ivybridge or zen2 node.
:::

You can add these same flags as an additional line in your `sbatch` script via (`#SBATCH --constraint=haswell`)

:::{note}
Using the --constraint flag can mean that you will wait longer for your job to start, as the scheduler (Slurm) will need to find and allocate the appropriate hardware that you have specified for your job. For more information about running jobs, see {ref}`using-slurm`. Finally, at this time only the OR operator `|` is supported when using `--constraint`.
:::
