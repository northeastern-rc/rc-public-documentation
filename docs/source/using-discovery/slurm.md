(using-slurm)=
# Using Slurm

## Brief Overview of Slurm
Slurm (Simple Linux Utility for Resource Management) is an open-source, highly configurable, fault-tolerant, and adaptable workload manager. It is extensively used across High-Performance Computing (HPC) environments.

Slurm is designed to accommodate the complex needs of large-scale computational workloads. It can efficiently distribute and manage tasks across clusters comprising thousands of nodes, offering seamless control over resources, scheduling, and job queuing.
It is the software on the HPC that lets users do tasks such as view information about the cluster, {ref}`job-submission-and-monitoring`, including {ref}`job-arrays`, {ref}`job-management`, view {ref}`account-information`, and check the {ref}`cluster-and-node-states`.

## Importance and Uses of Slurm in HPC
HPC systems are designed to perform complex, computationally intensive tasks. For example, users can specify complex workflows of jobs where specific jobs depend on others, and Slurm will manage the scheduling and execution of these workflows. Efficiently managing these tasks and resources in such an environment is a daunting challenge. That's where Slurm comes into play.

Slurm allows users to submit their computational tasks as jobs to be scheduled on the cluster's compute nodes. Its role-based access control ensures proper resource allocation and job execution, preventing resource conflicts.

Slurm is crucial in research environments, where it ensures fair usage of resources among a multitude of users, helps optimize the workload for the available resources, and provides precise job accounting and statistics.

**Page Objective:**

This tutorial aims to equip users with an understanding of the Slurm workload manager. It starts with the basics, teaching you how to install and configure Slurm, before diving into the more nuanced aspects of job submission and management. The tutorial also covers advanced usage, troubleshooting, and best practices to get the most out of your HPC environment.

**Who Should Use This Guide?**

This guide is ideal for beginners new to Slurm and HPC, researchers intending to use Slurm-based clusters for their computation tasks, system administrators managing HPC environments, and even seasoned HPC users looking to brush up on their knowledge. It progresses from fundamental to advanced topics, making it a valuable resource for a broad audience.

## Slurm: Basic Concepts
Before we delve into using Slurm, it's essential to grasp some fundamental concepts related to its operation.

### Nodes
In the context of Slurm, a 'node' refers to a server within the HPC cluster. Each node possesses its resources, such as CPUs, memory, storage, and potentially GPUs. Slurm manages these nodes and allocates resources to the tasks.

(slurm-partitions)=
### Partition(s)
A 'partition' is a grouping of nodes. You can think of partitions as virtual clusters within your HPC system. They allow administrators to segregate the compute environment based on factors like job sizes, hardware type, or resource allocation policies.

:::{seealso}
Our {ref}`partition-names` documentation.
:::

(account-information)=
### Account information
When running a job with either `srun` or `sbatch`, if you have more than one account associated with your username, we recommend you use the `--account=` flag and specify the account that corresponds to the respective project.

To find out what account(s) your username is associated with, use the following command:

:::{code} bash
sacctmgr show associations user=<yourusername>
:::

After you have determined what accounts your username is associated with, if you have more than one account association, you can use the `account=` flag with your usual `srun` or `sbatch` commands.

### Jobs, Job Steps, and Job Arrays
A **job** in Slurm is a user-defined computational task that's submitted to the cluster for execution. Each job has one or more **job steps**, sub-tasks that are part of a larger job and can be executed in parallel or sequentially.

**Job arrays** are a series of similar jobs that differ only by the array index. They're especially useful when you want to execute the same application with different inputs.

### Tasks
Tasks are the individual processes that run within a job step. They could be single-threaded or multi-threaded and can run on one or more nodes.

### Understanding the Configuration File

