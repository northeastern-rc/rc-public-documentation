(slurm-monitoring-and-managing)=
# Monitoring and Managing Jobs

You can use Slurm commands to check the status of the cluster, check details on the compute nodes, and check on the running jobs you have on the cluster. 

(cluster-and-node-states)=
## Query Partitions: `sinfo`
The `sinfo` command will show information about all partitions in the cluster, including the partition name, available nodes, and status. To view information about a specific partition (e.g., `short`, `gpu`, `long`):

:::{code} bash
sinfo -p <partition_name>
:::

as an example:

:::{code} bash
sinfo -p gpu-interactive
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
gpu          up    8:00:00      5 drain* c[2171,2184,2188],d[1008,1014]
gpu          up    8:00:00      3  down* c2162,d[1006,1017]
gpu          up    8:00:00      1  drain d1025
gpu          up    8:00:00      2   resv c2177,d1029
gpu          up    8:00:00     50    mix c[2160,2163-2170,2172-2176,2178-2179,2185-2187,2189-2195,2204-2207],d[1001,1003-1005,1007,1009-1013,1016,1018,1020-1024,1026-1028]
gpu          up    8:00:00      3  alloc d[1002,1015,1019]
gpu          up    8:00:00      4   idle c[2180-2183]
:::

You can use the `--Format` flag to get more information or a specific format for the output:

:::{code} bash
sinfo -p <partition> -t idle --Format=gres,nodes
:::

For more information about sinfo, please review the [sinfo manual].

(job-management)=
## Monitoring Jobs: `squeue`
The `squeue` command allows you to monitor the state of jobs in the queue. It provides information such as the job ID, the partition it is running on, and the job name.

To monitor all jobs of a specific user, use the following command:

:::{code} bash
squeue -u <username>
:::

For more information about squeue, please review the [squeue manual].

## Canceling Jobs: `scancel`
The `scancel` command is used to cancel a running or pending job.

To cancel a specific job, use:

:::{code} bash
scancel <job_id>
:::

To cancel all jobs of a specific user:

:::{code} bash
scancel -u <username>
:::

For more information about scancel, please review the [scancel manual].

[scancel manual]: https://slurm.schedmd.com/scancel.html
[sinfo manual]: https://slurm.schedmd.com/sinfo.html
[squeue manual]: https://slurm.schedmd.com/squeue.html