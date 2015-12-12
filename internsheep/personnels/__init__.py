
from flask import Blueprint

personnels_bp = Blueprint('personnels', __name__)

from . import views
