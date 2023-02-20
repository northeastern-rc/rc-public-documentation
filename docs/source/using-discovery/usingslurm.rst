.. _using_slurm:

***********
Using Slurm
***********

Slurm (Simple Linux Utility Resource Management) is the software on Discovery that lets you do the following:

* view information about the cluster
* schedule your jobs on Discovery
* monitor your jobs
* view information about your account
* check the state of the cluster and specific nodes

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
   :widths: 35 85
   :header-rows: 1

   * - Slurm Command
     - Function
   * - ``sinfo <options>``
     - View partition and node information. Use option ``-a`` to view all partitions.
   * - ``smap <options>``
     - View details about the cluster in a visual format

.. _submitting_jobs:

Submitting Jobs
================

There are two main commands for submitting jobs to Discovery: ``srun`` and ``sbatch``.
To run a job interactively, use ``srun``. To submit a job to run in the background with a script, use ``sbatch``.

.. list-table::
   :widths: 30 90
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
   :widths: 40 80
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


.. _using_srun:
Using srun
-----------
You can use the Slum command ``srun`` to allocate an interactive job. This means you use specific options with ``srun``
on the command line to tell Slurm what resources you need to run your job, such as number of nodes, amount of memory, and amount of
time. After typing your ``srun`` command and options on the command line and pressing enter, Slurm will find and then allocate the resources
you specified. Depending on what you specified, it can take a few minutes for Slurm to allocate those resources. You can view all of the
``srun`` options on the `Slurm documentation`_.

The following image shows an example of an ``srun`` command as run on a command line.

.. image:: /images/srun_example.jpg
  :alt: image of the command line showing an example srun command

Example Uses
^^^^^^^^^^^^
This section details a few examples using ``srun``. You should first review the :ref:`hardware_overview` and :ref:`partition_names` sections
to be familiar with the available hardware and partition limits on Discovery. This way, you can tailor your request to fit both the needs of your job
and the limits of the partitions. For example, if you specify ``--partition=debug`` and ``--time=01:00:00``, you'll get an error because the
time you've specified exceeds the limit for that partition. Also keep in mind that while these examples are all valid, general examples, they might not work
for your particular job.

simple ``srun`` example is to move to a compute node after you first log into Discovery. ::

 srun --pty /bin/bash

To request one node and one task for 30 minutes with X11 forwarding on the short partition, type::

 srun --partition=short --export=ALL --nodes=1 --ntasks=1 --x11 --mem=10G --time=00:30:00 --pty /bin/bash

To request one node, with 10 tasks and 2 CPUs per task (a total of 20 CPUs), 1GB of memory, for one hour on the express partition, type::

 srun --partition=express  --nodes 1 --ntasks 10 --cpus-per-task 2 --pty --export=ALL --mem=1G --time=01:00:00 /bin/bash

To request two nodes, each with 10 tasks per node and 2 CPUs per task (a total of 40 CPUs), 1GB of memory, for one hour on the express partition, type::

 srun --partition=express  --nodes=2 --ntasks 10 --cpus-per-task 2 --pty --export=ALL --mem=1G --time=01:00:00 /bin/bash

To allocate a GPU node, you should specify the ``gpu`` partition and use the --gres option::

 srun --partition=gpu --nodes=1 --ntasks=1 --export=ALL --gres=gpu:1 --mem=1Gb --time=01:00:00 --pty /bin/bash

For more information about working with GPUs, see :ref:`working_gpus`.

Monitor your jobs
~~~~~~~~~~~~~~~~~~
You can monitor your jobs by using the Slurm ``scontrol`` command. Type ``scontrol show jobid -d <JOBID>``, where ``JOBID`` is the number of your job. In the figure at the top of the page, you can see that when you submit your ``srun`` command, Slurm displays the unique ID number of your job (``job 12962519``). This is the number you use with ``scontrol`` to monitor your job.

.. _using_sbatch:
Using sbatch
=============
You use the ``sbatch`` command with a bash script to specify the
resources you need to run your jobs, such as the number of nodes you want to run your jobs on and how much memory you’ll need. Slurm then schedules your job based on the availability of the resources you’ve specified.

The general format for submitting a job to the scheduler is as follows::

   sbatch example.script

Where ``example.script`` is a script detailing the parameters of the job you want to run.

.. note::
  The default time limit depends on the partition that you specify in your submission script using the
  ``--partition=<partition name>`` option.
  If your job does not complete within the requested time limit,
  Slurm will automatically terminate the job.
  See :ref:`partition_names` for the most up-to-date partition names and parameters.


SBATCH Examples
---------------

Job request: one node
^^^^^^^^^^^^^^^^^^^^^^^
Run a job on one node for 4 hours on the short partition::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --partition=short
  <commands to execute>

Job request: one node with additional memory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default memory per allocated core is 1GB. If your calculations try to use more memory than what is allocated, Slurm automatically terminates your job. You should request a specific amount of memory in your job script if your calculations need more memory than the default. The example script below is requesting 100GB of memory (``--mem=100G``). Use one capital letter to abbreviate the unit of memory (K,M,G,T) with the ``--mem=`` option, as that is what Slurm expects to see. ::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --mem=100G
  #SBATCH --partition=short
  <commands to execute>
Job request: one node with exclusive use of a node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you need exclusive use of a node, such as when you have a job that has high I/O requirements, you can use the exclusive flag. The example script below specifies exclusive use of 1 node in the short partition for four hours. ::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --exclusive
  #SBATCH --partition=short
  <commands to execute>
Example Parallel Job Scripts
----------------------------
Parallel jobs should be used with code that is configured to use the reserved resources. If your code is not optimized for running in parallel, your job could fail. The following script examples all allocate additional memory. The default memory per allocated core is 1GB. If your calculations try to use more memory than what is allocated, Slurm automatically terminates your job. You should request a specific amount of memory in your job script if your calculations
need more memory than the default.

8-task job, one node and additional memory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --ntasks-per-node=8
  #SBATCH --cpus-per-task=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --mem=100G
  #SBATCH --partition=short
  <commands to execute>

8-task job, multiple nodes and additional memory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

  #!/bin/bash
  #SBATCH --nodes=4
  #SBATCH --ntasks-per-node=2
  #SBATCH --cpus-per-task=1
  #SBATCH --time=00:30:00
  #SBATCH --job-name=MyJobName
  #SBATCH --mem=100G
  #SBATCH --partition=express
  <commands to execute>


Using Arrays
------------

Using a job array can often help in situations where you need to submit multiple similar jobs. To use an array with your jobs, in your ``sbatch`` script, use the ``array=`` option.

For example, if you want to run a 10 job array, one job at a time, you would add the following line to your sbatch script:

``#SBATCH --array=1-10%1``

For more information on this command, go to the `Slurm documentation`_.


.. _Slurm documentation: https://slurm.schedmd.com/documentation.html