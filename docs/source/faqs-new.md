(faqs-new)=
# Frequently Asked Questions (FAQs)
Below are some common questions and answers regarding our HPC cluster and its operation.

::::{dropdown} How do I check my `/home/$USER` disk usage?
Run `du -shc .[^.]* * /home/$USER` which will output:
:::{code-block} shell
[<username>@<host> ~]$  du -shc .[^.]* * /home/$USER/
39M     .git
106M    discovery-examples
41K     README.md
3.3M    software-installation
147M    total
:::
::::

::::{dropdown} Can I install my software on the HPC cluster?
Yes, you can. Please follow the guidelines in the {ref}`package-managers` and {ref}`from-source` sections. If you encounter any issues, contact Research Computing.
::::
