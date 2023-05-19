(working-gpus)=

# Working with GPUs

The Discovery cluster has a number of NVIDIA Graphics Processing Units (GPUs) available, as detailed in the table below.

:::{note}
The tables on this page slide from left-to-right. Make sure to
swipe to right to see the content on the right side of the table
:::

```{eval-rst}
.. list-table::
  :widths: 40 40 40 40 40 40
  :header-rows: 1

  * - GPU Type
    - GPU Memory
    - Tensor Cores
    - CUDA Cores
    - Nodes in Public GPUs
    - Nodes in Private GPUs
  * - p100 (`Pascal <https://www.nvidia.com/en-us/data-center/tesla-p100/>`_)
    - 12GB
    - N/A
    - 3,584
    - 12 with 3-4 GPUs each
    - 3 with 4 GPUs each
  * - v100-pcie (`Volta <https://www.nvidia.com/en-us/data-center/v100/>`_)
    - 32GB
    - 640
    - 5,120
    - 4 with 2 GPUs each
    - 1 with (16GB) 2 GPUs
  * - v100-sxm2 (Volta)
    - 32GB
    - 640
    - 5,120
    - 24 with 4 GPUs each
    - 10 with 4 GPUs each & 16GB GPU memory; 8 with 4 GPUs & 32GB GPU memory
  * - t4 (`Turing <https://www.nvidia.com/en-us/data-center/tesla-t4/>`_)
    - 15GB
    - 320
    - 2,560
    - 2 with 3-4 GPUs each
    - 1 with 4 GPUs
  * - quadro (`Quadro RTX 8000 <https://www.nvidia.com/en-us/design-visualization/previous-quadro-desktop-gpus/>`_)
    - 46GB
    - 576
    - 4,608
    - 0
    - 2 with 3 GPUs each
  * - a30 ( `Ampere <https://www.nvidia.com/en-us/data-center/products/a30-gpu/>`_)
    - 24GB
    - 224
    - 3,804
    - 0
    - 1 with 3 GPUs
  * - a100 (`Ampere <https://www.nvidia.com/en-us/data-center/a100/>`_)
    - 41 & 82GB
    - 432
    - 6,912
    - 3 nodes with 4 GPUs each
    - 15 nodes with 2-8 GPUs each
  * - a5000 (`Ampere RTX A5000 <https://www.nvidia.com/en-us/design-visualization/rtx-a5000/>`_)
    - 24GB
    - 256
    - 8,192
    - 0
    - 6 with 8 GPUs each
  * - a6000 (`Ampere RTX A6000 <https://www.nvidia.com/en-us/design-visualization/rtx-a6000/>`_)
    - 49GB
    - 336
    - 10,752
    - 0
    - 3 with 8 GPUs each
