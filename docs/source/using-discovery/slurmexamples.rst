.. _slurm_examples:

***************
Slurm examples
***************

The following are example job scripts for submitting to Slurm using the ``sbatch``
command. You should review these to have a general understanding of the types
of jobs you can submit to the scheduler.

1-core job
==========

Run a 1-core job for 4 hours on the short partition::

  #!/bin/bash
  #SBATCH –nodes=1
  #SBATCH –time=4:00:00
  #SBATCH –job-name=MyJobName
  #SBATCH –partition=short
  <commands to execute>

1-core job and additional memory
=================================

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
========================================

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
=============================

Parallel jobs should be used with code that is configured to use the reserved resources.
If your code is not optimized for running in parallel, your job could fail.
The following script examples all allocate additional memory.
The default memory per allocated core is 1GB. If your calculations try to use more
memory than what is allocated, Slurm automatically terminates your job.
You should request a specific amount of memory in your job script if your calculations
need more memory than the default.

8-task job, one node and additional memory
============================================

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
==================================================

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

8-task job, multiple nodes, additional memory, and exclusive
=============================================================

If you need exclusive use of a node, such as when you have a job that has
high I/O requirements, you can use the exclusive flag.::

 #!/bin/bash
 #SBATCH --nodes=4
 #SBATCH --tasks-per-node=2
 #SBATCH --time=4:00:00
 #SBATCH --job-name=MyJobName
 #SBATCH --mem=100Gb
 #SBATCH --exclusive
 #SBATCH --partition=short
 <commands to execute>
