
# Data Management Plan for Funding Agencies

The Northeastern Research Computing (RC) team provides high-end research computing resources to all Northeastern University-affiliated faculty, researchers, and students. The team also manages Northeastern’s partnership with the Massachusetts Green High Performance Computing Center (MGHPCC). Resources available to the Northeastern community include a centralized high-performance computing (HPC) cluster, storage, software, high-level technical and scientific consultations, education, documentation, and training. All of these resources are accessible to all faculty and students, with RC staff available to assist researchers through consultations on how to leverage hardware and software for scientific applications and workflows.

As of January 2024, the Discovery cluster provides access to over 50,000 CPU cores and over 525 GPUs to all Northeastern faculty and students free of charge.  Hardware currently available for research consists of a combination of Intel Xeon (Cascadelake, Skylake, Broadwell, Haswell, Sandybridge and Ivybridge) and AMD (Zen, Zen2) CPU microarchitectures. Additionally, a selection of NVIDIA Pascal (P100), Volta (V100), Turing (T4), Ampere (A100), and Hopper (H100) GPUs.  Discovery is connected to the university network over 10 Gbps Ethernet (GbE) for high-speed data transfer, and Discovery provides 6 PB of available storage on a high-performance file system. Compute nodes are connected with either 10 GbE or high data rate InfiniBand (200 Gbps or 100 Gbps), supporting all types and scales of computational workloads.

A dedicated team of PhD scientists and staff manage the RC environment and support researchers in their use of the Discovery cluster resources. The RC team updates computational resources available through Discovery with the newest technologies on a yearly cycle to support the cutting-edge research being performed by Northeastern faculty and students.

Research groups who require access to dedicated computational resources can request to be part of a “buy-in” option, integrating their hardware into the Discovery cluster to provide unified access to both private and shared compute nodes for their research group members. Faculty-owned hardware that is part of the Discovery cluster is fully managed and maintained by the RC staff at no charge.

Alternatively, researchers can transfer grant dollars to RC to enable a ‘Co-op’ or paid allocations model. Principal Investigators (PIs) can purchase CPU or GPU hours, or storage capacity, tailored to the specific needs of a research project and/or grant. This alleviates the need for PIs to purchase capital equipment directly.

## Secure Data Enclave (SDE)

In response to research funding requirements, Northeastern University has developed a high-performance Secure Data Enclave (SDE) for researchers to store and process secure data. Types of secure data that the SDE can be used for include personally identifiable information (PII), personal health information (PHI), HIPAA and FERPA data. The SDE is comprised of two Infinidat Infinibox F4260 data storage systems, one located in the Massachusetts Green High-Performance Computing Center (MGHPCC) in Holyoke, Massachusetts, and the other located at the Markley Datacenter in Downtown Boston as a backup. In addition to data storage, there are dedicated CPUs and GPUs as part of the SDE that can be used for the computation of secure data in the enclave. The compute nodes do not have direct network access to anything outside of the SDE. Scientific and statistical software is also available pre-installed on the compute nodes. All components of the SDE are behind a network firewall.


Researchers affiliated with Northeastern must request an access account on the SDE through the Office of Research. Once approved, researchers can access the SDE through a multi-factor authentication process. Data transfer of secure data is completed through Globus, a data management system that has a higher assurance level to meet secure data compliance requirements


## NU SDE

The Secure Data Enclave (SDE) is a subset of RC systems configured to comply with Northeastern University's CMMC Program, creating a storage and computational environment that allows researchers to compete for government funding without having to support their own computational environments. Computational research is the focus of the SDE. There is no physical lab, and there is no physical CUI, but there is a cluster of hardware dedicated to storing and computing CUI data.

## Storage Services

The focus of any CMMC-approved environment is storage — specifically security, privacy, and auditing. The SDE has two (2) Infinidat systems that are configured with FIPS-140-2 validated encryption — one (1) at the MGHPCC in Holyoke, MA and the other in Boston, MA at the Markley Datacenter.

These systems both provide snapshot facilities, but the system at Markley is a dedicated off-site replication target for MGHPCC, the primary SDE datastore.

Data is staged into and out of the cluster using Globus ([www.globus.org](www.globus.org)), which provides the encryption and auditing required of CMMC environments.

## Compute Services

The SDE also offers compute services via Open OnDemand ([www.openondemand.org](www.openondemand.org)). OOD is a web-based interface to an HPC cluster that presents interfaces to traditional batch processing, conventional "desktop-style" research, and client-server based programs. The HPC cluster is managed by SLURM ([www.schedmd.com]), making the SDE a conventional research cluster with the enhanced security and auditing required for CMMC.

## Data Management Plan (DMP)

The Research Computing Team at Northeastern University ([www.rc.northeastern.edu](https://www.rc.northeastern.edu/)) provides research groups with up to 35 TB of high-performance data storage free of charge. This storage is owned and maintained by the University and is physically located in the Massachusetts Green High Performance Computing Center, a secure data center. All storage systems are on uninterruptible power supply (UPS)-backed power supplies, so that in the event of a power outage or interruption, there can be a graceful shutdown, minimizing the possibility of data loss. All storage file systems are backed up several times daily, and in certain cases, a second offsite copy is maintained. For secure, reliable data access, the Research Computing team maintains a Globus endpoint on Discovery that can be used by researchers to access and share their data.

The University provides website hosting for students, staff, and faculty, free of charge. Through https://sites.northeastern.edu/ anyone at NU can create a basic WordPress site. For more complex website needs, the university also has a dedicated team of web developers who can assist faculty and staff with their website needs.