from flask import Flask, render_template, redirect, url_for, request

from config import Config
from flask_login import LoginManager, current_user

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
# app.config['SECRET_KEY'] = 'your_secret_key'

app.config.from_object(Config)
db = SQLAlchemy()


login_manager = LoginManager(app)
login_manager.login_view = "login"  # Default login view for regular users

with app.app_context():
    from lms import models  # Import models to ensure they are known to SQLAlchemy
    db.create_all()  # Create database tables for our models

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500


@login_manager.user_loader
def load_user(user_id):
    from lms.models import User
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    if '/admin' in request.path:
        return redirect(url_for('admin.admin_login', next=request.url))
    return redirect(url_for('login', next=request.url))


from lms import routes
from lms.admin_routes import admin_bp 

# Register the Blueprint for admin routes
app.register_blueprint(admin_bp)