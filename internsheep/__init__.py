# -*- encoding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

from .models import connect_db, init_db, load_db

from flask.ext.bootstrap import Bootstrap



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
    g.db = models.connect_db()

@app.teardown_request
def teardown_request(exception):
    cur = getattr(g, 'cur', None)
    if cur is not None:
        cur.close()
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

from .main import main_bp
app.register_blueprint(main_bp)

from .organisations import organisations_bp
app.register_blueprint(organisations_bp, url_prefix='/organisations')

from .personnels import personnels_bp
app.register_blueprint(personnels_bp, url_prefix='/personnels')

from .stages import stages_bp
app.register_blueprint(stages_bp, url_prefix='/stages')
