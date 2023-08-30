(home-directory-storage-quota)=
# Home Directory Storage Quota

There are strict quotas for each {term}`home directory` (i.e., `/home/<username>`), and staying within the quota is vital for preventing issues on the HPC. This page provides some best practices for keeping within the {term}`quota`. For more information about data storage on the HPC, see {ref}`data-storage`.

:::{important}
All commands on this page should be run from a compute node because they are CPU-intensive. You can find more information on getting a job on a compute node from {ref}`using-srun`.
:::

## Analyze Disk Usage
From a compute node, run the following command from your `/home/<username>` directory:
:::{code-block} bash
du -shc .[^.]* ~/*
:::

This command will output the size of each file, directory, and hidden directory in your `/home/<username>` space, with the total of your `/home` directory being the last line of the output. After identifying the large files and directories, you can move them to the appropriate location (e.g., `/work` for research) or back up and delete them if they are no longer required. An example output would look like:
:::{code-block} shell
[<username>@<host> directory]$  du -shc .[^.]* ~/*
39M     .git
106M    discovery-examples
41K     README.md
3.3M    software-installation
147M    total
:::

## Utilize /work and /scratch
Use `/work` for long-term storage. PIs can request a folder in `/work` via [New Storage Space Request] and additional storage via [Storage Space Extension Request]. Utilize `/scratch/<username>` for temporary or intermediate files. Then, move files from `/scratch` to `/work` for persistent storage (i.e., the recommended workflow).

:::{note}
Please be mindful of the `/scratch` purge policy, which can be found on the [Research Computing Policy Page]. See {ref}`data-storage` for information on `/work` and `/scratch`.
:::

## Cleaning Directories
(cleaning-conda)=
### Conda

:::{note}
Conda environments are part of your research and should be stored in your PI's `/work` directory.
:::
Here are some suggestions to reduce the storage size of the environments for those using the `/home/<username>/.conda` directory.

Remove unused packages and clear caches of Conda by loading an Anaconda module and running the following:

:::{code-block} bash
source activate <your environment>
conda clean --all
:::

This will only delete unused packages in your `~/.conda/pkgs` directory.

To remove any unused conda environments, run:

:::{code-block} bash
conda env list
conda env remove --name <your environment>
:::

### Singularity

If you have pulled any containers to the HPC using {term}`Singularity`, you can clean your container cache in your `/home/<username>` directory by running the following command from a compute node:

:::{code-block} bash
module load singularity/3.5.3
singularity cache clean all
:::

To avoid your `~/.singularity` directory filling up, you can set a temporary directory for when you pull a {term}`container` to store the cache in that location; an example of this procedure (where `<project>` is your PI's `/work` directory) is the following:

:::{code-block} bash
mkdir /work/<project>/singularity_tmp
export SINGULARITY_TMPDIR=/work/<project>/singularity_tmp
:::

Then, pull the container using Singularity as usual.

### Cache

The `~/.cache` directory can become large with the general use of HPC and Open OnDemand. Make sure you are not running any processes or jobs at the time by running the following:

:::{code-block} bash
squeue -u <username>
:::

which prints a table with `JOBID`, `PARTITION`, `NAME`, `USER ST`, `TIME`, `NODES`, and `NODELIST (REASON)`, which is empty when no jobs are running (i.e., it is safe to remove `~/.cache` when no jobs are running).

## Storing research environments

(best-practices-conda-environments)=
### Conda environments

Use conda environments for Python on HPC. To create an environment in `/work`, use the `--prefix` flag as follows: (where `<project>` is your PI's `/work` directory and `<my conda env>` is an empty directory to store your Conda environment):

:::{code-block} bash
conda create --prefix=/work/<project>/<my conda env>
:::


Utilize the same conda environment to save storage space and time (i.e., avoid duplicate conda environments). Hence, shared environments can be easily done for a project accessing the same `/work` directory.


{ref}`More information about creating custom Conda environments. <conda>`

### Singularity containers

Containers pulled, built, and maintained for research work should be stored in your PI's `/work` directory, not your `/home/<username>` directory.

[New Storage Space Request]: https://bit.ly/NURC-NewStorage
[Research Computing Policy Page]: https://rc.northeastern.edu/policy/
[Storage Space Extension Request]: https://bit.ly/NURC-StorageExtension
