(faqs-new)=
# Frequently Asked Questions (FAQs)
Below are some common questions and answers regarding our HPC cluster and its operation.

::::{dropdown} - My OOD job shutsdown/completes quickly before/during/after starting? OR <br> - When I try and launch an OOD job, I get: "Disk quota exceeded" error. OR <br> - My OOD Desktop job starts and quickly moves to `Completed` without starting..

There are two main things to check:
1. Check that the memory available in `/home/$USER` is less than the quota limit.

There are storage quotas on `$HOME` directories. (See {ref}`home-directory-storage-quota` for more details). OOD applications run from the `$HOME` directory and it is important that there is enough space in `$HOME` for the OOD application to run.

In the terminal, run `du -shc .[^.]* * /home/$USER`, which should have output similar to the following:
:::{code-block} shell
[<username>@<host> ~]$  du -shc .[^.]* * /home/$USER/
39M     .git
106M    discovery-examples
41K     README.md
3.3M    software-installation
147M    total
:::

Based on the output, we can check which files are consuming how much memory, and which files can be removed to free up memory.

2. Check if there are other scripts running at startup (in `.bashrc`), or an anaconda or other environments loading at startup.
   
We recommend loading other scripts/environments after your main environment has been loaded. We recommend activating any conda environments _after_ the main environment has been loaded. If there are other scripts/environments you'd like to run, we recommend creating a separate bash script and sourcing it once the main environment has been loaded. For more details on the `.bashrc` file and best practices, see {ref}`about-bashrc`.
::::

::::{dropdown} Can I install my software on the HPC cluster?
Yes, you can. Please follow the guidelines in the {ref}`package-managers` and {ref}`from-source` sections. If you encounter any issues, contact Research Computing. To contact RC, see {ref}`getting-help`.
::::
