from flask import Blueprint
from . import views,forms

auth = Blueprint('auth',__name__)

from app.main import views