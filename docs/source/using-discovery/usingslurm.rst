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

:ref:`using_srun` and :ref:`using_sbatch` provide you with a few examples to help get you familiar with Slurm and be able to submit basic jobs on Discovery.

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

Account information
====================

Some Discovery users have more than one Discovery group account associated with their username. For example, a student might be in a class that is using Discovery,
and also be in a student club that is using Discovery for a club project. In this case, the student would have two group accounts associated with their username.

When running a job with either ``srun`` or ``sbatch``, if you have more than one account associated with your username, we recommend that you use the ``--account=`` flag and specify the account that corresponds to the project you are working on. In the example with a student associated with a class and a student club, if the student is on Discovery submitting a job for a project for his or her class, set the ``account=`` flag to the name of the class account. If the student is working on a project for the club, set the ``account=`` flag to the name of the student club account.

To find out what account(s) your username is associated with, use the following command::

  sacctmgr show associations user=<yourusername>
After you have determined what accounts your username is associated with, if you have more than one account association, you can use the ``account=`` flag with your usual ``srun`` or ``sbatch`` commands.

For example, if you are associated with an account named ``dataclub`` and an account named ``info7500``, and you're currently doing work that should be associated with the
``dataclub`` account, in your ``srun`` command, you can add the ``--account=dataclub`` flag to specify that account.::

  srun --account=dataclub --partition=short --nodes=1 --ntasks=28 --mem=0 --pty /bin/bash
.. note::
   If you do not have more than one account associated with your username, you do not need to use the ``--account=`` flag. Most users on Discovery have only one account
   associated with their username.

SLURM Commands
==============
**Controlling Jobs**

``scontrol hold <jobid>`` Place a hold on a pending job

``scontrol release <jobid>`` Release a held job

``scontrol requeue <jobid>`` Requeue a completed, failed, or cancelled job

**Job Reporting**

``sacct <options>`` Display job accounting information

``sreport <options>`` Generate reports about cluster utilization and job statistics

**Advanced Features**

``sprio <options>`` Show the priority of jobs and job steps

``sburst <options>`` Show the state of all burst buffer pools

Note: The exact options and functions for each command may vary depending on the Slurm version and configuration. It is recommended to consult the Slurm documentation for more information on the full range of available commands and their usage.

State of the Cluster and Specific Nodes
=======================================
Here are some more examples of using ``sinfo`` and ``scontrol`` to provide information about the state of the cluster and specific nodes:

**Using sinfo**

View information about all partitions::

   sinfo -a
This command will show information about all partitions in the cluster, including the partition name, available nodes, and status.

View information about a specific partition::

   sinfo -p <partition_name>
This command will show information about a specific partition in the cluster, including the number of nodes, number of free nodes, and state of the partition.

View detailed information about nodes::

   sinfo -N -l
This command will show detailed information about all nodes in the cluster, including the node name, state, CPU architecture, memory, and available features.

**Using scontrol**

View information about a specific node::

   scontrol show node <node_name>
This command will show information about a specific node in the cluster, including the node name, state, number of CPUs, and amount of memory.

View information about a specific job::

   scontrol show job <job_id>
This command will show information about a specific job, including the job ID, state, user name, and partition name.

View information about a specific reservation::

   scontrol show reservation <reservation_name>
This command will show information about a specific reservation in the cluster, including the reservation name, start time, end time, and nodes included in the reservation.

These are just a few examples of what you can do with ``sinfo`` and ``scontrol`` to view information about the state of the cluster and specific nodes. There are many other options and commands available, and it is recommended to consult the `Slurm documentation`_ for more information on how to use these tools effectively.

.. _Slurm documentation: https://slurm.schedmd.com/documentation.html