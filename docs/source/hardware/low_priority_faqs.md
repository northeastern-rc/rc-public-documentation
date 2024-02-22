(low-priority-faqs)=

# Low Priority Partition FAQs

## Partition Information

::::{dropdown} 1. What is the `lowpriority` partition and why is it important?
`lowpriority` is a new partition on Discovery that allows the research community to use **private resources** on the cluster when they are idle. This new partition has hardware not otherwise available to the general research community and, in time, could double the resources available to NURC users. This is a common practice in HPC clusters to optimize the use of idle private resources that consume power and cooling. 

More information about the low priority partition and examples on how to use it can be 
found {ref}`low-priority`.
::::

::::{dropdown} 2. What is a "low priority" job?
A job submitted to the `lowpriority` partition that comes from a user **who is NOT** a member of the private partition on which the job is scheduled to run.

A "low priority" job will be terminated from the `lowpriority` partition and re-queued if a member of the private partition submits a job to the private partition.
::::

::::{dropdown} 3. What is a “high priority” job?
A job submitted to a private partition by a user **who is** a member of that private partition, on which a low priority job is running.
::::

::::{dropdown} 4. How does SLURM handle low priority jobs?
In SLURM, jobs are submitted to partitions. SLURM is configured such that jobs submitted to the `lowpriority`partition are considered for execution on private partitions only when the requested job resources are idle.

In other words, a low priority job will be executed only if the private partition has resources to execute a job submitted to it. However, if a member of the private partition submits a job during this time, then the low priority job will be automatically terminated and re-queued (preempted). See {reF}`low-priority-preemption`.

Jobs submitted to the `lowpriority` partition have the lowest priority of any class of jobs and are only considered after all other high priority jobs have been placed. Jobs submitted by private partition members to their own partition always have higher priority.
::::

::::{dropdown} 5. Is the `lowpriority` partition default?
No, the default partition will still be the `short` partition. This ensures that by default, jobs are not subject to preemption.
::::

::::{dropdown} 6. How do I submit a job to the `lowpriority` partition?
The `lowpriority` partition is a distinct partition that must be requested explicitly. SLURM accepts a comma-separated list of partitions. If a job is scheduled to run in the `lowpriority` partition, it may be preempted and re-queued. This does not happen in other partitions. The `lowpriority` partition is the only partition that can be preempted. See examples in using {ref}`low-priority`.
::::

::::{dropdown} 7. How can I ensure that my `lowpriority` partition job can run on nodes with sufficient resources?
It is important to specify the required resources in the job script, including memory, CPUs and GPUs. For CPUs, this can include the number of cores and the micro-architecture and for GPUs this is typically handled by “class”. The GPU classes that are configured on the HPC system include P100, V100, T4, and A100. See our documentation on {ref}`slurm-guide-index` and {ref}`working-gpus` for additional information.
::::

::::{dropdown} 8. What is the downside of submitting a job to the `lowpriority` partition?
If a job is submitted to the `lowpriority` partition and a high priority job comes through that requires resources currently occupied by the low priority job, then that low priority job will be stopped/suspended within 30s and re-queued. 
::::

::::{dropdown} 9. When should I NOT use the `lowpriority` partition to run my jobs?
Jobs running on the `lowpriority` partition always carry the risk of being suspended before their wall time ends if a high priority job requests those resources while the low priority job is running. If you have checkpointing (see {ref}`checkpoint-jobs`) implemented in your workflow, such abrupt suspension of jobs would not be an issue, since your intermediate calculations/data are saved, and you can re-start your jobs from the point of their suspension. However, if you do not have checkpointing techniques implemented, and/or you expect your jobs to run for a while (and re-running them in the event of preemption means it is going to start all over again and take even longer to complete), it is not ideal to use the `lowpriority` partition. 
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::
## Resources

::::{dropdown} 1. What are the time limits on the `lowpriority` partition?
Partition limits for the `lowpriority` partition are the same as the default partition (`short`), which has a 4h default walltime and a 24h max-walltime.
::::

::::{dropdown} 2. What are the resource and job limits on the `lowpriority` partition?
Currently, the resource limits and the number for CPU-supported low priority jobs on the `lowpriority` partition are the same as the default partition (see {ref}`partition-names`). The resource limits and the number for GPU-supported low priority jobs on the `lowpriority` partition are the same as the gpu partition (see {ref}`partition-names`).
::::

::::{dropdown} 3. Is there a limit on the number of CPUs or GPUs that can be requested when trying to use the `lowpriority` partition?

The maximum limit for number of CPUs, GPUs, job time etc. will be the same as that on the `short` and `gpu` partitions. Please check our partitions (see {ref}`partition-names`) page for the core and RAM limits on these partition. 
::::

::::{dropdown} 4. I am an owner of a private partition, will this affect my group’s job wait time?
Jobs submitted by the members of your private partition to your privately owned resources always have the highest priority. When submitting jobs to your private partition, any low priority jobs currently running on your servers will be killed and sent back to the queue, introducing a slight delay (~30s) on the first job submitted. This new service is designed to favor partition owners heavily.
::::

::::{dropdown} 5. Will the `lowpriority` partition affect the limits on my own server(s)?
The `lowpriority` partition will not affect current partition definitions — it is an additional partition. As is true now, PIs will be able to request their private partitions be configured according to their research requirements. 
::::

::::{dropdown} 6. Will the software that my group uses exclusively on our server(s) be available on other servers?

