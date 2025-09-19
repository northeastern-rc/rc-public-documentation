(project-terms)=

# Terminology

This page provides a quick explanation of the vocabulary used with the software to manage `/projects`.

(user-types)=

## User Types

Users are split into five types. The user type determines the user's access level for a research project both on the filesystem and our software to manage `/projects`. The five types in ascending order of access level:

1. **Data-custodian**: the data-custodian is an email address that will receive information related to quotas and updates about the workspace;  access to the cluster is not a requirement (N.B. this is an optional user type to have for a group).
1. **Guests**: guests of a research group are users that can read and execute within a project directory but not write.
1. **Members**: members of a research group can read, write, and execute, but they are unable to add other members to the research group through the software to manage `/projects`.
1. **Delegates**: delegates are members elevated by the PI that can add and remove other members.
1. **PI**: the PI is the owner of the research project and, therefore, they have full access.

:::{note}
To see all the available commands for the different user types check out {ref}`project-commands`.
:::

## TTL

At the inception of every project, we establish a `ttl` or "Time To Live", which indicates how long the project is guaranteed to be supported.

This `ttl` can be viewed by the PI at any point (see {ref}`commands-for-viewing`), and, once the `ttl` expires, Research Computing will email the PI and data-custodian to inquire about the status and continuation of the research project on the cluster.

:::{important}
Although a TTL exists for a research group, its purpose is not punitive or restrictive, but rather it is purely administrative -- enabling us to find out if the group is still active,  if PI needs to be changed as they may have left, etc.
:::
