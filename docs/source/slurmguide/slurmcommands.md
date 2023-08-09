(slurm-commands)=
# Slurm Commands

SLURM provides options for customizing output filenames for your jobs through character replacements. Refer to the table below for some examples. You may use or combine variables as desired. Character replacements may also be used with other SBATCH directives such as error filename, input filename, and job name.
| Variable | Definition      | Example Directive(s)     | Output      |
|----------|-----------------|------------------------------------------------------|----------------------|
| %A       | A job array's main job ID | #SBATCH --array=1-2 #SBATCH -o %A.out #SBATCH --open-mode=append | 12345.out            |
| %a       | A job array's index number | #SBATCH --array=1-2 #SBATCH -o %A_%a.out             | 12345_1.out 12345_2.out |
| %J       | Job ID plus stepid | #SBATCH -o %J.out                                    | 12345.out            |
| %j       | Job ID          | #SBATCH -o %j.out                                    | 12345.out            |
| %N       | Hostname of the first compute node allocated to the job | #SBATCH -o %N.out                                    | r1u11n1.out          |
| %u       | Username        | #SBATCH -o %u.out                                    | netid.out            |
| %x       | Jobname         | #SBATCH --job-name=JobName #SBATCH -o %x.out         | JobName.out          |
