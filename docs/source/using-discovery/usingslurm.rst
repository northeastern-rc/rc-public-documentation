.. _using_slurm:

***********
Using Slurm
***********
.. contents:: Table of Contents
   :depth: 4

Slurm (Simple Linux Utility Resource Management) is the software on Discovery that lets you do the following:

* view information about the cluster
* schedule your jobs on Discovery
* monitor your jobs
* view information about your account
* check the state of the cluster and specific nodes

.. important::
   Slurm commands have numerous options to help your jobs run efficiently by requesting specific resources. Options usually have short and verbose versions, such as ``--nodes`` and ``-n`` (both mean the same thing). The examples in this documentation all use the verbose version of the options for clarity, but you can use the short version if you prefer. For example, ``srun -p short -N 1 -n 1`` means the same thing as ``srun --partition=short --nodes=1 --ntasks=1`` Refer to the official Slurm documentation to get in-depth information about these commands and their options: `Slurm documentation`_.

SLURM Commands
==============
List of typical Slurm commands for working on Discovery.

These functions are fully documented for the version of SLURM installed on in the manual pages. To get the manual pages for the SLURM functions, run::

   man <SLURM_command>
on the HPC which lists all the parameters and keywords that you can use with the given SLURM commands. You can also run::

   <SLURM_command> --help
which will list the help page for the SLURM function. These two give you the full possibilities of what these functions can do. The following sections are helpful/commonly used SLURM commands that are good to know for different ticket requests and common checks on the cluster.
Controlling Jobs
----------------
``scontrol hold <jobid>`` Place a hold on a pending job

``scontrol release <jobid>`` Release a held job

``scontrol requeue <jobid>`` Requeue a completed, failed, or cancelled job

Job Reporting
-------------
``sacct <options>`` Display job accounting information

``sreport <options>`` Generate reports about cluster utilization and job statistics

Advanced Features
------------------
``sprio <options>`` Show the priority of jobs and job steps

``sburst <options>`` Show the state of all burst buffer pools

**NOTE:** Each command's options and functions may vary depending on the Slurm version and configuration. We recommend consulting the Slurm documentation for more information on the full range of available commands and their usage.

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

.. _using_srun:
Using srun
-----------
Use the Slum command ``srun`` to allocate an interactive job. This means you use specific options with ``srun`` on the command line to tell Slurm what resources are needed to run your job, such as number of nodes, amount of memory, and amount of time. Enter ``srun`` command and options on the command line, the and press ``Return``. Slurm will find and then allocate the specified resources. Depending on the specifications, it may take a few minutes. All ``srun`` options can be found in the `Slurm documentation`_.

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

.. _using_sbatch:
Using sbatch
------------
You use the ``sbatch`` command with a bash script to specify the
resources you need to run your jobs, such as the number of nodes wanted to run jobs on and the amount of memory required. Slurm then schedules your job based on the available resources specified.

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
^^^^^^^^^^^^^^^

Job request: one node
~~~~~~~~~~~~~~~~~~~~~
Run a job on one node for 4 hours on the short partition::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --partition=short
  <commands to execute>

Job request: one node with additional memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The default memory per allocated core is 1GB. If calculations attempt to access more memory than allocated, Slurm automatically terminates thw job. Request a specific amount of memory in the job script if calculations require more than the default. The example script below requests 100GB of memory (``--mem=100G``). Use one capital letter to abbreviate the unit of memory (K, M, G, T) with the ``--mem=`` option, as that is what Slurm expects to see. ::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --mem=100G
  #SBATCH --partition=short
  <commands to execute>
Job request: one node with exclusive use of a node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you need exclusive use of a node, such as when you have a job that has high I/O requirements, you can use the exclusive flag. The example script below specifies the exclusive use of 1 node in the short partition for four hours. ::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --exclusive
  #SBATCH --partition=short
  <commands to execute>
