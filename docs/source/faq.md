(faq)=
# Frequently Asked Questions (FAQs)
Below are some common questions and answers regarding our HPC cluster and its operation.
```{dropdown}
:open:

Drop-down the item to see solution.
```
## Cluster Details
::::{dropdown} What hardware is in the cluster?
The cluster compute and storage capabilities are changing on a regular basis.

:::{seealso}
{ref}`hardware-overview` for detailed information on the HPCs hardware components, along with the {ref}`partitions <partition-names>` comprising subsets of these components.
:::
::::

::::{dropdown} What is a cluster?
A {term}`cluster` is a network of interconnected computers designed to work together as a unified and robust system. These computers, also known as {term}`nodes <node>`, collaborate to collectively handle complex computational tasks more efficiently than a single machine could achieve. By distributing workloads across multiple nodes, a cluster harnesses {term}`parallel computing` capabilities, enabling researchers and professionals to solve intricate problems, analyze large datasets, and perform simulations with incredible speed and precision. Clusters are widely used in {term}`high-performance computing (HPC)` environments, scientific research, data analysis, and other fields that demand significant computing resources.
::::

::::{dropdown} What is the policy on fair use of resources?
The {term}`fair use policy <fair share allocation>` for computing resources aims to provide equitable access and distribution within the {term}`cluster`. This policy ensures that all users have an equal opportunity to utilize the cluster resources based on their needs and priorities.

Fair use policies typically utilize a {term}`scheduler` that allocates resources to jobs based on {term}`job priority`, resource requirements, and historical resource usage. This approach prevents any single user or job type from monopolizing the resources and ensures a balanced and efficient allocation of resources across different users and projects.

This policy promotes fairness and efficient resource utilization and contributes to an inclusive and productive computing environment for all users.
:::{seealso}
{ref}`Our page on the Queuing System<introduction-to-queuing-systems>` and {ref}`job-scheduling`.
:::
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Accounts
::::{dropdown} How do I get an account for the HPC cluster?
{ref}`See Request An Account <request-an-account>`, and complete the [ServiceNow RC Access Request form] with your details and submit it. Your request will be processed within a few business days.
::::

::::{dropdown} How can I reset my password?
Please use our website's 'Account Management' tool for password reset. Follow the instructions to reset your password.

:::{seealso}
{ref}`changing-password`.
:::
::::

::::{dropdown} What happens to my account when I leave NU?
ITS controls access to the University’s computing resources, so when you or your students leave, you/they may lose access to many of these resources. Sponsored accounts allow people who work or volunteer at NU, but who are not paid by NU, to access the University’s computing resources. Researchers with sponsored accounts cannot request RC services, but they are allowed to use the systems we manage as members of a MyGroups (requires VPN connection) group controlled by a NU Principal Investigator (PI). Details on sponsored accounts are posted on the ITS sponsored accounts page.
::::

::::{dropdown} How do I get access?
The HPC resources are available to Northeastern University research faculty, and classes that require high-performance computing for their coursework, and students. For detailed information about reporting requirements and any access restrictions, please refer to our {ref}`getting-access` page. If you have questions about our access policy or procedures, please contact RC.

::::

::::{dropdown} What is my cluster username?
Your cluster username is the same as your NU username. If you do not have a cluster account, your NU username is usually your last name, period, and then the first letter of your first name plus your last name (for staff, first letter of first name, period, then followed by lastname). If you're unsure, please contact RC.

Your cluster username is the same as your NU username. Your NU username is the same as your email address without @northeastern.edu. If you're unsure, please contact RC.

:::{seealso}
{ref}`request-an-account`
:::
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## General Usage
::::{dropdown} How do I gain access to the cluster?
A faculty or research staff member must sponsor your HPC account request. Faculty and staff can self sponsor. Full details can be found here.
:::{seealso}
{ref}`getting-access`
:::
::::

::::{dropdown} How do I log on to the cluster?
Use an SSH client and connect to `login.discovery.neu.edu`. Instructions for using ssh and other login tools, as well as recommended clients for different operating systems, as described in {ref}`shell-environment-on-cluster`. You can also access the cluster through our Web-based interface {term}`Open OnDemand (OOD)`. {ref}`Learn more about acessing OOD <access-ood>`.
:::{seealso}
{ref}`connect-to-cluster`.
:::
::::

::::{dropdown} Where can I find a list of Linux commands?
We provide a cheat sheet of useful Linux ({ref}`command-line`) and Slurm commands ({ref}`using-slurm`) and there are more resources you can find online.
::::

