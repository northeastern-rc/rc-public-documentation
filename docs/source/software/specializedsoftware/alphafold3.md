# AlphaFold3

[AlphaFold3](https://github.com/google-deepmind/alphafold3) is a deep learning model developed by Google DeepMind for predicting the structure of proteins and other biomolecules. It is available on the Explorer HPC cluster as a Singularity container.

---

## Prerequisites

Before running AlphaFold3, you need:

- An active Explorer HPC account. See [Connecting to Explorer](../../connectingtocluster/index.md).
- AlphaFold3 model weights (`af3.bin`) obtained directly from Google DeepMind (see [Requesting Model Weights](#requesting-model-weights) below).

---

## Requesting Model Weights

AlphaFold3 model parameters are provided by Google DeepMind for non-commercial research use only.

1. Review the terms of use: [WEIGHTS_TERMS_OF_USE.md](https://github.com/google-deepmind/alphafold3/blob/main/WEIGHTS_TERMS_OF_USE.md)
2. Request access via the Google DeepMind form: [https://forms.gle/svvpY4u2jsHEwWYS6](https://forms.gle/svvpY4u2jsHEwWYS6)
3. Once approved, download the weights and store them in your lab's project directory, for example:

```bash
/projects/<your_lab>/af3_models/
```

:::{note}
The download link provided by Google DeepMind is time-limited. Download as soon as possible after approval.
:::

---

## Getting Started

### Step 1 — Copy the template SLURM script

```bash
cp /shared/container_repository/AlphaFold/af3/run_alphafold3.sh /scratch/$USER/run_alphafold3.sh
```

### Step 2 — Read the instructions

```bash
cat /shared/container_repository/AlphaFold/af3/af3_instructions
```

### Step 3 — Edit the USER CONFIGURATION section

Open the script and update these three variables:

```bash
my_input_json   # path to your input JSON file
my_output_dir   # path where results will be written
my_model_dir    # path to your lab's af3.bin weights directory
```

### Step 4 — Submit the job

```bash
cd /scratch/$USER
sbatch run_alphafold3.sh
```

---

## Important Notes

### GPU Partition and Time Limits

Always use the `gpu` partition (not `gpu-short`) for AlphaFold3 jobs:

```bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100-sxm2:1
#SBATCH --time=08:00:00
```

### GPU Idle Warning (IdleBot)

AlphaFold3 has CPU-intensive phases (MSA generation, template search) that run before GPU inference. During these phases, the GPU may appear idle, which can trigger an [IdleBot](../../gpus/idlebot.md) warning and eventual job cancellation after 1 hour of idle time.

To reduce idle time, increase the number of CPU cores to speed up the MSA phase:

```bash
#SBATCH --cpus-per-task=48
```

### Container and Database Paths

The following paths are managed by RC and should not be changed:

| Resource | Path |
|---|---|
| Container | `/shared/container_repository/AlphaFold/af3/alphafold3_v3.0.2.sif` |
| Reference databases | `/shared/container_repository/AlphaFold/database` |

---
