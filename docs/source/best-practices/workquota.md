(projects-directory-storage-quota)=
# Projects Directory Storage Quota

Every space in `/projects` has a quota for TB and inodes (file count). It is necessary to stay below the quota to be able to use the space effectively. 

We recommend the following practices to ensure effective use of your space in `/projects`

1. [Check your usage](homequota.md#how-to-check-your-quotas) regularily to avoid hitting the quota limit in the middle of running jobs, which will disrupt their execution. 

2. Compress directories that are not used frequently or for projects that have been completed.

When the output of a script has been generated and you wish to keep the intermediate files or intermediate outputs you can tar the directory. For large numbers of files or big files this can take time. We recommend running taring or compressing in an sbatch script. This can also be done as part of your sbatch script that generated the intermediate outputs.

:::{code} bash
#!/bin/bash
#SBATCH --job-name=tarit
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=24:00:00
#SBATCH -p short

# Commands to execute

tar cvxf project_1_output.tar.gz /projects/full/path/to/directory

:::

3. Delete no-longer needed intermediate outputs. This can also be done as part of the sbatch script to streamline the process of generating output.

4. Request additional space in `/projects`. Please review our [storage policies](https://rc.northeastern.edu/research-projects-storage-space-policy/) for the relevant costs associated, if applicable. 
