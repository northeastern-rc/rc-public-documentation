(singularity)=
# Singularity on Discovery

Singularity is the container runtime engine for the Discovery cluster and is installed as a module. With Singularity, you can run existing containers or pull and run your own custom container.

## How to run a container with Singularity

You can run a container image with the `run` or `exec` commands after moving to a compute node and loading the singularity module.

To see available singularity versions run this in the command line: module avail singularity

:::{important}
 The `--bind` or `-B` flag

It's important to mount the directories in the Discovery cluster to the container image so you can access necessary input data and to output the results of your software to the directory you specify.

For example, this command will allow you to access your directories on /work and /scratch while running the container.

-B "/work:/work,/scratch:/scratch" 
:::

### Example using an image already located on the file system

We have several container images located in /shared/container_repository

Here’s an `srun` example using a singularity image from the /shared/container_repository

```bash
srun --pty /bin/bash
module load singularity/3.10.3
singularity run -B "/work:/work" /shared/container_repository/star/star_2.7.8a.sif

Singularity>

Singularity> STAR
Usage: STAR  [options]... --genomeDir /path/to/genome/index/   --readFilesIn R1.fq R2.fq
Spliced Transcripts Alignment to a Reference (c) Alexander Dobin, 2009-2020

STAR version=2.7.8a
STAR compilation time,server,dir=Wed Nov 15 00:19:03 UTC 2023 f81ff285a72e:/opt/STAR-2.7.8a/source
For more details see:
<https://github.com/alexdobin/STAR>
<https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf>

To list all parameters, run STAR --help
```

An example sbatch script

```bash
#!/bin/bash

#SBATCH --nodes=1
#SBATCH --time=01:00:00
#SBATCH --partition=short
#SBATCH --job-name=star
#SBATCH --output=star.out
#SBATCH --error=star.err
#SBATCH --ntasks=1

module load singularity/3.10.3

cd /work/mygroup

singularity exec -B "/work:/work" /shared/container_repository/star/star_2.7.8a.sif STAR \

--genomeDIR /path/to/genome \
--readFilesIn R1.fq R2.fq
```

## Pull an image from a URL

with the command `singularity pull` you can pull an existing container image from the repositories listed below:

Docker Hub https://hub.docker.com/

Singularity Hub https://singularityhub.com/

(Nvidia Container Repository)[https://catalog.ngc.nvidia.com/containers?filters=&orderBy=weightPopularDESC&query=&page=&pageSize=]

:::{important}
The Importance of Tags and Scientific Reproducibility

Container images are cataloged using “tags”. The tag can indicate the version of the image build or some other aspect of the image. Common tags include “latest” and will pull the most recent version of the image. Care should be taken to distinguish the container version from the version of the software installed, as the same tag on a container image (i.e., “latest”) will pull different versions of software over time. We recommend pulling specific versions of images to better track the version used.
:::

### Example pulling Spades image from Dockerhub

We’ll use a compute node with the InfiniBand network to pull the image. The process of pulling an image and converting it to singularity format (.sif) will take longer for large images.

More about the spades metagenome assembler image can be found [here](https://hub.docker.com/r/staphb/spades).

```bash

 srun --constraint=ib -p short --pty /bin/bash
 module load singularity/3.10.3
 cd /work/groupname/container_images
 mkdir -p cache tmp
 export SINGULARITY_CACHEDIR=$(pwd)/cache 
 export SINGULARITY_TMPDIR=$(pwd)/tmp
 singularity pull spades_3.15.5.sif docker://staphb/spades:3.15.5

 # This will pull an image which will be named spades_3.15.5.sif
 
 # There will be several warnings (warn xattr{}) which can be ignored
 
 # Test the container with singularity run remember to use the "-B" flag to bind any directories 
 singularity run spades_3.15.5.sif
 
 Singularity> spades.py --test
```

This container image can now be used as in the srun and sbatch examples above.

:::{note}
Pulling container images to the Discovery cluster can contribute to your storage use in /home. If a cache and tmp directory aren't created and exported as in the example above, these items will be deposited in a hidden directory in your home at .singularity. 

Please check your home storage usage regularily to stay below the quota.
See {ref}`home-directory-storage-quota` for more.
:::