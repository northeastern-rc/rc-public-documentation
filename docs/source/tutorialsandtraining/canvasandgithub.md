(canvasandgithub)=
# Canvas and GitHub

## Recorded Trainings

The RC Team provides free online training sessions for cluster users and Northeastern Students. If you’re new to the cluster, we strongly recommend watching the [Discovery Introduction Video](https://www.linkedin.com/checkpoint/enterprise/login/74653650?pathWildcard=74653650&amp;application=learning&amp;redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Flearning%2Fcontent%2F1139340%3Fu%3D74653650). You’ll need to sign in using your Northeastern username and password to view the video.

Join the [Research Computing Training Course in Canvas](https://northeastern.instructure.com/enroll/LNNCHN) to access on-demand training videos. Once you have clicked the link to enroll, you must log in using your Northeastern credentials. The training sessions cover a wide range of topics for all skill levels and offer you the opportunity to explore training sessions at your own pace in the areas that you’re most interested in (e.g., Linux and Shell Scripting, Slurm Arrays, Software Installation, GPUs, Bioinformatics, Deep Learning, and LAMMPs). You can perform hands-on training exercises by accessing RC files shared on GitHub repositories. 

## Live Training

Make sure to keep an eye on your email or the RC Training Course in Canvas for upcoming live training sessions and the RC Summer Bootcamp.

## Classroom Facilitations

If you are a faculty member using Discovery with your class and would like us to develop or present a personalized training session for your class, please reach out to us at [rc.northeastern.edu](https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Frc.northeastern.edu%2F&amp;data=04%7C01%7Ct.ketchem%40NORTHEASTERN.EDU%7C0df6c43eab514b8a96c708da141e534c%7Ca8eec281aaa34daeac9b9a398b9215e7%7C0%7C0%7C637844417724461490%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&amp;sdata=KAEsJGBJg%2FwhHoPdAb%2B4JkkraL385D4mxEufV9AAi30%3D&amp;reserved=0).

## GitHub Repositories


## Previous Training Sessions
These are the previous training sessions led by Research Computing staff on a variety of topics related to HPC usage and workflow to domain specific topics. All videos are on Canvas and require you to enroll in our free [Canvas course] to access them.

### Bootcamp 2023

:::{list-table}
---
header-rows: 1
widths: 16 47
---
* - Session Title
  - Description
* - [Discovery Basics](https://northeastern.instructure.com/courses/126767/modules/items/8944711)
  - A beginner-level session for Discovery users to get them started with computing on the cluster. The session includes an introduction to basic concepts of high-performance computing including launching jobs interactively & in the background, accessing various partitions, monitoring the status of submitted jobs, and getting familiar with the cluster’s job scheduler; Slurm. This also includes hands-on exercises for getting started on Discovery.
* - [Introduction to OOD](https://northeastern.instructure.com/courses/126767/modules/items/8944999)
  - Beginner-level session for Discovery users to learn the basics of Open On Demand and the tools available to them.
* - [Linux & Shell Scripting](https://northeastern.instructure.com/courses/126767/modules/items/8945001)
  - Beginner to intermediate-level session for Discovery users to learn the basics of the Linux command line and scripting using the standard Linux command shell BASH.
* - [Slurm Arrays](https://northeastern.instructure.com/courses/126767/modules/items/8945002)
  - An advanced-level session for Discovery users to understand what Slurm arrays are and how they can be used to enhance the efficiency and scalability of job execution in HPC environments by allowing users to manage and execute a group of similar jobs as a unified entity.
* - [Storage](https://northeastern.instructure.com/courses/126767/modules/items/8953842)
  - Understanding storage tiers at Research Computing, how to access them, and perform data transfer to and from the cluster.
* - [Introduction to Software Installation](https://northeastern.instructure.com/courses/126767/modules/items/8954490)
  - Beginner-level session for users to learn about different ways to access/install software on Discovery, including the use of package managers (e.g., conda, spack) as well as installation from source.
* - [GPUs on Discovery](https://northeastern.instructure.com/courses/126767/modules/items/8954491)
  - Intermediate level session for Discovery users to familiarize themselves with utilizing various NVIDIA GPUs that are available to them on the cluster. The session includes various hands-on exercises to show how to launch jobs on the `gpu` partition with or without specific GPUs, running TensorFlow & PyTorch with GPU support on the cluster, and a few basic CUDA examples.
* - [Deep Learning Best Practices 1](https://northeastern.instructure.com/courses/126767/modules/items/8954495)
  - TBA
* - [LAMMPs](https://northeastern.instructure.com/courses/126767/modules/items/8954498)
  - This is an intermediate-level workshop covering the compiling of LAMMPS, basic constructions and format of input scripts, checkpointing LAMMPS jobs, using LAMMPS to calculate material properties, and basic benchmarking for optimal runtimes.
* - [ML Platforms on Discovery](https://northeastern.instructure.com/courses/126767/modules/items/8954500)
  - Intermediate-level session for Discovery users to familiarize themselves with various tools and platforms that are available to perform machine learning and data science on the cluster. The session includes various hands-on exercises to introduce the users to tools, such as JupyterLab, WEKA, KNIME, RAPIDS, PyCaret. If time permits, then we will execute workflows with big datasets like ImageNet on the cluster using PyTorch.
* - [Introduction to Accelerated Genomics](https://northeastern.instructure.com/courses/126767/modules/items/8967022)
  - Genomics sequencing is faster and cheaper than ever. The new bottleneck in the genomics pipeline is in the analysis. It can take upwards of 30 hours to run variant calling on a single sample, it could take months or even years to process thousands of samples. This is where CLARA Parabricks comes in. Using GPU acceleration, we have cut down the variant calling time to below 30 minutes for a 30x human genome. This allows for new genomics projects to be done at a scale that was not previously possible. In this session, we will discuss the capabilities of Parabricks, the performance compared to traditional genomics software packages (such as GATK), and show a demo of what it looks like in action.
* - [Using NVIDIA GPUs with Python](https://northeastern.instructure.com/courses/126767/modules/items/8967023)
  - In this workshop, you will get hands-on experience accelerating Python codes with NVIDIA GPUs. We will utilize code samples in two main categories to introduce you to Python GPU accelerated computing. First, we will explore drop-in replacements for SciPy and NumPy code through the CuPy library. Second, we will cover NVIDIA RAPIDS, which provides GPU acceleration for end-to-end data science workloads. We'll finish with an end-to-end example that incorporates all the tools introduced to tackle a geospatial problem. By the end of the workshop, you will have the skills to start accelerating your own Python codes with NVIDIA GPUs!
* - [HPC Parallel Computing](https://northeastern.instructure.com/courses/126767/modules/items/8954501)
  - Advanced-level session for Discovery users to learn about Parallel Computing (CPU-only) on Discovery. Includes introduction to HPC concepts, Parallelization approaches (shared memory, distributed memory, data parallel), Parallel computing libraries (OpenMP, MPI) and data-parallel example using Slurm job arrays.
Additional optional topics include: optimization approaches to run efficient parallel code, evaluating performance using advanced metrics: (speedup, efficiency and scaling tests), and Increasing MPI performance on the InfiniBand network.
* - [Bioinformatics 1: PCA and PCadapt](https://northeastern.instructure.com/courses/126767/modules/items/8954507)
  - Principal component analysis and outlier identification for population genomics data in PCAdapt.
* - [Bioinformatics 2: GWAS in GEMMA](https://northeastern.instructure.com/courses/126767/modules/items/8954506)
  - Genome-wide association test for population genomics data in GEMMA with imputation, kinship analyses, and covariant inclusion.
* - [Deep Learning Best Practices 2](https://northeastern.instructure.com/courses/126767/modules/items/8954508)
  - TBA
:::

### Intro Sessions Spring 2023

:::{list-table}
---
header-rows: 1
widths: 16 47
---
* - Session Title
  - Description
* - [Discovery Basics](https://northeastern.instructure.com/courses/126767/modules/items/7999641)
  - Beginner level session for Discovery users to get started with computing on the cluster. The session includes an introduction to basic concepts of high performance computing including launching jobs interactively and in the background, accessing various partitions, monitoring the status of submitted jobs, and getting familiar with the cluster’s job scheduler, Slurm. This also includes hands-on exercises for getting started on Discovery.
* - [Intro to GPUs](https://northeastern.instructure.com/courses/126767/modules/items/7999645)
  - Intermediate level session for Discovery users to familiarize themselves with utilizing various NVIDIA GPUs that are available to them on the cluster. The session includes various hands-on exercises to show how to launch jobs on the GPU partition with or without specific GPUs and running TensorFlow with GPU support on the cluster.
* - [Intro to Linux & Shell Scripting](https://northeastern.instructure.com/courses/126767/modules/items/7999695)
  - Beginner to intermediate-level session for Discovery users to learn the basics of the Linux command line and scripting using the standard Linux command shell BASH.
* - [Intro to OOD](https://northeastern.instructure.com/courses/126767/modules/items/7999643)
  - Beginner level session for Discovery users to learn the basics of Open On Demand and the tools available to them.
* - [Intro to Software Installation](https://northeastern.instructure.com/courses/126767/modules/items/7999718)
  - Beginner level session for users to learn about different ways to access/install software on Discovery, including the use of package managers (e.g., conda, spack) as well as installation from source.
* - [Intro to RC Storage](https://northeastern.instructure.com/courses/126767/modules/items/8664168)
  - Understanding storage tiers at Research Computing, how to access them, and perform data transfer to and from the cluster.
:::

### Fall 2022

:::{list-table}
---
header-rows: 1
widths: 16 47
---
* - Session Title
  - Description
* - [Intro to Discovery](https://northeastern.instructure.com/courses/126767/modules/items/8663302)
  - Beginner level session for Discovery users to get started with computing on the cluster. The session includes an introduction to basic concepts of high performance computing including launching jobs interactively and in the background, accessing various partitions, monitoring the status of submitted jobs, and getting familiar with the cluster’s job scheduler, Slurm. This also includes hands-on exercises for getting started on Discovery.
* - [Intro to OOD](https://northeastern.instructure.com/courses/126767/modules/items/8663308)
  - Beginner level session for Discovery users to learn the basics of Open On Demand and the tools available to them.
* - [Intro to GPUs](https://northeastern.instructure.com/courses/126767/modules/items/8663306)
  - Intermediate level session for Discovery users to familiarize themselves with utilizing various NVIDIA GPUs that are available to them on the cluster. The session includes various hands-on exercises to show how to launch jobs on the GPU partition with or without specific GPUs and running TensorFlow with GPU support on the cluster.
* - [Bioinformatics on Discovery](https://northeastern.instructure.com/courses/126767/modules/items/7999648)
  - Intermediate level session focused on running bioinformatics workflows on Discovery. We will cover some basic NGS workflows and hands-on exercises to demonstrate bioinformatics-specific job submission.
* - [Intro to Linux & Shell Scripting](https://northeastern.instructure.com/courses/126767/modules/items/8663311)
  - Beginner to intermediate-level session for Discovery users to learn the basics of the Linux command line and scripting using the standard Linux command shell BASH.
* - [Storage](https://northeastern.instructure.com/courses/126767/modules/items/7999706)
  - Understanding storage tiers at Research Computing, how to access them, and perform data transfer to and from the cluster.
* - [Intro Software Installation](https://northeastern.instructure.com/courses/126767/modules/items/8663318)
  - Beginner level session for users to learn about different ways to access/install software on Discovery, including the use of package managers (e.g., conda, spack) as well as installation from source.
* - [HPC & Parallel Computing](https://northeastern.instructure.com/courses/126767/modules/items/7999721)
  - Advanced-level session for Discovery users to learn about Parallel Computing (CPU-only) on Discovery. Includes introduction to HPC concepts, Parallelization approaches (shared memory, distributed memory, data parallel), Parallel computing libraries (OpenMP, MPI) and data-parallel example using Slurm job arrays.
Additional optional topics include: optimization approaches to run efficient parallel code, evaluating performance using advanced metrics: (speedup, efficiency and scaling tests), and Increasing MPI performance on the InfiniBand network.
* - [Job Arrays](https://northeastern.instructure.com/courses/126767/modules/items/7999725)
  - Intermediate level session to introduce slurm job array and its various aspects. The session will explore setting up simple to intermediate-level job arrays on the cluster and will include multiple hands-on exercises and demos.
:::

### Bootcamp 2022

:::{list-table}
---
header-rows: 1
widths: 16 47
---
* - Session Title
  - Description
* - [Discovery Tour](https://northeastern.instructure.com/courses/126767/modules/items/7388124)
  - Introductory session for non-Discovery users to learn about computing and storage resources offered by the university to all its members including high performance computing cluster, Discovery; how to request an account; what support is available; and how to receive support.
* - [Student Panel Discussion](https://northeastern.instructure.com/courses/126767/modules/items/7388126)
  - An informal discussion with the graduate research assistants (GRAs) of Research Computing (RC). Get to know our student staff, what it is like to be a GRA at RC, how to be an RC GRA, and any other questions one might have for our student staff.
* - [Discovery Basics](https://northeastern.instructure.com/courses/126767/modules/items/7388139)
  - Beginner level session for Discovery users to get them started with computing on the cluster. The session includes an introduction to basic concepts of high performance computing including launching jobs interactively & in the background, accessing various partitions, monitoring the status of submitted jobs, and getting familiar with the cluster’s job scheduler, Slurm. This also includes hands-on exercises for getting started on Discovery.
* - [Storage](https://northeastern.instructure.com/courses/126767/modules/items/7388140)
  - Understanding storage tiers at Research Computing, inside and outside of the HPC Cluster.
* - [Intro to OOD](https://northeastern.instructure.com/courses/126767/modules/items/7388138)
  - Beginner level session for Discovery users to learn the basics of Open On Demand and the tools available to them.
* - [Accessing and Installing Software on Discovery](https://northeastern.instructure.com/courses/126767/modules/items/7388114)
  - Intermediate level session for users to learn about different ways to access/install software on Discovery, including the use of package managers (e.g., conda, spack) as well as installation from source.
* - [ML on Discovery](https://northeastern.instructure.com/courses/126767/modules/items/7388128)
  - **Note: No video for this training.** Intermediate level session for Discovery users to familiarize themselves with various tools that are available to perform machine learning and data science on the cluster. The session includes various hands-on exercises to introduce the users to tools, such as JupyterLab, VSCode, PyCharm, running TensorFlow and PyTorch on the cluster, and executing workflows with big datasets like ImageNet on the cluster.
* - [GPUs on Discovery](https://northeastern.instructure.com/courses/126767/modules/items/7388129)
  - Intermediate level session for Discovery users to familiarize themselves with utilizing various NVIDIA GPUs that are available to them on the cluster. The session includes various hands-on exercises to show how to launch jobs on the `gpu` partition with or without specific GPUs, running TensorFlow & PyTorch with GPU support on the cluster, and a few basic CUDA examples.
* - [Bioinformatics on Discovery](https://northeastern.instructure.com/courses/126767/modules/items/7388130)
  - Intermediate level session focused on running bioinformatics workflows on Discovery. We will cover some basic NGS workflows and hands-on exercises to demonstrate bioinformatics-specific job submission.
* - [Checkpoint Restart on HPC](https://northeastern.instructure.com/courses/126767/modules/items/7388131)
  - Intermediate-level session for Discovery users to learn about Checkpointing methods on Discovery. Why it is important to use it on HPC, learn how to overcome scheduler time limits with Checkpointing techniques, how to use Checkpointing with Slurm job arrays and learn about user-level vs. application-level checkpointing.
* - [Linux & Shell Scripting](https://northeastern.instructure.com/courses/126767/modules/items/7388132)
  - Beginner to intermediate-level session for Discovery users to learn the basics of the Linux command line and scripting using the standard Linux command shell BASH.
* - [HPC Parallel Computing](https://northeastern.instructure.com/courses/126767/modules/items/7388133)
  - Advanced-level session for Discovery users to learn about Parallel Computing (CPU-only) on Discovery. Includes introduction to HPC concepts, Parallelization approaches (shared memory, distributed memory, data parallel), Parallel computing libraries (OpenMP, MPI) and data-parallel example using Slurm job arrays.Additional optional topics include: optimization approaches to run efficient parallel code, evaluating performance using advanced metrics: (speedup, efficiency and scaling tests), and Increasing MPI performance on the InfiniBand network.
* - [AMA](https://northeastern.instructure.com/courses/126767/modules/items/7388134)
  - Discovery Best Practices, but mostly your questions answered.
* - [Intro to Containers on Discovery](https://northeastern.instructure.com/courses/126767/modules/items/7388135)
  - Advanced-level session for Discovery users to understand what containers are and why they are useful for HPC. Includes introduction to common container frameworks (Docker, Singularity, and Podman) and container registries (DockerHub, Sylabs, Northeastern’s Harbor). The session includes several practical examples of how to pull and use containers on the cluster using Singularity (CPU and GPU supported containers).
:::

[Canvas course]: https://northeastern.instructure.com/enroll/LNNCHN