Example Parallel Job Scripts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Parallel jobs should use code configured to use the reserved resources. Running unoptimized code in parallel could fail. The following script examples all allocate additional memory. The default memory per allocated core is 1GB. If your calculations try to use more memory than allocated, Slurm automatically terminates your job. You should request a specific amount of memory in your job script if your calculations need more than the default.

8-task job, one node and additional memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
^^^^^^^^^^^^

Using a job array can often help in situations where you need to submit multiple similar jobs. To use an array with your jobs, in your ``sbatch`` script, use the ``array=`` option.

For example, if you want to run a 10 job array, one job at a time, you would add the following line to your sbatch script:

``#SBATCH --array=1-10%1``

For more information on this command, go to the `Slurm documentation`_.

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

You can monitor your jobs by using the Slurm ``scontrol`` command. Type ``scontrol show jobid -d <JOBID>``, where ``JOBID`` is the number of your job. In the figure at the top of the page, you can see that when you submit your ``srun`` command, Slurm displays the unique ID number of your job (``job 12962519``). This is the number you use with ``scontrol`` to monitor your job.

Account information
====================

Some Discovery users have more than one Discovery group account associated with their usernames. For example, a student might be in a class using Discovery and a student club using Discovery for a club project. In this case, the student would have two group accounts associated with their username.

When running a job with either ``srun`` or ``sbatch``, if you have more than one account associated with your username, we recommend you use the ``--account=`` flag and specify the account that corresponds to the respective project. In the example with a student associated with a class and a student club, if the student is on Discovery submitting a job for a project for their class, set the ``account=`` flag to the name of the class account. If the student is working on a project for the club, set the ``account=`` flag to the name of the student club account.

To find out what account(s) your username is associated with, use the following command::

  sacctmgr show associations user=<yourusername>
After you have determined what accounts your username is associated with, if you have more than one account association, you can use the ``account=`` flag with your usual ``srun`` or ``sbatch`` commands.

For example, if you are associated with an account named ``dataclub`` and an account named ``info7500``, and you're currently doing work that should be associated with the ``dataclub`` account, in your ``srun`` command, you can add the ``--account=dataclub`` flag to specify that account.::

  srun --account=dataclub --partition=short --nodes=1 --ntasks=28 --mem=0 --pty /bin/bash
.. note::
   If you do not have more than one account associated with your username, you do not need to use the ``--account=`` flag. Most users on Discovery have only one account associated with their username.

State of the Cluster and Specific Nodes
=======================================
Here are some more examples of using ``sinfo`` and ``scontrol`` to provide information about the state of the cluster and specific nodes:

Using sinfo
-----------
The ``sinfo`` command will show information about all partitions in the cluster, including the partition name, available nodes, and status. By default, ``sinfo`` reports:

.. list-table::
   :widths: 20 100
   :header-rows: 0

   * - ``PARTITION``
     - The list of the cluster’s partitions. It’s a set of compute nodes grouped logically
   * - ``AVAIL``
     - The active state of the partition. (up, down, idle)
   * - ``TIMELIMIT``
     - The maximum job execution walltime per partition.
   * - ``NODES``
     - The total number of nodes per partition.
   * - ``STATE``
     - See STATE table below.
   * - ``NODELIST(REASON)``
     - The list of nodes per partition.

**STATE Table**

.. list-table::
   :widths: 20 100
   :header-rows: 1

   * - State
     - Description
   * - ``mix``
     - Only part of the node is allocated to one or more jobs and the rest in an Idle state.
   * - ``alloc``
     - The entire resource on the node(s) is being utilized.
   * - ``idle``
     - The node is in an idle start and has none of it’s resources being used.
Example Uses
^^^^^^^^^^^^
View information about all partitions::

   $ sinfo -a
