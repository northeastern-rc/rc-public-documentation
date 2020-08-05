.. _using_srun:

***********
Using srun
***********
You can use the Slum command ``srun`` to allocate an interactive job. This means you use specific options with ``srun``
on the command line to tell Slurm what resources you need to run your job, such as number of nodes, amount of memory, and amount of
time. After typing your ``srun`` command and options on the command line and pressing enter, Slurm will find and then allocate the resources
you specified. Depending on what you specified, it can take a few minutes for Slurm to allocate those resources. You can view all of the
``srun`` options on the `Slurm documentation website <https://slurm.schedmd.com/archive/slurm-17.11.6/srun.html>`_.

The following is an example of an ``srun`` command as run on a command line.

.. image:: /images/srun_example.jpg

``srun`` examples
==================
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

 srun --partition=express  --nodes 2 --ntasks 10 --cpus-per-task 2 --pty --export=ALL --mem=1G --time=01:00:00 /bin/bash

To allocate a GPU node, you should specify the ``gpu`` partition and use the --gres option::

 srun --partition=gpu --node=node 1 --ntasks=1 --export=ALL --gres=gpu:1 --mem=1Gb --time=01:00:00 --pty /bin/bash

For more information about working with GPUs, see :ref:`working_gpus`.

When Discovery has maintenance, you can specify the ``t2sd`` ("time to shutdown") script with the ``--time`` option along with your usual SRUN options::

 srun --time=$( t2sd )

Monitor your jobs
~~~~~~~~~~~~~~~~~~
You can monitor your jobs by using the Slurm ``scontrol`` command. Type ``scontrol show jobid -d <JOBID>``, where ``JOBID`` is the number of your job.
In the figure at the top of the page, you can see that when you submit your ``srun`` command, Slurm displays the unique ID number of your job (``job 12962519``).
This is the number you use with ``scontrol`` to monitor your job.
