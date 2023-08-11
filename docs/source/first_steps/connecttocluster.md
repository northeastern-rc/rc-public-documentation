(connect-to-cluster)=
# Connecting to the Cluster
The following sections on this page will guide you in how to connect to the cluster using the command line access using the terminal and the web interface of Open OnDemand. Guides are provided for if your personal computer is running Windows or Mac OS.

## Using the Terminal
You connect to the HPC using a [secure shell] program to initiate an SSH session to
sign in to the HPC.

::::::{tab-set}
:::::{tab-item} Windows
Before you can connect to the HPC on a Windows computer, you’ll need to download a terminal program,
such as [MobaXterm] or PuTTY. We recommend MobaXterm, as you can also use it for file transfer,
whereas with other SSH programs, you would need a separate file transfer program.

**To connect to Discovery with MobaXterm:**

1. Open MobaXterm.
1. Click **Session**, then click **SSH** as the connection type.
1. In **Remote Host**, type `login.discovery.neu.edu`, make sure **Port** is set to 22, and click **OK**.
   (OPTIONAL: You can type your Northeastern username and password on MobaXterm, and it will save that information every time you sign in. If you opt to do this, you will be connected to Discovery after you click OK.)
1. At the prompt, type your Northeastern username and press Enter.
1. Type your Northeastern password and press Enter. Note that the cursor does not move as you type your password. This is expected behavior.

You are now connected to the cluster's login node.

Watch this video to see how to connect to the cluster with MobaXterm. If you do not see any controls on the video, right click on the video to see viewing options.

<video width="720" height="480" controls>
  <source src="../_static/video/windows_moba_connect.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<!-- ![Alt text](../_static/video/windows_moba_connect.mp4) -->

:::::
:::::{tab-item} Mac OS
Mac computers come with a Secure Shell (SSH) program called [Terminal]
that you use to connect to the HPC using SSH. If you need to use software that uses a GUI, such as Matlab or Maestro, make sure to use the -Y option in the second step below (see {ref}`using-x11`. for more tips and troubleshooting information).

:::{note}
If you use Mac OS X version 10.8 or higher, and you have [XQuartz] running in the background to do X11 forwarding, you should execute the following command in Terminal once before connecting:

`defaults write org.macosforge.xquartz.X11 enable_iglx -bool true`

You should keep XQuartz running in the background. If you close and restart XQuartz, you will need to execute the above command again after restarting. Do not use the Terminal application from within XQuartz to sign in to Discovery. Use the default Terminal program that comes with your Mac (see Step 1 in the procedure below).
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
:::::
::::::

## Using Open OnDemand
To learn more about connecting to the cluster using Open OnDemand, please see our dedicated pages on utilizing Open OnDemand starting with {ref}`using-ood`.

## Using X11
When you launch a software application that uses a graphical user interface (GUI) from the command line, this is completed through X11 forwarding.

::::::{tab-set}
:::::{tab-item} Windows
If you use MobaXterm on Windows, X11 forwarding is turned on by default.

:::{tip}
You can test to see if x11 forwarding is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::
:::::
:::::{tab-item} Mac OS
From a Mac Terminal log in using the -Y option (`ssh -Y <yourusername>@login.discovery.neu.edu`).

:::{tip}
If you used the -Y option to enable X11 forwarding on your Mac, you can test to see if it is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::
:::::
::::::

[MobaXterm]: https://mobaxterm.mobatek.net/
[secure shell]: https://www.ssh.com/ssh/protocol/
[Terminal]: https://support.apple.com/guide/terminal/welcome/mac
[XQuartz]: https://www.xquartz.org/ 