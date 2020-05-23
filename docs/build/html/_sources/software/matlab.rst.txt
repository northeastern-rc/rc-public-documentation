***********************************************
Working with MATLAB Parallel Computing Toolbox
***********************************************
The Discovery cluster has MATLAB Parallel Server installed. This topic page will detail how you
can setup and use MATLAB Parallel Computing Toolbox. This walkthrough uses MATLAB 2020a. There are
several parts to this walkthrough. We suggest that you read it through completely before starting.

This walkthrough will use Open onDemand, the web portal on Discovery, to launch MATLAB. You'll then create a
cluster profile. This allows you to define cluster properties that will be applied to your jobs. Supported
functions are *batch, parpool, and parcluster*. The Parallel Computing Toolbox comes with a cluster profile
called *local*, which you will change in the walkthrough below.

.. note::
   This walkthrough is for submitting jobs from Discovery, not using MATLAB on your local desktop or laptop.

Before starting, you should create a folder in your /scratch/<yourusername> directory. This
folder is where you'll save your job data.

1. Go to your /scratch directory: ``cd /scratch/<yourusername>`` where <yourusername> is your NU username
2. Make a new folder. We suggest calling it *matlab-metadata*: ``mkdir matlab-metadata``

**To start MATLAB and add a Cluster Profile, do the following:**

1. Go to http://ood.discovery.neu.edu. Sign in with your Discovery username and password if needed.
2. Click **Interactive Apps**, and select **MATLAB**.
3. Select **MATLAB version 2020a**, and keep the default time of 1 hour and default memory of 2GB. Click **Launch**.
4. If necessary, adjust the **Compression** and **Image Quality**, and then click **Launch MATLAB**.
5. On the MATLAB Home tab, in the **Environment** section, select **Parallel**, then click **Create and Manage Clusters**. This opens the Cluster Profile Manager window.
6. On the Cluster Profile Manager window, select **Add Cluster Profile**, then click **Slurm**. If prompted, click **OK** to the notice about needing Parallel Server.
7. Double click the new profile name in the Cluster Profile column, and type in the name Discovery. Press **Enter** to save the change.
8. Select **Edit** in the **Manage Profile** section. This lets you edit the options on the **Properties** tab. For this walkthrough, make the following edits:

  a. In the **Folder where job data is stored on the client** option, type ``/scratch/<yourusername>/matlab-metadata`` (this is the directory that you created in the first procedure above).
  b. In the **Numnber of workers available to cluster** option, type a number between 100 to 200. This field is the number of MPI processes you intend to run. This corresponds to the ``--ntasks`` Slurm option. The maximum is 1024 per job; however, for this task, we recommend keeping it lower and use threading inside the nodes.
  c. In the **Number of computational threads to use on each worker** option, type a number between 1 and 16. This field represents the number of threads that each worker will possess. This corresponds to ``cpus-per-task`` in Slurm. Do not exceed the number of available cores on the node.

9. When you have finished editing your properties, click **Done**.
10. (OPTIONAL) Click the Validate tab, ensure all of the stages are checked, then click Validate. This will check the properties of your profile.
11. (OPTIONAL) In the **Cluster Profile** column, right-click on the Discovery profile name and select **Set as Default**. This sets your profile as the default profile.

Now that you have set up your profile, you can use the default cluster profile you just created (*Discovery*) with the following commands::

     #with parpool
     parallel.defaultClusterProfile(‘Discovery’)
     parpool

     #with parcluster
     c = parcluster(‘Discovery’)

Using parcluster example
========================
This section will detail how to submit batch jobs to the cluster to perform scaling calculations for an integer factorization sample problem.
It is a computationally intensive problem, where the complexity of the factorization increases with the magnitude of the number. We will use the myParallelAlgorithmFcn.m MATLAB function.
This section assumes you have configured MATLAB Cluster Profile according to the procedure above.

On Discovery, there are benchmarking scripts and examples located in the ``/shared/centos7/matlab/R2020a/examples/parallel/main`` folder.
To add the path to this folder to the list of available paths, do one of the following:

* On the MATLAB Home tab, in the **Environment** section, click **Set Path** and add the path to the script.
* Alternatively, provide the full path of the script in the MATLAB command line.

The contents of myParallelAlgorithmFcn is as follows::

 function [numWorkers,time] = myParallelAlgorithmFcn ()

 complexities =  [2^18 2^20 2^21 2^22];
 numWorkers = [1 2 4 6 16 32 64];

 time = zeros(numel(numWorkers),numel(complexities));

 % To obtain obtain predictable sequences of composite numbers, fix the seed
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

**To submit myParallelAlgorithmFcn as a batch job, in the MATLAB Command Window, type**::

  totalNumberOfWorkers = 65;
  cluster = parcluster('Discovery');
  job = batch(cluster,'myParallelAlgorithmFcn',2,'Pool',totalNumberOfWorkers-1,'CurrentFolder','.');

This specifies the ``totalNumberOfWorkers`` as 65, where 64 workers will be issued to run *parfor* in parallel
(so the pool is set as 64), and the additional worker will run the main process.

To monitor the job after you submit it, click **Parallel**, then **Monitor Jobs** to open the Job Monitor.
You can view some job information, such as the state of the job (i.e. running, failed, finished etc.),
as well as the ability to fetch outputs if you right-click on the job line.

You can close MATLAB after you submit the job the scheduler. The job monitor tool will keep track of the jobs.

If you want to block MATLAB until the jobs are finished, type ``Wait(job)``.

When the jobs complete, you can transfer the outputs of the function using the ``fetchOutputs`` command::

 outputs = fetchOutputs(job);
 numWorkers = outputs{1};
 time = outputs{2};

You can plot the performance (speedup) by typing::

 figure
 speedup = time(1,:)./time;
 plot(numWorkers,speedup);
 legend('Problem complexity 1','Problem complexity 2','Problem complexity 3','Problem complexity 4','Location','northwest');
 title('Speedup vs complexity');
 xlabel('Number of workers');
 xticks(numWorkers(2:end));
 ylabel('Speedup');
