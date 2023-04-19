.. _hardware_overview:

******************
Hardware overview
******************
The Discovery cluster provides you with access to over 1024 CPU nodes, 50,000 CPU cores, and over 200 GPUs. Discovery is connected
to the university network over 10 Gbps Ethernet (GbE) for high-speed data transfer.
Compute nodes are connected to each other with either 10 GbE or a high-performance HDR200 InfiniBand (IB) interconnect
running at 200 Gbps (with some nodes running HDR100 IB, if HDR200 IB is not supported on those nodes).

CPU nodes
=================================
Table 1 shows the feature names, number of nodes by partition type (public, private, and total), and the RAM memory range per node. The feature name follows archspec microachitecture specification (https://archspec.readthedocs.io/en/latest/index.html)

**Table 1: CPU Nodes**

.. list-table::
  :widths: 30 10 5
  :header-rows: 1

  * - Feature Name
    - Number of Nodes (public, private, total)
    - RAM memory per node
  * - skylake
    - 0, 170, 170
    - 186 - 3094 GB
  * - zen2
    - 40, 292, 332
    - 256 - 2000 GB
  * - zen
    - 40, 300, 340
    - 256 - 2000 GB
  * - ivybridge
    - 64, 130, 194
    - 31 - 1031 GB
  * - sandybridge
    - 8, 0, 8
    - 384 GB
  * - haswell
    - 230, 62, 292
    - 109 - 1031 GB
  * - broadwell
    - 756, 226, 982
    - 128 - 515 GB
  * - cascadelake
    - 260, 88, 340
    - 186 - 3094 GB

If you are looking for information about GPUs, see :ref:`working_gpus`.

If you are looking for information about the partitions on Discovery, see :ref:`partition-names`. You can view more information about what is currently available on each node on a desired partition at :ref: `viewing-partition-info`. 


Using the ``--constraint`` flag
================================
When using ``srun`` or ``sbatch``, you can specify specific hardware features as part of your job by using the ``--constraint=`` flag. Currently, you can use the ``--constraint=`` flag to restrict your job to a specific feature name (e.g., ``haswell``, ``ivybridge``) or you can use the flag: ``ib`` to only include nodes that are connected by InfiniBand (IB) with a job that needs to use multiple nodes. See below for a few simple examples using ``srun``. You can add the same flag as an additional line in your ``sbatch`` script via (``#SBATCH --constraint=haswell``)::

        srun --constraint=haswell --pty /bin/bash
        srun --constraint=ivybridge --pty /bin/bash
        srun --constraint=ib --pty /bin/bash  
        srun --constraint="[ivybridge|zen2]" --pty /bin/bash #this uses the OR operator | to select either an ivybridge or zen2 node. 

Note, using a constraint can mean that you will wait longer for your job to start, as the scheduler (Slurm) will need to find and allocate the appropriate hardware that you have specified for your job. For more information about running jobs, see :ref:`using_slurm`. Finally, at this time only the OR operator ``|`` is supported when using ``--contraint``. 


