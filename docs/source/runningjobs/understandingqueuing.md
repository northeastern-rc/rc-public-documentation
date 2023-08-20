(understanding-queuing)=
# Understanding the Queuing System

The queuing system in a high-performance computing (HPC) environment manages and schedules computing tasks. Our HPC cluster uses the Slurm Workload Manager as our queuing system. This section aims to help you understand how the queuing system works and how to interact effectively.

## Introduction to Queuing Systems

The Slurm scheduler manages jobs in the queue. When you submit a job, it gets placed in the queue. The scheduler then assigns resources to the job when they become available, according to the job's priority and the available resources.

## Job Submission and Scheduling

Jobs are submitted to the queue via a script specifying the resources required (e.g., number of CPUs, memory, and GPUs) and the commands to be executed. Once submitted, the queuing system schedules the job based on the resources requested, the current system load, and scheduling policies.

## Scheduling Policies**

Our cluster uses a fair-share scheduling policy. This means that usage is tracked for each user or group, and the system attempts to balance resource allocation over time. If a user or group has been using many resources, their job priority may be temporarily reduced to allow others to use the system. Conversely, users or groups that have used fewer resources will have their jobs prioritized.

The following policies ensure fair use of the cluster resources:

- **Single job size**: The maximum number of nodes a single job can request is **XX**.
- **Run time limit**: The maximum run time for a job is **XX** hours.
- **Priority decay**: If a job remains in the queue without running for an extended period, its priority may slowly decrease.

## Job Priority**

Several factors determine job priority:

- **Fairshare**: This is based on the historical resource usage of your group. The more resources your group has used, the lower your job's priority becomes, and vice versa.
- **Job size**: Smaller jobs (regarding requested nodes) typically have higher priority.
- **Queue wait time**: The longer a job has been in the queue, the higher its priority becomes.

## Job States

Each job in the queue has a state. The main job states are:

- Pending (PD): The job is waiting for resources to become available.
- Running (R): The job is currently running.
- Completed (CG): The job has been completed successfully.

A complete list of job states can be found in the Slurm documentation.

## Monitoring the Queue**

You can use the following commands to interact with the queue:

- `squeue`: Displays the state of jobs or job steps. It has a wide variety of filtering, sorting, and formatting options. For example, to display your jobs:

:::{code} bash
squeue -u your_username
:::

- `scontrol`: Used to view and modify Slurm configuration and state. For example, to show the details of a specific job:

:::{code} bash
scontrol show job your_job_id
:::

## Tips for Efficient Queue Usage**

- Request only the resources you need: Overestimating your job's requirements can result in longer queue times.
- Break up large jobs: Large jobs tend to wait in the queue longer than small jobs. Break up large jobs into smaller ones.
- Use idle resources: Sometimes, idle resources can be used. If your job is flexible regarding start time and duration, you can use the `--begin` and `--time` options to take advantage of these idle resources.
