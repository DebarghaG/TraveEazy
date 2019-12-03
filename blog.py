import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from TravelWebsite.db import get_db

bp = Blueprint('blog', __name__, url_prefix='/blog')
"""
To add new blog posts, create html files and then
from there on and then we create a page by route here
in this blueprint
"""
@bp.route('/')
def blog():
    return render_template('blog/blog.html')

@bp.route('/singleblog')
def singleblog():
    return render_template('/blog/singleblog.html')
