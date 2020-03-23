.. _discovery_storage:

****************************
Storage Options on Discovery
****************************

There are several storage options available to you on Discovery. These options have specific quotas and limitations.
The list below details the storage options available to you if you have an account on Discovery. These are storage options
that are connected to Discovery and you should use when working on Discovery.

**NAME:** ``/home/<yourusername>`` where ``yourusername`` is your username, e.g. ``/home/j.smith``
 - **DESCRIPTION:** You are given a ``/home`` directory automatically when your Discovery account is created. This storage is mainly intended for environment tools and very low utilization. It is not performant storage.
 - **QUOTA:** 50GB

**NAME:** ``/scratch/<yourusername>``
 - **DESCRIPTION:** You are given a ``/scratch`` directory automatically when your Discovery account is created. This is a shared space for all users. The total storage available is 1.8PB; however, while this is performant storage, it is for temporary use only. It is not backed up. Data on ``/scratch`` should be moved as soon as possible to another location for permanent storage.
 - **QUOTA:** N/A

**NAME:** ``/work/<yourusername>``
 - **DESCRIPTION:** In addition to your automatically provided ``/home`` and ``/scratch`` directories, individuals and research groups can additional storage on ``/work``. You can request this extra storage through the `New Storage request <https://northeastern.service-now.com/research?id=sc_cat_item&sys_id=891235d31b20c0502dafc8415b4bcb0e>`_ on ServiceNow. Note that currently this storage tier is not performant storage.

 .. note::
    You can also request additional storage if needed. See :ref:`general_storage` for details about the storage options that are not connected to Discovery, and that are available to anyone affiliated with Northeastern University.
