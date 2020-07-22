.. _using_slurm:

***********
Using Slurm
***********

Slurm (Simple Linux Utility Resource Management) is the software on Discovery
that lets you do the following:

* view information about the cluster
* schedule your jobs on Discovery
* monitor your jobs

:ref:`slurm_examples` provides you with a few examples to help get you familiar
with Slurm and be able to submit and monitor basic jobs on Discovery.
For in-depth information on Slurm, see https://slurm.schedmd.com/.


Viewing Cluster Information
===========================

Use the following commands to view information about the cluster. This information can help you better understand the
hardware that is available in order to customize your job scripts.

.. list-table::
   :widths: 20 100
   :header-rows: 1

   * - Slurm Command
     - Function
   * - ``sinfo <options>``
     - View partition and node information. Use option -a to view all partitions.
   * - ``smap <options>``
     - View details about the cluster in a visual format

.. _submitting_jobs:

Controlling Jobs
================

There are two main commands for submitting jobs to Discovery: ``srun`` and ``sbatch``.
To run a job interactively, use ``srun``. To submit a job to run in the back ground with a script, use ``sbatch``.

.. list-table::
   :widths: 20 100
   :header-rows: 1

   * - Slurm Command
     - Function
   * - ``srun``
     - Run an interactive job on the cluster
   * - ``sbatch <scriptname.script>``
     - Submit a script to the scheduler for running a job
   * - ``scancel <jobid>``
     - Cancel a pending or running job on the cluster

Monitoring Jobs
===============

.. list-table::
   :widths: 20 100
   :header-rows: 1

   * - Slurm Command
     - Function
   * - ``seff <jobid>``
     - Reports the computational efficiency of your calculations
   * - ``squeue``
     - View job status

.. _batch_jobs:

Batch Jobs
~~~~~~~~~~

You use the ``sbatch`` command with a bash script to specify the
resources you need to run your jobs, such as the number of nodes you want to run your jobs
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
