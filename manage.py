#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from internsheep import app, database
from internsheep.database import create_db, init_db, load_db
from flask.ext.script import Manager, Shell


manager = Manager(app)

def make_shell_context():
    return dict(app=app, database=database)
manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def initdb():
    """ Initialize la BDD, si besoin en effacant tout."""
    create_db()
    init_db()
    load_db()
    print 'Base de donnees initialisée: OK'

@manager.command
def profile(length=25, profile_dir=None):
    """Start the application under the code profiler."""
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                      profile_dir=profile_dir)
    app.run()

if __name__ == '__main__':
    manager.run()
