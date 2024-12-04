(class-guide)=
# Course Guide

We support classroom education at Northeastern University by providing access to computing resources (CPU and GPU) and storage resources for instructors and their students.

We’ve supported courses from many disciplines, including biology, chemistry, civil engineering, machine learning, computer science, mathematics, and physics.

To gain access to HPC resources instructors need to submit a [classroom access form.](https://bit.ly/NURC-Classroom)

:::{important}
Please submit classroom access requests prior to the beginning of each term (preferred), or at least **one week** prior to the start of when you plan on using the HPC cluster for your class. If you're requesting a customized application we require **two-weeks** to **one-month** time to complete prior to when you'd like to use it.
:::

## Classroom setup

Once access is provided, each course will have a course-specific directory under `/courses/` following this sample file tree. As shown for the course BINF6430.202410 below:

:::{code-block} bash

/courses/
└── BINF6430.202410/
    ├── data/
    ├── shared/
    ├── staff/
    └── students/

:::

The sub-directory `staff/` will be populated with a folder for each of the following: instructors, co-instructors, and TAs. The `students/` sub-directory contains a folder for each student. And the `data/` and `shared/` sub-directories can be populated by those in staff but is read-only for students. Students only have permission to read into their own directories under `students/` and cannot view into another students space.

All those in staff have read-write-execute permissions within the entirety of their courses directory, allowing them to store data, homework assignments, build conda environments, create new directories, etc, as they see fit.

Each course directory gets a default 1TB of storage space. This amount can be increased in the initial application form for classroom access, or requested anytime during an actively running course, by contacting <rchelp@northeastern.edu>

Once the course has ended, and final grades have been submitted, the courses space including all data and shared class files will be archived, and all student personal directories will be deleted. Any students who had access to the HPC cluster only though the course will no longer have access when the course is completed.

Please see our page on [getting-access](https://rc.northeastern.edu/getting-access/) if you would like an account that persists through taking courses.

## Courses Partitions

We have two partitions dedicated to the use of students and instructors for the duration of their course.

::::{list-table}
---
header-rows: 1
---
* - Name
  - Time Limit (default/max)
  - Running Jobs (max)
  - RAM Limit
* - courses
  - 4 hrs / 24 hrs
  - 50
  - 256 GB
* - courses-gpu
  - 4 hrs / 8 hrs
  - 2
  - 12 GB
::::

The resources available in the courses/courses-gpu partitions can be queried with the command `sinfo` as run in the command line. We manage the resourses in courses/courses-gpu each term in response to the number of courses and requested usage per course.

:::{code-block} bash
sinfo -p courses-gpu  --Format=nodes,cpus,gres,statecompact
:::

These partitions can be used in the following ways:

(sbatch-courses-index)=

### sbatch script

An sbatch script can be submitted on the command line via the command `sbatch scriptname.sh`. Below are some examples of sbatch scripts using the courses and courses-gpu partitions. See {ref}`slurm-running-jobs` for more information on running sbatch scripts or run `man sbatch` for additional sbatch parameters.

::::{dropdown} courses partition
:::{code-block}bash

 #!/bin/bash

 #SBATCH --nodes=1  
 #SBATCH --time=4:00:00  
 #SBATCH --job-name=MyCPUJob  
 #SBATCH --partition=courses  
 #SBATCH --mail-type=ALL  
 #SBATCH --mail-users=username@northeastern.edu  

# commands to execute  

:::
::::

::::{dropdown} courses-gpu partition
:::{code-block}bash

 #!/bin/bash

 #SBATCH --nodes=1  
 #SBATCH --time=4:00:00  
 #SBATCH --job-name=MyGPUJob  
 #SBATCH --partition=courses-gpu  
 #SBATCH --gres=gpu:1  
 #SBATCH --mail-type=ALL  
 #SBATCH --mail-users=username@northeastern.edu  

# commands to execute for gpu

:::
::::

(srun-courses-index)=

## srun interactive session

An interactive session can be run on the command line via the `srun` command as shown in the examples below. See {ref}`slurm-running-jobs` for more information on using `srun` or run `man srun` to see additinal parameters that can be set with `srun`.

::::{dropdown} courses partition
:::{code-block} bash
srun --time=4:00:00 --job-name=MyJob --partition=courses --pty /bin/bash
:::
::::

::::{dropdown} courses-gpu partition
:::{code-block} bash
srun --time=4:00:00 --job-name=MyJob --partition=courses-gpu --gres=gpu:1 --pty /bin/bash
:::
::::

(OOD-courses-index)=

### Open OnDemand

We have several widely-used applications available on the Open OnDemand (OOD) website including, Jupyterlab Notebook, Rstudio, Matlab, GaussView and more.

You can login to the Open OnDemand website via the link below.

[ood.explorer.northeastern.edu](https://ood.explorer.northeastern.edu/)

All of the applications under the “Courses” tab on the dashboard can be set to either the `courses` or `courses-gpu` partitions via the applications specific pull down menus.

### Monitoring Jobs

Whichever way you choose to run your jobs, you can monitor their progress with the command `squeue`.

:::{code-block} bash
squeue -u username
:::

You can also monitor jobs being run on either of the courses partitions.

:::{code-block} bash
squeue -p courses
squeue -p courses-gpu
:::

Jobs can be canceled with the command `scancel` and the slurm job id that is assigned when your job is submitted to the scheduler.

:::{code-block} bash
scancel jobid
:::

:::{note} A cluster is a collection of shared resources. We highly recommend canceling any jobs that are still running in an interactive session (on the OOD or via srun) when you have completed your work. This frees up the resources for other classmates and instructors.
:::

## Software Applications

All courses have access to the [command line](https://rc-docs.northeastern.edu/en/latest/first_steps/usingbash.html#command-line).

We have many software applications installed system wide as modules that are available through the command line via the [“module” command](https://rc-docs.northeastern.edu/en/latest/software/systemwide/modules.html).

We also support many software applications for courses and have interactive versions on the [Open OnDemand](https://rc-docs.northeastern.edu/en/latest/using-ood/index.html) website including:

Jupyterlab notebook, Rstudio, Matlab, VSCode, Maestro (Schrodinger), and a unix Desktop

Professors should create custom conda environments for their course which can be used in JupyterLab notebook or used in interactive mode (srun) or sbatch scripts on the command line.

## Custom Course Applications

At Northeastern University instructors have a great deal of flexibility in how they use the HPC for their classroom, and this is most apparent in the use of software applications.

We encourage professors to perform local software installations via conda environments within the `/courses` directory for their class. These can be used by the students to complete tutorials and homework assignments. Students can also create their own conda environments in their `/courses/course.code/students/username` directory to complete their own projects. [Conda environments](https://rc-docs.northeastern.edu/en/latest/software/packagemanagers/conda.html#conda) can be used to install a variety of research software and are not only useful for coding in python.

For most courses, the instructor is able to create a shared conda environment in their `/courses` directory that can provide all the necessary packages for the class.

In other cases, where specialized software is needed, please book a classroom consultation with one of the [RC team members](https://outlook.office365.com/owa/calendar/ResearchComputing2@northeastern.onmicrosoft.com/bookings/) to discuss what is needed. Please allow at least **one month** for specialized app development and testing. In some cases we may be unable to provide the exact specifications requested. We will work with the instructor to find a suitable solution.
