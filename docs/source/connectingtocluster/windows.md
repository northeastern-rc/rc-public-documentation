(connecting-on-windows)=
# Connecting on Windows

Windows computers do not include a full-featured SSH program with a graphical interface, so we recommend [MobaXterm] to connect to the HPC using SSH. MobaXterm includes a built-in X11 server, so if you need to use software that uses a GUI, such as MATLAB or Maestro, X11 forwarding works without installing anything extra.

:::{note}
Download the **Home Edition (Installer edition)** of MobaXterm from the [MobaXterm download page][MobaXterm Download] and install it before continuing. The Portable edition also works, but saved sessions are easier to keep with the Installer edition.
:::

## Copy your SSH Keys from the cluster

Login to the Open OnDemand website (ood.explorer.northeastern.edu) and copy your public and private key from /home/$username/.ssh to your local computer. Your keys should match the pattern below:

:::{code-block} bash
$username-$generationdate     : your private key
$username-$generationdate.pub : your public key
:::

On your local computer, put your keys in a folder you can easily find, such as `C:\Users\<windows-username>\.ssh`. If the `.ssh` folder does not exist, create it. Keep your private key private; do not share it or store it in a shared or synced public folder.

:::{code-block} bash
C:\Users\<windows-username>\.ssh\s.caplins-20261027T140127Z
C:\Users\<windows-username>\.ssh\s.caplins-20261027T140127Z.pub
:::

## Connecting To Cluster On Windows

1. Open MobaXterm from the Start menu.
1. Click **Session** in the top-left corner of the toolbar, and then click **SSH** at the top of the window that opens.
1. In the **Remote host** field, type `login.explorer.northeastern.edu`.
1. Check the **Specify username** box and type your Northeastern username (for example, `s.caplins`).
1. Leave the **Port** set to `22`.
1. Click **Advanced SSH settings**.
1. Check **X11-Forwarding** if you need to use software with a GUI. This box is checked by default, and you can leave it checked even if you do not plan to use a GUI.
1. Check **Use private key**, click the file icon on the right side of the field, and select your private key from above (the file that does **not** end in `.pub`).
1. Click **OK**.

MobaXterm opens a new terminal tab and connects to the cluster.

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

:::{note}
The first time you connect, MobaXterm may ask whether you want to save your password or to trust the host. Because you are signing in with an SSH key, you do not need to save a password. Click **Accept** if prompted to accept the host key.
:::

## Create a Saved Session
For ease of logging in, MobaXterm saves your connection settings as a session. After you click **OK** in the procedure above, MobaXterm automatically saves the session in the **Sessions** panel on the left side of the window. This is entirely optional, but it means you do not need to re-enter your settings each time.

To rename the session, right-click it in the **Sessions** panel, click **Edit session**, and enter a name such as `explorer` in the **Session name** field under the **Bookmark settings** tab.

To connect again later, double-click the session in the **Sessions** panel.

(x11-windows)=
## X11 on Windows
MobaXterm includes a built-in X server. When X11-Forwarding is checked in your session settings, it starts automatically when you open MobaXterm. You can confirm it is running by looking for the **X server** icon in the top-right corner of the MobaXterm window, which should appear active (not greyed out).

:::{tip}
If X11 forwarding is enabled, you can test to see if it is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::

[MobaXterm]: https://mobaxterm.mobatek.net/
[MobaXterm Download]: https://mobaxterm.mobatek.net/download.html


(x11-windows)=
## X11 on Windows
If you use MobaXterm on Windows, X11 forwarding is turned on by default.

:::{tip}
You can test to see if x11 forwarding is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::

[MobaXterm]: https://mobaxterm.mobatek.net/
