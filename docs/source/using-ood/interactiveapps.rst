.. _accessing_ood:

*****************************
Using OOD's Interactive Apps
*****************************

There are a number of applications that you can access and use through the OOD web portal.
When you select an application and click launch, the scheduler (Slurm) allocates a compute node with
a predetermined number of cores and amount of memory. The default time for running any of the
applications is one hour. It is recommended that you keep the default. If you ask for more than one
hour, you will need to wait for Slurm to allocate a resource that can run for your requested time,
which could take a long time to be allocated, depending on how busy the cluster is.

.. note::
   Some apps are reserved for specific research groups and are not for general access. If you get an access error when attempting to
   open an app, and you believe that you should have access to it, please email rchelp@northeastern.edu with your username,
   research group, the app you are trying to access, a screenshot of the error that you are getting, and we will
   look into the issue.

1. In a web browser, go to ood.discovery.neu.edu. If prompted, enter your myNortheastern username and password.

2. Select **Interactive Apps**, then select the application you want to use.

3. Accept the default of 1 hour, and click **Launch**. You might have to wait a
   minute or two for a compute node to be allocated with your requested time and resource.

.. note::
   If you request more than one hour, you might have to wait much longer for a compute node to be allocated to you.

4. If you selected Jupyter Notebook, click **Connect to Jupyter**.
   A Jupyter Notebook opens in a new tab on your browser.

.. tip::
  On the Jupyter Notebook Home tab, click **New**, then select the kernel you want to use.
  Your selected kernel opens in a new tab on your browser. Click the **Running** tab to see a
  list of what Notebooks you already have running.
  If you already have a Notebook saved to your home directory, on the **Files** tab,
  click the name of the file to restart the Notebook in a new tab on your browser.
