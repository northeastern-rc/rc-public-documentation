# Access to Multi-GPU Partition
The `multigpu` partition in the HPC cluster enables parallel processing across multiple GPUs. This setup is ideal for applications that require significant computational power, such as deep learning, scientific simulations, and large-scale data analysis.

Please follow these steps to apply for the Multi-GPU Partition.

## MultiGPU Partition Access Guide

### Requesting Access to MultiGPU partition

- Please use the partition application form here: [HPC Partition Request](https://bit.ly/NURC-PartitionAccess)
- Select under "Partition Type" - `Multigpu`
- Make sure that you have filled the form with briefly answering the setup questions at the end.
:::{note}
   Please consider the following while requesting GPUs for testing:
   - Testing should represent your planned work but doesn't need full production runs.
   - Use scaled-down versions of your jobs for timing data when possible.
   - Ensure your test cases cover a range of processor/GPU counts to measure scaling accurately.
   - Consider testing with different problem sizes to understand how scaling efficiency changes with workload.
   - If you need to use A100s in your workflow, consider testing your code on V100 GPUs:
     * V100 testing is often sufficient to demonstrate scaling.
     * If a job scales well on V100s, it will also scale on A100s.
     * This approach conserves A100 resources for all the users on the cluster.
     * Only use A100s for testing if your job requires their capabilities or memory that V100s cannot provide.
:::


- Submit the form.
- After submitting the form Research Computing team will reach out to you for an estimate of the duration needed for testing (preferably less than 24 hrs).
- Research Computing team will contact you with more details for accessing a multi-GPU node. 

### Testing the Code on the Temporary Reservation

In the testing phase, you will be provided with the reservation for performing test on 1, 2, 4, and 8 GPUs and recording runtimes for each test to calculate efficiency.

#### Check your reservation
    
Before you begin check your reservation
```bash
scontrol show reservation=<reservation_name>
    
#<reservation_name> will be in the details provided by the RC team.
```

#### Interactive Job
    
To run an {term}`Interactive Job`, for example, using V100-sxm2 with 4 GPUs, use the command below

```bash
srun -p reservation --reservation=<reservation_name> --gres=gpu:v100-sxm2:4 --time=24:00:00 -N 1 --pty /bin/bash
```

:::{note}
   Your local machine must remain active for successful job execution. Be aware of the following risks:
   - Network disconnections have the potential to interrupt the job.
   - Computer sleep/hibernation can break the connection.
   - Losing RDP session (e.g., timeout, local reboot) stops GUI-dependent processes.
   - Power outages or system updates can cause unexpected disconnects.

**Recommendations:**
   - Use a stable network connection.
   - Disable sleep mode on your local machine during testing.
   - Implement job checkpointing where possible.
   - Monitor job status regularly.
   - Use [Non-interactive job](https://rc-docs.northeastern.edu/en/latest/gpus/multigpu-partition-access.html#non-interactive-job)
:::

#### Non-interactive job

To run {term}`Non-interactive job`, you can use the following command
    
    1- Create a script
    
    ```bash
    nano my_job.sh 
    # You can use any text editor you prefer, not just nano. Choose the editor you're most comfortable with for modifying files. 
    ```
    
    2- Add reservation and job details
    
    ```bash
    #!/bin/bash
    #SBATCH --job-name=MyJob             # Job name
    #SBATCH -p reservation
    #SBATCH --reservation=<reservation_name>
    #SBATCH --gres=gpu:v100-sxm2:4
    #SBATCH --nodes=1                    # Number of nodes
    #SBATCH --ntasks=4                   # Number of tasks
    #SBATCH --cpus-per-task=2            # Number of CPUs per task
    #SBATCH --mem=8G                     # Total CPU memory (not GPU memory)
    #SBATCH --time=02:00:00              # Time limit hh:mm:ss
    #SBATCH --output=output_%j.txt       # Standard output and error log
    #SBATCH --error=error_%j.txt         # Standard error log
    
    # Load any required modules
    module load python #example
    
    # Run your program
    srun python your_script.py #example

    # You can use the editor of your choice to edit and save the file on the cluster.
    # Following commands are for the editor 'Nano', and can be used to write this script to disk
    # Ctrl+x to save the file 
    # press 'Y' to save the changes
    # press enter to complete saving the file to the disk
    ```
    
    3- Submit the job 
    
    ```bash
    sbatch job_script.sh
    ```
    
    4-You can monitor the status of your job using the squeue command:
    
    ```bash
    squeue -u <your_username>
    
    #To cancel a job
    scancel <job_id> # where <job_id> is the ID of the Job we are canceling
    ```

:::{important}
This multi-GPU setup is intended for research workflows only. For course-related multi-GPU needs, please refer to the course request form. Instructors should submit those requests directly through the appropriate channels.
:::

#### Post-Testing Sharing Performance Results

- Ensure your {term}`Scaling efficiency` is adequate (generally over 0.5) when using the maximum GPUs selected on the `multigpu` partition⁠. If needed, please consult with the Research Computing (RC) team for guidance and support throughout the process⁠.
- Share your execution time across 1, 2, 3, 4 GPUs with efficiency in the ticket for review.
- Based on your performance, the team will evaluate your application for permanent access to the `multigpu` partition until your research work is completed.

