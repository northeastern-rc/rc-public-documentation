(connecting-on-mac)=
# Connecting on a Mac

Mac computers come with a Secure Shell (SSH) program called [Terminal] that you use to connect to the HPC using SSH. If you need to use software that uses a GUI, such as MATLAB or Maestro, make sure to use the -Y option in the second step below using X11 forwarding.

:::{note}
If you use Mac OS X version 10.8 or higher, and you have [XQuartz] running in the background to do X11 forwarding, you should execute the following command in Terminal once before connecting:

`defaults write org.macosforge.xquartz.X11 enable_iglx -bool true`

You should keep XQuartz running in the background. If you close and restart XQuartz, you will need to execute the above command again after restarting. Do not use the Terminal application from within XQuartz to sign in to Explorer. Use the default Terminal program that comes with your Mac (see Step 1 in the procedure below).
:::

## Copy your SSH Keys from the cluster

Login to the Open OnDemand website (ood.explorer.northeastern.edu) and copy your public and private key from /home/$username/.ssh to your local computer. Your keys should match the pattern below:

:::{code-block} bash
$username-$generationdate     : your private key
$username-$generationdate.pub : your public key
:::

On your local computer put your keys in your ~/.ssh directory. And make sure the permissions are set as below 600 for private key and 644 for the public key:

:::{code-block} bash
-rw------- 1 s.caplins users  411 Oct 27 10:00 s.caplins-20261027T140127Z
-rw-r--r-- 1 s.caplins users   98 Oct 27 10:00 s.caplins-20261027T140127Z.pub
:::

Set the permissions if needed:

:::{code-block} bash
chmod 600 s.caplins-20261027T140127Z
chmod 644 s.caplins-20261027T140127Z.pub
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
[s.lurm@explorer-02 ~]$

:::



(x11-mac)=
## X11 on Mac OS
From a Mac Terminal log in using the -Y option (`ssh -Y <yourusername>@login.explorer.northeastern.edu`).

:::{tip}
If you used the -Y option to enable X11 forwarding on your Mac, you can test to see if it is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::

[Terminal]: https://support.apple.com/guide/terminal/welcome/mac
[XQuartz]: https://www.xquartz.org/
