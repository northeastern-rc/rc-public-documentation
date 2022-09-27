
.. _partition_names:

**********
Low priority partition
**********
:sub:`Updated July, 2022`

Introduction
===================
‘Low priority partition’ is a new partition on Discovery that allows the research community to use resources associated with 
private partitions on the cluster when they are idle. The low priority partition has hardware not otherwise available to the general research 
community and, in time, will double the resources accessible to users.

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

If labs have purchased a partition, the corresponding lab's members have priority access to those resources. 
In the case of low priority partition, this means that if your job is running on another lab's private partition and a job is
submitted by the owner lab's member during this time, then your job will be automatically killed and re-queued 
since the lab member's job has higher priority. If you use `checkpointing <https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html>`_, this would be less of an issue. 
If your job gets killed this way, its restart time depends on the availability of resources at that time. 
