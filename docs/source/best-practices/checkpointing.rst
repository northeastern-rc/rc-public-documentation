*****************************************
Checkpoint/Restart Discovery Jobs
*****************************************

The complexity of HPC systems may introduce unpredictable behaviors and may result in job failures due to hardware or software. Applying fault tolerance techniques to your HPC workflows allows your jobs to become more resilient to crashes, partition time limits and hardware failures.

Checkpointing will allow you to:

 * Create resilient workflows in the existence of faults.
 * Overcome most scheduler resource time limitations.
 * Implement an early error detection approach by inspecting intermediate results.  

The Checkpointing technique
================================

Checkpointing is a fault tolerance technique designed to overcome the “fail-stop” failure type (interruption of the execution of a job). It is based on the BER technique (Backward error recovery or Rollback-recovery algorithm):

 * Use data redundancy - create checkpoint files saving all of the necessary calculation state data. Checkpoint files are generally created at constant time intervals during the run. 
 * If a failure occures - start from an error-free state, check for consistency and restore the algorithm to the previous error-free state.

.. image:: /images/checkpointing.png
 :width: 300
 :alt: Checkpointing algorithm flow chart.

Checkpointing types
================================

Checkpointing can be implemented in different levels of your workflow:

  * User-level Checkpointing - suitable if you develop your own code, or have sufficient knowledge of the application code to integrate checkpointing techinques yourself. Generally, this approach is not recommended for most Discovery users.
  * Application-level Checkpointing - recommended for most Discovery users. Utilize the Checkpointing tool that is already available in your software application. Most software designed for HPC have a Checkpointing option, and information on proper usage is often available in the software user manual. 
  * System-level Checkpointing - done on the system side, where the state of the entire process is being saved. This option is less efficient than User-level or Application-level Checkpointing as it introduces a lot of redundancy.   

.. note::
  If you are developing code using Python, Matlab or R, there are packages and functions that can be used to implement Checkpointing easily. Some examples include `Python Pytorch Checkpointing <https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html>`_, `TensorFlow Checkpointing <https://www.tensorflow.org/guide/checkpoint>`_, `Python Pickle Checkpointing <https://deap.readthedocs.io/en/master/tutorials/advanced/checkpoint.html>`_, `MATLAB Checkpointing <https://www.mathworks.com/help/gads/work-with-checkpoint-files.html>`_ and `R Checkpointing <https://cran.r-project.org/web/packages/checkpoint/vignettes/checkpoint.html>`_. Additionally, many Computational Chemistry and Molecular Dynamics software have built-in Checkpointing options, such as `GROMACS <https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html>`_ and `LAMMPS <https://docs.lammps.org/restart.html>`_.  


Checkpointing can be acheived by a combination of implementing Checkpointing at some level in your job with the use of `Slurm Job Arrays <https://slurm.schedmd.com/job_array.html>`_. 

.. note::
   To overcome partition time limits, replace your long single job with multiple shorter jobs. Using job arrays, set each job to run after another. Each job will write a checkpoint file if checkpointing is implemented. The next job in line will the latest checkpoint file to continue from the latest state of the calculation.

GROMACS Checkpointing example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to implement a longer `GROMACS <https://www.gromacs.org/>`_ 120 hour calculation on using multiple shorter jobs on the **short** partition with Slurm job arrays and the GROMACS built-in Checkpointing option (read more `here <https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html>`_).

The following script **submit_mdrun_array.bash** creates a Slurm job array of ::

 #!/bin/bash
 #SBATCH --partition=short
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

Where we used the checkpoint flag followed by the file name ``-cpi state`` to be used to checkpointing. This directs mdrun to use the checkpoint file named ``state.cpt`` when loading the state. The Slurm option ``--array=1-10%1`` will create 10 Slurm array tasks, and will run one task job at a time for 12 hours. Note that the saved variable ``%A`` denotes the main job ID, while variable ``%a`` denotes the task ID (spanning values 1-10).

To submit these jobs to the scheduler, use the command::

   sbatch submit_mdrun_array.bash

