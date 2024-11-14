(using-r)=
# Using R

[R](https://www.r-project.org/) is available as a {ref}`modules <using-module>` and it is also an interactive app on {ref}`Open OnDemand <using-ood>` (OOD). You can also install R with anaconda or miniconda in a conda environment.

## Using R on Open OnDemand

The Open OnDemand application offers several different versions of R accessed through an interactive session with RStudio server in a [Rocker Container](https://rocker-project.org/images/versioned/rstudio). We provide the geospatial *flavor* of Rocker which includes many useful base packages.

In addition to different R packages you will find additional package requirements (e.g, compilers) also present in geospatial flavor.

## Running the Rocker Container in an sbatch script

If you have installed packages in the Open OnDemand Rstudio application, you may want to use those same packages in an sbatch script (non-interactive).

It makes sense to move to sbatch scripts when you have tested your scripts interactively in the Open OnDemand and code needs to just run without supervision.

Here is an example sbatch script using the container runtime engine `Apptainer` and the command `Rscript`.

:::{code-block} bash

#!/bin/bash
#SBATCH --job-name=Rcontainer
#SBATCH --partition=short
#SBATCH --nodes 1
#SBATCH --ntasks 2
#SBATCH --mem=10g
#SBATCH --time 24:00:00

ROCKER_IMAGE=/shared/container_repository/explorer/rstudio/4.4.2/rocker-geospatial-4.4.2.sif

# Run R with Apptainer
apptainer exec -B "/projects:/projects" $ROCKER_IMAGE Rscript my_r_code.sh
:::