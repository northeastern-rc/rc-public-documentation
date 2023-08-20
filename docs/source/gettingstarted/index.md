# Getting Started

```{toctree}
:hidden:
:maxdepth: 3

get_access
accountmanager
connectingtocluster/index
```

Welcome to the Getting Started guide for our HPC! Here, you'll find essential information to kickstart your journey with our HPC cluster. This section is designed to assist both newcomers and experienced users in accessing and utilizing our computing resources.

::::{grid} 3
:::{grid-item-card} {ref}`getting-access`
Before you can use our HPC cluster, you need to request access.
:::
:::{grid-item-card} {ref}`account-manager`
Manage your account credentials and cluster environment.
:::
:::{grid-item-card} {ref}`connect-to-cluster`
Support for {ref}`connecting-on-mac` and {ref}`connecting-on-windows`.
:::
::::
(getting-access-index)=
## Getting Access

Follow the steps outlined below:

1. **Fill Out the Access Request Form**: [Instructions on requesting an HPC account], with all required details.
2. **Wait for Approval**: Our team will review your application and notify you via email.
3. **Accept Terms and Conditions**: Read and accept our usage policies.

:::{seealso}
{ref}`More about Getting Access <getting-access>`.
:::

(account-manager-index)=
## Account Manager

Managing your account effectively ensures a smooth experience with our system.

- **Reset Password**: Use the {ref}`passwordless-ssh` if needed.
- **Update Profile Information**: Keep your contact details up to date.
- **Monitor Usage**: Track your resource consumption (i.e., {ref}`Monitoring and Managing Jobs <slurm-monitoring-and-managing>`).

:::{seealso}
{ref}`More about Account Manager <account-manager>`.
:::
(connecting-to-the-index)=
## Connecting to Cluster
:::{seealso}
{ref}`connect-to-cluster`.
:::
Once you have access, you'll want to connect to the cluster to begin your work.

- **Using SSH**: Connect using SSH from a command-line interface. Here's an example for Linux/Mac users:
   ```bash
   ssh username@login.discovery.neu.edu
  ```
- Mac Users: {ref}`Connect a Mac <connecting-on-mac>` via terminal using SSH.
- Windows Users: You may use tools like PuTTY for SSH connections for {ref}`connecting-on-windows`.
- File Transfers: Use SCP or SFTP for secure file transfers: be sure use the transfer node when {ref}`transferring-data`. Other options for transferring files using a graphical interface include {ref}`file-explorer` or via {ref}`Globus <using-globus>`.
:::{code} bash
scp -r <source-path> <user-name>@xfer.discovery.neu.edu:<target-path>
:::
- Accessing GUI Applications: Details on using remote desktop or {ref}`X-forwarding <using-x11>`.

[Instructions on requesting an HPC account]: https://service.northeastern.edu/tech?id=kb_article_view&sysparm_article=KB0013989&sys_kb_id=e8381ac48764a594ba9a0fad0ebb3533&spa=1
