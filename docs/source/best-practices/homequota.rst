*******************************************************
Stay Under your Quota at /home/
*******************************************************
It is vital to stay under your ``/home/<username>`` quota to prevent issues using Open OnDemand and performing tasks on Discovery. Here are some suggestions to stay under quota and general best practices with using your ``/home/<username>`` directory.

Utlilize /scratch and /work Directories
=======================================================
For long-term research work storage, ``/work`` should be used. If your PI does not have space in ``/work`` setup, they can request it using the following form https://bit.ly/NURC-NewStorage and can request additional storage using https://bit.ly/NURC-StorageExtension. More details of ``/work`` can be found at :ref:`discovery_storage`. For temporary job files you can utilize /scratch/<username>. Please be mindful of the purge policy of ``/scratch`` which is covered in :ref:`discovery_storage.rst`.

Determine Large Files/Directories in /home/<username>
=======================================================
From a compute node, ``srun --pty /bin/bash``, run the following command from your ``/home/<username>`` directory ::
    
 du -shc .[^.]* *

which will output the size of each file, directory, and hidden directory in your ``/home/<username>`` space, with the total of your ``/home`` directory being the last line of the output. After determining the large files and directories, you can move them to the appropriate locations such as ``/work`` for research or you can back them up and delete them if they are no longer required.

Conda Environment Best Practices
=======================================================
Conda virtual environments should be used for all python based workflows and should be located in your PI's /work directory. To create a conda environment in a ``/work`` directory, please use the ``--prefix`` flag with conda as follows ::

 conda create myenv --prefix=/work/<project>/<my directory>

where ``<project>`` is your PI's ``/work`` directory and ``<my directory>`` is an empty directory to store your conda environment. More information about creating custom conda environments can be found here :ref:`conda`

Conda environments that are stored in a commonly accessibly directory in your PI's ``/work`` directory will be accessible by fellow group members will be able to ``source activate <env name>`` and utilize the same conda environment to save storage space and time in building duplicate conda environments. 

Clean ~/.conda Directory
=======================================================
.. note::
  Conda environments are part of your research and should be stored in your PI's ``/work`` directory. 

If conda environments are stored in your ``/home/<username>`` directory, here are some suggestions to reduce storage size of the environments.

To remove any unused packages and caches from using conda, from an srun session, ``srun --pty /bin/bash``, load the version of anaconda/minicoda the environment are built with and run ::

 source activate <your environment>
 conda clean --all

This will not delete any unused packages in anything but your ``~/.conda/pkgs`` directory.

Remove any unused conda environments ::

 conda env list
 conda env remove --name <your environment>

Singularity Container Best Practices
=======================================================
Containers that are pulled, built and maintained for research work should be stored in your PI's ``/work`` directory and not your ``/home/<username>`` directory. 

Clean ~/.singularity Directory
=======================================================
If you have pulled any containers to Discovery using Singularity, you can clean your container cache in your ``/home/<username>`` directory by running from an srun session, ``srun --pty /bin/bash``, ::

 module load singularity/3.5.3
 singularity cache clean all

To avoid your ``~/.singularity`` directory filling up, you can set a temporary directory for when you pull containers to store the cache in that location. An example of this procedure is ::

 mkdir /work/<project>/singularity_tmp
 export SINGULARITY_TMPDIR=/work/<project>/singularity_tmp

where ``<project>`` is your PI's ``/work`` directory. Then pull use singularity to pull your container as you normally would. 
