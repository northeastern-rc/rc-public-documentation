(make)=
# Make

If you want to use `make` to add software locally to your path, you must first download the software package from its source (such as a webpage or GitHub) and unpack it or unzip it if need be. Then, you must set the installation path to a directory with write access on Discovery, such as your home directory. You can use `./configure` to do this, such as  `./configure --prefix=/home/<yourusername>/software` After you have set the installation path, you need to compile the code using `make` and then install the software using `make install`.

## Makefile Example: Installing FFTW Library

Even without root access, you can install software system-wide by installing it in your home directory. Let's continue with the FFTW library as an example.

1. Download the FFTW tarball. Here, we download version 3.3.9:

:::{code} bash
cd ~
wget http://www.fftw.org/fftw-3.3.9.tar.gz
:::

2. Extract the tarball:

:::{code} bash
tar xzf fftw-3.3.9.tar.gz
:::

3. Move into the directory:

:::{code} bash
cd fftw-3.3.9
:::

4. Configure the build process, specifying the prefix as a location in your home directory. This location is where the library will be installed. Note that the specified directory should be in your `PATH` to ensure system-wide accessibility.

:::{code} bash
./configure --prefix=$HOME/fftw
:::

5. Compile the software:

:::{code} bash
make -j 8
:::

6. Instead of `make install` (which typically requires root access for system-wide installation), you can `make install` with the prefix configuration to install the software in your home directory.

:::{code} bash
make install
:::

The FFTW library should now be installed in the `fftw` directory in your home directory.

Remember to include this location in your PATH if it still needs to be included. You can do this by editing your shell profile (e.g., `~/.bashrc` for bash or `~/.zshrc` for zsh) and adding the following line:

:::{code} bash
export PATH=$HOME/fftw/bin:$PATH
:::

This line ensures the system can find the FFTW library binaries when needed. Note that you will need to source your profile or restart your shell for these changes to take effect:

:::{code} bash
source ~/.bashrc
:::

Always refer to the specific installation instructions of the software you're installing. If the software requires dependencies not installed on the system, you might need to install those in your home directory manually.
