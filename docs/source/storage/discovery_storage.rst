.. _discovery_storage:

*********************************
Data Storage Options
*********************************
The Research Computing (RC) team is responsible for the procurement and ongoing maintenance of several data storage options, 
including active and archive storage solutions. If you are affiliated with Northeastern, you can request one or more storage 
solutions to meet your storage needs. It is highly recommended that if you anticipate needing storage as part of a grant requirement,
`schedule a consultation with a Research Computing staff member <https://rc.northeastern.edu/support/consulting>`_ to understand what
storage options would best meet your research needs.

Data Storage
==================================

There are two main storage systems connected to Discovery: ``/home`` and ``/scratch``. These options have specific quotas and limitations.
The list below details the storage options available to you on Discovery if you have an account on Discovery. These are storage options
that are connected to Discovery, and you should use when working on Discovery. Every individual with an account on Discovery has
both a ``/home`` and ``/scratch`` directory. Research groups can request additional storage on the ``/work`` storage system. Note that currently
``/work`` storage is not provisioned to individuals. 

.. important::
   The ``/scratch`` space is only for temporary storage. It is not backed up, and there is a purge policy for data older than 28 days 
   on /scratch. Please review the /scratch policy on our Policy page: https://rc.northeastern.edu/policy/

**NAME:** ``/home/<yourusername>`` where ``yourusername`` is your username, e.g. ``/home/j.smith``
 - **DESCRIPTION:** You are given a ``/home`` directory automatically when your Discovery account is created. This storage is mainly intended for storing relatively small files such as script files, source code, software installation files, and other small files that you need for your work on Discovery. While it is permanent storage that is backed up and replicated, it is not performant storage. It also has a small quota, so you should frequently check your space usage (use a command such as ``du -h /home/<yourusername>`` where ``<yourusername>`` is your user name, to see the total space usage). For running jobs and directing output files, you should use your ``/scratch`` directory.
 - **QUOTA:** 75GB

**NAME:** ``/scratch/<yourusername>``
 - **DESCRIPTION:** You are given a ``/scratch`` directory automatically when your Discovery account is created. Scratch is a shared space for all users. The total storage available is 1.8PB; however, while this is performant storage, it is for temporary use only. **It is not backed up.** Data on ``/scratch`` should be moved as soon as possible to another location for permanent storage. You should run your jobs from ``/scratch`` and direct your output files to your ``/scratch`` directory for best performance, but it is best practice to move your files off of scratch to avoid any potential data loss.
 - **QUOTA:** N/A

**NAME:** ``/work/<groupname>``
 - **DESCRIPTION:** Research groups can request additional storage on ``/work``. A PI can request this extra storage through the `New Storage Space request <https://bit.ly/NURC-NewStorage>`_ . This is a performant, persistent, and long-term storage that is meant for storing data being actively used for research. It can be accessed by all members of the research group who have access permissions to this directory. 
- **QUOTA:** Each group can request up to **35TB** of free storage across all supplemental storage tiers: ``/work/<groupname>`` and ``/nese``.  

.. note::
   The ``/research`` storage tier is no longer provided. Please contact Research Computing if you are a former user of ``/research`` and have questions or issues related to this by `submitting a ticket <https://bit.ly/NURC-Assistance>`_. Other storage options include ``/work``, `Sharepoint <https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012695>`_, and `OneDrive <https://service.northeastern.edu/tech?id=kb_article&sysparm_article=KB0012764>`_. 

Archival Storage
==================================

**NAME:** ``/nese``
 - **DESCRIPTION:** This is archival, non-performant storage that is intended for researchers who need to have a long-term storage option for their data.
 - **QUOTA:** Each group can request up to **35TB** of free storage across all supplemental storage tiers: ``/work/<groupname>`` and ``/nese``.  

.. important::
   If you are not connected to the campus internet, you must be connected to
   the university's VPN (GlobalProtect) before you can access the ``/nese`` system.
   You can find detailed information about downloading and using the GlobalProtect VPN
   in the `FAQ: VPN and remote access <https://service.northeastern.edu/tech?id=kb_article&sys_id=4701e07adb93485084ba5595ce9619a9>`_.