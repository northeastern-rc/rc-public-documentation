(recurring-jobs)=
# Recurring Jobs

You can use `scrontab` to schedule recurring jobs. Its syntax is similar to that of `[crontab](https://man7.org/linux/man-pages/man5/crontab.5.html)`, which is a [standard Unix/Linux utility](https://en.wikipedia.org/wiki/Cron) for running programs at specified intervals.

:::{tip} `scrontab` vs `crontab`
If you are familiar with `crontab`, there are some important differences to note:
- The scheduled times for `scrontab` indicate when your job is *eligible* to start. They are not start times like in traditional Cron jobs.
- Jobs managed with `scrontab` won't start if an earlier iteration of the same job is still running. Cron will happily run multiple copies of a job at the same time.
- You have one `scrontab` file for the entire cluster, unlike `crontabs`, which are stored locally on each computer.
:::

## Set Up Your `scrontab`

:::{seealso}
{ref}`using-slurm`
:::

### Edit Your `scrontab`

To edit your `scrontab` file, run `scrontab -e`. If you prefer to use `nano` to edit files, run `EDITOR=nano scrontab -e`.

Lines that start with `#SCRON` are treated like the beginning of a new batch job and work like `#SBATCH` directives for batch jobs. Slurm will ignore `#SBATCH` directives in scripts that you run as `scrontab` jobs. You can use most common `sbatch` options just as you would when using Slurm. The first line after your `SCRON` directives specifies the schedule for your job and the command to run.

:::{note}
All of your `scrontab` jobs will start with your home directory as the working directory. You can change this with the `--chdir` Slurm option.
:::

## Cron syntax

Crontab's syntax is specified in five columns, which specify minutes, hours, days of the month, months, and days of the week. If you're new to crontab, it may be easiest to use a helper application to generate your cron date fields. Two popular options are [crontab-generator] and [cronhub.io]. Alternatively, you can use shorthand syntax such as `@hourly`, `@daily`, `@weekly`, `@monthly`, and `@yearly` instead of the five separate columns.

## What to Run

If you're running a script, it must be marked as executable. Jobs handled by `scrontab` do not run in a full login shell. Therefore, if you have customized your `.bashrc` file, you need to add the following line to your script to ensure that your environment is set up correctly:

:::{code} bash
source ~/.bashrc
:::

Note that the command specified in the `scrontab` file is executed via bash, NOT `sbatch`. You can list multiple commands separated by `;` and use other shell features, such as redirects. Additionally, any `#SBATCH` directives in executed scripts will be ignored. To use the `scrontab` file, you must use `#SCRON` instead.

::::{note}
Your `crontab` jobs will appear to have the same JobID every time they run until the next time you edit your `crontab` file. This means that only the most recent job will be logged to the default output file. If you want a deeper history, redirect the output in your scripts to filenames with more unique names, such as a date or timestamp. For example:

:::{code} bash
python my_script.py > $(date +"%Y-%m-%d")_myjob_scrontab.out
:::
::::

If you want to see the accounting of a job that was handled by crontab, for example job `12345`, run the following command to view the slurm accounting:

:::{code} bash
sacct --duplicates --jobs 12345
# or with short options
sacct -Dj 12345
:::

## Recurring Job Examples

### Running a Daily Simulation

This example demonstrates how to submit a 6-hour simulation that is eligible to start at 12:00 AM every day.

:::{code} bash
#SCRON --time 6:00:00
#SCRON --cpus-per-task 4
#SCRON --name "daily_sim"
#SCRON --chdir /home/netid/project
#SCRON -o my_simulations/%j-out.txt
@daily ./simulation_v2_final.sh
:::

### Running a Weekly Transfer Job

This example demonstrates how to submit a transfer script that is set to start every Wednesday at 8:00 PM.

:::{code} bash
#SCRON --time 1:00:00
#SCRON --partition transfer
#SCRON --chdir /home/netid/project/to_transfer
#SCRON -o transfer_log_%j.txt
0 20 * * 3 ./rclone_commands.sh
:::

### Capture output from each run in a separate file

By default, `crontab` overwrites the output file from the previous run when the same `jobid` is used. To avoid this, you can redirect the output to a file with a date-stamp.

:::{code} bash
0 20 * * 3 ./commands.sh > myjob_$(date +%Y%m%d%H%M).out
:::

[cronhub.io]: https://crontab.cronhub.io/
[crontab-generator]: http://crontab-generator.org/
