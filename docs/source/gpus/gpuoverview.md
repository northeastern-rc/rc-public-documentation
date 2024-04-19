(working-gpus)=

# GPUs on the HPC
:::{seealso}
[Learn more about partitions.](../hardware/partitions.md)
:::
This page covers the {term}`Graphics Processing Unit (GPU)` resources available on the {term}`cluster`.

:::{list-table} The NVIDIA GPUs available on gpu-equipped partitions.
--------------
header-rows: 1
align: center
widths: auto
--------------

* - GPU Type
  - GPU Architecture
  - Memory (GB)
  - Tensor Cores
  - CUDA Cores
  - Public Nodes (*x* # GPUs)
  - Private Nodes (*x* # GPUs)
* - [P100]
  - [Pascal]
  - 12
  - N/A
  - 3,584
  - 12(*x*3-4)
  - 3(*x*4)
* - [V100 PCle](https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet-letter-fnl-web.pdf)
  - [Volta]
  - 32
  - 640
  - 5,120
  - 4(*x*2)
  - 1(*x*2), 16GB
* - [V100 SXM2](https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet-letter-fnl-web.pdf)
  - [Volta]
  - 32
  - 640
  - 5,120
  - 24(*x*4)
  - 10(*x*4), 16GB<br>8(*x*4), 32GB
* - [T4]
  - [Turing]
  - 15
  - 320
  - 2,560
  - 2(*x*3-4)
  - 1(*x*4)
* - [A100]
  - [Ampere]
  - 41 & 82
  - 432
  - 6,912
  - 3(*x*4)
  - 15(*x*2-8)
* - [Quadro RTX 8000](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/quadro-rtx-8000-us-nvidia-946977-r1-web.pdf)
  - [Turing]
  - 46
  - 576
  - 4,608
  - 0
  - 2(*x*3)
* -  [A30]
  - [Ampere]
  - 24
  - 224
  - 3,804
  - 0
  - 1(*x*3)
* - [RTX A5000]
  - [Ampere]
  - 24
  - 256
  - 8,192
  - 0
  - 6(*x*8)
* - [RTX A6000]
  - [Ampere]
  - 49
  - 336
  - 10,752
  - 0
  - 3(*x*8)
:::

The `gpu` {term}`partition` is the general GPU resource for HPC users looking to use a GPU; `multigpu` is the alternative, where more than one GPU are accessible.

Anyone with a cluster account has access to the `gpu` partition. However, you must submit a [ServiceNow ticket] requesting temporary access to `multigpu` provided sufficient need and preparation.

:::{note}
The `multigpu` partition is available for a limited time window to fulfill urgent needs. In addition, only instances that require `multigpu` will be granted access to this partition. As the partition is only accessible for a limited time (e.g., 48 hours), it is advisable to use it at full capacity. A member of the RC team will review your request to ensure that there is a genuine need for the partition. **Please note that all user limits are subject to the availability of the `multigpu` resources at the time and will be allocated based on user needs.**
:::

:::{list-table}
--------------
header-rows: 1
align: center
widths: auto
--------------

* - Name
  - Requires Approval?
  - Time in Hours (Default/Max)
  - Submitted Jobs
  - GPU per Job Limit
  - User Limit (No. GPUs)
* - `gpu`
  - No
  - 4/8
  - 50/100
  - 1
  - 8
* - `multigpu`
  - **Yes**
  - 4/24
  - 50/100
  - 12
  - 12
:::
::::{important}
Consider the compatibility of the GPU, as some programs do not work on the older k40m or k80 GPUs.

Execute the following command to display the `non-Kepler` GPUs that are available:

:::
sinfo -p gpu --Format=nodes,cpus,memory,features,statecompact,nodelist,gres
:::

This indicates the state (idle or not) of gpu-types and could be helpful to find one that is `idle`. However, the command does not give real-time information of the state and should be used carefully.
::::