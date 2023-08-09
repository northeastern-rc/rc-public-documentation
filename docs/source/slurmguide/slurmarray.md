(slurm-arrays)=
# Slurm Array Jobs and Dependencies

Slurm job arrays offer a mechanism for submitting and managing collections of similar jobs. This page comprehensively introduces Slurm job arrays, explains their syntax, presents a series of practical and more advanced use cases, and shares best practices.

## Introduction to Slurm Job Arrays

A Slurm job array is an ensemble of similar independent jobs submitted using a single script. Each job in the array is assigned a unique array index that can be utilized within the script to differentiate the behavior of each job.

## Syntax and Command Options

The standard syntax for submitting a job array is as follows:

:::{code} bash
#SBATCH --array=<indexes>
:::

`<indexes>` can be a list of specific indices or a range of indices.

Hence, syntax for creating job arrays in Slurm is the `--array` or `-a` option, followed by the array specification. Here are the various ways you can specify job arrays:

- A range of integers: `-array=0-99` submits a hundred jobs with indices 0 through 99.
- Specific integers: `-array=7,8,11` submits three jobs with indices 7, 8, and 11.
- Step values: `-array=0-99:2` submits fifty jobs with indices 0, 2, 4,...,98.
- Combining specifications: `-array=0-9:2,11,12,15-20` submits jobs with indices 0, 2, 4, 6, 8, 11, 12, 15, 16,...,20.

## Use Cases: Novice to Expert

These use cases progress from simple to complex, demonstrating the flexibility of Slurm job arrays. The `$SLURM_ARRAY_TASK_ID` variable is a built-in variable that contains the current job's index.

### Novice Use-Cases

Submit an array of 10 jobs, each printing its array index:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
echo "I am job number $SLURM_ARRAY_TASK_ID"
:::


An array of 10 jobs, each creating a uniquely-named directory:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
mkdir "directory${SLURM_ARRAY_TASK_ID}"
:::

Process different files using an array job. Assume you have files named file1.txt, file2.txt, etc., up to file10.txt:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
filename="file${SLURM_ARRAY_TASK_ID}.txt"
touch $filename # touch creates empty files with that name if they do not exist
:::


Execute a Python script with a unique argument from each job in the array:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
python my_script.py --index $SLURM_ARRAY_TASK_ID
:::

### Intermediate Use-Cases
Create an array of 10 jobs, each sleeping for a different duration:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
sleep $SLURM_ARRAY_TASK_ID
:::

Use an array job to run simulations with different random seeds:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10

./my_simulation --seed $SLURM_ARRAY_TASK_ID
:::

Analyzing Different Sets of Images**

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10

./image_analysis "images/set${SLURM_ARRAY_TASK_ID}" > "analysis${SLURM_ARRAY_TASK_ID}.txt"
:::

### Expert Use-Cases
Use an array job to compute the factorial of numbers from 1 to 10. Here we use a small Python script:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
python -c "import math; print(math.factorial($SLURM_ARRAY_TASK_ID))"
:::

Creating Different Directories for Each Job's Output

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10

mkdir -p "output${SLURM_ARRAY_TASK_ID}"
./my_program > "output${SLURM_ARRAY_TASK_ID}/output.txt"
:::

Use an array job to process different datasets with different parameters. Assume you have parameters stored in a parameters.txt file:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
param_line=$(sed -n "${SLURM_ARRAY_TASK_ID}p" parameters.txt)
./my_program $param_line
:::

An array job that runs a set of Monte Carlo simulations, with each job starting from a different initial condition:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
initial_condition=$(($SLURM_ARRAY_TASK_ID * 10))
./my_simulation --initial $initial_condition
:::

An array job that processes large datasets chunk-wise. Each job processes a unique chunk of data:

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10
start_line=$(($SLURM_ARRAY_TASK_ID * 1000))
end_line=$(($start_line + 999))
sed -n "${start_line},${end_line}p" large_dataset.txt | ./my_program
:::

## More Advanced Usage of Slurm Job Arrays

While the primary usage of Slurm job arrays is pretty straightforward, you can achieve much more sophisticated job control with some advanced techniques.

### Handling Large Job Arrays

For handling huge job arrays, Slurm allows you to specify a maximum number of simultaneously running tasks from the array job. For instance, if you want to submit a thousand jobs but want only a maximum of 50 jobs running at any given time, you can use the "%" operator:

:::{code} bash
#SBATCH --array=1-1000%50
:::

<aside>
ℹ️ The maximum number of elements on our cluster is 50.

</aside>

### Using Array Index in Shell Scripting

The array index can be used in shell scripting, allowing for more complex behaviors. For instance, if you have a list of files to process, you can construct an array in Bash and then index  it with the `$SLURM_ARRAY_TASK_ID`.

:::{code} bash
#!/bin/bash
#SBATCH --array=0-9

files=("file1.txt" "file2.txt" "file3.txt" "file4.txt" "file5.txt" "file6.txt" "file7.txt" "file8.txt" "file9.txt" "file10.txt")

my_program "${files[$SLURM_ARRAY_TASK_ID]}"
:::

### Array Dependencies**

You can set up dependencies between array jobs using the same syntax as regular job dependencies. For example, the following will only run the second array job after all tasks from the first array job have been completed:

:::{code} bash
#SBATCH --array=1-10
#SBATCH --job-name=jobA

# ... Job Script for jobA here ...

#SBATCH --array=1-10
#SBATCH --job-name=jobB
#SBATCH --dependency=afterok:jobA

# ... Job Script for jobB here ...
:::

### Debugging Array Jobs

Array jobs can be tricky to debug because each task is independent and can generate a lot of output. One technique is to redirect each task's output to a different file. The `$SLURM_ARRAY_TASK_ID` can be used to create unique file names.

:::{code} bash
#SBATCH --array=1-10
#SBATCH --output="output_%A_%a.out"
#SBATCH --error="error_%A_%a.err"
:::

### Conditional Execution

In some cases, you may want to conditionally execute tasks within the job array. You can achieve this by using conditional statements in your job script and leveraging the `$SLURM_ARRAY_TASK_ID`.

:::{code} bash
#!/bin/bash
#SBATCH --array=1-10

if (( SLURM_ARRAY_TASK_ID % 2 == 0 )); then
  # execute for even task IDs
  my_program_even
else
  # execute for odd task IDs
  my_program_odd
fi
:::

These advanced usages of Slurm job arrays demonstrate how they can provide versatile and powerful job control mechanisms for high-throughput computing tasks.

## Best Practices

- Use the `$SLURM_ARRAY_TASK_ID` variable directly in your scripts for unique behavior per job.
- Monitor your array jobs with the `squeue` command, which shows the status of all jobs in the queue.
- Remember that jobs in your array will be scheduled as resources become available, which could result in a delay between jobs if resources are limited.

Job arrays offer a powerful feature of Slurm that can help you manage multiple similar jobs more efficiently. Don't hesitate to ask questions or share your use cases in our User Community and Forums.
