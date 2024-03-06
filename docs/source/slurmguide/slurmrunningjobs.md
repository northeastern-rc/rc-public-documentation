(slurm-running-jobs)=
# Slurm Running Jobs

You have two options when running tasks, run interactively via {ref}`using-srun` or by batch via {ref}`using-sbatch`.

For parallel tasks, one can treat each task as a separate job and run them independently. The other option is to allocate resources for all the jobs simultaneously, allowing them to overlap (share CPUs, RAM, etc.). This is done with the `--overlap` flag: the assumption must be that not all tasks require all resources simultaneously, creating a more natural working environment, and resources are not wasted on idle time.

:::{note}
While the `sbatch` and `srun` commands request resource allocation if none exists, using `salloc` allows us to separate the allocation and submission processes.
:::

Some things Slurm assumes, like there is no overlap between different CPUs by default: tasks do not share CPUs with others running parallel. If overlap is needed, use the following Slurm flag:

:::{code} bash
--overlap
:::

Also, set the environment variable `SLURM_OVERLAP=1` via
:::{code} bash
export SLURM_OVERLAP=1
:::

:::{important}
Run `export SLURM_OVERLAP=1` prior to logging onto a compute node when using MPI interactively.
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

:::{code} bash
srun -N 1 -n 1 --pty bash
:::

This command starts an interactive bash shell on one node with one task.

### Examples using `srun`

The user needs to review the {ref}`hardware-overview` and {ref}`partition-names` to be familiar with the available hardware and partition limits on Discovery. This way, user can tailor the request to fit both the needs of the job and the limits of partitions. For example, if the user specifies `--partition=short` and `--time=01:00:00`, it will result in an error because the time specified exceeds the limit for that partition.

This simple `srun` example is to move to a *compute* node after you first log into the HPC:

:::{code} bash
srun --pty /bin/bash
:::

To request one node and one task for 30 minutes with X11 forwarding on the short partition, type:

:::{code} bash
srun --partition=short --nodes=1 --ntasks=1 --x11 --mem=10G --time=00:30:00 --pty /bin/bash
:::

To request one node, with 10 tasks and 2 CPUs per task (a total of 20 CPUs), 1 GB of memory, for one hour on the express partition, type:

:::{code} bash
srun --partition=short --nodes 1 --ntasks 10 --cpus-per-task 2 --pty --mem=1G --time=01:00:00 /bin/bash
:::

To request two nodes, each with 10 tasks per node and 2 CPUs per task (a total of 40 CPUs), 1 GB of memory, for one hour on the express partition, type:

:::{code} bash
srun --partition=short --nodes=2 --ntasks 10 --cpus-per-task 2 --pty --mem=1G --time=01:00:00 /bin/bash
:::

To allocate a GPU node, you should specify the `gpu` partition and use the `–gres` option:

:::{code} bash
srun --partition=gpu --nodes=1 --ntasks=1 --gres=gpu:1 --mem=1Gb --time=01:00:00 --pty /bin/bash
:::

(using-sbatch)=
## Batch Jobs: `sbatch`
The `sbatch` command is used to submit a job script for later execution. The script includes the `SBATCH` directives that control the job parameters like the number of nodes, CPUs per task, job name, etc.

### Syntax: `sbatch`
:::{code} bash
sbatch [options]  <script_file>
:::

### Options and Usage: `sbatch`
- `n, --ntasks= <number>` : specify the number of tasks
- `N, --nodes=<minnodes[-maxnodes]>` : specify the number of nodes
- `J, --job-name=<jobname>` : specify a name for the job

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

### Examples using `sbatch`
#### Single node
Run a job on one node for four hours on the short partition:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --partition=short

# <commands to execute>
:::

# Slurm Job Scripts

## `sbatch` Job Script Examples

### Single node with additional memory
The default memory per allocated core is 1.95GB. If calculations attempt to access more memory than allocated, Slurm automatically terminates the job. Request a specific amount of memory in the job script if calculations require more than the default. The example script below requests 100GB of memory (`--mem=100G`). Use one capital letter to abbreviate the unit of memory (i.e., kilo `K`, mega `M`, giga `G`, and tera `T`) with the `--mem=` option, as that is what Slurm expects to see:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --mem=100G
#SBATCH --partition=short

# <commands to execute>
:::

### Single with exclusive use of a node
If you need exclusive use of a node, such as when you have a job that has high I/O requirements, you can use the exclusive flag. The example script below specifies the exclusive use of one node in the short partition for four hours:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --exclusive
#SBATCH --partition=short

# <commands to execute>
:::