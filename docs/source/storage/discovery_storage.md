(discovery-storage)=

# Data Storage Options

RC is responsible for procuring and maintaining several data storage options, including active and archive storage solutions. If affiliated with Northeastern University, you can request one or more storage solutions to meet your needs. If you anticipate needing storage as part of a grant requirement, please [schedule a storage consultation] with an RC staff member to understand what storage options best meet your research needs.

## Active Storage

**Updated 2023-07-18**

Two main storage systems are connected to Northeastern's HPC cluster: `/home` and `/scratch`; these options have specific quotas and limitations. The list below details the storage options available on the HPC cluster if you have an account. Every individual with an account has a `/home` and `/scratch`. While research groups can request additional storage on the `/work` storage system, `/work` storage is not currently provisioned for individuals.

:::{important}
The `/scratch` space is only for temporary storage; this storage is not backed up, and there is a purge policy for data older than 28 days. Please review the `/scratch` policy on our [Policy page].
:::

`/home/$USER`
- **Description:** All users are automatically given a `/home` when their account is created. This storage is mainly intended for storing relatively small files such as script files, source code, and software installation files. While `/home` is permanent storage backed up and replicated, `/home` is not performant storage. `/home` also has a small quota, so you should frequently check your space usage (use a command such as `du -h /home/$USER` to see the total space usage). For running jobs and directing output files, you should use your `/scratch`.
- **Storage Quota:** 75GB
- **File Quota:** 2,500,000

`/scratch/$USER`
- **Description:** All users are automatically given a `/scratch` when their account is created. Scratch is a shared space for all users. The total storage available is 1.8PB; however, while this is performant, it is for temporary use only. **It is not backed up.** Data on `/scratch` should be moved to another location for permanent storage as soon as possible. You should run your jobs from and direct output to your `/scratch` for best performance. However, moving your files from scratch is the best practice to avoid potential data loss.
- **Storage Quota:** N/A
- **File Quota:**

`/work/<project-name>`
- **Description:** Research groups can request additional storage on `/work`. A PI can request this extra storage through the [New Storage Space request]. This is performant, persistent, and long-term storage for storing data actively used for research. It can be accessed by all members of the research group who have necessary access permissions, facilitating collaboration and seamless sharing of data within the group.
- **Quota:** Each PI can request up to **35TB** of free storage across all supplemental storage tiers: `/work/<project-name>` and the archival space.
- **File Quota:**

:::{note}
**Access Request:** Students part of research groups can request access to the PI’s storage on `/work`. To expedite the request process, we recommend that you inform the group owner they will be receiving an email requesting their permission to grant you access to `/work` before you submit the request.

1. To request access to `/work`, students can either create a [ServiceNow ticket with RC] or email [rchelp@northeastern.edu](mailto:rchelp%40northeastern.edu) to automatically generate a ticket in ServiceNow. Please include both the storage space name and the PI’s name.
1. Once you have been added to the Unix group for the space on `/work`, please close all open connections to the HPC and log in again for the changes to reflect on your end. On Open OnDemand, under the `Develop` drop-down, select `Restart Web Server` to update your Unix groups. Just so you know, Unix groups are assigned at login time, and this step makes sure that your access privileges are updated accordingly. To confirm you have been added to the group, you can run the command `groups` on the terminal.
:::

:::{attention}
The `/research` storage tier is no longer provided. Please contact Research Computing if you are a former user of `/research` and have questions or issues related to `/research` by [submitting a ticket]. Other storage options include `/work`, [Sharepoint], and [OneDrive].
:::

## Archival Storage

Two types of archival storage are offered: archival disk and archival tape. These are non-performant storage options intended for researchers needing long-term storage options for their data. These storage options utilize Globus to transfer data to and from the archival system. For more information on using Globus, please refer to {ref}`using-globus`.

:::{attention}
**Quota:** Each PI can request up to **35TB** of free storage across all supplemental storage tiers: `/work/<project-name>` and the archival space.
:::

[FAQ: VPN and remote access]: https://service.northeastern.edu/tech?id=kb_article_view&sysparm_article=KB0013983>
[New Storage Space request]: https://bit.ly/NURC-NewStorage
[OneDrive]: https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012764
[Policy page]: https://rc.northeastern.edu/policy/
[schedule a storage consultation]: https://rc.northeastern.edu/support/consulting
[ServiceNow ticket with RC]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0a0bfc5adb9f1fc075892f17d4961993
[Sharepoint]: https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012695
[submitting a ticket]: https://bit.ly/NURC-Assistance
