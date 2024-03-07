(slurm-arrays)=
# Slurm Array Jobs

Job arrays are a convenient way to submit and manage large numbers of similar jobs quickly. Job arrays are particularly useful when running similar jobs, such as performing the same analysis with different inputs or parameters.

There are several ways to define job arrays, such as specifying the range of indices or providing a list of indices in a file. Slurm also offers various features to manage and track job arrays, such as options to simultaneously suspend, resume, or cancel all jobs in the array.

:::{warning}
50 is the maximum number of jobs allowed to be run at once per user-account.
:::

## Job Array Examples
The most basic configuration for a job array is as follows:
:::{code} bash
#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=job-array-example
#SBATCH --output=out_array_%A_%a.out
#SBATCH --error=err_array_%A_%a.err
#SBATCH --array=1-6
:::
This command runs the same script six times using Slurm job arrays. Each job array has two additional environment variable sets. `SLURM_ARRAY_JOB_ID` (`%A`) is set to the first job ID of the array, and `SLURM_ARRAY_TASK_ID` (`%a`) is set to the job array index value. Both the `SLURM_ARRAY_JOB_ID` (`%A`) and `SLURM_ARRAY_TASK_ID` (`%a`) are referenced when naming outputs in the example so they are not overwrite when a "task" (i.e., one of the executions of the script through the job array) finishes.

::::{tip}
Generally, we want to pass the former as an argument for our script. If you are using R, you can retrieve the former using `task_id <- Sys.getenv("SLURM_ARRAY_TASK_ID")`. If you are using job arrays with Python, you can obtain the task ID using the following:

:::{code} python
import sys
taskId = sys.getenv('SLURM_ARRAY_TASK_ID')
:::
::::

## Resource Allotment in Job Arrays 
When submitting an array and setting its size with many dimensions, please use the `%` symbol to indicate how many tasks run simultaneously. Whenever you specify the memory, number of nodes, number of CPUs, or other specifications, they will be applied to each task. For example, the following code specifies an array of 600 jobs, with 20 running at a time:

:::{code}
#!/bin/bash
#SBATCH --partition=short
#SBATCH --job-name=job-array-example
#SBATCH --output=out-array_%A_%a.out
#SBATCH --error=err-array_%A_%a.err
#SBATCH --array=1-600%20
#SBATCH --mem=128G
#SBATCH --nodes=2
:::

Slurm will submit 20 jobs simultaneously. Each job, represented by a task ID, will use two nodes with 128GB of RAM each. In most cases, setting up a single task is sufficient.

Lastly, we usually use job arrays for embarrassingly parallel jobs. If your case is such that the job executed at each job ID does not use any multi-threading libraries, you can use the following header to avoid wasting resources:

:::{code} bash
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

## Job Arrays from Commmand Line

You can launch job arrays from the sbatch submission on the command line as follows:

:::{code} bash
sbatch --array=<indexes> [options] script_file
:::

Indexes can be listed as `1-5` (i.e., one to five), `=1,2,3,5,8,13` (i.e., each index listed), or `1-200%5` (i.e., produce a 200 task job array with only 5 tasks active at any given time).
