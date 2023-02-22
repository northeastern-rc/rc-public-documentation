*******************************************************
Staying Under /home/<username> Quota
*******************************************************
It is vital to stay under your /home/<username> quota to prevent issues in using Open OnDemand and performing tasks on Discovery. Here are some suggestions to stay under quota and general best practices with using your /home/<username> directory.

Utlilize /scratch and /work Directories
=======================================================
For long term research work storage, /work should be used. If your PI does not have space in /work setup, they can request it using the following form https://bit.ly/NURC-NewStorage and can request additional storage using https://bit.ly/NURC-StorageExtension. More details of /work can be found at :ref:`_discovery_storage` For temporary job files you can utilize /scratch/<username>. Please be mindful of the purge policy of /scratch which is covered in :ref:`_discovery_storage.rst`.

Determine Large Files/Directories in /home/<username>
=======================================================
From a compute node, ``srun --pty /bin/bash``, run the following command from your /home/<username> directory ::
    
 du -h --max-depth=1 *

which will output the size of each file, directory and first sub-directory in your /home/<username> directory. After determining the large files and directories, you can move them to the appropriate locations such as /work for research or you can back them up and delete them if they are no longer required.

Conda Environment Best Practices
=======================================================
Conda virtual environments should be used for all python based workflows and should be located in your research group's /work directory. To create a conda environment in a /work directory, please use the ``--prefix`` flag with conda as follows ::

 conda create myenv --prefix=/work/<project>/<my directory>

where <project> is your PIs /work directory and <my directory> is an empty directory to store your conda environment. More information about creating custom conda environments can be found here :ref:`conda`

Clean ~/.conda Directory
=======================================================
If conda environments are stored in your /home/<username> directory, here are some suggestions to reduce storage size of the environments.

To remove any unused packages and caches from using conda, from an srun session, ``srun --pty /bin/bash``, load the version of anaconda/minicoda the environment are built with and run ::

 source activate <your environment>
 conda clean --all

This will not delete any unused packages in anything but your local ~/.conda/pkgs directory.

Remove any unused conda environments ::

 conda env list
 conda env remove --name <your environment>

Clean ~/.singularity Directory
=======================================================
If you have pulled any containers to Discovery using Singularity, you can clean your container cache in your /home/<username> directory by running from an srun session, ``srun --pty /bin/bash``, ::

 module load singularity/3.5.3
 singularity cache clean all

To avoid your ~/.singularity directory filling up, you can set a temporary directory for when you pull containers to store the cache in that location. An example of this procedure is ::

 mkdir /scratch/<username>/singularity_tmp
 export SINGULARITY_TMPDIR=/scratch/<username>/singularity_tmp

then pull use singularity to pull your container as you normally would.