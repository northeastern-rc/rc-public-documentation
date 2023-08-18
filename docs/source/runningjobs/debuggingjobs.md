(debugging-jobs)=
# Debugging and Troubleshooting Jobs
This page focuses on common issues encountered when running jobs, how to interpret error messages and some practical strategies to debug these problems.

## Understanding Slurm Errors

Understanding the error messages that Slurm can generate is critical to resolving job issues.

:::{table} CREATE TABLE OF COMMON ERRORS:
| Common Slurm Error Messages and Potential Solutions                                 |
|-------------------------------------------------------------------------------------|
| sbatch: error: Batch job submission failed: Socket timed out on send/recv operation |
| srun: error: Unable to allocate resources: No such file or directory                |
:::

## Checking Job Status

This section will focus on the `scontrol show jobid -dd <jobid>` command to provide detailed information about the job. Example usage and output of the command can be included here.

## Redirecting Standard Output and Error Streams

Explain how to use `#SBATCH --output` and `#SBATCH --error` to redirect standard output and error to files. This helps in capturing any error messages produced by the program.

## Debugging Strategies

This section will explain the importance of testing jobs on a small scale before submitting large jobs. It can discuss using a single node for testing, using the --test-only option, and examining output and error files.

:::{code} bash
#SBATCH --output=myjob.out
#SBATCH --error=myjob.err
:::

## Interactive Job Session

Explain how to start an interactive job session with the `salloc` command, which allows users to interact with their job and troubleshoot issues in real-time directly.

:::{code} bash
salloc --nodes=1 --time=01:00:00 --account=myaccount
:::

## Using Debuggers

Discuss using debuggers such as GDB for C/C++ and PDB for Python to step through the code and identify bugs. Include a brief example of how to use them.

## Common Job Issues and Their Resolutions

List some common issues users might encounter, like jobs getting stuck in the queue, jobs not producing expected output, or jobs using more memory than expected. Offer solutions or workarounds for each of these issues.
