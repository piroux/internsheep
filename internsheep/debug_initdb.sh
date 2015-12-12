#!/bin/bash

set -x
set -o errexit

bash create_db.sh

psql -v ON_ERROR_STOP=1 -f db/schema.sql internsheep

psql -v ON_ERROR_STOP=1 -f db/data_init_main.sql internsheep

psql -v ON_ERROR_STOP=1 -f db/data_init_geo.sql internsheep
