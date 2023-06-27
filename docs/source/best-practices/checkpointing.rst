*****************************************
Checkpoint/Restart Discovery Jobs
*****************************************

The complexity of HPC systems may introduce unpredictable behaviors in hardware or software components resulting in job failures. Applying fault tolerance techniques to your HPC workflows makes your jobs more resilient to crashes, partition time limits, and hardware failures.


The Checkpointing technique
================================

Checkpointing is a fault tolerance technique based on the Backward error recovery (BER) technique and is designed to overcome the “fail-stop” failure type (interruption of the execution of a job)

 * Use data redundancy - create checkpoint files saving all of the necessary calculation state data. Generally, we checkpoint files at constant time intervals during the run.
 * If a failure occurs - start from an error-free state, check for consistency, and restore the algorithm to the previous error-free state.

.. image:: /images/checkpointing.png
 :width: 300
 :alt: Checkpointing algorithm flow chart.
 
 Checkpointing will allow you to:

 * Create resilient workflows in the existence of faults
 * Overcome most scheduler resource time limitations
 * Implement an early error detection approach by inspecting intermediate results

Different levels of Checkpointing in workflow:
==============================================

  * Application-level checkpointing - recommended for most Discovery users. Utilize the checkpointing tool that is already available in your software application. For example, most software designed for HPC has a checkpointing option, and information on proper usage is often available in the software user manual.
  * User-level checkpointing - suitable approach if you develop your code or possess sufficient knowledge of the application code to integrate checkpointing techniques effectively. We recommend this approach for some Discovery users with advanced proficiency and familiarity with checkpointing mechanisms.
  * System-level checkpointing - done on the system side, where the user saves the state of the entire process. This option is less efficient than User-level or Application-level checkpointing as it introduces a lot of redundancy.
  * Model-level checkpointing - suitable approach for saving model's internal state (its weights, current learning rate, etc.) so that the  framework can resume the training from this point whenever desired. This is often the intent of the user doing machine learning on Discovery.

Which checkpointing method to use?
----------------------------------
 * If your software already comes with **built-in checkpointing**, it is often the preferred option. It is the most optimized and efficient way to the checkpoint.
 * **Application-level** checkpointing is the easiest to use, as it exists in your application: it does not require significant changes to your scripts. It also saves only the relevant data for your specific application.
 * **User-level** If you're writing your code - use DMTCP or implement your own checkpointing.
 * **ML Model-level** checkpointing is specific to model training and deployment (see `ML Model-level`_)

.. note::
Note:
  Some packages and functions allow for easy checkpointing if you are developing code using Python, Matlab, or R. Some examples include `Python PyTorch checkpointing <https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html>`_, `TensorFlow checkpointing <https://www.tensorflow.org/guide/checkpoint>`_, `Python Pickle checkpointing <https://deap.readthedocs.io/en/master/tutorials/advanced/checkpoint.html>`_, `MATLAB checkpointing <https://www.mathworks.com/help/gads/work-with-checkpoint-files.html>`_ and `R checkpointing <https://cran.r-project.org/web/packages/checkpoint/vignettes/checkpoint.html>`_. Additionally, many Computational Chemistry and Molecular Dynamics software have built-in checkpointing options, such as `GROMACS <https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html>`_ and `LAMMPS <https://docs.lammps.org/restart.html>`_.


Implementing checkpointing can be achieved by:
 * Some save-and-load mechanisms of your calculation state
 * The use of `Slurm Job Arrays <https://slurm.schedmd.com/job_array.html>`_

.. note::
Note:
   To overcome partition time limits, replace your single long job with multiple shorter jobs. Then, using job arrays, set each job to run one after the other. Each job will write a checkpoint file if checkpointing is implemented. The following job in line will be the latest checkpoint file to continue from the latest state of the calculation.

Application-level checkpointing
===============================

Checkpointing using GROMACS
---------------------------

The following example demonstrates how to break a long 120-hour `GROMACS <https://www.gromacs.org/>`_  job into multiple shorter jobs on the **short** partition. We use Slurm job arrays and the GROMACS built-in checkpointing option (read more `here <https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html>`_) to implement checkpointing.

The following script **submit_mdrun_array.bash** creates a Slurm job array of 10 individual array jobs::

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
 source /shared/centos7/gromacs/2020.3-gcc7.3/bin/GMXRC.bashi

 srun --mpi=pmi2 -n $SLURM_NTASKS gmx_mpi mdrun -ntomp 1 -s myrun.tpr -v -dlb yes -cpi state

In the above script, we use the checkpoint flag ``-cpi state`` followed by the file name to be used for checkpointing. This directs mdrun to use the checkpoint file named ``state.cpt`` when loading the state. The Slurm option ``--array=1-10%1`` will create 10 Slurm array tasks, and will run one task job at a time for 12 hours. Note that the saved variable ``%A`` denotes the main job ID, while variable ``%a`` denotes the task ID (spanning values 1-10).

To submit this array job to the scheduler, use the following command::

   sbatch submit_mdrun_array.bash

Checkpointing using DMTCP
--------------------------

`DMTCP <https://dmtcp.sourceforge.io/>`_ (Distributed MultiThreaded checkpointing) is available on the cluster, enabling checkpointing without the need to modify your code, and it works with most Linux applications (e.g., Python, Matlab, R, GUI, and MPI).
The program runs in the background of your program without significant performance loss and saves the process states into checkpoint files. DMTCP is available on the cluster ::

 module avail dmtcp
 module show dmtcp
 module load dmtcp/2.6.0

