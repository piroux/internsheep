
from flask import Blueprint

stages_bp = Blueprint('stages', __name__)

from . import views
