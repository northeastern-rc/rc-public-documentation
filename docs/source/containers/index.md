(containers)=
# Containers on Explorer
```{toctree}
:hidden:
:maxdepth: 4

apptainer
```

A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. ([Reference](https://www.docker.com/resources/what-container/))

Containers allow reproducibility and portability in scientific workflows.

They ensure that scientific experiments can be reproduced on any system, such as our laptop, our friend’s laptop, HPC as well as public cloud-based environments. Containers achieve this by encapsulating the entire software environment of the specific analysis or simulation. This eliminates the "it works on my machine" problem by providing a consistent runtime environment across various platforms.

This consistency also allows for more collaboration, allowing researchers to share their work without encountering compatibility issues, thereby speeding up scientific workflows.

Containers also simplify software dependency issues by isolating software and its dependencies from the underlying HPC environment. This reduces project conflicts and makes managing different software versions much more accessible.

We recommend using containers on the HPC because they provide isolation from the HPC environment and complete control of the software environment to the researcher. Many technologies exist that could be used for containerization, including Docker, Podman, and Singularity/Apptainer. On Explorer, we use Apptainer/Singularity as the containerization engine, however, Apptainer/Singularity can work with containers built with Docker or Podman.


::::{grid} 1 2 3 4
:gutter: 1 1 1 2


:::{grid-item-card} {octicon}`book;1.5em;sd-mr-1` Apptainer on Explorer
:link: apptainer
:link-type: doc
 
 See how to use containers on HPC
 +++
 :::{grid-item-card} {octicon}list;1.5em;sd-mr-1 List of Available Containers:link: containers offered :link-type: doc
