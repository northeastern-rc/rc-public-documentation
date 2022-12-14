.. _partition_names:

**********
Low priority partition FAQs
**********
:sub:`Updated November 2022`

Partition information
===================

**1. What is the** ``lowpriority`` **partition and why is it important?**

``lowpriority`` is a new partition on Discovery that allows the research community to use **private resources** on 
the cluster when they are idle. This new partition has hardware not otherwise available to the general research 
community and, in time, could double the resources available to NURC users. This is a common practice in HPC clusters 
to optimize the use of idle private resources that consume power and cooling. 

More information about the low priority partition and examples on how to use it can be 
found `here <https://northeastern-university-rc-public-documentation--19.com.readthedocs.build/en/19/hardware/lowpriority.html>`_. 

**2. What is a "low priority" job?**

A job submitted to the ``lowpriority`` partition that comes from a user **who is NOT** a member of the private 
partition on which the job is scheduled to run.

**3. What is a “high priority” job?**

A job submitted to a private partition by a user **who is** a member of that private partition, on which a low 
priority job is running.

**4. How does SLURM handle low priority jobs?**

In SLURM, jobs are submitted to partitions. SLURM is configured such that jobs submitted to the ``lowpriority`` 
partition are considered for execution on private partitions only when the requested job resources are idle. 

In other words, a low priority job will be executed only if the private partition has resources to execute a 
job submitted to it. However, if a member of the private partition submits a job during this time, then the low 
priority job will be automatically stopped/suspended and re-queued (preempted). 

Jobs submitted to the ``lowpriority`` partition have the lowest priority of any class of jobs and are only considered 
after all other high priority jobs have been placed. Jobs submitted by private partition members to their own 
partition always have higher priority. 

**5. Will the** ``lowpriority`` **partition become the default partition?**

No, the default partition will still be the ``short`` partition. This ensures that by default, jobs are not subject to preemption.

**6. How do I submit a job to the** ``lowpriority`` **partition?**

The ``lowpriority`` partition is a distinct partition that must be requested explicitly. SLURM accepts a 
comma-separated list of partitions. If a job is scheduled to run in the ``lowpriority`` partition, it may be 
preempted and re-queued. This does not happen in other partitions. The ``lowpriority`` partition is the only partition 
that can be preempted. See examples `here <https://northeastern-university-rc-public-documentation--19.com.readthedocs.build/en/19/hardware/lowpriority.html>`_.

**7. How can I ensure that my** ``lowpriority`` **partition job can run on nodes with sufficient resources?**

It is important to specify the required resources in the job script, including memory, CPUs and GPUs. For CPUs, this can include the number of cores 
and the micro-architecture and for GPUs this is typically handled by “class”. The GPU classes that are configured on 
the HPC system include P100, V100, T4, and A100. See our documentation on `using slurm <https://rc-docs.northeastern.edu/en/latest/using-discovery/usingslurm.html>`_ and 
`working with GPUs <https://rc-docs.northeastern.edu/en/latest/using-discovery/workingwithgpu.html#working-gpus>`_ for additional information.

**8. What is the downside of submitting a job to the** ``lowpriority`` **partition?**

If a job is submitted to the ``lowpriority`` partition and a high priority job comes through that requires resources 
currently occupied by the low priority job, then that low priority job will be stopped/suspended within 30s and 
re-queued. 

**9. When should I NOT use the** ``lowpriority`` **partition to run my jobs?**

Jobs running on the ``lowpriority`` partition always carry the risk of being suspended before their wall time ends 
if a high priority job requests those resources while the low priority job is running. If you have 
`checkpointing <https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html>`_ implemented in your 
workflow, such abrupt suspension of jobs would not be an issue, since your intermediate calculations/data are saved, 
and you can re-start your jobs from the point of their suspension. However, if you do not have checkpointing 
techniques implemented, and/or you expect your jobs to run for a while (and re-running them in the event of 
preemption means it is going to start all over again and take even longer to complete), it is not ideal to use 
the ``lowpriority`` partition. 

Resources
===================

**1. What are the time limits on the** ``lowpriority`` **partition?**

Partition limits for the ``lowpriority`` partition are the same as the default partition (``short``), which has a 4h 
default walltime and a 24h max-walltime.

**2. What are the resource and job limits on the** ``lowpriority`` **partition?**

