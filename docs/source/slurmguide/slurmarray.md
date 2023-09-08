(slurm-arrays)=
# Slurm Array Jobs and Dependencies

<> (job-arrays)=
## Slurm Job Arrays
Job arrays are a convenient way to submit and manage large numbers of similar jobs quickly. They can process millions of tasks in milliseconds, provided they are within size limits. Job arrays are particularly useful when running similar jobs, such as performing the same analysis with different inputs or parameters.

Using job arrays can save time and reduce the amount of manual work required. Instead of submitting each job individually, you can submit a single job array and let Slurm handle the scheduling of individual jobs. This approach is beneficial if you have limited time or resources, as it allows you to use the cluster's computing power more efficiently by running multiple jobs in parallel.

There are several ways to define job arrays, such as specifying the range of indices or providing a list of indices in a file. Slurm also offers various features to manage and track job arrays, such as options to simultaneously suspend, resume, or cancel all jobs in the array.

### Syntax: Job Arrays
The most basic configuration for a job array is as follows:
:::{code}
#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=jarray-example
#SBATCH --output=out/array_%A_%a.out
#SBATCH --error=err/array_%A_%a.err
#SBATCH --array=1-6
:::
This command runs the same script six times using Slurm job arrays. Each job array has two additional environment variable sets. `SLURM_ARRAY_JOB_ID` (`%A`) is set to the first job ID of the array, and `SLURM_ARRAY_TASK_ID` (`%a`) is set to the job array index value.

:::{note}
Both the `SLURM_ARRAY_JOB_ID` (`%A`) and `SLURM_ARRAY_TASK_ID` (`%a`) are referenced when naming outputs so file do not overwrite when a "task" (i.e., one of the executions of the script through the job array) finishes.
:::

::::{tip}
Generally, we want to pass the former as an argument for our script. If you are using R, you can retrieve the former using `task_id <- Sys.getenv("SLURM_ARRAY_TASK_ID")`. If you are using job arrays with Python, you can obtain the task ID using the following:

:::{code} python
import sys
taskId = sys.getenv('SLURM_ARRAY_TASK_ID')
:::
::::

When submitting an array and setting its size with many dimensions, please use the `%` symbol to indicate how many tasks run simultaneously. For example, the following code specifies an array of 600 jobs, with 20 running at a time:

:::{code} bash
#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=jarray-example
#SBATCH --output=out/array_%A_%a.out
#SBATCH --error=err/array_%A_%a.err
#SBATCH --array=1-600%20
:::

Whenever you specify the memory, number of nodes, number of CPUs, or other specifications, they will be applied to each task. Therefore, if we set the header of our submission file as follows:

:::{code}
#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=jarray-example
#SBATCH --output=out/array_%A_%a.out
#SBATCH --error=err/array_%A_%a.err
#SBATCH --array=1-600%20
#SBATCH --mem=128G
#SBATCH --nodes=2
:::
Slurm will submit 20 jobs simultaneously. Each job, represented by a task ID, will use two nodes with 128GB of RAM each. In most cases, setting up a single task is sufficient.

Lastly, we usually use job arrays for embarrassingly parallel jobs. If your case is such that the job executed at each job ID does not use any multi-threading libraries, you can use the following header to avoid wasting resources:

:::{code}
#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=jarray-example
#SBATCH --output=out/array_%A_%a.out
#SBATCH --error=err/array_%A_%a.err
#SBATCH --array=1-600%50  # 50 is the maximum number
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G ## debug prior to know how much RAM
:::

:::{warning}
50 is the maximum number of jobs allowed to be run at once per user-account.
:::

The above examples apply for interactive mode, as well. For instance:

:::{code} bash
sbatch --array=<indexes> [options] script_file
:::

Indexes can be listed as `1-5` (i.e., one to five), `=1,2,3,5,8,13` (i.e., each index listed), or `1-200%5` (i.e., produce a 200 task job array with only 5 tasks active at any given time). **The symbol used is the % sign, which tasks to be submitted at once** (again, cannot be set larger than 50).


### Use-cases: Job Arrays
Job arrays can be used in situations where you have to process multiple data files using the same procedure or program. Instead of creating multiple scripts or running the same script multiple times, you can create a job array, and Slurm will handle the parallel execution for you.

### Example using Job Array Flag

In the following script, the `$SLURM_ARRAY_TASK_ID` variable is used to differentiate between array tasks.

:::{code} bash
#!/bin/bash
#SBATCH -J MyArrayJob           # Job name
#SBATCH -N 1                    # Number of nodes
#SBATCH -n 1                    # Number of tasks
#SBATCH -o output_%A_%a.txt     # Standard output file (%A for array job ID, %a for array index)
#SBATCH -e error_%A_%a.txt      # Standard error file

# Your program/command here
srun ./my_program input_$SLURM_ARRAY_TASK_ID
:::

To submit this job array, save it as `my_array_job.sh` and run:

:::{code} bash
sbatch --array=1-50 my_array_job.sh
:::

This command will submit 50 jobs, running `my_program` with `input_1` through `input_100`.
