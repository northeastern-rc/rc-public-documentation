(using-gpus-index)=
# Working with GPUs

```{toctree}
:hidden:
:maxdepth: 3

gpuoverview
accessinggpus
gpujobsubmission
```

Harnessing the power of Graphics Processing Units (GPUs) can significantly accelerate your computations on our High-Performance Computing (HPC) cluster. This section provides insights into using GPUs effectively, from understanding their capabilities to best practices for optimization.


::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`home;1.5em;sd-mr-1` GPUs on our HPC
:link: gpuoverview
:link-type: doc

Overview of the GPUs on the HPC.
+++
[Learn more »](gpuoverview)
:::
:::{grid-item-card} {octicon}`home;1.5em;sd-mr-1` GPU Access
:link: accessinggpus
:link-type: doc

How to utilize GPUs interactively (srun) and passively (sbatch).
+++
[Learn more »](accessing-gpus)
:::
:::{grid-item-card} {octicon}`home;1.5em;sd-mr-1` GPU Job Submission
:link: gpujobsubmission
:link-type: doc

Using CUDA and building deep learning environments.
+++
[Learn more »](gpujobsubmission)
:::

:::{grid-item-card} {octicon}`home;1.5em;sd-mr-1` Access to the `multigpu` Partition
:link: gpuoverview
:link-type: doc

Overview of the GPUs on the HPC.
+++
[Learn more »](gpuoverview)
::::

:::{include} ../_snippets/helpfooter.md
:::
