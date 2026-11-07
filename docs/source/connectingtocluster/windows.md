(connecting-on-windows)=
# Connecting on Windows
Before you can connect to the HPC on a Windows computer, you’ll need to download a terminal program,
such as [MobaXterm] or PuTTY. We recommend MobaXterm, as you can also use it for file transfer,
whereas with other SSH programs, you would need a separate file transfer program.

## To connect to cluster with MobaXterm

1. Open MobaXterm.
1. Click **Session**, then click **SSH** as the connection type.
1. In **Remote Host**, type `login.explorer.northeastern.edu`, make sure **Port** is set to 22, and click **OK**.
   (OPTIONAL: You can type your Northeastern username and password on MobaXterm, and it will save that information every time you sign in. If you opt to do this, you will be connected to Explorer after you click OK.)
1. At the prompt, type your Northeastern username and press Enter.
1. Type your Northeastern password and press Enter. Note that the cursor does not move as you type your password. This is expected behavior.

You are now connected to the cluster's login node.


(x11-windows)=
## X11 on Windows
If you use MobaXterm on Windows, X11 forwarding is turned on by default.

:::{tip}
You can test to see if x11 forwarding is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::

[MobaXterm]: https://mobaxterm.mobatek.net/
