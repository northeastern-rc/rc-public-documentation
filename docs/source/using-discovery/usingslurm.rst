.. _using_slurm:

***********
Using Slurm
***********

Slurm (Simple Linux Utility Resource Management) is the software on Discovery
that lets you do the following:

* view information about the cluster
* monitor your jobs
* schedule your jobs on Discovery
* view information about your account

:ref:`using_srun` and :ref:`using_sbatch` provide you with a few examples to help get you familiar
with Slurm and be able to submit basic jobs on Discovery.

.. important::
   Slurm commands have numerous options to help your jobs run efficiently by requesting specific resources. Options also usually have both short and verbose versions, such as
   ``--nodes`` and ``-N`` (both mean the same thing). The examples in this documentation all use the
   verbose version of the options for clarity, but you can use the short version if you prefer. For example, ``srun -p short,lowpriority -N 1 -n 1`` means the exact same thing as ``srun --partition=short,lowpriority --nodes=1 --ntasks=1``
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

Account information
====================

Some Discovery users have more than one Discovery group account associated with their username. For example, a student might be in a class that is using Discovery,
and also be in a student club that is using Discovery for a club project. In this case, the student would have two group accounts associated with their username.
When running a job with either ``srun`` or ``sbatch``, if you have more than one account associated with your username, we recommend that you use the ``--account=`` flag and specify the account
that corresponds to the project you are working on. In the example with a student associated with a class and a student club, if the student is on Discovery submitting a job for a project
for his or her class, set the ``account=`` flag to the name of the class account. If the student is working on a project for the club, set the ``account=`` flag to the name of the student club account.

To find out what account(s) your usesrname is associated with, use the following command::

  sacctmgr show associations user=<yourusername>

After you have determined what accounts your username is associated with, if you have more than one account association, you can use the ``account=`` flag with your usual ``srun`` or ``sbatch`` commands.

For example, if you are associated with an account named ``dataclub`` and an account named ``info7500``, and you're currently doing work that should be associated with the
``dataclub`` account, in your ``srun`` command, you can add the ``--account=dataclub`` flag to specify that account.::

  srun --account=dataclub --partition=short --nodes=1 --ntasks=28 --mem=0 --pty /bin/bash

.. note::
   If you do not have more than one account associated with your username, you do not need to use the ``--account=`` flag. Most users on Discovery have only one account
   associated with their username.