::::{note}
Most users should not be concerned with slurm configurations, beyond being aware of the configurations.
:::{seealso}
[Slurm documentation](https://slurm.schedmd.com/documentation.html) for a complete list of available parameters as shown in the example config file belong, along with their meanings.
:::
::::

The slurm.conf file is the primary configuration file (i.e., `slurm.conf`) for Slurm. It contains the parameters that govern the behavior of the Slurm controller, nodes, and partitions.

::::{dropdown} Example of a very basic `slurm.conf` file:

:::{code} bash
# Basic slurm.conf file
ControlMachine=slurm-controller  # Hostname of the control node
AuthType=auth/munge              # Authentication type
CryptoType=crypto/munge          # Cryptography type
MpiDefault=none                  # Default MPI type
ProctrackType=proctrack/pgid     # Process tracking type
ReturnToService=1                # Return failed nodes to service
SlurmctldPidFile=/var/run/slurmctld.pid  # PID file for the Slurm controller
SlurmctldPort=6817               # Communication port for the Slurm controller
SlurmdPidFile=/var/run/slurmd.pid        # PID file for the Slurm daemon
SlurmdPort=6818                  # Communication port for the Slurm daemon
SlurmdSpoolDir=/var/spool/slurmd # Spool directory for the Slurm daemon
SlurmUser=slurm                  # User the Slurm daemon runs as
StateSaveLocation=/var/spool/slurmctld # Where state information is saved
SwitchType=switch/none           # Job switch type
TaskPlugin=task/none             # Task plugin
#
# Node definitions
NodeName=compute[1-16] CPUs=1 State=UNKNOWN
#
# Partition definitions
PartitionName=test Nodes=compute[1-16] Default=YES MaxTime=INFINITE State=UP
:::
::::

(job-submission-and-monitoring)=
## Job Submission and Monitoring
To submit your job script to Slurm, you use the `sbatch` command:

:::{code} bash
sbatch job_script.sh
:::

Slurm will then schedule your job to run when resources are available. It returns a job ID that you can use to monitor your job's status.

To check the status of your job, you use the `squeue` command:

:::{code} bash
squeue -u *<username>*
:::

To cancel a job, you use the `scancel` command with the job ID:

:::{code} bash
scancel *<job_id>*
:::

To check detailed information about a job, use the `scontrol` command:
:::{code} bash
scontrol show job *<job_id>*
:::

This information is crucial for managing your jobs and ensuring they are running as expected.

(using-sbatch)=
## Batch Jobs: `sbatch` Command
The `sbatch` command is used to submit a job script for later execution. The script includes the `SBATCH` directives that control the job parameters like the number of nodes, CPUs per task, job name, etc.

### Syntax: `sbatch`
:::{code} bash
sbatch [options] *<script_file>*
:::

### Options and Usage: `sbatch`
- `n, --ntasks=*<number>*` : specify the number of tasks
- `N, --nodes=<minnodes[-maxnodes]>` : specify the number of nodes
- `J, --job-name=<jobname>` : specify a name for the job

### Code Example of Job Submission Script
:::{code} bash
#!/bin/bash
#SBATCH -J MyJob               # Job name
#SBATCH -N 2                   # Number of nodes
#SBATCH -n 16                  # Number of tasks
#SBATCH -o output_%j.txt       # Standard output file
#SBATCH -e error_%j.txt        # Standard error file

# Your program/command here
srun ./my_program
:::

To submit this job script, save it as `my_job.sh` and run:
:::{code} bash
sbatch my_job.sh
:::

### Examples using sbatch
**Job request: one node**
Run a job on one node for four hours on the short partition:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --partition=short

# <commands to execute>
:::

**Job request: one node with additional memory**
The default memory per allocated core is 1.95GB. If calculations attempt to access more memory than allocated, Slurm automatically terminates the job. Request a specific amount of memory in the job script if calculations require more than the default. The example script below requests 100GB of memory (`--mem=100G`). Use one capital letter to abbreviate the unit of memory (i.e., kilo `K`, mega `M`, giga `G`, and tera `T`) with the `--mem=` option, as that is what Slurm expects to see:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --mem=100G
# SBATCH --partition=short

# <commands to execute>
:::

**Job request: one node with exclusive use of a node**
If you need exclusive use of a node, such as when you have a job that has high I/O requirements, you can use the exclusive flag. The example script below specifies the exclusive use of one node in the short partition for four hours:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --exclusive
# SBATCH --partition=short

# <commands to execute>
:::

(using-srun)=
## Interactive Jobs: `srun` Command
The `srun` command is used to submit an interactive job which runs a single task directly via the shell. This method is useful when you want to test a short computation or run an interactive session like a shell, Python, or an R terminal.

### Syntax: `srun`

:::{code} bash
srun [options] [command]
:::

### Options and Usage: `srun`
- **`n, --ntasks=<number>`**: specify the number of tasks
- **`N, --nodes=<minnodes[-maxnodes]>`**: specify the number of nodes
- **`J, --job-name=<jobname>`**: specify a name for the job

### Code Example for Interactive Job Submission
:::{code} bash
srun -N 1 -n 1 --pty bash
:::

This command starts an interactive bash shell on one node with one task.

### Viewing Cluster Information
:::{code} bash
sinfo <options>
:::

This command allows to view partition and node information. Use option -a to view all partitions.

:::{code} bash
smap <options>
:::

This command allows to view details about the cluster in a visual format

### Examples using srun

The user needs to review the {ref}`hardware-overview` and {ref}`partitions` to be familiar with the available hardware and partition limits on Discovery. This way, user can tailor the request to fit both the needs of the job and the limits of partitions. For example, if the user specifies `--partition=short` and `--time=01:00:00`, it will result in an error because the time specified exceeds the limit for that partition.

This simple `srun` example is to move to a *compute* node after you first log into the HPC:

:::{code} bash
srun --pty /bin/bash
:::

To request one node and one task for 30 minutes with X11 forwarding on the short partition, type:

:::{code} bash
srun --partition=short --export=ALL --nodes=1 --ntasks=1 --x11 --mem=10G --time=00:30:00 --pty /bin/bash
:::

To request one node, with 10 tasks and 2 CPUs per task (a total of 20 CPUs), 1 GB of memory, for one hour on the express partition, type:

:::{code} bash
srun --partition=short --nodes 1 --ntasks 10 --cpus-per-task 2 --pty --export=ALL --mem=1G --time=01:00:00 /bin/bash
:::

To request two nodes, each with 10 tasks per node and 2 CPUs per task (a total of 40 CPUs), 1 GB of memory, for one hour on the express partition, type:

:::{code} bash
srun --partition=short --nodes=2 --ntasks 10 --cpus-per-task 2 --pty --export=ALL --mem=1G --time=01:00:00 /bin/bash
:::

To allocate a GPU node, you should specify the `gpu` partition and use the `–gres` option:

:::{code} bash
srun --partition=gpu --nodes=1 --ntasks=1 --export=ALL --gres=gpu:1 --mem=1Gb --time=01:00:00 --pty /bin/bash
:::

(job-arrays)=
## Job Arrays
Job arrays are a series of similar jobs. They are especially useful when you want to run the same job multiple times with minor changes, such as different input files.

In HPC environments, users often need to run large numbers of jobs that are very similar, such as simulations with varying input parameters or the processing of multiple data files. Managing and tracking individual jobs can be a cumbersome and time-consuming process. **Enter: Slurm job arrays.**

A job array is a collection of related jobs submitted to Slurm as a single entity. A unique index identifies each job in the array, which runs independently on a separate compute node. The index can specify different input files or parameters for each job, allowing for the efficient processing of many similar tasks.

There are several ways to define job arrays, such as specifying the range of indices or providing a list of indices in a file. Slurm also offers various features to manage and track job arrays, such as options to simultaneously suspend, resume, or cancel all jobs in the array.

### Syntax: Job Arrays
:::{code} bash
sbatch --array=<indexes> [options] script_file
:::

### Use-cases: Job Arrays
Job arrays can be used in situations where you have to process multiple data files using the same procedure or program. Instead of creating multiple scripts or running the same script multiple times, you can create a job array, and Slurm will handle the parallel execution for you.

### Code Example Showcasing Job Array Submission
In the following script, the `$SLURM_ARRAY_TASK_ID` variable is used to differentiate between array tasks.

:::{code} bash
#!/bin/bash
#SBATCH -J MyArrayJob           # Job name
#SBATCH -N 1                    # Number of nodes
#SBATCH -n 1                    # Number of tasks
#SBATCH -o output_%A_%a.txt     # Standard output file (%A for array job ID, %a for array index)
#SBATCH -e error_%A_%a.txt      # Standard error file

# Your program/command here
srun ./my_program input_$SLURM_ARRAY_TASK_ID
:::

To submit this job array, save it as `my_array_job.sh` and run:

:::{code} bash
sbatch --array=1-100 my_array_job.sh
:::

This command will submit 100 jobs, running `my_program` with `input_1` through `input_100`.

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

### Modifying Jobs
The `scontrol` command allows you to modify the parameters of a queued or running job. The changes take effect immediately but are not permanent and will be lost when the job completes.

You can monitor your jobs by using the Slurm `scontrol` command. Type `scontrol show jobid -d <JOBID>`, where `JOBID` is the number of your job. In the figure at the top of the page, you can see that when you submit your `srun` command, Slurm displays the unique ID number of your job (`job 12962519`). This is the number you use with `scontrol` to monitor your job.

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

#### Code Example of Modifying Running Jobs
To hold a job:

:::{code} bash
scontrol hold jobid=<job_id>
:::

To release a job:

:::{code} bash
scontrol release jobid=<job_id>
:::

To requeue a job:

:::{code} bash
scontrol requeue jobid=<job_id>
:::

### Cancelling Jobs
The `scancel` command is used to cancel a running or pending job. Once cancelled, a job cannot be resumed.
#### Syntax: `scancel`
:::{code} bash
scancel [options] [job_id]
:::

#### Options and Usage: `scancel`
- **`u, --user=<user_name>`**: cancel all jobs of a specific user
- **`-name=<job_name>`**: cancel all jobs with a specific name

#### Code Example of Cancelling Jobs
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

The job management section aims to give you a solid understanding of how to manage and control your jobs effectively. Always ensure to monitor your jobs regularly and adjust parameters as needed to achieve the best performance.

(cluster-and-node-states)=
## Cluster and Node States
Below are some more examples of using `sinfo` and `scontrol` to provide information about the state of the cluster and specific nodes.

### Using `sinfo`
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
The current `TimeLimit` for the queues:
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
View what nodes are in what state in a partition using `statecompact`:
sinfo -p <partition> --Format=time,nodes,statecompact,features,memory,cpus,nodelist
:::

### Using `scontrol`
The `scontrol` command is a command-line utility that allows users to view and control Slurm jobs and job-related resources. It provides a way to check the status of jobs, modify job properties, and perform other job-related tasks.

Some of the tasks that can done using `scontrol` include:

Viewing job status and properties: `scontrol` can display detailed information about a job, including its status, node allocation, and other properties.

Modifying job properties: `scontrol` allows users to modify job properties such as the job name, the number of nodes, the time limit, and other parameters.

Managing job dependencies: `scontrol` provides a way to specify job dependencies and view the dependencies between jobs.

Suspending and resuming jobs: `scontrol` can stop and resume running jobs, allowing users to temporarily halt jobs or continue them as needed.

Canceling jobs: `scontrol` can cancel jobs that are running or queued, allowing users to stop jobs that are no longer needed.

Overall, `scontrol` is a powerful tool for managing Slurm jobs and job-related resources. Its command-line interface allows users to perform a wide range of tasks, from checking the status of jobs to modifying job properties and managing dependencies.

### Controlling jobs
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

## Advanced Usage
Advanced usage of Slurm involves working with multi-node jobs, GPU jobs, and understanding priority and Quality of Service (QoS) parameters. It also involves memory management and the use of environment variables in job scripts.

### Multi-node Jobs
Multi-node jobs involve executing a single job across multiple nodes. Such jobs are typically used for computationally intensive tasks that require significant parallelization.

#### Use-cases: Multi-node Jobs
Multi-node jobs are used in scenarios where tasks can be broken down into sub-tasks that can be executed in parallel, such as simulation and modeling, machine learning training, or big data analysis.

#### Code Example for Multi-node Job Submission
:::{code} bash
#!/bin/bash
#SBATCH -J MultiNodeJob     # Job name
#SBATCH -N 4                # Number of nodes
#SBATCH -n 16               # Number of tasks

# Your program/command here
srun ./my_program
:::

### GPU Jobs
Slurm can also manage GPU resources, allowing you to specify GPU requirements in your job scripts.

#### Use-cases: GPUs
GPU jobs are used in scenarios where tasks are parallelized and can benefit from the high computational capabilities of GPUs, such as machine learning and deep learning workloads, image processing, or simulations.

#### Code Example for GPU Job Submission
:::{code} bash
#!/bin/bash
#SBATCH -J GPUJob            # Job name
#SBATCH -N 1                 # Number of nodes
#SBATCH -n 1                 # Number of tasks
#SBATCH --gres=gpu:2         # Number of GPUs

# Your program/command here
srun ./my_gpu_program
:::

### Priority and QoS
Slurm uses priority and Quality of Service (QoS) parameters to determine the order in which jobs are scheduled.

#### Understanding Job Priorities and Quality of Service (QoS) Parameters
The job priority is a numerical value assigned to each job, determining its position in the queue. Higher priority jobs are scheduled before lower priority ones.
Quality of Service (QoS) parameters control various job limits, such as the maximum allowed job runtime, the maximum number of CPUs or nodes a job can use, etc.

#### Code Example to Manipulate Job Priority
:::{code} bash
scontrol update jobid=<job_id> priority=<new_priority>
:::

### Memory Management
In Slurm, memory allocation can be controlled on the job or task level using the `--mem` or `--mem-per-cpu` options, respectively.

#### Code example for specifying memory in job scripts
:::{code} bash
#!/bin/bash
#SBATCH -J MyJob             # Job name
#SBATCH -N 1                 # Number of nodes
#SBATCH -n 4                 # Number of tasks
#SBATCH --mem=8G             # Memory for the entire job
#SBATCH --mem-per-cpu=2G     # Memory per task (CPU)

# Your program/command here
srun ./my_program
:::

### Using Environment Variables in Job Scripts
Slurm sets several environment variables that you can use in your job scripts to control the job behavior dynamically. Some of these include `SLURM_JOB_ID`, `SLURM_JOB_NUM_NODES`, `SLURM_JOB_NODELIST`, etc.

#### Code Example Showcasing Use of Environment Variables

:::{code} bash
#!/bin/bash
#SBATCH -J MyJob             # Job name
#SBATCH -N 2                 # Number of nodes
#SBATCH -n 8                 # Number of tasks

echo "Job ID: $SLURM_JOB_ID"
echo "Number of nodes: $SLURM_JOB_NUM_NODES"
echo "Node list: $SLURM_JOB_NODELIST"

# Your program/command here
srun ./my_program
:::

## Common Problems and Troubleshooting
Despite its flexibility and robustness, it's not uncommon to encounter issues when using Slurm. Here we'll explore some common problems and provide strategies for debugging and optimizing job scripts.
### Commonly Encountered Issues in Using Slurm
1. **Job Stuck in Queue:** If your job is stuck in the queue and not getting scheduled, it may be due to insufficient resources, low priority, or system limits set by the Quality of Service (QoS) parameters.

    *Solution:* Check the job requirements, priority, and QoS parameters using `scontrol show job <job_id>` . Ensure your job requirements do not exceed available resources and system limits.

2. **Job Failed with Non-zero Exit Code:** If your job script or the program it's running exits with a non-zero code, it indicates an error.

    *Solution:* Check the job's output and error files for any error messages. They can provide valuable clues about what went wrong.

3. **Insufficient Memory:** If your job fails with "Out Of Memory" (OOM) errors, it means it's using more memory than allocated.

    *Solution:* Increase the `--mem` or `--mem-per-cpu` value in your job script. Remember that requesting more memory might increase the time your job spends in the queue.

### Strategies for Debugging and Optimizing Job Scripts
1. **Testing Job Scripts Interactively:** Use the `srun` command to run your job script interactively for debugging purposes. This approach allows you to observe the program's behavior in real-time.

srun --pty bash -i

2. **Using echo Command for Debugging:** Use the `echo` command in your job script to print the values of variables, command outputs, etc., to the output file. This method can help you understand the script's flow and pinpoint any issues.

echo "Value of variable x is $x"

3. **Optimizing Job Resources:** Monitor your job's resource usage using `sstat <job_id>` and adjust the resource requirements accordingly in your job script. Requesting more resources than needed can result in your job spending more time in the queue, while requesting less than needed can lead to job failures.
Remember, troubleshooting requires patience and a systematic approach. Begin by identifying the problem, then hypothesize potential causes, test those hypotheses, and apply solutions. Make small changes one at a time and retest after each change. With experience, you will be able to troubleshoot effectively and make the most of your HPC resources.

## Best Practices
In this section, we will discuss some best practices that can help you make efficient use of resources, write optimized job scripts, and ensure maximum throughput and minimal queue time in a Slurm-based HPC environment.

### Efficient Usage of Resources
1. **Request Only What You Need:** When submitting a job, request only the resources that you need. Overestimating your requirements can result in longer queue times as Slurm waits for the requested resources to become available.
1. **Use Job Arrays for Similar Jobs:** If you need to run multiple similar jobs, consider using job arrays. This approach makes job management more straightforward and reduces overhead.
1. **Use Appropriate Partitions:** Select the appropriate partition for your job based on your requirements. Each partition may have different limits and priorities, so choose the one that suits your needs best.

## Writing Optimized Job Scripts
1. **Use Environment Variables:** Slurm provides several environment variables that can be used to customize job behavior dynamically. Use these variables to make your scripts more flexible and efficient.
1. **Specify All Necessary Options:** Ensure to specify all necessary SBATCH options in your job script. Missing options can lead to unpredictable job behavior or performance.
1. **Check Exit Codes:** Always check the exit codes of commands in your job script. Non-zero exit codes usually indicate an error, and failing to check these can lead to undetected job failures.

:::{code} bash
command
if [ $? -ne 0 ]; then
  echo "Command failed"
  exit 1
fi
:::

### Guidelines to Ensure Maximum Throughput and Minimal Queue Time
1. **Monitor Job Performance:** Regularly monitor your jobs' performance using `sstat` and adjust resource requests as needed. This can help improve job scheduling efficiency.
1. **Use the `time` Option Judiciously:** While it's crucial to give your job enough time to complete, overestimating can lead to longer queue times. Start with a reasonable estimate and adjust based on actual run times.
1. **Prioritize Critical Jobs:** If you have a critical job that needs to be run immediately, you can temporarily increase its priority using `scontrol`. However, use this feature sparingly to maintain fairness.

Remember, these best practices aim to ensure efficient and fair usage of shared HPC resources. Always be mindful of other users and try to use the resources in a way that maximizes productivity for everyone.


### Proper resource request syntax
:::{code} bash
#!/bin/bash
#SBATCH --job-name=my_job       # Job name
#SBATCH --ntasks=4              # Number of tasks
#SBATCH --cpus-per-task=2       # Number of CPUs per task
#SBATCH --mem-per-cpu=4G        # Memory per CPU
#SBATCH --time=02:00:00         # Time limit
#SBATCH --partition=my_partition # Partition (queue) to use
:::

Use environment modules: Load the necessary modules before running your job. In this example, we load the Python and TensorFlow modules:

:::{code} bash
module load python/3.8
module load tensorflow/2.5.0
:::

For further reading and resources, consider the following:
- [Slurm Quick Start User Guide]
- [Slurm Workload Manager Documentation]
- [High Performance Computing For Dummies, IBM Limited Edition]
If you need further support, please contact your system administrator or visit the [Slurm community page] for mailing lists and support forums.

(slurm-appendix)=
## Appendix
### RC-Slurm Related Repos
**To do.**

### Glossary of Slurm Terms
1. **Node:** A computer or server in the HPC cluster.
1. **Partition:** A group of nodes with specific attributes and limits.
1. **Job:** A user-submitted work request.
1. **Task:** A unit of work within a job.

### Full List of Slurm Commands and Their Options
- [Slurm Commands]
- [Slurm Options]

### Sample Job Scripts for Various Use-cases
- [Sample Job Scripts]

### Slurm FAQs
- [Frequently Asked Questions].

## Slurm References
1. SchedMD. (2023). Slurm Workload Manager. [https://slurm.schedmd.com](https://slurm.schedmd.com/)
2. SchedMD. (2023). Slurm Quick Start User Guide. [https://slurm.schedmd.com/quickstart.html](https://slurm.schedmd.com/quickstart.html)
3. IBM. (2023). High Performance Computing For Dummies, IBM Limited Edition. [https://www.ibm.com/downloads/cas/WQDZWBYJ](https://www.ibm.com/downloads/cas/WQDZWBYJ)
Thank you for following along with this guide, and we wish you success in your HPC journey!

[Frequently Asked Questions]: https://slurm.schedmd.com/faq.html
[Sample Job Scripts]: https://github.com/SchedMD/slurm/tree/master/contribs
[Slurm Commands]: https://slurm.schedmd.com/quickstart_admin.html
[Slurm community page]: https://slurm.schedmd.com/community.html
[Slurm Options]: https://slurm.schedmd.com/sbatch.html
[Slurm Quick Start User Guide]: https://slurm.schedmd.com/quickstart.html
[Slurm Workload Manager Documentation]: https://slurm.schedmd.com/documentation.html
[High Performance Computing For Dummies, IBM Limited Edition]: https://www.ibm.com/downloads/cas/WQDZWBYJ
