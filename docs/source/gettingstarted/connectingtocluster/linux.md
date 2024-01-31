(connecting-on-linux)=
# Connecting on Linux

Linux computers come with a Secure Shell (SSH) program called Terminal that you use to connect to the HPC using SSH. If you need to use software that uses a GUI, such as Matlab or Maestro, make sure to use the -Y option in the second step below using X11 forwarding.

## Connecting To the Cluster on Linux

1. Search for the Terminal application from the launcher menu.
1. At the prompt, type `ssh <username>@login.discovery.neu.edu`, where `<username>` is your Northeastern username. If you need to use X11 forwarding, type `ssh -Y <username>@login.discovery.neu.edu`.
1. Type your Northeastern password and press `Enter`.

You are now connected to Discovery at a login node.

(x11-linux)=
## X11 on Linux
To use X11 forwarding, from the Terminal appication, log in using the -Y option (`ssh -Y <yourusername>@login.discovery.neu.edu`).

:::{tip}
If you used the -Y option to enable X11 forwarding on your Linux machine, you can test to see if it is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::
