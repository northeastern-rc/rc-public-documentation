*******************************************************
Home Directory Storage Quota
*******************************************************
There are strict quotas for each home directory (i.e., ``/home/<username>``), and staying within the quota is vital for preventing issues on the HPC. This page provides some best practices for keeping within the quota. For more information about data storage on the HPC, see :ref:`discovery_storage`.

.. important::
  All commands on this page should be run from a compute node because they are cpu intensive. You can find more information on getting a job on a compute node from :ref:`_using_srun`.


Analyze Disk Usage
=======================================================
From a compute node, run the following command from your ``/home/<username>`` directory: ::
    
 du -shc .[^.]* ~/*

This command will output the size of each file, directory, and hidden directory in your ``/home/<username>`` space, with the total of your ``/home`` directory being the last line of the output. After identifying the large files and directories, you can move them to the appropriate location, (g.g., ``/work`` for research) or you can back up and delete the files and directories if they are no longer required. An example output would look like:

.. code-block:: bash
  :emphasize-lines: 6
  
  [<username>@<host> directory]$  du -shc .[^.]* ~/*
  39M	  .git
  106M	discovery-examples
  41K	  README.md
  3.3M	software-installation
  147M	total

Utlilize /scratch and /work
=======================================================
Use ``/work`` for long-term storage. PIs can request a folder in ``/work`` via `New Storage Space Request <https://bit.ly/NURC-NewStorage>`_, and they can request additional storage via `Storage Space Extension Request <https://bit.ly/NURC-StorageExtension>`_. Utilize ``/scratch/<username>`` for temporary or intermediate files. Then, move files from ``/scratch`` to ``/work`` for persistent storage (i.e., the recommended work flow).

.. note::
    Please be mindful of the ``/scratch`` purge policy, which can be found on the [Research Computing Policy Page](https://rc.northeastern.edu/policy/). See :ref:`discovery_storage` for information on ``/work`` and ``/scratch``.

Conda Directory
=======================================================
.. note::
  Conda environments are part of your research and should preferably be stored in your PI's ``/work`` directory. 

Here are some suggestions to reduce the storage size of the environments for those using the ``/home/<username>/.conda`` directory.

Remove unused packages and clear caches of conda by loading an anaconda module and running the following: ::

 source activate <your environment>
 conda clean --all

This will only delete unused packages in your ``~/.conda/pkgs`` directory.

To remove any unused conda environments, run: ::

 conda env list
 conda env remove --name <your environment>

Singularity Directory
=======================================================
If you have pulled any containers to the HPC using Singularity, you can clean your container cache in your ``/home/<username>`` directory by running the following command from a compute node: ::

 module load singularity/3.5.3
 singularity cache clean all

To avoid your ``~/.singularity`` directory filling up, you can set a temporary directory for when you pull containers to store the cache in that location; an example of this procedure, (where ``<project>`` is your PI's ``/work`` directory) is: ::

 mkdir /work/<project>/singularity_tmp
 export SINGULARITY_TMPDIR=/work/<project>/singularity_tmp

Then, pull the container using singularity as usual.

Cache Directory
=======================================================
The ``~/.cache`` directory can become large over time with general use of the HPC and Open OnDemand. Make sure you are not running any processes or jobs at the time by running: ::
 
 squeue -u <username>

which prints a table with ``JOBID``, ``PARTITION``, ``NAME``, ``USER ST``, ``TIME``, ``NODES``, and ``NODELIST (REASON)`` which is empty when no jobs are running (i.e., it is safe to remove ``~/.cache`` when no jobs are running). 

Best Practices
=======================================================

Conda environments
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Use conda environments for python on HPC. To create an environment in ``/work``, use the ``--prefix`` flag as follows: (where ``<project>`` is your PI's ``/work`` directory and ``<my conda env>`` is an empty directory to store your conda environment): ::

 conda create --prefix=/work/<project>/<my conda env>

More information about creating custom conda environments can be found here :ref:`working_conda`. 

Utilize the same conda environment to save storage space and time (i.e., avoiding duplicate conda environments). Hence, shared environments can be easily done for a project accessing the same ``/work`` directory. For more information about creating custom conda environments, see :ref:`working_conda`. 

Singularity containers
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Containers that are pulled, built and maintained for research work should be stored in your PI's ``/work`` directory, not in your ``/home/<username>`` directory. 
