(from-source)=
# From Source
```{toctree}
:hidden:
:maxdepth: 3

makefile
cmake
```
## System-Wide Software
::::{grid} 2

:::{grid-item-card} {ref}`make`
:::
:::{grid-item-card} {ref}`cmake`
:::
::::

(installing-your-own-module)=
### Installing Your Own Module
In addition to the pre-installed software on our HPC cluster, users may need to install their software. This section outlines the general steps for doing so.

1. Check If the Software Is Already Installed

Before installing new software, check if it is already installed by using the `module avail` command:

:::{code} bash
module avail
:::

This command lists all the available modules (i.e., software) on the system.

2. Choose the Appropriate Location for Installation

Users should install their software in their home directory or a designated project directory to avoid permission issues. For example:

:::{code} bash
cd /home/<username>/software
:::

Replace `<username>` with your username.

3. Download the Software

Download the software package using `wget` or `curl`, for example:

:::{code} bash
wget http://example.com/software.tar.gz
:::

Ensure to replace `http://example.com/software.tar.gz` with the actual URL of the software package.

4. Extract the Software

Most software packages are distributed as compressed files that must be extracted.

:::{code} bash
tar -xvzf software.tar.gz
:::

Replace `software.tar.gz` with the actual filename of the software package.

5. Install the Software

Installation steps can vary widely between different programs. Many use the `configure`, `make`, `make install` steps, like this:

:::{code} bash
cd software_directory   # Replace with actual directory
./configure --prefix=/home/<username>/software
make
make install
:::

Replace `<username>` with your username and `software_directory` with the actual directory of the software.

:::{note}
Always read the software's installation instructions, as steps may vary.
:::

6. Test the Software

After installation, it is important to test the software to ensure it works correctly. Most software packages include a set of test cases for this purpose. Refer to the software's documentation for how to run these tests.

:::{figure} ../../_static/image/build-diagram.jpg

A workflow of software installation (replace with our own).
:::

7. Make the Software Available via Modules

For ease of use, consider creating a module file for the software. Here is an example of a basic module file for software installed in `/home/<username>/software`:

:::{code} bash
#%Module
set root /home/<username>/software
prepend-path PATH $root/bin
prepend-path LD_LIBRARY_PATH $root/lib
:::

Replace `<username>` with your username.

:::{table} Common Software Installation Commands

| Command      | Description                           |
|--------------|---------------------------------------|
| module avail | List all available modules            |
| cd           | Change the current directory          |
| wget or curl | Download files                        |
| tar          | Extract files from a tarball          |
| ./configure  | Configure the software for the system |
| make         | Compile the software                  |
| make install | Install the software                  |
:::

Following these steps, users should be able to install most software packages on their own. However, always refer to the specific software's documentation, as steps can vary. If you run into issues or need help, please contact support.
