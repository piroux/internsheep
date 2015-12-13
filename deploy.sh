#!/bin/bash

rm -rf internsheep_env/
find -name '*.pyc' -delete

set -o errexit

virtualenv internsheep_env

source internsheep_env/bin/activate

pip install -r requirements.txt

cat README
