***************
Working with R
***************
`R <https://www.r-project.org/>`_ is available as a module (see :ref:`using_module` for more information) and
it is also an interactive app on Open onDemand (see :ref:`using_ood` for more information). You can also use R with Anaconda. See :ref:`working_conda` and the `Anaconda documentation <https://docs.anaconda.com/anaconda/packages/r-language-pkg-docs/>`_ for more information

If you work with R packages, using a Packrat environment can be helpful. Use the procedure below to create a Packrat environment on Discovery.

Creating a Packrat Environment (for R)
======================================

Packrat is an application that helps you manage packages for R. After you create a new directory for your R project, you can then use Packrat
to store your package dependencies inside it. For more information about Packrat, see the website: https://rstudio.github.io/packrat/.

1. Connect to Discovery.
2. Type ``module load R/3.6.2``.
3. Create a new directory for your R project by typing, ``mkdir /scratch/<yourusername>/<directoryname>`` where ``yourusername`` is your user name, and ``directoryname`` is the name of the directory you want to create for your R project. For example, ``/scratch/j.smith/r_testlab``
4. Open the R interface and install Packrat::

    install.packages("packrat") #during the installation, you will be prompted to install in a local directory, as you cannot install as root

5. Initialize the environment where R packages will be written to::

    packrat::init("/scratch/<yourusername>/<directoryname>")

You can then install R packages that you need. For example, to install a package called ``rtracklayer``, type the following::

   if (!requireNamespace("BiocManager", quietly = TRUE))
   install.packages("BiocManager")
   BiocManager::install("rtracklayer")
