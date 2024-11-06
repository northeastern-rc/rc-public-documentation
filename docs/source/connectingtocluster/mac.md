(connecting-on-mac)=
# Connecting on a Mac

Mac computers come with a Secure Shell (SSH) program called [Terminal] that you use to connect to the HPC using SSH. If you need to use software that uses a GUI, such as MATLAB or Maestro, make sure to use the -Y option in the second step below using X11 forwarding.

:::{note}
If you use Mac OS X version 10.8 or higher, and you have [XQuartz] running in the background to do X11 forwarding, you should execute the following command in Terminal once before connecting:

`defaults write org.macosforge.xquartz.X11 enable_iglx -bool true`

You should keep XQuartz running in the background. If you close and restart XQuartz, you will need to execute the above command again after restarting. Do not use the Terminal application from within XQuartz to sign in to Explorer. Use the default Terminal program that comes with your Mac (see Step 1 in the procedure below).
:::

## Connecting To Cluster On A Mac

1. Go to Finder > Applications > Utilities, and then double click Terminal.
1. At the prompt, type `ssh <username>@login.explorer.northeastern.edu`, where `<username>` is your Northeastern username. If you need to use X11 forwarding, type `ssh -Y <username>@login.explorer.northeastern.edu`.
1. Type your Northeastern password and press `Enter`.

You are now connected to Explorer at a login node.

:::{code-block} bash
    _______  __ ____  __    ____  ____  __________
   / ____/ |/ // __ \/ /   / __ \/ __ \/ ____/ __ \
  / __/  |   // /_/ / /   / / / / /_/ / __/ / /_/ /
 / /___ /   |/ ____/ /___/ /_/ / _, _/ /___/ _, _/
/_____//_/|_/_/   /_____/\____/_/ |_/_____/_/ |_|

+-----------------------------------------------------------+
| You are now connected to the Explorer cluster. Visit our   |
| website http://rc.northeastern.edu/support for links to   |
| our service catalog, documentation, training, and consul- |
| tations. You can also email us at rchelp@northeastern.edu |
| to generate a help ticket.                                |
|                                                           |
| The Research Computing Team                               |
+-----------------------------------------------------------+
[s.falken@explorer-02 ~]$

:::

(passwordless-ssh-mac)=
## Passwordless SSH On A Mac
You must set up passwordless ssh to ensure that GUI-based applications launch without issues. Please make sure that your keys are added to the authorized.key file in your `~/.ssh` directory. This needs to be done anytime you regenerate your SSH keys. If you are having an issue opening an application that needs X11 forwarding, such as MATLAB or Schrodinger, and you recently regenerated your keys, make sure to add your keys to the authorized.key file.

:::{note}
Ensure you’re on your local computer for steps 1 through 4—type `exit` to return to your local computer if connected to the cluster.
:::

1. On a Mac, open the Terminal application and type `cd ~/.ssh`. This moves you to the ssh folder on your local computer.
1. Type `ssh-keygen -t rsa` to generate two files, `id_rsa` and `id_rsa.pub`.
1. Press `Enter` on all the prompts (do not generate a passphrase).
1. Type `ssh-copy-id -i ~/.ssh/id_rsa.pub <yourusername>@login.explorer.northeastern.edu` to copy `id_rsa.pub` to your `/home/.ssh` folder on Explorer. You can enter your NU password if prompted. This copies the token from `id_rsa.pub` file to the `authorized_keys` file, which will either be generated or appended if it already exists.
1. Connect to Explorer via `ssh <yourusername>@login.explorer.northeastern.edu`. You should now be connected without having to enter your password.

**Now on the cluster,**

1. Type `cd ~/.ssh` to move to your ssh folder.
1. Type `ssh-keygen -t rsa` to generate your key files.
1. Press Enter on all the prompts (do not generate a passphrase). If prompted to overwrite a file, type `Y`.
1. Type `cat id_rsa.pub >> authorized_keys`. This adds the contents of your public key file to a new line in the `~/.ssh/authorized_keys` file.

(x11-mac)=
## X11 on Mac OS
From a Mac Terminal log in using the -Y option (`ssh -Y <yourusername>@login.explorer.northeastern.edu`).

:::{tip}
If you used the -Y option to enable X11 forwarding on your Mac, you can test to see if it is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::

[Terminal]: https://support.apple.com/guide/terminal/welcome/mac
[XQuartz]: https://www.xquartz.org/
