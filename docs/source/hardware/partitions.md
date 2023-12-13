(partition-names)=

# Partitions

A {term}`partition` is a logical collections of nodes that comprise different hardware resources and limits to help meet the wide variety of jobs that get scheduled on the cluster. Occasionally, the Research Computing team might need to make updates to the partitions based on monitoring job submissions to help reduce job wait times. As our cluster grows, changes to the partitions also help to ensure the fair, efficient distribution of resources for all jobs being submitted to the cluster.

On Discovery, there are several partitions:

- General access (`debug`, `express`, `short`, `gpu`)
- Application only (`long`, `large`, `multigpu`)
- PI owned (accessed only by members of the PIs’ group)

:::{note}
PI-owned partitions only include the hardware that those PIs own and are only accessible to the members of the PI's group.
:::

The general access and application only partitions span the hardware on the cluster, with `gpu` and `multigpu` spanning the GPUs on the cluster and the other partitions spanning the CPUs. For example, if you use the `debug` partition you are using the same hardware as `short`, just with different time, job, and core limits. Refer to the tables below for detailed information on the current partitions. 

:::{note}
In the following table, the `Running Jobs Per User/Per Research Group`, Core and RAM limits are set per user, across all running jobs (not pending). **Keep in mind that the number of running jobs is limited by the available resources on the cluster at the time of the job submission and may not adhere to the number stated below.**

It is possible for you to see the message below in the output of `squeue -u $USER`, even though you submitted fewer jobs than the number of submitted jobs indicated in the table. This implies that Slurm has reached the hard-coded limit of 10,000 total jobs/per account at that time. Here the account refers to the Slurm account that you, as a cluster user, is associated with. So you will continue to receive this error message until some of your jobs start running and/or get completed before you can submit more jobs.

*job violates accounting/QOS policy*
:::

:::{list-table}
---
header-rows: 1
---
* - Name
  - Requires approval?
  - Time limit (default/max)
  - Running jobs
  - Submitted jobs
  - Core limit (per user)
  - RAM limit
  - Use Case
* - debug
  - No
  - 20 minutes/20 minutes
  - 10/25
  - 5000
  - 128
  - 256GB
  - Best for serial and parallel jobs that can run under 20 minutes. Good for testing code.
* - express
  - No
  - 30 minutes/60 minutes
  - 50/250
  - 5000
  - 2048
  - 25TB
  - Best for serial and parallel jobs that can run under 60 minutes.
* - short
  - No
  - 4 hours/24 Hours
  - 50/500
  - 5000
  - 1024
  - 25TB
  - Best for serial or small parallel jobs (``--nodes=2`` max) that need to run for up to 24 hours.
* - long
  - **Yes**
  - 1 day/5 Days
  - 25/250
  - 1000 per user/5000 per group
  - 1024
  - 25TB
  - Primarily for serial or parallel jobs that need to run for more than 24 hours. Need to prove that your code cannot checkpoint to use this partition.
* - large
  - **Yes**
  - 6 hours/6 Hours
  - 100/100
  - 1000 per user/5000 per group
  - N/A
  - N/A
  - Primarily for running parallel jobs that can efficiently use more than 2 nodes. Need to demonstrate that your code is optimized for running on more than 2 nodes.
:::

---

:::{list-table}
---
widths: 20 20 20 20 30 20 20 30
header-rows: 1
---
* - Name
  - Requires approval?
  - Time limit (default/max)
  - Running jobs
  - Submitted jobs
  - GPU limit
  - GPU limit
  - Use Case
* - `gpu`
  - No
  - 4 hours/8 Hours
  - 25/250
  - 50/100
  - 1
  - 8
  - For jobs that can run on a single GPU processor.
* - `multigpu`
  - **Yes**
  - 4 hours/24 Hours
  - 25/100
  - 50/100
  - 12
  - 12
  - For jobs that require more than one GPU and take up to 24 hours to run.
:::

## Viewing partition information

Slurm commands allow you to view information about the partitions. Three commands that can show you partition information are `sinfo`, `sacct`, and `scontrol`. The following are common options to use with these commands:

:::{code} shell
sinfo -p <partition name> #displays the state of the nodes on a specific partition
sinfo -p <partition name> --Format=time,nodes,cpus,socketcorethread,memory,nodeai,features #displays more detailed information using the Format option, including features like the type of processors
sacct --partition <partition name> #displays the jobs that have been run on this partition
scontrol show partition <partition name> #displays the Slurm configuration of the partition
:::

For more information about these commands, see our [Using Slurm] and the official [Slurm documentation].

## Allocating partitions in your jobs

To specify a partition when running jobs, use the option `--partition=<partition name>` with either `srun` or `sbatch`. When using a partition with your job and specifying the options of `--nodes=` and `--ntasks=` and/or `--cpus-per-task=`, make sure that you are requesting options that best fit your job. It can actually have the opposite effect on jobs that are better suited to running with smaller requirements, as you have to wait for the extra resources that your job will not use. See {ref}`using-slurm` for more information on using Slurm to run jobs.

:::{note}
Requesting the maximum number of nodes or tasks will not make your job run faster or give you higher priority in the job queue.
:::

:::{tip}
You should always try to have job requests that will attempt to allocate the best resources for the job you want to run. For example, if you are running a job that is not parallelized, you only need to request one node (`--nodes=1`). For some parallel jobs, such as a small MPI job, you can also use one node (`--nodes=1`) with the `–-ntasks=` option set to correspond to the number of MPI ranks (tasks) in your code. For example, for a job that has 12 MPI ranks, request 1 node and 12 tasks within that node (`--nodes=1 –-ntasks=12`). If you request 12 nodes, Slurm is going to run code between those nodes, which could slow your job down significantly if it is not optimized to run between nodes.

If your code is optimized to run on more than two nodes and needs less than one hour to run, you can use the `express` partition. If your code needs to run on more than 2 nodes for more than one hour, you should apply to use the `large` partition. See the section Partition Access Request below for more information.
:::

(partition-access)=

## Partition Access Request

If you need access to the `large`, `long`, or `multigpu` partition, you need to submit a [ServiceNow ticket]. Access is not automatically granted. You will need to provide details and test results that demonstrate your need for access for these partitions. If you need temporary access to `multigpu` to perform testing before applying for permanent access, you should also submit a [ServiceNow ticket]. All requests are evaluated by members of the RC team. Once reviewed and approved, you will be added to have access to that partition.

[ServiceNow ticket]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7
[Slurm documentation]: https://slurm.schedmd.com/
[Using Slurm]: https://rc-docs.northeastern.edu/en/latest/using-discovery/slurm.html
