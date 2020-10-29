.. _general_storage:

*****************************
General Data Storage Options
*****************************
The Research Computing (RC) team is responsible for the procurement and ongoing
maintenance of several data storage options, including active and archive
storage solutions. If you are affiliated with Northeastern, you can request
one or more storage solutions to meet your storage needs. It is highly recommended
that if you anticipate needing storage as part of a grant requirement,
schedule a consultation with a Research Computing staff member to understand what
storage options would best meet your research needs.
You can schedule an online consultation on the `RC website <https://rc.northeastern.edu/support/consulting>`_.

.. note::
   If you have an account on Discovery, see :ref:`discovery_storage`
   for details on the storage available to you specifically for use with Discovery's compute resources. The options listed below are not connected to Discovery.

**NAME:** ``/research``
  - **DESCRIPTION:** This storage tier is intended to be a repository for data derived from equipment such as lab machines,
    instruments, etc. The performance capabilities are not intended for parallel or high performance workloads.
    Data are backed up and a second copy is created. You can request storage on ``/research`` by submitting a `New Storage Space request <https://bit.ly/NURC-NewStorage>`_.
    See the section "Connecting to /research" below for information on how to connect to this storage.
  - **QUOTA:** Up to 10TB per research group.

**NAME:** ``/nese``
  - **DESCRIPTION:** This is archival, non-performant storage that is intended for researchers
    who need to have a long-term storage option for their data.
  - **QUOTA:** Up to 25TB per research group.

..
     **NAME:** ``/secure``
     - **DESCRIPTION:** Secure data storage is restricted to data that must be stored in a secure,
     encrypted server, such as personally identifiable information (PII) data.
     You should first set up a consultation with a Research Computing staff member using the link above to
     determine if your data requires secure storage before requesting it.

.. important::
   If you are not connected to the campus internet, you must be connected to
   the university's VPN (GlobalProtect) before you can access these storage systems.
   You can find detailed information about downloading and using the GlobalProtect VPN
   in the `ServiceNow Knowledge Base <https://service.northeastern.edu/tech?id=kb_article&sys_id=4701e07adb93485084ba5595ce9619a9>`_.

Connecting to /research
========================
After you have received notification that your shared storage folder on /research is ready for you to use, you
can connect to it on your laptop. Use the following procedures to connect to /research from either a Windows PC or a Macbook.
If you are not on the campus internet, you will need to first be connected to Northeastern's VPN before you can connect to /research.

**Windows**

 1. Open **File Explorer**.
 2. In the left pane, select **This PC**.
 3. On the **Computer** tab, select **Map network drive**.
 4. Select any letter not currently mapped to a drive. It does not matter what letter.
 5. In the **Folder** box, type ``\\nunet.neu.edu\rc-shares\<sharename>``, where ``<sharename>`` is the name of your shared storage. If you want this drive to reconnect automaically every time you log in, check Reconnect at sign in.
 6. Click Finish. Your shared folder now be available in File Explorer.

**Mac**

 1. Click the **Finder** icon, and in the **Finder** window, select **Go**, then click **Connect to Server**.
 2. In the **Server Address** field type ``smb://nunet.neu.edu/rc-shares/<sharename>`` where ``<sharename>`` is the name of the share you want to connect to.
 3. Click Connect.
 4. If you are prompted to enter your name and password for the nunet server, select **Connect as Registered User**, in the **Name** field type ``NUNET\<yourusername>``, (where ``<yourusername>`` is your NU username) and type your NU password in the **Password** field. If you want to connect to /research automatically when you log in to your computer, select **Remember this password in my keychain**.
 5. Click Connect. Your share should appear as a folder in the Finder window.
