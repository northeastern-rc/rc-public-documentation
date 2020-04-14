
.. _partition_names:

**********
Partitions
**********
:sub:`Updated April 3, 2020`

.. note::
   As of February 2020, the partition names were updated. You should refer to the table below for
   the most current partition names to use with your submission scripts.

The Discovery cluster is sectioned into virtual partitions. The partitions available for general use
are debug, express, short, and gpu. Each partition consists of several processor architectures and different compute node counts.
There are also partitions that are reserved for individual faculty members.
Three partitions, long, large, and multigpu, are accessible only after application approval
For more information see :ref:`partition_access` and the RC website: https://rc.northeastern.edu/policy/.

.. note::
   In the following table, the Running Jobs Per User/Per Research Group. RAM limit is per user, across all jobs.

.. list-table::
   :widths: 20 20 20 20 30 20 20
   :header-rows: 1

   * - Name
     - Requires approval?
     - Time limit (default/max)
     - Running jobs
     - Submitted jobs
     - Core limit
     - RAM limit
   * - debug
     - No
     - 20 minutes/20 minutes
     - 10/25
     - 5000
     - 128
     - 256GB
   * - express
     - No
     - 30 minutes/60 minutes
     - 50/250
     - 5000
     - 2048
     - 25TB
   * - short
     - No
     - 4 hours/24 Hours
     - 50/500
     - 5000
     - 1024
     - 25TB
   * - long
     - **Yes**
     - 1 day/5 Days
     - 25/250
     - 1000 per user/5000 per group
     - 1024
     - 25TB
   * - large
     - **Yes**
     - 6 hours/6 Hours
     - 100/100
     - 1000 per user/5000 per group
     - N/A
     - N/A

.. list-table::
   :widths: 20 20 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Requires approval?
     - Time limit (default/max)
     - Running jobs
     - Submitted jobs
     - GPU per job limit
     - GPU per user limit
   * - gpu
     - No
     - 4 hours/8 Hours
     - 25/250
     - 50/100
     - 1
     - 8
   * - multigpu
     - **Yes**
     - 4 hours/24 Hours
     - 25/100
     - 50/100
     - 12
     - 12

You can view all of the partitions by using the Slurm command ``sinfo -a``. To specify a partition in
your job submission script, use the option ``--partition=<partition name>``.
For more information about Slurm, see :ref:`using_slurm`.

.. _partition_access:

Partition Access Request
==========================

If you need access to the large, long, or multigpu partition, you need to submit a `ServiceNow ticket <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7>`_.
Access is not automatically granted. You will need to provide details and test results that demonstrate your need for access for these partitions.
If you need temporary access to multigpu to perform testing before applying for permanent access,
you should also submit a `ServiceNow ticket <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7>`_. All requests are evaluated by members of the RC team,
and multigpu requests are also evaluated by two faculty members.
