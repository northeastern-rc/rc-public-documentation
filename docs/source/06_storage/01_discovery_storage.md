(discovery-storage)=

# Data Storage Options

The Research Computing (RC) team is responsible for the procurement and ongoing maintenance of several data storage options,
including active and archive storage solutions. If you are affiliated with Northeastern, you can request one or more storage
solutions to meet your storage needs. If you anticipate needing storage as part of a grant requirement, please
[schedule a storage consultation with a Research Computing staff member] to understand what storage options would best meet your research needs.

::::::{tab-set}
:::::{tab-item} Data Storage

%## Data Storage
There are two main storage systems connected to Northeastern's HPC cluster: `/home` and `/scratch`; these options have specific quotas and limitations. The list below details the storage options available to you on the HPC cluster by having an account. Every individual with an account has both a `/home` and `/scratch` directory. While research groups can request additional storage on the `/work` storage system, `/work` storage is not currently provisioned to individuals.

:::{important}
The `/scratch` space is only for temporary storage; this storage is not backed up, and there is a purge policy for data older than 28 days. Please review the `/scratch` policy on our [Policy page].
:::

**NAME:** `/home/<yourusername>` where `yourusername` is your username, e.g., `/home/j.smith`
: - **DESCRIPTION:** All users are given a `/home` directory automatically when their account is created. This storage is mainly intended for storing relatively small files such as script files, source code, and software installation files. While `/home` is permanent storage that is backed up and replicated, `/home` is not performant storage. `/home` also has a small quota, so you should frequently check your space usage (use a command such as, `du -h /home/<yourusername>` where `<yourusername>` is your user name, to see the total space usage). For running jobs and directing output files, you should use your `/scratch` directory.

- **QUOTA:** 75GB

**NAME:** `/scratch/<yourusername>`
: - **DESCRIPTION:** All users are given a `/scratch` directory automatically when their account is created. Scratch is a shared space for all users. The total storage available is 1.8PB; however, while this is performant storage, it is for temporary use only. **It is not backed up.** Data on `/scratch` should be moved as soon as possible to another location for permanent storage. You should run your jobs from `/scratch` and direct your output files to your `/scratch`directory for best performance, but it is best practice to move your files off of scratch to avoid any potential data loss.

- **QUOTA:** N/A

**NAME:** `/work/<groupname>`
: - **DESCRIPTION:** Research groups can request additional storage on `/work`. A PI can request this extra storage through the [New Storage Space request]. This is a performant, persistent, and long-term storage that is meant for storing data being actively used for research. `/work` can be accessed by all members of the research group who have access permissions to this directory.

- **QUOTA:** Each group can request up to **35TB** of free storage across all supplemental storage tiers: `/work/<groupname>` and `/nese`.

:::{note}
The `/research` storage tier is no longer provided. Please contact Research Computing if you are a former user of `/research` and have questions or issues related to `/research` by [submitting a ticket]. Other storage options include `/work`, [Sharepoint], and [OneDrive].
:::
:::::
:::::{tab-item} Archival Storage
%## Archival Storage

**NAME:** `/nese`
: - **DESCRIPTION:** This is archival, non-performant storage intended for researchers who need to have a long-term storage option for their data.

- **QUOTA:** Each group can request up to **35TB** of free storage across all supplemental storage tiers: `/work/<groupname>` and `/nese`.

:::{important}
If you are not connected to the campus internet, you must be connected to the university's VPN (GlobalProtect) before you can access the `/nese` system. You can find detailed information about downloading and using the GlobalProtect VPN in the [FAQ: VPN and remote access].
:::
:::::
::::::

[FAQ: VPN and remote access]: https://service.northeastern.edu/tech?id=kb_article_view&sysparm_article=KB0013983>
[New Storage Space request]: https://bit.ly/NURC-NewStorage
[OneDrive]: https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012764
[Policy page]: https://rc.northeastern.edu/policy/
[schedule a storage consultation with a Research Computing staff member]: https://rc.northeastern.edu/support/consulting
[Sharepoint]: https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012695
[submitting a ticket]: https://bit.ly/NURC-Assistance
