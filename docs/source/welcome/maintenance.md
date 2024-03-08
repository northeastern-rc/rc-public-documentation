(regular_maintenance)=

# Routine Cluster Maintenance

Routine cluster maintenance is performed on the first Tuesday of each month. RC sends maintenance emails to inform users of upcoming maintenance window, a description of the maintenance, and how users will be affected.

:::{seealso}
Users can also check the maintenance status via [ITS Maintenance and Status] page.
:::
(annual_shutdown)=
## MGHPCC Annual Shutdown

The Massachusetts Green High Performance Computing Center (MGHPCC) conducts an annual shutdown for maintenance work. During this shutdown, all RC-managed services are powered down and unavailable for approximately four days. RC will send frequent reminders leading up to the shutdown to ensure that users are able to plan accordingly.

## ITS Statuspage

All routine cluster maintenance, emergency maintenance, and annual shutdown maintenance information will be posted to the [ITS Maintenance and Status]. Please subscribe to ensure you receive updates on the status of all ITS systems.

## Preparing Cluster Maintenance

To ensure that your job scripts account for the scheduled shutdown period of the cluster, use the `--time` option when submitting your jobs. If maintenance is set to start in less than 24 hours from when you submit your job, be sure to ask for less than 24 hours or time with your srun command.

- If you usually use the `srun` command:

:::{code} bash
srun --time=12:00:00 <srun args>
:::

- If you usually use the `sbatch` command to submit batch jobs:

:::{code} bash
sbatch --time=12:00:00 script.sbatch
:::

Note that if you usually run your jobs on a partition with short time limits (e.g., debug or express), you only need to ensure that those time limits (20 and 60 minutes, respectively) exist before the scheduled start of maintenance.

:::{seealso}
{ref}`partition-names` for more information about available partitions.
:::

:::{important}
Ensuring that your job scripts account for the scheduled maintenance of the cluster is applicable to jobs running on *private* partitions as well.
:::

Moreover, we can help you set up a default and maximum time configuration on your partition. This configuration can significantly alleviate the issues you may experience with job runtime. By defining default and maximum time limits, you can establish a predefined window for job execution without explicitly specifying the runtime for each job.

However, note that even with the default and maximum time configuration in place, there will always be a time equal to the default time limit where explicitly specifying the job's runtime becomes helpful. This allows for better control and management of job scheduling within the available resources.

If you want to set up the default and maximum time configuration on your partition or have any concerns or questions regarding job runtime management, please let us know. We are here to assist you further.

Following these instructions ensures that your job scripts consider the maintenance period and set appropriate time limits. If you have any further questions, feel free to ask!

[ITS Maintenance and Status]: https://northeastern.statuspage.io/