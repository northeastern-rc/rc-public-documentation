(connecting-on-mac)=
# Connecting on Mac

Mac computers come with a Secure Shell (SSH) program called [Terminal] that you use to connect to the HPC using SSH. If you need to use software that uses a GUI, such as Matlab or Maestro, make sure to use the -Y option in the second step below using X11 forwarding.

:::{note}
If you use Mac OS X version 10.8 or higher, and you have [XQuartz] running in the background to do X11 forwarding, you should execute the following command in Terminal once before connecting:

`defaults write org.macosforge.xquartz.X11 enable_iglx -bool true`

You should keep XQuartz running in the background. If you close and restart XQuartz, you will need to execute the above command again after restarting. Do not use the Terminal application from within XQuartz to sign in to Discovery. Use the default Terminal program that comes with your Mac (see Step 1 in the procedure below).
:::

## Connecting To Cluster On A Mac

1. Go to Finder > Applications > Utilities, and then double click Terminal.
1. At the prompt, type `ssh <username>@login.discovery.neu.edu`, where `<username>` is your Northeastern username. If you need to use X11 forwarding, type `ssh -Y <username>@login.discovery.neu.edu`.
1. Type your Northeastern password and press `Enter`.

You are now connected to Discovery at a login node.

Watch this video of how to connect to Discovery on a Mac. If you do not see any controls on the video, right-click on the video to see viewing options.

<video width="720" height="480" controls>
  <source src="../../_static/video/connect_mac_terminal.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

(x11-mac)=
## X11 on Mac OS
From a Mac Terminal log in using the -Y option (`ssh -Y <yourusername>@login.discovery.neu.edu`).

:::{tip}
If you used the -Y option to enable X11 forwarding on your Mac, you can test to see if it is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::

[Terminal]: https://support.apple.com/guide/terminal/welcome/mac
[XQuartz]: https://www.xquartz.org/
