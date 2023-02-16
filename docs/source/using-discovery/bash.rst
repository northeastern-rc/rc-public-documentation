.. _using_bash:

***********
Using Bash
***********
.. figure:: /images/bash-logo.png
   :class: with-border
   :width: 300
   :alt: Bash (Bourne Again SHell) logo.
   :align: center

   Bash (Bourne Again SHell)

Overview
=================
Bash (Bourne Again SHell) is a popular shell and command-line interface in Unix-like operating systems. A shell is an interface between the user and the underlying operating system, allowing users to interact with the system and perform tasks. Bash provides a range of features for running commands, managing files, and performing other tasks.

Bash commands perform various tasks within the shell environment. Some common bash commands include ``ls`` for listing the contents of a directory, ``cd`` for changing the current directory, ``cp`` for copying files, ``mv`` for moving files, and ``rm`` for removing files. Bash also provides a range of advanced commands, such as ``grep`` for searching for text within files, sed for performing text transformations, and ``awk`` for processing text data. We cover these commands, along with others, in this tutorial.

Bash also provides a rich set of features for scripting, allowing users to automate tasks and perform complex operations. Bash scripts are text files that contain a series of bash commands, and the shell can execute them to perform a specific task. As a result, scripts cover a range of tasks, including backups, system maintenance, and more.

Bash is a powerful and versatile shell environment that provides a rich set of features for performing tasks on a Unix-like operating system. Whether a beginner or an advanced user, bash offers the tools to perform various functions from the command line.

In summary, Shell commands perform various tasks with the terminal, as depicted in the following figure.

.. figure:: /images/terminal-view.png
   :class: with-border
   :width: 300
   :alt: Bash (Bourne Again SHell) logo.
   :align: center

   Bash (Bourne Again SHell)

Terminal
=================

Mac Users
---------
Mac OS comes with a default terminal program. There are various, more advanced terminals available, as well. `iTerm2`_ is one of the more popular choices.

To launch the terminal:
#. Press Command + Space Bar on your Mac keyboard (alternatively, press F4)
#. Type in “Terminal”
#. When you see Terminal in the Spotlight search list, click it to open the app.

iTerm2 can be installed via the terminal using `Homebrew`_::

   brew install --cask iterm2

If Homebrew is not already installed, run the following command in the terminal before installing iTerm2::

   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Linux Users
-----------
Linux also comes with a default terminal program. And, again, there are various, more advanced terminals available. `Terminator`_ is one of the more popular choices.

To download Terminator, open a terminal (``Ctrl+Alt+T`` is the shortcut to do so). Then, execute the following::

   sudo add-apt-repository ppa:gnome-terminator
   sudo apt-get update
   sudo apt-get install terminator

Windows Users
-------------
Windows users must install a terminal. There are various flavors available. One suggestion is to visit the Windows Apps and download directly from Microsoft (`Download Windows Terminal`_).
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

find
-----
``find`` is a powerful command line tool used to search for files and directories within a specified location. It operates by starting at a specified directory and recursively searching through its subdirectories. The user can select a range of criteria to match, such as the file name, size, modification time, and more, and ``find`` will return a list of all files and directories that match the specified criteria. ``find`` provides a range of options for further processing the results, such as executing a command on each matching file, printing the results, or performing other operations. As a result, it is a versatile tool for various tasks, including searching for specific files, cleaning up old files, and more.

Examples
^^^^^^^^^
Here are several advanced examples of using the ``find`` command to search for files and directories:

Finding files based on size::

   $ find /path/to/dir -size +10M
This will find all files in /path/to/dir that are larger than 10 MB.

Finding files based on modification time::

   $ find /path/to/dir -mtime +7
This will find all files in /path/to/dir that have been modified more than 7 days ago.

Finding files based on type::

   $ find /path/to/dir -type f
This will find all files in /path/to/dir that are regular files (not directories).

Finding files based on name::

   $ find /path/to/dir -name "*.txt"
This will find all files in /path/to/dir that have a .txt file extension.

