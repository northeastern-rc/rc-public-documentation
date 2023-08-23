#!/bin/bash
# assume the data (testfile.txt) is in the same folder as this script.
DATA_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
awk '{print $1}' "${DATA_DIR}/testfile.txt"
echo -e "----\n"
awk 'BEGIN{FS="\n"; RS=""} {print $1,$3}' "${DATA_DIR}/testfile.txt"