Currently, the resource limits and the number for CPU-supported low priority jobs on the ``lowpriority`` partition 
are the same as the `default partition <https://rc-docs.northeastern.edu/en/latest/hardware/partitions.html>`_. The 
resource limits and the number for GPU-supported low priority jobs on the ``lowpriority`` partition are the same as 
the `gpu partition <https://rc-docs.northeastern.edu/en/latest/hardware/partitions.html>`_.

**3. Is there a limit on the number of CPUs or GPUs that can be requested when trying to use the** ``lowpriority`` **partition?**

The maximum limit for number of CPUs, GPUs, job time etc. will be the same as that on the ``short`` and ``gpu`` partitions. 
Please check our `partitions <https://rc-docs.northeastern.edu/en/latest/hardware/partitions.html>`_ page for the 
core and RAM limits on these partition. 

**4. I am an owner of a private partition, will this affect my group’s job wait time?**

As a PI who purchased your own equipment, jobs submitted by the members of your private partition to your own 
resources always have the highest priority. When submitting jobs to your private partition, any low priority jobs 
currently running on your servers will be killed and sent back to the queue, introducing a slight delay (~30s) on 
the first job submitted. This new service is designed to favor partition owners heavily.

**5. Will the** ``lowpriority`` **partition affect the limits on my own server(s)?**

The ``lowpriority`` partition will not affect current partition definitions — it is just an additional partition. As 
is true now, PIs will be able to request their private partitions be configured according to their research 
requirements. 

**6. Will the software that my group uses exclusively on our server(s) be available on other servers?**

Yes, all software used in the private partitions is available on all servers. Software that is restricted to a 
particular group’s license will remain restricted to members of that group, but they will be able to use that 
software on any server. 

**7. What hardware will be part of the** ``lowpriority`` **partition?**

All PI-owned hardware purchased on or after 2019 will be part of the ``lowpriority`` partition.

**8. Do you have a clear inventory of the various resources available through the** ``lowpriority`` **partition?**

Throughout the testing phase, RC will be updating its `technical documentation <https://northeastern-university-rc-public-documentation--19.com.readthedocs.build/en/19/hardware/lowpriority.html>`_ 
to reflect the resources that are part of public and private partitions. Please check the `documentation <https://northeastern-university-rc-public-documentation--19.com.readthedocs.build/en/19/hardware/lowpriority.html>`_ regularly for latest information. 
See our `CPUs <https://rc-docs.northeastern.edu/en/latest/hardware/hardware_overview.html>`_ and `GPUs <https://rc-docs.northeastern.edu/en/latest/using-discovery/workingwithgpu.html#working-gpus>`_ pages.

Preemption
===================

**1. What does 'preemption' or 'preemptable job' mean?**

In SLURM terminology, preemption is a scheduling mechanism that involves stopping/suspending one or more 
low priority jobs, to accommodate a high priority job (i.e. job submitted by the partition owner’s group member). 
A low priority job that can get suspended in this manner is also known as a ‘preemptable’ job. Preemptable jobs 
can run on private hardware owned by other research groups, with the potential risk of being suspended before their 
wall time ends if the private partition’s group member submits a job and requests for resources. 

**2. What do I need to know about preemption and are there any drawbacks for my research group?**

**For private partition owners:** 
When low priority jobs are running on your hardware, you may experience a slight delay (~30s) when submitting your 
first job to your private partition. This is the time it will take the scheduler to kill/preempt low priority jobs 
running on your partition. This new service is designed to minimize that delay.

**For users of the** ``lowpriority`` **partition:** 
Submitting jobs to this partition will make your jobs preemptable. That means they may be stopped/suspended and 
re-queued at any time. We recommend that you use strategies such as 
`checkpointing <https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html>`_ to take full advantage 
of the ``lowpriority`` partition. RC is working on `detailed documentation <https://northeastern-university-rc-public-documentation--19.com.readthedocs.build/en/19/hardware/lowpriority.html>`_
and training sessions that will be available later in the Fall 2022 semester, once the service is ready to be released.

**3. How does re-queuing of preempted (stopped/suspended) low priority jobs work?**

Preempted jobs are put back in the default partition queue (``short``) and scheduled normally.

**4. My servers are being used by others, how fast can we retrieve them?**

As a private partition owner you will always have the highest priority when accessing your own resources. When 
submitting jobs to your private partition, any low priority jobs currently running on your servers will be killed 
and sent back to the queue. You will retrieve your server(s) within approximately 30s.

