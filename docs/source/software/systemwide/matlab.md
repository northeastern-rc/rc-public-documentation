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

If you want to run an interactive pool job on the cluster we can use a `parpool` like above:

```{code-block} matlab
>> % Get a handle to the cluster
>> c = parcluster;

>> % Open a pool of 64 workers on the cluster
>> pool = c.parpool(64);
```

Instead of the open instance of MATLAB running this code, this will be run across the HPC cluster. Run the following code:

```{code-block} matlab
>> % Run a parfor over 1000 iterations
>> parfor idx = 1:1000
      a(idx) = rand;
   end
```

When you no longer need the pool, you can delete it and free up the resources with:

```{code-block} matlab
>> % Delete the pool
>> pool.delete
```

### Using the MATLAB with a batch job on the HPC cluster

You can use the `batch` command to submit passively running jobs to the HPC cluster from MATLAB. This command will return a job object that can be used to access the output of the submitted batch job. 

```{code-block} matlab
>> % Get a handle to the cluster
>> c = parcluster;

>> % Submit job to query where MATLAB is running on the cluster
>> job = c.batch(@pwd, 1, {}, 'CurrentFolder','.');

>> % Query job for state
>> job.State

>> % If state is finished, fetch the results
>> job.fetchOutputs{:}

>> % Delete the job after results are no longer needed
>> job.delete

```

To see the jobs that have been completed or still are running, you can call `parcluster` to return the cluster object that stores this information. Run the following command in the Command Window:

```{code-block} matlab
>> c = parcluster;
>> jobs = c.Jobs
>>
>> % Get a handle to the second job in the list
>> job2 = c.Jobs(2);
```

Once you locate the job, you can retrieve the results with `fetchOutputs` if you are using it interactively in the Command Window or you can use `load` if you are using it in a MATLAB script.

```{code-block} matlab
>> % Fetch all results from the second job in the list
>> job2.fetchOutputs{:}
```

### Parallel MATLAB Batch Job

The `batch` command can also submit parallel workflows to the HPC cluster. As an example, save the following code to a MATLAB script called `parallel_example.m.`

```{code-block} matlab
function [sim_t, A] = parallel_example(iter)
 
if nargin==0
    iter = 8;
end
 
disp('Start sim')
 
t0 = tic;
parfor idx = 1:iter
    A(idx) = idx;
    pause(2)
    idx
end
sim_t = toc(t0);
 
disp('Sim completed')
 
save RESULTS A
 
end
```

When you submit the job using the `batch` command, you will need to also specify the MATLAB Pool argument:

```{code-block} matlab
>> % Get a handle to the cluster
>> c = parcluster;

>> % Submit a batch pool job using 4 workers for 16 simulations
>> job = c.batch(@parallel_example, 1, {16}, 'Pool',4, ...
       'CurrentFolder','.');

>> % View current job status
>> job.State

>> % Fetch the results after a finished state is retrieved
>> job.fetchOutputs{:}
ans = 
   8.8872
```

This example took 8.89 seconds to run utilizing four workers. These jobs will always request N+1 number of CPUs for the task since 1 worker is required to manage the batch job and the pool of workers.

We can run the same simulation but increase the size of the Pool. We will retrieve the results later so we will keep the submitted job id as a reference.

```{note}

```

```{code-block} matlab 
>> % Get a handle to the cluster
>> c = parcluster;

>> % Submit a batch pool job using 8 workers for 16 simulations
>> job = c.batch(@parallel_example, 1, {16}, 'Pool',8, ...
       'CurrentFolder','.');

>> % Get the job ID
>> id = job.ID
id =
   4
>> % Clear job from workspace (as though MATLAB exited)
>> clear job
```

You need to get a handle of the cluster and then you can use the `findJob` method to obtain information about the job:

```{code-block} matlab
>> % Get a handle to the cluster
>> c = parcluster;

>> % Find the old job
>> job = c.findJob('ID', 4);

>> % Retrieve the state of the job
>> job.State
ans = 
finished
>> % Fetch the results
>> job.fetchOutputs{:};
ans = 
4.7270
```

This job ran for 4.73 seconds using 8 workers in MATLAB. You can run the code with different numbers of works to determine the ideal number of works for the job.

You can also use the MATLAB GUI to obtain the results from the job using the Job Monitor found in the Parallel dropdown in the Home tab and select Monitor Jobs.

:::{list-table}
---
header-rows: 1
---
* - Function
  - Description
  - Applies Only to Desktop
* - clusterFeatures
  - List of cluster features/constraints
  - 
* - clusterGpuCards
  - List of cluster GPU cards
  - 
* - clusterPartitionNames
  - List of cluster partition/queue names
  - 
* - disableArchiving
  - Modify file archiving to resolve file mirroring issue
  - true
* - fixConnection
  - Reestablish cluster connection (e.g., after reconnection of VPN)
  - true
* - willRun
  - Explain why job is queued
  - 
:::