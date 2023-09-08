(classroom-faq)=
# Classroom HPC: FAQ

There are several use cases for teaching and learning with the cluster in a classroom. The cluster offers a command line and web interface, allowing access and instruction-level flexibility. Using the cluster gives you, and your students access to many popular scientific applications and allow you and your students to install other packages as needed. The easy-to-use Open OnDemand web portal also offers a built-in visual file explorer for viewing and transferring.

The following Frequently Asked Questions section should help answer most of your questions about using the cluster for classroom use. You can also contact us at <rchelp@northeastern.edu> or submit a ServiceNow ticket for further information.

## How can I use Discovery with my class?

There are several ways you can use the cluster in your classroom. Your class can use the cluster to access specific software packages and working environments and learn how to utilize high-performance computing (HPC) resources for large and complex data processing, such as machine learning; AI and molecular simulations; and more.

## How do I get my class access to the cluster?
You fill out an [HPC Classroom Use Request] ticket. The form asks you to submit a list of your student’s names and emails. We will create accounts on the cluster for them. Follow the steps in the article [How to Download a List of Student Email Addresses from Canvas] to get a list of your students’ emails. If your class roster is incomplete, you can attach a preliminary list to the ticket and follow up with us on the same ticket with an updated roster when the add/drop period is over.

## Is there any training on the cluster for my class?

Yes, we currently provide online training for your class on using the cluster. In the past, we have also given in-person presentations during a class period on the Boston campus. We provide training each semester. We can customize the training to focus on the resources you will be using with them for the class. Email us at <rchelp@northeastern.edu> and provide details about your class and what training you would like us to provide.

## Do my students have to learn Linux to work with the cluster?

Depending on your class assignments, many students can work with the Open OnDemand web portal, which does not require any knowledge of Linux to use. In cases where you want them to work on the command line, they should have a basic understanding of Linux commands. Please see the question “Is there any training on the cluster for my class” above if you would like us to provide your class with an introductory training course before using the cluster.

## What software is available to use with my class on the cluster?

Many software packages are available, including popular software apps such as Jupyter Notebook, RStudio, and MATLAB. If you have an account on the cluster, you can see the list of available software by using the `module avail` command. See {ref}`using-module` for more information. Students have access to all the modules on the cluster. They can also use the interactive apps available on Open OnDemand. See {ref}`using-ood` for more information. We can also install additional modules and libraries for your class as needed.

## My class needs access to a specific software application that I do not see installed on the cluster or Open OnDemand (OOD). What should I do?

If your class requires software not currently installed on the cluster or OOD, follow the procedure below to request that software be installed on the cluster. You must be a professor or instructor to initiate this request. Students in your class should refrain from making this request. If your students need a specific software application, you must complete the form for them. This is to ensure that we only get one request for the software. Students in one class often make multiple requests for the same software, so having all requests go through the professor or instructor reduces this overlap.

To request additional software (**instructors only**):

1. Go to [HPC Cluster Software Request]. If prompted, sign in to ServiceNow with your Northeastern username and password to access the form.
1. In the Sponsor’s Name field, enter your name.
1. Make sure to follow the instructions on the form regarding either providing the URL of the open-source software library or uploading the installation package in your home directory if it requires you to register it first. The request will only be completed with this information.
1. Select the acknowledgment checkbox, and click **Submit**.

:::{note}
Software requests can take up to 24 hours to verify; additional time is needed to complete the installation. We might not be able to install every software application requested. If so, we will notify you and provide alternative software to meet your needs.
:::

:::{tip}
You and your students can install software locally to your PATH on the cluster, which may be a better option in some cases, such as installing multiple conda environments. See {ref}`software-overview` for more information.
:::

## I just need my class to access Open OnDemand. How do I request that?

Open OnDemand is a web portal that lets you access the resources on the cluster through an easy-to-navigate web browser interface. As outlined above, you request course access like you would access the cluster. Please specify that you’d like your course to be on Open OnDemand for your students, in addition to the information we request above.

## I'd like my class to use specific resources on the cluster. Can you create a reservation on the cluster for my class?

We often create a reservation on the cluster for your class for specific hardware resources. For example, if your course assignments require GPUs or nodes with a large amount of memory, we can create a reservation on specific nodes that only your class can access for the course duration. However, the cluster is a shared resource, so we ask that you test out your assignments on the cluster so that you are requesting an appropriate amount of resources for your class. We can always increase your reservation if a class needs more resources due to higher-than-expected use. But, if a reservation is not being used to capacity, we will ask you to review the need for the requested resources and adjust the reservation accordingly. We understand that sometimes it takes time to determine precisely your resource needs. Still, we do need to keep a reservation to a reasonable limit to keep the shared resources available to all users.


## How long do my students have access to the cluster?

Students will have access to the cluster for the whole class duration. They must request an individual account if they want to continue accessing the cluster after that period.

## How do I get an account on the cluster?

If you are a professor or instructor at Northeastern, you can request an account on the cluster. See {ref}`instructor-access` for more information.

## How do my students get help with the cluster?
You and your students can submit a [Get Assistance with Research Computing] ticket or email <rchelp@northeastern.edu>.

[HPC classroom use request]: https://bit.ly/NURC-Classroom
[HPC cluster software request]: https://bit.ly/NURC-Software
[get assistance with research computing]: https://bit.ly/NURC-Assistance
[how to download a list of student email addresses from canvas]: https://service.northeastern.edu/tech?id=kb_article&sys_id=0f84a740db20901084ba5595ce961981
