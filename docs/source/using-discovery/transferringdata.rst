******************
Transferring Data
******************

This document will list various options to perform inter-cluster and intra-cluster data transfers.

- Inter-cluster data transfer: Transfer data between Discovery cluster and an external machine.
- Intra-cluster data transfer: Transfer data between any two locations within the Discovery cluster.

.. caution::

	Discovery has a dedicated transfer node that you must use to transfer data to and from the cluster.
	You are not allowed to transfer data from any other node.
	The node name is ``<username>@xfer.discovery.neu.edu:`` where ``<username>`` is your Northeastern username.

.. caution::

   The /scratch directory is for temporary file storage only. It is not backed up.
   If you have directed your output files to /scratch, you should transfer your data from /scratch
   to another location as soon as possible. See :ref:`discovery_storage` for more information.
   
   
Using Open OnDemand's File Explorer
===================================

You can use Open OnDemand web portal for inter-cluster and intra-cluster data transfers.

For details on how to use OOD's File Explorer, refer :ref:`file_explorer`

Using SCP
=========

You can use SCP command on a terminal for inter-cluster data transfers.

Transfer data from external machine to Discovery cluster
--------------------------------------------------------

The format of the scp command is as follows:

``scp <-r if transfering folder> <path_to_file/folder_on_external_machine> <yourusername>@xfer.discovery.neu.edu:<path_to_destination_folder_on_discovery>``

For example, to transfer test-data folder from local machine to /scratch/k.joisher, we need to execute the following command on the external machine's terminal:

``scp -r test-data k.joisher@xfer.discovery.neu.edu:/scratch/k.joisher``

.. image:: /images/scp.png	

Transfer data from Discovery cluster to external machine
--------------------------------------------------------

Similar to transfering data from external machine to Discovery cluster, we can use scp to transfer data from the cluster to an external machine using the following command:

``scp <-r if transfering folder> <yourusername>@xfer.discovery.neu.edu:<path_to_destination_folder_on_discovery> <path_to_file/folder_on_external_machine>``

For example, to transfer test-data folder from Discovery to an external machine, we need to execute the following command on the external machine's terminal:

``scp -r k.joisher@xfer.discovery.neu.edu:/scratch/k.joisher/test-data .``

Using SSHFS
===========

You can use SSHFS to mount a directory on Discovery cluster to your local machine. You can then perform inter-cluster data transfer using this mounted directory.

Use the following command format to mount a directory on Discovery to your local machine.

``sshfs <yourusername>@xfer.discovery.neu.edu:</your/remote/path> <your/local/path> -<options>``

For example, to mount /scratch/k.joisher/test-data to a directory called 'mount_point' on the local machine, we can use the following command on the local machine's terminal:

``sshfs k.joisher@xfer.discovery.neu.edu:/scratch/k.joisher/test-data ~/mount_point``

Now if you open the ``mount_point`` directory on your local machine, you will see the contents of ``/scratch/k.joisher/test-data``.

If you then want to transfer data from your local machine to Discovery, you can use the following command on local machine's terminal:

``cp <path/to/local/file> <path/to/mounted/directory>``

For example, to transfer a file called ``local.txt`` from the local machine to ``/scratch/k.joisher/test-data``, we can use the following command on local machine's terminal:

``cp local.txt ~/mount_point``

After executing the above command, local.txt will be transferred to /scratch/k.joisher/test-data.

Similarly, to transfer file from ``/scratch/k.joisher/test-data`` to the local machine, we can use the following command on local machine's terminal:

``cp ~/mount_point/file1.txt file1_copy.txt``


Using rsync
===========

You can use rsync command to perform inter-cluster and intra-cluster data transfer.

Inter-cluster data transfer
---------------------------

The rsync command format is as follows:
rsync [options] <source> <destination>

For example, to transfer test-data folder from local machine to /scratch/k.joisher folder on Discovery cluster, we can use the following command on the local machine:

``rsync -av test-data/ k.joisher@xfer.discovery.neu.edu:/scratch/k.joisher``

.. image:: /images/rsync_local_to_discovery.PNG


Similarly, to transfer test-data folder from Discovery cluster to local machine, we can use the following command:

``rsync -av k.joisher@xfer.discovery.neu.edu:/scratch/k.joisher/test-data .``

.. image:: /images/rsync_discovery_to_local.PNG

Intra-cluster data transfer
---------------------------

Similar to inter-cluster data transfer, rsync can be used to copy files within the Discovery cluster. 

First you need to provision a compute node using the srun command (This is to make sure that you are not using login node for data transfer) 

``srun --partition=short --export=ALL --nodes=1 --ntasks=1 --x11 --mem=2G --time=00:05:00 --pty /bin/bash``

After a compute node is provisioned, use the rsync command to transfer files. For example, to transfer data from ``/scratch/k.joisher/source_folder`` to ``/home/k.joisher/destination_folder``, use the following command:
``rsync -av /scratch/k.joisher/source_folder /home/k.joisher/destination_folder``

For more details on how to use sbatch, refer :ref:`using_srun`


Using sbatch
============

Similar to srun command, you can use sbatch script to transfer files within Discovery to perform intra-cluster data transfer.
Using sbatch allows you to transfer files non-interactively and also allows to run multiple data transfer tasks.

Consider an example where we need to transfer data from ``/scratch/k.joisher/source_folder1`` to ``/home/k.joisher/destination_folder1`` and 
``/scratch/k.joisher/source_folder2`` to ``/home/k.joisher/destination_folder2``

In order to transfer this data non-interactively, first create a script file

::

  #!/bin/bash
  #SBATCH --nodes=1
  #SBATCH --ntasks=2
  #SBATCH --time=0:05:00
  #SBATCH --job-name=DataTransfer
  #SBATCH --mem=2G
  #SBATCH --partition=short
  #SBATCH -o %j.out
  #SBATCH -e %j.err

  rsync -av /scratch/k.joisher/source_folder1 /home/k.joisher/destination_folder1
  rsync -av /scratch/k.joisher/source_folder2 /home/k.joisher/destination_folder2


After creating the script file, use the following command to dispatch a sbatch job:

``sbatch data_transfer.script``

After the job gets completed, the data would be copied from the source folder to the destination folder. 

For more details on how to use sbatch, refer :ref:`using_sbatch`

Using Globus
============

You can use Globus data management system to perform inter-cluster and intra-cluster data transfers.
Detailed steps on how to setup and use Globus can be found here - :ref:`using_globus`


Using MobaXterm
===============

You can use MobaXterm to perform inter-cluster and intra-cluster data transfers. 
You need to install MobaXterm from the following website: https://mobaxterm.mobatek.net/download.html

1. Open MobaXterm.

2. Click **Session**, then select **SFTP**.

3. In the **Remote host** field, type ``xfer.discovery.neu.edu``

4. In the **Username** field, type your Northeastern username.

5. In the **Port** field, type 22.

6. In the **Password** box, type your Northeastern password and click **OK**. Click **No** if prompted to save your password.

You will now be connected to the transfer node and can transfer files through MobaXterm.

Using FileZilla
===============

FileZilla can be used for inter-cluster data transfers.
You can download FileZilla from this link: https://filezilla-project.org/

1. Open FileZilla.

2. In the **Host** field, type ``sftp://xfer.discovery.neu.edu``

3. In the **Username** field, type your Northeastern username.

4. In the **Password** field, type your Northeastern password.

5. In the **Port** field, type 22.

You will now be connected to the transfer node and can transfer files through FileZilla.