Yes, all software used in the private partitions is available on all servers. Software that is restricted to a particular group’s license will remain restricted to members of that group, but they will be able to use that software on any server. 
::::

::::{dropdown} 7. What hardware will be part of the `lowpriority` partition?
All PI-owned hardware purchased on or after 2019 will be part of the `lowpriority` partition.
::::

::::{dropdown} 8. Do you have a clear inventory of the various resources available through the `lowpriority` partition?

Throughout the testing phase, RC will be updating its `low priority` documentation (see {ref}`low-priority`)to reflect the resources that are part of public and private partitions. Please check the documentation (see {ref}`low-priority`) regularly for latest information. See our CPUs ({ref}`hardware-overview`) and GPUs ({ref}`working-gpus`) pages.
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::
(low-priority-preemption)=
## Preemption

::::{dropdown} 1. What does 'preemption' or 'preemptable job' mean?
In Slurm terminology, preemption is a scheduling mechanism that involves stopping/suspending one or more low priority jobs, to accommodate a high priority job. Preemptable jobs can run on private hardware owned by other research groups, with the potential risk of being suspended before their wall time ends if the private partition’s group member submits a job and requests for resources.
::::

::::{dropdown} 2. What do I need to know about preemption and are there any drawbacks for my research group?

**For private partition owners:** 
When low priority jobs are running on your hardware, you may experience a slight delay (~30s) when submitting your first job to your private partition while the scheduler preempts the low priority jobs running on your partition. This new service is designed to minimize that delay.

**For users of the** `lowpriority` **partition:** 
Submitting jobs to this partition will make your jobs preemptable, which means they may be stopped/suspended and re-queued at any time; {ref}`checkpoint-jobs`) can help you take full advantage of the {ref}`low-priority`.
::::

::::{dropdown} 3. How does re-queuing of preempted (terminated) low priority jobs work?
Preempted jobs are put into the default partition queue (`short`) and scheduled normally.
::::

::::{dropdown} 4. My servers are being used by others, how fast can we retrieve them?
As a private partition owner you will always have the highest priority when accessing your own resources. When submitting jobs to your private partition, any low priority jobs currently running on your servers will be preempted and sent back to the default (`short`) queue. You will retrieve your server(s) within approximately 30s.
::::

::::{dropdown} 5. I already have access to one or more of the large, long, and/or multigpu partition(s), do I benefit from using the `lowpriority` partition?

The goal of `lowpriority` partition is to double the resources available to Discovery users. Specifying the `lowpriority` partition in your Slurm job header gives your job a higher chance of being allocated resources when your first choice of partition is unavailable. For example, when you specify `#SBATCH --partition=short,lowpriority`, your job can start running on the `lowpriority` partition when `short` is unavailable. 
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## RC Policy

::::{dropdown} 1. Can I opt-out?
Opening up idle private resources that consume power and cooling makes the cluster more useful for everyone (including you). This is a common practice in HPC implemented by many other universities and national labs. Also, all private hardware purchases that were placed since 2019 came with the explicit understanding that they would be added to the `lowpriority` partition when it became available (see next question).

If your private resources have constraints (i.e., funding stipulations), please reach out to the RC team and we will remove your resources from the low priority partition.
::::

::::{dropdown} 2. What is the understanding between RC and private partition owners?
The following understanding applies to all individual private partition owners who purchased servers hosted at MGHPCC since 2019:

RC racks, installs and maintains privately owned servers; RC purchases the equipment needed to connect these servers to the infiniband network fabric; RC pays for power and cooling to operate the servers during their entire lifetime; In return, private partition owners make their servers available to the `lowpriority` partition.
::::

::::{dropdown} 3. I have resources I would like to make available to the rest of the research community, what can I do?

All hardware purchased on or after 2019 will be part of the `lowpriority` partition. Feel free to contact us if you purchased hardware before 2019 and would like to make it available to the `lowpriority` partition.
::::

::::{dropdown} 4. Why should I make my private resources available to the rest of the research community?

By making your private resources available to others through the `lowpriority` partition, you will allow the Northeastern research community to use them when they are idle. This, in time, could double the resources available to Northeastern researchers. This is a common practice in HPC clusters to optimize the use of idle private resources that consume power and cooling. 
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Testing and Release

::::{dropdown} 1. Will there be a testing and review phase?
We are currently looking for PIs who own private hardware and would like to be part of our testing phase. Once the testing phase is over RC will present the finalized service to the RCAC and all private partition owners for review.
::::

::::{dropdown} 2. What is the timeline of the testing phase?
The `lowpriority` partition will be available for testing in Fall 2023. Only groups who opt in will have access to the `lowpriority` partition during the testing phase and only hardware owned by those groups will be part of the test partition.
::::

::::{dropdown} 3. How can I participate in the testing phase?
Let us know by sending an email to [rchelp@northeastern.edu](mailto:rchelp%40northeastern.edu) with the subject “lowpriority partition”. Members of your group will get first access to all newly opened resources for the duration of the testing phase. Only hardware owned by PIs who opt-in will be part of the testing phase.
::::

::::{dropdown} 4. When will the `lowpriority` partition be officially released?
Once testing, configuration, and documentation are complete, we will schedule an additional rollout of the `lowpriority` partition and provide access to all users of the HPC cluster. We anticipate this to be in **late 2022/early 2023**. 
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::