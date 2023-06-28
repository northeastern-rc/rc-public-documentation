(transfering-data)=

# Transferring Data

The HPC has a dedicated transfer node that you must use to transfer data to and from the cluster. You are not allowed to transfer data from any other node to or from the HPC to your local machine. The node name is `<username>@xfer.discovery.neu.edu:` where `<username>` is your Northeastern username to login into the transfer node.

You can also transfer files using Globus. This is highly recommended if you need to transfer large amounts of data. See {ref}`using-globus` for more information.

If you are transferring data from different directories on the HPC, you need to use a compute node (see {ref}`using-srun` or {ref}`using-sbatch`) with scp, rsync, or with the copy command to complete this tasks. You should use the `--constraint=ib` flag (see {ref}`hardware-overview`) to ensure the fastest data transfer rate.

:::{caution}
The `/scratch` space is for temporary file storage only. It is not backed up. If you have directed your output files to `/scratch`, you should transfer your data from `/scratch` to another location as soon as possible. See {ref}`discovery-storage` for more information.
:::

## Transfer via Terminal

:::::{tab-set}
::::{tab-item} SCP

You can use `scp` to transfer files/directories to and from your local machine and the HPC. As an example, you can use this command to transfer a file to your `/scratch` space on the HPC from your local machine:

:::{code-block} bash
scp <filename> <username>@xfer.discovery.neu.edu:/scratch/<username>
:::

where `<filename>` is the name of the file in your current directory you want to transfer and `<username>` is your Northeastern username. Note, this command is run on your local machine.

If you want to transfer a directory in your `/scratch` called `test-data` from the HPC to your local machine's currenting working directory, an example of that command would be:

:::{code-block} bash
scp -r <username>@xfer.discovery.neu.edu:/scratch/<username>/test-data .
:::

where `-r` flag is for the recurssive transfer because it is a directory. Note, this command is run on your local machine.

::::
::::{tab-item} Rsync
You can use the `rsync` command to transfer data to and from the HPC and local machine. You can also use `rsync` to transfer data from different directories on the cluster.

The syntex of `rsync` is

:::{code} bash
rsync [options] <source> <destination>
:::

An example of using rsync to transfer a directory called `test-data` in your current working directory on your local machine to your `/scratch` on the HPC is

:::{code} bash
rsync -av test-data/ <username>@xfer.discovery.neu.edu:/scratch/<username>
:::

where this command is run on your local machine in the directory that contains `test-data`.

Similarily, `rsync` can be used to copy from the current working directory on the HPC to your current working directory on your local machine:

:::{code} bash
rsync -av <username>@xfer.discovery.neu.edu:/scratch/<username>/test-data .
:::

where this command is run on your local machine in the current directory that you want to save the directory `test-data`.

You can also use rsync to copy data from different directories on the HPC:

:::{code-block} bash
srun --partition=short --nodes=1 --ntasks=1 --time=01:05:00 --constraint=ib --pty /bin/bash
rsync -av /scratch/<username>/source_folder /home/<username>/destination_folder
:::

::::
::::{tab-item} sbatch

You can use an sbatch job to complete data transfers by submitting the job to the HPC queue. An example of using `rsync` through an sbatch script is as follows:

:::{code-block} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --time=0:05:00
#SBATCH --job-name=DataTransfer
#SBATCH --mem=2G
#SBATCH --partition=short
#SBATCH --constraint=ib
#SBATCH -o %j.out
#SBATCH -e %j.err

rsync -av /scratch/<username>/source_folder /home/<username>/destination_folder
:::

where we are transfering the data from `source_folder` to the `destination_folder`.

::::
::::{tab-item} SSHFS

If you want to use `sshfs`, you will need to use it with the dedicated transfer node `xfer.discovery.neu.edu`. It will not work on the login or compute nodes. On a Mac, you will also have to install macFUSE and sshfs (please refer to [macFUSE]) to use the `sshfs` command.

Use this syntax to perform file transfers with `sshfs`:

:::{code-block} bash
sshfs <username>@xfer.discovery.neu.edu:</your/remote/path> <your/local/path> -<options>
:::

For example, this will mount a directory in your `/scratch` named `test-data` to a local directory on your machine `~/mount_point`:

:::{code-block} bash
sshfs <username>@xfer.discovery.neu.edu:/scratch/<username>/test-data ~/mount_point
:::

where you can interact with the directory from your GUI or using the terminal to perform tasks on it.
::::
:::::

## Transfer via GUI Application

:::::{tab-set}
::::{tab-item} OOD's File Explorer

You can use OOD's File Explorer application to transfer data from different directories on the HPC and also to transfer data to and from your local machine to the HPC. For more information to complete this please see {ref}`file-explorer`.
::::
::::{tab-item} MobaXterm

You can use MobaXterm to transfer data to and from the HPC. Please checkout [MobaXterm] to download MobaXterm.

1. Open MobaXterm.
1. Click **Session**, then select **SFTP**.
1. In the **Remote host** field, type `xfer.discovery.neu.edu`
1. In the **Username** field, type your Northeastern username.
1. In the **Port** field, type 22.
1. In the **Password** box, type your Northeastern password and click **OK**. Click **No** if prompted to save your password.

You will now be connected to the transfer node and can transfer files through MobaXterm. Please refer to [MobaXterm] for further information.


::::
::::{tab-item} FileZilla
You can use FileZilla to transfer data to and from the HPC. Please checkout [FileZilla] to download MobaXterm.

1. Open FileZilla.
1. In the **Host** field, type `sftp://xfer.discovery.neu.edu`
1. In the **Username** field, type your Northeastern username.
1. In the **Password** field, type your Northeastern password.
1. In the **Port** field, type 22.

You will now be connected to the transfer node and can transfer files through FileZilla. Please refer to [FileZilla] for further information.
::::
:::::

[FileZilla]: https://filezilla-project.org/
[MobaXterm]: https://mobaxterm.mobatek.net/
[macFUSE]: https://osxfuse.github.io/
