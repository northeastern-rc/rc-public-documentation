(connecting-on-linux)=
# Connecting on Linux

Linux computers come with a Secure Shell (SSH) program called Terminal that you use to connect to the HPC using SSH. If you need to use software that uses a GUI, such as MATLAB or Maestro, make sure to use the -Y option in the second step below using X11 forwarding.

## Copy your SSH Keys from the cluster

Login to the Open OnDemand website (ood.explorer.northeastern.edu) and copy your public and private key from /home/$username/.ssh to your local computer. Your keys should match the pattern below:

:::{code-block} bash
$username-$generationdate : your private key
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


## Connecting to the Cluster on Linux

1. Open the Terminal application from the launcher menu. 
2. At the prompt, type `ssh -i ~/.ssh/<ssh-key> <username>@login.explorer.northeastern.edu`, where `<username>` is your Northeastern username, and <ssh-key></ssh-key> is your private key from above. If you need to use X11 forwarding, type `ssh -Y -i ~/.ssh/<ssh-key> <username>@login.explorer.northeastern.edu`.
3. Press Enter.

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

## Create a Config Entry
For ease of logging in, you should create a ~/.ssh/config file or add the following to your config file if you already have one. Just enter your username as it is on the cluster in place of $username and the SSH key with the timestamp as it is in your ~/.ssh directory. This is entirely optional.

?
Host explorer
    HostName login.explorer.northeastern.edu
    User s.caplins
    IdentityFile ~/.ssh/s.caplins-20261019T173141Z
And then you can login via:

?
ssh explorer

(x11-linux)=
## X11 on Linux
To use X11 forwarding, from the Terminal application, log in using the -Y option (`ssh -Y <yourusername>@login.explorer.northeastern.edu`).

:::{tip}
If you used the -Y option to enable X11 forwarding on your Linux machine, you can test to see if it is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::
