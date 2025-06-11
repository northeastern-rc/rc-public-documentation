(accessing-gpus)=
# GPU Access

## Running Jobs
Use `srun` for interactive and `sbatch` for batch mode. The `srun` example below is requesting 1 node and 1 GPU with 4GB of memory in the `gpu` partition. You must use the `--gres=` option to request a gpu:

:::{code} bash
srun --partition=gpu --nodes=1 --pty --gres=gpu:v100-pcie:1 --ntasks=1 --mem=4GB --time=01:00:00 /bin/bash
:::

:::{note}
On the `gpu` partition, requesting more than 1 GPU (`--gres=gpu:1`) will cause your request to fail. Additionally, one cannot request all the CPUs on that gpu node as they are reserved for other GPUs.
:::

The `sbatch` example below is similar to the `srun` example above, but it submits the job in the background, gives it a name, and directs the output to a file:

:::{code-block} shell
#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100-pcie:1
#SBATCH --time=01:00:00
#SBATCH --job-name=gpu_run
#SBATCH --mem=4GB
#SBATCH --ntasks=1
#SBATCH --output=myjob.%j.out
#SBATCH --error=myjob.%j.err

## <your code>

:::

## Specifying a GPU type
You can add a specific type of GPU to the `--gres=` option (with either `srun` or `sbatch`). For a list of available GPU types, refer to the GPU Type column in [GPU Nodes](https://rc.northeastern.edu/compute/) table, that are listed as *Public*.

:::{code-block} bash
:caption: Flag to request one v100 GPU:
--gres=gpu:v100-pcie:1
:::

:::{note}
Requesting a specific type of GPU could result in longer wait times, based on GPU availability at that time.
:::
