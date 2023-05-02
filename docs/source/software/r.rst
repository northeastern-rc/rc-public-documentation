***************
Working with R
***************
`R <https://www.r-project.org/>`_ is available as a module (see :ref:`using_module` for more information) and
Rstudio is also an interactive app on Open onDemand (see :ref:`using_ood` for more information). You can also use R with Anaconda. See :ref:`working_conda` and the `Anaconda documentation <https://docs.anaconda.com/anaconda/packages/r-language-pkg-docs/>`_ for more information

If you work with R packages, using a Packrat environment can be helpful. Use the procedure below to create a Packrat environment on Discovery.

Creating a Packrat Environment (for R)
======================================

Packrat is an application that helps you manage packages for R. Packrat allows for greater reproducibility because it saves the exact package version that you installed, it's portable from one machine to another (or node-to-node in HPC land), and it's isolated, allowing you to create separate project directories and avoid potential package conflicts. After you create a new directory for your R project, you can then use Packrat to store your package dependencies inside it. For more information about Packrat, see the website: https://rstudio.github.io/packrat/.

**When using R in the command line:**

1. Connect to Discovery.
2. Type ``module load R/3.6.2``.
3. Create a new directory for your R project by typing, ``mkdir /scratch/<yourusername>/<directoryname>`` where ``yourusername`` is your user name, and ``directoryname`` is the name of the directory you want to create for your R project. For example, ``/scratch/j.smith/packrat_r``
4. Open the R interface and install Packrat::

    install.packages("packrat") #during the installation, you will be prompted to install in a local directory, as you cannot install as root

5. Initialize the environment where R packages will be written to::

    packrat::init("/scratch/<yourusername>/<directoryname>")

You can then install R packages that you need. For example, to install a package called ``rtracklayer``, type the following::

   if (!requireNamespace("BiocManager", quietly = TRUE))
   install.packages("BiocManager")
   BiocManager::install("rtracklayer")

**When using Rstudio in the OOD App:**

1. Launch an RStudio instance on the OOD.
2. In the Rstudio console type:

         ``install.packages("packrat)`` 

.. note::
        This will install by default in ``$HOME/R/x86_64-pc-linux-gnu-library/<version>/`` as long as you don't have previous environments or those have been turned off (see below). For packrat installation, it is best to specify a "project folder" in your $HOME, /scratch or /work directory (if you do not have /work please see here for access). The location /tmp/Rtmp8CbQCA/downloaded_packages would not work because /tmp corresponds to the compute node that you were on while running the R session. Optimally, you would like to have the packrat location in a persistent place so that all packages and libraries are available to you at all times regardless of the compute node you are on. 

3. In the Rstudio terminal (the second tab in the lower left quad) create the packrat project directory at the desired location using ``mkdir``. Or you can select "New Folder" in the "Files" tab in the lower right hand side.
 
        ``mkdir projectfolder``

4. In the Rstudio console, initialize the packrat. If your current directory is the project folder (i.e., ``getwd()`` == "packrat project folder") you can omit the path here. 

        ``packrat::init("<path-to-project-folder>")`` 

5. You can now record all the currently installed packages to your packrat with the ``snapshot`` command. This may take some time if you have installed a lot of packages.

        ``packrat::snapshot()``

6. And now you can check on the status of your packrat with: 

        ``packrat::status()``

7. Now turn packrat on. Packrat will now stay on for all your Rstudio sessions and across the Rstudio flavors (Rstudio, geospatial, and tidyverse).

        ``packrat::on()``

8. You can now install packages as normal. You should see the install location for your packrat project folder. E.g., "Installing package into ‘/work/groupname/username/packrat_R/'"

        ``install.packages("viridis")``


A few Packrat tips
==================

* At any time you can check the status of your packrat with ``packrat::status()`` 

* Packrat can be toggled on and off with ``packrat::on()`` and ``packrat::off()`` respectively. 

* To disconnect packrat and allow for package installation outside of your packrat project folder: ``packrat::disable(project = NULL, restart = TRUE)`` Where ``project`` refers to the current packrat project folder, and ``restart = TRUE`` will restart the R session.

* To re-initialize packrat run: ``packrat::init("<path-to-packrat-project-folder>")`` This will automatically restart your R session.

* A package can be removed from packrat via: ``remove.packages("viridis)``, but will remain in your packrat snapshot and can be restored with: ``packrat::restore()``

* The function ``packrat::clean(dry.run=T)`` will list any unused packages that were installed in your snapshot. You can remove them with: ``packrat::clean()``

.. note:: 
        For most cases, having a single packrat directory is sufficient, unless you notice specific package conflicts or need different versions of the same package. A single packrat directory also saves from having to install the same dependencies multiple times in different locations.

**To turn-off previously set environments**

If you find the install location is not setting to your project folder you may need to turn-off these environments. In some cases, these folders could also be present in your `/work/groupname/<project-name>` directory. 

        ``mv ~/.rstudio ~/.rstudio-off``

        ``mv ~/.local ~/.local-off``

        ``mv ~/ondemand ~/ondemand.off``
        
        ``mv ~/.Rprofile ~/.Rprofile.off``
        
        ``mv ~/.Rhistory ~/.Rhistory.off``

