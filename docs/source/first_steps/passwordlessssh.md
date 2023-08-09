(passwordless-ssh)=
# Passwordless SSH

You need to set up passwordless ssh to ensure that GUI-based applications will launch without any issues. You also need to make sure that your keys are added to the authorized.key file in your ~/.ssh directory. This needs to be done anytime you regenerate your ssh keys. If you're having an issue with opening an application that need X11 forwarding, such as MATLAB or Schrodinger, and you recently regenerated your keys, make sure to add your keys to the authorized.key file.

::::::{tab-set}
:::::{tab-item} Windows
**To set up passwordless ssh:**

1. Sign in to the cluster using MobaXterm.
1. Type `cd ~/.ssh` to move to your ssh folder.
1. Type `ssh-keygen -t rsa` to generate your key files.
1. Press `Enter` to all the prompts (do not generate a passphrase). If prompted to overwrite a file, type `Y`.
1. Type `cat id_rsa.pub >> authorized_keys`. This adds the contents of your public key file to a new line in the `~/.ssh/authorized_keys`.

:::{note}
Errors that you can see on Windows when launching a GUI-based program include the following:

> `Error: unable to open display localhost:19.0`
>
> `Launch failed: non-zero return code`

If you are getting these types of errors, it could be because of following reasons:

1. You haven't set up passwordless SSH. If that's the case, you can follow the steps below to set up passwordless SSH.
1. When requesting a compute node from the login node, you may have forgotten to include the `--x11` option. In that case please see this example [srun](https://rc-docs.northeastern.edu/en/latest/using-discovery/srun.html?highlight=X11#srun-examples) command for more details.
:::
:::::
:::::{tab-item} Mac OS
:::{note}
Make sure you’re on your local computer for steps 1 through 4. If you are connected to the cluster, type `exit` to return to your local computer.
:::

1. On a Mac, open the Terminal application and type `cd ~/.ssh`. This moves you to the ssh folder on your local computer.
1. Type `ssh-keygen -t rsa` to generate two files, `id_rsa` and `id_rsa.pub`.
1. Press `Enter` to all the prompts (do not generate a passphrase).
1. Type `ssh-copy-id -i ~/.ssh/id_rsa.pub <yourusername>@login.discovery.neu.edu` to copy `id_rsa.pub` to your `/home/.ssh` folder on Discovery. Enter your NU password if prompted. This copies the token from `id_rsa.pub` file to the `authorized_keys` file which will either be generated or appended if it already exists.
1. Connect to Discovery via `ssh <yourusername>@login.discovery.neu.edu`. You should now be connected without having to enter your password.

Now on the cluster,

6. Type `cd ~/.ssh` to move to your ssh folder.
1. Type `ssh-keygen -t rsa` to generate your key files.
1. Press Enter to all the prompts (do not generate a passphrase). If prompted to overwrite a file, type `Y`.
1. Type `cat id_rsa.pub >> authorized_keys`. This adds the contents of your public key file to a new line in the `~/.ssh/authorized_keys` file.
:::::
::::::