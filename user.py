from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from TravelWebsite.auth import login
from TravelWebsite.db import get_db

bp = Blueprint('user',__name__, url_prefix='/user')

@bp.route('/Checkin_links')
def Checkin_links_get():


@bp.route("/Bookings")
def Bookings_get():



@bp.route("/")
