.. _slurm_examples:

***************
Slurm examples
***************

You can submit jobs using ``srun`` or ``sbatch``. ``srun`` is for submitting interactive jobs, while you use ``sbatch`` with a script.
You should review the examples on this page to have a general understanding of the types
of jobs you can submit to the scheduler.

Refer to the official Slurm documentation for more information about these
commands and their options: https://slurm.schedmd.com.

``SRUN`` Examples
=================

Use `srun <https://slurm.schedmd.com/srun.html>`_ from the terminal (see: :ref:`intro_connect`) to start an interactive job. 

A simple interactive session
+++++++++++++++++++++++++++++

A simple ``srun`` example is to move to a compute node after you first log into Discovery. 

.. code-block:: console

   [<USERNAME>@login-00 ~]$ srun --pty /bin/bash

Note the ``$`` and everything before it is what you will see at the command line in the terminal. You do not need to type that, it is showing you your username and the machine you are SSH'd into.

**Explanation of command:**

  * ``srun`` - Run a slurm job.
  * ``--pty /bin/bash`` - After provisioning the job, move the terminal to into the new node.

After running this command you should see that the job has been submitted

.. code-block:: console

   srun: job <JOB_NUMBER> queued and waiting for resources

and then after a few moments, the job should start after the resources have been allocated

.. code-block:: console

   srun: job <JOB_NUMBER> has been allocated resources
   [<USERNAME>@<COMPUTE_NODE> ~]$ 

Note how the text before the ``$`` changed, indicating that the terminal switched from the log-in remote machine to the compute node provisioned for this interactive job. From here you can execute your compute commands on the compute node. 


Specifying interactive session paramters
+++++++++++++++++++++++++++++++++++++++++

The number of nodes, cores, run time, X11 forwarding, memory, and gpus can all be controlled with the ``srun`` command. 

To allocate one node (N 2), one core (n 3) for 30 minutes with X11 forwarding on the short partition (p short), type.

.. code-block:: console

   $ srun -p short --export=ALL -n 2 -N 3 --mem=10Gb --time=00:30:00 --x11 --pty /bin/bash

**Explanation of command:**

  * ``srun`` - Run a slurm job.
  * ``-p short`` - Request the ``short``  partition (i.e., type of compute node) for the resource allocation. Different resources will be available on different types of partitions. See :ref:partition_names for a list of partitions available on Discovery 
  * ``-n 3`` - Specify that three tasks will be run, so specify at least 3 CPU cores.
  * ``-N 2`` - Specify that two compute nodes should be provisioned.
  * ``--mem=10Gb`` - Specify that a minimum of 410GB of memory should be allocated to the job.
  * ``--time=00:30:00`` - The job will request only 30 minutes of wall clock run time, after which the job will be automatically terminated. 
  * ``--x11`` - Enable graphical interfaces to be forwared through the SSH connection using the `X Window System <https://en.wikipedia.org/wiki/X_Window_System>`_.
  * ``--export=ALL`` - Export all of the users environment variables to the loaded environment. (This is the default behavior and probably not necessary.)
  * ``--pty /bin/bash`` - After provisioning the job, move the terminal to into the new node.

Allocating a GPU node
++++++++++++++++++++++

To allocate a GPU node, you should specify the ``gpu`` partition and use the --gres option

.. code-block:: console

   $ srun -p gpu --gres=gpu:1 --pty /bin/bash

**Explanation of command:**

  * ``srun`` - Run a slurm job.
  * ``-p gpu`` - Request a ``gpu`` partition
  * ``--gres=gpu:1`` - Request one gpu resource
  * ``--pty /bin/bash`` - After provisioning the job, move the terminal to into the new node.

Other interactive session commands
+++++++++++++++++++++++++++++++++++

Note that you need to use ``squeue -u <yourusername>`` after you submit an interactive job
to view the job.

When Discovery has maintenance, you can specify the ``t2sd`` ("time to shutdown") script with the ``--time`` option along with your usual SRUN options

.. code-block:: console

   $ srun --time=$( t2sd )

SBATCH Examples
===============

`sbatch <https://slurm.schedmd.com/sbatch.html>`_ will submit a batch script to Slurm to run without showing an interactive terminal to the user. 

Core job
+++++++++++

Run a 1-core job for 4 hours on the short partition::

  #!/bin/bash
  #SBATCH –nodes=1
  #SBATCH –time=4:00:00
  #SBATCH –job-name=MyJobName
  #SBATCH –partition=short
  <commands to execute>

Core job and additional memory
+++++++++++++++++++++++++++++++

The default memory per allocated core is 1GB. If your calculations try to use
more memory than what is allocated, Slurm automatically terminates your job.
You should request a specific amount of memory in your job script if your
calculations need more memory than the default. The example script below is
requesting 100GB of memory (mem=100Gb).::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --mem=100Gb
  #SBATCH --partition=short
  <commands to execute>


Core job with exclusive use of a node
++++++++++++++++++++++++++++++++++++++

If you need exclusive use of a node, such as when you have a job that has high
I/O requirements, you can use the exclusive flag. The example script below
specifies exclusive use of 1 node in the short partition for four hours.::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --exclusive
  #SBATCH --partition=short
  <commands to execute>

Example Parallel Job Scripts
============================

Parallel jobs should be used with code that is configured to use the reserved resources.
If your code is not optimized for running in parallel, your job could fail.
The following script examples all allocate additional memory.
The default memory per allocated core is 1GB. If your calculations try to use more
memory than what is allocated, Slurm automatically terminates your job.
You should request a specific amount of memory in your job script if your calculations
need more memory than the default.

Task job, one node and additional memory
+++++++++++++++++++++++++++++++++++++++++

::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --tasks-per-node=8
  #SBATCH --cpus-per-task=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --mem=100Gb
  #SBATCH --partition=short
  <commands to execute>

Task job, multiple nodes and additional memory
+++++++++++++++++++++++++++++++++++++++++++++++

::

  #!/bin/bash
  #SBATCH --nodes=4
  #SBATCH --tasks-per-node=2
  #SBATCH --cpus-per-task=1
  #SBATCH --time=4:00:00
  #SBATCH --job-name=MyJobName
  #SBATCH --mem=100Gb
  #SBATCH --partition=short
  <commands to execute>


Using Arrays
=============

Using a job array can often help in situations where you need to submit multiple similar jobs.
To use an array with your jobs, in your sbatch script, use the ``array=`` option.

For example, if you want to run a 10 job array, one job at a time, you would add the following
line to your sbatch script:

``#SBATCH --array=1-10%1``

Go `here <https://slurm.schedmd.com/job_array.html>`_ for more information about using the
``array=`` option.
