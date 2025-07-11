(running-job-with-job-assist)=
# Running Jobs with job-assist

The `job-assist` command is designed to simplify the process of submitting jobs on the Discovery cluster using SLURM's `srun` and `sbatch` modes. It provides an intuitive interface for requesting resources and managing job submissions on the cluster.

## Features

This command provides three modes of operation:

| Mode              | Description                                               |
|-------------------|-----------------------------------------------------------|
| **Default**  | To quickly start a job with the default settings.         |
| **Interactive** | To submit the job interactively with customized resource requests. |
| **Batch**    | To generate and save `sbatch` scripts with specified parameters. |

## Getting Started with job-assist Command

#### Load the job-assist Module

:::{code} bash
module load job-assist
:::

#### To launch an interactive session, use the following command:

:::{code} bash
job-assist
:::

This command will display a menu option with different modes of operation.


:::{code} bash
#Simple Example of the Menu Options
SLURM Menu:
1. Default mode (srun --pty /bin/bash)
2. Interactive Mode
3. Batch Mode
4. Exit
Enter your option:
:::


### Default Mode

This mode runs a basic SLURM job with the command:

:::{code} bash
srun --pty /bin/bash
:::

By default, the resource allocated is short partition with 2 CPUs, 1 task, 1 node, and 2GB of memory for a duration of 4 hours.

::::{dropdown} Default Mode Example
:::{code-block} bash
[rc.computing@login-00 ~]$ job-assist
SLURM Menu:
1. Default mode (srun --pty /bin/bash)
2. Interactive Mode
3. Batch Mode
4. Exit
Enter your option: 1
Running default job: srun --pty /bin/bash
srun: job 43910949 queued and waiting for resources
srun: job 43910949 has been allocated resources
[rc.computing@d1019 ~]$
:::
::::


### Interactive Mode

In this mode, `job-assist` guide you through interactively requesting resources. You will be prompted to provide the following information:

- **Partition Name**: Choose from available partitions like `debug`, `express`, `short`, or `gpu-interactive`.
- **Number of Nodes**: Specify the number of nodes required.
- **Number of Tasks**: Specify the number of tasks.
- **CPUs per Task**: Specify how many CPUs are needed per task.
- **Time**: Specify the maximum run time for the job in `HH:MM:SS` format.
- **Memory**: Specify the memory required per node in the correct format (e.g., `4G` for 4 GB).

If you select the `gpu-interactive` partition, you will have the option to choose the type of GPU needed. This mode automatically submits the job to the scheduler and allocates the resources.

::::{dropdown} Interactive Mode Example
:::{code-block} bash
[rc.computing@login-00 ~]$ job-assist
SLURM Menu:
1. Default mode (srun --pty /bin/bash)
2. Interactive Mode
3. Batch Mode
4. Exit
Enter your option: 2
Partitions:
debug express short gpu-interactive
Enter partition name: short
Maximum number of nodes available for short is 2
Enter number of nodes (1-2): 1
Enter number of tasks: 2
Enter number of cpus per task: 4
Maximum time for short partition is 24:00:00
Enter time(HH:MM:SS): 01:00:00
Enter memory required per node (<size>[units]): 4G
Running command: srun --partition=short --nodes=1 --ntasks=2 --cpus-per-task=4 --time=01:00:00 --mem=4G --pty /bin/bash
srun: job 43911332 queued and waiting for resources
srun: job 43911332 has been allocated resources
[rc.computing@d1019 ~]$
:::
::::

:::{note}
For Default and Interactive Modes, once the resources are allocated, the job will transition from the login node (`login-00`) to a compute node (e.g., `d1019`).
:::


### Batch Mode

This mode allows you to create and save an `sbatch` script with your specific requirements. By default, it will save the batch script in the `/home` directory. If prompted for a specific directory, it will save it in the location you specify.

::::{dropdown} Batch Mode Example
:::{code-block} bash
[rc.computing@login-00 ~]$ job-assist
SLURM Menu:
1. Default mode (srun --pty /bin/bash)
2. Interactive Mode
3. Batch Mode
4. Exit
Enter your option: 3
Partitions:
debug express short gpu
Enter partition name: debug
Enter number of nodes: 2
Enter number of tasks: 4
Enter number of cpus per task: 4
Maximum time for debug partition is 00:20:00
Enter time(HH:MM:SS): 00:20:00
Enter memory required per node (<size>[units]): 32M
Do you want to specify a directory to save the batch script [Defaults to home]? (y/n): n
Enter the filename for the batch script without any extension: batch-mode
Batch script saved to /home/<user-name>/batch-mode.sh
[rc.computing@login-00 ~]$
:::
::::

**To view the content of the batch script:**

:::{code-block} bash
nano /home/<user-name>/batch-mode.sh
#Replace <user-name> with your actual username in the path
:::

This creates a basic structure for the batch script to interpret with SLURM. You can edit it to add software, environment modules, and programs to execute.

:::{tip}
**Efficient Resource Usage**: Requesting only the resources you need (e.g., nodes, memory, CPUs) can help your job start sooner. Be mindful that requesting more CPUs or longer run times may result in longer queue times.
:::
