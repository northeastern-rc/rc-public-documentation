(interactive-and-batch-mode)=
# Interactive and Batch Mode

In our High-Performance Computing (HPC) environment, users can run jobs in two primary modes: Interactive and Batch. This page provides an in-depth guide to both, assisting users in selecting the appropriate mode for their specific tasks.

(using-srun)=
## Interactive Jobs: `srun` Command
The `srun` command is used to submit an interactive job, which runs in a shell terminal. This method is useful when you want to test a short computation or run an interactive session like a shell, Python, or an R terminal.

To start an `srun` session, the following syntax is used from the login node:

:::{code} bash
srun [options] [command]
:::

The following is an example of an `srun` job running on 1 node, with 1 task:

:::{code} bash
srun -N 1 -n 1 -p short --pty bash
:::

- **`n, --ntasks=<number>`**: specify the number of tasks
- **`N, --nodes=<minnodes[-maxnodes]>`**: specify the number of nodes
- **`p, --partition=<partition-name>`**: specify a partition for the job to run on

To see all options for `srun`, please refer to [srun manual] from SchedMD.

### Examples Using `srun`

You can tailor your request to fit both the needs of the job and the partition limits if you're familiar with the available [hardware](https://rc-docs.northeastern.edu/en/latest/hardware/hardware_overview.html#hardware-overview) and [partitions](https://rc-docs.northeastern.edu/en/latest/hardware/partitions.html) on Explorer. 

To request one node and one task for 30 minutes with X11 forwarding (check that you have [X11 forwarding](https://rc-docs.northeastern.edu/en/latest/gettingstarted/connectingtocluster/mac.html#x11-on-mac-os) setup) on the short partition, type:

:::{code} bash
srun --partition=short --nodes=1 --ntasks=1 --x11 --mem=2G --time=00:30:00 --pty /bin/bash
:::

To request one node, with 10 tasks and 2 CPUs per task (a total of 20 CPUs), 40 GB of memory, for one hour on the express partition, type:

:::{code} bash
srun --partition=short --nodes 1 --ntasks 10 --cpus-per-task 2 --pty --mem=40G --time=01:00:00 /bin/bash
:::

To request 2 nodes, each with 10 tasks per node and 2 CPUs per task (a total of 40 CPUs), 80 GB of memory, for one hour on the express partition, type:

:::{code} bash
srun --partition=short --nodes=2 --ntasks 10 --cpus-per-task 2 --pty --mem=80G --time=01:00:00 /bin/bash
:::

To allocate a GPU node, you should specify the `gpu` partition and use the `--gres` option:

:::{code} bash
srun --partition=gpu-interactive --nodes=1 --ntasks=1 --gres=gpu:1 --mem=2Gb --time=01:00:00 --pty /bin/bash
:::

(using-sbatch)=
## Batch Jobs: `sbatch` Command
The `sbatch` command is used to submit a job script for passive execution. The script includes the `SBATCH` directives that control the job parameters (e.g., number of nodes, CPUs per task, job name). A node is a single machine in the cluster allocated for computation, while a task is a unit of parallel work required from within the job. Not all programs are optimized to run on more than one node. We recommmend testing if increasing the number of tasks decreases job runtime prior to testing if increasing the number of nodes decreases runtime.

:::{important}
Remember for all requests to the scheduler, the more resources requested the longer your job may sit in the queue waiting for the allocation of those resources.
:::

To submit the batch jobs, the following is run from the login node:

:::{code} bash
sbatch [options]  <script_file>
:::

An example sbatch script for a job utilizing 2 nodes and 16 tasks per node:

:::{note}
Only use more than 1 node if your program is optimized for multi-nodal execution.
:::

:::{code} bash
#!/bin/bash
#SBATCH -J MyJob                            # Job name
#SBATCH -N 2                                # Number of nodes
#SBATCH -n 16                               # Number of tasks
#SBATCH -o output_%j.txt                    # Standard output file
#SBATCH -e error_%j.txt                     # Standard error file
#SBATCH --mail-user=$USER@northeastern.edu  # Email
#SBATCH --mail-type=ALL                     # Type of email notifications

# Your program/command here

./my_program
:::

To submit this job script, save it as `my_job.sh` and run:
:::{code} bash
sbatch my_job.sh
:::

For more information on the `SBATCH` directives that can be used in the script, please refer to the [sbatch manual] from Schedmd.

Request a specific amount of memory in the job script if calculations require more than the default 2GB per allocated code. The example script below requests 100GB of memory (`--mem=100G`). Use one capital letter to abbreviate the unit of memory (i.e., kilo `K`, mega `M`, giga `G`, and tera `T`) with the `--mem=` option, as that is what Slurm expects to see:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --mem=100G
#SBATCH --partition=short

# <commands to execute>
:::


[sbatch manual]: https://slurm.schedmd.com/sbatch.html
[srun manual]: https://slurm.schedmd.com/srun.html