Python TensorFlow Checkpointing example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to implement a longer TensorFlow ML job by training using the **tf.keras** Checkpointing `API <https://www.tensorflow.org/tutorials/keras/save_and_load>`_ and multiple shorter Slurm job arrays on the gpu partition.
Below the example **submit_tf_array.bash** script::

 #!/bin/bash
 #SBATCH --job-name=myrun
 #SBATCH --time=00:10:00
 #SBATCH --partition=gpu
 #SBATCH --nodes=1
 #SBATCH --gres=gpu:1
 #SBATCH --mem=10Gb
 #SBATCH --output=%A-%a.out
 #SBATCH --error=%A-%a.err
 #SBATCH --array=1-10%1  #execute 10 array jobs, 1 at a time.

 module load miniconda3/2020-09
 source activate tf_gpu

 ##Define the number of steps based on the job id:
 numOfSteps=$(( 500 * SLURM_ARRAY_TASK_ID ))

 # run the python code, save all output to a log file corresponding the the current job task that is running:
 python train_with_checkpoints.py $numOfSteps &> log.$SLURM_ARRAY_TASK_ID

Where the checkpointing implementation is given in this code snippet of ``train_with_checkpoints.py``::

 checkpoint_path = "training_2/{epoch:d}.ckpt"
 checkpoint_dir = os.path.dirname(checkpoint_path)
 cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    verbose=1,
    save_weights_only=True,
    period=5)

The full scripts can be found `here <https://github.com/northeastern-rc/training-checkpointing/tree/main/Exercise_2>`_ and were modified from `TensorFlow Save and load models <https://www.tensorflow.org/tutorials/keras/save_and_load>`_.

The Slurm option ``--array=1-10%1`` will create 10 Slurm array tasks, and will run one task job at a time. Note that the saved variable ``%A`` denotes the main job ID, while variable ``%a`` denotes the task ID (spanning values 1-10). Note that also the output/error files are unique in order to prevent different jobs writing to the same files.
The Shell variable ``SLURM_ARRAY_TASK_ID`` holds the unique task ID value and can be used within the Slurm Shell script to point to different files or variables.

To submit this job to the scheduler, use the command::
   
  sbatch submit_tf_array.bash

Checkpointing using DMTCP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`DMTCP <https://dmtcp.sourceforge.io/>`_ (Distributed MultiThreaded Checkpointing) is a Checkpointing tool that lets you Checkpoint without the need to change your code. It Works with most Linux applications such as Python, Matlab, R, GUI, MPI etc. 
The program runs in the background of your program, without significant performance loss, and saves the process states into checkpoint files. DMTCP is available on the cluster ::

 module avail dmtcp
 module show dmtcp
 module load dmtcp/2.6.0

As DMTCP runs in the background, it requires some changes to your Shell script. For examples of how to checkpoint with DMTCP visit `here <https://github.com/northeastern-rc/training-checkpointing/tree/main/Exercise_3>`_. 
The example demonstrates how to use DMTCP with a simple C++ program (scripts modified from `RSE-Cambridge <https://github.com/RSE-Cambridge/dmtcp-tests>`_).


Checkpointing tips
~~~~~~~~~~~~~~~~~~~

What data to save?
 * Non-temporary application data
 * Any application data that has been modified since the last checkpoint
 * Delete checkpoints that are no longer useful - keep only the most recent checkpoint file.

How frequently to checkpoint? 
 * Too often – will slow down your calculation, may be I/O heavy and memory-limited.
 * Too infrequently – leads to large/long rollback times.
 * Consider how long it takes to checkpoint and restart your calculation. 
 * In most cases a rate of every 10-15 minutes is ok.

Which checkpointing method to use?
 * If your software already comes with built-in checkpointing, it is often the preferred option. It is probably the most optimized and efficient way to checkpoint.
 * Application-level Checkpointing is the easiest to use as it is already integrated in your applicaion. Does not require major changes to your scripts.
 * Application-level Checkpointing will save only the relevant data for your specific application.
 * If you're writing your own code - use DMTCP or implement your own Checkpointing.
