(data-storage)=

# Data Storage Options

Research Computing is responsible for procuring and maintaining data storage options, including active and archive storage solutions. If you are affiliated with Northeastern, you can request one or more storage solutions to meet your needs. If you anticipate needing storage as part of a grant requirement, please [schedule a storage consultation] with an RC staff member to understand what storage options best meet your research needs.

If you find that you need more than the allotted complimentary storage, please refer to the [Research Projects Storage Space Policy] page for more information about Active and Archival storage costs.

## Active Storage

Two main storage systems are connected to Northeastern's HPC cluster: `/home` and `/scratch`; these options have specific quotas and limitations. The list below details the storage options available on the HPC cluster if you have an account. Every individual with an account has a `/home` and `/scratch`. While research groups can request additional storage on the `/work` storage system, `/work` storage is not currently provisioned for individuals.

:::{important}
The `/scratch` space is only for temporary storage; this storage is not backed up. Please review the `/scratch` policy on our [Scratch Space Policy page].
:::

**$HOME:** `/home/<username>` where `username` is your NU login, e.g., `/home/j.smith`
- **Description:** All users are automatically given a `/home` when their account is created. This storage is mainly intended for storing relatively small files such as script files, source code, and software installation files. Storage in `/home` is backed up and replicated. `/home` also has a small quota, so you should frequently [check your `/home` space usage](https://rc-docs.northeastern.edu/en/latest/best-practices/homequota.html). 
- **Quota:** 75GB

**Scratch:** `/scratch/<username>`
- **Description:** All users are automatically given a `/scratch` when their account is created. {term}`Scratch space` is a shared space for all users and is meant for temporary storage. **It is not backed up.** Data on `/scratch` should be moved to another location for permanent storage as soon as possible. The space in `/scratch` is [purged](https://rc-docs.northeastern.edu/en/latest/best-practices/homequota.html) on the first Tuesday of every month. 
- **Quota:** N/A

**Work:** `/work/<groupname>`
- **Description:** Research groups can request additional storage on `/work`. A PI can request this extra storage through the [New Storage Space Request]. This is permanent, persistent, and long-term storage for storing data actively used for research. It can be accessed by all members of the research group who have the necessary access permissions, facilitating collaboration and seamless sharing of data within the group.
- **Quota:** Each PI can request up to **35 TB** and **7.5 million inodes** of complimentary storage summed across all `/work` they own. We recommend [compressing directories in `/work`](https://rc-docs.northeastern.edu/en/latest/best-practices/workquota.html) if they are not in regular use. 
- **Access Request:** Students with research groups can request access to the PI’s storage on `/work`. To expedite the request process, we recommend that you inform the group owner that they will be receiving an email requesting their permission to grant you access to `/work` before you submit the request.

1. To request access to `/work`, students can either create a  [ServiceNow ticket with RC] or email [rchelp@northeastern.edu](mailto:rchelp%40northeastern.edu) to automatically generate a ticket in ServiceNow. Please include both the storage space name and the PI’s name.
1. Once you have been added to the Unix group for the space on `/work`, please close all open connections to the HPC and log in again for the changes to reflect on your end. As you know, UNIX groups are assigned at login time, and this step ensures that your access privileges are updated accordingly. To confirm you have been added to the group, you can run the command `groups`.
- **Default Permission:** By default, users are given read and write access when added to `/work`. However, specific permissions might be granted at the PI’s request.


##  Archival Storage

**NAME:** `NESE`
- **Description:** This is archival, non-permanent storage intended for researchers needing a long-term storage option for their data. We have no free options for NESE archival storage.
- **Quota:** A PI can request this storage through the [New Storage Space Request].

[How do I connect to Northeastern VPN?]: https://service.northeastern.edu/tech?id=kb_article_view&sysparm_article=KB000017951
[New Storage Space Request]: https://bit.ly/NURC-NewStorage
[OneDrive]: https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012764

[Scratch Space Policy page]: https://rc.northeastern.edu/policies-scratch-space-policy/
[schedule a storage consultation]: https://rc.northeastern.edu/support/gettinghelp/

[ServiceNow ticket with RC]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0a0bfc5adb9f1fc075892f17d4961993
[Sharepoint]: https://service.northeastern.edu/tech?id=kb_article_view&sysparm_article=KB0012695
[submitting a ticket]: https://bit.ly/NURC-Assistance
[Research Projects Storage Space Policy]: https://rc.northeastern.edu/research-projects-storage-space-policy/
