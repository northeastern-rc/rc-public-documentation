(working-gpus)=

# Working with GPUs

The cluster has various NVIDIA Graphics Processing Units (GPUs) available on gpu-equipped partitions, as listed in the table below.

:::{seealso}
[Learn more about partitions.](../hardware/partitions.md)
:::


:::{list-table}
--------------
header-rows: 1
align: center
--------------

* - GPU Type
  - GPU Memory
  - Tensor Cores
  - CUDA Cores
  - Nodes in Public GPUs
  - Nodes in Private GPUs
* - p100 ([Pascal])
  - 12GB
  - N/A
  - 3,584
  - 12 (x3-4 GPUs)
  - 3 (x4 GPUs)
* - v100-pcie ([Volta])
  - 32GB
  - 640
  - 5,120
  - 4 (x2 GPUs)
  - 1 (x2 GPUs, 16GB)
* - v100-sxm2 ([Volta])
  - 32GB
  - 640
  - 5,120
  - 24 (x4 GPUs)
  - 10 (x4 GPUs, 16GB); 8 (x4 GPUs, 32GB)
* - t4 ([Turing])
  - 15GB
  - 320
  - 2,560
  - 2 (x3-4 GPUs)
  - 1 (x4 GPUs)
* - quadro ([Quadro RTX 8000])
  - 46GB
  - 576
  - 4,608
  - 0
  - 2 (x3 GPUs)
* - a30 ([Ampere])
  - 24GB
  - 224
  - 3,804
  - 0
  - 1 (x3 GPUs)
* - a100 ([Amperea100])
  - 41 & 82GB
  - 432
  - 6,912
  - 3 (x4 GPUs)
  - 15 (x2-8 GPUs)
* - a5000 ([Ampere RTX A5000])
  - 24GB
  - 256
  - 8,192
  - 0
  - 6 (x8 GPUs)
* - a6000 ([Ampere RTX A6000])
  - 49GB
  - 336
  - 10,752
  - 0
  - 3 (x8 GPUs)
:::

The `gpu` partition is the general GPU resource for HPC users looking to use a GPU; `multigpu` is the alternative, where more than one GPU are accessible.

Anyone with a Discovery account can use the `gpu` partition. However, you must submit a [ServiceNow ticket] to request temporary access to `multigpu`: the `multigpu` partition is available for times in need for predefined time window. In other words, instances that require `multigpu` must demonstrate the need; furthermore, the specifics of the working code, as the partition is only accessible for a limited of time (e.g., 48 hours), so best to make sure to use at full capacity. Your request will be evaluated by members of the RC team to ensure that the resources in this partition will be used appropriately.

:::{note}
All user limits are subject to the availability of cluster resources at the time of submission and will be honored according to that.
:::

:::{list-table}
--------------
header-rows: 1
--------------

* - Name
  - Requires Approval?
  - Time limit (Default/Max)
  - Submitted Jobs
  - GPU per job Limit
  - Max GPUs per user Limit
* - gpu
  - No
  - 4 hours/8 Hours
  - 50/100
  - 1
  - 8
* - multigpu
  - **Yes**
  - 4 hours/24 Hours
  - 50/100
  - 12
  - 12
:::

## Requesting GPUs with Slurm

Use `srun` for interactive and `sbatch` for batch mode. The `srun` example below is requesting 1 node and 1 GPU with 4GB of memory in the `gpu` partition. You must use the `--gres=` option to request a gpu:

:::{code} bash
srun --partition=gpu --nodes=1 --pty --gres=gpu:1 --ntasks=1 --mem=4GB --time=01:00:00 /bin/bash
:::

:::{note}
On the `gpu` partition, requesting more than 1 GPU (`--gres=gpu:1`) will cause your request to fail. Additionally, one cannot request all the CPUs on that gpu node as they are reserved for other GPUs.
:::

The `sbatch` example below is similar to the `srun` example above, but it submits the job in the background, gives it a name, and directs the output to a file:

:::{code-block} shell
#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --time=01:00:00
#SBATCH --job-name=gpu_run
#SBATCH --mem=4GB
#SBATCH --ntasks=1
#SBATCH --output=myjob.%j.out
#SBATCH --error=myjob.%j.err

## <your code>

:::

### Specifying a GPU type

You can add a specific type of GPU to the `--gres=` option (with
either `srun` or `sbatch`). For a list of available GPU types,
refer to the GPU Types column in the table, at the top of this page,
that are listed as `Public`. The following is an example for
requesting a single p100 GPU:

:::{code-block} bash
--gres=gpu:p100:1
:::

:::{note}
Requesting a specific type of GPU could result in longer wait
times, based on GPU availability at that time.
:::

## Using CUDA

There are several versions of CUDA Toolkits on Discovery, including:

```
cuda/9.0
cuda/9.2
cuda/10.0
cuda/10.2
cuda/11.0
cuda/11.1
cuda/11.2
cuda/11.3
cuda/11.4
cuda/11.7
cuda/11.8
cuda/12.1
```

