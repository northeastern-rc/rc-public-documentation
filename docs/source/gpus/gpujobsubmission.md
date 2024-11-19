(gpu-job-submission)=
# GPU Job Submission

## Using CUDA
There are several versions of CUDA Toolkits available on our HPC cluster. To see several versions available, use the `module avail` command to check for the latest software versions on the cluster.

:::{code-block} bash
---
emphasize-lines: 3-5
---
$ module avail cuda

------------------------------- /shared/EL9/explorer/modulefiles -------------------------------
cuda/12.1.1    cuda/12.3.0
:::

To see details on a specific CUDA toolkit version, use `module show` (e.g., `module show cuda/12.1.1`).

To add CUDA to your path, use `module load` (e.g., `module load cuda/12.1.1` adds CUDA 12.1.1).

:::{note}
Executing `nvidia-smi` (i.e., NVIDIA System Management Interface) on a GPU node displays the CUDA driver information and monitor the GPU device.
:::

(gpus-for-deep-learning)=
## GPUs for Deep Learning

:::{seealso}
Deep learning frameworks tend to cost storage that can quickly surpass {ref}`home-directory-storage-quota`: follow best practices for {ref}`best-practices-conda-environments`.
:::

Select the tab with the desire deeplearning framework.

:::{important}
Each tab helps you get on a GPU node and load CUDA and anaconda modules, as shown below.
:::
::::::{tab-set}
:::::{tab-item} PyTorch
The following example demonstrates how to build PyTorch inside a conda virtual environment for CUDA version 12.1.1.

::::{code-block} bash
---------------------
caption: |
    PyTorch's installation steps for Python 3.12.4 and Cuda 12.1.1:
---
srun --partition=gpu --nodes=1 --gres=gpu:v100-sxm2:1 --cpus-per-task=2 --mem=10GB --time=02:00:00 --pty /bin/bash
module purge
module load explorer anaconda3/2024.06 cuda/12.1.1
conda create --name pytorch_env -c conda-forge python=3.12.4 -y
source activate pytorch_env
conda install jupyterlab -y
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu121
::::

Now, let us check the installation:

::::{code} bash
python -c 'import torch; print(torch.cuda.is_available())'
::::

If CUDA is detected by PyTorch, you should see the result, `True`.

If you want to use an older version of CUDA, here is the following example that demonstrates how to build PyTorch inside a conda virtual environment for CUDA version 11.8.

::::{code-block} bash
---------------------
caption: |
    PyTorch's installation steps for Python 3.10 and Cuda 11.8:
---
srun --partition=gpu --nodes=1 --gres=gpu:v100-sxm2:1 --cpus-per-task=2 --mem=10GB --time=02:00:00 --pty /bin/bash
module load anaconda3/2024.06 cuda/11.8
conda create --name pytorch_env -c conda-forge python=3.10 -y
source activate pytorch_env
conda install jupyterlab -y
pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118
::::

Now, let us check the installation:

::::{code} bash
python -c 'import torch; print(torch.cuda.is_available())'
::::

If CUDA is detected by PyTorch, you should see the result, `True`.

:::{seealso}
[PyTorch documentation](https://pytorch.org/) for the most up-to-date instructions and for different CUDA versions.
:::
:::::
:::::{tab-item} TensorFlow

Here are steps for installing CUDA 12.1 with the latest version of TensorFlow (TF).

::::{seealso}
[Compatibility of CUDA and TensorFlow versions](https://www.tensorflow.org/install/source#gpu), and [detailed installation instructions](https://www.tensorflow.org/install/pip).
::::

For the latest installation, use the TensorFlow pip package, which includes GPU support for CUDA-enabled devices:

::::{code-block} bash
---------------------
caption: |
    Tensorflow's installation steps for Python 3.12.4 and Cuda 12.1:
---
srun -p gpu --gres=gpu:v100-pcie:1 --pty /bin/bash
module load anaconda3/2024.06 cuda/12.1.1
conda create --name TF_env python=3.12.4 -y
source activate TF_env
pip install --upgrade pip
pip install tensorflow[and-cuda]
pip install jupyterlab
::::

Verify the installation:

::::{code} bash
python -c 'import tensorflow as tf; print("True" if tf.config.list_physical_devices("GPU") else "False")'
::::

If CUDA is detected by Tensorflow, you should see the result, `True`.

::::{note}
Ignore the `Warning` messages that get generated after executing the above commands.
::::
:::::
::::::