::::{dropdown} How do I reset my password?
Access to the HPC cluster requires a valid Northeastern University email account. Your HPC password is the same as your Northeastern University account password so in order to reset it, reset your Northeastern University account password.
:::{seealso}
Find KB article
:::
::::

::::{dropdown} How can I view .pdf or .csv files on the cluster?
You can view .pdf and .csv files utilizing the File Explorer application on Open OnDemand and the Open OnDemand Desktop Application.
:::{seealso}
{ref}`file-explorer` and {ref}`desktop-app`
:::
::::

::::{dropdown} How do I request all CPUs on a node with more than one GPU?
You may wish to request a single GPU on a node and all of the node's CPUs. However, the GPUs are bound to specific CPUs so the job will only run on the CPUs associated with the GPU you're running on. Specifying the --exclusive flag in your job script or requesting all of the node's CPUs will not change this. If you would like to use all cores on a node with one of the GPUs, you must specify this in your Slurm script: #SBATCH --gres-flags=disable-binding

Refer to the Slurm documentation for further information.
::::

::::{dropdown} How can I get information on the HPC such as how busy it is?
From a login node, you can run `sinfo -p short` to get the state of the HPC.
:::{seealso}
{ref}`slurm-monitoring-and-managing`
:::
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Data Transfer

::::{dropdown} How can I transfer data to/from the HPC cluster?
Data transfer can be done using various methods like `scp`, `rsync`, or `Globus`. Refer to the 'Transferring Data' section in 'Data Management' for detailed instructions.
:::{seealso}
{ref}`data-storage-index`
:::
::::

::::{dropdown} What Linux commands can I use to transfer files to/from the cluster?
Smaller files can be transferred to/from the cluster using `scp`, `sftp`, and `rsync` as well as standard FTP tools utilizing `xfer.discovery.neu.edu`.

Larger files should be moved using Globus.
:::{seealso}
{ref}`data-storage-index`
:::
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Job Management
::::{dropdown} How do I submit jobs?
You submit jobs by writing a Slurm script and submitting it with the sbatch command. Please see our Slurm documentation page.
:::{seealso}
{ref}`using-sbatch`
:::
::::

::::{dropdown} How do I submit an interactive job?
For an interactive job on the command line, submit an `srun` job from the login node. Examples can be seen at {ref}`using-srun`

If you wish to run a program that requires a graphical user interface or generates other graphics for display, such as a plot or chemical model, use one of the Open OnDemand interactive apps. Several are available, but if you one you wish to use isn’t in the list, submit an OOD Desktop job. You can also use X11 forwarding with `srun`.
:::{seealso}
{ref}`using-ood`
:::
::::

::::{dropdown} What partitions can I use?
All account holders have access to the `short`, `debug`, `express`, and `gpu` partitions. For more information please see {ref}`partition-names`.
::::

::::{dropdown} How do I choose which partition to use?
Partitions are set up to emphasize run time limits and different resource limits and specialty hardware including GPUs. More information about partitions can be found at {ref}`partition-names`.
::::

::::{dropdown} How do I check the status of my jobs?
Run the command `squeue -u $USER` from the login node.

If reporting a problem to us about a particular job, please let us know the JobID for the job that you are having a problem with. You can also run `squeue -u $USER` to obtain the JobID.
::::

::::{dropdown} Why is my job not starting?
Several things can cause jobs to wait in the queue. If you request a resource combination we do not have available at the moment the job will be marked pending (PD). You may also have run a large number of jobs in the recent past and the “fair share” algorithm is allowing other users higher priority. Finally, the queue you requested may simply be very busy. If your job is pending there will be another field with the reason; if it is Resources that means that the resource you requested isn’t available, either because it is busy or because you requested a nonexistent resource. If the reason is “Priority” it means that a job with higher priority than yours is running. Your job will rise in priority as it waits, so it will start eventually. To request an estimate from the queueing system of your start time, run `squeue -u $USER --start`.
::::

::::{dropdown} How can I check when my job will start?
Run
:::{code} bash
squeue -j <jobid> --start
:::
Slurm will provide an estimate of the day and time your job will start.
::::

::::{dropdown} Why was my job killed?
Usually this is because you inadvertently submitted the job to run in a location that the compute nodes can’t access or is temporarily unavailable. If your jobs exit immediately this is usually why. Other common reasons include using too much memory, too many cores, or running past a job’s timelimit.

You can run `sacct`:

