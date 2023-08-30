(using-matlab)=
# Using MATLAB

::::{sidebar}
:::{seealso}
{ref}`using-module` and {ref}`using-ood`.
:::
::::
MATLAB is available on the cluster as a module and as an interactive app on Open OnDemand. You can also download MATLAB for your computer through the [Northeastern portal on the MATLAB website](https://www.mathworks.com/academia/tah-portal/northeastern-university-30294223.html). Note that the procedures detailed below pertain specifically to using MATLAB on Discovery, and not to using MATLAB on your computer.

## Installing MATLAB toolboxes

Use the following procedure if you need to install a MATLAB toolbox:

1. Download the toolbox from its source website.

1. Connect to Discovery.

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

The cluster has MATLAB Parallel Server installed. This section details an example of how you can set up and use the MATLAB Parallel Computing Toolbox. This walkthrough uses MATLAB 2020a launched as an interactive app on the Open OnDemand web portal. There are several parts to this walkthrough. We suggest that you read it through completely before starting. The parameters presented represent only one scenario.

This walkthrough will use Open OnDemand, the web portal on Discovery, to launch MATLAB. You will then create a
cluster profile. This allows you to define cluster properties that will be applied to your jobs. Supported
functions are `batch`, `parpool`, and `parcluster`. The Parallel Computing Toolbox comes with a cluster profile
called *local*, which you will change in the walkthrough below.

:::{note}
This walkthrough details submitting jobs through Discovery's Open OnDemand web portal. Some parameters will vary if you are using MATLAB from the command line. This walkthrough does not apply
to other versions of MATLAB.
:::

Before starting, create a folder in your `/scratch/<username>` directory. This folder is where you will save your job data.

1. Go to your `/scratch` directory: `cd /scratch/<username>` where `<username>` is your NU username

1. Make a new folder. We suggest calling it *matlab-metadata*: `mkdir matlab-metadata`

To start MATLAB and add a Cluster Profile, do the following:

1. Go to <http://ood.discovery.neu.edu>. If prompted, sign in with your Discovery username and password.

1. Click **Interactive Apps**, and select **MATLAB**.1. Select **MATLAB version 2020a**, and keep the default time of one hour and default memory of 2GB. Click **Launch**.

1. If necessary, adjust the **Compression** and **Image Quality**, and then click **Launch MATLAB**.

1. On the MATLAB Home tab, in the **Environment** section, select **Parallel**, then click **Create and Manage Clusters**. This opens the Cluster Profile Manager window.

1. On the Cluster Profile Manager window, select **Add Cluster Profile**, then click **Slurm**. If prompted, click **OK** on the notice about needing a Parallel Server.

1. Double-click the new profile name in the Cluster Profile column, and type a name such as **TestProfile**. Press **Enter** to save the change.

1. Select **Edit** in the **Manage Profile** section. This lets you edit the options on the **Properties** tab. For this walkthrough, make the following edits:

   1. In the **Folder where job data is stored on the client** option, type `/scratch/<yourusername>/matlab-metadata` (this is the directory that you created in the first procedure above).
   1. In the **Number of workers available to cluster** option, type a number between between 1 and 10. This field is the number of MPI processes you intend to run. This corresponds to the `--ntasks` Slurm option. The maximum is 128 per job; however, for this task, we recommend keeping it lower and use threading inside the nodes. The number you set here will be the default maximum for the job. You can set it for less than or equal to this number in the MATLAB Command Window when submitting your job.
   1. In the **Number of computational threads to use on each worker** option, type a number between 1 and 10. This field represents the number of threads that each worker will possess. This corresponds to `cpus-per-task` in Slurm. Do not exceed the number of available cores on the node.

9. When you have finished editing your properties, click **Done**.
1. (Optional) If you want to validate your setup, click the **Validation** tab (next to the Properties tab). Ensure all the stages are checked, then click the **Validate** button at the bottom of the page.

This will check the properties of your profile. You might need to wait a minute or two for this to complete.

:::{caution}
Do not click the green **Validate** button. This will attempt validation using the maximum number of workers, which can cause the validation to hang or fail. If you accidentally click the green Validate button, click **Stop** to end the validation process.
:::

(OPTIONAL) In the **Cluster Profile** column, right-click on the TestProfile name and select **Set as Default**. This sets your profile to be the default.

Now that you have set up your profile, you can use the default cluster profile you just created (*TestProfile*) with the following commands:

:::{code-block} matlab
#with parpool
parallel.defaultClusterProfile(‘TestProfile’)
parpool

#with parcluster
c = parcluster(‘TestProfile’)
:::

### Using parcluster example
This section provides instructions for submitting batch jobs to the cluster for scaling calculations on an integer factorization sample problem. The complexity of this problem increases with the magnitude of the number, making it computationally intensive. To perform these calculations, we will use the `myParallelAlgorithmFcn.m` MATLAB function. Please note that this section assumes you have already configured a MATLAB Cluster Profile per the procedure above.

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

### Submit Batch Job
To submit myParallelAlgorithmFcn as a batch job, in the MATLAB Command Window, type:

:::{code-block} matlab
totalNumberOfWorkers = 65;
cluster = parcluster('TestProfile');
job = batch(cluster,'myParallelAlgorithmFcn',2,'Pool',totalNumberOfWorkers-1,'CurrentFolder','.');
:::

This specifies the **`totalNumberOfWorkers`** as 65, where 64 workers will be used to run **`parfor`** in parallel (so the pool is set to 64), and the additional worker will run the main process.

To monitor the job after submitting it, click on **`Parallel`**, then **`Monitor Jobs`** to open the Job Monitor. Here, you can view job information, such as the job state (i.e., running, failed, finished, etc.), and fetch outputs by right-clicking on the job line.

You can close MATLAB after submitting the job to the scheduler. The job monitor tool will continue to track the jobs.

If you want to block MATLAB until the jobs are finished, type **`Wait(job)`**.

Once the jobs are complete, you can transfer the function outputs using the **`fetchOutputs`** command.

:::{code} matlab
outputs = fetchOutputs(job);
numWorkers = outputs{1};
time = outputs{2};
:::

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
