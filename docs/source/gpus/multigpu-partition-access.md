# Access to Multi-GPU Partition
The `multigpu` partition in the HPC cluster allows users for extensive parallel processing on multiple GPUs. This setup is ideal for applications that require significant computational power, such as deep learning, scientific simulations, and large-scale data analysis.

## Applying for Multi GPU reservation

### Step 1

- Use the partition application form link in here: [HPC Partition Request](https://bit.ly/NURC-PartitionAccess)
- Select under "Partition Type" - `Multigpu - Partition (Testing Access)`
- Fill in the number of GPUs and the type of GPU you'd like to test on. Please also provide a short description of your expected testing workload.
.. note::
   **Important considerations while requesting GPU**
   - Prefer V100 GPUs for multi-GPU testing if your jobs fit:
     * V100 testing is often sufficient to demonstrate scaling.
     * If a job scales well on V100s, it's likely to scale similarly on A100s.
     * This approach conserves A100 resources for production work.
   - Testing should represent your planned work but doesn't need full production runs.
   - Use scaled-down versions of your jobs for timing data when possible.
   - Only use A100s for testing if your job specifically requires their capabilities or memory.
   - Ensure your test cases cover a range of processor/GPU counts to measure scaling accurately.
   - Consider testing with different problem sizes to understand how scaling efficiency changes with workload.
- Submit the form.
- The Research Computing team will then contact you with further details for accessing a multi-GPU node. The Research Computing team will need an estimate of the duration needed for testing (preferably less than 24 hrs.)

### Step 2

- To check your reservation
    
    ```bash
    scontrol show reservation=<reservation_name>
    
    #<reservation_name> will be in the details provided by the RC team.
    ```
    
- To run an {term}`Interactive Job`, for example, using V100-sxm2 with 4 GPUs, use the command below

```bash
srun -p reservation --reservation=<reservation_name> --gres=gpu:v100-sxm2:4 --time=24:00:00 -N 1 --pty /bin/bash
```

***Note***
   Your local machine must remain active for successful job execution. Be aware of the following risks:

   - Network disconnections will interrupt the job
   - Computer sleep/hibernation will break the connection
   - Losing RDP session (e.g., timeout, local reboot) stops GUI-dependent processes
   - Power outages or system updates can cause unexpected disconnects

   Recommendations:
   - Use a stable network connection
   - Disable sleep mode on your local machine
   - Consider using persistent remote desktop solutions
   - Implement job checkpointing where possible
   - Monitor job status regularly

- **To run {term}`Non-interactive job`, you can use the following command**
    
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
    #SBATCH --mem=8G                     # Total memory
    #SBATCH --time=02:00:00              # Time limit hh:mm:ss
    #SBATCH --output=output_%j.txt       # Standard output and error log
    #SBATCH --error=error_%j.txt         # Standard error log
    
    # Load any required modules
    module load python #example
    
    # Run your program
    srun python your_script.py #example
    
    # Following Nano-editor commands are used to write this script to disk
    # ctrl+x 
    # press 'Y'
    # press enter
    ```
    
    3- Submit the job 
    
    ```bash
    sbatch job_script.sh
    ```
    
    4-**You can monitor the status of your job using the squeue command:**
    
    ```bash
    squeue -u <your_username>
    
    #To cancel a job
    scancel <job_id> # where <job_id> is the ID of the Job we are cancelling
    ```
    
- **You will also need to state whether it is for a class or for your own research work. If it is for a class, then the request should come from the instructor directly.** 
RC staff should make sure that the instructor is contacted and educated about this and then create a reservation for all the students for the duration of the class.
- Perform testing on 1,2,..(4,8) GPUs. Record runtimes for each test (calculate efficiency).

### Step-3

**Post-Testing Application**

- Ensure your {term}`Scaling efficiency` is adequate (generally over 0.5) when using the maximum GPUs selected on the `multigpu` partition⁠. If needed, please consult with the Research Computing (RC) team for guidance and support throughout the process⁠.
- Re-enter the partition application form and select "Multigpu - Partition (Post Testing)" under "Partition Type."
- Please fill out the form with your test results and submit it.
- After the RC team reviews and approves your application, you will be granted access to the `multigpu` partition.
