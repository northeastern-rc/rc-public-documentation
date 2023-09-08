(slurm-scripts)=
# Slurm Job Scripts

## `sbatch` Job Script Examples

### Single node with additional memory
The default memory per allocated core is 1.95GB. If calculations attempt to access more memory than allocated, Slurm automatically terminates the job. Request a specific amount of memory in the job script if calculations require more than the default. The example script below requests 100GB of memory (`--mem=100G`). Use one capital letter to abbreviate the unit of memory (i.e., kilo `K`, mega `M`, giga `G`, and tera `T`) with the `--mem=` option, as that is what Slurm expects to see:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --mem=100G
#SBATCH --partition=short

# <commands to execute>
:::

### Single with exclusive use of a node
If you need exclusive use of a node, such as when you have a job that has high I/O requirements, you can use the exclusive flag. The example script below specifies the exclusive use of one node in the short partition for four hours:

:::{code} bash
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=4:00:00
#SBATCH --job-name=MyJobName
#SBATCH --exclusive
#SBATCH --partition=short

# <commands to execute>
:::
