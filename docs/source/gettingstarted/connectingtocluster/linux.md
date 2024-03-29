(connecting-on-linux)=
# Connecting on Linux

Linux computers come with a Secure Shell (SSH) program called Terminal that you use to connect to the HPC using SSH. If you need to use software that uses a GUI, such as Matlab or Maestro, make sure to use the -Y option in the second step below using X11 forwarding.

## Connecting to the Cluster on Linux

1. Search for the Terminal application from the launcher menu.
1. At the prompt, type `ssh <username>@login.discovery.neu.edu`, where `<username>` is your Northeastern username. If you need to use X11 forwarding, type `ssh -Y <username>@login.discovery.neu.edu`.
1. Type your Northeastern password and press `Enter`.

You are now connected to Discovery at a login node.

(passwordless-ssh-linux)=
## Passwordless SSH In Linux
You must set up passwordless ssh to ensure that GUI-based applications launch without issues. Please make sure that your keys are added to the authorized.key file in your `~/.ssh` directory. This needs to be done anytime you regenerate your SSH keys. If you are having an issue opening an application that needs X11 forwarding, such as MATLAB or Schrodinger, and you recently regenerated your keys, make sure to add your keys to the authorized.key file.

:::{note}
Ensure you’re on your local computer for steps 1 through 4—type `exit` to return to your local computer if connected to the cluster.
:::

1. Open the Terminal application and type `cd ~/.ssh`. This moves you to the ssh folder on your local computer.
1. Type `ssh-keygen -t rsa` to generate two files, `id_rsa` and `id_rsa.pub`.
1. Press `Enter` on all the prompts (do not generate a passphrase).
1. Type `ssh-copy-id -i ~/.ssh/id_rsa.pub <yourusername>@login.discovery.neu.edu` to copy `id_rsa.pub` to your `/home/.ssh` folder on Discovery. You can enter your NU password if prompted. This copies the token from `id_rsa.pub` file to the `authorized_keys` file, which will either be generated or appended if it already exists.
1. Connect to Discovery via `ssh <yourusername>@login.discovery.neu.edu`. You should now be connected without having to enter your password.

**Now on the cluster,**

1. Type `cd ~/.ssh` to move to your ssh folder.
1. Type `ssh-keygen -t rsa` to generate your key files.
1. Press Enter on all the prompts (do not generate a passphrase). If prompted to overwrite a file, type `Y`.
1. Type `cat id_rsa.pub >> authorized_keys`. This adds the contents of your public key file to a new line in the `~/.ssh/authorized_keys` file.

(x11-linux)=
## X11 on Linux
To use X11 forwarding, from the Terminal application, log in using the -Y option (`ssh -Y <yourusername>@login.discovery.neu.edu`).

:::{tip}
If you used the -Y option to enable X11 forwarding on your Linux machine, you can test to see if it is working by typing `xeyes`. This will run a small program that makes a pair of eyes appear to follow your cursor.
:::
