(understanding-queuing)=
# Understanding the Queuing System

The queuing system in a high-performance computing (HPC) environment manages and schedules computing tasks. Our HPC cluster uses the Slurm Workload Manager as our queuing system. This section aims to help you understand how the queuing system works and how to interact with it effectively.

When you submit a job via the commands `srun` or `sbatch`, it gets placed in the queue. The scheduler then assigns the resources you requested (e.g., number of CPUs, memory, and GPUs) to the job when they become available, according to the job's priority and the available resources.

## Scheduling Policies

Our cluster uses a fair-share scheduling policy. This means that usage is tracked for each user or group, and the system attempts to balance resource allocation over time. If a user or group has been using many resources, their job priority may be temporarily reduced to allow others to use the system. Conversely, users or groups that have used fewer resources will have their jobs prioritized.

Several factors determine job priority:

- **Fairshare**: This is based on the historical resource usage of your group. The more resources your group has used, the lower your job's priority becomes, and vice versa.
- **Job size**: Smaller jobs (regarding requested nodes) typically have higher priority.
- **Queue wait time**: The longer a job has been in the queue, the higher its priority becomes.

:::{important}
1) Request only the resources you need: Overestimating your job's requirements can result in longer queue times. See {ref}`seff` to learn about viewing historical job resource utilization.
2) Break up large jobs: Large jobs tend to wait in the queue longer than small jobs. Break up large jobs into smaller ones.
:::
