(working-gpus)=
# GPUs on the HPC
:::{seealso}
[Learn more about partitions.](../hardware/partitions.md)
:::
:::{seealso}
[GPU Hardware details.](../hardware/hardware_overview.md#gpu-hardware)
:::
This page covers the {term}`Graphics Processing Unit (GPU)` resources available on the {term}`cluster`.

The `gpu` {term}`partition` is the general GPU resource for HPC users looking to use a GPU; `multigpu` is the alternative, where more than one GPU are accessible.

Anyone with a cluster account has access to the `gpu` partition. However, you must submit a [ServiceNow ticket] requesting temporary access to `multigpu` provided sufficient need and preparation.

:::{note}
**When working with shared computational resources, it is important to remember not to leave the jobs idle.**
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
  - 4/100
  - 1
  - 4
* - `multigpu`
  - **Yes**
  - 4/24
  - 8/100
  - 8
  - 8
:::
::::{important}
Consider the compatibility of the GPU, as some programs do not work on the older k40m or k80 GPUs.

Execute the following command to display the `non-Kepler` GPUs that are available:

:::
sinfo -p gpu --Format=nodes,cpus,memory,features,statecompact,nodelist,gres
:::

This indicates the state (idle or not) of gpu-types and could be helpful to find one that is `idle`. However, the command does not give real-time information of the state and should be used carefully.
::::