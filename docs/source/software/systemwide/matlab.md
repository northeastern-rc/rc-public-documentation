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

The cluster has MATLAB Parallel Server installed. This section details an example of how you can set up and use the MATLAB Parallel Computing Toolbox. This walkthrough uses MATLAB 2023a launched as an interactive app on the Open OnDemand web portal. There are several parts to this walkthrough. We suggest that you read it through completely before starting. The parameters presented represent only one scenario.

This walkthrough will use Open OnDemand, the web portal on the cluster, to launch MATLAB. You will then use the default cluster profile.This allows you to utilize the resources that are allocated to your Open On Demand MATLAB job.

To start MATLAB and work with the Parallel Server, do the following:

1. Go to <http://ood.discovery.neu.edu>. If prompted, sign in with your cluster username and password.

1. Click **Interactive Apps**, and select **MATLAB**.

1. Select **MATLAB version 2023a**, and set the time for the length of your jobs, the number of cpus to be 1 plus the number you plan to use for the parallel toolbox work, and default memory to at least 2 times the number of cpus you request. Click **Launch**.

1. If necessary, adjust the **Compression** and **Image Quality**, and then click **Launch MATLAB**.

The following commands `parpool(feature('numcores'))` will start the Parallel Server with the number of cores that are allocated in the MATLAB Open OnDemand job (`feature('numcores')`). You can inspect the Parallel Server and the state of it with the command `parcluster`.

:::{code-block} matlab
#with parpool
parpool(feature('numcores'))

#with parcluster
parcluster
:::

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