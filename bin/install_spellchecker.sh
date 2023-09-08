#!/bin/bash

git clone git@github.com:pyenchant/pyenchant.git
cd pyenchant
python setup.py install
# shellcheck disable=SC2103
cd ..
