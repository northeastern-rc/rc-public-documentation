.. _working_gpus:

******************
Working with GPUs
******************
The Discovery cluster has a number of Graphics Processing Units (GPUs) available, as detailed in the table below.

.. list-table::
  :widths: 40 40 40 40 40
  :header-rows: 1

  * - GPU Type
    - Number of nodes/GPUs
    - CPU Type
    - CPUs/node
    - RAM per node
    - GPU Memory
    - Tensor Cores
    - Cuda Capibility 
  * - p100 (Pascal)
    - 12 nodes with 4 GPUs each
    - broadwell
    - 28
    - 512GB
    - 
  * - v100-pcie (Volta)
    - 4 nodes with 2 GPUs each
    - AMD zen
    - 32
    - 480GB
  * - v100-sxm2 (Volta)
    - 24 nodes with 4 GPUs each
    - Intel skylake_avx512
    - 28
    - 187GB
  * - t4 (Turing)
    - 2 nodes with 4 GPUs each
    - Intel skylake_avx512
    - 28  
    - 187GB
  * - a100 (Ampere)
    - 1 node with 4 GPUs
    - AMD zen3
    - 64  
    - 512GB    

These GPUs are available within two partitions, named ``gpu`` and
``multigpu``. The differences between the two partitions are the
number of GPUs that one can request per job and the time limit on each
job. Both partitions give access to all of the above GPU types. The
table below shows the differences between the two partitions. For more
information about the partitions on Discovery, see
:ref:`partition_names`.

.. list-table::
   :widths: 20 20 20 20 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Requires Approval?
     - Time limit (Default/Max)
     - Running Jobs
     - Submitted Jobs
     - Core Limit
     - RAM Limit
     - GPU per job Limit
     - GPU per user Limit
   * - gpu
     - No
     - 4 hours/8 Hours
     - 25/250
     - 50/100
     - N/A
     - N/A
     - 1
     - 8
   * - multigpu
     - **Yes**
     - 4 hours/24 Hours
     - 25/100
     - 50/100
     - N/A
     - N/A
     - 12
     - 12

Anyone with a Discovery account can use the ``gpu`` partition. However, you must submit a `ServiceNow ticket <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7>`_ to request temporary access to multigpu for testing, or to request full access to the ``multigpu`` partition.  
Your request will be evaluated by members of the RC team to ensure that the resources in this partition will be used appropriately.

Requesting GPUs with ``srun`` or ``sbatch``
===========================================
Use ``srun`` for interactive mode and ``sbatch`` for batch mode. The ``srun`` example below is requesting 1 node and 1 GPU with 4GB of memory in the ``gpu`` partition. You must use the ``--gres=`` option to request a gpu::

  srun --partition=gpu --nodes=1 --pty --gres=gpu:1 --ntasks=1 --mem=4GB --time=01:00:00 /bin/bash

.. note::
   On the ``gpu`` partition, requesting more than 1 GPU (``--gres=gpu:1``) will cause your request to fail. Also, you cannot request all CPUs on that node, since they are reserved for other GPUs.

The ``sbatch`` example below is similar to the ``srun`` example above, but it gives the job a name and directs the output to a file::

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

Specifying a GPU type
+++++++++++++++++++++
You can add a specific type of GPU to the ``--gres=`` option (with either ``srun`` or ``sbatch``). For a list of available GPU types, refer to the GPU Types column in the table at the top of this page. The following example is a request for 1 p100 GPU::

  --gres=gpu:p100:1

.. note::
   Requesting a specific type of GPU could result in longer wait times, based on GPU availability at that time. 

Using CUDA
===========
There are several versions of CUDA Toolkits on Discovery, including::

  cuda/9.0
  cuda/9.2
  cuda/10.0
  cuda/10.2
  cuda/11.0
  cuda/11.1
  cuda/11.2
  cuda/11.3
  cuda/11.4

Use the ``module avail`` command to check for the latest software versions on Discovery. To see details on a specific CUDA toolkit version, use ``module show``. For example, ``module show cuda/11.4``.

To add CUDA to your path, use ``module load``. For example, type ``module load cuda/11.4`` to load version 11.4 to your path.

Use the command ``nvidia-smi`` (NVIDIA System Management Interface) inside a GPU node to get the CUDA driver information and monitor the GPU device.

Using GPUs with PyTorch
========================
You should use PyTorch with a conda virtual environment if you need to run the environment on the Nvidia GPUs on Discovery. The following examples demonstrate how to build PyTorch inside a conda virtual environment for CUDA version 11.7. 
Make sure that you are on a GPU node before loading the environment. Please note, the installation does not work on k40m or k80 GPU's

PyTorch installation steps (with Anaconda libraries)::

  srun --partition=gpu --nodes=1 --pty --gres=gpu:v100-sxm2:1 --ntasks=1 --mem=4GB --time=01:00:00 /bin/bash
  module load cuda/11.7
  module load anaconda3/2022.05
  conda create --name pytorch_env python=3.9 -y
  source activate pytorch_env
  conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia -y
  python -c'import torch; print(torch.cuda.is_available())'

.. note::
   If the installation times out, please ensure that your .condarc file doesn't contain additional channels. Also, consider cleaning your conda instance using the conda clean command.

If CUDA is detected by PyTorch, you should see the result, ``True``.

As the latest version of PyTorch often depends on the newest CUDA available, please refer to the `PyTorch documentation page <https://pytorch.org/>`_ for the installation instructions. 

Alternatively, you can use the existing Pytorch build (`pytorch_env_training` environment, PyTorch version 1.8.0, works with cuda/11.1 on any GPU including k40m & k80) by typing::

  srun --partition=gpu --nodes=1 --pty --gres=gpu:1 --ntasks=1 --mem=4GB --time=01:00:00 /bin/bash
  module load anaconda3/2022.01 
  module load cuda/11.1 
  source activate pytorch_env_training

Using GPUs with TensorFlow
==========================
We recommend that you use CUDA 11.2 (latest supported version) when working on a GPU with the latest version of TensorFlow (TF).
TensorFlow provides information on the `compatibility of CUDA and TensorFlow versions <https://www.tensorflow.org/install/source#gpu>`_, and `detailed installation instructions <https://www.tensorflow.org/install/pip>`_. 

For the latest installation, use the TensorFlow pip package, which includes GPU support for CUDA-enabled devices::

  srun --partition=gpu --gres=gpu:1 --nodes=1 --ntasks=1 --mem=10GB --time=01:00:00 --pty /bin/bash
  module load anaconda3/2022.05
  module load cuda/11.2
  conda create --name TF_env python=3.9 -y
  source activate TF_env
  conda install -c conda-forge cudatoolkit=11.2.2 cudnn=8.1.0 -y
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
  mkdir -p $CONDA_PREFIX/etc/conda/activate.d
  echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
  pip install --upgrade pip
  pip install tensorflow==2.11.*

Verify the installation::

  # Verify the CPU setup (if successful, then a tensor is returned):
  python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"

  # verify the GPU setup (if successful, then a list of GPU devices is returned):
  python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

  # test if a GPU device is detected with TF (if successful, then True is returned):
  python3 -c 'import tensorflow as tf; print(tf.test.is_built_with_cuda())' 

To get the name of the GPU, type::

   python -c 'import tensorflow as tf;  print(tf.test.gpu_device_name())'

If the installation is successful, then you should see the following output,::

   2023-02-24 16:39:35.798186: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1613] Created device /device:GPU:0 with 10785 MB memory:  -> device: 0, name: Tesla K80, pci bus id: 0000:0a:00.0, compute capability: 3.7 /device:GPU:0
