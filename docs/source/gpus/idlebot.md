(idle-bot)=

# IdleBot

To help address the issue of extended waiting times for GPUs caused by allocated idle resources, northeastern research computing built the IdleBot. The IdleBot monitors the GPU usage across our public GPU nodes. If a GPU has been under-utilized for 15 minutes, the IdleBot will email the user to inform them, and, if the GPU remains under-utilized for an entire hour, the IdleBot will cancel the job to free the resources.

## GPU Log Information

The information that the IdleBot uses to adjudicate is logged for 7 days after completion and is available to the user that ran the job, regardless of whether the job was efficient or inefficient, through our `gpu-logs` command (see {ref}`gpu_logs`).

## Idle Graph Creation

Within a few hours of a job's cancellation by the IdleBot, a graph plotting the GPU and memory utilization by time-step for each GPU used will be saved in `/scratch/<user>/idle_bot_graphs/<job_id>.png`.

This can be viewed by accessing the file through our Open OnDemand platform's File Explorer or by transferring the file to your local machine (see {ref}`transferring-data`).
