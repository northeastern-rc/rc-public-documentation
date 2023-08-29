(working-gpus)=

# Working with GPUs
:::{seealso}
[Learn more about partitions.](../hardware/partitions.md)
:::
This page covers the {term}`Graphics Processing Unit (GPU)` resources available on the {term}`cluster`.

:::{list-table} The NVIDIA GPUs available on gpu-equipped partitions.
--------------
header-rows: 1
align: center
widths: auto
--------------

* - GPU Type
  - GPU Architecture
  - Memory (GB)
  - Tensor Cores
  - CUDA Cores
  - Public Nodes (*x* # GPUs)
  - Private Nodes (*x* # GPUs)
* - [P100]
  - [Pascal]
  - 12
  - N/A
  - 3,584
  - 12(*x*3-4)
  - 3(*x*4)
* - [V100 PCle](https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet-letter-fnl-web.pdf)
  - [Volta]
  - 32
  - 640
  - 5,120
  - 4(*x*2)
  - 1(*x*2), 16GB
* - [V100 SXM2](https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet-letter-fnl-web.pdf)
  - [Volta]
  - 32
  - 640
  - 5,120
  - 24(*x*4)
  - 10(*x*4), 16GB<br>8(*x*4), 32GB
* - [T4]
  - [Turing]
  - 15
  - 320
  - 2,560
  - 2(*x*3-4)
  - 1(*x*4)
* - [A100]
  - [Ampere]
  - 41 & 82
  - 432
  - 6,912
  - 3(*x*4)
  - 15(*x*2-8)
* - [Quadro RTX 8000](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/quadro-rtx-8000-us-nvidia-946977-r1-web.pdf)
  - [Turing]
  - 46
  - 576
  - 4,608
  - 0
  - 2(*x*3)
* -  [A30]
  - [Ampere]
  - 24
  - 224
  - 3,804
  - 0
  - 1(*x*3)
* - [RTX A5000]
  - [Ampere]
  - 24
  - 256
  - 8,192
  - 0
  - 6(*x*8)
* - [RTX A6000]
  - [Ampere]
  - 49
  - 336
  - 10,752
  - 0
  - 3(*x*8)
:::

The `gpu` {term}`partition` is the general GPU resource for HPC users looking to use a GPU; `multigpu` is the alternative, where more than one GPU are accessible.

Anyone with a cluster account has access to the `gpu` partition. However, you must submit a [ServiceNow ticket] requesting temporary access to `multigpu` provided sufficient need and preparation.

:::{note}
The `multigpu` partition is available for a limited time window to fulfill urgent needs. In addition, only instances that require `multigpu` will be granted access to this partition. As the partition is only accessible for a limited time (e.g., 48 hours), it is advisable to use it at full capacity. A member of the RC team will review your request to ensure that there is a genuine need for the partition. **Please note that all user limits are subject to the availability of the `multigpu` resources at the time and will be allocated based on user needs.**
:::

:::{list-table}
--------------
header-rows: 1
align: center
widths: auto
--------------

* - Name
  - Requires Approval?
  - Time in Hours (Default/Max)
  - Submitted Jobs
  - GPU per Job Limit
  - User Limit (No. GPUs)
* - gpu
  - No
  - 4/8
  - 50/100
  - 1
  - 8
* - multigpu
  - **Yes**
  - 4/24
  - 50/100
  - 12
  - 12
:::
::::{important}
Consider the compatibility of the GPU, as some programs do not work on the older k40m or k80 GPUs.

Execute the following command to display the `non-Kepler` GPUs that are available:

:::
sinfo -p gpu --Format=nodes,cpus,memory,features,statecompact,nodelist,gres
:::

This indicates the state (idle or not) of gpu-types and could be helpful to find one that is `idle`. However, the command does not give real-time information of the state and should be used carefully.
::::

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

You can add a specific type of GPU to the `--gres=` option (with either `srun` or `sbatch`). For a list of available GPU types, refer to the GPU Types column in the table, at the top of this page, that are listed as *Public*.

:::{code-block} bash
---
caption: Command to request one p100 GPU.
---
--gres=gpu:p100:1
:::

:::{note}
Requesting a specific type of GPU could result in longer wait times, based on GPU availability at that time.
:::

## Using CUDA
There are several versions of CUDA Toolkits available on the HPC, including. Use the `module avail` command to check for the latest software versions on the cluster.

:::{code-block} bash
---
emphasize-lines: 3-5
---
$ module avail cuda

------------------------------- /shared/centos7/modulefiles -------------------------------
cuda/10.0    cuda/10.2          cuda/11.1    cuda/11.3    cuda/11.7    cuda/12.1    cuda/9.1
cuda/10.1    cuda/11.0(default) cuda/11.2    cuda/11.4    cuda/11.8    cuda/9.0     cuda/9.2
:::

To see details on a specific CUDA toolkit version, use `module show` (e.g., `module show cuda/11.4`).

To add CUDA to your path, use `module load` (e.g., `module load cuda/11.4` adds CUDA 11.4).

:::{note}
Executing `nvidia-smi` (i.e., NVIDIA System Management Interface) on a GPU node displays the CUDA driver information and monitor the GPU device.
:::

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

Select the tab with the desire deeplearning framework.

:::{important}
Each tab assumes you are on a GPU node before with CUDA 11.8 and anaconda modules loaded as done above.
:::
::::::{tab-set}
:::::{tab-item} PyTorch
The following example demonstrates how to build PyTorch inside a conda virtual environment for CUDA version 11.8.


::::{code-block} bash
---------------------
caption: |
    PyTorch's installation steps for Python 3.9 and Cuda 11.8:
---
conda create --name pytorch_env python=3.10 -y
source activate pytorch_env
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
::::
Now, let's check the installation:
::::{code} bash
python -c 'import torch; print(torch.cuda.is_available())'
::::

If CUDA is detected by PyTorch, you should see the result, `True`.

:::{seealso}
[PyTorch documentation] for the most up-to-date instructions and for different CUDA versions.
::::
:::::
:::::{tab-item} TensorFlow

Here are steps for installing CUDA 11.8 with the latest version of TensorFlow (TF).

::::{seealso}
[Compatibility of CUDA and TensorFlow versions](https://www.tensorflow.org/install/source#gpu), and [detailed installation instructions](https://www.tensorflow.org/install/pip).
::::

For the latest installation, use the TensorFlow pip package, which includes GPU support for CUDA-enabled devices:

::::{code-block} bash
---------------------
caption: |
    Tensorflow's installation steps for Python 3.9 and Cuda 11.8:
---
conda create --name TF_env python=3.9 -y
source activate TF_env
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit -y
pip install --upgrade pip
pip install tensorflow==2.13.*
::::

Verify the installation:

:::{code} bash
python3 -c 'import tensorflow as tf; print(tf.test.is_built_with_cuda())' # True
::::

::::{note}
Ignore the `Warning` messages that get generated after executing the above commands.
::::
:::::
:::::{tab-item} PyTorch + TensorFlow
::::{code-block} bash
---------------------
caption: |
    PyTorch and Tensorflow's installation steps for Python 3.9 and Cuda 11.8:
---
conda create --name deeplearning-cuda11_8 python=3.9 -y
source activate deeplearning-cuda11_8
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit -y
pip install --upgrade pip
pip install tensorflow==2.13.*
::::

Verify installation:

:::{code} bash
python -c 'import torch; print(torch.cuda.is_available())' # True
python3 -c 'import tensorflow as tf; print(tf.test.is_built_with_cuda())' # True
::::
:::::

::::::

::::{tip}
Install `jupyterlab` and few other commonly used datascience packages in the `pytorch_env` environment:
:::{code} bash
conda install pandas scikit-learn matplotlib seaborn jupyterlab -y
:::
::::

[P100]: https://www.nvidia.com/en-us/data-center/tesla-p100/
[PyTorch documentation]: https://pytorch.org/
[Volta]: https://www.nvidia.com/en-us/data-center/volta-gpu-architecture/
[Turing]: https://developer.nvidia.com/blog/nvidia-turing-architecture-in-depth/
[T4]: https://www.nvidia.com/en-us/data-center/tesla-t4/
[Quadro RTX 8000]: https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/quadro-rtx-8000-us-nvidia-946977-r1-web.pdf
[Ampere]: https://www.nvidia.com/en-us/data-center/ampere-architecture/
[A30]: https://www.nvidia.com/en-us/data-center/products/a30-gpu/
[A100]: https://www.nvidia.com/en-us/data-center/a100/
[Pascal]: https://www.nvidia.com/en-us/data-center/pascal-gpu-architecture/
[RTX A5000]: https://www.nvidia.com/en-us/design-visualization/rtx-a5000/
[RTX A6000]: https://www.nvidia.com/en-us/design-visualization/rtx-a6000/
[ServiceNow ticket]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7