**5. I already have access to one or more of the large, long, and/or multigpu partition(s), do I benefit from 
using the ``lowpriority`` partition?**

The goal of ``lowpriority`` partition is to double the resources available to Discovery users. Hence, specifying 
the ``lowpriority`` partition in your SLURM job header gives your job a higher chance of being allocated resources, 
even when your first choice of partition is unavailable. For e.g., when you specify 
``#SBATCH --partition=short,lowpriority``, your job can start running on the ``lowpriority`` partition even when ``short`` 
is unavailable. 

RC policy
===================

**1. Can I opt-out?**

We would prefer if you did not. Opening up idle private resources that consume power and cooling makes the cluster 
more useful for everyone (including you). This is a common practice in HPC implemented by many other universities and 
national labs. Also, all private hardware purchases that were placed since 2019 came with the explicit understanding 
that they would be added to the ``lowpriority`` partition when it became available (see below).  

**2. What is the understanding between RC and private partition owners?**

The following understanding applies to all individual private partition owners who purchased servers hosted at MGHPCC since 2019:

RC racks, installs and maintains privately owned servers; RC purchases the equipment needed to connect these servers 
to the infiniband network fabric; RC pays for power and cooling to operate the servers during their entire lifetime; 
In return, private partition owners make their servers available to the ``lowpriority`` partition.

**3. Are there policies or other formal documents available?**

RC is currently drafting a memorandum of understanding (MoU) that will be distributed to all private partitions 
owners later in the Fall semester 2022. This document will formalize the understanding that was stated to all 
private partitions owners at the time of purchase, since 2019. Moreover, RC is working on a detailed set of 
documentation, service level objectives and training sessions that will be available later in the Fall 2022 semester, 
once the service is ready to be released.

**4. I have resources I would like to make available to the rest of the research community, what can I do?**

All hardware purchased on or after 2019 will be part of the ``lowpriority`` partition. Feel free to contact us if you 
purchased hardware before 2019 and would like to make it available to the ``lowpriority`` partition.

**5. Why should I make my private resources available to the rest of the research community?**

By making your private resources available to others through the ``lowpriority`` partition, you will allow the 
Northeastern research community to use them when they are idle. This, in time, could double the resources available 
to NURC users and is a common practice in HPC clusters to optimize the use of idle private resources that consume 
power and cooling. 


Testing and release
===================

**1. Will there be a testing and review phase?**

We are currently looking for PIs who own private hardware and would like to be part of our testing phase. Once the 
testing phase is over RC will present the finalized service to the RCAC and all private partition owners for review. 

**2. What is the timeline of the testing phase?**

The ``lowpriority`` partition will be available for testing after the October maintenance window (October 4, 2022). 
Only groups who opt in will have access to the ``lowpriority`` partition during the testing phase and only hardware 
owned by those groups will be part of the test partition.

**3. How can I participate in the testing phase?**

Let us know by sending an email to rchelp@northeastern.edu with the subject “lowpriority partition”. Members of your 
group will get first access to all newly opened resources for the duration of the testing phase. Only hardware owned 
by PIs who opt-in will be part of the testing phase.

**4. When will the** ``lowpriority`` **partition be officially released?**

Once testing, configuration, and documentation are complete, we will schedule an additional rollout of 
the ``lowpriority`` partition and provide access to all users of the HPC cluster. We anticipate this to 
be in **late 2022/early 2023**. 

Miscellaneous
===================

**1.Where can I learn more about the** ``lowpriority`` **partition?**

RC is working on a `detailed set of documentation <https://northeastern-university-rc-public-documentation--19.com.readthedocs.build/en/19/hardware/lowpriority.html>`_, 
service level objectives, and training sessions that will be available later in the Fall 2022 semester, once the 
service is ready to be released.

**2. Are there tools or resources available to help me better use and understand the ``lowpriority`` partition?**

Use `checkpointing <https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html>`_ to take full 
advantage of the ``lowpriority`` partition. RC is working on a detailed set of documentation and training sessions 
that will be available later in the Fall 2022 semester to coincide with the release of this new service.

**3. I have additional questions that are not addressed in the FAQs, what do I do?**

Kindly send your questions to `rchelp@northeastern.edu <mailto:rchelp@northeastern.edu>`_ or schedule a consultation 
with us `here <https://rc.northeastern.edu/support/consulting/>`_.