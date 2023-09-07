(slurm-best-practices)=
# Slurm Best Practices

Slurm is the nerve center of many High-Performance Computing (HPC) clusters. Understanding it well is not optional; it's a requirement for effective computational research or tasks. This guide outlines how to navigate Slurm as a user.

(slurm-best-practices-job-submission)=
## Job Submission

(slurm-best-practices-batch-interactive-jobs)=
### Interactive and Batch Jobs
- **Batch Jobs**: Use ``sbatch`` for long-running jobs. Create an sbatch script specifying resources and runtime parameters.
- **Interactive Jobs**: For testing or debugging, use ``srun`` or ``salloc``.

(slurm-best-practices-sbatch)=
#### Sbatch Scripts

:::{code} bash
#!/bin/bash
#SBATCH --job-name=example_job
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=2-00:00:00

# commands to execute
:::

The above script is a template. Modify the directives according to your needs.

(slurm-best-practices-optimization)=
## Optimizing Resource Usage

(slurm-best-practices-requirements)=
### Specify Exact Requirements
- Use ``--cpus-per-task`` to specify the exact number of CPU cores your job requires.
- Allocate only the memory you need using ``--mem``.
Make sure to check the amount of resources you are allowed to use for a given partition.

(slurm-best-practices-monitoring-jobs)=
## Monitoring Jobs

(slurm-best-practices-job-status)=
### Job Status
- ``squeue``: Shows the status of your submitted jobs.
- ``sacct``: Provides account information after job completion, good for diagnosing problems.

(slurm-best-real-time-monitoring)=
### Real-Time Monitoring
- ``sstat``: This is your real-time dashboard for jobs, showing you CPU, memory, and IO metrics.

(slurm-best-practices-troubleshooting)=
## Troubleshooting

(slurm-best-practices-job-priority)=
### Job Priority
- ``sprio``: Use this to understand the priority of your pending jobs and why they might be queued.

(slurm-best-practices-logs)=
### Logs

- Each Slurm job generates logs. Know how to access and interpret them.

(slurm-best-practices-data-management)=
## Data Management

(slurm-best-practices-input-output)=
### Input and Output
- Use ``--input`` and ``--output`` directives in your sbatch script to handle data.

(slurm-best-practices-staging)=
### Staging
- Utilize tools like ``rsync`` to move data to and from the cluster efficiently. Be mindful of disk quotas.
