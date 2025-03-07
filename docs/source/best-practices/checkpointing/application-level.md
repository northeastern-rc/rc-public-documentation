(application-level)=
## Application-level checkpointing

### GROMACS checkpointing example

The following example shows how to implement a 120-hour [GROMACS](https://www.gromacs.org/) job using multiple shorter jobs on the *short* partition. We use Slurm job arrays and the GROMACS built-in checkpointing option to implement checkpointing.

:::{seealso}
[https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html](https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html)
:::
The following script `submit_mdrun_array.sh` creates a Slurm job array of 10 individual array jobs:

:::{code} shell
#!/bin/bash
#SBATCH --partition=short
#SBATCH --constraint=cascadelake
#SBATCH --nodes=1
#SBATCH --time=12:00:00
#SBATCH --job-name=myrun
#SBATCH --ntasks=56
#SBATCH --array=1-10%1  # execute 10 array jobs, 1 at a time
#SBATCH --output=myrun-%A_%a.out
#SBATCH --error=myrun-%A_%a.err

module load cuda/10.2
module load gcc/7.3.0
module load openmpi/4.0.5-skylake-gcc7.3
module load gromacs/2020.3-gpu-mpi
source /shared/centos7/gromacs/2020.3-gcc7.3/bin/GMXRC.bash

srun --mpi=pmi2 -n $SLURM_NTASKS gmx_mpi mdrun -ntomp 1 -s myrun.tpr -v -dlb yes -cpi state
:::

The script above sets the checkpoint flag `-cpi state` preceding the filename to dump checkpoints. This directs `mdrun` to the checkpoint in `state.cpt` when loading the state. The Slurm option `--array=1-10%1` creates 10 Slurm array tasks and runs one task job serially for 12 hours. The variable `%A` denotes the main job ID, while `%a` denotes the task ID (i.e., spanning `1-10`).

To submit this array job to the scheduler, use the following command:

:::{code} shell
sbatch submit_mdrun_array.bash
:::

### DMTCP checkpoint example

Distributed MultiThreaded checkpointing ([DMTCP](https://dmtcp.sourceforge.io/)) is a tool checkpoint without changing code. It works with most Linux applications, such as Python, Matlab, R, GUI, and MPI.

The program runs in the background of your program, without significant performance loss and saves the process states into checkpoint files. DMTCP is available on the cluster

:::{code} shell
module avail dmtcp
module show dmtcp
module load dmtcp/2.6.0
:::

Since DMTCP runs in the background, it requires some changes to your shell script. See [examples of checkpointing with DMTCP](https://github.com/northeastern-rc/training-checkpointing/tree/main/Exercise_3), which use DMTCP with a simple C++ program (scripts modified from [RSE-Cambridge](https://github.com/RSE-Cambridge/dmtcp-tests)).


### Application-level checkpointing tips

What data should you save?
- Non-temporary application data
- Any application data that has been modified since the last checkpoint
- Delete no longer useful checkpoints; keep only the most recent checkpoint file.

How frequently do checkpoints occur?
- Too often will slow your calculation; maybe I/O is heavy and memory intensive.
- Too infrequently leads to large or long rollback times.
- Consider how long it takes to reach a checkpoint and restart your calculation.
- In most cases, every 10–15 minutes is okay.
