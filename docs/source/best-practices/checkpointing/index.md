(checkpoint-jobs)=
# Checkpointing Jobs

```{toctree}
:hidden:
:maxdepth: 3

application-level
ml-model-level
```

Checkpointing is a technique used to save a snapshot of the state of a program at regular intervals. 

This allows for restarting the program from the saved state in case of any failures or job interruption.

:::{image} ../images/checkpointing.png
---
width: 300
alt: Checkpointing algorithm flow chart.
align: right
:::

Checkpointing can be implemented at different levels of the workflow, such as application-level, user-level, system-level or model-level (e.g. in ML). We'll discuss the application level and model level checkpointing.

:::{note}
Some packages can be used to implement checkpointing if you are developing in Python, Matlab, or R. Some examples include [Python PyTorch checkpointing], [TensorFlow checkpointing], [MATLAB checkpointing], and [R checkpointing]. Additionally, many Computational Chemistry and Molecular Dynamics software packages have built-in checkpointing options (e.g., [GROMACS] and [LAMMPS]).
:::

Implementing checkpointing can be achieved by the following:
- Some save-and-load mechanisms of your calculation state.
- The use of [Slurm Job Arrays].

:::{note}
To overcome partition time limits, replace your single long job with multiple shorter jobs. Then, use job arrays to set each job to run one after the other. If checkpointing is used, each job will write a checkpoint file. The following job will use the latest checkpoint file to continue from the latest state of the calculation.
:::



::::{grid} 3
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`repo-forked;1.5em;screen-full` Application-Level Checkpointing
:link: application-level
:link-type: doc

Using Checkpointing at application level.

+++
[Learn more »](application-level)
:::

:::{grid-item-card} {octicon}`versions;1.5em;sd-mr-1` Model-Level Checkpointing
:link: ml-model-level
:link-type: doc

Using Checkpointing at model level, e.g. for ML models.

+++
[Learn more »](ml-model-level)
:::


::::






[GROMACS]: https://manual.gromacs.org/documentation/current/user-guide/managing-simulations.html
[LAMMPS]: https://docs.lammps.org/restart.html
[MATLAB checkpointing]: https://www.mathworks.com/help/gads/work-with-checkpoint-files.html
[Python PyTorch checkpointing]: https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html
[R checkpointing]: https://cran.r-project.org/web/packages/checkpoint/vignettes/checkpoint.html
[Slurm Job Arrays]: https://slurm.schedmd.com/job_array.html
[TensorFlow checkpointing]: https://www.tensorflow.org/guide/checkpoint
