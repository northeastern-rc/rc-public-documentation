.. _using_bash:

***********
Using Bash
***********
Overview
=================
Bash (Bourne Again SHell) is a popular shell and command-line interface in Unix-like operating systems. A shell is an interface between the user and the underlying operating system, allowing users to interact with the system and perform tasks. Bash provides a range of features for running commands, managing files, and performing other tasks.

Bash commands perform various tasks within the shell environment. Some common bash commands include ls for listing the contents of a directory, cd for changing the current directory, cp for copying files, mv for moving files, and rm for removing files. Bash also provides a range of advanced commands, such as grep for searching for text within files, sed for performing text transformations, and awk for processing text data.

Bash also provides a rich set of features for scripting, allowing users to automate tasks and perform complex operations. Bash scripts are text files that contain a series of bash commands, and the shell can execute them to perform a specific task. As a result, scripts cover a range of tasks, including backups, system maintenance, and more.

Bash is a powerful and versatile shell environment that provides a rich set of features for performing tasks on a Unix-like operating system. Whether a beginner or an advanced user, bash offers the tools to perform various functions from the command line.


Basic Commands
=================
``ls`` - List the contents of a directory::

   $ ls

.. code-block::

   file1.txt  file2.txt  directory1

``cd`` - Change the current working directory::

   $ cd directory1
   $ pwd

.. code-block::

   /path/to/directory1

``pwd`` - Print the current working directory::

   $ pwd

.. code-block::

   /path/to/directory1

``mkdir`` - Create a new directory::

   $ mkdir directory2
   $ ls

.. code-block::

   file1.txt  file2.txt  directory1  directory2

``rm`` - Remove a file or directory::

   $ rm file1.txt
   $ ls

.. code-block::

   file2.txt  directory1  directory2

``cp`` - Copy a file or directory::

   $ cp file2.txt file3.txt
   $ ls

.. code-block::

   file2.txt  file3.txt  directory1  directory2

``mv`` - Move or rename a file or directory::

   $ mv file2.txt file4.txt
   $ ls

.. code-block::

   file3.txt  file4.txt  directory1  directory2

``echo`` - Display a message or the value of a variable::

   $ echo "Hello, world!"

.. code-block::

   Hello, world!

``cat`` - Concatenate and display the contents of one or more files::

   $ cat file3.txt

.. code-block::

   This is the contents of file3.txt

``grep`` - Search for a pattern in a file or input::

   $ grep "the" file3.txt

.. code-block::

   This is the contents of file3.txt

``sort`` - Sort the lines of a file or input::

   $ sort file3.txt

.. code-block::

   This is the contents of file3.txt

``uniq`` - Remove duplicates from a sorted file or input::

   $ sort file3.txt | uniq

.. code-block::

   This is the contents of file3.txt

``wc`` - Count the number of lines, words, and characters in a file or input::

   $ wc file3.txt

.. code-block::

   1   4  26 file3.txt

``head`` - Display the first lines of a file or input::

   $ head file3.txt

.. code-block::

   This is the contents of file3.txt

``tail`` - Display the last lines of a file or input::

   $ tail file3.txt

.. code-block::

   This is the contents of file3.txt

``less`` - View the contents of a file one page at a time::

   $ less file3.txt

``top`` - Show the currently running processes and system information::

   $ top

``ps`` - Show information about the currently running processes::

   $ ps

``kill`` - Terminate a process by its process ID::

   $ kill <pid>

Advanced Commands
=================
Here is the output for the kill command::

   $ kill <pid>

Note: ``<pid>`` in the command should be replaced with the actual process ID of the process you want to terminate: the output of the kill command will typically be empty unless there is an error in executing the command.

It's essential to be cautious when using the kill command, as terminating a process can cause data loss or corruption. Therefore, before using kill, you should always try to gracefully stop the process by sending a termination signal, such as SIGTERM, first. If that does not work, you can try a stronger signal, such as SIGKILL.


Here are some advanced Unix commands, along with references and examples:

``find`` - Search for files and directories::

   $ find /path/to/search -name "*.txt"

.. code-block::

   /path/to/search/file1.txt
   /path/to/search/file2.txt

Reference: `find(1) manual page`_

``gzip`` - Compress or decompress files::

   $ gzip file1.txt
   $ ls


.. code-block::

   file1.txt.gz
::

   $ gunzip file1.txt.gz
   $ ls

.. code-block::

   file1.txt

Reference: `gzip(1) manual page`_

``tar`` - Create or extract compressed archive files::

   $ tar cvf archive.tar file1.txt file2.txt
   $ ls

.. code-block::

   archive.tar file1.txt file2.txt
::
   $ tar xvf archive.tar
   $ ls

.. code-block::

   file1.txt file2.txt

Reference: `tar(1) manual page`_

awk - Process text data and perform actions based on patterns::

   $ cat file1.txt

.. code-block::

   This is line 1
   This is line 2
   This is line 3
::

   $ awk '/line 2/ {print "Line 2 found"}' file1.txt

.. code-block::

   Line 2 found

Reference: `awk(1) manual page`_

``sed`` - Stream editor for filtering and transforming text::

   $ cat file1.txt

.. code-block::

   This is line 1
   This is line 2
   This is line 3
::

   $ sed 's/line 1/Line 1/' file1.txt

.. code-block::

   This is Line 1
   This is line 2
   This is line 3

Reference: `sed(1) manual page`_

``rsync`` - Synchronize files between two locations::

   $ rsync -av /path/to/source/ /path/to/destination/

Reference: `rsync(1) manual page`_

``ssh`` - Connect to a remote machine using Secure Shell (SSH)::

   $ ssh user@remote.example.com

Reference: `ssh(1) manual page`_

These are just a few examples of advanced Unix commands. There are many more commands available, and it is recommended to consult online resources or Unix/Linux documentation for more information on how to use these tools effectively.


.. _find(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/find.1posix.html
.. _gzip(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/gzip.1.html
.. _tar(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/tar.1.html
.. _awk(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/awk.1plan9.html
.. _sed(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/sed.1.html
.. _rsync(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/rsync.1.html
.. _ssh(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/find.1posix.html