Because DMTCP runs in the background, changes to your shell script are required. For examples of how to checkpoint with DMTCP visit `here <https://github.com/northeastern-rc/training-checkpointing/tree/main/Exercise_3>`_.
The examples demonstrates how to use DMTCP with a simple C++ program (scripts modified from `RSE-Cambridge <https://github.com/RSE-Cambridge/dmtcp-tests>`_).

Tips and Tricks
---------------------

What data to save?
 * Non-temporary application data
 * Any application data that has changed since the last checkpoint
 * Delete improper checkpoints - keep only the most recent checkpoint file

How frequently should we checkpoint?
Consider the duration required for checkpointing and restarting your calculation. In most cases, a checkpointing interval of every 10-15 minutes is adequate. It is important to keep in mind that if you checkpoint too frequently, it can slow down your calculation. Conversely, if you checkpoint too infrequently, you run the risk of encountering lengthy rollback times.

.. _ML Model-level:

ML Model-level checkpointing
============================

Model-level checkpointing is a technique employed to periodically save the state of a machine learning (ML) model during its training. This checkpointing enables the training process to be resumed from the saved checkpoint in case of interruptions or premature termination. The saved state typically includes the model’s parameters, optimizer state, and essential training information such as the epoch number and loss value (or the accuracy). The following instructions are helpful for long-running training jobs, as they enable faster recovery from failures and better tracking of the training process.

Why checkpointing is important in Deep Learning?
------------------------------------------------------

Checkpointing is crucial in deep learning, as the training process can be time-consuming and require significant computational resources. In addition, the training process may sometimes get interrupted due to hardware or software issues. Checkpointing provides a solution to this problem, as it allows saving the current state of the model, which can then be resumed from where it was stopped.

Moreover, checkpointing also saves the best-performing model, which can then be used for making predictions. For example, in deep learning, the model's performance can vary based on the initialization and the optimization algorithm, so checkpointing provides a way to select the best model based on a performance metric.

In summary, checkpointing is essential in deep learning as it provides a way to save progress, resume training from where it was stopped, and select the best-performing model.

Python TensorFlow
------------------

The following example demonstrates how to implement a longer TensorFlow ML job by training using the **tf.keras** checkpointing `API <https://www.tensorflow.org/tutorials/keras/save_and_load>`_ and multiple shorter Slurm job arrays on the gpu partition.
Below is the example **submit_tf_array.bash** script::

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

 # run the python code, and save all output to a log file corresponding the current job task that is running:
 python train_with_checkpoints.py $numOfSteps &> log.$SLURM_ARRAY_TASK_ID

The checkpointing implementation is given in this code snippet of ``train_with_checkpoints.py``::

 checkpoint_path = "training_2/{epoch:d}.ckpt"
 checkpoint_dir = os.path.dirname(checkpoint_path)
 cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path,
    verbose=1,
    save_weights_only=True,
    period=5)

The entire scripts can be found `here <https://github.com/northeastern-rc/training-checkpointing/tree/main/Exercise_2>`_ and were modified from `TensorFlow Save and load models <https://www.tensorflow.org/tutorials/keras/save_and_load>`_.

The Slurm option, ``--array=1-10%1``, will create 10 Slurm array tasks and run one task at a time. Note that the saved variable ``%A`` denotes the main job ID, while variable ``%a`` indicates the task ID (spanning values 1-10). Also note that the output/error files are unique to prevent different jobs from writing to the same files.
The Shell variable, ``SLURM_ARRAY_TASK_ID``, holds the unique task ID value and can be used within the Slurm Shell script to point to different files or variables.

To submit this job to the scheduler, use the command::

  sbatch submit_tf_array.bash

Python PyTorch
------------------

Tips and tricks
------------------

Save only the model's State_dict
""""""""""""""""""""""""""""""""
Save only the model's state_dict and the optimizer's state, as this allows us to save only the
necessary information needed to resume training. In addition, this reduces the size of the checkpoint file and makes it
easier to load the model. Avoid saving unnecessary information in the checkpoint file, such as irrelevant metadata or tensors that can bereconstructed during training. This will reduce the size of the checkpoint file and make it easier to manage.

Save regularly
""""""""""""""""""""
To prevent losing progress in case of a crash or interruption, save the checkpoint file regularly (i.e., after each epoch).

Save to multiple locations
""""""""""""""""""""""""""""""""
Save the checkpoint file to multiple locations, such as a local drive and the cloud, to ensure that
the checkpoint is recovered in case of failure.

Use the latest versions of libraries
""""""""""""""""""""""""""""""""""""""""
Using the latest version of PyTorch and other relevant libraries is vital; changes in these libraries may cause
compatibility issues with older checkpoints. With these best practices, you can ensure that your PyTorch models are
saved efficiently and effectively and that your progress is not lost in case of a crash or interruption.

Naming conventions
""""""""""""""""""""
Develop a consistent naming convention for checkpoint files; include information such as the date, time, and epoch
number in the file name to make tracking multiple checkpoint files easier and ensure you are choosing the proper checkpoint to
load.

Validate the checkpoint
"""""""""""""""""""""""""""
Validate the checkpoint after loading it to ensure that the model's state_dict and the optimizer's state are correctly
loaded by making a prediction using the loaded model and checking that the results are as expected.

Periodic clean-up
""""""""""""""""""""
Periodically, remove old checkpoint files to avoid filling up storage. This can be done by keeping only the latest
checkpoint or keeping only checkpoint files from the last few epochs.

Documenting checkpoints
""""""""""""""""""""""""""
Document the purpose of each checkpoint and what it contains; include the model architecture, the training data, the
hyper-parameters, and the performance metrics. This will help to keep track of the progress and make it easier to
compare different checkpoints. With these additional best practices, you can ensure that your checkpointing process is
efficient, effective, and well-organized.

