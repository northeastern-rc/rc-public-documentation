
.. _partition_names:

**********
Scavenger
**********
:sub:`Updated July, 2022`

Introduction
===================
‘Scavenger’ is a new partition on discovery that allows the research community to use private resources 
on the cluster when they are idle. ‘Scavenger’ has hardware not otherwise available to the general research 
community and, in time, will double the resources to which users have access.

When to use scavenger
===================

From best to less-good case scenarios:

1. Code that can be check-pointed
2. Jobs that fit on a single node
3. Jobs that require multiple nodes (eg, MPI)
4. When waiting is too hard

How to use scavenger
===================

To use the ``scavenger`` partition, just add that to your partition list. As the partition list is a 
comma-delimited list of values, ``srun --partition=short,scavenger`` is perfectly reasonable. For this example, 
we will exclude partition ``short`` and focus on ``scavenger``. When you run the ``squeue`` command, you can see 
that your job has been assigned to the scavenger partition::

  [m.joshi@login-01 ~]$ srun  -p scavenger --pty /bin/bash
  srun: job 23498584 queued and waiting for resources
  srun: job 23498584 has been allocated resources

  [m.joshi@d3110 ~]$ squeue -u m.joshi
  JOBID    PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
  23498592      ctbp     bash  m.joshi  R       0:07      1 d3110
  23498584 scavenger     bash  m.joshi  R       2:19      1 d3110

For the example provided on our `checkpointing <https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html?highlight=array#gromacs-checkpointing-example>`_ page, you can use the scavenger partition as::

 #!/bin/bash
 #SBATCH --partition=short,scavenger
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

If labs have purchased a partition, they have priority access to those resources. 
In the case of scavenger, this means that if your job is running on a private partition 
from a specific PI’s lab that was idle but is now necessary for a job from that PI’s lab, 
your job will be killed and re-queued. If you use checkpointing, this would be less of an issue. 
