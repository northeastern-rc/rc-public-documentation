(command-line)=

# Cluster via Command-Line


## Overview

Bash (Bourne Again SHell) is a popular shell and command-line interface. Specifically, a shell is an interface between the user and the underlying operating system, allowing users to interact with the system and perform tasks. Bash provides a range of features for running commands, managing files, navigating systems, and performing other tasks.

:::{figure} ../images/bash-logo.png
---
alt: Bash (Bourne Again SHell) logo.
width: 350px
align: right
class: with-border

       Bash (Bourne Again SHell)
---
:::

Bash commands perform various tasks within the shell environment. Commands span basic functionalities (e.g., `ls`, `cd`, `cp`, `mv`, and `rm`) to more advanced ones(e.g., `grep` and `awk`). We cover these commands and more in this tutorial. Bash can also be used in scripts, allowing users to automate tasks and perform more complex operations via loops, conditional logic, and defining functions, which we cover at the end of this page.

In summary, shell commands perform various tasks with the terminal.


## Terminal

The terminal - the command line interface (CLI) - is a text-based interface for interacting with an operating system. It is a way for users to interact with the system and perform tasks by typing commands and receiving text-based output.

In contrast to graphical user interfaces (GUIs), the terminal provides a more direct and powerful way to interact with the system. Tasks requiring several steps in a GUI can often be accomplished much more quickly and efficiently in the terminal.

:::{figure} ../images/terminal-view.png
---
alt: Terminal View.
class: with-border
align: left
width: 350px
------------
:::

Whether you are a beginner or an advanced user, the terminal provides a powerful and versatile interface for interacting with your operating system. With some theory and practice, you can use the terminal to accomplish a wide range of tasks and take control of your system in new and powerful ways.

Various terminal options (i.e., flavors) are offered for different operating systems. [Power Shell] is available for Windows, Linux, and MacOS.

Let us explore options and specifics for each operating system; Mac, Linux, and Windows terminals.

### MacOS

macOS comes with a default terminal program, but more advanced terminals are available; [iTerm2] is one of the more popular choices.

To launch the terminal:

1. Press Command(⌘) + Space on your Mac keyboard (alternatively, press F4)
2. Type “Terminal”
3. When you see Terminal in the Spotlight search list, click it to open the app.

iTerm2 can be installed via the terminal using [Homebrew]:

:::{code-block} bash
brew install --cask iterm2
:::

If Homebrew is not already installed, run the following command in the terminal before installing iTerm2:

:::{code-block} bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
:::

### Linux

Linux also comes with a default terminal program, but more advanced terminals are available; [Terminator] is a popular choice.

To download Terminator, open a terminal (`Ctrl+Alt+T` is the shortcut to do so). Next, execute the following:

:::{code-block} bash
sudo add-apt-repository ppa:gnome-terminator
sudo apt-get update
sudo apt-get install terminator
:::

### Windows

Windows users must install a terminal; you can visit Windows Apps and download the Windows Terminal directly from Microsoft ([Download Windows Terminal]).

