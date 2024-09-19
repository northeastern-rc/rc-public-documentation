(scratch-directory-purge)=
# Scratch Directory Purge

The space assigned to every user in `/scratch/<username>` is not meant for persistant storage and is purged every month by the Research Computing team. Files are not backed up in /scratch and as such important data or scripts need to be transfered quickly to /work or /home to be retained.

:::{important}
The /scratch space is intended to provide temporary storage for jobs that produce a lot of output, not all of which will be retained.
:::

There are several things you can do to prepare for a purge of /scratch.

1. Transfer any materials that you need to save to /work or /home.

Example using `srun`

:::{code-block}
srun --pty /bin/bash
mv /scratch/<username>/file_to_keep.out /home/<username>/
:::

Example using taring and moving files via an sbatch script. You will need to copy the script below to a text file (e.g., tarmaker.sh) and submit it to the scheduler with the command sbatch tarmaker.sh

:::{code-block}
!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=05:00:00
#SBATCH --partition=short
#SBATCH --job-name=tar
#SBATCH --ntasks=1

# compress the directory that you need with tar

tar cvzf filename.tar.gz /scratch/<username>/output/path

# if statement to check if tar.gz file exists, delete the output path

FILE=filename.tar.gz

if [ -f $FILE ]; then
    echo "File $FILE exists."
    mv /scratch/$FILE /work/<groupname>/myimportantdata

fi
:::

2. On the day of the /scratch purge you will not be able to write job outputs to /scratch. Please edit your sbatch scripts to write outputs to /work.

3. If you have jobs that continually write output to scratch and run for long periods of time, please make sure you are [checkpointing](https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html). This will allow the resumption of your jobs around the /scratch purge.

4. If you wish to retain entire directories that were generated in /scratch as part of a job output, you can tar the directory and move the compressed file to your /home or /work.

:::{code-block}
# First get on a compute node
srun --pty /bin/bash
tar czvf name_of_output.tar.gz /scratch/<username>/directory
:::

The code above can also be run in an sbatch job. Note, taring and compressing files can take time for large directories.

## What happens during a purge of /scratch ?

All files are removed during a /scratch purge. Previously the Resesarch Computing team removed files that had been in /scratch for more than 28 days without being edited. Now we remove *all* files. This saves space for the proper function of the filesystem for all users.

## How do I know /scratch is usable again following the /scratch purge?

We will message via XX. You can also check if the below commands work:

:::{code-block}
cd /scratch/<username>
touch test-scratch
:::

## My files are too big to transfer to /home

Home has a limit of 75GBs. If your usage in /scratch is greater than than for the files that you want to keep, please apply for a space in [/work](https://bit.ly/NURC-NewStorage) or if you are a student request that your PI applies for /work. Do this well in advance of the /scratch purge to ensure your files are saved.