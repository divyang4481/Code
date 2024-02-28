from flask import request, redirect, url_for, make_response
from lms.models import User
from lms import db

from functools import wraps
from flask import redirect, url_for, request
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            return redirect(url_for('admin.admin_login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def login_user(username, password, is_admin):
    user = User.query.filter_by(username=username, is_admin=is_admin).first()
    if user and user.check_password(password):
        resp = make_response(redirect(url_for('admin.admin_dashboard' if is_admin else 'index')))
        resp.set_cookie('username', username)
        return resp
    return None

def logout_user():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', '', expires=0)
    return resp
