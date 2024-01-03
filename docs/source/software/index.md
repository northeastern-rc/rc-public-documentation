(software-overview)=
# Software Overview
```{toctree}
:hidden:
:maxdepth: 3

System Wide <systemwide/index>
Package Managers <packagemanagers/index>
From Source <fromsource/index>
```
## Cluster Software
<!-- ::::{grid} 2

:::{grid-item-card} {ref}`system-wide-overview`
Cluster's nuts and bolts.
:::
:::{grid-item-card} {ref}`package-managers`
Allow you to build specific environments.
:::
:::{grid-item-card} {ref}`from-source`
Using `make` or `cmake`.
:::
:::: -->

::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`globe;1.5em;screen-full` System-wide Software
:link: /systemwide
:link-type: doc

Cluster’s nuts and bolts.

+++
[Learn more »](software/systemwide)
:::

:::{grid-item-card} {octicon}`package;1.5em;sd-mr-1` Package Managers
:link: /packagemanagers
:link-type: doc

Allow you to build specific environments.

+++
[Learn more »](software/packagemanagers)
:::

:::{grid-item-card} {octicon}`desktop-download;1.5em;sd-mr-1` From Source
:link: /fromsource
:link-type: doc

Using make or cmake.

+++
[Learn more »](software/fromsource)
:::

::::

---
The cluster offers you many options for working with software. Two of the easiest and most convenient ways are using the `module` command on the {ref}`command line <command-line>` and the {ref}`interactive-ood-apps` web portal.

::::{sidebar}
:::{seealso}
{ref}`More about using module. <using-module>`
:::
::::

If you need a specific software package, first check to see if it is already available through one of the preinstalled modules on the cluster. The Research Computing team adds new modules regularly, so use the `module avail` command to view the most up-to-date list.

## Requesting Software Installation Assistance
If the software you need is not a module on the cluster, cannot be installed via Spack, and is not available through another way of self-installation (e.g., `make`), please submit a [ServiceNow software request ticket].

:::{note}
Some packages might not be able to be installed on the cluster due to hardware incompatibility issues.
:::

Following these steps, users should be able to install most software packages on their own. However, always refer to the specific software's documentation, as steps can vary. If you run into issues or need help, please contact support.

[servicenow software request ticket]: https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=777c510bdbebd340a37cd206ca9619b0
