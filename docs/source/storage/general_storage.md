(general-storage)=

# Storage Options

The Research Computing (RC) team is responsible for the procurement and ongoing maintenance of several data storage options, including active and archive storage solutions. If you are affiliated with Northeastern, you can request one or more storage solutions to meet your storage needs. It is highly recommended that if you anticipate needing storage as part of a grant requirement, schedule a consultation with a Research Computing staff member to understand what storage options would best meet your research needs. You can schedule an online consultation on the [RC website](https://rc.northeastern.edu/support/consulting).

:::{note}
If you have an account on Discovery, see [Storage Accessible on Discovery](discovery_storage) for details on the storage available to you specifically for use with Discovery's compute resources. The options listed below are not connected to Discovery.
:::

**NAME:** `/research`
: - **DESCRIPTION:** This storage tier is intended to be a repository for data derived from equipment such as lab machines, instruments, etc. The performance capabilities are not intended for parallel or high performance workloads. Data are backed up and a second copy is created. You can request storage on `/research` by submitting a [New Storage Space request](https://bit.ly/NURC-NewStorage). See the section {ref}`connecting-to-research` below for information on how to connect to this storage.

- **QUOTA:** Each group can request up to **35TB** of free storage across all supplemental storage tiers: `/work/<groupname>`, `/research` () and `/nese`.

**NAME:** `/nese`
: - **DESCRIPTION:** This is archival, non-performant storage that is intended for researchers who need to have a long-term storage option for their data.

- **QUOTA:** Each group can request up to **35TB** of free storage across all supplemental storage tiers: `/work/<groupname>`, `/research` and `/nese`.

% **NAME:** ``/secure``
% - **DESCRIPTION:** Secure data storage is restricted to data that must be stored in a secure,
% encrypted server, such as personally identifiable information (PII) data.
% You should first set up a consultation with a Research Computing staff member using the link above to
% determine if your data requires secure storage before requesting it.

:::{important}
If you are not connected to the campus internet, you must be connected to the university's VPN (GlobalProtect) before you can access these storage systems. You can find detailed information about downloading and using the GlobalProtect VPN in the [ServiceNow Knowledge Base].
:::

(connecting-to-research)=

## Connecting to `/research`

After you have received notification that your shared storage folder on `/research` is ready for you to use, you
can connect to it on your laptop. Use the following procedures to connect to `/research` from either a Windows PC or a Macbook.
If you are not on the campus internet, you will need to first be connected to Northeastern VPN before you can connect to `/research`.

:::::{tab-set}
::::{tab-item} Windows

1. Open _File Explorer_.
1. In the left pane, select _This PC_.
1. On the _Computer_ tab, select _Map network drive_.
1. Select any letter not currently mapped to a drive. It does not matter what letter.
1. In the _Folder_ box, type `\\nunet.neu.edu\rc-shares\<sharename>`, where `<sharename>` is the name of your shared storage. If you want this drive to reconnect automatically every time you log in, check Reconnect at sign in.
1. Click Finish. Your shared folder now be available in File Explorer.

::::
::::{tab-item} Mac
1. Click the _Finder_ icon, and in the _Finder_ window, select _Go_, then click _Connect to Server_.
1. In the _Server Address_ field type `smb://nunet.neu.edu/rc-shares/<sharename>` where `<sharename>` is the name of the share you want to connect to.
1. Click _Connect_.
1. If you are prompted to enter your name and password for the nunet server, select _Connect as Registered User_, in the _Name_ field type `NUNET\<yourusername>`, (where `<yourusername>` is your NU username) and type your NU password in the _Password_ field. If you want to connect to /research automatically when you log in to your computer, select _Remember this password in my keychain_.
1. Click _Connect_. Your share should appear as a folder in the Finder window.
::::
:::::

[ServiceNow Knowledge Base]: https://service.northeastern.edu/tech?id=kb_article&sys_id=4701e07adb93485084ba5595ce9619a9