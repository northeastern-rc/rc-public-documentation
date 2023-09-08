(desktop-app)=
# Desktop App

Open OnDemand provides a containerized desktop to run on the HPC cluster.

The following tools and programs are accessible on our Desktop App:

- Slurm (for running Slurm commands via the terminal in the desktop and interacting on compute nodes)
- Module command (for loading and running HPC-ready modules)
- File explorer (able to traverse and view files that you have access to on the HPC)
- Firefox web browser
- VLC media player
- LibreOffice suite of applications (word, spreadsheet, and presentation processing)

:::{note}
The desktop application is a {term}`Singularity` container; a Singularity container cannot run inside the desktop application. It fails if users run a container-based module or program via the desktop application.
:::
