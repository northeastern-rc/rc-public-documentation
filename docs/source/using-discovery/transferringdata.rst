******************
Transferring Data
******************
Discovery has a dedicated transfer node that you must use to transfer data to and from the cluster.
You are not allowed to transfer data from any other node.
The node name is ``<username>@xfer.discovery.neu.edu:`` where ``<username>`` is your Northeastern username.

You can also transfer files using Globus. This is highly recommended if you need to transfer large amounts of data.
See :ref:`using_globus` for more information.

.. caution::

   The /scratch directory is for temporary file storage only. It is not backed up.
   If you have directed your output files to /scratch, you should transfer your data from /scratch
   to another location as soon as possible.

Data transfer node using Mac
============================

You can use Terminal to transfer data to and from Discovery.

Use this command to transfer a file to your /scratch space:

``scp <filename> <yourusername>@xfer.discovery.neu.edu:/scratch/<yourusername>``

Where ``<filename>`` is the name of the file you want to transfer and ``<yourusername>`` is your Northeastern username.

Data transfer node using Windows
================================
You can use MobaXterm to transfer data to and from Discovery. You can also use a file transfer program, such as FileZilla.
The Files menu in Open onDemand (OOD) also allows you to transfer files. See :ref:`file_explorer` for more information.

**To transfer data using MobaXterm:**

1. Open MobaXterm.

2. Click **Session**, then select **SFTP**.

3. In the **Remote host** field, type ``xfer.discovery.neu.edu``

4. In the **Username** field, type your Northeastern username.

5. In the **Port** field, type 22.

6. In the **Password** box, type your Northeastern password and click **OK**. Click **No** if prompted to save your password.

You will now be connected to the transfer node and can transfer files through MobaXterm.

**To transfer data using FileZilla:**

1. Open FileZilla.

2. In the **Host** field, type ``sftp://xfer.discovery.neu.edu``

3. In the **Username** field, type your Northeastern username.

4. In the **Password** field, type your Northeastern password.

5. In the **Port** field, type 22.

You will now be connected to the transfer node and can transfer files through FileZilla.
