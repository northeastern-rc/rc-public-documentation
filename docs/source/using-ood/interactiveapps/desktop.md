(desktop)=
# Desktop

This Open OnDemand application is a containerized desktop running on the HPC cluster. It has access to these tools/programs:

- Slurm (for running Slurm commands via the terminal in the desktop and interacting on compute nodes)
- Module command (for loading and running HPC-ready modules)
- File explorer (able to traverse and view files that you have access to on the HPC)
- Firefox web browser
- VLC media player
- Office Libre suite of applications (word processing, spreadsheets, presentation applications)

:::{note}
The desktop application is a Singularity container: a Singularity container cannot run inside. It will fail if a user tries to run a module or program that runs a container inside this application.
:::