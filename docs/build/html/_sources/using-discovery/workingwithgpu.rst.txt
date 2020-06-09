******************
Working with GPUs
******************
The Discovery cluster has a number of Graphics Processing Units (GPUs) available, as detailed in the table below.

.. list-table::
  :widths: 40 40 40 40
  :header-rows: 1

  * - GPU Type
    - Number of nodes/GPUs
    - CPU Type
    - RAM per node
  * - k20m
    - 23 nodes with 1 GPU each
    - E5-2650\@\2.00GHz
    - 128GB
  * - k40m
    - 16 nodes with 1 GPU each
    - E5-2690v3\@\2.60GHz
    - 128GB
  * - k80
    - 8 nodes with 8 GPUs each
    - E5-2680v4\@\2.40GHz
    - 512GB
  * - p100
    - 12 nodes with 4 GPUs each
    - E5-2680v4\@\2.40GHz
    - 512GB
  * - v100
    - 4 nodes with 2 GPUs each
    - AMD EPYC 7351\@\2.60GHz
    - 480GB
  * - v100-sxm2
    - 24 nodes with 4 GPUs each
    - Intel Gold 6132\@\2.60Ghz
    - 187GB

These GPUs are available within two partitions, named ``gpu`` and ``multigpu``. Note that partitions on Discovery are not physical partitions, they  are virtual partitions. The differences between the two partitions are the number of GPUs that you can request per job, as well as the time
limit on each job. Both partitions give you access to all of the above GPU types. See the table below for the differences between the two partitions.

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
     - 8
     - 8

Anyone with an account on Discovery can use the ``gpu`` partition. Using ```multigpu`` requires an application process, which includes documenting
the need for using ``multigpu``. You can find the application for ``multigpu`` and how to submit it in the Policies section on the
`RC website <https://rc.northeastern.edu/files/2020/02/access_request_multigpu.docx>`_.

Requesting GPUs with ``srun`` or ``sbatch``
===========================================
Use ``srun`` for interactive mode and ``sbatch`` for batch mode.

The ``srun`` example below is requesting 1 node and 1 GPU with 1GB of memory in the ``gpu`` partition. Note that on the ``gpu`` partition, you cannot request more than 1 GPU (``--gres=gpu:1``)
or your request will fail.

``srun --partition gpu --nodes 1 --pty --export=All --gres=gpu:1 --mem=1Gb --time=00:30:00 /bin/bash``

The ``sbatch`` example below is the similar to the ``srun`` example above, except for giving the job a name and directing the output to a file::

  #SBATCH --nodes=1
  #SBATCH --time=0:30:00
  #SBATCH --job-name=gpu_run
  #SBATCH --mem=1Gb
  #SBATCH --gres=gpu:1
  #SBATCH --output=exec.%j.out
  <your code>

Specifying a GPU type
+++++++++++++++++++++
You can add a specific type of GPU to the ``--gres=`` option (with either ``srun`` or ``sbatch``). For example::

  --gres=gpu:k40m:1

Note that specifying one type of GPU could result in a longer wait time for that specific resource.

Using CUDA
===========
Currently, there are four versions of CUDA on Discovery::

  cuda/9.0
  cuda/9.2
  cuda/10.0
  cuda/10.2

You can always use the ``module avail`` command to check for the latest software versions on Discovery as well.

To add CUDA to your path use ``module load``. For example, type ``module load cuda/10.0`` to load version 10 to your path.

Using GPUs with PyTorch
========================
You should use PyTorch with a conda virtual environment if you need to run the environment on the Nvidia GPUs on Discovery.

The following is an example of using a conda virtual environment with PyTorch. Make sure that you are on a GPU node before loading the environment::

  module load cuda/10.2
  module load anaconda3/3.7
  conda create --name pytorch_env python=3.7 anaconda
  conda activate pytorch_env
  conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
  python -c'import torch; print(torch.cuda.is_available())'

Using TensorFlow
================
We recommend that you use CUDA 10.2 with the latest version of TensorFlow. You can find the compatibility of CUDA and TensorFlow versions here – https://www.tensorflow.org/install/source#gpu.::

  module load anaconda3/3.7
  module load cuda/10.2
  conda create --name TF_env python=3.7 anaconda #where TC_env is the name of the conda environment
  conda  activate TF_env
  conda install -c anaconda tensorflow-gpu

If you want to test your environment, first make sure you are on GPU node, then type::

   python -c 'import tensorflow as tf;  print(tf.test.is_built_with_cuda())'

You should see the result ``True`` if successful.

To get the name of the GPU, type::

   python -c 'import tensorflow as tf;  print(tf.test.gpu_device_name())'

For example, you should see output like the line below::

   physical GPU (device: 0, name: Tesla K40m, pci bus id: 0000:0b:00.0, compute capability: 3.5) /device:GPU:0
