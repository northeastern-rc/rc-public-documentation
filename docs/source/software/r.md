# Using R

[R](https://www.r-project.org/) is available as a module (see [Using Module](../software/modules.md) for more information) and
it is also an interactive app on Open onDemand (see [Introduction to Open OnDemand (OOD)](../using-ood/introduction.md) for more information). You can also use R with Anaconda. See [Working with Conda/Miniconda/Anaconda](./conda.md) and the [Anaconda documentation](https://docs.anaconda.com/anaconda/packages/r-language-pkg-docs/) for more information

If you work with R packages, using a Packrat environment can be helpful. Use the procedure below to create a Packrat environment on Discovery.

## Creating a Packrat Environment (for R)

Packrat is an application that helps you manage packages for R. After you create a new directory for your R project, you can then use Packrat to store your package dependencies inside it. For more information about Packrat, see the website: <https://rstudio.github.io/packrat/>.

1. Connect to Discovery.

1. Type `module load R/4.2.1`.

1. Create a new directory for your R project by typing, `mkdir /scratch/<username>/<directoryname>` where `<username>` is your username, and `<directoryname>` is the name of the directory you want to create for your R project. For example, `/scratch/j.smith/packrat_r`.

1. Create a new directory for your R project by typing, `mkdir /scratch/<yourusername>/<directoryname>` where `yourusername` is your user name, and `directoryname` is the name of the directory you want to create for your R project. For example, `/scratch/j.smith/r_testlab`

1. Open the R interface and install Packrat:

______________________________________________________________________

:::{code-block}
   install.packages("packrat") # install in a local directory, as you cannot install as root
:::

______________________________________________________________________

5. Initialize the environment where R packages will be written to:

______________________________________________________________________

:::
   packrat::init("/scratch/<yourusername>/<directoryname>")
:::

______________________________________________________________________

You can then install R packages that you need. For example, to install a package called `rtracklayer`, type the following:

______________________________________________________________________

:::
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