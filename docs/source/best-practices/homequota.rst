*******************************************************
Storage Quota at /home/
*******************************************************
Staying under your ``/home/<username>`` quota is vital in preventing issues using Open OnDemand and performing tasks on Discovery. Here are some suggestions to stay under quota and general best practices with using your ``/home/<username>`` directory.

Analyze disk usage
=======================================================
From a compute node, ``srun --pty /bin/bash``, run the following command from your ``/home/<username>`` directory: ::
    
 du -shc .[^.]* *

This command will output the size of each file, directory, and hidden directory in your ``/home/<username>`` space, with the total of your ``/home`` directory being the last line of the output. After identifying the large files and directories, you can move them to the appropriate location, (g.g., ``/work`` for research) or you can back up and delete the files and directories if they are no longer required.

Utlilize /scratch and /work
=======================================================
For long-term research work storage, ``/work`` should be used. If your PI does not have space in ``/work`` setup, they can request ``/work`` using the `New Storage Space Request <https://bit.ly/NURC-NewStorage>`_. PIs can also request additional storage using the `Storage Space Extension Request <https://bit.ly/NURC-StorageExtension>`_. More details of ``/work`` can be found at :ref:`discovery_storage`. 

For temporary job files, you can utilize ``/scratch/<username>``. Please be mindful of the ``/scratch`` purge policy, which is can be found on the `Research Computing Policy Page <https://rc.northeastern.edu/policy/>`_.

Clean ~/.conda directory
=======================================================
.. note::
  Conda environments are part of your research and should be stored in your PI's ``/work`` directory. 

If conda environments are stored in your ``/home/<username>`` directory, here are some suggestions to reduce storage size of the environments.

To remove any unused packages and caches from using conda, from an srun session, ``srun --pty /bin/bash``, load the version of anaconda/minicoda the environment are built with and run: ::

 source activate <your environment>
 conda clean --all

This will only delete unused packages in your ``~/.conda/pkgs`` directory.

To remove any unused conda environments, run: ::

 conda env list
 conda env remove --name <your environment>

Clean ~/.singularity directory
=======================================================
If you have pulled any containers to Discovery using Singularity, you can clean your container cache in your ``/home/<username>`` directory by running the following command from an srun session (``srun --pty /bin/bash``): ::

 module load singularity/3.5.3
 singularity cache clean all

To avoid your ``~/.singularity`` directory filling up, you can set a temporary directory for when you pull containers to store the cache in that location; an example of this procedure, (where ``<project>`` is your PI's ``/work`` directory) is: ::

 mkdir /work/<project>/singularity_tmp
 export SINGULARITY_TMPDIR=/work/<project>/singularity_tmp

Then, use singularity to pull your container as you normally would. 

Best practices
=======================================================
The following sections provide best practices to maintain your ``/home/<username>`` quota for work that utilizes conda environments and containers.

Conda environments
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Conda virtual environments should be used for all python based workflows and should be located in your PI's /work directory. To create a conda environment in a ``/work`` directory, please use the ``--prefix`` flag with conda as follows (where ``<project>`` is your PI's ``/work`` directory and ``<my directory>`` is an empty directory to store your conda environment): ::

 conda create myenv --prefix=/work/<project>/<my directory>

More information about creating custom conda environments can be found here :ref:`conda`. 

Conda environments that are stored in a commonly accessible directory in your PI's ``/work`` directory can be used by fellow group members by running ``source activate <env name>``. Utilizing the same conda environment will save storage space and time in building duplicate conda environments for the same project. 

Singularity containers
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
Containers that are pulled, built and maintained for research work should be stored in your PI's ``/work`` directory, not in your ``/home/<username>`` directory. 
