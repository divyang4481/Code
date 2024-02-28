from flask import Blueprint, render_template, redirect, url_for, request

from lms.utils.auth import admin_required, login_user, logout_user
from flask_login import login_required
from lms import routes, admin_routes
from lms import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')



@admin_bp.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_admin = True  # For admin login
        response = login_user(username, password, is_admin)
        if response:
            return response
    return render_template('admin/login.html')

@admin_bp.route('/')
@admin_required  # Use your custom decorator here
def admin_dashboard():
    return render_template('admin/dashboard.html')
