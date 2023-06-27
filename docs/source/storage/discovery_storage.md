(discovery-storage)=

# Data Storage Options

RC is responsible for the procurement and ongoing maintenance of several data storage options, including active, and archive storage solutions. If you are affiliated with Northeastern, you can request one or more storage solutions to meet your storage needs. If you anticipate needing storage as part of a grant requirement, please [schedule a storage consultation] with an RC staff member to understand what storage options would best meet your research needs.

## Active Storage

There are two main storage systems connected to Northeastern's HPC cluster: `/home` and `/scratch`; these options have specific quotas and limitations. The list below details the storage options available to you on the HPC cluster by having an account. Every individual with an account has both a `/home` and `/scratch`. While research groups can request additional storage on the `/work` storage system, `/work` storage is not currently provisioned to individuals.

:::{important}
The `/scratch` space is only for temporary storage; this storage is not backed up, and there is a purge policy for data older than 28 days. Please review the `/scratch` policy on our [Policy page].
:::

**$HOME:** `/home/<username>` where `username` is your NU login, e.g., `/home/j.smith`
- **Description:** All users are given a `/home` automatically when their account is created. This storage is mainly intended for storing relatively small files such as script files, source code, and software installation files. While `/home` is permanent storage that is backed up and replicated, `/home` is not performant storage. `/home` also has a small quota, so you should frequently check your space usage (use a command such as, `du -h /home/<yourusername>` where `<yourusername>` is your username, to see the total space usage). For running jobs and directing output files, you should use your `/scratch`.
- **Quota:** 75GB

**Scratch:** `/scratch/<username>`
- **Description:** All users are given a `/scratch` automatically when their account is created. Scratch is a shared space for all users. The total storage available is 1.8PB; however, while this is performant storage, it is for temporary use only. **It is not backed up.** Data on `/scratch` should be moved as soon as possible to another location for permanent storage. You should run your jobs from and direct output to your `/scratch` for best performance. However, it is best practice to move your files off of scratch to avoid any potential data loss.
- **Quota:** N/A

**Work:** `/work/<groupname>`
- **Description:** Research groups can request additional storage on `/work`. A PI can request this extra storage through the [New Storage Space request]. This is a performant, persistent, and long-term storage that is meant for storing data being actively used for research. It can be accessed by all members of the research group who have necessary access permissions, facilitating collaboration and seamless sharing of data within the group.
- **Quota:** Each group can request up to **35TB** of free storage across all supplemental storage tiers: `/work/<groupname>` and `/nese`.
- **Access Request:** Students with research groups can request access to the PI’s storage on `/work`. To expedite the request process, we recommend that you inform the group owner they will be receiving an email requesting their permission to grant you access to `/work` before you submit the request.

1. To request access to `/work`, students can either create a  [ServiceNow ticket with RC] or email [rchelp@northeastern.edu](mailto:rchelp%40northeastern.edu) to automatically generate a ticket in ServiceNow. Please include both the storage space name and the PI’s name.
1. Once you have been added to the unix group for the space on `/work`, please ensure to close all open connections to the HPC and login again for the changes to reflect on your end. Please note that UNIX groups are assigned at login time, and this step ensures that your access privileges are updated accordingly. To confirm you have been added to the group, you can run the command `groups`.
- **Default Permission:** By default, users are given read and write access when added to `/work`. However, specific permissions might be granted at the PI’s request.


:::{attention}
The `/research` storage tier is no longer provided. Please contact Research Computing if you are a former user of `/research` and have questions or issues related to `/research` by [submitting a ticket]. Other storage options include `/work`, [Sharepoint], and [OneDrive].
:::

##  Archival Storage

:::{important}
If you are not connected to the campus internet, you must be connected to the university's VPN (GlobalProtect) before you can access the `/nese` system. You can find detailed information about downloading and using the GlobalProtect VPN in the [FAQ: VPN and remote access].
:::

**NAME:** `/nese`
- **Description:** This is archival, non-performant storage intended for researchers who need to have a long-term storage option for their data.
- **Quota:** Each group can request up to **35TB** of free storage across all supplemental storage tiers: `/work/<groupname>` and `/nese`.


[FAQ: VPN and remote access]: https://service.northeastern.edu/tech?id=kb_article_view&sysparm_article=KB0013983>
[New Storage Space request]: https://bit.ly/NURC-NewStorage
[OneDrive]: https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012764
[Policy page]: https://rc.northeastern.edu/policy/
[schedule a storage consultation]: https://rc.northeastern.edu/support/consulting
[ServiceNow ticket with RC]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0a0bfc5adb9f1fc075892f17d4961993
[Sharepoint]: https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012695
[submitting a ticket]: https://bit.ly/NURC-Assistance