:::{code} bash
[user@login-00 ~] sacct
       JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
159637       ompi_char+   parallel  hpc_admin         80  COMPLETED      0:0
159637.batch      batch             hpc_admin          1  COMPLETED      0:0
159637.0          orted             hpc_admin          3  COMPLETED      0:0
159638       ompi_char+   parallel  hpc_admin        400    TIMEOUT      0:1
159638.batch      batch             hpc_admin          1  CANCELLED     0:15
159638.0          orted             hpc_admin         19  CANCELLED  255:126
:::

If it’s still not clear why your job was killed, please contact us and send us the output from `sacct`.
::::

::::{dropdown} How can I submit a job to the HPC cluster?
Jobs can be submitted with `sbatch` and `srun` to the HPC.
:::{seealso}
{ref}`using-sbatch` and {ref}`using-srun`
:::
::::

::::{dropdown} How can I check the status of my job?
You can check the status of your job using the `squeue -u $USER` command, which will display your current jobs in the queue.
:::{seealso}
{ref}`job-management`
:::
::::

::::{dropdown} What should I do if my job fails?
Check the output and error files for any error messages if your job fails. These files are usually located in your job's working directory. If you cannot resolve the issue yourself, contact Research Computing with the details of the error message.
::::

::::{dropdown} When will my job start?
You can list information on your job’s start time using the `squeue`git  command:

:::{code} bash
squeue -u $USER --start
:::
Note that Slurm’s estimated start time can be a bit inaccurate. This is because Slurm calculates this estimation off the jobs that are currently running or queued in the system. Any job that is submitted after yours with a higher priority may delay your job. Alternatively, if jobs complete in less time than they've requested, more jobs can start sooner than anticipated.

For more information on the `squeue` command, take a look at our {ref}`job-management`
::::

::::{dropdown} How do I check the efficiency of my completed jobs?
Run the command seff on the Slurm job ID:

:::{code} bash
[user@login-00 ~] seff 38391902
Job ID: 38391902
Cluster: discovery
User/Group: user/users
State: COMPLETED (exit code 0)
Cores: 1
CPU Utilized: 00:00:00
CPU Efficiency: 0.00% of 00:03:25 core-walltime
Job Wall-clock time: 00:03:25
Memory Utilized: 652.00 KB
Memory Efficiency: 0.03% of 1.95 GB
:::
::::

::::{dropdown} What is a batch system? / What is a job scheduler?
The purpose of a **batch system** is to execute a series of tasks in a computer program without user intervention (non-interactive jobs). The operation of each program is defined by a set or **batch** of inputs, submitted by users to the system as “job scripts.”

When job scripts are submitted to the system, the **job scheduler** determines how each job is queued. If there are no queued jobs of higher priority, the submitted job will run once the necessary compute resources become available.
::::

::::{dropdown} What are the differences between batch jobs, interactive jobs, and GUI jobs?
A **batch job** is submitted to the batch system via a job script passed to the `sbatch` command. Once queued, a batch job will run on resources chosen by the scheduler. When a batch job runs, a user cannot interact with it.

- View a walk-through of an example batch job script
An **interactive job** is any process that is run at the command line prompt, generally used for developing code or testing job scripts. Interactive jobs should only be run in an interactive session, which are requested through the `srun` command. As soon as the necessary compute resources are available, the job scheduler will start the interactive session.

- View the Interactive Development & Testing documentation page
A **GUI job** uses the cluster compute resources to run an application, but displays the application’s graphical user interface (GUI) to the local client computer. GUI sessions are also managed by the job scheduler, but require additional software to be installed on the client side computer or ran through Open OnDemand.
::::

::::{dropdown} How do I submit a job to the batch system?
The primary job submission mechanism is via the `sbatch` command via the Linux command line interface
:::{code} bash
$ sbatch <your_job_script>
:::
where <your_job_script> is a file containing the commands that the batch system will execute on your behalf. 
:::{seealso}
{ref}`using-sbatch`
:::
::::

::::{dropdown} How do I run applications that use multiple processors (i.e. parallel computing)?
Parallel computing refers to the use of multiple processors to run multiple computational tasks simultaneously. Communications between tasks use one of the following interfaces, depending on the task:

- OpenMP – used for communication between tasks running concurrently on the same node with access to shared memory
- MPI (eg OpenMPI) – used for communication between tasks which use distributed memory
- Hybrid – a combination of both OpenMP and MPI interfaces

