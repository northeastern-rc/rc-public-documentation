(getting-access)=

# Getting Access

(id1)=

## Request an account

To access Discovery, you must first have an account. You can request an account through ServiceNow but need a Northeastern username and password. If you are new to the university or a visiting researcher, you should work with your sponsor to obtain a Northeastern username and password.

:::{important}
If you previously had access to Discovery but are now working with a different PI, you should submit a [ServiceNow RC Access Request form] and enter the name of your current PI in the Sponsor field. This will link your account to your current PI and expedite updating your account with any of your current PI's resources on Discovery, such as shared storage or a private partition.
:::

:::{sidebar} Valid NU Credentials
Access to the cluster is limited to Northeastern affiliates with a valid NU username and password. Research Computing cannot create or renew Northeastern accounts. You must work with your sponsor to obtain or update your credentials.

For **non-Northeastern personnel**, request a Northeastern sponsored account using this [kb article].
:::

**To request an account, follow these steps:**

1. Visit the [ServiceNow RC Access Request form].
1. Complete the form, check the acknowledgment box, and submit it.

Your request may take up to 24 hours after your sponsor approves it (see Sponsor Approval Process below). You will receive an email confirmation when your access has been granted. Once you have access, if you are unfamiliar with Discovery, high-performance computing, or Linux, you may want to take one of our training courses. Visit the [Research Computing website] for more information about our training and services.

:::{sidebar} PI and instructor access
If you are a PI, professor, or instructor at Northeastern and need access to the cluster, use the access form in the above procedure and enter your name in the `Sponsor Name` field.
:::

(instructor-access)=

### Sponsor Approval Process

HPC users need a sponsor, usually a NU PI or professor, to approve their request. PIs, professors, and instructors can sponsor themselves. Students (undergraduate or graduate), visiting researchers, or staff members must have a sponsor approve their request. When you fill out the ServiceNow form, an email is sent to the specified sponsor upon submitting the request. Sponsors will receive email reminders until they approve the request through the link in the email to ServiceNow. We recommend letting your sponsor know to look for the email with the approval link before submitting an access request.

## Cluster Maintenance
To ensure that your job scripts account for the scheduled shutdown period of the cluster, use the `t2sd` script in the `--time` option when submitting your jobs. This script calculates the remaining time until the cluster becomes unavailable and sets the appropriate time limit for your job. Here's an example of how to use it.

- If you usually use the `srun` command:

:::{code} bash
srun --time=$(t2sd) <srun args>
:::

- If you usually use the `sbatch` command to submit batch jobs:

:::{code} bash
sbatch --time=$(t2sd) script.sbatch
:::

Note that if you usually run your jobs on a partition with short time limits (e.g., debug or express), you only need to add the `$(t2sd)` option once it's closer to the start of the maintenance window. Use `$(t2sd)` only if the time remaining before the start of the maintenance period is less than the default time limit of the partition.

For instance, the default time limit for the express partition is 60 minutes. If you want to run a job on the express partition at 5 a.m. on June 1, you wouldn't need to add the `$(t2sd)` option. However, if you wanted to run a job at 7:30 a.m. on June 1 on the express partition, you would need to include the `$(t2sd)` option to account for the remaining time.

:::{seealso}
{ref}`partition-names` for more information about available partitions.
:::

Moreover, we can help you set up a default and maximum time configuration on your partition. This configuration can significantly alleviate the issues you may experience with job runtime. By defining default and maximum time limits, you can establish a predefined window for job execution without explicitly specifying the runtime for each job.

However, note that even with the default and maximum time configuration in place, there will always be a time equal to the default time limit where explicitly specifying the job's runtime becomes helpful. This allows for better control and management of job scheduling within the available resources.

If you want to set up the default and maximum time configuration on your partition or have any concerns or questions regarding job runtime management, please let us know. We are here to assist you further.

Following these instructions ensures that your job scripts consider the maintenance period and set appropriate time limits. If you have any further questions, feel free to ask!

[research computing website]: https://rc.northeastern.edu/support/training/
[servicenow rc access request form]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0ae24596db535fc075892f17d496199c
[kb article]: https://service.northeastern.edu/tech?id=kb_article_view&sysparm_article=KB0013989&sys_kb_id=e8381ac48764a594ba9a0fad0ebb3533&spa=1
