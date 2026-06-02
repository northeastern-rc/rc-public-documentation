(storage-query)=

# Querying Project Storage

There are two explorer unique commands to help identify the file usage within a project directory: `project-storage` and `project-storage-components`.

These commands can be particularly helpful when you're trying to identify candidate files and directories to tarr when looking to reduce quota storage capacity or inode usage.

:::{note}
Both the `project-storage` and `project-storage-components` command can be ran by anyone in the project research group.
:::

## Setup

In order to run one of these commands, just as with checking your quota ({ref}`checking-your-quotas`) or running project group management commands ({ref}`project-commands`), you must be on any node in the `short` partition. To launch a job on the short partition, run:

:::{code-block} bash
srun -p short --constraint=ib --pty bash
:::

(project-storage-commands)=

## Project Storage

To see a tree visualization of your project directory with storage and last access time, you can run the following:
:::{code-block} bash
project-storage --project <project_name>
:::
an output will then resemble the following:
:::{code-block} text
<project_name> [size=55.3GiB, atime=<TODAY'S_DATE>]
    ├── <dir_name_1> [size=2.8MiB, atime=2026-01-10T20:08:33.983850687-05:00]
    │   ├── <file_name_1> [size=2.8MiB, atime=2025-11-30T10:06:40.895056162-05:00]
    │   └── <file_name_2> [size=72B, atime=2026-01-10T20:08:33.977276807-05:00]
    ├── <dir_name_2> [size=156.3KiB, atime=2025-11-11T12:41:53.541384959-05:00]
    │   ├── <dir_name_4> [size=104.4KiB, atime=2026-01-14T12:09:52.302996929-05:00]
    │   │   ├── <file_name_3> [size=0B, atime=2025-11-02T12:44:51.598328266-05:00]
    │   │   ├── <dir_name_4> [size=14.4KiB, atime=2025-11-02T12:44:51.70097234-05:00]
    │   │   │   ├── <file_name_4> [size=452B, atime=2025-11-02T12:44:51.633902125-05:00]
    │   │   │   ├── <file_name_5> [size=896B, atime=2025-11-02T12:44:51.641999345-05:00]
                                         ...
                                         ...
                                         ...
:::

To see a tree visualization of your project directory with storage and last access time of only the files that have not been accessed since a particular date and to see how these files contribute to the project's quota's used capacity, you can supply a date parameter to the project-storage command:
:::{code-block} bash
project-storage --project <project_name> --date <YYYY-MM-DD>
:::
an output will then resembling the following:
:::{code-block} text
<project_name> [size=20.8GiB, atime=<TODAY'S_DATE>]
                                         ...
                                         ...
                                         ...
        ├── <dir_name_1> [size=140.3KiB, atime=2023-11-17T11:52:16.380044419-05:00]
        │   ├── <file_name_1> [size=133.8KiB, atime=2023-10-05T10:13:36.430788748-04:00]
        │   └── <file_name_2> [size=6.5KiB, atime=2023-10-18T16:20:31.539474352-04:00]
        ├── <dir_name_2> [size=782.5KiB, atime=2023-10-17T17:08:57.927651117-04:00]
        │   ├── <dir_name_3> [size=11.2KiB, atime=2023-10-17T17:08:57.938182424-04:00]
        │   │   └── <file_name_3> baseline-checkpoint.ipynb [size=11.2KiB, atime=2023-10-12T11:14:29.181336376-04:00]
        │   ├── <file_name_4> [size=379.9KiB, atime=2023-10-22T17:47:50.461758297-04:00]
        │   ├── <file_name_5> [size=380.3KiB, atime=2023-10-17T17:08:43.950738185-04:00]
        │   └── <file_name_6> baseline.ipynb [size=11.2KiB, atime=2023-11-17T11:51:49.435964249-05:00]
        ├── <file_name_7> [size=126.9KiB, atime=2023-11-17T11:51:49.550177359-05:00]
        └── <file_name_8> [size=11.6KiB, atime=2023-11-17T11:52:13.937973979-05:00]


+------------+---------------------+------------------------------------+
| TOTAL SIZE | USED QUOTA CAPACITY | PERCENT OF QUOTA THAT'S UNACCESSED |
+------------+---------------------+------------------------------------+
| 20.8GiB    | 55.3GiB             | 0.38                               |
+------------+---------------------+------------------------------------+
:::

## Project Storage Components

To produce an enumeration of directories where all files and subdirectories listed are from before a particular date, you can run the following:
:::{code-block} bash
project-storage-components --project <project_name> --date <YYYY-MM-DD>
:::
, which will enumerate the appropriate directories in tabular form:
:::{code-block} text
+-----------------------------------------------------------+------------+-----------------------------------+
| PATH                                                      | TOTAL SIZE | PERCENT OF USED CAPACITY IN QUOTA |
+-----------------------------------------------------------+------------+-----------------------------------+
| <project_name>/<sub_dir_1>                                | 10.9MiB    | 0.00                              |
| <project_name>/<sub_dir_2>                                | 30.6GiB    | 0.55                              |
| <project_name>/<sub_dir_3>                                | 688.7KiB   | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_11>                   | 227.3KiB   | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_12>                   | 96.4MiB    | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_13>                   | 183.2MiB   | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_14>                   | 4.9GiB     | 0.09                              |
| <project_name>/<sub_dir_4>/<sub_dir_15>                   | 5.4KiB     | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_16>                   | 426.1MiB   | 0.01                              |
| <project_name>/<sub_dir_4>/<sub_dir_17>                   | 604.1KiB   | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_18>                   | 3.0MiB     | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_19>                   | 537.6KiB   | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_20>/<sub_dir_27>      | 9.9KiB     | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_20>/<sub_dir_28>      | 11.8KiB    | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_21>                   | 96.6MiB    | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_22>                   | 5.0MiB     | 0.00                              |
| <project_name>/<sub_dir_4>/<sub_dir_22>                   | 6.0MiB     | 0.00                              |
| <project_name>/<sub_dir_5>/<sub_dir_23>/<sub_dir_29>      | 14.4KiB    | 0.00                              |
| <project_name>/<sub_dir_5>/<sub_dir_23>/<sub_dir_30>      | 183B       | 0.00                              |
| <project_name>/<sub_dir_5>/<sub_dir_24>                   | 448.0KiB   | 0.00                              |
| <project_name>/<sub_dir_5>/<sub_dir_25>                   | 15.0GiB    | 0.27                              |
| <project_name>/<sub_dir_5>/<sub_dir_26>/<sub_dir_31>      | 17.7KiB    | 0.00                              |
| <project_name>/<sub_dir_5>/<sub_dir_26>/<sub_dir_32>      | 49.7KiB    | 0.00                              |
| <project_name>/<sub_dir_6>                                | 309.9KiB   | 0.00                              |
| <project_name>/<sub_dir_7>                                | 19.9MiB    | 0.00                              |
| <project_name>/<sub_dir_8>                                | 460.2MiB   | 0.01                              |
| <project_name>/<sub_dir_9>                                | 472.6MiB   | 0.01                              |
| <project_name>/<sub_dir_10>                               | 1.0MiB     | 0.00                              |
+-----------------------------------------------------------+------------+-----------------------------------+
:::
