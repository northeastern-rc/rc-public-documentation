(quickstart-h200)=
# Quick Start Guide for H200s

## Introduction
The Research Computing team would like to share a general quick start guide on accessing the H200s on the Explorer HPC cluster. The H200s will be accessible for your jobs in the terminal in sbatch and srun sessions and on Open OnDemand in the gpu-short, gpu, and multigpu partitions. 

We have documentation on utilizing GPU resources on the Explorer HPC cluster. Please see {ref}`accessing-gpus`. Only the `gres` flag will have to be changed in the submission.

## Using H200s in `srun`
:::{code} bash
srun --partition=gpu --nodes=1 --pty --gres=gpu:h200:1 --ntasks=1 --mem=4GB --time=01:00:00 /bin/bash
:::
This example is for an interactive session running on 1 node, with 1 CPU core and 4 GB of CPU memory for 1 hour with an H200 GPU.

:::{note}
On the `gpu` partition, requesting more than 1 GPU (`--gres=gpu:1`) will cause your request to fail. Additionally, you cannot request all the CPUs on that GPU node, as those CPUs are reserved for other GPUs.
:::

## Using H200s in `sbatch`
:::{code-block} bash
#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gres=gpu:h200:1
#SBATCH --time=01:00:00
#SBATCH --job-name=gpu_run
#SBATCH --mem=4GB
#SBATCH --ntasks=1
#SBATCH --output=myjob.%j.out
#SBATCH --error=myjob.%j.err

## <your code>
:::
This example is for an sbatch job requesting 1 node, with 1 CPU core and 4 GB of CPU memory for 1 hour with an H200 GPU.

:::{note}
Requesting a specific type of GPU could result in longer wait times, based on GPU availability at that time.
:::

## For use in Open OnDemand
In Open OnDemand, for the application you would like to launch, please select `gpu-short`, `gpu`, and `multigpu` from the partition drop down menu. Then from the GPU Type drop down menu, please select the `h200` option.
