(using-matlab)=
# Using MATLAB

::::{sidebar}
:::{seealso}
{ref}`using-module` and {ref}`using-ood`.
:::
::::
MATLAB is available on the cluster as a module and as an interactive app on Open OnDemand. You can also download MATLAB for your computer through the [Northeastern portal on the MATLAB website](https://www.mathworks.com/academia/tah-portal/northeastern-university-30294223.html). Note that the procedures detailed below pertain specifically to using MATLAB on the cluster, and not to using MATLAB on your computer.

## Installing MATLAB toolboxes

Use the following procedure if you need to install a MATLAB toolbox:

1. Download the toolbox from its source website.

1. Connect to the cluster.

1. Create a directory in your /home directory. We recommend creating a directory called `matlab` by typing:

   :::
   mkdir /home/<username>/matlab  #where <username> is your username
   :::

1. Go to the directory you just created by typing:

   :::
   cd /home/<username>/matlab
   :::

1. Unzip the toolbox file by typing:

   :::
   unzip <toolboxname>
   :::

1. Load MATLAB by typing:

   :::
   module load matlab
   :::

1. Start MATLAB by typing:

   :::
   matlab
   :::

1. Add the toolbox to your PATH by typing:

   :::
   addpath('/home/<username>/matlab/<toolbox>') #where <toolbox> is the name of the toolbox you just unzipped
   :::

1. If this is a toolbox you want to use more than once, you should save it to your path by typing:

   :::
   savepath()
   :::

1. You can now use the toolbox within MATLAB. When you are done, type `quit`.

## Using MATLAB Parallel Server


### Configuration of MATLAB client on the HPC

The cluster has MATLAB Parallel Server installed. This section details an example of how you can set up and use the MATLAB Parallel Computing Toolbox. This walkthrough uses MATLAB launched as an interactive app on the Open OnDemand web portal. There are several parts to this walkthrough. We suggest that you read it through completely before starting. The parameters presented represent only one scenario.

1. Go to <http://ood.discovery.neu.edu>. If prompted, sign in with your cluster username and password.

1. Click **Interactive Apps**, and select **MATLAB**.

1. Select **MATLAB version R2023a** or newer, and set the time for the length of your job, the number of cpus to be 8, and the memory to at least 16 GB. Click **Launch**.

1. If necessary, adjust the **Compression** and **Image Quality**, and then click **Launch MATLAB**.

1. Once MATLAB is open, click on the Home tab, click Parallel > Discover Clusters... to discover the profile. Note, this is valid for R2023a and newer. Alternatively, you can create a cluster profile to run parallel jobs by running `configCluster` in the Command Window. Note: `configCluster` should only be called once on the HPC.

Now MATLAB is configured to have jobs submitted to the HPC cluster and not run in the current session.

### Installation and Configuration of MATLAB on a local machine

MATLAB can be configured on your local machine to submit jobs to the HPC cluster. To complete this, please follow the following steps:


### Configuring Jobs

Prior to submitting jobs to the HPC, various parameters can be assigned and adjusted for your job such as partition, email, job walltime, etc. 

To get a handle on the cluster and the current configurations please run the following command in the Command Window:

```{code-block} matlab
>> % Get a handle to the cluster
>> c = parcluster;
```

A required field that needs to be set is the memory per CPU core:

```{code-block} matlab
>> % Specify memory to use, per core (default: 4gb)
>> c.AdditionalProperties.MemPerCPU = '6gb';
```

You need to save the changes after modifying the AdditionalProperties:

```{code-block} matlab
>> c.saveProfile
```

To view the values of the currently saved configuration, use the following command in the Command Window:

```{code-block} matlab
>> % To view current properties
>> c.AdditionalProperties
```

If you need to unset a saved parameter, you can do the following in the Command Window:

```{code-block} matlab
>> % Turn off email notifications 
>> c.AdditionalProperties.EmailAddress = '';
>> c.saveProfile
```

The following are optional fields that can be set and adjusted for the parcluster and include the following items.

Specifying a constaint such as a CPU constraint ():

```{code-block} matlab
>> % Specify a constraint 
>> c.AdditionalProperties.Constraint = 'feature-name';
```

Setting an email to receive updates on the SLURM job:

```{code-block} matlab
>> % Request email notification of job status
>> c.AdditionalProperties.EmailAddress = 'user-id@northeastern.edu';
```

Setting the number of GPUs used and the type of GPU ():

```{code-block} matlab
>> % Specify number of GPUs (default: 0)
>> c.AdditionalProperties.GPUsPerNode = 1;
>> c.AdditionalProperties.GPUCard = 'gpu-card';
```

```{note}
You need to make sure the partition you are submitting the job to is the `gpu` or `multigpu` partition of a private partition that has GPUs available.
```

Selecting the partition () you want the job to run on the HPC cluster:

```{code-block} matlab
>> % Specify the partition	
>> c.AdditionalProperties.Partition = 'partition-name';
```

Setting the number of cores for the job:

```{code-block} matlab
>> % Specify cores per node (default: 0)
>> c.AdditionalProperties.ProcsPerNode = 4;
```

Setting exclusive use of the node:

```{code-block} matlab
>> % Set node exclusivity (default: false)
>> c.AdditionalProperties.RequireExclusiveNode = true;
```

```{note}
The exclusive node option can increase your wait time in the queue so only user if required.
```

If you are running the job on a reservation that has be setup:

```{code-block} matlab
>> % Use reservation 
>> c.AdditionalProperties.Reservation = 'reservation-name';
```

Setting the time for the job to run on the HPC cluster:

```{code-block} matlab
>> % Specify the wall time (e.g., 1 day, 5 hours, 30 minutes)
>> c.AdditionalProperties.WallTime = '1-05:30';
```

```{note}
You need to make sure the time matches the partition you are submitting to or the jobs will not run.
```

### Using the MATLAB client interactively on the HPC cluster

If you want to run an interactive pool job on the cluster, you can continue to use the `parpool` that was set above:

```{code-block} matlab

```

### Using parcluster example

:::{note}
For this example, please select 6 hours, 65 cpus, and 130 GB of memory.
:::

This section provides instructions for submitting a job to the cluster for scaling calculations on an integer factorization sample problem. The complexity of this problem increases with the magnitude of the number, making it computationally intensive. To perform these calculations, we will use the `myParallelAlgorithmFcn.m` MATLAB function. Please note that this section assumes you have already started a MATLAB Parallel Server.

There are benchmarking scripts and examples available in **`**/shared/centos7/matlab/R2020a/examples/parallel/main/**`** on the cluster.

To make the scripts and examples available, add the path to this folder to the list of available paths by doing one of the following:

- On the MATLAB Home tab, in the **Environment** section, click **Set Path** and add the path to the script.
- Alternatively, provide the script's full path in the MATLAB command line.

The contents of _myParallelAlgorithmFcn_ are as follows:

```{code-block} matlab
function [numWorkers,time] = myParallelAlgorithmFcn ()

complexities =  [2^18 2^20 2^21 2^22];
numWorkers = [1 2 4 6 16 32 64];

time = zeros(numel(numWorkers),numel(complexities));

% To obtain predictable sequences of composite numbers, fix the seed
% of the random number generator.
rng(0,'twister');

for c = 1:numel(complexities)

   primeNumbers = primes(complexities(c));
   compositeNumbers =    primeNumbers.*primeNumbers(randperm(numel(primeNumbers)));
   factors = zeros(numel(primeNumbers),2);

   for w = 1:numel(numWorkers)
       tic;
       parfor (idx = 1:numel(compositeNumbers), numWorkers(w))
          factors(idx,:) = factor(compositeNumbers(idx));
       end
       time(w,c) = toc;
   end
end
```

### Running the Job
To run the myParallelAlgorithmFcn in MATLAB, in the MATLAB Command Window, type:

:::{code-block} matlab
parpool(feature('numcores'))
[numWorkers,time] = myParallelAlgorithmFcn
:::

This specifies the number of cpus allocated in the MATLAB Open OnDemand to be utilized in the Parallel Toolbox and runs the function `myParallelAlgorithmFcn` and stores the outputs as `[numWorkers,time]`.

You can plot the performance (speedup) by typing:

:::{code-block} matlab
figure
speedup = time(1,:)./time;
plot(numWorkers,speedup);
legend('Problem complexity 1','Problem complexity 2','Problem complexity 3','Problem complexity 4','Location','northwest');
title('Speedup vs complexity');
xlabel('Number of workers');
xticks(numWorkers(2:end));
ylabel('Speedup');
:::