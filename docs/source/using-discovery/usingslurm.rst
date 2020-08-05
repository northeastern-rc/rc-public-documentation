.. _using_slurm:

***********
Using Slurm
***********

Slurm (Simple Linux Utility Resource Management) is the software on Discovery
that lets you do the following:

* view information about the cluster
* monitor your jobs
* schedule your jobs on Discovery

:ref:`using_srun` and :ref:`using_sbatch` provide you with a few examples to help get you familiar
with Slurm and be able to submit basic jobs on Discovery.

.. important::
   Slurm commands have numerous options to help your jobs run efficiently by requesting specific resources. Options also usually have both short and verbose versions, such as
   ``--nodes`` and ``-n`` (both mean the same thing). The examples in this documentation all use the
   verbose version of the options for clarity, but you can use the short version if you prefer. For example, ``srun -p short -N 1 -n 1`` means the exact same thing as ``srun --partition=short --nodes=1 --ntasks=1``
   Refer to the official Slurm documentation to get in-depth information about these commands and their options: `Slurm documentation website <https://slurm.schedmd.com/archive/slurm-17.11.6/srun.html>`_.

Viewing Cluster Information
===========================

Use the following commands to view information about the cluster. This information can help you better understand the
hardware that is available in order to customize your job scripts. Also see :ref:`hardware_overview` for more information.

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

Submitting Jobs
================

There are two main commands for submitting jobs to Discovery: ``srun`` and ``sbatch``.
To run a job interactively, use ``srun``. To submit a job to run in the background with a script, use ``sbatch``.

.. list-table::
   :widths: 20 100
   :header-rows: 1

   * - Slurm Command
     - Function
   * - ``srun``
     - Run an interactive job on the cluster. See :ref:`using_srun`
   * - ``sbatch <scriptname.script>``
     - Submit a script to the scheduler for running a job. See :ref:`using_sbatch`
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
     - Reports the computational efficiency of your calculations.
   * - ``squeue -u <your user name>``
     - Displays your job status in the job queue. Good to use with ``sbatch``.
   * - ``scontrol show jobid -d <JOBID>``
     - Displays your job information. Good to use with ``srun``.