Executing commands on matching files::

   $ find /path/to/dir -name "*.txt" -exec chmod 644 {} \;
This will find all files in ``/path/to/dir`` that have a ``.txt`` file extension and execute the ``chmod`` command on each file, changing its permissions to ``644``.

These are just a few examples of the many advanced features available with the ``find`` command. See `find(1) manual page`_ for more information on how to use the command effectively.

awk
-----
``awk`` is a powerful text processing tool widely used for data extraction, report generation, and other text-related tasks. It operates by reading a file line-by-line and processing each line based on a set of rules defined by the user. The regulations specify the conditions under which certain actions are performed, such as printing specific fields, performing calculations, or modifying the text in some way. ``awk`` is particularly useful for processing tabular data, such as that found in CSV files, and can extract and manipulate data in various ways. Additionally, ``awk`` provides a rich set of string and numerical manipulation functions, making it a powerful tool for working with large data sets.

Examples
^^^^^^^^^

Printing the first field of each line in a file::

   $ awk '{print $1}' file.txt
Printing the second field of each line in a file, only if the first field is equal to a specific value::

   $ awk '$1 == "value" {print $2}' file.txt
Printing the sum of all numbers in the third field of a file::

   $ awk '{sum+=$3} END {print sum}' file.txt
Printing the average of all numbers in the fourth field of a file::

   $ awk '{sum+=$4; count++} END {print sum/count}' file.txt
Printing the line number and the line text for each line in a file that contains a specific word::

   $ awk '/word/ {print NR, $0}' file.txt
Printing the line number and the line text for each line in a file that starts with a specific string::

   $ awk '$1 ~ /^string/ {print NR, $0}' file.txt
Printing the line number, the line text, and the length of each line in a file::

   $ awk '{print NR, $0, length($0)}' file.txt
These are just a few examples of ``awk`` processing and manipulating text data. There are many more options and features available. Consult the `awk(1) manual page`_ for more information on effectively using the tool.


Git Configurations: Tips and Tricks:
----------------------------------
Git is a distributed version control system for software development and other collaborative projects. It allows multiple users to work on a project simultaneously while keeping track of changes and enabling easy collaboration. With Git, users can commit their changes to a local repository and push them to a remote repository so that others can access and merge their changes into the main project. Git also provides a robust set of tools for managing branches, resolving conflicts, and performing other tasks related to version control.

Git provides a range of configuration options that allow users to customize their behavior to suit their needs, including setting the user name and email, specifying a preferred text editor, setting up aliases for frequently used commands, and many others. In addition, users can configure Git globally, which applies the configuration to all of their Git repositories, or locally, which applies the configs to a specific repo. This flexibility allows users to work with Git in a way that suits their workflow and provides a high degree of control over how Git operates.

Example Configurations
^^^^^^^^^^^^^^^^^^^^^^
Setting your user name and email::

   $ git config --global user.name "Your Name"
   $ git config --global user.email "your.email@example.com"
Setting your preferred text editor::

   $ git config --global core.editor nano
Setting your preferred diff tool::

   $ git config --global diff.tool emacs
   $ git config --global difftool.prompt false
Setting up aliases for frequently used Git commands::

   $ git config --global alias.st status
   $ git config --global alias.co checkout
   $ git config --global alias.ci commit
Setting up a default push behavior::

   $ git config --global push.default simple
Enabling colored output for Git commands::

   $ git config --global color.ui true
Ignoring files globally across all your Git repositories::

   $ git config --global core.excludesfile ~/.gitignore_global
Enabling automatic line wrapping in Git log output::

   $ git config --global log.autoWrap true
These are just a few examples of Git configuration options. There are many more options available. See `Git User Manual`_ for more information on how to customize Git to your needs.


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


.. _Download Windows Terminal: https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=us&rtc=1
.. _Homebrew: https://brew.sh/
.. _iTerm2: : https://iterm2.com/
.. _Terminator: https://gnome-terminator.org/
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