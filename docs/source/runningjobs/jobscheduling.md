(job-scheduling)=
# Job Scheduling Policies and Priorities
In an HPC environment, efficient job scheduling is crucial for allocating computing resources and ensuring optimal cluster utilization. Job scheduling policies and priorities determine the order in which jobs are executed and the resources they receive. Understanding these policies is essential for maximizing job efficiency and minimizing wait times.

## Scheduling Policies

### FIFO (First-In-First-Out)

Jobs are executed in the order they are submitted. Although simple, this policy may lead to long wait times for large, resource-intensive jobs if smaller jobs are constantly being submitted.

### Fair Share

This policy ensures that all users receive a fair share of cluster resources over time. Users with high resource usage may experience reduced priority, allowing others to access resources more regularly.

### Priority-Based

Jobs are assigned priorities based on user-defined criteria or system-wide rules. Higher-priority jobs are executed before lower-priority ones, allowing for resource allocation based on user requirements.

## Job Priorities

### User Priority

Users can assign priority values to their jobs. Higher values result in increased job priority and faster access to resources.

### Resource Requirements

Jobs with larger resource requirements may be assigned higher priority, as they require more significant resources to execute efficiently.

### Walltime Limit

Jobs with shorter estimated execution times may receive higher priority, ensuring they are executed promptly and freeing up resources for other jobs.

## Balancing Policies

### Backfilling

This policy allows smaller jobs to "backfill" into available resources ahead of larger jobs, optimizing resource utilization and reducing wait times.

### Preemption

Higher-priority jobs can preempt lower-priority ones, temporarily pausing the lower-priority job's execution to make resources available for the higher-priority job.

## Best Practices

- **Set Realistic Priorities**: Assign accurate priorities to your jobs to reflect their importance and resource requirements.
- **Use Resource Quotas**: Be mindful of the resources you request to prevent over- or underutilization.
- **Leverage Backfilling**: Submit smaller, shorter jobs that can backfill into available resources while waiting for larger jobs to start.

Understanding these scheduling policies and priorities empowers you to make informed decisions when submitting jobs, ensuring that your computational tasks are executed efficiently and promptly. If you need further guidance on selecting the right scheduling policy for your job or optimizing your resource usage, our support team is available at <rchelp@northeastern.edu> or consult our {ref}`faq`.

Optimize your job execution by maximizing our cluster's scheduling capabilities. Happy computing!
