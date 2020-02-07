.. _using_slurm:

***********
Using Slurm
***********

Slurm (Simple Linux Utility Resource Management) is the scheduling software that
you use to schedule your jobs on Discovery.
:ref:`slurm_examples` provides you with a few simple examples to help get you familiar
with Slurm and be able to submit and monitor basic jobs on Discovery.
For in-depth information on Slurm, see https://slurm.schedmd.com/.

Commonly used Slurm commands
============================

The following table highlights some common Slurm commands.

.. list-table::
   :widths: 20 100
   :header-rows: 1

   * - Slurm Command
     - Function
   * - ``sinfo <options>``
     - View partition and node information. Use option -a to view all partitions.
   * - ``squeue``
     - View details about jobs being run on the cluster
   * - ``srun``
     - Run an interactive job on the cluster
   * - ``sbatch <scriptname.script>``
     - Submit a script to the scheduler for running a job
   * - ``scancel <jobid>``
     - Cancel a pending or running job on the cluster
   * - ``seff``
     - Reports the computational efficiency of your calculations

.. _submitting_jobs:

Submitting Jobs
===============

You use Slurm to submit jobs to Discovery. Slurm commands allow you to specify the
resources you need to run your jobs, such as which nodes you want to run your jobs
on and how much memory you’ll need. Slurm then schedules your job based on the
availability of the resources you’ve specified.
The general format for submitting a job to the scheduler is as follows::

   sbatch example.script

Where ``example.script`` is a script detailing the parameters of the job you want to run.
See :ref:`slurm_examples` for more information on writing scheduler scripts.

.. note::
  The default time limit depends on the partition that you specify in your submission script using the
  ``--partition=<partition name>`` option.
  If your job does not complete within the requested time limit,
  Slurm will automatically terminate the job.
  See :ref:`partition_names` for the most up-to-date partition names and parameters.
