(using-slurm)=
# Introduction to Slurm

Slurm (Simple Linux Utility for Resource Management) is an open-source, highly configurable, fault-tolerant, and adaptable workload manager. It is extensively used across High-Performance Computing (HPC) environments.

Slurm is designed to accommodate the complex needs of large-scale computational workloads. It can efficiently distribute and manage tasks across clusters comprising thousands of nodes, offering seamless control over resources, scheduling, and job queuing.
It is the software on the HPC that provides functionalities such as {ref}`job-arrays`, {ref}`job-management`, view {ref}`account-information`, and check the {ref}`cluster-and-node-states`.

##  Slurm on HPC
HPC systems are designed to perform complex, computationally intensive tasks. For example, users can specify complex workflows of jobs where specific jobs depend on others, and Slurm will manage the scheduling and execution of these workflows. Efficiently managing these tasks and resources in such an environment is a daunting challenge. That's where Slurm comes into play.

Slurm allows users to submit their computational tasks as jobs to be scheduled on the cluster's compute nodes. Its role-based access control ensures proper resource allocation and job execution, preventing resource conflicts.

Slurm is crucial in research environments, where it ensures fair usage of resources among a multitude of users, helps optimize the workload for the available resources, and provides precise job accounting and statistics.

## Section Objective:
To understand the Slurm workload manage, which will allow you to properly leverage the HPC. It starts with the basics - the resources that Slurm manager. Then, useful Slurm features (e.g., job submission, monitoring, canceling, etc.) are mentioned with code examples. We discuss jobs that are both interactive (i.e., {ref}`using-srun`) and batch (i.e., {ref}`using-sbatch`), along with the slurm array variants (i.e., {ref}`job-arrays`). {ref}`advanced-usage`, {ref}`common-problems-slurm`, and {ref}`best-practices` are also covered.

## Who Should Use This Guide?
This guide is for HPC users: researchers intending to use Slurm-based clusters for their computation tasks, system administrators managing HPC environments, and even seasoned HPC users looking to brush up on their knowledge. It progresses from fundamental to advanced topics, making it a valuable resource for a broad audience.

## Slurm: Basic Concepts
Before we delve into using Slurm, it's essential to grasp some fundamental concepts related to its operation.

### Nodes
In the context of Slurm, a 'node' refers to a server within the HPC cluster. Each node possesses its resources, such as CPUs, memory, storage, and potentially GPUs. Slurm manages these nodes and allocates resources to the tasks.

(slurm-partitions)=
### Partition(s)
A 'partition' is a grouping of nodes. You can think of partitions as virtual clusters within your HPC system. They allow administrators to segregate the compute environment based on factors like job sizes, hardware type, or resource allocation policies.

:::{seealso}
Our {ref}`partition-names` documentation.
:::

(account-information)=
### Account information
When running a job with either `srun` or `sbatch`, if you have more than one account associated with your username, we recommend you use the `--account=` flag and specify the account that corresponds to the respective project.

To find out what account(s) your username is associated with, use the following command:

:::{code} bash
sacctmgr show associations user=<yourusername>
:::

After you have determined what accounts your username is associated with, if you have more than one account association, you can use the `account=` flag with your usual `srun` or `sbatch` commands.

### Jobs, Job Steps, and Job Arrays
A **job** in Slurm is a user-defined computational task that's submitted to the cluster for execution. Each job has one or more **job steps**, sub-tasks that are part of a larger job and can be executed in parallel or sequentially.

**Job arrays** are a series of similar jobs that differ only by the array index. They're especially useful when you want to execute the same application with different inputs.

### Tasks
Tasks are the individual processes that run within a job step. They could be single-threaded or multi-threaded and can run on one or more nodes.

## Slurm References
1. SchedMD. (2023). Slurm Workload Manager. [https://slurm.schedmd.com](https://slurm.schedmd.com/)
2. SchedMD. (2023). Slurm Quick Start User Guide. [https://slurm.schedmd.com/quickstart.html](https://slurm.schedmd.com/quickstart.html)
3. IBM. (2023). High Performance Computing For Dummies, IBM Limited Edition. [https://www.ibm.com/downloads/cas/WQDZWBYJ](https://www.ibm.com/downloads/cas/WQDZWBYJ)
Thank you for following along with this guide, and we wish you success in your HPC journey!

[Frequently Asked Questions]: https://slurm.schedmd.com/faq.html
[Sample Job Scripts]: https://github.com/SchedMD/slurm/tree/master/contribs
[Slurm Commands]: https://slurm.schedmd.com/quickstart_admin.html
[Slurm community page]: https://slurm.schedmd.com/community.html
[Slurm Options]: https://slurm.schedmd.com/sbatch.html
[Slurm Quick Start User Guide]: https://slurm.schedmd.com/quickstart.html
[Slurm Workload Manager Documentation]: https://slurm.schedmd.com/documentation.html
[High Performance Computing For Dummies, IBM Limited Edition]: https://www.ibm.com/downloads/cas/WQDZWBYJ
