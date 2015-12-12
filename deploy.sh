#!/bin/bash

set -o errexit

virtualenv .

source bin/activate

pip install -r requirements.txt

echo "Postgresql need to be installed ..."
echo "Ready ? Now run:"
echo
echo "python manage.py initdb"
echo "python manage.py runserver"