Use the `module avail` command to check for the latest software
versions on Discovery. To see details on a specific CUDA toolkit
version, use `module show`. For example, `module show cuda/11.4`.

To add CUDA to your path, use `module load`. For example, type
`module load cuda/11.4` to load version 11.4 to your path.

Use the command `nvidia-smi` (NVIDIA System Management Interface)
inside a GPU node to get the CUDA driver information and monitor the
GPU device.

(gpus-for-deep-learning)=
## GPUs for Deep Learning

:::{seealso}
Deep learning frameworks tend to cost storage that can quickly surpass {ref}`home-directory-storage-quota`: follow best practices for {ref}`best-practices-conda-environments`.
:::

First, log onto `gpu` interactively, and load anaconda and CUDA 11.8:

:::{code} bash
srun --partition=gpu --nodes=1 --gres=gpu:v100-sxm2:1 --cpus-per-task=2 --mem=10GB --time=02:00:00 --pty /bin/bash
module load anaconda3/2022.05 cuda/11.8
:::

::::{note}
Be aware of compatibility regarding the GPU type: some installations do not work on k40m or k80 GPUs. To see what `non-Kepler` GPUs might be available execute the following command:

:::
sinfo -p gpu --Format=nodes,cpus,memory,features,statecompact,nodelist,gres
:::

This will indicate the state (idle or not) of a certain gpu-type that could be helpful in requesting an `idle` gpu. However, the command does not give real-time information of the state and should be used with caution.
::::

Select the tab with the desire deeplearning framework.

:::{warning}
Each tab assumes you are on a GPU node before with CUDA 11.8 and anaconda modules loaded as done above.
:::
::::::{tab-set}
:::::{tab-item} PyTorch
The following example demonstrates how to build PyTorch inside a conda virtual environment for CUDA version 11.8.


::::{code-block} bash
---------------------
caption: |
    PyTorch's installation steps (with a specific GPU-type):
---
conda create --name pytorch_env python=3.10 -y
source activate pytorch_env
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
::::
Now, let's check the installation:
::::{code} bash
python -c 'import torch; print(torch.cuda.is_available())'
::::
::::

If CUDA is detected by PyTorch, you should see the result, `True`.

::::{seealso}
[PyTorch documentation] for the most up-to-date instructions and for different CUDA versions.
::::
:::::
:::::{tab-item} TensorFlow

We recommend that you use CUDA 11.2 (the latest supported version) when
working on a GPU with the latest version of TensorFlow (TF).
TensorFlow provides information on the [compatibility of CUDA and
TensorFlow versions](https://www.tensorflow.org/install/source#gpu),
and [detailed installation instructions](https://www.tensorflow.org/install/pip).

For the latest installation, use the TensorFlow pip package, which
includes GPU support for CUDA-enabled devices:

::::{code-block} bash
srun --partition=gpu --gres=gpu:1 --nodes=1 --cpus-per-task=2 --mem=10GB --time=02:00:00 --pty /bin/bash

module load anaconda3/2022.05 cuda/11.2
conda create --name TF_env python=3.9 -y
source activate TF_env
conda install -c conda-forge cudatoolkit=11.2.2 cudnn=8.1.0 -y

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
pip install --upgrade pip
pip install tensorflow==2.11.*
::::

Verify the installation:

::::{code-block} bash
# Verify the CPU setup (if successful, then a tensor is returned):
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal((1000, 1000))))"

# verify the GPU setup (if successful, then a list of GPU device is returned):
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# test if a GPU device is detected with TF (if successful, then True is returned):
python3 -c 'import tensorflow as tf; print(tf.test.is_built_with_cuda())'
::::

To get the name of the GPU, type:

::::{code-block} bash
python -c 'import tensorflow as tf;  print(tf.test.gpu_device_name())'
::::

If the installation is successful, then, for example, you should see
the following as an output:

::::{code-block} bash
2023-02-24 16:39:35.798186: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1613\] Created device /device:GPU:0 with 10785 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:0a:00.0, compute capability: 3.7 /device:GPU:0
::::

::::{note}
Ignore the `Warning` messages that get generated after executing the above commands.
::::

:::::
::::::

[Pascal]: https://www.nvidia.com/en-us/data-center/tesla-p100/
[PyTorch documentation]: https://pytorch.org/
[Volta]: https://www.nvidia.com/en-us/data-center/v100/
[Turing]: https://www.nvidia.com/en-us/data-center/tesla-t4/
[Quadro RTX 8000]: https://www.nvidia.com/en-us/design-visualization/previous-quadro-desktop-gpus/
[Ampere]: https://www.nvidia.com/en-us/data-center/products/a30-gpu/
[Amperea100]: https://www.nvidia.com/en-us/data-center/a100/
[Ampere RTX A5000]: https://www.nvidia.com/en-us/design-visualization/rtx-a5000/
[Ampere RTX A6000]: https://www.nvidia.com/en-us/design-visualization/rtx-a6000/
[ServiceNow ticket]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7
