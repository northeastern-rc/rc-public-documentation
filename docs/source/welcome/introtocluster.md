(intro-to-cluster)=
# Introduction to HPC and Slurm


:::{image} ../images/testwhite.svg
    :class: only-light
:::

:::{image} ../images/testgrey-blue.svg
    :class: only-dark
:::


## The HPC Cluster

Our cluster is a high-performance computing (HPC) resource available to the Northeastern University research community. The cluster is in the Massachusetts Green HPC Center (MGHPC) in Holyoke, MA. MGHPC is a 90,000 square food, 15-megawatt research computing and data center facility that houses computing resources for five institutions: Northeastern University, Boston University, Harvard University, the Massachusetts Institute of Technology (MIT), and the University of Massachesetts (UMass). 


:::{image} ../images/discovery.png
:::


## Slurm

We use the job scheduling manager `slurm` to perform vital actions in the cluster, including allocating access to a compute node for a duration of time so users can do their work. Slurm also allows the work that is performed on the cluster to be monitored (e.g., start time, end time, and memory resources used), and it manages the use of computing resources through a queue of pending jobs. 

To learn more about how to use slurm on the Northeastern cluster please see our {ref}` slurm documentation <_slurmguide>` or reach out to rchelp@northeastern.edu for any additional questions.


