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
   file1.txt  file2.txt  directory1
``cd`` - Change the current working directory::

   $ cd ~/directory1
   $ pwd
   <$HOME>/directory1
Note: ``~`` is shorthand for specifying the home directory of the current user.

``pwd`` - Print the current working directory::

   $ pwd
   /path/to/directory1
``mkdir`` - Create a new directory::

   $ mkdir directory2
   $ ls
   file1.txt  file2.txt  directory1  directory2
``rm`` - Remove a file or directory::

   $ rm file1.txt
   $ ls
   file2.txt  directory1  directory2
``cp`` - Copy a file or directory::

   $ cp file2.txt file3.txt
   $ ls
   file2.txt  file3.txt  directory1  directory2
``mv`` - Move or rename a file or directory::

   $ mv file2.txt file4.txt
   $ ls
   file3.txt  file4.txt  directory1  directory2
``echo`` - Display a message or the value of a variable::

   $ echo "Hello, world!"
   Hello, world!
``cat`` - Concatenate and display the contents of one or more files::

   $ cat file3.txt
   This is the contents of file3.txt
``grep`` - Search for a pattern in a file or input::

   $ grep "the" file3.txt
   This is the contents of file3.txt
``sort`` - Sort the lines of a file or input::

   $ sort file3.txt
   This is the contents of file3.txt
``uniq`` - Remove duplicates from a sorted file or input::

   $ sort file3.txt | uniq
   This is the contents of file3.txt
``wc`` - Count the number of lines, words, and characters in a file or input::

   $ wc file3.txt
   1   4  26 file3.txt
``head`` - Display the first lines of a file or input::

   $ head file3.txt
   This is the contents of file3.txt
``tail`` - Display the last lines of a file or input::

   $ tail file3.txt
   This is the contents of file3.txt
``less`` - View the contents of a file one page at a time::

   $ less file3.txt
``top`` - Show the currently running processes and system information::

   $ top
``ps`` - Show information about the currently running processes::

   $ ps
``kill`` - Terminate a process by its process ID::

   $ kill <pid>
Note: ``<pid>`` in the command should be replaced with the actual process ID of the process you want to terminate: the output of the ``kill`` command will typically be empty unless there is an error in executing the command.

It's essential to be cautious when using the ``kill`` command, as terminating a process can cause data loss or corruption. Therefore, before using ``kill``, you should always try to gracefully stop the process by sending a termination signal, such as ``SIGTERM``, first. If that does not work, you can try a stronger signal, such as ``SIGKILL``.

Advanced Commands
=================
Here are some advanced Unix commands, along with references and examples.

``find`` - Search for files and directories::

   $ find /path/to/search -name "*.txt"
   /path/to/search/file1.txt
   /path/to/search/file2.txt
Reference: `find(1) manual page`_

``gzip`` - Compress or decompress files::

   $ gzip file1.txt
   $ ls
   file1.txt.gz
::

   $ gunzip file1.txt.gz
   $ ls
   file1.txt
Reference: `gzip(1) manual page`_

``tar`` - Create or extract compressed archive files::

   $ tar cvf archive.tar file1.txt file2.txt
   $ ls
   archive.tar file1.txt file2.txt
::

   $ tar xvf archive.tar
   $ ls
   file1.txt file2.txt
Reference: `tar(1) manual page`_

awk - Process text data and perform actions based on patterns::

   $ cat file1.txt
   This is line 1
   This is line 2
   This is line 3
::

   $ awk '/line 2/ {print "Line 2 found"}' file1.txt
   Line 2 found
Reference: `awk(1) manual page`_

``sed`` - Stream editor for filtering and transforming text::

   $ cat file1.txt
   This is line 1
   This is line 2
   This is line 3
::

   $ sed 's/line 1/Line 1/' file1.txt
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

Regular expressions::

   $ grep -E '^[A-Z][a-z]+$' file1.txt
   John
   Jane
