# Classroom HPC: FAQ

There are several use cases for teaching and learning with the Discovery cluster in a classroom. Discovery offers both a command line and web interface, allowing flexibility in access and instruction level. Using Discovery gives you and your students access to many popular scientific applications, and also allows you and your students to install other packages as needed. The easy-to-use Open onDemand web portal also offers a built-in visual file explorer for file viewing and transfer.

The following Frequently Asked Questions section should help to answer most of your questions about how you can use the Discovery cluster for classroom use. You can also reach out to us at <rchelp@northeastern.edu> or submit a ServiceNow ticket if you need further information.

**How can I use Discovery with my class?**

There are several ways you can use Discovery in your classroom. Your class can use Discovery for accessing specific software packages and working environments, as well as learning how to utilize high performance computing (HPC) resources for large and complex data processing, such as machine learning; AI and molecular simulations; and more.

**How do I get my class access to Discovery?**

You fill out a [Discovery Classroom Use Request] ticket. The form asks you to submit a list of your students' names and emails. We will create accounts on Discovery for them. Follow the steps in the article [How to Download a List of Student Email Addresses from Canvas] to get a list of your students' emails. If your class roster is not complete, you can attach a preliminary list to the ticket, and then follow up with us on the same ticket with an updated roster when the add/drop period is over.

**Is there any training on Discovery for my class?**

Yes, we currently provide online training for your class on using Discovery. In the past, we have also given in-person presentations during a class period on the Boston campus. We hope to provide in-person training again in 2021. We can customize the training to focus on the resources you will be using with them for the class. Email us at <rchelp@northeastern.edu> and provide us with some details about your class and what training you would like us to provide.

**Do my students have to learn Linux to work with Discovery?**

Depending on your class assignments, many students can work with the Open onDemand web portal, which does not require any knowledge of Linux to use. In cases where you want them to work on the command line, they should have a basic understanding of Linux commands. Please see the question "Is there any training on Discovery for my class" above if you would like us to provide your class with a basic training course prior to using Discovery.

**What software is available to use with my class on Discovery?**

There are many software packages available, including popular software apps such as Jupyter Notebook, RStudio, and MATLAB. If you have an account on Discovery, you can see the list of available software by using the `module avail` command. See [Using Module] for more information. Students have access to all the modules on Discovery. They can also use the interactive apps available on Open onDemand. See [Introduction to Open OnDemand (OOD)] for more information. We can also install additional modules and libraries specifically for your class as needed.

**My class needs access to a specific software application that I do not see installed on Discovery or Open onDemand (OOD). What should I do?**

If you class requires software not currently installed on Discovery or OOD, follow the procedure below to request that software be installed on Discovery.
You must be a professor or instructor to initiate this request. Students in your class should not make this request. If your students need a specific software application, you must complete the form for them. This is to ensure that we only get one request for the software. Students in one class often make multiple requests for the same software, so having all requests go through the professor or instructor reduces this overlap.

To request additional software (instructors only):

1. Go to the [Discovery Cluster Software Request]. If prompted, sign in to ServiceNow with your Northeastern username and password to access the form.
1. In the Sponsor’s Name field, enter your name.
1. Make sure to follow the instructions on the form regarding either providing the URL of the open source software library or uploading the installation package in your home directory if it requires you to register it first. The request will not be completed without this information.
1. Select the acknowledgement checkbox, and click **Submit**.

:::{note}
Software requests can take up to 24 hours to verify, and then additional time is needed to complete the installation. We might not be able to install every software application requested. If this is the case we will notify you and try to provide alternative software to meet your needs.
:::

:::{tip}
You and your students can install software locally to your PATH on Discovery, which may be a better option in some cases, such as installing multiple conda environments. See {ref}`software-overview` for more information.
:::

**I just need my class to access Open onDemand. How do I request that?**

Open onDemand is a web portal that lets you access the resources on Discovery through an easy-to-navigate web browser interface. You request course access the same way you would to get access to
Discovery, as outlined above. Please specify that you'd like your course to be on Open onDemand for your students, in
addition to the information we request above.

**I'd like my class to use specific resources on Discovery. Can you create a reservation on Discovery for my class?**

In many cases, we will create a reservation on Discovery for your class for specific hardware resources. For example, if you course assignments
require the use of GPUs or nodes with a large amount of memory, we can create a reservation on specific nodes that only your class can access
for the duration of the course. However, Discovery is a shared resource, so we ask that you test out your assignments on Discovery so
that you are requesting an appropriate amount of resources for your class. If a class needs an increase in resources due to higher than
expected use, we can always increase your reservation. But, if a reservation is not being used to capacity, we will ask you to review the
need for the requested resources, and adjust the reservation accordingly. We understand that sometimes it is difficult to determine exactly
what your resource needs will be, but we do need to keep a reservation to a reasonable limit so that we keep the shared resources available to
all users.

**How long do my students have access to Discovery?**

Students will have access to Discovery for the full duration of the class. If they want to continue to have access to Discovery after that time period, they'll need to request an individual account.

**How do I get an account on Discovery?**

If you are a professor or instructor at Northeastern, you can request an account on Discovery. See {ref}`instructor-access` for more information.

**How do my students get help with Discovery?**

You and/or your students can either submit a [Get Assistance with Research Computing] ticket or email <rchelp@northeastern.edu>.

<!--LINKS-->

[discovery classroom use request]: https://bit.ly/NURC-Classroom
[discovery cluster software request]: https://bit.ly/NURC-Software
[get assistance with research computing]: https://bit.ly/NURC-Assistance
[how to download a list of student email addresses from canvas]: https://service.northeastern.edu/tech?id=kb_article&sys_id=0f84a740db20901084ba5595ce961981
[introduction to open ondemand (ood)]: ../08_using-ood/01_introduction.md
[using module]: ../04_software/02_modules.md
