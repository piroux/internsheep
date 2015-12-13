# -*- encoding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flask.ext.bootstrap import Bootstrap

from . import database


DATABASE = 'internsheep'
DEBUG = True
SECRET_KEY = 'devkey'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'default'


app = Flask(__name__)
Bootstrap(app)
app.debug = DEBUG
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.db = database.connect_db()

@app.teardown_request
def teardown_request(exception):
    cur = getattr(g, 'cur', None)
    if cur is not None:
        cur.close()
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

from .main.views import main_bp
app.register_blueprint(main_bp)

from .organisations.views import organisations_bp
app.register_blueprint(organisations_bp, url_prefix='/organisations')

from .personnels.views import personnels_bp
app.register_blueprint(personnels_bp, url_prefix='/personnels')

from .stages.views import stages_bp
app.register_blueprint(stages_bp, url_prefix='/stages')
