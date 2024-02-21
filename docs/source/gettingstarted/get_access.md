(getting-access)=

# Getting Access

(request-an-account)=
## Request Account
:::{important}
If you previously had access to Discovery but are now working with a different PI, you should submit a [ServiceNow Access Request] form and enter the name of your current PI in the Sponsor field. This will link your account to your current PI and expedite updating your account with any of your current PI's resources on Discovery, such as shared storage or a private partition.
:::

:::{sidebar} Valid NU Credentials
Access to the cluster is limited to Northeastern affiliates with a valid NU username and password. Research Computing cannot create or renew Northeastern accounts. You must work with your sponsor to obtain or update your credentials.

For **non-Northeastern personnel**, request a Northeastern sponsored account via a [sponsored account request].
:::

To access Discovery, you must first have an account. You can request an account through ServiceNow but need a Northeastern username and password. If you are new to the university or a visiting researcher, you should work with your sponsor to obtain a Northeastern username and password.

**To request an account, follow these steps:**

1. Visit the [ServiceNow Access Request] form.
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
::::



[Consultation page]: https://rc.northeastern.edu/support/consulting/
[Transferring Data]: https://rc-docs.northeastern.edu/en/latest/using-discovery/transferringdata.html
[research computing website]: https://rc.northeastern.edu/support/training/
[ServiceNow Access Request]: https://bit.ly/NURC-AccessRequest
[sponsored account request]: https://service.northeastern.edu/tech?id=kb_article_view;amp;table=kb_knowledge;amp;sys_kb_id=f617b57c97ed7590350cb9cfe153afb5
[rchelp@northeastern.edu]: mailto:rchelp@northeastern.edu

