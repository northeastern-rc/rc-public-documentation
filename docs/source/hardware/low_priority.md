(low-priority)=

# Low Priority Partition

## Introduction

The new `lowpriority` partition allows the research community to use private resources on the high performance computing (HPC) cluster when those resources are idle. This is a common practice in HPC clusters to optimize the use of idle private resources that consume power and cooling. This new partition has hardware that is not otherwise available to the general research community and, in time, could double the resources available to NURC users.

## When to use the Low Priority Partition

From most to least-recommended scenarios:

1. Code that can be checkpointed ( {ref}`checkpoint-jobs`)
1. Jobs that fit on a single node 
1. Jobs that require multiple nodes (e.g., MPI - please see {ref}`using-mpi`)
1. When facing longer than average waits times in the other partitions

## How to use the Low Priority Partition

To use the low priority partition, just add `lowpriority` (no space between 'low' and 'priority') to your partition list. The partition list is a comma-delimited list of values indicating the order of preference for assigning the job to a particular partition. Hence, the low priority partition must be specified after a general partition has been mentioned, as `srun --partition=short,lowpriority`. For the example below, we will exclude partition `short` and focus on `lowpriority`. When you run the `squeue` command, you can see that your job has been assigned to the low priority partition

:::{code} bash 
$ srun -p lowpriority --pty /bin/bash
srun: job 23498584 queued and waiting for resources
srun: job 23498584 has been allocated resources

$ squeue -u $USER
JOBID      PARTITION     NAME     USER   ST   TIME  NODES  NODELIST(REASON)
23498584 lowpriority     bash    $USER    R   2:19      1  d3110
:::

### Checkpointing Example (GROMACS)

For the example provided on our {ref}`checkpoint-jobs` page, you can specify the low priority partition along with a shared partition as

:::{code} bash
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
:::

### Slurm Job Array Example

For this example, a python script and input lists from the [Slurm Job Array Training] are used to show how the `lowpriority` partition can be used with Slurm job arrays.

:::{code} bash
#!/bin/bash
#SBATCH --partition=short,lowpriority
#SBATCH --nodes=1
#SBATCH --cpus-per-task=2
#SBATCH --time=2:00:00
#SBATCH --job-name=myrun
#SBATCH --array=1-4%4  #execute 4 array jobs at the same time
#SBATCH --output=myrun-%A_%a.out
#SBATCH --error=myrun-%A_%a.err

# Load a python environment
module load anaconda3/2022.05

# Where myjob.py requires an input indexed by the sub job id ($SLURM_ARRAY_TASK_ID)
python getMax.py list$SLURM_ARRAY_TASK_ID > output.list$SLURM_ARRAY_TASK_ID
:::

## Key Features of using Low Priority

Jobs running on the `lowpriority` partition always carry the risk of being suspended before their wall time ends if a high priority job requests those resources while the low priority job is running (see our {ref}`low-priority-faqs` page for a description of "low" and "high" priority jobs). The members of a PI's partition have priority access to the resources of that partition. This means that if a job is submitted to the `lowpriority` partition and a high priority job comes through that requires resources currently occupied by the low priority job, then that low priority job will be stopped/suspended within 30s and re-queued. If you have checkpointing (Please see {ref}`checkpoint-jobs`) implemented in your workflow, such an abrupt suspension of the job would not be an issue. However, if your job gets suspended this way, then its restart time will depend on the availability of resources at that time.

[Slurm Job Array Training]:https://github.com/northeastern-rc/training-slurmarrayjobs/tree/main/Exercise_sequential_python