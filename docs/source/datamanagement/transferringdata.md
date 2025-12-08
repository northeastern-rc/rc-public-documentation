(transferring-data)=

# Transfer Data

The HPC has a dedicated transfer node that you must use to transfer data to and from the cluster. You cannot transfer data from any other node or the HPC to your local machine. The node name is `<username>@xfer.discovery.neu.edu:` where `<username>` is your Northeastern username to login into the transfer node.

:::{important}
At the moment, only the Discovery transfer node is available for data transfers to and from the cluster. Folder names such as `/projects/foo` on Explorer and `/work/foo` on Discovery are mapped together. Accessing and making changes to `/work/foo` on Discovery will be reflected in `/projects/foo` on Explorer, and vice-versa.
:::

You can also transfer files using Globus. This is highly recommended if you need to transfer large amounts of data. See {ref}`using-globus` for more information.

If you are transferring data from different directories on the HPC, you need to use a compute node (see {ref}`using-srun` or {ref}`using-sbatch`) with SCP, rsync, or the copy command to complete these tasks. You should use the `--constraint=ib` flag which will use the infiniband network for the fastest transfer.

:::{caution}
The `/scratch` space is for temporary file storage only. It is not backed up. If you have directed your output files to `/scratch`, you should transfer your data from `/scratch` to another location as soon as possible. See our [website for more data storage information](https://rc.northeastern.edu/data-storage-options/).
:::

## Transfer via Terminal

:::::{tab-set}
::::{tab-item} SCP

You can use `scp` to transfer files/directories to and from your local machine and the HPC. As an example, you can use this command to transfer a file to your `/scratch` space on the HPC from your local machine:

:::{code-block} bash
scp <filename> <username>@xfer.discovery.neu.edu:/scratch/<username>
:::

where `<filename>` is the name of the file in your current directory you want to transfer, and `<username>` is your Northeastern username. So that you know, this command is run on your local machine.

If you want to transfer a directory in your `/scratch` called `test-data` from the HPC to your local machine's current working directory, an example of that command would be:

:::{code-block} bash
scp -r <username>@xfer.discovery.neu.edu:/scratch/<username>/test-data .
:::

where `-r` flag is for the recursive transfer because it is a directory. So that you know, this command is run on your local machine.

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

Similarly, `rsync` can be used to copy from the current working directory on the HPC to your current working directory on your local machine:

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

You can use a sbatch job to complete data transfers by submitting the job to the HPC queue. An example of using `rsync` through a sbatch script is as follows:

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

where we are transferring the data from `source_folder` to the `destination_folder`.

::::
::::{tab-item} SSHFS

If you want to use `sshfs`, use it with the dedicated transfer node `xfer.discovery.neu.edu`. It will not work on the login or compute nodes. On a Mac, you will also have to install macFUSE and sshfs (please refer to [macFUSE]) to use the `sshfs` command.

Use this syntax to perform file transfers with `sshfs`:

:::{code-block} bash
sshfs <username>@xfer.discovery.neu.edu:</your/remote/path> <your/local/path> -<options>
:::

For example, this will mount a directory in your `/scratch` named `test-data` to a local directory on your machine `~/mount_point`:

:::{code-block} bash
sshfs <username>@xfer.discovery.neu.edu:/scratch/<username>/test-data ~/mount_point
:::

You can interact with the directory from your GUI or use the terminal to perform tasks on it.
::::

::::{tab-item} rclone

Rclone can be used to connect to external databases including dropbox and google drive. Rclone must first be installed on your personal computer and the external database authorised prior to transfering data to/from the cluster. 

## Configure rclone on your personal compute

This is a required step. Install rclone locally (on your personal computer). Rclone can be found here. [https://rclone.org/downloads/](https://rclone.org/downloads/) (Please select the correct executable for your operating system).

Then in terminal run:

:::{code-block} bash
rclone authorize “dropbox”
:::

This will open a browser window asking if you authorize rclone to have access to your dropbox. Say "yes"

After accepting you should see an ‘access token’ on your terminal.

Copy this token. You will need it for Explorer.

## Configuring rclone on Explorer

Start an interactive session either on the terminal from an ssh session or via the Open Ondemand option under "Cluster" and "explorer Shell Access"

:::{code-block} bash
srun --pty /bin/bash
module load rclone/1.72
rclone configure

		n #for new 

		name > mydropbox

		9 or “dropbox”. #select the number or name of the type of storage you would like to configure

		client_id> #hit enter to leave blank

		client_secret> #leave blank

		edit advanced config?

		y

		token> #leave blank

		auth_url> #leave blank

		token_url> #leave blank

		chunk_size> 150M 

		impersonate> #leave blank

		encoding> #leave blank for default

		Remote config

		use auto config?

		n

		result> # paste the token from above into this space. It should start with curly brackets {”access_token”: ”…….”}

		# hit enter
:::

You should now see a little summary showing the name of your remote in square brackets and some of the settings that you specified below:

:::{code-block} bash
[mydropbox]
type = dropbox
chunk_size = 150M
token = {”access_token”:....}

# Hit q to quit
:::


To test that rclone is correctly connected to your dropbox type this:

:::{code-block} bash
# note if you have a lot stored in your dropbox you may want to specify a more specific path here, otherwise it will take a while to load your directory contents
rclone ls mydropbox:  
:::
This command should print out a list of everything in your dropbox.

To copy over all of your files from dropbox to Explorer run the following:
:::{code-bash} bash
rclone copy mydropbox: test_dropbox
:::

:::{note}
The destination to copy your files can be the file path (for example: /scratch/s.caplins/test_dropbox) or a relative path. If the destination folder (test_dropbox) does not already exist it will be created.

Please be aware of all directory quota limits when copying data. Your home directory in particular is not the best location for data transfer. Use /scratch or /projects instead.
:::

## Once rclone is configured move to the transfer node to transfer data

:::{code-block} bash
exit out of login node

ssh username@xfer.discovery.neu.edu

module load rclone

rclone copy mydropbox: path/where/you/want/the/file/dropbox # if file dropbox does not exist this will create it
:::
## Or transfer data using rclone in an sbatch script

Here is an example sbatch script you can modify to reflect your database name and transfer location

:::{code-block} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=12:00:00
#SBATCH --job-name=rclone
#SBATCH --mem=10G
#SBATCH --partition=short
#SBATCH --constraint=ib

module load rclone/1.72.0
rclone copy mydropbox:/path/if/needed /projects/<project_name>/destination_folder
:::

:::::

## Transfer via GUI Application

:::::{tab-set}
::::{tab-item} OOD's File Explorer

You can use OOD's File Explorer application to transfer data from different directories on the HPC and also to transfer data to and from your local machine to the HPC. 
::::
::::{tab-item} MobaXterm

You can use MobaXterm to transfer data to and from the HPC. Please check out [MobaXterm] to download MobaXterm.

1. Open MobaXterm.
1. Click **Session**, then select **SFTP**.
1. In the **Remote host** field, type `xfer.discovery.neu.edu`
1. In the **Username** field, type your Northeastern username.
1. In the **Port** field, type 22.
1. In the **Password** box, type your Northeastern password and click **OK**. Click **No** if prompted to save your password.

You will now be connected to the transfer node and can transfer files through MobaXterm. Please refer to [MobaXterm] for further information.


::::
::::{tab-item} FileZilla
You can use FileZilla to transfer data to and from the HPC. Please check out [FileZilla] to download.

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