Additionally, [Mobaxterm], an enhanced terminal for Windows with an X11 server, tabbed SSH client, and network tools dubbed *the ultimate toolbox for remote computing*, is a great tool for connecting to the login node, exploring the Discovery file system, and transferring files. Check out their [demo](https://mobaxterm.mobatek.net/demo.html), [software features](https://mobaxterm.mobatek.net/features.html), and [download](https://mobaxterm.mobatek.net/download.html).

## Bash Manuals

The man command is used in the terminal to display manual pages for various tools and utilities. A manual or "man page" is detailed documentation for a specific command or utility that provides information about its usage, options, and examples.

To use the man command, simply type man followed by the command name or utility for which you want to view the manual page. For example, to view the manual page for the ls command, you would type the following:

:::{code-block} bash
man ls
:::

::::{admonition} Show manual page for ls
:class: dropdown

:::{include} ../_snippets/ls-man.md
:::

::::
The manual page will be displayed in a pager program such as less, which allows you to scroll through the text and search for specific information.

The man command is a valuable tool for learning about new commands and utilities, and it is an essential resource for understanding how to use the terminal effectively. Whether you are a beginner or an advanced user, the man command provides the information you need to get the most out of your tools and utilities.

## Basic Commands

:::{note}
See `_getting_access` for instructions on creating a Discovery user account.
:::

`ssh` - Connect to a remote machine using Secure Shell (SSH):

:::{code-block} bash
ssh <user-name>@login.discovery.neu.edu
:::

Reference: [ssh(1) manual page]

:::{note}
The `~` character is shorthand for specifying the current user's home directory, i.e., `~` is the same as `$HOME`.
:::

`echo` - Display a message or the value of a variable.

:::{code-block} bash
echo "Hello, world!"
:::
:::{code-block} bash
    Hello, world!
:::

:::{note}
Variable names are accessible by appending their name to `$` (e.g., \$\{VARIABLE_NAME}, where `{}` are optional but safer.)
:::

`pwd` - Print the current working directory.

:::{code-block} bash
:emphasize-lines: 2

pwd
/path/to/directory1
:::

:::{note}
`pwd` is also stored as an environment variable, i.e., `${PWD}`. Running `echo ${PWD}` prints the same output as `pwd`, but has the advantage of being accessed as part of a file pointer (e.g., `ls ${PWD}/directory2` to print all contents of `directory2` in the working directory.)
:::

`ls` - List the contents of a directory.

:::{code-block} bash
:emphasize-lines: 2

ls
file1.txt file2.txt directory1
:::

`cd` - Change the current working directory.

:::{code-block} bash
---
emphasize-lines: 3
---
cd ~/directory1
pwd
<$HOME>/directory1
:::

`mkdir` - Create a new directory.

:::{code-block} bash
:emphasize-lines: 3

 mkdir directory2
 ls
 file1.txt file2.txt directory1 directory2
:::

`rm` - Remove a file or directory.

:::{code-block} bash
:emphasize-lines: 3

 rm file1.txt
 ls
 file2.txt directory1 directory2
:::

:::{note}
To remove a directory, use `rmdir` if the folder is empty. Otherwise, recursively delete the directory and its contents via `rm -r <FOLDER_PATH>`.
:::

`cp` - Copy a file or directory.

:::{code-block} bash
:emphasize-lines: 3

 cp file2.txt file3.txt
 ls
 file2.txt file3.txt directory1 directory2
:::

:::{note}
Similar to removing, `cp` works for files; copying a folder and its contents must be done recursively via `cp -r <FOLDER_PATH> <DESTINATION>`.
:::

`mv` - Move or rename a file or directory.

:::{code-block} bash
:emphasize-lines: 3

mv file2.txt file4.txt
ls
file3.txt file4.txt directory1 directory2
:::

`cat` - Concatenate and display the contents of one or more files.

:::{code-block} bash
:emphasize-lines: 2

cat file3.txt
This is the contents of file3.txt
:::

`grep` - Search for a pattern in a file or input.

:::{code-block} bash
:emphasize-lines: 2

grep "the" file3.txt
This is the contents of file3.txt
:::

`sort` - Sort the lines of a file or input.

:::{code-block} bash
:emphasize-lines: 2

sort file3.txt
This is the contents of file3.txt
:::

`uniq` - Remove duplicates from a sorted file or input.

:::{code-block} bash
:emphasize-lines: 2

sort file3.txt | uniq
This is the contents of file3.txt
:::

`wc` - Count the number of lines, words, and characters in a file or input.

:::{code-block} bash
:emphasize-lines: 2

 wc file3.txt
 1   4  26 file3.txt
:::

`head` - Display the first lines of a file or input.

:::{code-block} bash
:emphasize-lines: 2

 head file3.txt
 This is the contents of file3.txt
:::

`tail` - Display the last lines of a file or input.

:::{code-block} bash
:emphasize-lines: 2

tail file3.txt
This is the contents of file3.txt
:::

`less` - View the contents of a file one page at a time.

:::{code-block} bash
less file3.txt
:::

`top` - Show the currently running processes and system information.

:::{code-block} bash
top
:::

To exit, press `q`.

`ps` - Show information about the currently running processes.

:::{code-block} bash
ps
:::

:::{note}
`<pid>` (`PID`) in the command should be replaced with the actual process ID of the process you want to terminate; the output of the `kill` command will typically be empty unless there is an error in executing the command.
:::

It is essential to be cautious when using the `kill` command, as terminating a process can cause data loss or corruption. Therefore, before using `kill`, you should always try to gracefully stop the process by sending a termination signal, such as `SIGTERM`, first. If that does not work, you can try a stronger signal, such as `SIGKILL`.

`kill` - Terminate a process by its process ID:

:::{code-block} bash
kill <pid>
:::

## Advanced Commands

In this section, we will provide examples of some helpful advanced commands, and then take a closer look at three essential advanced commands.

`sed` - Stream editor for filtering and transforming text.

:::{code-block} bash
:emphasize-lines: 2-4, 7-9

cat file1.txt
This is line 1
This is line 2
This is line 3

sed 's/line 1/Line 1/' file1.txt
This is Line 1
This is line 2
This is line 3
:::

Reference: [sed(1) manual page]

`gzip` - Compress or decompress files.

:::{code-block} bash
:emphasize-lines: 3

gzip file1.txt
ls
file1.txt.gz
:::

:::{code-block} bash
:emphasize-lines: 3

gunzip file1.txt.gz
ls
file1.txt
:::

Reference: [gzip(1) manual page]

`tar` - Create or extract compressed archive files.

:::{code-block} bash
:emphasize-lines: 3

tar cvf archive.tar file1.txt file2.txt
ls
archive.tar file1.txt file2.txt
:::

:::{code-block} bash
:emphasize-lines: 3

tar xvf archive.tar
ls
file1.txt file2.txt
:::

Reference: [tar(1) manual page]

Regular expressions:

:::{code-block} bash
:emphasize-lines: 2-3

grep -E '^[A-Z][a-z]+$' file1.txt
John
Jane
:::

Parameter expansion:

:::{code-block} bash
:emphasize-lines: 3

name="John Doe"
echo ${name// /_}
John_Doe
:::

Command line options:

:::{code-block} bash
:emphasize-lines: 2-5

ls -lh
total 8.0K
drwxrwxr-x 2 user user 4.0K Feb 14 13:29 directory1
-rw-rw-r-- 1 user user   12 Feb 14 13:29 file1.txt
-rw-rw-r-- 1 user user   14 Feb 14 13:29 file2.txt
:::

Parameter substitution:

:::{code-block} bash
:emphasize-lines: 2

echo ${name:4:3}
Doe
:::

Arithmetic operations:

:::{code-block} bash
:emphasize-lines: 2

echo $((2 + 2))
4
:::

File tests:

:::{code-block} bash
:emphasize-lines: 5

file=file1.txt
if [ -f $file ]; then
>   echo "$file is a regular file"
> fi
file1.txt is a regular file
:::

String tests:

:::{code-block} bash
:emphasize-lines: 5

 string="hello"
 if [ "$string" == "hello" ]; then
 >   echo "The strings match"
 > fi
 The strings match
:::

Command substitution with process substitution:

:::{code-block} bash
diff <(ls /path/to/dir1) <(ls /path/to/dir2)
:::

The next few subsections provide more details on a few advanced bash tools that often come in handy.

### rsync

The `rsync` command is a powerful and versatile file transfer utility commonly used to synchronize files and directories between different locations. It can transfer files over a network connection and run in various modes, including local and remote transfers and backup operations. One of the key benefits of using `rsync` is its ability to transfer only the differences between the source and destination files, which can significantly reduce the amount of data transfer time required. Additionally, `rsync` supports various advanced features, including the ability to perform incremental backups and preserve symbolic links, making it a popular tool for system administrators and other advanced users.

:::{important}
File transfers must be done using the transfer node on the Discovery, i.e., do not copy to or from the login node accessible via `xfer.discovery.neu.edu`. See {ref}`transferring-data` for more information.
:::

We have listed a few examples of `rsync` synchronizing files and directories between two locations, but many more options are available. Consult the [rsync(1) manual page] for more information on effectively using `rsync`.

Syncing a local directory to a remote server:

:::{code-block} bash
rsync -avz /local/path user@xfer.discovery.neu.edu:/remote/path
:::

Syncing a remote server to a local directory:

:::{code-block} bash
rsync -avz user@xfer.discovery.neu.edu:/remote/path /local/path
:::

Syncing a local directory to a remote server with compression:

:::{code-block} bash
rsync -avz --compress /local/path user@xfer.discovery.neu.edu:/remote/path
:::

Syncing a remote server to a local directory while preserving permissions:

:::{code-block} bash
rsync -avz --perms user@xfer.discovery.neu.edu:/remote/path /local/path
:::

Syncing only files that have been modified in the last hour:

:::{code-block} bash
rsync -avz --update --min-age=3600 /local/path user@xfer.discovery.neu.edu:/remote/path
:::

Syncing a local directory to a remote server while excluding certain files:

:::{code-block} bash
rsync -avz --exclude='*.log' /local/path user@xfer.discovery.neu.edu:/remote/path
:::

Syncing a remote server to a local directory while preserving symbolic links:

:::{code-block} bash
rsync -avz --links user@xfer.discovery.neu.edu:/remote/path /local/path
:::

### find

`find` is a command line tool used to search for files and directories within a specified location. It starts at a specified directory and recursively searches through its subdirectories. The user can select a range of criteria to match (e.g., file name, size, modification time), and `find` will return a list of all files and directories that match the specified criteria. `find` provides a range of options for further processing the results, such as executing a command on each matching file, printing the results, or performing other operations. As a result, it is a versatile tool to search for specific files and to clean up old files.

Here are several advanced examples of using the `find` command to search for files and directories; see [find(1) manual page] for more information on how to use the command effectively.

To search for files and directories:

:::{code-block} bash
:emphasize-lines: 2-3

find /path/to/search -name "*.txt"
/path/to/search/file1.txt
/path/to/search/file2.txt
:::

Finding files based on size

:::{code-block} bash
find /path/to/dir -size +10M
:::

This will find all files in `/path/to/dir` that are larger than 10 MB.

Finding files based on modification time:

:::{code-block} bash
find /path/to/dir -mtime +7
:::

This will find all files in `/path/to/dir` that have been modified more than 7 days ago.

Finding files based on type:

:::{code-block} bash
find /path/to/dir -type f
:::

This will find all files in `/path/to/dir` that are regular files (not directories).

Finding files based on the name

:::{code-block} bash
find /path/to/dir -name "*.txt"
:::

This will find all files in `/path/to/dir` with a `.txt` file extension.

Executing commands on matching files:

:::{code-block} bash
find /path/to/dir -name "*.txt" -exec chmod 644 {} \;
:::

This will find all files in `/path/to/dir` with a `.txt` file extension and execute the `chmod` command on each file, changing its permissions to `644`.

### awk

`awk` is a text-processing tool widely used for data extraction, report generation, and other text-related tasks. It operates by reading a file line-by-line and processing each line based on a set of rules defined by the user. The regulations specify the conditions under which certain actions are performed, such as printing specific fields, performing calculations, or modifying the text in some way. `awk` is particularly useful for processing tabular data, such as those found in CSV files, and extracting and manipulating data in various ways. Additionally, `awk` provides a rich set of string and numerical manipulation functions, making it a powerful tool for working with large data sets.

Below are a few examples of `awk` processing and manipulating text data, but there are many more options and features available. Consult the [awk(1) manual page] for more information on effectively using the tool.

We will use the sample file `_resources/awk-example.sh` to work through this section.

{download}`Download <../_resources/awk-example.sh>`, or create and name a file as shown in the following block. Also, be sure to store it in the working directory.

:::{code-block} bash
:emphasize-lines: 2-6

cat awk-example.txt
John Doe 25
Jane Doe 30
Jim Smith 40
Sara Johnson 35
Michael Brown 29
:::

This file contains a list of names and ages, with each line representing a different person and their age. The first column is the name, and the second column is the age. The columns are separated by a space.

This sample file can be used in the examples provided in the previous response to demonstrate the usage of `awk` command.

Print the entire contents of a file:

:::{code-block} bash
:emphasize-lines: 2-6

awk '{print}' awk-example.txt
John Doe 25
Jane Doe 30
Jim Smith 40
Sara Johnson 35
Michael Brown 29
:::

Print specific columns from a tab-delimited file:

:::{code-block} bash
:caption: Assuming the file is not tab-delimited.
:emphasize-lines: 2-6

awk -F "\t" '{print $2}' awk-example.txt
25
30
40
35
29
:::

Sum a column of numbers:

:::{code-block} bash
:emphasize-lines: 2

awk '{sum+=$2} END {print sum}' awk-example.txt
169
:::

Print only lines that match a pattern:

:::{code-block} bash
:emphasize-lines: 2, 3

awk '/Doe/ {print}' awk-example.txt
John Doe 25
Jane Doe 30
:::

Format the output:

:::{code-block} bash
:emphasize-lines: 2-6

awk '{printf "Name: %s, Age: %d\n", $1, $2}' awk-example.txt
Name: John Doe, Age: 25
Name: Jane Doe, Age: 30
Name: Jim Smith, Age: 40
Name: Sara Johnson, Age: 35
Name: Michael Brown, Age: 29
:::

:::{code-block} bash
:emphasize-lines: 2

awk '/Sara/ {print "Sara found"}' awk-example.txt
Sara found
:::

Printing the first field of each line in a file:

:::{code-block} bash
:emphasize-lines: 2-6

awk '{print $1}' awk-example.txt
John
Jane
Jim
Sara
Michael
:::

Printing the second field of each line in a file, only if the first field is equal to a specific value:

:::{code-block} bash
:emphasize-lines: 2-3

awk '$2 == "Doe" {print $1}' awk-example.txt
John
Jane
:::

Printing the sum of all numbers in the third field (Age) of a file:

:::{code-block} bash
:emphasize-lines: 2

awk '{sum+=$3} END {print sum}' awk-example.txt
159
:::

Printing the average of all numbers in the fourth field of a file:

:::{code-block} bash
:emphasize-lines: 2

awk '{sum+=$3; count++} END {print sum/count}' awk-example.txt
31.8
:::

Printing the line number and the line text for each line in a file that contains a specific word:

:::{code-block} bash
:emphasize-lines: 2-3

awk '/Doe/ {print NR, $0}' awk-example.txt
1 John Doe 25
2 Jane Doe 30
:::

Printing the line number and the line text for each line in a file that starts with a specific string:

:::{code-block} bash
:emphasize-lines: 2-4

awk '$1 ~ /^J/ {print NR, $0}' awk-example.txt
1 John Doe 25
2 Jane Doe 30
3 Jim Smith 40
:::

Printing the line number, the line text, and the length of each line in a file:

:::{code-block} bash
:emphasize-lines: 2-6

awk '{print NR, $0, length($0)}' awk-example.txt
1 John Doe 25 11
2 Jane Doe 30 11
3 Jim Smith 40 12
4 Sara Johnson 35 15
5 Michael Brown 29 16
:::

### Git configurations tips and tricks

Git is a distributed version control system for software development and other collaborative projects that allows multiple users to work on a project simultaneously while keeping track of changes and enabling easy collaboration. With Git, users can commit their changes to a local repository and push them to a remote repository so that others can access and merge their changes into the main project. Git also provides a robust set of tools for managing branches, resolving conflicts, and performing other tasks related to version control.

Git provides a range of configuration options that allow users to customize their behavior to suit their needs, including setting the username and email, specifying a preferred text editor, and setting up aliases for frequently used commands. In addition, users can either configure Git globally, which will apply the configuration to all of their Git repositories, or configure locally, which will apply the configuration only to a specific repository. This flexibility allows users to work with Git in a way that suits their workflow.

#### Custom Configurations

Below you will find a few examples of Git configuration options. See [Git User Manual] for more information on how to customize Git to your needs.

Setting your username and email

:::{code-block} bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
:::

Setting your preferred text editor

:::{code-block} bash
git config --global core.editor nano
:::

Setting your preferred diff tool

:::{code-block} bash
git config --global diff.tool emacs
git config --global difftool.prompt false
:::

Setting up aliases for frequently used Git commands

:::{code-block} bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
:::

Setting up a default push behavior:

:::{code-block} bash
git config --global push.default simple
:::

Enabling colored output for Git commands:

:::{code-block} bash
git config --global color.ui true
:::

Ignoring files globally across all your Git repositories as follows:

:::{code-block} bash
git config --global core.excludesfile ~/.gitignore_global
:::

Enabling automatic line wrapping in Git log output as follows:

:::{code-block} bash
git config --global log.autoWrap true
:::

## Text Editors

There are a few popular text editors to create, view, and modify text files from a terminal: Emacs, Vim, and Nano. Here, we briefly describe these text editors, all of which are available by default on Discovery.

### Emacs

Emacs is a popular text editor that is widely used to program, write, and read text files. You should consult the [Emacs Manual] or online resources for more information on how to use the text editor effectively.

To start Emacs, open a terminal and type the following command:

:::{code-block} bash
emacs
:::

Once open, the following table summarizes common keyboard shortcuts (i.e., commands) for working in the text editor.

:::{list-table} Common Emacs Commands
--------------
header-rows: 1
align: center
widths: auto
--------------
* - Functionality
  - Command
* - Open file
  - ``Ctrl + x Ctrl + f``
* - Save the file
  - ``Ctrl + x Ctrl + s``
* - Close file
  - ``Ctrl + x Ctrl + w``
* - Cut text
  - ``Ctrl + k``
* - Paste text
  - ``Ctrl + y``
* - Undo
  - ``Ctrl + /``
* - Redo
  - ``C-x C-/``
* - Search text
  - ``C-s``
* - Quit Emacs
  - ``C-s``
* - *Moving cursor*
  - ``C-x C-c``
* - previous line
  - ``C-p``
* - next line
  - ``C-n``
* - forward character
  - ``C-f``
* - backward character
  - ``C-b``
:::

For more commands, see [Emacs Cheat Sheet].

### Vim

Vim is a popular text editor that is widely used for programming, writing, and other text-related tasks. Consult the [VIM Manual] for more information on using the text editor effectively.

Vim starts in **normal mode**: a mode that allows for the navigation through the text and performs various operations (e.g., search), but in read-online mode (i.e., cannot edit text).

Open a terminal and type the following command:

:::{code-block} bash
vim
:::

To open an existing file, type the following command:

:::{code-block} bash
vim filename
:::

:::{list-table} Common Vim Commands
--------------
header-rows: 1
align: center
widths: auto
--------------
* - Functionality
  - Command
* - Enter insert mode
  - ``i``
* - Enter normal mode
  - ``esc``
* - Save the file
  - ``:w``
* - Close file
  - ``:q``
* - Cut text (from the front)
  - ``v``
* - Cut text (from the end)
  - ``d``
* - Paste text
  - ``p``
* - Undo
  - ``u``
* - Redo
  - ``Ctrl+r``
* - Search text
  - ``/text``
* - Quit VIM
  - ``:q``
* - *Moving cursor*
  - ``C-x C-c``
* - Left
  - ``h``
* - Down
  - ``j``
* - Up
  - ``k``
* - Right
  - ``l``
:::

### GNU Nano

Nano is a simple, easy-to-use text editor commonly used in Unix-like operating systems. Consult the [GNU Nano Manual] or online resources for more information on how to use the text editor effectively.

Nano can launch one of two ways from a terminal: (1) to open to an empty, unnamed file, run:

:::{code-block} bash
nano
:::

To open a file by name, whether it already exists or needs to be created, run:

:::{code-block} bash
nano filename.txt
:::

If the file does not exist, it will open an empty file that will persist upon saving.

:::{list-table} Common Nano Commands
--------------
header-rows: 1
align: center
widths: auto
--------------
* - Functionality
  - Command
* - Save the file
  - ``Ctrl + O``
* - Close file
  - ``Ctrl + X``
* - Cut text (from the front)
  - ``Alt + A``
* - Cut text (from the end)
  - ``Ctrl + K``
* - Paste text
  - ``Ctrl + U``
* - Undo
  - ``Ctrl + T``
* - Redo
  - ``Ctrl + Y``
* - Search text
  - ``Ctrl + W``
* - Quit Nano
  - ``Ctrl + X``
:::

## Shell Scripting

Shell scripts are a feature of Bash that allows you to automate tasks and perform complex operations. A shell script is a text file containing a series of bash commands that the shell can execute to perform a specific task.

Here is a simple example of a shell script that prints the message `Hello, World!` to the screen:

:::{code-block} bash
#!/bin/bash

echo "Hello, World!"
:::

Notice the line `#!/bin/bash` at the top of a shell script (i.e., the shebang line). This line specifies which shell interpreter will be used when running the script. In this case, line `#!/bin/bash` specifies that the script uses the bash shell.

:::{note}
The shebang line is the first line of the script and must start with the characters `#!`. The path that follows the shebang (`/bin/bash` in this case) specifies the location of the shell interpreter. In most cases, `/bin/bash` is the correct path for the bash shell.
:::

First we must make the file executable to run this script. This is done as follows:

:::{code-block} bash
chmod +x hello_world.sh
:::

Then, run the script as follows:

:::{code-block} bash
./hello_world.sh
:::

This will print the message `Hello, World!` on the screen.

Shell scripts can do many tasks, including backups, system maintenance, and the commands covered in this tutorial. For example, you could create a script to automate the backup of your home directory by copying all of its files to a remote server. The script could include commands for compressing the files, copying them to the server, and logging the results.

[awk(1) manual page]: https://manpages.ubuntu.com/manpages/kinetic/en/man1/awk.1plan9.html
[download windows terminal]: https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=us&rtc=1
[emacs cheat sheet]: https://www.gnu.org/software/emacs/refcards/pdf/refcard.pdf
[emacs manual]: https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html
[find(1) manual page]: https://manpages.ubuntu.com/manpages/kinetic/en/man1/find.1posix.html
[git user manual]: https://git-scm.com/docs/user-manual
[gnu nano manual]: https://www.nano-editor.org/dist/latest/nano.pdf
[gzip(1) manual page]: https://manpages.ubuntu.com/manpages/kinetic/en/man1/gzip.1.html
[homebrew]: https://brew.sh/
[iterm2]: https://iterm2.com/
[mobaxterm]: https://mobaxterm.mobatek.net/
[power shell]: https://learn.microsoft.com/en-us/powershell/
[rsync(1) manual page]: https://manpages.ubuntu.com/manpages/kinetic/en/man1/rsync.1.html
[sed(1) manual page]: https://manpages.ubuntu.com/manpages/kinetic/en/man1/sed.1.html
[ssh(1) manual page]: https://manpages.ubuntu.com/manpages/kinetic/en/man1/find.1posix.html
[tar(1) manual page]: https://manpages.ubuntu.com/manpages/kinetic/en/man1/tar.1.html
[terminator]: https://gnome-terminator.org/
[vim manual]: https://www.vim.org/docs.php
