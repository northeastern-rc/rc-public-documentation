(gpu-job-submission)=
# GPU Job Submission

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

Select the tab with the desire deeplearning framework.

:::{important}
Each tab assumes you are on a GPU node before with CUDA 11.8 and anaconda modules loaded as done above.
:::
::::::{tab-set}
:::::{tab-item} PyTorch
The following example demonstrates how to build PyTorch inside a conda virtual environment for CUDA version 12.1.

::::{code-block} bash
---------------------
caption: |
    PyTorch's installation steps for Python 3.10 and Cuda 12.1:
---
srun --partition=gpu --nodes=1 --gres=gpu:v100-sxm2:1 --cpus-per-task=2 --mem=10GB --time=02:00:00 --pty /bin/bash
module load anaconda3/2022.05 cuda/12.1
conda create --name pytorch_env -c conda-forge python=3.10 -y
source activate pytorch_env
conda install jupyterlab -y
pip3 install torch torchvision torchaudio
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
module load anaconda3/2022.05 cuda/11.8
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
    Tensorflow's installation steps for Python 3.9 and Cuda 12.1:
---
srun -p gpu --gres=gpu:v100-pcie:1 --pty /bin/bash
module load anaconda3/2022.05
module load cuda/12.1
conda create --name TF_env python=3.9 -y
source activate TF_env
pip install --upgrade pip
pip install tensorflow[and-cuda]
pip install jupyterlab
::::

Verify the installation:

::::{code} bash
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))" # True
::::

::::{note}
Ignore the `Warning` messages that get generated after executing the above commands.
::::
:::::
::::::