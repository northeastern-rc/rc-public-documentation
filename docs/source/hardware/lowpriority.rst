
.. _partition_names:

**********
Low priority partition
**********
:sub:`Updated September, 2022`


Introduction
===================
``lowpriority`` is a new partition on Discovery that allows the research community to use private resources on the HPC cluster when they are idle. 
This new partition has hardware not otherwise available to the general research community and, in time, could double the resources available to NURC users. 
This is a common practice in HPC clusters to optimize the use of idle private resources that consume power and cooling. 

When to use the low priority partition
===================

From most to least-recommended scenarios:

1. Code that can be checkpointed
2. Jobs that fit on a single node
3. Jobs that require multiple nodes (eg, MPI)
4. When waiting is too hard

How to use the low priority partition
===================

To use the low priority partition, just add ``lowpriority`` (no space between 'low' and 'priority') to your partition list. As the partition list is a 
comma-delimited list of values, it will need to be specified as ``srun --partition=short,lowpriority``. For this example, 
we will exclude partition ``short`` and focus on ``lowpriority``. When you run the ``squeue`` command, you can see 
that your job has been assigned to the low priority partition::

  $ srun -p lowpriority --pty /bin/bash
  srun: job 23498584 queued and waiting for resources
  srun: job 23498584 has been allocated resources

  $ squeue -u m.joshi
  JOBID      PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
  23498592        ctbp     bash  m.joshi  R       0:07      1 d3110
  23498584 lowpriority     bash  m.joshi  R       2:19      1 d3110

For the example provided on our `checkpointing <https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html?highlight=array#gromacs-checkpointing-example>`_ page, you can use the low priority partition as::

 #!/bin/bash
 #SBATCH --partition=short,lowpriority
 #SBATCH --constraint=cascadelake
 #SBATCH --nodes=1
 #SBATCH --time=12:00:00
 #SBATCH --job-name=myrun
 #SBATCH --ntasks=56
 #SBATCH --array=1-10%1  #execute 10 array jobs, 1 at a time.
 #SBATCH --output=myrun-%A_%a.out
 #SBATCH --error=myrun-%A_%a.err
 
 module load cuda/10.2
 module load gcc/7.3.0
 module load openmpi/4.0.5-skylake-gcc7.3
 module load gromacs/2020.3-gpu-mpi
 source /shared/centos7/gromacs/2020.3-gcc7.3/bin/GMXRC.bash

 srun --mpi=pmi2 -n $SLURM_NTASKS gmx_mpi mdrun -ntomp 1 -s myrun.tpr -v -dlb yes -cpi state

What is the downside
===================

Jobs running on the lowpriority partition always carry the risk of being suspended before their wall time ends if a 
high priority job requests those resources while the low priority job is running. If labs have purchased a partition, 
the corresponding lab’s members have priority access to those resources. This means that if If a job is submitted to 
the lowpriority partition and a high priority job comes through that requires resources currently occupied by the 
low priority job, then that low priority job will be stopped/suspended within 15s and re-queued. If you have 
`checkpointing <https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html>`_, implemented in your 
workflow, such abrupt suspension of jobs would not be an issue. If your job gets killed this way, it’s restart time 
depends on the availability of resources at that time.

Low priority partition FAQs
====================

Or The FAQs can go here 