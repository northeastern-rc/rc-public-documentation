(slurm-monitoring-and-managing)=
# Monitoring and Managing Jobs

The monitoring and management section aims to give you a solid understanding of how to manage and control your jobs effectively. Always ensure to monitor your jobs regularly and adjust parameters as needed to achieve the best performance.

(cluster-and-node-states)=
## Cluster and Node States: `sinfo`
Below are some more examples of using `sinfo` and `scontrol` to provide information about the state of the cluster and specific nodes.

## Using `sinfo`
The `sinfo` command will show information about all partitions in the cluster, including the partition name, available nodes, and status. By default, `sinfo` reports:

:::{code} bash
| PARTITION | The list of the cluster’s partitions; a set of compute nodes grouped logically |
| --- | --- |
| AVAIL | The active state of the partition (up, down, idle) |
| TIMELIMIT | The maximum job execution wall-time per partition |
| NODES | The total number of nodes per partition |
| STATE | See STATE table below |
| NODELIST(REASON) | The list of nodes per partition |
:::

### Examples using `sinfo`
View information about all partitions:

:::{code} bash
sinfo -a
:::

Or, a specific partition, which gives all the nodes and the states the nodes are in at the current time:

:::{code} bash
sinfo -p gpu
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
gpu          up    8:00:00      5 drain* c[2171,2184,2188],d[1008,1014]
gpu          up    8:00:00      3  down* c2162,d[1006,1017]
gpu          up    8:00:00      1  drain d1025
gpu          up    8:00:00      2   resv c2177,d1029
gpu          up    8:00:00     50    mix c[2160,2163-2170,2172-2176,2178-2179,2185-2187,2189-2195,2204-2207],d[1001,1003-1005,1007,1009-1013,1016,1018,1020-1024,1026-1028]
gpu          up    8:00:00      3  alloc d[1002,1015,1019]
gpu          up    8:00:00      4   idle c[2180-2183]
:::

The current `TimeLimit` for the queues:

:::{code} bash
sinfo  -o "%12P %.10A %.11l"
PARTITION    NODES(A/I)   TIMELIMIT
debug           402/174       20:00
express         403/180     1:00:00
short*          401/178  1-00:00:00
long             224/47  5-00:00:00
large           376/172     6:00:00
gpu               41/17     8:00:00
multigpu          41/17  1-00:00:00
lowpriority     118/102  1-00:00:00
reservation     617/402 100-00:00:0
ai-jumpstart       2/15  2-00:00:00
allshouse           5/7    infinite
bansil             15/4 30-00:00:00
ce-mri             3/10 30-00:00:00
chen               0/12 30-00:00:00
ctbp               0/20 30-00:00:00
.
.
.
:::

View information about a specific partition (e.g., `short`, `gpu`, `long`):

:::{code} bash
sinfo -p <partition_name>
:::

Or, only view nodes in a certain state:

:::{code} bash
sinfo -p <partition> -t <state>
:::

You can use the `--Format` flag to get more information or a specific format for the output:

:::{code} bash
sinfo -p <partition> -t idle --Format=gres,nodes
:::

Below command will show detailed information about all nodes in the cluster, including the node name, state, CPU architecture, memory, and available features:

:::{code} bash
sinfo -N -l
:::

View what features a node has:

:::{code} bash
sinfo -n <node> --Format=nodes,nodelist,statecompact,features
:::

View what nodes are in what state in a partition using `statecompact`:

:::{code} bash
sinfo -p <partition> --Format=time,nodes,statecompact,features,memory,cpus,nodelist
:::

The `scontrol` command is a command-line utility that allows users to view and control Slurm jobs and job-related resources. It provides a way to check the status of jobs, modify job properties, and perform other job-related tasks.

You can monitor your jobs by using the Slurm `scontrol` command. Type `scontrol show jobid -d <JOBID>`, where `JOBID` is the number of your job. In the figure at the top of the page, you can see that when you submit your `srun` command, Slurm displays the unique ID number of your job (`job 12962519`). This is the number you use with `scontrol` to monitor your job.


