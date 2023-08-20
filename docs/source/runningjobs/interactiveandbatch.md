(interactive-and-batch-mode)=
# Interactive and Batch Mode

In our High-Performance Computing (HPC) environment, users can run jobs in two primary modes: Interactive and Batch. This page provides an in-depth guide to both, assisting users in selecting the appropriate mode for their specific tasks.

## Interactive Mode

Interactive mode allows users to run jobs that need immediate execution and feedback.

### Getting Started with Interactive Mode

To launch an interactive session, use the following command:

:::{code} bash
# Request an interactive session
srun --pty /bin/bash
:::

This command allocates resources and gives you a shell prompt on the allocated node.

(interactive-mode-use-cases)=
### Interactive Mode Use Cases
- **Development and Testing**: Ideal for code development and testing.
- **Short Tasks**: Best for tasks that require less time and immediate results.

:::{seealso}
ADD LINK for More Examples and Guides for Interactive Mode
:::

## Batch Mode
Batch mode enables users to write scripts that manage job execution, making it suitable for more complex or longer-running jobs.

### Creating Batch Scripts
A typical batch script includes directives for resource allocation, job name, and commands. Here's an example:

:::{code} bash
#!/bin/bash
#SBATCH --job-name=my_job
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=01:00:00

# Commands to execute
module load my_program
srun my_program.exe
:::

Save this script with a `.sh` extension, e.g., my_script.sh.

### Submitting Batch Jobs
Submit your batch script using the sbatch command:

:::{code} bash
sbatch my_script.sh
:::

### Monitoring Batch Jobs
You can monitor the status of your batch job using the squeue command:

:::{code} bash
squeue -u username
:::

Replace username with your actual username.

(batch-mode-use-cases)=
### Use Cases
- **Long-Running Jobs**: Suitable for extensive simulations or calculations.
- **Scheduled Tasks**: Execute jobs at specific times or under certain conditions.
- **Automated Workflows**: Manage complex workflows using multiple scripts.

:::{seealso}
ADD LINK for More Examples and Guides for Batch Mode
:::

Interactive and Batch modes cater to different needs and scenarios in the HPC environment. Explore both modes to choose the one that best aligns with your tasks. For more detailed guides and support, please consult the specific guides linked above or contact our support team at <rchelp@northeastern.edu>.

Happy computing!
