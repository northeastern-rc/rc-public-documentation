# Using R

[R](https://www.r-project.org/) is available as a [module](../software/modules.md) and
it is also an interactive app on Open onDemand [OOD](../using-ood/introduction.md). You can also use R with Anaconda. See [Working with Conda/Miniconda/Anaconda](./conda.md) and the [Anaconda documentation](https://docs.anaconda.com/anaconda/packages/r-language-pkg-docs/) for more information.

## Using R on Open onDemand

The Open onDemand app offers several different versions of R accessed through an interactive session with Rstudio server in a [Rocker Container](https://rocker-project.org/images/versioned/rstudio). Each version of R is available as a different *flavor* whereby different packages are pre-installed. We host three flavors whose package lists build off one another in the following order: Rstudio < Tidyverse < Geospatial.

In addition to different R packages you will find additional package requirements (e.g, compilers) also present in the three flavors in increasing order. 


:::{important}

If you have tried to install a package in the Rstudio or Tidyverse flavors and recieve an error message suggesting a necessary compiler is missing (e.g., glibc, CMAKE, zlib) or other "compilation failed" message. Please try and install the package again in the Geospatial flavor. If this still returns an error reach out to rchelp@northeastern.edu 

:::


## Creating a Packrat Environment (for R)

If you work with R packages, using a [Packrat environment](https://rstudio.github.io/packrat/) can be a helpful way to access packages across different sessions in the Open onDemand app, between the Open onDemand app and the command line, or between the different R flavors. Use the procedure below to create a Packrat environment on Discovery.

After you create a new directory for your R project, you can then use Packrat to store your package dependencies inside it.

We recommend making your packrat directory in /work (preferred) or /home

1. Connect to Discovery via ssh.

1. Type `module load R/4.2.1`.

1. Create a new directory for your R project by typing, `mkdir /work/<groupname>/<username>/<directoryname>` where `<groupname> is your group name, `<username>` is your username, and `<directoryname>` is the name of the directory you want to create for your R project. For example, `/work/coolsciencegroup/j.smith/packrat_r`.

1. Create a new directory for your R project by typing, `mkdir <directoryname>`

1. Open the R interface and install Packrat:

______________________________________________________________________

:::{code-block}
   install.packages("packrat") # install in a local directory, as you cannot install as root
:::

______________________________________________________________________

5. Initialize the environment where R packages will be written to:

______________________________________________________________________

:::{code-block}
   packrat::init("/work/<groupname>/<yourusername>/<directoryname>")
:::

______________________________________________________________________

You can then install R packages that you need. For example, to install a package called `rtracklayer`, type the following:

______________________________________________________________________

:::{code-block}
if (!requireNamespace("BiocManager", quietly = TRUE))
install.packages("BiocManager")
BiocManager::install("rtracklayer")
:::

______________________________________________________________________

**When using RStudio in the OOD App:**

The instructions below can be applied on any RStudio “flavor” available (i.e., RStudio, Geospatial, and Tidyverse). Once a packrat snapshot is created it can easily be transfered between flavors and even machines (e.g., personal laptop, Discovery).

1. Launch an RStudio instance on the OOD. Specify the flavor and other parameters as usual.
1. In the RStudio console type: `install.packages("packrat)`.

:::{note}
This will install by default in `$HOME/R/x86_64-pc-linux-gnu-library/<version>/` as long as you don’t have previous environments or those have been turned off (see below). For packrat installation, it is best to specify a “project folder” in your `$HOME`, `/scratch` or `/work` directory (if you do not have `/work` please see [here](https://rc-docs.northeastern.edu/en/latest/storage/discovery_storage.html) for access). The location `/tmp/Rtmp8CbQCA/downloaded_packages` would not work because `/tmp` corresponds to the compute node that you were on while running the R session. Optimally, you would like to have the packrat location in a persistent place so that all packages and libraries are available to you at all times regardless of the compute node you are on.
:::

3. Create a packrat project directory at the desired location by selecting “New Folder” in the “Files” tab in the lower right hand side of the RStudio screen. Alternatively, use `mkdir` in the terminal tab on the lower left-hand side of the RStudio screen. For example: `mkdir projectfolder`.

1. In the RStudio console, initialize the packrat. If your current directory is the project folder (i.e., `getwd()` == “packrat project folder”) you can omit the path here.

:::{code}
packrat::init("<path-to-project-folder>")
:::

5. You can now record all the currently installed packages to your packrat with the snapshot command. This may take some time if you have installed a lot of packages.

:::{code}
packrat::snapshot()
:::

6. And now you can check on the status of your packrat with:

:::{code}
packrat::status()
:::

7. Now turn packrat on. Packrat will now stay on for all your RStudio sessions and across the RStudio flavors (RStudio, geospatial, and tidyverse).

:::{code}
packrat::on()
:::

8. You can now install packages as normal. You should see the install location for your packrat project folder. E.g., “Installing package into ‘/work/groupname/username/packrat_R/’”

:::{code}
install.packages("viridis")
:::

## Packrat Tips

- At any time you can check the status of your packrat with `packrat::status()`.
- Packrat can be toggled on and off with `packrat::on()` and `packrat::off()`, respectively.
- To disconnect packrat and allow for package installation outside of your packrat project folder: `packrat::disable(project = NULL, restart = TRUE)`, where `project` refers to the current packrat project folder, and `restart = TRUE` will restart the R session.
- To re-initialize packrat run: `packrat::init("<path-to-packrat-project-folder>")`. This will automatically restart your R session.
- A package can be removed from packrat via: `remove.packages("viridis)`, but will remain in your packrat snapshot and can be restored with: `packrat::restore()`.
- The function `packrat::clean(dry.run=T)` will list any unused packages that were installed in your snapshot. You can remove them with: `packrat::clean()`.

:::{note}
For most cases, having a single packrat directory is sufficient, unless you notice specific package conflicts or need different versions of the same package. A single packrat directory also saves from having to install the same dependencies multiple times in different locations.
:::

If the installation location is not setting to your project folder you may need to turn off these environments. In some cases, these folders could also be present in your `/work/groupname/<project-name>` directory.

:::{code-block} bash
mv ~/.rstudio ~/.rstudio-off
mv ~/.local ~/.local-off
mv ~/ondemand ~/ondemand.off
mv ~/.Rprofile ~/.Rprofile.off
mv ~/.Rhistory ~/.Rhistory.off
:::
