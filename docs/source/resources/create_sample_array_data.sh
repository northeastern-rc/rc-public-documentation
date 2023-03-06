#!/bin/bash
# This block of code creates N_FILES*INDEX_SKIP files in the WORK_DIR directory.
# Each file contains the string "some data" followed by a newline character, the string "k=" followed by the value of K,
# and another newline character.
# The value of K is calculated as k * INDEX_SKIP, where k is the loop variable.
# The resulting files are named toy_data_<k>.dat, where <k> is the value of K for each iteration of the loop.

WORK_DIR="$(pwd)/array_example_data"
N_FILES=20
INDEX_SKIP=2
# calculate the value of the variable K_MAX by multiplying N_FILES and INDEX_SKIP. The result is printed to the console.
K_MAX=$(( ${N_FILES} * ${INDEX_SKIP} ))
echo "** K_MAX: ${K_MAX}"
# his line checks if the directory specified by the WORK_DIR variable already exists.
# If it does, the directory is deleted recursively (rm -rf) using the force flag (-f).
if [[ -d ${WORK_DIR} ]]; then rm -rf "${WORK_DIR}"; fi
#
mkdir "${WORK_DIR}"
for (( k=0; k< ${N_FILES}; k++ )); do
    # data directory array_example_data populated with kth text files.
	K=$(( $k * ${INDEX_SKIP} ))
    echo "some data:\nk=$K\n" >  "${WORK_DIR}"/toy_data_${K}.dat
done
