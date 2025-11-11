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

(passwordless-ssh-windows)=
## Passwordless SSH On Windows Using MobaXterm
You must set up passwordless ssh to ensure that GUI-based applications launch without issues. Please make sure that your keys are added to the authorized.key file in your `~/.ssh` directory. This needs to be done anytime you regenerate your SSH keys. If you are having an issue opening an application that needs X11 forwarding, such as MATLAB or Schrodinger, and you recently regenerated your keys, make sure to add your keys to the authorized.key file.

1. Sign in to the cluster using MobaXterm.
1. Type `cd ~/.ssh` to move to your ssh folder.
1. Type `ssh-keygen -t rsa` to generate your key files.
1. Press `Enter` on all the prompts (do not generate a passphrase). If prompted to overwrite a file, type `Y`.
1. Type `cat id_rsa.pub >> authorized_keys`. This adds the contents of your public key file to a new line in `~/.ssh/authorized_keys`.

:::{note}
Errors that you can see on Windows when launching a GUI-based program include the following:

> `Error: unable to open display localhost:19.0`
>
> `Launch failed: non-zero return code`

If you are getting these types of errors, it could be because of the following reasons:

1. You still need to set up passwordless SSH. If so, you can follow the steps below to set up passwordless SSH.
1. When requesting a compute node from the login node, you may have forgotten to include the `--x11` option. Please see this example [srun](https://rc-docs.northeastern.edu/en/latest/using-discovery/srun.html?highlight=X11#srun-examples) command.
:::

(x11-windows)=
## X11 on Windows
If you use MobaXterm on Windows, X11 forwarding is turned on by default.

:::{tip}
You can test to see if x11 forwarding is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::

[MobaXterm]: https://mobaxterm.mobatek.net/
