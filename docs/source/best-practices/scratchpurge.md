(scratch-directory-purge)=
# Preparing for a /scratch purge

The space assigned to every user in /scratch/<username> is not meant for persistant storage and is purged every month by the Research Computing team. Files are not backed up in /scratch and as such important data or scripts need to be transfered quickly to /work or /home to be retained.

The /scratch space is intended to provide temporary storage for jobs that produce a lot of output, not all of which will be retained.

There are several things you can do to prepare for a purge of /scratch.

1. Transfer any materials that you need to save to /work or /home.

   
:::{code-block} srun example
srun --pty /bin/bash
mv /scratch/<username>/file/to/keep /home/<username>/
:::
    sbatch example

    Idealy this step is incorporated into your sbatch script and occurs after the job has been written. We provide an example of how to do this below.


2. On the day of the /scratch purge you will not be able to write job outputs to /scratch. Please edit your sbatch scripts to write outputs to /work.

3. If you have jobs that continually write output to scratch and run for long periods of time, please make sure you are [checkpointing](https://rc-docs.northeastern.edu/en/latest/best-practices/checkpointing.html). This will allow the resumption of your jobs around the /scratch purge.

## What happens during a purge of /scratch ?

All files are removed during a /scratch purge. Previously the Resesarch Computing team removed files that had been in /scratch for more than 28 days without being edited. Now we remove *all* files. This saves space for the proper function of the filesystem for all users.

## How do I know /scratch is usable again following the /scratch purge?

We will message via XX. You can also check if the below commands work:

:::{code-block}
cd /scratch/<username>
touch test-scratch
:::

## My files are too big to transfer to /home

Home has a limit of 75GBs. If your usage in /scratch is greater than than for the files that you want to keep, please apply for a space in [/work]() or if you are a student request that your PI applies for /work. 