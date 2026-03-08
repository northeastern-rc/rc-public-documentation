(checkpoint-jobs)=
# Checkpointing Jobs

The complexity of HPC systems can introduce unpredictable hardware or software component behavior, leading to job failures. Applying checkpointing to your HPC workflows can make your jobs more resilient to crashes, partition time limits, and hardware failures. Checkpointing is a fault tolerance technique based on Backward Error Recovery (BER), designed to overcome interruptions during the execution of a job.

:::{image} ../images/checkpointing.png
---
width: 300
alt: Checkpointing algorithm flow chart.
align: right
:::

To implement checkpointing:

- Use data redundancy to create checkpoint files, saving all necessary calculation state data. Checkpoint files are generally created at constant intervals during the run.
- If a failure occurs, start from an error-free state, check for consistency, and restore the algorithm to the previous error-free state.

Checkpointing allows you to:

- Create resilient workflows in the event of faults.
- Overcome most scheduler resource time limitations and efficiently use the `lowpriority` partition.
- Implement an early error detection approach by inspecting intermediate results.

## Checkpointing Types

Checkpointing can be implemented at different levels of your workflow.

- **Application-level Checkpointing:** Recommended for most Explorer users. Software designed for HPC often has a checkpointing option; information on proper usage can be found in the software user manual.
- **User-level Checkpointing:** A good option if you develop your code or know the application code well enough to integrate checkpointing techniques effectively. We recommend this approach for Discovery users with advanced proficiency and familiarity with checkpointing mechanisms.
- **System-level Checkpointing:** Done on the system side, where the user saves the state of the entire process. This option is less efficient than User-level or Application-level checkpointing as it introduces a lot of redundancy.
- **Model-level Checkpointing:** Suitable for saving a model's internal state (i.e., its weights or current learning rate) so that the framework can resume the training from a specific point whenever desired. This is often the intent of users doing machine learning on Discovery. See **ML Model-Level Checkpointing** for details.

:::{note}
Some packages can be used to implement checkpointing if you are developing in Python, Matlab, or R. Some examples include [Python PyTorch checkpointing], [TensorFlow checkpointing], [MATLAB checkpointing], and [R checkpointing]. Additionally, many Computational Chemistry and Molecular Dynamics software packages have built-in checkpointing options (e.g., [GROMACS] and [LAMMPS]).
:::

:::{note} Using Job Arrays with Checkpointing
To overcome partition time limits, or to use the `lowpriority` partition effectively, replace your single long job with multiple shorter jobs. Using job arrays, set each job to run one after the other. Each job will write a checkpoint file if checkpointing is implemented. The next job in line will use the latest checkpoint file to continue from the latest state of the calculation.
:::

## Application-level Checkpointing

### GROMACS Checkpointing Example

The following example shows how to implement a 120-hour [GROMACS](https://www.gromacs.org/) job using multiple shorter jobs on the *short* or *lowpriority* partition using Slurm job arrays and the GROMACS built-in checkpointing.

:::{seealso}
[https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html](https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html)
:::

The following script `submit_mdrun_array.sh` creates a Slurm job array of 10 individual array jobs:

:::{code} shell
#!/bin/bash
#SBATCH --partition=short,lowpriority
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

### DMTCP Checkpoint Example

Distributed MultiThreaded checkpointing ([DMTCP](https://dmtcp.sourceforge.io/)) is a tool available on the cluster that allows you to checkpoint without changing your code. DMTCP works with most Linux applications (e.g., Python, Matlab, R, GUI, and MPI). DMTCP runs in the background of your program without significant performance loss and saves the process states into checkpoint files.

:::{code} shell
module avail dmtcp
module show dmtcp
module load dmtcp/2.6.0
:::

Since DMTCP runs in the background, it requires some changes to your shell script. See [examples of checkpointing with DMTCP](https://github.com/northeastern-rc/training-checkpointing/tree/main/Exercise_3), which use DMTCP with a simple C++ program (scripts modified from [RSE-Cambridge](https://github.com/RSE-Cambridge/dmtcp-tests)).

### Application-level Checkpointing Tips

- You should be saving all non-temporary application data and any application data that has been modified since the last checkpoint. You only need to keep the most recent checkpoint file.
- When determining the frequency of your checkpoints, keep in mind that if you checkpoint too often, you will slow your calculation, and too infrequently can lead to long rollback times. In most cases, checkpointing every 10–15 minutes is preferred.


[GROMACS]: https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html
[LAMMPS]: https://docs.lammps.org/restart.html
[MATLAB checkpointing]: https://www.mathworks.com/help/gads/work-with-checkpoint-files.html
[Python PyTorch checkpointing]: https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html
[R checkpointing]: https://cran.r-project.org/web/packages/checkpoint/vignettes/checkpoint.html
[Slurm Job Arrays]: https://slurm.schedmd.com/job_array.html
[TensorFlow checkpointing]: https://www.tensorflow.org/guide/checkpoint
