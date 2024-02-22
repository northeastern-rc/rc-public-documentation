(slurm-guide-index)=
# Slurm

```{toctree}
:hidden:
:maxdepth: 3

introductiontoslurm
slurmcommands
slurmrunningjobs
slurmmonitoringandmanaging
slurmscripts
slurmarray
slurmbestpractices
```

Slurm (Simple Linux Utility for Resource Management) is an open-source, highly configurable, fault-tolerant, and adaptable workload manager. It is extensively used across High-Performance Computing (HPC) environments.

Slurm is designed to accommodate the complex needs of large-scale computational workloads. It can efficiently distribute and manage tasks across clusters comprising thousands of nodes, offering seamless control over resources, scheduling, and job queuing.
It is the software on the HPC that provides functionalities such as {ref}`slurm-arrays`, {ref}`slurm-monitoring-and-managing`, view {ref}`account-information`, and check the {ref}`cluster-and-node-states`.

(basic-slurm-usage-index)=
## Basic Slurm Usage

<!-- ::::{grid} 3
:::{grid-item-card} {ref}`slurm-commands`
This page provides the basic slurm commands used for running, monitoring, and canceling jobs.
:::
:::{grid-item-card} {ref}`slurm-running-jobs`
This page provides advanced usage and explanation of `srun` and `sbatch` for running jobs.
:::
:::{grid-item-card} {ref}`slurm-monitoring-and-managing`
This page provides advanced usage and explanation of `squeue`, `scontrol`, and `sinfo` for monitoring jobs.
:::
:::: -->

::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`browser;1.5em;screen-full` Slurm Commands
:link: slurmguide/slurmcommands
:link-type: doc

This page provides the basic slurm commands used for running, monitoring, and canceling jobs.

+++
[Learn more »](slurmguide/slurmcommands)
:::

:::{grid-item-card} {octicon}`video;1.5em;sd-mr-1` Slurm Running Jobs
:link: slurmguide/slurmrunningjobs
:link-type: doc

This page provides advanced usage and explanation of `srun` and `sbatch` for running jobs.

+++
[Learn more »](slurmguide/slurmrunningjobs)
:::

:::{grid-item-card} {octicon}`device-desktop;1.5em;sd-mr-1` Monitoring and Managing Jobs
:link: slurmguide/slurmmonitoringandmanaging
:link-type: doc

This page provides advanced usage and explanation of `squeue`, `scontrol`, and `sinfo` for monitoring jobs.

+++
[Learn more »](slurmguide/slurmmonitoringandmanaging)
:::

::::


## Advanced Slurm Usage

<!-- ::::{grid} 2
:::{grid-item-card} {ref}`slurm-arrays`
This page provides an introduction and use cases for slurm job arrays for launching a large series of jobs.
:::
:::{grid-item-card} {ref}`slurm-best-practices`
This page provides the best practices for slurm HPC usage when submitting jobs.
:::
:::: -->

::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`git-compare;1.5em;screen-full` Slurm Array Jobs and Dependencies
:link: slurmguide/slurmarray
:link-type: doc

This page provides an introduction and use cases for slurm job arrays for launching a large series of jobs.

+++
[Learn more »](slurmguide/slurmarray)
:::

:::{grid-item-card} {octicon}`checklist;1.5em;sd-mr-1` Slurm Best Practices
:link: slurmguide/slurmbestpractices
:link-type: doc

This page provides the best practices for slurm HPC usage when submitting jobs.

+++
[Learn more »](slurmguide/slurmbestpractices)
:::

::::