Or, a specific partition::

   $ sinfo -p gpu
   PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
   gpu          up    8:00:00      5 drain* c[2171,2184,2188],d[1008,1014]
   gpu          up    8:00:00      3  down* c2162,d[1006,1017]
   gpu          up    8:00:00      1  drain d1025
   gpu          up    8:00:00      2   resv c2177,d1029
   gpu          up    8:00:00     50    mix c[2160,2163-2170,2172-2176,2178-2179,2185-2187,2189-2195,2204-2207],d[1001,1003-1005,1007,1009-1013,1016,1018,1020-1024,1026-1028]
   gpu          up    8:00:00      3  alloc d[1002,1015,1019]
   gpu          up    8:00:00      4   idle c[2180-2183]
which give all the nodes and the states the nodes are in at the current time.

The current TimeLimit for the queues::

   sinfo  -o "%12P %.10A %.11l"
   PARTITION    NODES(A/I)   TIMELIMIT
   debug           402/174       20:00
   express         403/180     1:00:00
   short*          401/178  1-00:00:00
   long             224/47  5-00:00:00
   large           376/172     6:00:00
   gpu               41/17     8:00:00
   multigpu          41/17  1-00:00:00
   lowpriority     118/102  1-00:00:00
   reservation     617/402 100-00:00:0
   ai-jumpstart       2/15  2-00:00:00
   allshouse           5/7    infinite
   bansil             15/4 30-00:00:00
   ce-mri             3/10 30-00:00:00
   chen               0/12 30-00:00:00
   ctbp               0/20 30-00:00:00
   .
   .
   .
View information about a specific partition::

   sinfo -p <partition_name>
Or, only view nodes in a certain state::

   sinfo -p <partition> -t <state>
For example::

   $ sinfo -p gpu -t idle
   PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
   gpu          up    8:00:00      1  drain d1025
   gpu          up    8:00:00      2   resv c2177,d1029
   gpu          up    8:00:00     13   idle c[2160,2163-2164,2166,2168-2170,2175,2179-2183]
This command will show information about a specific partition in the cluster, including the number of nodes, number of free nodes, and state of the partition.

You can use the ``--Format`` flag to get more information or a specific format for the output::

   sinfo -p <partition> -t idle --Format=gres,nodes
For example::

   $ sinfo -p gpu -t idle --Format=gres,nodes
   GRES                NODES
   gpu:t4:4(S:0-1)     1
   gpu:k80:8(S:0-1)    5
   gpu:a100:4          1
   gpu:k40m:1          8
   gpu:k80:7(S:0-1)    1
gpu:a100:4 - The number after : i.e 4 indicates that 1 node has 4 gpu:a100s.

View detailed information about nodes::

   sinfo -N -l
This command will show detailed information about all nodes in the cluster, including the node name, state, CPU architecture, memory, and available features.

View what features a node has::

   sinfo -n <node> --Format=nodes,nodelist,statecompact,features
For Example::

   $ sinfo -n d0139 --Format=nodes,nodelist,statecompact,features
   NODES               NODELIST            STATE               AVAIL_FEATURES
   1                   d0139               mix                 zen2,ib,prod
View what nodes have what features in a partition::

   sinfo -p <partition> --Format=nodes,cpus,features,nodelist
