.. _using_sbatch:

*************
Using sbatch
*************

You use the ``sbatch`` command with a bash script to specify the
resources you need to run your jobs, such as the number of nodes you want to run your jobs
on and how much memory you’ll need. Slurm then schedules your job based on the
availability of the resources you’ve specified.
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
================

Job requesting one node
~~~~~~~~~~~~~~~~~~~~~~~

Run a job on one node for 4 hours on the short partition::

  #!/bin/bash
  #SBATCH –-nodes=1
  #SBATCH –-time=4:00:00
  #SBATCH –-job-name=MyJobName
  #SBATCH –-partition=short
  <commands to execute>

Job requesting one node and additional memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


Job requesting one node with exclusive use of a node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
  #SBATCH --time=00:30:00
  #SBATCH --job-name=MyJobName
  #SBATCH --mem=100Gb
  #SBATCH --partition=express
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
