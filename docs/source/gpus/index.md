(using-gpus-index)=
# Using GPUs on our HPC Cluster

```{toctree}
:hidden:
:maxdepth: 3

gpuoverview
accessinggpus
jobsubmission
bestpractices
```

Harnessing the power of Graphics Processing Units (GPUs) can significantly accelerate your computations on our High-Performance Computing (HPC) cluster. This section provides insights into using GPUs effectively, from understanding their capabilities to best practices for optimization.

::::{grid} 4

:::{grid-item-card} {ref}`gpu-overview`
:::
:::{grid-item-card} {ref}`accessing-gpus`
:::
:::{grid-item-card} {ref}`gpu-job-submission`
:::
:::{grid-item-card} {ref}`best-practices-gpus`
:::
::::

(gpu-overview-index)=
## GPU Overview
Get acquainted with the capabilities and benefits of using GPUs in our HPC cluster.

- **GPU Types**: An overview of the GPU hardware available.
- **Benefits**: Understand how GPUs can accelerate your computations.

:::{seealso}
{ref}`More about GPU Overview <gpu-overview>.`
:::

(accessing-gpus-index)=
## Accessing GPUs

Learn how to access and request GPU resources for your tasks.

- **Available GPUs**: Details on the GPUs available for use.
- **Reservation**: How to reserve GPU resources for your jobs.

:::{seealso}
{ref}`More about Accessing GPUs <accessing-gpus>.`
:::

(gpu-job-submission-index)=
## GPU Job Submission

Discover how to submit jobs that utilize GPU resources effectively.

- **GPU Job Scripts**: Creating job scripts for GPU-accelerated tasks (e.g., CUDA and Deep Learning).
- **Monitoring GPU Usage**: Tools and commands to monitor GPU resources.

:::{seealso}
{ref}`More about Job Submission <job-submission>.`
:::

(best-practices-gpu-index)=
## Best Practices for GPUs

Optimize your GPU-based computations with best practices and tips.

- **GPU Memory Management**: Efficiently manage GPU memory usage.
- **Parallelization**: Strategies for parallelizing tasks for GPUs.

:::{seealso}
{ref}`More about Best Practices for GPUs <best-practices-gpus>.`
:::

:::{include} ../_snippets/helpfooter.md
:::