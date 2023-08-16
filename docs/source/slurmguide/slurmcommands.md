(slurm-commands)=
# Slurm Commands

## Running Jobs on the HPC

### `srun`

### `sbatch`

To submit your job script to Slurm, you use the `sbatch` command:

:::{code} bash
sbatch job_script.sh
:::

## Monitoring and Canceling Jobs

### `squeue`

Slurm will then schedule your job to run when resources are available. It returns a job ID that you can use to monitor your job's status.

To check the status of your job, you use the `squeue` command:

:::{code} bash
squeue -u  <username>
:::

### `scancel`

To cancel a job, you use the `scancel` command with the job ID:

:::{code} bash
scancel  <job_id>
:::

## Information on Partitions, Jobs, and Job Efficiency

### `sinfo`

To view cluster information, use `sinfo`: this command allows to view partition and node information. Use option -a to view all partitions.
:::{code} bash
sinfo <options>
:::

### `scontrol`

To check detailed information about a job, use the `scontrol` command:
:::{code} bash
scontrol show job  <job_id>
:::

This information is crucial for managing your jobs and ensuring they are running as expected.

### `seff`