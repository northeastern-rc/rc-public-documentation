(getting-access)=

# Getting Access

## Request an account
:::{important}
If you previously had access to Discovery but are now working with a different PI, you should submit a [ServiceNow RC Access Request form] and enter the name of your current PI in the Sponsor field. This will link your account to your current PI and expedite updating your account with any of your current PI's resources on Discovery, such as shared storage or a private partition.
:::

:::{sidebar} Valid NU Credentials
Access to the cluster is limited to Northeastern affiliates with a valid NU username and password. Research Computing cannot create or renew Northeastern accounts. You must work with your sponsor to obtain or update your credentials.

For **non-Northeastern personnel**, request a Northeastern sponsored via [How do I submit a sponsored account request?]
:::

To access Discovery, you must first have an account. You can request an account through ServiceNow but need a Northeastern username and password. If you are new to the university or a visiting researcher, you should work with your sponsor to obtain a Northeastern username and password.



**To request an account, follow these steps:**

1. Visit the [ServiceNow RC Access Request form].
1. Complete the form, check the acknowledgment box, and submit it.

Your request may take up to 24 hours after your sponsor approves it (see Sponsor Approval Process below). You will receive an email confirmation when your access has been granted. Once you have access, if you are unfamiliar with Discovery, high-performance computing, or Linux, you may want to take one of our training courses. Visit the [Research Computing website] for more information about our training and services.

(instructor-access)=

### Sponsor Approval Process

:::{sidebar} PI and instructor access
If you are a PI, professor, or instructor at Northeastern and need access to the cluster, use the access form in the above procedure and enter your name in the `Sponsor Name` field.
:::

HPC users need a sponsor, usually a NU PI or professor, to approve their request. PIs, professors, and instructors can sponsor themselves. Students (undergraduate or graduate), visiting researchers, or staff members must have a sponsor approve their request. When you fill out the ServiceNow form, an email is sent to the specified sponsor upon submitting the request. Sponsors will receive email reminders until they approve the request through the link in the email to ServiceNow. We recommend letting your sponsor know to look for the email with the approval link before submitting an access request.

## Cluster Usage

**DO NOT USE** the login node for CPU-intensive activities, as this will impact the performance of this node for all cluster users. It will also not provide the best performance for the tasks you are trying to accomplish.

:::{seealso}
{ref}`connect-to-cluster`
:::

::::{important}
If you are attempting to run a job, you should move to a compute node. You can do this interactively using the `srun` command or non-interactively using the `sbatch` command.
:::{seealso}
{ref}`using-sbatch` and {ref}`using-srun` for more information.
:::

If you are attempting to transfer data, we have a dedicated transfer node that you should use.

:::{seealso}
{ref}`transferring-data`.
:::

[//]: # (If you have any questions or need further assistance, please email us at [rchelp@northeastern.edu] or book a consultation using the link on our [Consultation page].)
::::

## Routine Cluster Maintenance

Routine cluster maintenance is performed on the first Tuesday of each month. RC sends maintenance emails to inform users of upcoming maintenance window, a description of the maintenance, and how users will be affected.

:::{seealso}
Users can also check the maintenance status via [IT Maintenance and Status page].
:::

## MGHPCC annual shutdown

The Massachusetts Green High Performance Computing Center (MGHPCC) conducts an annual shutdown for maintenance work. During this shutdown, all RC-managed services are powered down and unavailable for approximately four days. RC will send frequent reminders leading up to the shutdown to ensure that users are able to plan accordingly.

## IT Statuspage

All routine cluster maintenance, emergency maintenance, and annual shutdown maintenance information will be posted to the [IT Statuspage]. Please subscribe to ensure you receive updates on the status of all ITS systems.

## Prepare for cluster maintenance

To ensure that your job scripts account for the scheduled shutdown period of the cluster, use the `t2sd` script in the `--time` option when submitting your jobs. This script calculates the remaining time until the cluster becomes unavailable and sets the appropriate time limit for your job. Here is an example of how to use it.

- If you usually use the `srun` command:

:::{code} bash
srun --time=$(t2sd) <srun args>
:::

- If you usually use the `sbatch` command to submit batch jobs:

:::{code} bash
sbatch --time=$(t2sd) script.sbatch
:::

Note that if you usually run your jobs on a partition with short time limits (e.g., debug or express), you only need to add the `$(t2sd)` option once it is closer to the start of the maintenance window. Use `$(t2sd)` only if the time remaining before the start of the maintenance period is less than the default time limit of the partition.

For instance, the default time limit for the express partition is 60 minutes. If you want to run a job on the express partition a day before the maintenance is scheduled to start, you would not need to add the `$(t2sd)` option. However, if you wanted to run your job on the express partition 2 hours before the maintenance start time, you would need to include the `$(t2sd)` option to account for the remaining time.

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


[Consultation page]: https://rc.northeastern.edu/support/consulting/
[Transferring Data]: https://rc-docs.northeastern.edu/en/latest/using-discovery/transferringdata.html
[research computing website]: https://rc.northeastern.edu/support/training/
[servicenow rc access request form]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0ae24596db535fc075892f17d496199c
[How do I submit a sponsored account request?]: https://service.northeastern.edu/tech?id=kb_article_view&sysparm_article=KB0013989&sys_kb_id=e8381ac48764a594ba9a0fad0ebb3533&spa=1
[rchelp@northeastern.edu]: mailto:rchelp@northeastern.edu
[IT Maintenance and Status]: https://northeastern.statuspage.io/
