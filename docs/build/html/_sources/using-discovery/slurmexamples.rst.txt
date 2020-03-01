.. _slurm_examples:

***************
Slurm examples
***************

You can submit jobs using ``srun`` or ``sbatch``. ``srun`` is for submitting interactive jobs, while you use ``sbatch`` with a script.
You should review the examples on this page to have a general understanding of the types
of jobs you can submit to the scheduler.

Refer to the official Slurm documentation for more information about these
commands and their options: https://slurm.schedmd.com.

SRUN Examples
=============

Use ``srun`` to start an interactive job. Note that you need to use ``squeue -u <yourusername>`` after you submit an interactive job
to view the job.

A simple ``srun`` example is to move to a compute node after you first log into Discovery. ::

  srun --pty /bin/bash

To allocate one node (N 1), one core (n 1) for 30 minutes with X11 forwarding on the short partition (p short), type::

  srun -p short --pty --export=ALL -n 1 -N 1 --x11 --mem=10Gb --time=00:30:00 /bin/bash

When Discovery has maintenance, you can specify the ``t2sd`` ("time to shutdown") script with the ``--time`` option along with your usual SRUN options::   

  srun --time=$( t2sd )

SBATCH Examples
===============

1-core job
~~~~~~~~~~

Run a 1-core job for 4 hours on the short partition::

  #!/bin/bash
  #SBATCH –nodes=1
  #SBATCH –time=4:00:00
  #SBATCH –job-name=MyJobName
  #SBATCH –partition=short
  <commands to execute>

1-core job and additional memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


1-core job with exclusive use of a node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

8-task job, one node and additional memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

8-task job, multiple nodes and additional memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
