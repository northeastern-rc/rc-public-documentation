(cluster-usage)=

# Cluster Usage

When using the cluster, it is important to use the appropriate resources for different tasks.

## Login vs. Compute Node

Once you have logged into the cluster, it is important to run CPU-intensive activities on compute nodes by submitting a slurm job.

:::{seealso}
{ref}`using-sbatch` and {ref}`using-srun` for more information on creating a slurm job.
:::

Performing CPU-intensive activities on the login nodes is detrimental to the performance of for all cluster users and it will not provide the best performance for the tasks you are trying to accomplish.

Conversely, if you allocate CPU or GPU resources through a slurm job, it is important to use them or end your job, as other users may be waiting for the resources to be freed.

:::{important}
There are bots monitoring the usage of the login nodes and compute nodes that identify inappropriate resource usage, alerting both RC and the user in question via email.
:::

## Transferring Data

If you are attempting to transfer data, we have a dedicated transfer node that you should use.

:::{seealso}
{ref}`transferring-data`.
:::

(seff)=
## Job Efficiency

It's important to request only the resources that are necessary for your job at hand. Requesting more than is necessary will result with a longer queue time for both this job and for other users that are waiting for the resources to be freed. You can inform your decision about what resources you may need in the future by examining the job efficiency of historical similar jobs.

### seff

To see the job efficiency for a given job, you can run the `seff` command on your Slurm job ID:

:::{code} bash
[user@login-00 ~] seff 38391902
Job ID: 38391902
Cluster: discovery
User/Group: user/users
State: COMPLETED (exit code 0)
Cores: 1
CPU Utilized: 00:00:00
CPU Efficiency: 0.00% of 00:03:25 core-walltime
Job Wall-clock time: 00:03:25
Memory Utilized: 652.00 KB
Memory Efficiency: 0.03% of 1.95 GB
:::
::::

### historical-seff

If you have forgotten the particular Slurm job ID or if you simply want to see historical efficiency across a timeframe, you can run `historical-seff` with the optional date parameters to see the Slurm job IDs, the CPU and memory utilization, and the job's start and end times.

To run historical-seff, first start a job on a node in the short partition:

:::{code-block} bash
srun -p short --constraint=ib --pty bash
:::

Afterwards, you can then run historical-seff with the desired parameters as follows:

:::{code-block} bash
# Use default values (will check jobs for the current month)
historical-seff
# Specify a start time (with the endtime of today)
historical-seff --starttime YYYY-MM-DD
# Specify a start and end time
historical-seff --starttime YYYY-MM-DD --endtime YYYY-MM-DD
:::

The output will be the relevant information of your jobs in that timeframe:

:::{code-block} text
         JobID CPU Utilization Mem Utilization     Start Time       End Time
      47890214           80.94           78.02 2025-02-28T09:23:04 2025-02-28T10:01:24
      47890987           11.07            8.33 2025-02-28T09:30:12 2025-02-28T10:27:49
:::

:::{note}
If you request to see historical efficiencies across a wide timeframe, depending on how many jobs you have run, it may take some time to initially retrieve the values, but, upon subsequent searches, it will be faster.
:::
