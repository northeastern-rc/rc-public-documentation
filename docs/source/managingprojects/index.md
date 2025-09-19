(managing-projects)=
# Managing /Projects

```{toctree}
:hidden:
:maxdepth: 3

terminology
cheatsheet
commands
```

For our Explorer cluster we developed custom `/projects` management software to empower researchers, giving them full control of their research groups on the cluster. What does this entail?

* User-management: rather than having to fill out and wait upon an access ticket, a PI need only enter a command on the cluster, or the PI can delegate this task to elevated users.
* Guests: in addition to the unix research group, the software creates a `guest` group that allows read-only access to the project directory -- similarly be managed by the command-line.
* ACL-Management: the software negates the need for custom Access Control Lists (ACLs) and will provision the project directories with relevant ones applied.
* Email-management: the PI can set an additional email for correspondence concerning the group and workspace directory.

::::{grid} 1 1 2 2
:gutter: 2

:::{grid-item-card} {octicon}`repo;1.5em;sd-mr-1` Terminology
:link: terminology
:link-type: doc

Learn about the terminology used with this software to manage `/projects`.

+++
[Learn more »](terminology)
:::

:::{grid-item-card} {octicon}`command-palette;1.5em;sd-mr-1` Available Commands
:link: commands
:link-type: doc

Explore the commands available with the project-mangagement software.

+++
[Learn more »](commands)
:::

:::{grid-item-card} {octicon}`note;1.5em;sd-mr-1` Explorer Projects Cheatsheet
:link: cheatsheet
:link-type: doc

A one-page guide that provides all the information necessary on our software that manages `/projects`.
+++
[Learn more »](cheatsheet)
:::

::::
