<!--#  NEU's HPC Docs-->

# NU's High-Performance Computing (HPC)

::::{grid}
:reverse:
:gutter: 3 4 4 4
:margin: 1 2 1 2

:::{grid-item}
:columns: 12 4 4 4

```{image}  _static/logo-square.png
:width: 200px
:class: sd-m-auto
:name: landing-page-logo
```

:::

:::{grid-item}
:columns: 12 8 8 8
:child-align: justify
:class: sd-fs-5

```{rubric} Welcome to HPC Cluster online documentation.
```
A dedicated platform for researchers, scholars, and students to access, learn, and leverage our state-of-the-art HPC resources.

````{div} sd-d-flex-row


```{button-ref} welcome/welcome
:ref-type: doc
:color: primary
:class: sd-rounded-pill sd-mr-3

Get Started
```

```{button-ref} first_steps/get_access
:ref-type: doc
:color: secondary
:class: sd-rounded-pill sd-mr-3

Get Access
```
```{button-ref} welcome/gettinghelp
:ref-type: doc
:color: secondary
:class: sd-rounded-pill

Get Help
```
````

:::

::::

---

::::{grid} 1 2 2 3
:gutter: 1 1 1 2

:::{grid-item-card} {octicon}`markdown;1.5em;screen-full` Open OnDemand (OOD)
:link: using-ood/introduction.rst
:link-type: ref

OOD provides a various available software interactively through your favorite browser.

+++
[Learn more »](using-ood/introduction.rst)
:::

:::{grid-item-card} {octicon}`plug;1.5em;sd-mr-1` Classroom Integration
:link: roles-directives
:link-type: ref

Request a reservation devoted for the classroom, whether an entire curriculum or specific assignments and lessons.

+++
[Learn more »](classroom/class_use.rst)
:::

:::{grid-item-card} {octicon}`tools;1.5em;sd-mr-1` Best Practices
:link: best-practices/checkpointing
:link-type: doc

Learn to optimize your projects by following some best practices.

+++
[Learn more »](best-practices/checkpointing.rst)
:::

::::

```{note}
Access to the HPC Cluster is subject to university policy and guidelines. Please ensure that you read and understand these guidelines before using the facility. If you require assistance or have any questions, please do not hesitate to contact our dedicated support team.
```


The Northeastern University HPC Cluster is a high-powered, multi-node, parallel computing system designed to meet the computational and data-intensive needs of various academic and industry-oriented research projects. The cluster incorporates cutting-edge computing technologies and robust storage solutions, providing an efficient and scalable environment for large-scale simulations, complex calculations, artificial intelligence, machine learning, big data analytics, bioinformatics, and more.

Whether you are a seasoned user or just beginning your journey into high-performance computing, our portal offers comprehensive resources, including in-depth guides, tutorials, best practices, and troubleshooting tips. Furthermore, the platform provides a streamlined interface to monitor, submit, and manage your computational jobs on the HPC cluster.

We invite you to explore the resources, tools, and services available through the portal. Join us as we endeavor to harness the power of high-performance computing, enabling breakthroughs in research and fostering innovation at Northeastern University.

```{toctree}
:hidden:
:caption: 👋 Welcome

welcome/welcome
welcome/gettinghelp
```

```{toctree}
:hidden:
:caption: 🔎 First Steps with Discovery

first_steps/get_access
first_steps/connect_mac
first_steps/connect_windows
first_steps/connect_ood
first_steps/bashrc
```
```{toctree}
:hidden:
:caption: 🖥️ Hardware on Discovery

hardware/hardware_overview
hardware/partitions
```

```{toctree}
:hidden:
:caption: Using HPC

using-discovery/usingslurm
using-discovery/sbatch
using-discovery/srun
using-discovery/workingwithgpu
using-discovery/transferringdata
using-discovery/globus
```

```{toctree}
:hidden:
:caption: 📚 Software Guides

software/softwareoverview
software/modules
software/matlab
software/conda
software/spack
software/r
software/mpi
```

```{toctree}
:hidden:
:caption: Understanding storage options

storage/discovery_storage
storage/general_storage
```

```{toctree}
:hidden:
:caption: Best practices

best-practices/checkpointing
```

```{toctree}
:hidden:
:caption: 📖 Using Open OnDemand (OOD)

   using-ood/introduction
   using-ood/fileexplore
   using-ood/interactiveapps
```

```{toctree}
:hidden:
:caption: 🧑‍🏫 HPC for the classroom

classroom/class_use
classroom/cps_ood
```