You must properly configure your job script in order to run an application that uses multiple processors. View sample SLURM scripts for each case below:
::::

::::{dropdown} Why do I get the error 'slurmstepd: Exceeded job memory limit at some point'?
Sometimes, SLURM will log the error slurmstepd: Exceeded job memory limit at some point. This appears to be due to memory used for cache and page files triggering the warning. The process that enforces the job memory limits does not kill the job, but the warning is logged. The warning can be safely ignored. If your job truly does exceed the memory request, the error message will look like:

:::{code} bash
slurmstepd: Job 5019 exceeded memory limit (1292 > 1024), being killed
slurmstepd: Exceeded job memory limit
slurmstepd: *** JOB 5019 ON dev1 CANCELLED AT 2016-05-16T15:33:27 ***
:::
::::

::::{dropdown} How do I check the my job status?
You can use the following command to check the status of the jobs you’ve submitted:

:::{code} bash
$ squeue -u <user_name>
:::

To check the status of jobs running under a particular group, modify the command with the -A flag:
:::{code} bash
$ squeue -A <group_name>
:::
To also return QoS information for jobs under a particular group, use the following command:
:::{code} bash
$ squeue -O jobarrayid,qos,name,username,timelimit,numcpus,reasonlist -A <group_name>
:::
::::

::::{dropdown} How do I delete a job from the batch system?
You can use the command
:::{code} bash
$ scancel <job_id>
:::
to delete jobs from the queue. You can only delete jobs that you submitted.
::::

::::{dropdown} What are the wall time limits for a partition?
You can check the wall time limits, denoted as TIMELIMIT, for a partition with the following command replacing $PARTITION with the partition of interest
:::{code} bash
$ sinfo -p $PARTITION
:::
::::

::::{dropdown} How can I check how busy a partition is?
Use the following command to view how busy the partition is
:::{code} bash
$ sinfo -p $PARTITION
:::
and view the STATE column to see how many nodes are 'idle' (no jobs running on them).
::::

::::{dropdown} How can I use GPUs for my job?
To use GPUs for your job, you need to request them in your job script. You can find more information in the 'Working with GPUs' section.
:::{seealso}
{ref}`working-gpus`
:::
::::

::::{dropdown} How do I login to the compute node my job is running on?
You will only be able to login to compute nodes that your jobs are running on. If the job is running on one node use:
:::{code} bash
srun --jobid=jobid --pty /bin/bash
:::
where you can find your jobid by running
:::{code} bash
squeue -u $USER
:::
If the job is running on more than one node, specify the node you want to login to:
:::{code} bash
srun --jobid=jobid --nodelist=node_name -N1 --pty /bin/bash
:::
If your job is allocated all of the resources on the node, you will need to include the --overlap option.
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Storage

::::{dropdown} What are the data storage options?
Several data storage options are available depending on your needs, such as `/home`, project directories (`/work/$PROJECT`), and temporary storage (`/scratch`). Details can be found in the 'Data Management' section.
:::{seealso}
{ref}`data-storage`
:::
::::

:::{dropdown} What types of storage are available and how should each type be used?

:::

