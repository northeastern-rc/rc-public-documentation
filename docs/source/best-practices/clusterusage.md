(cluster-usage)=

# Cluster Usage

When using the cluster, it is important to use the appropriate resources for different tasks.

## Login vs. Compute Node

Once you have logged into the cluster, it is important to run CPU-intensive activities on compute nodes by submitting a slurm job.

:::{seealso}
{ref}`using-sbatch` and {ref}`using-srun` for more information on creating a slurm job.
:::

Perfoorming CPU-intensive activities on the login nodes is detrimental to the performance of for all cluster users and it will not provide the best performance for the tasks you are trying to accomplish.

Conversely, if you allocate CPU or GPU resources through a slurm job, it is important to use them or end your job, as other users may be waiting for the resources to be freed.

:::{important}
There are bots monitoring the usage of the login nodes and compute nodes that identify inappropriate resource usage, alerting both RC and the user in question.
:::

## Transferring Data

If you are attempting to transfer data, we have a dedicated transfer node that you should use.

:::{seealso}
{ref}`transferring-data`.
:::