```

The public GPUs are available within two partitions, named `gpu` and
`multigpu`. The differences between the two partitions are the
number of GPUs that one can request per job and the time limit on each
job. Both partitions give access to all of the public GPU types
mentioned above. The table below shows the differences between the two
partitions. For more information about the partitions on Discovery,
see {ref}`partition_names`.

:::{note}
All user limits are subject to the availability of cluster
resources at the time of submission and will be honored according to that.
:::

```{eval-rst}
.. list-table::
   :widths: 20 20 20 20 20 20
   :header-rows: 1

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
```

Anyone with a Discovery account can use the `gpu`
partition. However, you must submit a [ServiceNow ticket](https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7)
to request temporary access to multigpu for testing, or to request
full access to the `multigpu` partition.  Your request will be
evaluated by members of the RC team to ensure that the resources in
this partition will be used appropriately.

## Requesting GPUs with `srun` or `sbatch`

Use `srun` for interactive and `sbatch` for batch mode. The
`srun` example below is requesting 1 node and 1 GPU with 4GB of
memory in the `gpu` partition. You must use the `--gres=` option
to request a gpu:

```
srun --partition=gpu --nodes=1 --pty --gres=gpu:1 --ntasks=1 --mem=4GB --time=01:00:00 /bin/bash
```

:::{note}
On the `gpu` partition, requesting more than 1 GPU
(`--gres=gpu:1`) will cause your request to fail. Additionally,
one cannot request all the CPUs on that gpu node as they are
reserved for other GPUs.
:::

The `sbatch` example below is similar to the `srun` example above,
but it submits the job in the background, gives it a name, and directs
the output to a file:

```
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
<your code>
```

### Specifying a GPU type

You can add a specific type of GPU to the `--gres=` option (with
either `srun` or `sbatch`). For a list of available GPU types,
refer to the GPU Types column in the table, at the top of this page,
that are listed as `Public`. The following is an example for
requesting a single p100 GPU:

```
--gres=gpu:p100:1
```

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

## Using GPUs with PyTorch

You should use PyTorch with a conda virtual environment if you need to
run the environment on the Nvidia GPUs on Discovery. The following
example demonstrates how to build PyTorch inside a conda virtual
environment for CUDA version 11.7.

:::{note}
Make sure to be on a GPU node before loading the
environment. Additionally, the latest version of PyTorch is not
compatible with GPUs with CUDA version 11.7 or less. Hence, the
installation does not work on k40m or k80 GPU's. In order to see
what `non-Kepler` GPUs might be available, one can execute this
command:

```
sinfo -p gpu --Format=nodes,cpus,memory,features,statecompact,nodelist,gres
```

This will indicate the state (idle or not) of a certain gpu-type
that could be helpful in requesting an `idle` gpu. However, the
command does not give real-time information of the state and should
be used with caution.
:::

PyTorch installation steps (with a specific GPU-type):

```
srun --partition=gpu --nodes=1 --gres=gpu:v100-sxm2:1 --cpus-per-task=2 --mem=10GB --time=02:00:00 --pty /bin/bash
module load anaconda3/2022.05 cuda/11.7
conda create --name pytorch_env python=3.9 -y
source activate pytorch_env
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia -y
python -c'import torch; print(torch.cuda.is_available())'
```

:::{note}
If the installation times out, please ensure that your .condarc
file doesn't contain additional channels. Also, consider cleaning
your conda instance using the `conda clean` command. See [Conda
best practices](https://rc-docs.northeastern.edu/en/latest/software/conda.html#conda-best-practices) .
:::

If CUDA is detected by PyTorch, you should see the result, `True`.

As the latest version of PyTorch often depends on the newest CUDA
available, please refer to the [PyTorch documentation page](https://pytorch.org/) for the most up to date instructions on
installation.

The above PyTorch installation instructions will not include
`jupyterlab` and few other commonly used datascience packages in the
environment. In order to include those one can execute the following
command after activating the `pytorch_env` environment:

```
conda install pandas scikit-learn matplotlib seaborn jupyterlab -y
```

## Using GPUs with TensorFlow

We recommend that you use CUDA 11.2 (latest supported version) when
working on a GPU with the latest version of TensorFlow (TF).
TensorFlow provides information on the [compatibility of CUDA and
TensorFlow versions](https://www.tensorflow.org/install/source#gpu),
and [detailed installation instructions](https://www.tensorflow.org/install/pip).

For the latest installation, use the TensorFlow pip package, which
includes GPU support for CUDA-enabled devices:

```
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
```

Verify the installation:

```
# Verify the CPU setup (if successful, then a tensor is returned):
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

# verify the GPU setup (if successful, then a list of GPU device is returned):
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# test if a GPU device is detected with TF (if successful, then True is returned):
python3 -c 'import tensorflow as tf; print(tf.test.is_built_with_cuda())'
```

To get the name of the GPU, type:

```
python -c 'import tensorflow as tf;  print(tf.test.gpu_device_name())'
```

If the installation is successful, then, for example, you should see
the following as an output,:

```
2023-02-24 16:39:35.798186: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1613] Created device /device:GPU:0 with 10785 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:0a:00.0, compute capability: 3.7 /device:GPU:0
```

:::{note}
Ignore the `Warning` messages that get generated after executiing
the above commands.
:::

test
