(gpu-job-submission)=
# GPU Job Submission

::::{sidebar}
:::{seealso}
{ref}`accessing-gpus`
:::
::::

## Using CUDA
There are several versions of CUDA Toolkits available on the HPC. Use the `module avail` command to check for the latest software versions on the cluster.

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

Select the tab with the desired deep learning framework.

:::{important}
Each tab assumes you are on a GPU node with CUDA 11.8 and anaconda modules loaded as done above.
:::
::::::{tab-set}
:::::{tab-item} PyTorch
The following example demonstrates how to build PyTorch inside a conda virtual environment for CUDA version 11.8.


::::{code-block} bash
---------------------
caption: |
    PyTorch's installation steps for Python 3.9 and Cuda 11.8:
---
conda create --name pytorch_env python=3.9 -y
source activate pytorch_env
conda install jupyterlab -y
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
::::
Now, let us check the installation:
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
conda create --name tensorflow_env python=3.9 -y
source activate tensorflow_env
conda install jupyterlab -y
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit -y
pip install --upgrade pip
pip install tensorflow[and-cuda]==2.13.*
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
conda create --name deeplearning_env python=3.9 -y
source activate deeplearning_env
conda install jupyterlab -y
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia -y
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit -y
pip install --upgrade pip
pip install tensorflow[and-cuda]==2.13.*
::::

Verify installation:

:::{code} bash
python -c 'import torch; print(torch.cuda.is_available())' # True
python3 -c 'import tensorflow as tf; print(tf.test.is_built_with_cuda())' # True
::::
:::::

::::::

::::{tip}
Install other commonly used datascience packages in the `pytorch_env`, `tensorflow_env`, or the `deeplearning_env` environment:
:::{code} bash
conda install pandas scikit-learn matplotlib seaborn -y
:::
For the `tensorflow_env` or the `deeplearning_env`, install with `conda install` prior to your first `pip install` and use `pip install` after your first `pip install` in the environment. 
::::

[PyTorch documentation]: https://pytorch.org/
