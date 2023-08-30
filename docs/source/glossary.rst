=================
Glossary
=================
This glossary provides definitions for terms and abbreviations you may encounter when using our HPC cluster.

-------

.. glossary::

   Backfilling
      A scheduling technique that allows smaller jobs to be scheduled ahead of larger jobs, as long as they don't impact the completion of larger high-priority jobs.

   Cluster
      A group of computers connected in a way that allows them to function as a single system.

   Cluster Manager
      A software system responsible for monitoring and managing the health, status, and communication among nodes in a cluster.

   Concurrency
      The ability of the system to handle multiple tasks or jobs simultaneously, without waiting for each task to complete before starting another.

   Container
      TBD.

   Core
      A processor within a CPU. Each core can execute its tasks.

   CPU (Central Processing Unit)
      The primary component of a computer that performs most processing inside the computer. CPUs can have multiple cores.

   Fair Share Allocation
      A scheduling policy that ensures all users receive a fair share of cluster resources over time, regardless of job size or priority.

   Graphics Processing Unit (GPU)
      A specialized electronic circuit designed to rapidly manipulate and alter memory to accelerate the creation of images in a frame buffer intended for output to a display device.

   GPU Acceleration
      The use of GPUs to offload computation-intensive tasks from the CPU, leading to faster processing of tasks like simulations and data analysis.

   Home Directory
      A user's directory in the cluster where personal files, application settings, and other user-specific data are stored.

   HPC (High-Performance Computing)
      The use of parallel processing for running advanced application programs efficiently, reliably, and quickly. It's often used for scientific research, big data analysis, and modeling complex systems.

   Job
      A set of computations a user submits to the HPC cluster for execution.

   Job Dependency
      The condition where one job relies on the successful completion of another job before it can start, ensuring proper sequencing of tasks.

   Job Script
      A file that contains a series of commands that the HPC cluster will execute.

   Module
      In the context of HPC, a module is a bundle of software that can be loaded or unloaded in the user's environment.

    Message Passing Interface (MPI)
      A standardized and portable message-passing system used to enable communication between nodes in a parallel computing environment.

   Node
      A single machine within a cluster. A node can have multiple processors and its memory and storage.

   Node Allocation
      The process of reserving a set of nodes for a specific job, ensuring that the required resources are available for successful execution.

   Overcommitment
      Allowing more resources to be allocated to jobs than physically available, relying on intelligent scheduling and efficient resource management.

   Package Manager
       A collection of software tools that automates the process of installing, upgrading, configuring, and removing computer programs for a computer in a consistent manner.

   Parallel Computing
      A type of computation in which multiple calculations or processes are carried out simultaneously to solve a problem faster.

   Partition
      A division of the cluster resources. Each partition can have different configurations, such as different types of nodes and different access policies.

   Quota
      TBD.

   Queue
      A waiting line for jobs ready to be executed but waiting for resources to become available.

   Resource Reservation
      The process of specifying resources required for a job in advance to ensure availability and prevent resource conflicts.

   Scheduling Policy
      A set of rules and algorithms used by the scheduler to determine the order in which jobs are executed based on their priority, resource requirements, and other factors.

   Scratch Space
      Temporary storage that allows users to store intermediate data during job execution. Data in scratch space is not preserved between jobs.

   Storage Cluster
      A set of networked storage devices used to provide centralized and scalable storage solutions for the HPC environment.

   Scheduler
      A program that manages the cluster's resources and allocates them to jobs based on priority, requested resources, and fair use policies.

   Singularity
      TBD.

   Slurm
      An open-source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small HPC clusters.

   Task
      A unit of work within a job that can be executed independently. A job can consist of multiple tasks.

   VPN
      TBD.

-------

This glossary is not exhaustive. If you come across a term not listed here, please check the specific section of the documentation or ask in our User Community and Forums.
