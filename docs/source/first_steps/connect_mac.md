(connect-mac)=

# Connecting Mac

You connect to Discovery using a [secure shell](https://www.ssh.com/ssh/protocol/) program to initiate an SSH session to
sign in to Discovery. If you usually launch software from the command line that uses a graphical user interface (GUI), see {ref}`using-x11` for tips and troubleshooting information.

## Mac

Mac computers come with a Secure Shell (SSH) program called [Terminal](https://support.apple.com/guide/terminal/welcome/mac)
that you use to connect to the HPC using SSH. If you need to use software that uses a GUI, such as Matlab or Maestro, make sure to use the -Y option in the second step below (see [Using X11](using-x11) for more tips and troubleshooting information).

:::{note}
If you use Mac OS X version 10.8 or higher, and you have [XQuartz](https://www.xquartz.org/) running in the background to do X11 forwarding, you should execute the following command in Terminal once before connecting:

`defaults write org.macosforge.xquartz.X11 enable_iglx -bool true`

You should keep XQuartz running in the background. If you close and restart XQuartz, you will need to execute the above command again after restarting. Do not use the Terminal application from within XQuartz to sign in to Discovery. Use
the default Terminal program that comes with your Mac (see Step 1 in the procedure below).
:::

**To connect to Discovery on a Mac:**

1. Go to Finder > Applications > Utilities, and then double click Terminal.
1. At the prompt, type `ssh <username>@login.discovery.neu.edu`, where `<username>` is your Northeastern username. If you need to use X11 forwarding, type `ssh -Y <username>@login.discovery.neu.edu`.
1. Type your Northeastern password and press `Enter`.

You are now connected to Discovery at a login node.

Watch this video of how to connect to Discovery on a Mac. If you do not see any controls on the video, right-click on the video to see viewing options.

<video width="720" height="480" controls>
  <source src="../_static/video/connect_mac_terminal.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<!-- ![Alt text](../_static/video/connect_mac_terminal.mp4) -->

(using-x11)=

## Using X11

When you launch a software application that uses a graphical user interface (GUI) from the command line, this is completed through X11 forwarding. If you use MobaXterm on Windows, X11 forwarding
is turned on by default. If you use the Terminal program on Mac, you'll need to log in using the -Y option (`ssh -Y <yourusername>@login.discovery.neu.edu`).

:::{tip}
If you used the -Y option to enable X11 forwarding on your Mac, you can test to see if it is working by typing `xeyes`. This will run a small program that makes
a pair of eyes appear to follow your cursor.
:::

### Passwordless ssh

You need to set up passwordless ssh to ensure that GUI-based applications will launch without any issues. You also
need to make sure that your keys are added to the authorized.key file. This needs to be done anytime you regenerate your keys. If you're having
an issue with opening an application that need X11 forwarding, such as MATLAB or Schrodinger, and you recently regenerated your keys, make sure to
add your keys to the authorized.key file.

:::{note}

Errors that you can see on both Mac and Windows when launching a GUI-based program include the following:
>
> `Error: unable to open display localhost:19.0`
>
> `Launch failed: non-zero return code`

If you are getting these types of errors, it could be because of following reasons:

1. You haven't set up passwordless SSH. If that's the case, you can follow the steps below to set up passwordless SSH.
1. When requesting a compute node from the login node, you may have forgotten to include the `--x11` option. In that case please see this example [srun](https://rc-docs.northeastern.edu/en/latest/using-discovery/srun.html?highlight=X11#srun-examples) command for more details.
:::

**Setting up passwordless ssh:**

:::{note}

Make sure you’re on your local computer for steps 1 through 4. If you are connected to the cluster, type `exit` to return to your local computer.
:::

1. On a Mac, open Terminal and type `cd ~/.ssh`. This moves you to the ssh folder on your local computer.
1. Type `ssh-keygen -t rsa` to generate two files, `id_rsa` and `id_rsa.pub`.
1. Press `Enter` to all the prompts (do not generate a passphrase).
1. Type `ssh-copy-id -i ~/.ssh/id_rsa.pub <yourusername>@login.discovery.neu.edu` to copy `id_rsa.pub` to your `/home/.ssh` folder on Discovery. Enter your NU password if prompted. This copies the token from `id_rsa.pub` file to the `authorized_keys` file which will either be generated or appended if it already exists.
1. Connect to Discovery via `ssh <yourusername>@login.discovery.neu.edu`. You should now be connected without having to enter your password.

:::{note}

If you are using a Windows machine using MobaXterm, sign in to the HPC as usual, then complete steps 6 through 9 to complete the passwordless ssh setup.
:::

6. Type `cd ~/.ssh` to move to your ssh folder.
1. Type `ssh-keygen -t rsa` to generate your key files.
1. Press Enter to all the prompts (do not generate a passphrase). If prompted to overwrite a file, type `Y`.
1. Type `cat id_rsa.pub >> authorized_keys`. This adds the contents of your public key file to a new line in the `~/.ssh/authorized_keys` file.

**Next Steps**

:::{include} ../_snippets/next-steps.md
:::
