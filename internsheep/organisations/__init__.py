# -*- encoding: utf-8 -*-

from flask import Blueprint

organisations_bp = Blueprint('organisations', __name__, template_folder='organisations')

from . import views
