# -*- encoding: utf-8 -*-

import psycopg2
from contextlib import closing
import subprocess
import os.path
import os

from flask import current_app

def connect_db():
    # use peer authentication
    return psycopg2.connect('dbname={}'.format(
        current_app.config['DATABASE']))


def execute_sql_script(script):
    print 'Execute script: {}'.format(script)
    with closing(connect_db()) as db:
        #with current_app.open_resource(script, mode='r') as f:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), script), mode='r') as f:
            db.cursor().execute(f.read())
        db.commit()

def create_db():
    p = subprocess.Popen(['bash', 'create_db.sh'], cwd=os.path.dirname(os.path.abspath(__file__)))
    p.communicate()

def init_db():
    execute_sql_script('schema.sql')


def load_db():
    execute_sql_script('data_init_main.sql')
    execute_sql_script('data_init_geo.sql')
