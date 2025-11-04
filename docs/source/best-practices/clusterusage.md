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
There are bots monitoring the usage of the login nodes and compute nodes that identify inappropriate resource usage, alerting both RC and the user in question via email. (See {ref}`idle-bot`)
:::

## Transferring Data

If you are attempting to transfer data, we have a dedicated transfer node that you should use.

:::{seealso}
{ref}`transferring-data`.
:::

(job_eff)=

## Job Efficiency

It's important to request only the resources that are necessary for your job at hand. Requesting more than is necessary will result with a longer queue time for both this job and for other users that are waiting for the resources to be freed. You can inform your decision about what resources you may need in the future by examining the job efficiency of historical similar jobs.

Additionally, if you have used a gpu on one of our public partitions within the past week, by using our `gpu-logs` command you can gain insight into the effectiveness of your gpu workflow, seeing the efficiency of the gpu(s) broken down by timestep for your job.

(seff)=

### seff

To see the job efficiency for a given job, you can run the `seff` command on your Slurm job ID:

:::{code} bash
[user@explorer-01 ~] seff 38391902
Job ID: 38391902
Cluster: explorer
User/Group: user/users
State: COMPLETED (exit code 0)
CPU Utilized: 00:00:00
CPU Efficiency: 0.00% of 00:03:25 core-walltime
Job Wall-clock time: 00:03:25
Memory Utilized: 652.00 KB
Memory Efficiency: 0.03% of 1.95 GB
:::

(historical_seff)=

### historical-seff

If you have forgotten the particular Slurm job ID or if you simply want to see historical efficiency across a timeframe, you can run `historical-seff` with the optional date parameters to see the Slurm job IDs, the CPU and memory utilization, the GPU and GPU memory utilization (if applicable), and the job's start and end times.

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
        JobID CPU Utilization Mem Utilization Avg GPU % Avg GPU Mem %     Start Time       End Time          Partition
       3290271           40.13           27.92     32.04         87.32 2025-10-15T12:12:33 2025-10-15T13:10:05    gpu-interactive
       3174104            0.39           13.24       N/A           N/A 2025-10-16T13:32:17 2025-10-16T13:35:40              short
:::

:::{note}

If you request to see historical efficiencies across a wide timeframe, depending on how many jobs you have run, it may take some time to initially retrieve the values, but, upon subsequent searches, it will be faster.

:::

(gpu_logs)=

### gpu-logs

If you would like to examine how effectively you used a GPU or GPUs on a public node on a job within the past 7 days, you can run `gpu-logs` followed by your job-id, which will break down your GPU and GPU memory utilization by time-steps where metrics were recorded every 5 minutes.

To run gpu-logs, first start a job on a node in the short partition:

:::{code-block} bash

srun -p short --constraint=ib --pty bash

:::

Afterwards, you can then run gpu-logs on your desired job, producing the following output:

:::{code-block} text

$ gpu-logs <job-id>
                       GPU Info
                        GPU #6
            Time|    Memory|   GPU Utility|  Activity
=====================================================
2025-10-24T23:21|   30.14 %|         100 %|    active
2025-10-24T23:22|   30.14 %|         100 %|    active
2025-10-24T23:23|   30.14 %|         100 %|    active
2025-10-24T23:24|   30.14 %|         100 %|    active
2025-10-24T23:25|   30.14 %|         100 %|    active
2025-10-24T23:27|   30.14 %|         100 %|    active
2025-10-24T23:30|   30.14 %|         100 %|    active
2025-10-24T23:32|   30.14 %|         100 %|    active
2025-10-24T23:34|   30.14 %|         100 %|    active
:::
