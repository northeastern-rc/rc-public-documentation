(slurm-guide-index)=
# Slurm

```{toctree}
:hidden:
:maxdepth: 3

slurmcommands
slurmrunningjobs
slurmmonitoringandmanaging
slurmarray
```

Slurm (Simple Linux Utility for Resource Management) is an open-source, highly configurable, fault-tolerant, and adaptable workload manager. It is extensively used across High-Performance Computing (HPC) environments.

Slurm is designed to accommodate the complex needs of large-scale computational workloads. It can efficiently distribute and manage tasks across clusters comprising thousands of nodes, offering seamless control over resources, scheduling, and job queuing.
It is the software on the HPC that provides functionalities such as {ref}`slurm-arrays`, {ref}`slurm-monitoring-and-managing`, and check the {ref}`cluster-and-node-states`.

::::{grid} 3
:::{grid-item-card} {ref}`slurm-commands`
Basic Slurm commands used for running, monitoring, and canceling jobs.
:::
:::{grid-item-card} {ref}`slurm-running-jobs`
Advanced usage and explanation of `srun` and `sbatch` for running jobs.
:::
:::{grid-item-card} {ref}`slurm-monitoring-and-managing`
Advanced usage and explanation of `squeue`, `scontrol`, and `sinfo` for monitoring jobs.
:::
:::{grid-item-card} {ref}`slurm-arrays`
An introduction and use cases for Slurm job arrays for launching a large series of jobs.
:::
::::