## Using `scontrol`
Some of the tasks that can done using `scontrol` include:
- **Viewing job status and properties:** `scontrol` can display detailed information about a job, including its status, node allocation, and other properties.
- **Modifying job properties:** `scontrol` allows users to modify job properties such as the job name, the number of nodes, the time limit, and other parameters.
- **Managing job dependencies:** `scontrol` provides a way to specify job dependencies and view the dependencies between jobs.
- **Suspending and resuming jobs:** `scontrol` can stop and resume running jobs, allowing users to temporarily halt jobs or continue them as needed.
- **Canceling jobs:** `scontrol` can cancel jobs that are running or queued, allowing users to stop jobs that are no longer needed.

Overall, `scontrol` is a powerful tool for managing Slurm jobs and job-related resources. Its command-line interface allows users to perform a wide range of tasks, from checking the status of jobs to modifying job properties and managing dependencies.

### Controlling jobs: `scontrol`
Place a hold on a pending job, i.e., prevent specified job from starting. <job_list> is either a space separate list of job IDs or job names.

:::{code} bash
scontrol hold <jobid>
:::

Release a held job, i.e., permit specified job to start (see hold).

:::{code} bash
scontrol release <jobid>
:::

Re-queue a completed, failed, or cancelled job

:::{code} bash
scontrol requeue <jobid>
:::

For more information on the commands listed above, along with a complete list of `scontrol` commands run below:

:::{code} bash
scontrol --help
:::

#### Syntax: `scontrol`
:::{code} bash
scontrol [command] [options]
:::

#### Example: `scontrol`
:::{code} bash
scontrol show jobid -d <JOBID>
:::

#### Options and Usage: `scontrol`
- **`update`**: used to modify job or system configuration
- **`hold jobid=<job_id>`**: hold a specific job
- **`release jobid=<job_id>`**: release a specific job
- **`requeue jobid=<job_id>`**: requeue a specific job

### Examples using `scontrol`
View information about a specific node:

:::{code} bash
scontrol show node -d <node_name>
:::

For information on all reservations, this command will show information about a specific node in the cluster, including the node name, state, number of CPUs, and amount of memory:

:::{code} bash
scontrol show reservations
:::

View information about a specific job. This command will show information about a specific job, including the job ID, state, username, and partition name:

:::{code} bash
scontrol show job <job_id>
:::

To view information about a specific reservation (e.g., found via `scontrol show res` listed above), and print information about a specific reservation in the cluster, including the reservation name, start time, end time, and nodes included in the reservation:

:::{code} bash
scontrol show reservation <reservation_name>
:::

(job-management)=
## Job Management
Managing jobs in a Slurm-based HPC environment involves monitoring running jobs, modifying job parameters, and canceling jobs when necessary. This section will cover the commands and techniques you can use for these tasks.

### Monitoring Jobs
The `squeue` command allows you to monitor the state of jobs in the queue. It provides information such as the job ID, the partition it's running on, the job name, and more.

#### Syntax: `squeue`

:::{code} bash
squeue [options]
:::

#### Options and Usage
- **`j, --jobs=<job_id>`**: display information about specific job(s)
- **`u, --user=<user_name>`**: display jobs for a specific user
- **`l, --long`**: display more information (long format)

#### Code Example of Job Monitoring
To monitor all jobs of a specific user, use the following command:

:::{code} bash
squeue -u <username>
:::

To monitor a specific job, use:

:::{code} bash
squeue -j <job_id>
:::

### Cancelling Jobs: `scancel`
The `scancel` command is used to cancel a running or pending job. Once cancelled, a job cannot be resumed.

#### Syntax: `scancel`
:::{code} bash
scancel [options] [job_id]
:::

#### Options and Usage: `scancel`
- **`u, --user=<user_name>`**: cancel all jobs of a specific user
- **`-name=<job_name>`**: cancel all jobs with a specific name

#### Examples using `scancel`
To cancel a specific job, use:

:::{code} bash
scancel <job_id>
:::

To cancel all jobs of a specific user:

:::{code} bash
scancel -u <username>
:::

To cancel all jobs with a specific name:

:::{code} bash
scancel --name=<job_name>
:::