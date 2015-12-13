#!/bin/bash


if [[ "$USER" == "postgres" ]]
then
    echo "Creation BDD pour app de gestion des stages sur PostgreSQL"
elif [[ "$UID" == "0" ]]
then
    exec su postgres -c "bash $0 $1"
else
    echo "Connexion nécessaire en root :"
    exec sudo bash "$0" "$USER" # for debian/ubuntu
    #exec su -c "bash $0 \"$USER\"" # for redhat/fedora
fi

cd

TARGET_USER=$1
TARGET_DATABASE="internsheep"

set -x

createuser -s $TARGET_USER

set -o errexit

psql << EOF
DROP DATABASE IF EXISTS "$TARGET_DATABASE";
ALTER USER "$TARGET_USER" WITH SUPERUSER CREATEDB;
CREATE DATABASE "$TARGET_DATABASE" WITH OWNER "$TARGET_USER";
GRANT ALL PRIVILEGES ON DATABASE "$TARGET_DATABASE" to "$TARGET_USER";
\dg
\l
EOF

exit
exit
