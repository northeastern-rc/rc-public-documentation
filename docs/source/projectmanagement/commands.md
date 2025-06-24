(project-commands)=

# Commands

The commands for interacting with the project-management software can be thought of in four areas: viewing, adding, updating, and removing.

Every command below is detailed with the type of user able to run the command with respect to the project (for more information on user type see  {ref}`user-types`).

:::{note}
Every command below follows the form `project <project-name> ...`, and, apart from the name of your project, you can use tab-completion to help write the command.
:::

## Setup

In order to run a command, just as with checking your quota ({ref}`checking-your-quotas`), you must be on any node in the `short` partition. To launch a job on the short partition, run:

:::{code-block} bash
srun -p short --constraint=ib --pty bash
:::

(commands-for-viewing)=

## Viewing

To view the members of a research group, any _member_ of the group can run the following:
:::{code-block} bash
project <project_name> view members
:::

To view the delegates of a research group, any _delegate_ or the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> view delegates
:::

To view the guests of a research group, any _delegate_ or the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> view guests
:::

To view the emails we have for correspondening with a research group, the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> view groupemail
:::

To view the ttl of a research group, the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> view ttl
:::

## Adding

To add users to the members of a research group, any _delegate_ or the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> add members <user1,user2,etc.>
:::

To elevate users to be delegates of a research group,  the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> add delegates <user1,user2,etc.>
:::

To add guests to a research group,  the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> add guests <user1,user2,etc.>
:::

## Updating

To update the data-custodian for a research group,  the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> update groupemail <data_custodian_email>
:::

## Removing

To remove members from a research group, any _delegate_ or the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> remove members <user1,user2,etc.>
:::

To remove delegates  from a research group, the _PI_ of the group can run the following:
:::{code-block} bash
project <project_name> remove delegates <user1,user2,etc.>
:::
