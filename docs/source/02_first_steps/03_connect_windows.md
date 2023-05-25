(connect-windows)=

# Connecting Windows

You connect to Discovery using a [secure shell](https://www.ssh.com/ssh/protocol/) program to initiate an SSH session to
sign in to Discovery. This topic is about how to connect using Windows. See [connect mac](./02_connect_mac.md) for information about connecting with a Mac.

% 2FA Authentication with DUO

% ============================

% When you connect to Discovery you are required to complete two-factor authentication (2FA) using the app Duo. All Northeastern staff, faculty, and students

% should already have Duo, as it is used with many other online campus resources, such as Canvas and myNortheastern. To learn more about using Duo,

% go to `Northeastern's 2FA informational website <https://get2fa.northeastern.edu/>`_.

Before you can connect to Discovery on a Windows computer, you’ll need to download a terminal program,
such as [MobaXterm](https://mobaxterm.mobatek.net/) or PuTTY. We recommend MobaXterm, as you can also use it for file transfer,
whereas with other SSH programs, you would need a separate file transfer program.

**To connect to Discovery with MobaXterm:**

1. Open MobaXterm.
2. Click **Session**, then click **SSH** as the connection type.
3. In **Remote Host**, type `login.discovery.neu.edu`, make sure **Port** is set to 22, and click **OK**.
   (OPTIONAL: You can type your Northeastern username and password on MobaXterm, and it will save that information every time you sign in. If you opt to do this, you will be connected to Discovery after you click OK.)
4. At the prompt, type your Northeastern username and press Enter.
5. Type your Northeastern password and press Enter. Note that the cursor does not move as you type your password. This is expected behavior.

You are now connected to Discovery at a login node.

Watch this video to see how to connect to Discovery with MobaXterm. If you do not see any controls on the video, right click on the video to see viewing options.

<video width="720" height="480" controls>
  <source src="../_static/video/windows_moba_connect.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<!-- ![Alt text](../_static/video/windows_moba_connect.mp4) -->


## Passwordless ssh on Windows

You need to setup passwordless ssh to ensure that GUI-based applications will launch without any issues. You also
need to make sure that your keys are added to the authorized.key file. This needs to be done anytime you regenerate your keys. If you're having
an issue with opening an application that need X11 forwarding, such as MATLAB or Schrodinger, and you recently regenerated your keys, make sure to
add your keys to the authorized.key file.

:::{note}
> Errors that you can see on Windows when launching a GUI-based program include the following:
>
> `Error: unable to open display localhost:19.0`
>
> `Launch failed: non-zero return code`

If you are getting these types of errors, follow the steps below to set up passwordless ssh.
:::

**To setup passwordless ssh:**

1. Sign into Discovery using MobaXterm.
2. Type `cd ~/.ssh` to move to your ssh folder.
3. Type `ssh-keygen -t rsa` to generate your key files.
4. Press `Enter` to all of the prompts (do not generate a passphrase). If prompted to overwrite a file, type `Y`.
5. Type `cat id_rsa.pub >> authorized_keys`. This adds the contents of your public key file to a new line in the `~/.ssh/authorized_keys`.

The following video tutorial goes through this process.

% .. raw:: html

% <video width="710" autoplay mute controls>

% <source src="../video/windows_passwordless.mp4" type="video/mp4">

% Your browser does not support embedded videos.

% </video>

(windows-next-steps)=
### Next steps

After you are connected, you can run jobs either in interactive mode with `srun` or submit a script using `sbatch`. See {ref}`using-slurm` and {ref}`using-sbatch` for more information.

To load and run software, see {ref}`software-overview`.
To find out more about the hardware and partitions on Discovery, see {ref}`hardware-overview` and {ref}`partitions`.

To watch an introductory training video, go to [Northeastern's LinkedIn Learning page](https://www.linkedin.com/checkpoint/enterprise/login/74653650?pathWildcard=74653650&application=learning&redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Flearning%2Fcontent%2F1139340%3Fu%3D74653650).