:::{dropdown} Can my `/work` storage quota be increased?
You can request a quota increase by submitting a [Storage Space Extension Request](https://bit.ly/NURC-StorageExtension)
:::

::::{dropdown} Why can't I run jobs in my home directory?
`/home/$USER` directories are intended for relatively small amounts of human-readable data such as text files, shell scripts, and source code. All research work should be stored at `/work/$PROJECT` for long term storage and `/scratch/$USER` should be used for temporary job storage during run time. Be mindful of `/scratch/$USER` purge policy.
:::{seealso}
{ref}`data-storage`
:::
::::

::::{dropdown} Why should I use `/scratch` storage?
Scratch storage is fast and provides a large quantity of free space for temporary jobs files. However, there are limits on the number of files and the amount of space you may use and there is a time based purge policy that is implimented. Please review our scratch filesystem policy for details.
:::{seealso}
{ref}`data-storage`
:::
::::

::::{dropdown} How do I check my `/home/$USER` disk usage?
Run `du -shc .[^.]* * /home/$USER` which will output:
:::{code-block} shell
[<username>@<host> ~]$  du -shc .[^.]* * /home/$USER/
39M     .git
106M    discovery-examples
41K     README.md
3.3M    software-installation
147M    total
:::
::::

::::{dropdown} How long can I store files in /scratch?
`/scratch` is designed to serve as fast, temporary storage for running jobs, and is not long-term storage. For this reason, files are periodically marked for deletion from all `/scratch` directories. Please review the `/scratch` filesystem policy for more details. Store longer-term files in your `/work/$PROJECT` directory. 
:::{seealso}
{ref}`data-storage`
:::
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Software
::::{dropdown} What software applications are available?
The full list of applications installed on the cluster is available by using the `module avail` command from the terminal on the HPC.
:::{seealso}
{ref}`using-module`
:::
::::

::::{dropdown} May I submit an installation request for an application?
You can submit a [Software Installation Request](https://bit.ly/NURC-Software) ticket to the Research Computing team. 

You can also try and install your program locally with package mangers or compiling from source by following our documentation pages.
:::{seealso}
{ref}`package-managers` and {ref}`from-source`
:::
::::

::::{dropdown} Can I install my software on the HPC cluster?
Yes, you can. Please follow the guidelines in the {ref}`package-managers` and {ref}`from-source` sections. If you encounter any issues, contact Research Computing.
::::

:::{dropdown} How do I use research software that’s already installed?
We use the `modules` system for managing software environments. Learn more about how to use `modules` from {ref}`using-modules`.
::::

::::{dropdown} Can I run this Docker container on the cluster?
We do not run Docker on the cluster due to security issues. Instead, we use Singularity. Singularity can run Docker images directly, or you can convert a Docker image to a Singularity image (.sif). To import existing Docker images, use the singularity pull command.

:::{code} bash
module load singularity
singularity pull docker://<container repository URL path>
:::
::::

::::{dropdown} Can I run application/container X on a GPU?
Please check the documentation for your application/container before running on a GPU. The developer of the program/container will outline GPU support and commands for the program.
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Classroom (course specific)

::::{dropdown} How can I get my class access to the HPC?
Please submit a [Classroom Access Request]() ticket in order for a classroom to get a access.
:::{seealso}
{ref}`classroom-faq-index`
:::
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Development
::::{dropdown} How do I develop and test software?
Use compute nodes for software development and testing. Connect to the cluster and use the following command to start a developmental session:

:::{code} bash
$ module load ufrc
$ srundev
:::

The srundev command can be modified to request additional time, processors, or memory, which have defaults of 10 minutes, 1 core, and 2GB memory, respectively. For example, to request a 60-minute session with 4 cores and 4GB memory, use:

:::{code} bash
$ module load ufrc
$ srundev --time=60 --cpus-per-task=4 --mem-per-cpu=4gb
:::

Generally speaking, we use modules to manage our software environment including our PATH and LD_LIBRARY_PATH environment variables. To use any available software package that is not part of the default environment, including compilers, you must load the associated modules. For example, to use the Intel compilers and link against the fftw3 libraries you would first run:

:::{code} bash
$ module load intel
$ module load fftw
:::

Which may be collapsed to the single command:

:::{code} bash
$ module load intel fftw
:::
::::

::::{dropdown} What compilers are available?
We have two compiler suites, the GNU Compiler Collection (GCC) and the Intel Compiler Suite (Composer XE). The default environment provides access to the GNU Compiler collection while the Composer XE may be accessed by loading the intel module (preferably, the latest version).
::::

::::{dropdown} I need to push and commit code changes from the cluster account to my GitHub account. How do I set that up?
You must first generate an ssh key and then copy it to your git repository. Here are the instructions for generating the ssh key and what to do on your git page:

To generate an ssh key, see the following link: ssh key generation

- Click on the drop-down menu next to my Git profile picture in the upper right corner; Select Settings; Click on SSH and GPG keys in the left column;
- - Click on the New SSH Key button and followed the directions to upload your ssh key.
- Make sure that the ssh key is in your authorized_keys file in your .ssh directory on the cluster.

The next step is to clone the repository using the ssh link. If you have already cloned the repository using the http link and made a number of changes to your files, you won’t want to redo them. Rename the directory that was created when you first cloned the repository. Then, re-clone the repository using the ssh link and copy all the files you had changed to the new directory. Finally, push those changes back to the repository.
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Open OnDemand
::::{dropdown} Why do I see a blank window when starting an OnDemand desktop?
Occasionally, when users try to start an interactive session in OnDemand, the desktop displays as a blank blue or grey window with no applications menu or way to open a terminal window. Files get cached when sessions are opened and then either get corrupted or can't be used. To fix this problem, delete the following hidden subdirectories in your home directory and start a new OnDemand desktop session:

:::{code} bash
rm -rf ~/.vnc
rm -rf ~/.cache
rm -rf ~/.config/xfce4
:::
::::

::::{dropdown} How can I access my project directory from a JupyterLab?
Create a symbolic link in your home or work directory that points to your project directory. Then you'll be able to navigate through the symbolic link in the Jupyter Notebook. To create a symbolic link in your home directory called 'projects' run the `ln -s` command, replacing the full path of your project directory and your username in the example below:
:::{code}
ln -s /work/<group_name> $HOME/projects
:::
You'll then have the link `$HOME/projects` that takes you to your project directory.
::::

::::{dropdown} How can I fix the XFCE PolicyKit Agent error in OnDemand desktop sessions?
If you see an error box that says XFCE PolicyKit Agent you can click the Close button and proceed with using the OnDemand desktop.
::::

::::{dropdown} Why does my OnDemand desktop or app show it's starting but then it immediately ends?
There are two common reasons why you might not be able to launch OnDemand sessions including interactive desktops and apps like Jupyter Notebook and Matlab.

You are over quota in your home directory. See more on managing OnDemand job data
You have an Anaconda environment loading in your .bashrc environment file or are loading a Python module in your .bashrc file that is interfering with the OnDemand desktop setup. See also
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Applications
### MATLAB
:::{dropdown} How do I run MATLAB programs?
You may use the interactive MATLAB interpreter on the test nodes. However, in order to run MATLAB programs through the batch system, you must compile your MATLAB source code into a standalone executable. This is required because there are not enough MATLAB licenses available to run the programs directly. To learn how to compile your MATLAB program please see our MATLAB wiki page.
::::

::::{dropdown} How do I compile a MATLAB program?
Generally speaking, you will load the MATLAB module and then use the MATLAB compiler, mcc, to compile your MATLAB program(s). See our MATLAB wiki page for more detailed instructions.
::::

::::{dropdown} Why can't I check out a MATLAB compiler license?
If you tried to use the MATLAB compiler, mcc, and received the message “Could not check out a compiler license” it is because Research Computing does not have its own MATLAB licenses but relies on the UF campus license. There are a limited number of MATLAB compiler licenses shared by the whole campus. When the license is checked out during an interactive MATLAB session, it does not get checked back in until the MATLAB session is terminated, which could take a long time depending on what the user is doing. Unfortunately, you will not be able to run mcc until a license becomes available.
::::

### VSCode
### Stata

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Common Errors and Issues
::::{dropdown} Why can't I log in?
This is a very generic question that is difficult for us to answer. CCR supports many services. If you were to ask this question in a help ticket we would respond with: What are you trying to login to? Are you getting any error messages? So we'll provide links here to the primary services CCR users login to and the corresponding documentation:

OnDemand
HPC clusters command line SSH or SFTP logins
Lake Effect Research Cloud Horizon Dashboard
Common errors:

SSH error "no supported authentication methods available": SSH keys are required for command line SSH and SFTP access to CCR's login nodes. Password logins are not accepted. Please see more info here
SSH error "Permission denied (publickey)": You either do not have your SSH public key uploaded to your CCR account (see error above) or you are not specifying the private key on your personal device when trying to login to CCR. See this page for more info
Missing home directory: Your account hasn't been provisioned yet. See here for more info
Password expired: Reset your password using the identity management portal. instructions can be found here
Invalid credentials: This means either your password, one time token, or both were entered incorrectly.
Access denied, or You don't have access to this resource: If receiving this when attempting to login to ColdFront or OnDemand, this means you do not have two-factor authentication enabled. 2FA is required. Follow these instructions to enable it.
Bad request or Server not available when trying to log in to OnDemand: These are often caused by corrupted cache files in our browser. Clear your browser cache and cookies data and restart your browser or try a different browser. Incognito windows often do not solve this problem.
::::

::::{dropdown} Why can I log in to the help portal but not my NU account?
The Freshdesk help desk portal accounts are separate from our NU system accounts. This allows people who do not yet have a NU account to request help from NU staff. For more info on CCR accounts, see our Getting Access page. For more info on the help desk portal, see here.
::::

::::{dropdown} Why does my application keep getting killed on the login nodes?
Login nodes have a 15-minute time limit on running processes and are not intended for running applications. Please submit a job to the cluster for running or debugging applications or use a compile node for installing software.
::::

::::{dropdown} Why do I get "Fatal system error" or "Account already exists" error when creating a new account?
When trying to create a new CCR account, you get an error that says "fatal system error" or "account with this username already exists" please contact CCR help. Staff will need to take manual action to rectify the problem.
::::

::::{dropdown} Why am I getting 'no space left on device' errors?
If you're sure you're not over quota in either file size or number of files, it may be an issue with file permissions. In the shared project and Panasas scratch directories, users must ensure the group ownership of a file or directory is set to the faculty or project group of that directory. This is set automatically for new files and when copying files. However, sometimes users override these defaults. If you get this error, this is definitely the problem:

:::{code} bash
mv: failed to preserve ownership for 'filename': no space left on device
:::

Other possible reasons for this error:
:::{code} bash
Moving Files: If you are trying to move a file from another location, change the group ownership of the file before moving it or use the copy command instead.
:::
- **Editing or Creating New Files**: If you get this error when trying to edit an existing file or trying to create a new one, it is because the 'sticky bit' is not set correctly on the subdirectory you are trying to write in. You must add the sticky bit to the group permissions on the subdirectory to fix this: chmod g+s directory_name NOTE: You will NOT have to do this if you do not alter the default permissions within the project or scratch directory. This is only if you copy over subdirectories that do not have this set or accidentally change the permissions and want to set them back.
- **Compiling Code**: It could be that your permissions are correct but the code you're compiling is using your primary unix group when creating new files. When running make install you may see an error like file INSTALL cannot copy file or when trying to install a conda package you may see An error occurred while installing package 'None'. OSError(28, 'No space left on device' As a workaround, switch to your research group unix group using the command newgrp group-name and then proceed with the installation.
::::

::::{dropdown} How can I see what the file permissions are?
The `getfacl` command is an easy way to see the permissions of a file or directory. It will display the file/directory name, owner of the file/directory, group name that owns the file/directory, and the detailed permissions of the file/directory. See also: `man getfacl` or `getfacl --help`
::::

::::{dropdown} Why am I see the error "kinit: Unknown credential cache type while getting default ccache" when using ccrkinit?
This error is caused by Anaconda conflicting with the Kerberos used by CCR's authentication system. Some users load Anaconda environments or personal/group Python or Anaconda modules in their .bashrc file (found in your home directory). These environments break Kerberos (and also OnDemand desktops and apps!) so we do not recommend loading them in the .bashrc file.
::::


::::{dropdown} Why am I getting "error while loading shared libraries" when trying to install Anaconda?
During installation, you may see an error such as "conda.exe: error while loading shared libraries: libz.so.1: failed to map segment from shared object: Operation not permitted"

This relates to an issue storing temporary files created during installation. Please create a temporary directory within your project or Panasas scratch directory and specify that location in the installation command. For example:

:::{code} bash
mkdir /projects/academic/<group_name>/condatemp
TMPDIR=/projects/academic/<group_name>/condatemp ./Anaconda3-2020.02-Linux-x86_64.sh --prefix=/projects/academic/<group_name>/<install_dir>
:::
::::

::::{dropdown} Why is my job pending with reason `ReqNodeNotAvail`?
The `ReqNodeNotAvail` message usually means that your node has been reserved for maintenance during the period you have requested within your job script. This message often occurs in the days leading up to our regularly scheduled maintenance, which is performed the last Tuesday of every month (unless otherwise noted on our downtime schedule). For example, if you run a job with a 72-hour wall clock request on the last Tuesday of the month, you will see the ReqNodeNotAvail status because the node is reserved for maintenance within that 72-hour window. You can confirm whether the requested node has a reservation by typing `scontrol` show reservation to list all active reservations.

If you receive this message, the following solutions are available:

1. Submit a job requesting less time so that it does not intersect with the maintenance window.
-OR-
2. Wait until after the maintenance window has finished and your job will resume automatically when there are resources available.

If this message is not due to an upcoming maintenance downtime, then it means that whatever type of node or feature you requested is not available in the partition you submitted your job to run on. Users will see this more frequently as CCR moves nodes from the UB-HPC cluster over to the new environment. These nodes are being reinstalled and are only available in the ubhpc-future reservation. This reservation is available to all UB-HPC cluster users, however, it must be specified in your job script, `salloc` request, or by using OnDemand 3. For more info, see HERE
::::

::::{dropdown} How do I fix `sbatch: error: Batch script contains DOS line breaks`?
If you receive an error message like this when trying to submit a job, it is because your batch script was edited in a Windows editor, not a unix editor. Windows editors can add line breaks that the unix interpreter doesn't recognize. You may receive an error such as:

:::{code} bash
sbatch: error: Batch script contains DOS line breaks (\r\n)
sbatch: error: instead of expected UNIX line breaks (\n).
:::

Run the `dos2unix` command on your file to remove the Windows line breaks. For example: `dos2unix myBatchFile`.
Use the `man` command to see all the options for the `dos2unix` command: `man dos2unix`.
::::

::::{dropdown} Why do I get an ‘Invalid Account, Partition, or QOS Specification’ error when I try to run a job?
If you're getting errors like these, you're not specifying the right combination of cluster, account, partition, and qos based on what your account has access to:

:::{code} bash
salloc: error: Job submit/allocate failed: Invalid qos specification
salloc: error: Job submit/allocate failed: Invalid account or account/partition combination specified
sbatch: error: Batch job submission failed: Invalid partition or qos specification
:::

CCR uses Quality of Service (QOS) to restrict access to partitions and to provide research groups that support CCR financially with a boost in their job priorities. Slurm will use your default account, unless you specify differently in your job script or when starting an OnDemand app. Use the slimits command to see what accounts and QOS settings you have access to. This is managed in ColdFront under allocations. More details on QOS and partition limits can be found here. Information on becoming a CCR supporter can be found on our website.
::::

::::{dropdown} Why am I getting a `QOSMaxSubmitJobPerUserLimit` error when I try to submit a job?
You may see this error when submitting batch scripts or when attempting to launch apps in OnDemand:

:::{code} text
sbatch: error: QOSMaxSubmitJobPerUserLimit
sbatch: error: Batch job submission failed: Job violates accounting/QOS policy (job submit limit, user's size and/or time limits)
:::

You will get this error if you have reached the partition or per user limits as described here. For example, if you have 1000 jobs in the general-compute partition and try to submit another one, you will get this error. If you've already launched one viz desktop, you've reached your limit. Wait for some of your jobs to finish and submit more at that time.
::::

::::{dropdown} Why does my SSH session automatically disconnect?
SSH connections will time out either due to inactivity or network disruptions. If your sessions are disconnecting due to inactivity, one thing you can do to keep the SSH connection open is to have ssh send a periodic keep alive packet to the server so it will not timeout. Add the -o ServerAliveInterval=600 option to your ssh login command. SSH can be sensitive to any disruptions in the network which can be common with Wi-Fi networks. Sometimes the 'keep alive' setting prevents this. Other times, it may be that you have a setting on your Wi-Fi or ethernet adapter that tells the operating system it can put the device to sleep after a period of inactivity. This is especially common on Windows. Check your network adapters for 'Power Settings' and uncheck any options that tell the system it can disable the device to save power. This will vary by operating system so we recommend you conduct an internet search for the appropriate instructions.
::::

::::{dropdown} Why am I seeing WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED when I log in?
Some users logging in through ssh may encounter this error message. If you receive this message, please see our instructions on how to clear this error.

When I try to log in with ssh, nothing happens when I type my password!
When you type your passaword, the ssh program does not echo your typing or move your cursor. This is normal behavior.
::::

::::{dropdown} When running Firefox on the cluster, I get : “Firefox is already running, but is not responding. To open a new window, you must first close the existing Firefox process, or restart your system.” What can I do?
From your home directory on the cluster, run the commands:

:::{code} bash
rm -rf ~/.mozilla/firefox/*.default/.parentlock
rm -rf ~/.mozilla/firefox/*.default/lock
:::
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

## Other Questions
::::{dropdown} How do I acknowledge the use of Research Computing resources?
Please acknowledge resources provided by Northeastern University's Research Computing in publications as follows:

Support provided by Research Computer at Northeastern University [1]. And cite as (using the appropriate citation format):

[1] Research Computing, Northeastern University, https://rc.northeastern.edu/.
::::

::::{dropdown} I think I have a cluster issue, but I'm not sure about it. What should I do?
You can always open a support request when you have questions even if you are not sure whether there is an issue.
:::{seealso}
{ref}`getting-help`
:::
::::

::::{dropdown} How do I report a HPC problem?
Please see {ref}`getting-help`
::::

::::{dropdown} What if my question does not appear here?
Take a look at our documentation. If your answer isn’t there, contact Research Computing using {ref}`getting-help`.
::::

:::{button-link} faq.html
:color: primary
:align: center
Back to the top
:::

---
This FAQ is not exhaustive. If you have further questions, check the relevant section of the documentation or contact Research Computing support.

[servicenow rc access request form]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0ae24596db535fc075892f17d496199c