Parameter expansion::

   $ name="John Doe"
   $ echo ${name// /_}
   John_Doe
Command line options::

   $ ls -lh
   total 8.0K
   drwxrwxr-x 2 user user 4.0K Feb 14 13:29 directory1
   -rw-rw-r-- 1 user user   12 Feb 14 13:29 file1.txt
   -rw-rw-r-- 1 user user   14 Feb 14 13:29 file2.txt
Parameter substitution::

   $ echo ${name:4:3}
   Doe
Arithmetic operations::

   $ echo $((2 + 2))
   4
File tests::

   $ file=file1.txt
   $ if [ -f $file ]; then
   >   echo "$file is a regular file"
   > fi
   file1.txt is a regular file
String tests::

   $ string="hello"
   $ if [ "$string" == "hello" ]; then
   >   echo "The strings match"
   > fi
   The strings match
Command substitution with process substitution::

   $ diff <(ls /path/to/dir1) <(ls /path/to/dir2)
These are just a few more examples of advanced bash scripting techniques.

The next few subsections provide more details on a few advanced bash tools that often come in handy.

rsync
-----
``rsync`` is a powerful and versatile file transfer utility commonly used to synchronize files and directories between different locations. It can transfer files over a network connection and run in various modes, including local and remote transfers, backup operations, and more. One of the key benefits of using ``rsync`` is its ability only to transfer the differences between the source and destination files, which can significantly reduce the amount of data transfer time required. Additionally, ``rsync`` supports various advanced features, including the ability to perform incremental backups and preserve symbolic links, making it a popular tool for system administrators and other advanced users.

Examples
^^^^^^^^^
Syncing a local directory to a remote server::

   $ rsync -avz /local/path user@remote.example.com:/remote/path
Syncing a remote server to a local directory::

   $ rsync -avz user@remote.example.com:/remote/path /local/path
Syncing a local directory to a remote server with compression::

   $ rsync -avz --compress /local/path user@remote.example.com:/remote/path
Syncing a remote server to a local directory while preserving permissions::

   $ rsync -avz --perms user@remote.example.com:/remote/path /local/path
Syncing only files that have been modified in the last hour::

   $ rsync -avz --update --min-age=3600 /local/path user@remote.example.com:/remote/path
Syncing a local directory to a remote server while excluding certain files::

   $ rsync -avz --exclude='*.log' /local/path user@remote.example.com:/remote/path
Syncing a remote server to a local directory while preserving symbolic links::

   $ rsync -avz --links user@remote.example.com:/remote/path /local/path
These are just a few examples of ``rsync`` synchronizing files and directories between two locations. There are many more options available. Consult the `rsync(1) manual page`_ for more information on effectively using the tool.
Text Editors
===============
There are a few popular text editors that enable modifying text files from the terminal. Here, we provide include emacs, vim, and nano - each are available by default on discovery.

Emacs
------
Emacs is a popular text editor that is widely used for programming, writing, and other text-related tasks. Here is a basic tutorial on how to use emacs:

**Starting emacs**

Open a terminal and type the following command::

   $ emacs
**Opening a file**
To open an existing file, use the following command::

   C-x C-f
This will open the file dialog, where you can enter the name of the file you want to open.

**Saving a file**
To save a file, use the following command::

   C-x C-s
**Closing a file**
To close a file, use the following command::

   C-x C-w
**Moving the cursor**
To move the cursor, use the arrow keys or the following commands::

   C-p (previous line)
   C-n (next line)
   C-f (forward character)
   C-b (backward character)
**Cutting and pasting text**

To cut text, use the following command::

   C-w
To paste text, use the following command::

   C-y
**Undo and redo**
To undo, use the following command::

   C-/
To redo, use the following command::

   C-x C-/
**Searching for text**

To search for text, use the following command::

   C-s
**Quitting emacs**

To quit emacs, use the following command::

   C-x C-c
These are just a few basic commands for using emacs. There are many more commands available, and it is recommended to consult the emacs manual page or online resources for more information on how to use the text editor effectively.

VIM
------
Vim is a popular text editor that is widely used for programming, writing, and other text-related tasks. Here is a basic tutorial on how to use Vim.

**Starting Vim**

Open a terminal and type the following command::

   $ vim
**Opening a file**

To open an existing file, type the following command::

   vim filename
**Normal mode**

When you start Vim, you are in normal mode. In normal mode, you can navigate through the text and perform various operations, but you cannot type or edit text.

To enter insert mode, type the following command::

   i
**Saving a file**

To save a file, type the following command in normal mode::

   :w
**Closing a file**

To close a file, type the following command in normal mode::

   :q
**Moving the cursor**

In normal mode, you can move the cursor using the following keys::

   h (left)
   j (down)
   k (up)
   l (right)
**Cutting and pasting text**

To cut text, first move the cursor to the start of the text you want to cut, then type the following command in normal mode::

   v
Move the cursor to the end of the text you want to cut, then type the following command in normal mode::

   d
To paste text, move the cursor to the location where you want to paste, then type the following command in normal mode::

   p
**Undo and redo**

To undo, type the following command in normal mode::

   u
To redo, type the following command in normal mode::

   Ctrl+r
**Searching for text**

To search for text, type the following command in normal mode::

   /text
**Quitting Vim**

To quit Vim, type the following command in normal mode::

   :q
These are just a few basic commands for using Vim. There are many more commands available. Consult the `VIM Manual`_ for more information on using the text editor effectively.

GNU Nano
---------
Nano is a simple, easy-to-use text editor commonly used in Unix-like operating systems. Here is a basic tutorial on how to use Nano:

**Starting Nano**

Open a terminal and type the following command::

   $ nano
**Opening a file**

To open an existing file, type the following command::

   nano filename
**Saving a file**

To save a file, press the following key combination::

   Ctrl + O
**Closing a file**

To close a file, press the following key combination::

   Ctrl + X
**Moving the cursor**

Use the arrow keys to move the cursor.

**Cutting and pasting text**

First, move the cursor to the start of the text you want to cut, then press the following key combination::

   Alt + A
Move the cursor to the end of the text you want to cut, then press the following key combination::

   Ctrl + K
To paste text, move the cursor to the location where you want to paste, then press the following key combination::

   Ctrl + U
**Undo and redo**

To undo, press the following key combination::

   Ctrl + T
To redo, press the following key combination::

   Ctrl + Y
**Searching for text**

To search for text, press the following key combination::

   Ctrl + W
**Quitting Nano**

To quit Nano, press the following key combination::

   Ctrl + X
These are just a few basic commands for using Nano. There are many more commands available Consult the `GNU Nano Manual`_ or online resources for more information on how to use the text editor effectively.


.. _find(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/find.1posix.html
.. _gzip(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/gzip.1.html
.. _tar(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/tar.1.html
.. _awk(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/awk.1plan9.html
.. _sed(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/sed.1.html
.. _rsync(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/rsync.1.html
.. _ssh(1) manual page: https://manpages.ubuntu.com/manpages/kinetic/en/man1/find.1posix.html
.. _Git User Manual: https://git-scm.com/docs/user-manual
.. _GNU Nano Manual: https://www.nano-editor.org/dist/latest/nano.pdf
.. _VIM Manual: : https://www.vim.org/docs.php