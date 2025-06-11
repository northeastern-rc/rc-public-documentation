(faq)=
# Frequently Asked Questions (FAQs)
Below are some common questions and answers regarding our HPC cluster and its operation.

::::{dropdown} - My OOD job shutsdown/completes quickly before/during/after starting? OR <br> - When I try and launch an OOD job, I get: "Disk quota exceeded" error. OR <br> - My OOD Desktop job starts and quickly moves to `Completed` without starting..

There are two main things to check:
1. Check that the memory available in `/home/$USER` is less than the quota limit.

There are storage quotas on `$HOME` directories. (See {ref}`home-directory-storage-quota` for more details). OOD applications run from the `$HOME` directory and it is important that there is enough space in `$HOME` for the OOD application to run.

In the terminal, run `du -shc .[^.]* * /home/$USER`, which should have output similar to the following:
:::{code-block} shell
[<username>@<host> ~]$  du -shc .[^.]* * /home/$USER/
39M     .git
106M    examples
41K     README.md
3.3M    software-installation
147M    total
:::

Based on the output, we can check which files are consuming how much memory, and which files can be removed to free up memory.

2. Check if there are other scripts running at startup (in `.bashrc`), or an anaconda or other environments loading at startup.
   
We recommend loading other scripts/environments after your main environment has been loaded. We recommend activating any conda environments _after_ the main environment has been loaded. If there are other scripts/environments you'd like to run, we recommend creating a separate bash script and sourcing it once the main environment has been loaded. For more details on the `.bashrc` file and best practices, see {ref}`about-bashrc`.
::::

::::{dropdown} Can I install my software on the HPC cluster?
Yes, you can. Please follow the guidelines in the {ref}`package-managers` and {ref}`from-source` sections. If you encounter any issues, contact [Research Computing](https://rc.northeastern.edu/support/gettinghelp/).
::::

::::{dropdown} How to Resolve the "Error: C++17 standard requested but CXX17 is not defined" When Installing a Package in R?
1. Ensure that you have the GCC version 11.1.0 module loaded. Run the following command
:::{code-block} shell
module load gcc/11.1.0
:::
      
2. Later create a .R/Makevars file to add compiler flags using following commands.
:::{code-block} shell
mkdir -p ~/.R
nano ~/.R/Makevars
::: 

3. Next, make sure to add the following flags in the file.
::: {code-block}
CXX17 = g++ -std=c++17 -fPIC
CXX17STD = -std=c++17
PKG_CXXFLAGS = -std=c++17 -fPIC
PKG_LIBS = -fPIC
::: 

5. Now try to install the desired package.

6. If you are using a different version of GCC, adjust the module load command accordingly (e.g., module load gcc/9.3.0).

::::   
::::{dropdown} To use a node connected by Infiniband please use the flag 'constraint=ib' in your srun or sbatch sessions.
::: {code-block}
#SBATCH --constraint=ib
:::
:::{code-block}
srun -p short --constraint=ib --pty /bin/bash
:::
::::
