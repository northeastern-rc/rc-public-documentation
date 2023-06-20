.. _discovery_storage:

*********************************
Storage Accessible on  Discovery
*********************************
There are two main storage systems connected to Discovery: /home and /scratch. These options have specific quotas and limitations.
The list below details the storage options available to you on Discovery if you have an account on Discovery. These are storage options
that are connected to Discovery, and you should use when working on Discovery. Every individual with an account on Discovery has
both a /home and /scratch directory. Research groups can request additional storage on the /work storage system. Note that currently
/work storage is not provisioned to individuals.

.. important::
   The /scratch space is only for temporary storage. It is not backed up, and there is a purge policy for data older than 28 days on /scratch. Please review
   the /scratch policy on our Policy page: https://rc.northeastern.edu/policy/

**NAME:** ``/home/<yourusername>`` where ``yourusername`` is your username, e.g. ``/home/j.smith``
 - **DESCRIPTION:** You are given a ``/home`` directory automatically when your Discovery account is created. This storage is mainly intended for storing relatively small files such as script files, source code, software installation files, and other small files that you need for your work on Discovery. While it is permanent storage that is backed up and replicated, it is not performant storage. It also has a small quota, so you should frequently check your space usage (use a command such as ``du -h /home/<yourusername>`` where ``<yourusername>`` is your user name, to see the total space usage). For running jobs and directing output files, you should use your ``/scratch`` directory.
 - **QUOTA:** 75GB

**NAME:** ``/scratch/<yourusername>``
 - **DESCRIPTION:** You are given a ``/scratch`` directory automatically when your Discovery account is created. Scratch is a shared space for all users. The total storage available is 1.8PB; however, while this is performant storage, it is for temporary use only. **It is not backed up.** Data on ``/scratch`` should be moved as soon as possible to another location for permanent storage. You should run your jobs from ``/scratch`` and direct your output files to your ``/scratch`` directory for best performance, but it is best practice to move your files off of scratch to avoid any potential data loss.
 - **QUOTA:** N/A

**NAME:** ``/work/<groupname>``
 - **DESCRIPTION:** Research groups can request additional storage on ``/work``. A PI can request this extra storage through the `New Storage Space request <https://bit.ly/NURC-NewStorage>`_ . This is a performant, persistent, and long-term storage that is meant for storing data being actively used for research. It can be accessed by all members of the research group who have necessary access permissions, facilitating collaboration and seamless sharing of data within the group. 
 - **REQUESTING ACCESS:** Students working with research groups can request access to the PI’s space on ``/work``. To expedite the request process, we recommend that you inform the group owner they will be receiving an email requesting their permission to grant you access to ``/work`` before you submit the request.
  
   1. To request access to ``/work``, students can either create a  `ServiceNow ticket with RC <https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0a0bfc5adb9f1fc075892f17d4961993>`_ or send an email to rchelp@northeastern.edu to automatically generate a ticket in ServiceNow. Please include both the storage space name and the PI’s name.
   2. Once you have been added to the unix group for the space on ``/work``, please ensure to close all open connections to discovery and login again for the changes to reflect on your end. Please note that UNIX groups are assigned at login time, and this step ensures that your access privileges are updated accordingly. To confirm you have been added to the group, you can run the command ``groups``.
 - **DEFAULT PERMISSIONS:** By default, users are given read and write access when added to ``/work``. However, specific permissions might be granted at the PI’s request.
   
 .. note::
  Your group can also request additional general data storage if needed. See :ref:general_storage for details about the storage options that are not associated with Discovery but are available to anyone affiliated with Northeastern University. Each group can request up to 35TB of free storage across all supplemental storage tiers: /work, /research and /nese.