For example::

   $ sinfo -p short --Format=nodes,cpus,features,nodelist
   NODES               CPUS                AVAIL_FEATURES      NODELIST
   13                  28                  broadwell,next      c[0699-0711]
   8                   56                  ib,cascadelake,next d[0001-0008]
   120                 56                  ib,cascadelake,prod d[0009-0128]
   32                  20                  ivybridge,prod      c[3000-3006,3008-303
   115                 24                  lenovo,rapl,haswell,c[0156,0158-0159,016
   381                 28                  broadwell,prod      c[0336-0343,0376-040
   4                   16                  sandybridge,largememc[2000-2003]
   2                   112                 cascadelake,ib,prod d[0129-0130]
   20                  128                 zen2,ib,prod        d[0131-0150]
View what nodes are in what state in a partition using ``statecompact``::

   sinfo -p lopez --Format=time,nodes,statecompact,features,memory,cpus,nodelist
Using scontrol
--------------
The ``scontrol`` command is used for monitoring and modifying queued, running jobs, and reservations.

Example Uses
^^^^^^^^^^^^
View information about a specific node::

   scontrol show node -d <node_name>
For example::

   $ scontrol show node -d c2180
   NodeName=c2180 Arch=x86_64 CoresPerSocket=14
   CPUAlloc=0 CPUTot=28 CPULoad=0.01
   AvailableFeatures=broadwell,prod
   ActiveFeatures=broadwell,prod
   Gres=gpu:k80:7(S:0-1)
   GresDrain=N/A
   GresUsed=gpu:k80:0(IDX:N/A)
   NodeAddr=c2180 NodeHostName=c2180 Version=21.08.8-2
   OS=Linux 3.10.0-1160.25.1.el7.x86_64 #1 SMP Wed Apr 28 21:49:45 UTC 2021
   RealMemory=512000 AllocMem=0 FreeMem=486591 Sockets=2 Boards=1
   State=IDLE ThreadsPerCore=1 TmpDisk=0 Weight=6 Owner=N/A MCS_label=N/A
   Partitions=gpu,multigpu,reservation
   BootTime=2022-12-14T07:23:47 SlurmdStartTime=2022-12-23T07:40:56
   LastBusyTime=2023-01-19T14:40:02
   CfgTRES=cpu=28,mem=500G,billing=728,gres/gpu=7
   AllocTRES=
   CapWatts=n/a
   CurrentWatts=0 AveWatts=0
   ExtSensorsJoules=n/s ExtSensorsWatts=0 ExtSensorsTemp=n/s
For information on all reservations::

   scontrol show reservations
This command will show information about a specific node in the cluster, including the node name, state, number of CPUs, and amount of memory.

View information about a specific job::

   scontrol show job <job_id>
This command will show information about a specific job, including the job ID, state, user name, and partition name.

View information about a specific reservation::

   scontrol show reservation <reservation_name>
This command will show information about a specific reservation in the cluster, including the reservation name, start time, end time, and nodes included in the reservation.

These are just a few examples of what you can do with ``sinfo`` and ``scontrol`` to view information about the state of the cluster and specific nodes. There are many other options and commands available, and it is recommended to consult the `Slurm documentation`_ for more information on how to use these tools effectively.


Best Practices
===============
#. Use the proper resource request syntax: Slurm uses a specific syntax to request resources, such as the number of CPUs, memory, and time required for your job. Make sure to use the proper syntax to avoid any errors.
#. Specify an appropriate job name: Giving your job a descriptive name will help you and other users identify it easily.
#. Submit jobs using batch scripts: It's best to submit jobs using batch scripts instead of typing commands manually. Batch scripts allow you to automate the process and make it easier to run multiple jobs at once.
#. Use the correct partition: Slurm HPC has several partitions, each designed for specific purposes. Choose the proper partition for your job to ensure you use the most appropriate resources.
#. Monitor your job's progress: Keep an eye on your job's progress to ensure it's running correctly and identify any issues that may arise.
#. Avoid overloading the system: Be mindful of the resources you're requesting and avoid overloading the system, as it ensures that other users have access to the resources they need.
#. Use checkpoints: If your job is long-running, consider using checkpoints to save your progress, allowing for resuming jobs if interrupted.
#. Use environment modules: Slurm uses environment modules to manage software installations. Make sure to load the appropriate modules before running your job.
#. Use the appropriate file system: Slurm HPC typically has several file systems with different performance characteristics. Use the proper file system for your job to ensure you get the best performance.
#. Please clean up after your job: Make sure to remove any files or directories that your job created after it's finished running. It helps keep the system clean and frees up resources for other users.

.. _Slurm documentation: https://slurm.schedmd.com/documentation.html