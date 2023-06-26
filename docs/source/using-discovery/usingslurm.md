(using-slurm)=
# Using Slurm

Slurm (Simple Linux Utility Resource Management) is the software on Discovery
that lets you do the following:

* View information about the cluster
* Submit jobs on Discovery, including Job arrays
* Monitor jobs
* View account information
* Check the cluster state, along with that of specific nodes
* Gain knowledge of various best practices when using Slurm


{ref}`using-srun` and {ref}`using-sbatch` provide you with a few examples to help get you familiar with Slurm and be able to submit basic jobs on Discovery.

:::{important}
Slurm commands have numerous options to help your jobs run efficiently by requesting specific resources. Options also usually have both short and verbose versions, such as
`--nodes` and `-n` (both mean the same thing). The examples in this documentation all use the verbose version of the options for clarity, but you can use the short version if you prefer. For example, `srun -p short -N 1 -n 1` means the exact same thing as `srun --partition=short --nodes=1 --ntasks=1` Refer to the official Slurm documentation to get in-depth information about these commands and their options: [Slurm documentation website](https://slurm.schedmd.com/archive/slurm-17.11.6/srun.html).
:::

## Slurm on Discovery
Slurm is the software on Discovery; to be most effective, a basic understanding of Slurm is essential. Slurm provides features to support the efficient management of high-performance computing (HPC) resources, including job submission, scheduling, prioritization, and accounting. For example, Slurm allows users to submit jobs and request resources and manages the allocation and distribution of resources across the cluster. Slurm can also handle job dependencies, allowing users to define dependencies between jobs and specify when specific jobs should start.

One of the key features of Slurm is its ability to support heterogeneous clusters, where different compute nodes have varying hardware specifications. Slurm can manage resources on various hardware and software configurations. It provides a way to specify the job requirements to ensure scheduling with the appropriate nodes.

Another critical feature of Slurm is its ability to handle complex workflows and dependencies. For example, users can specify complex workflows of jobs where specific jobs depend on others, and Slurm will manage the scheduling and execution of these workflows.

Overall, Slurm is a powerful and versatile tool for managing HPC resources. Its flexibility, scalability, and reliability make it an essential tool for many HPC environments. By following the contents of this page, the user will be able to use Slurm to:



Hence, Slurm is a job scheduler and batch manager. Here are the main Slurm commands:

.. list-table:: Common Slurm commands exemplified throughout this page.
   :widths: 25 75
   :header-rows: 1

   * - Command
     - Description
   * - `sbatch`
     - Submit a job script
   * - `srun`
     - Run a command on allocated compute node(s)
   * - `scancel`
     - Delete a job
   * - `squeue`
     - Show state of jobs
   * - `sinfo`
     - Show state of nodes and partitions (queues)
   * - `smap`
     - Show jobs, partitions and nodes in a graphical network topology
   * - `scontrol`
     - Modify jobs or show information about various aspects of the cluster

Please continue reading for some good examples of each.

This page is specific for using Slurm on Discovery. For more in-depth and general information, please refer to the official [Slurm documentation].


##  Slurm CLI
List of typical Slurm commands for working on Discovery.

These functions are fully documented for the version of Slurm installed, which is listed in the manual pages. To get the manual pages for the Slurm functions, run `man <SLURM_command>` on the HPC. This command lists all the parameters and keywords that you can use with the given Slurm commands. You can also run `<SLURM_command> --help`, which will list the help page for the Slurm function. These two give you the full possibilities of what these functions can do. The following sections are helpful/commonly used Slurm commands that are good to know for different ticket requests and common checks on the cluster.

:::{important}
Slurm commands have numerous options to help your jobs run efficiently by requesting specific resources. Options usually have both short and verbose versions, such as `--nodes` and `-n` (both mean the same thing). The examples in this documentation all use the verbose version of the options for clarity, but you can use the short version if you prefer. For example, `srun -p short -N 1 -n 1` means the same thing as `srun --partition=short --nodes=1 --ntasks=1`.
:::

### Job reporting
.. list-table::
   :widths: 35 85
   :header-rows: 1

   * - Command
     - Description
   * - `sacct <options>`
     - Display job accounting information
   * - `sreport <options>`
     - Generate reports about cluster utilization and job statistics

:::{note}
Each command's options and functions may vary depending on the Slurm version and configuration. We recommend consulting the Slurm documentation for more information on the full range of available commands and their usage. See [Slurm documentation] for details.
:::


## Viewing Cluster Information

Use the following commands to view information about the cluster. This information can help you better understand the hardware that is available in order to customize your job scripts.

:::{seealso}
{ref}`hardware-overview` for more information.
:::

:::{list-table}
---
header-rows: 1
---
* - Slurm Command
  - Function
* - `sinfo <options>`
  - View partition and node information. Use option -a to view all partitions.
* - `smap <options>`
  - View details about the cluster in a visual format
:::

(submitting-jobs)=

## Submitting Jobs
There are two main commands for submitting jobs to Discovery: `srun` and `sbatch`.
To run a job interactively, use `srun`. To submit a job to run in the background with a script, use `sbatch`.


:::{list-table}
---
header-rows: 1
---
* - Slurm Command
  - Function
* - `srun`
  - Run an interactive job on the cluster. See {ref}`using-srun`
* - `sbatch <scriptname.script>`
  - Submit a script to the scheduler for running a job. See {ref}`using-sbatch`
* - `scancel <jobid>`
  - Cancel a pending or running job on the cluster
:::

## Account information
Some Discovery users have more than one Discovery group account associated with their usernames. For example, a student might be in a class using Discovery and a student club using Discovery for a club project. In this case, the student would have two group accounts associated with their username.

When running a job with either `srun` or `sbatch`, if you have more than one account associated with your username, we recommend you use the `--account=` flag and specify the account that corresponds to the respective project. In the example with a student associated with a class and a student club, if the student is on Discovery submitting a job for a project for their class, set the `account=` flag to the name of the class account. If the student is working on a project for the club, set the `account=` flag to the name of the student club account.

To find out what account(s) your username is associated with, use the following command:

:::{code} bash
sacctmgr show associations user=<yourusername>
:::

After you have determined what accounts your username is associated with, if you have more than one account association, you can use the `account=` flag with your usual `srun` or `sbatch` commands.

For example, if you are associated with an account named `dataclub` and an account named `info7500`, and you're currently doing work that should be associated with the `dataclub` account, in your `srun` command, you can add the `--account=dataclub` flag to specify that account:

:::{code} bash
srun --account=dataclub --partition=short --nodes=1 --ntasks=28 --mem=0 --pty /bin/bash
:::

:::{note}
If you do not have more than one account associated with your username, you do not need to use the `--account=` flag. Most users on Discovery have only one account associated with their username.
:::

**Use environment modules**: Slurm's environment is set via modules to manage software installations. Make sure to load the appropriate modules before running your job.




### Viewing Cluster Info
Use the following commands to view information about the cluster. This information can help you better understand the hardware that is available in order to customize your job scripts. Also see {ref}`hardware-overview` for more information.

:::{list-table}
---
widths: 35 85
header-rows: 1
---
* - Slurm Command
  - Function
* - `sinfo <options>`
  - View partition and node information; use option `-a` to view all partitions
* - `smap <options>`
  - View details about the cluster in a visual format
:::

:::{list-table}
---
widths: 30 90
header-rows: 1
---
* - Slurm Command
  - Function
* - `srun`
  - Run an interactive job on the cluster
* - `sbatch <scriptname.script>`
  - Submit a script to the scheduler for running a job
* - `scancel <jobid>`
  - Cancel a pending or running job on the cluster
:::

(using-srun)=
## Using srun
Use the Slurm command `srun` to allocate an interactive job. This means you use specific options with `srun` on the command line to tell Slurm what resources are needed to run your job, such as number of nodes, amount of memory, and amount of time. Enter `srun` command and options on the command line, the and press `Return`. Slurm will find, and then allocate, the specified resources. Depending on the specifications, this process may take a few minutes. All `srun` options can be found in the [Slurm documentation]. The following image shows an example of an `srun` command as run on a command line.

:::{image} ../images/srun_example.jpg
---
alt: image of the command line showing an example `srun` command
width: 500px
align: center
---
:::

### Examples using srun
This section details a few examples using `srun`. You should first review the {ref}`hardware-overview` and {ref}`partition-names` sections
to be familiar with the available hardware and partition limits on Discovery. This way, you can tailor your request to fit both the needs of your job
and the limits of the partitions. For example, if you specify `--partition=short` and `--time=01:00:00`, you'll get an error because the
time you've specified exceeds the limit for that partition. Also keep in mind that while these examples are all valid, general examples, they might not work
for your particular job.

This simple `srun` example is to move to a _compute_ node after you first log into the HPC:

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

To allocate a GPU node, you should specify the `gpu` partition and use the --gres option:

:::{code} bash
srun --partition=gpu --nodes=1 --ntasks=1 --export=ALL --gres=gpu:1 --mem=1Gb --time=01:00:00 --pty /bin/bash
:::

For more information about working with GPUs, see {ref}`working-gpus`.

(using-sbatch)=
## Using sbatch
You use the `sbatch` command with a bash script to specify the
resources you need to run your jobs, such as the number of nodes wanted to run jobs on and the amount of memory required. Slurm then schedules your job based on the available resources specified.

The general format for submitting a job to the scheduler is as follows:

:::{code} bash
sbatch example.script
:::

Where `example.script` is a script detailing the parameters of the job you want to run.

::::{note}
The default time limit depends on the partition that you specify in your submission script using the `--partition=<partition name>` option. If your job does not complete within the requested time limit, Slurm will automatically terminate the job.

:::{seealso}
{ref}`partition-names` for the most up-to-date partition names and parameters.
:::
::::

### Examples using sbatch
#### Job request: one node
Run a job on one node for four hours on the short partition:

:::{code} shell
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
# SBATCH --partition=short

# <commands to execute>
:::

#### Job request: one node with additional memory
The default memory per allocated core is 1GB. If calculations attempt to access more memory than allocated, Slurm automatically terminates the job. Request a specific amount of memory in the job script if calculations require more than the default. The example script below requests 100GB of memory (`--mem=100G`). Use one capital letter to abbreviate the unit of memory (K, M, G, T) with the `--mem=` option, as that is what Slurm expects to see:

:::{code} shell
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --mem=100G
# SBATCH --partition=short

# <commands to execute>
:::

#### Job request: one node with exclusive use of a node
If you need exclusive use of a node, such as when you have a job that has high I/O requirements, you can use the exclusive flag. The example script below specifies the exclusive use of one node in the short partition for four hours:

:::{code} shell
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --exclusive
# SBATCH --partition=short

# <commands to execute>
:::

### Example parallel job scripts

Parallel jobs should use code configured to use the reserved resources. Running unoptimized code in parallel could fail. The following script examples all allocate additional memory. The default memory per allocated core is 1 GB. If your calculations try to use more memory than allocated, Slurm automatically terminates your job. You should request a specific amount of memory in your job script if your calculations need more than the default.

#### 8-task job, one node and additional memory
:::{code} shell
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --mem=100G
# SBATCH --partition=short

# <commands to execute>
:::

#### 8-task job, multiple nodes and additional memory
:::{code} shell
#!/bin/bash
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=1
#SBATCH --time=00:30:00
#SBATCH --job-name=MyJobName
#SBATCH --mem=100G
# SBATCH --partition=short

# <commands to execute>
:::

## Slurm job arrays
In HPC environments, users often need to run large numbers of jobs that are very similar, such as simulations with varying input parameters or the processing of multiple data files. Managing and tracking individual jobs can be a cumbersome and time-consuming process. Enter: Slurm job arrays.

A job array is a collection of related jobs submitted to Slurm as a single entity. A unique index identifies each job in the array, which runs independently on a separate compute node. The index can specify different input files or parameters for each job, allowing for the efficient processing of many similar tasks.

There are several ways to define job arrays, such as specifying the range of indices or providing a list of indices in a file. Slurm also offers various features to manage and track job arrays, such as options to simultaneously suspend, resume, or cancel all jobs in the array.

### Using Slurm arrays
Slurm Job Arrays can be a valuable tool when dealing with jobs that consist of numerous identical tasks. For example, when processing a large set of input files or running simulations with varying input parameters, a Job Array can simplify your submission process, improve code versatility, and reduce the load on the scheduler.


To use an array with your jobs, in your `sbatch` script, use the `array=` option, which is exemplified throughout the following subsections. Let us assume that we want to run a 10 job array one job at a time. We would add the following line to the bash script:

:::{code} shell
#SBATCH --array=1-10%1
:::

To illustrate, let's consider three possible ways to process a collection of input files.

* Write a single script that loops through the input files and executes the processing code.
* Write a script that processes a single file and submits it multiple times, once for each file, with the filename accepted as a parameter.
* Use a job array, which allows you to apply a single-file script to a large set of input files without putting undue stress on the scheduler.

In summary: (**1**) can be challenging to parallelize effectively; (**2**) can create many jobs, potentially putting undue stress on the job scheduler; (**3**) can be helpful when developing a script that works well for both single and large groups of files. Furthermore, all sub-jobs in the array share the same base job ID, making it easy to group and organize your workflow.

Using Slurm job arrays can simplify job management and streamline your workflow, mainly when dealing with large sets of identical tasks.

### Sample data
See :download:`bash script to generate sample data <../resources/create_sample_array_data.sh>`. This script simply creates a data directory array_example_data and populates it with some text files.


.. literalinclude:: create_sample_array_data.sh
   :language: bash
   :emphasize-lines: 12,15-18
   :linenos:


### Batch script and array
We will then use this script, which we save as `array_batch.sh` to “evaluate” the data:

:::{code-block}
---
name: array_batch.sh
emphasize-lines: 2,3
lineno-start: 1
---

#!/bin/bash
#
#SBATCH --ntasks=1
#SBATCH --partition=short
#SBATCH --output=array_example_%j.out
#SBATCH --error=array_example_%j.err
#
##SLURM_ARRAY_TASK_ID=4

# default values:
F_PATH="array_example_data"
F_NAME="toy_data_0.dat"
F_PATH_NAME=${F_PATH}/${F_NAME}
COMPLETED_FILES_PATH="processed_files"
#
if [[ ! -d ${COMPLETED_FILES_PATH} ]]; then
  mkdir -p ${COMPLETED_FILES_PATH}
fi
#
# if a parameter is provided, assume it is the full pathname. NOTE: we'll override
#  this behavior shortly...
if [[ ! -z ${1} ]]; then
  F_PATH_NAME=$1
fi
#
# ... however, if we have an array index, redeine F_PATH_NAME, etc.
if [[ ! -z ${SLURM_ARRAY_TASK_ID} ]]; then
  if [[ ! -z ${1} ]]; then
     F_PATH=${1}
  fi
  #
  # now, how do we get the filename. The easiest thing to do is something like:
  #F_NAME="toy_data_${SLURM_ARRAY_TASK_ID}.DAT"
  #
  # the problem, of course, is that we need to have full control of the filenames.
  # Let's do something like this instead:
  fls=( ./${F_PATH}/*.dat )
  F_NAME=${fls[${SLURM_ARRAY_TASK_ID}]}
  #
  F_PATH_NAME=${F_PATH}/${F_NAME}

fi

# The action:
# In this case, not much. We'll just shout out the host name and cat the contents
#  of the file.
echo "Hosthame: `hostname`"
echo "CPU codename: \n`cpu_codename`"
#
echo "File: ${F_PATH_NAME}\n"
cat ${F_PATH_NAME}
mv ${F_PATH_NAME} ${COMPLETED_FILES_PATH}/
:::

:::{note}
The SLURM directives in the header of this file are perhaps better suited for a single run, against one input file. To run as an array:

1. Provide an `--array` directive;
1. Modify the `--output` and `--error` directives slightly.
:::

Then, submit the job as follows:

:::{code} bash
sbatch --array=0-19 --output=job_array_example_%A_%a.out --error=job_array_example_%A_%a.err array_batch.sh
:::

`%A` and `%a` will output the parent `jobID` and array index, respectively. Submitted this way, Slurm will generate 20 jobs; for each job, a unique index value (i.e., `[0, 1, ..., 19]`) will be assigned to the `SLURM_ARRAY_TASK_ID` environment variable, which has various uses. For example, as discussed in the script comments, it can define the input path name, or as we have done in this example, it can select the `k-th` file in the directory, or it can choose a set of user-defined input parameters, for example, from a JSON file, or it can be used simply as an input parameter.

:::{important}
The example script above can be run as an array or against a single file, either interactively or as a batch script, without making any additional changes. Additionally, an optional parameter can specify the input filename (single task mode) or an input directory (array mode).
:::

Checkout our tutorials on GitHub for more examples of running Slurm Job Arrays, and via different interfaces and languages (i.e., [Training Slurm Job Arrays on GitHub]).

## Monitoring Jobs

:::{list-table}
---
header-rows: 1
---
* - Slurm Command
  - Function
* - `seff <jobid>`
  - Reports the computational efficiency of your calculations.
* - `squeue -u <your user name>`
  - Displays your job status in the job queue. Good to use with `sbatch`.
* - `scontrol show jobid -d <JOBID>`
  - Displays your job information. Good to use with `srun`.
:::

You can monitor your jobs by using the Slurm `scontrol` command. Type `scontrol show jobid -d <JOBID>`, where `JOBID` is the number of your job. In the figure at the top of the page, you can see that when you submit your `srun` command, Slurm displays the unique ID number of your job (`job 12962519`). This is the number you use with `scontrol` to monitor your job.

## Cluster and Node States
Here are some more examples of using `sinfo` and `scontrol` to provide information about the state of the cluster and specific nodes:

### Using sinfo
The `sinfo` command will show information about all partitions in the cluster, including the partition name, available nodes, and status. By default, `sinfo` reports:


:::{list-table}
---
widths: 20 100
header-rows: 0
---
* - `PARTITION`
  - The list of the cluster’s partitions; a set of compute nodes grouped logically
* - `AVAIL`
  - The active state of the partition (up, down, idle)
* - `TIMELIMIT`
  - The maximum job execution wall-time per partition
* - `NODES`
  - The total number of nodes per partition
* - `STATE`
  - See STATE table below
* - `NODELIST(REASON)`
  - The list of nodes per partition
:::


:::{list-table} State Table
---
widths: 20 100
header-rows: 1
---
* - State
  - Description
* - `mix`
  - Only part of the node is allocated to one or more jobs and the rest in an Idle state
* - `alloc`
  - The entire resource on the node(s) is being utilized
* - `idle`
  - The node is in an idle start and has none of its resources being used
:::

#### Examples using sinfo
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

For example, this command will show information about a specific partition in the cluster, including the number of nodes, number of free nodes, and state of the partition::

:::{code} bash
sinfo -p gpu -t idle
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
gpu          up    8:00:00      1  drain d1025
gpu          up    8:00:00      2   resv c2177,d1029
gpu          up    8:00:00     13   idle c[2160,2163-2164,2166,2168-2170,2175,2179-2183]
:::

You can use the `--Format` flag to get more information or a specific format for the output:

:::{code} bash
sinfo -p <partition> -t idle --Format=gres,nodes
:::

For example:

:::{code} bash
sinfo -p gpu -t idle --Format=gres,nodes
GRES                NODES
gpu:t4:4(S:0-1)     1
gpu:k80:8(S:0-1)    5
gpu:a100:4          1
gpu:k40m:1          8
gpu:k80:7(S:0-1)    1
:::

Where `gpu:a100:4` is read as follows: The number after (i.e, 4) indicates that the 1 node has 4 `gpu:a100s`.

View detailed information about nodes:

:::{code} bash
sinfo -N -l
:::

This command will show detailed information about all nodes in the cluster, including the node name, state, CPU architecture, memory, and available features.

View what features a node has:

:::{code} bash
sinfo -n <node> --Format=nodes,nodelist,statecompact,features
:::

For Example:

:::{code} bash
sinfo -n d0139 --Format=nodes,nodelist,statecompact,features
NODES               NODELIST            STATE               AVAIL_FEATURES
1                   d0139               mix                 zen2,ib,prod
:::

View what nodes have what features in a partition:

:::{code} bash
sinfo -p <partition> --Format=nodes,cpus,features,nodelist
:::

For example:

:::{code} bash
sinfo -p short --Format=nodes,cpus,features,nodelist
NODES               CPUS                AVAIL_FEATURES      NODELIST
13                  28                  broadwell,next      c[0699-0711]
8                   56                  ib,cascadelake,next d[0001-0008]
120                 56                  ib,cascadelake,prod d[0009-0128]
32                  20                  ivybridge,prod      c[3000-3006,3008-303
115                 24                  lenovo,rapl,haswell,c[0156,0158-0159,016
381                 28                  broadwell,prod      c[0336-0343,0376-040
4                   16                  sandybridge,largememc[2000-2003]
2                   112                 cascadelake,ib,prod d[0129-0130]
20                  128                 zen2,ib,prod        d[0131-0150]
:::

View what nodes are in what state in a partition using `statecompact`:

:::{code} bash
sinfo -p lopez --Format=time,nodes,statecompact,features,memory,cpus,nodelist
:::

### Using scontrol
The `scontrol` command is a command-line utility that allows users to view and control Slurm jobs and job-related resources. It provides a way to check the status of jobs, modify job properties, and perform other job-related tasks.

Some of the tasks that can done using `scontrol` include:
* Viewing job status and properties: `scontrol` can display detailed information about a job, including its status, node allocation, and other properties.
* Modifying job properties: `scontrol` allows users to modify job properties such as the job name, the number of nodes, the time limit, and other parameters.
* Managing job dependencies: `scontrol` provides a way to specify job dependencies and view the dependencies between jobs.
* Suspending and resuming jobs: `scontrol` can stop and resume running jobs, allowing users to temporarily halt jobs or continue them as needed.
* Canceling jobs: `scontrol` can cancel jobs that are running or queued, allowing users to stop jobs that are no longer needed.

Overall, `scontrol` is a powerful tool for managing Slurm jobs and job-related resources. Its command-line interface allows users to perform a wide range of tasks, from checking the status of jobs to modifying job properties and managing dependencies.

#### Controlling jobs
`scontrol hold <jobid>` Place a hold on a pending job, i.e., prevent specified job from starting. <job_list> is either a space separate list of job IDs or job names.

`scontrol release <jobid>` Release a held job, i.e., permit specified job to start (see hold).

`scontrol requeue <jobid>` Re-queue a completed, failed, or cancelled job

For more information on the commands listed above, along with a complete list of `scontrol` commands run `scontrol --help`.

#### Examples using scontrol
View information about a specific node:

:::{code} bash
scontrol show node -d <node_name>
:::

For example:

:::{code} bash
scontrol show node -d c2180
NodeName=c2180 Arch=x86_64 CoresPerSocket=14
CPUAlloc=0 CPUTot=28 CPULoad=0.01
AvailableFeatures=broadwell,prod
ActiveFeatures=broadwell,prod
Gres=gpu:k80:7(S:0-1)
GresDrain=N/A
GresUsed=gpu:k80:0(IDX:N/A)
NodeAddr=c2180 NodeHostName=c2180 Version=21.08.8-2
OS=Linux 3.10.0-1160.25.1.el7.x86_64 #1 SMP Wed Apr 28 21:49:45 UTC 2021
RealMemory=512000 AllocMem=0 FreeMem=486591 Sockets=2 Boards=1
State=IDLE ThreadsPerCore=1 TmpDisk=0 Weight=6 Owner=N/A MCS_label=N/A
Partitions=gpu,multigpu,reservation
BootTime=2022-12-14T07:23:47 SlurmdStartTime=2022-12-23T07:40:56
LastBusyTime=2023-01-19T14:40:02
CfgTRES=cpu=28,mem=500G,billing=728,gres/gpu=7
AllocTRES=
CapWatts=n/a
CurrentWatts=0 AveWatts=0
ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s
:::

For information on all reservations, this command will show information about a specific node in the cluster, including the node name, state, number of CPUs, and amount of memory::

:::{code} bash
scontrol show reservations
:::

Which is equivalent to both of the following commands::

:::{code} bash
scontrol show reservation
scontrol show res
:::

View information about a specific job. This command will show information about a specific job, including the job ID, state, username, and partition name::

:::{code} bash
scontrol show job <job_id>
:::

To view information about a specific reservation (e.g., found via `scontrol show res` listed above), and print information about a specific reservation in the cluster, including the reservation name, start time, end time, and nodes included in the reservation:

:::{code} bash
scontrol show reservation <reservation_name>
:::

These are just a few examples of what you can do with `sinfo` and `scontrol` to view information about the state of the cluster and specific nodes. There are many other options and commands available, and it is recommended to consult the [Slurm documentation] for more information on how to use these tools effectively.


## Slurm Best practices
Proper resource request syntax:

:::{code} bash
#!/bin/bash
#SBATCH --job-name=my_job       # Job name
#SBATCH --ntasks=4              # Number of tasks
#SBATCH --cpus-per-task=2       # Number of CPUs per task
#SBATCH --mem-per-cpu=4G        # Memory per CPU
#SBATCH --time=02:00:00         # Time limit
#SBATCH --partition=my_partition # Partition (queue) to use
:::

* Submit jobs using batch scripts: Save the above sample code in a file named `my_job.sh`. To submit the job, run the following command:

:::{code} bash
sbatch my_job.sh
:::

* Monitor your job's progress: Use the `squeue` command to check the status of your submitted job:
:::{code} bash
squeue -u username
:::

* Use environment modules: Load the necessary modules before running your job. In this example, we load the Python and TensorFlow modules:
:::{code} bash
  module load python/3.8
  module load tensorflow/2.5.0
:::

Use the appropriate file system:
For I/O-intensive tasks, use the local scratch storage (e.g., /scratch directory) for temporary files and I/O operations. In your job script, you could include:
:::{code} bash
#!/bin/bash
# Other Slurm directives...

# Set the scratch directory
SCRATCH_DIR=/scratch/username/my_job_${SLURM_JOB_ID}
mkdir -p ${SCRATCH_DIR}

# Copy input files to the scratch directory
cp input_files/* ${SCRATCH_DIR}

# Execute the job in the scratch directory
cd ${SCRATCH_DIR}
python my_script.py

# Copy output files back to the home directory
cp output_files/* /home/username/output/

# Clean up the scratch directory
rm -r ${SCRATCH_DIR}
:::

Understand basic Slurm commands:
View cluster information: sinfo
Submit a job: sbatch my_job.sh
View the job queue: squeue -u username
Cancel a job: scancel job_id
Manage and view job details: scontrol
Choose the appropriate partition:
To check available partitions and their specifications, use the sinfo command:

:::{code} bash
#!/bin/bash
#SBATCH --job-name=my_job       # Job name
#SBATCH --ntasks=4              # Number of tasks
#SBATCH --cpus-per-task=2       # Number of CPUs per task
#SBATCH --mem-per-cpu=4G        # Memory per CPU
#SBATCH --time=02:00:00         # Time limit
#SBATCH --partition=my_partition # Partition (queue) to use

# Load necessary modules
module load python/3.8
module load tensorflow/2.5.0

# Your script to run
python my_script.py
:::

* Avoid overloading the system: Request only the resources you need, without over- or under-allocating. Over-allocation can lead to longer wait times, while under-allocation may cause job failures.

* Use checkpoints: For long-running jobs, use checkpointing to save intermediate results. This can help you recover your work in case of job failure or cluster issues. Here is an example for TensorFlow:

:::{code} python

import tensorflow as tf

# Create a checkpoint callback
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
           filepath='checkpoints/model_{epoch:02d}.ckpt',
           save_weights_only=True,
           save_freq='epoch'
)

# Train the model with the checkpoint callback
model.fit(train_data, train_labels, epochs=100, callbacks=[checkpoint_callback])
:::

* Clean up after your job: Remove any files or directories that your job created after it's finished running. This practice helps keep the system clean and frees up resources for other users. In the code snippet provided for using the appropriate file system, we included an example of cleaning up the scratch directory after the job completion:

:::{code} bash
  # Clean up the scratch directory
  rm -r ${SCRATCH_DIR}
:::

* Use the proper resource request syntax: Slurm follows a specific syntax to request resources, such as the number of CPUs, memory, and time required for your job. Make sure to use the proper syntax to avoid any errors.
* Specify an appropriate job name: Giving your job a descriptive name will help you and other users identify it easily.
* Submit jobs using batch scripts: It's best to submit jobs using batch scripts instead of typing commands manually. Batch scripts allow you to automate the process and make it easier to run multiple jobs at once.
* Use the correct partition: Slurm HPC has several partitions, each designed for specific purposes. Choose the proper partition for your job to ensure you use the most appropriate resources.
* Monitor your job's progress: Keep an eye on your job's progress to ensure it's running correctly, and you can identify any issues that may arise.
* Avoid overloading the system: Be mindful of the resources you're requesting and avoid overloading the system so that other users have access to the resources they need.
* Use checkpoints: If your job is long-running, consider using checkpoints to save your progress, allowing for resuming jobs if interrupted.
* Use environment modules: Slurm's environment is set via modules to manage software installations. Make sure to load the appropriate modules before running your job.
* Use the appropriate file system: Slurm HPC typically has several file systems with different performance characteristics. Use the proper file system for your job to ensure you get the best performance.
* Clean up after your job: Make sure to remove any files or directories that your job created after it's finished running. This practice helps keep the system clean and frees up resources for other users.

* Understand the basic Slurm commands: Familiarize yourself with basic Slurm commands such as `sinfo`, `sbatch`, `squeue`, `scancel`, and `scontrol`. These commands will help you manage and monitor your jobs on the HPC cluster.

* Use the appropriate partition: Choose the right partition (queue) for your job based on resource requirements, such as CPU, memory, and time limit. Use the `sinfo` command to check available partitions and their specifications.

:::{code} bash
sinfo -a
:::

* Specify required resources: Clearly specify the resources needed for your job using `--cpus-per-task`, `--mem`, and `--time` options. Overestimating resource requirements can lead to longer wait times in the queue.

:::{code} bash
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=02:00:00
:::

* Use job arrays for parallel tasks: If your research involves running many similar tasks, use job arrays to efficiently submit and manage them.

:::{code} bash
  #SBATCH --array=1-100
:::

* Check job status and reason for pending: Use the `squeue` command to check the status of your job and understand why it's pending. This can help you identify any issues with your submission script.


:::{code} bash
squeue -u username
:::

* Cancel unnecessary jobs: If you realize that a submitted job is no longer required, cancel it to free up resources for other users.

:::{code} bash
scancel job_id
:::

* Test your jobs with small datasets: Before running a full-scale job, test your scripts with smaller datasets to ensure they work correctly and efficiently.
* Use checkpointing for long-running jobs: If your job runs for a long time, use checkpointing to save intermediate results. This can help you recover your work in case of job failure or cluster issues.
* Set email notifications: Use the `--mail-type` and `--mail-user` options to receive email notifications when your job starts, ends, or encounters errors.

:::{code} bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=your_email@northeastern.edu
:::

* Use local scratch storage for I/O intensive tasks: To improve performance, use the local scratch storage (e.g., /scratch directory) for temporary files and I/O operations.
* Optimize code for parallel execution: Where possible, parallelize your code to take advantage of multiple CPU cores or nodes.
* Monitor job performance: Use tools such as `sstat` and `sreport` to monitor the performance of your job, including CPU and memory usage.

:::{code} bash
sstat --format=AveCPU,AveRSS,MaxRSS job_id
:::

Use environment modules: Load required software modules using the module command to maintain a clean and consistent environment for your jobs.

:::{code} bash
module load software_name/version
:::  

* Request resources as needed: Request only the resources you need, without over- or under-allocating. Over-allocation can lead to longer wait times, while under-allocation may cause job failures.

* Document your job scripts: Use comments in your job scripts to explain resource requests, module loads, and other important information. This can help others understand your work and facilitate collaboration.

:::{code} bash
#!/bin/bash
#SBATCH --job-name=my_job        # Job name
#SBATCH --output=my_job_%A.out   # Output file name
#SBATCH --error=my_job_%A.err    # Error file name
#SBATCH --ntasks=4               # Number of tasks
#SBATCH --mem=8G                 # Memory per task
#SBATCH --time=02:00:00          # Time limit
#SBATCH --partition=my_partition # Partition (queue) to use

# Load necessary modules
module load python/3.8
module load tensorflow/2.5.0

# Your script to run
python my_script.py
:::

Now, here are 10 best practices for running machine learning tasks on a Slurm-based HPC cluster:

1. Use GPU resources: If your cluster has GPU nodes available, use them for training and inference tasks that can benefit from the parallel processing capabilities of GPUs.

:::{code} bash
#SBATCH --gres=gpu:1
:::

* Efficiently manage GPU resources: Request only the required number of GPUs and set the `CUDA_VISIBLE_DEVICES` variable to limit the GPUs accessible to your code.

:::{code} bash
export CUDA_VISIBLE_DEVICES=$SLURM_JOB_GPUS
:::

* Scale up with distributed training: If your cluster has multiple nodes, consider using distributed training techniques, such as Horovod or TensorFlow's tf.distribute API, to speed up training.
* Use data parallelism: If your dataset is large, partition it across multiple nodes to speed up processing.
* Implement checkpointing and early stopping: For long-running training jobs, implement checkpointing to save intermediate models and early stopping to end training when the model performance plateaus.
* Tune hyperparameters: Perform hyperparameter tuning by creating job arrays to run multiple training jobs with different parameter combinations.

:::{code} bash
#SBATCH --array=1-20
:::

* Monitor resource usage: Continuously track the resource usage of your jobs, including GPU, CPU, and memory, to identify performance bottlenecks and optimize your code.

:::{code} bash
sstat --format=AveCPU,AveGPU,AveRSS,MaxRSS job_id
:::
* Use pre-built machine learning libraries: Leverage pre-built libraries, such as TensorFlow, PyTorch, and Scikit-learn, to streamline your machine learning tasks.
* Preprocess data efficiently: Perform data preprocessing tasks, such as data normalization and augmentation, in parallel to minimize the time spent on data processing.
* Optimize I/O operations: Store large datasets on a parallel filesystem, such as Lustre, to improve read and write performance. Also, consider using data loaders and iterators that support parallel I/O for efficient data access during training.


[Slurm documentation]: https://slurm.schedmd.com/documentation.html
[Training Slurm Job Arrays on GitHub]: https://github.com/northeastern-rc/training-slurmarrayjobs
