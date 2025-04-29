(quickstart-h200)=
# Quick Start Guide for H200s

## Introduction
The Research Computing team would like to share a general quick start guide on accessing the H200s on the Explorer HPC cluster. The H200s will be accessible for your jobs in the terminal in sbatch and srun sessions and on Open OnDemand in the gpu-short, gpu, and multigpu partitions. 

We have documentation on utilizing GPU resources on the Explorer HPC cluster: {ref}`accessing-gpus`, only the `gres` flag will have to get change in the submission.

## For use in `srun`
:::{code} bash
srun --partition=gpu --nodes=1 --pty --gres=gpu:h200:1 --ntasks=1 --mem=4GB --time=01:00:00 /bin/bash
:::
for an interactive session running on 1 node, with 1 CPU core and 4 GB of CPU memory for 1 hour with an H200 GPU.

:::{note}
On the `gpu` partition, requesting more than 1 GPU (`--gres=gpu:1`) will cause your request to fail. Additionally, one cannot request all the CPUs on that gpu node as they are reserved for other GPUs.
:::

## For use in 'sbatch`
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
for a sbatch job requesting the same resources as the `srun` example.

:::{note}
Requesting a specific type of GPU could result in longer wait times, based on GPU availability at that time.
:::

## For use in Open OnDemand
In Open OnDemand, for the application you would like to launch, please select the `gpu-short`, `gpu`, and `multigpu` from the partition drop down menu and then from the gpu type drop down, please select the `h200` option.
