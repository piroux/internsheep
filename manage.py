#!/usr/bin/env python

import os
import subprocess

from internsheep import app, init_db, load_db
from flask.ext.script import Manager, Shell


manager = Manager(app)

def make_shell_context():
    #return dict(app=app, db=db, User=User, Note=Note, Role=Role, Tag=Tag, Notebook=Notebook)
    return dict(app=app)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def initdb():
    """ Initialize la BDD, si besoin en effacant tout."""
    p = subprocess.Popen(['bash', 'internsheep/create_db.sh'])
    p.communicate()
    init_db()
    load_db()
    print 'Base de donnees initialisee: OK'

@manager.command
def profile(length=25, profile_dir=None):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()

if __name__ == '__main__':
    manager.run()
