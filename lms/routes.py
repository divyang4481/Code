from flask import request, render_template
from lms.utils.auth import login_user, logout_user
from lms import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_admin = False  # Adjust based on your form input
        response = login_user(username, password, is_admin)
        if response:
            return response
    return render_template('login.html')

@app.route('/logout')
def logout():
    return logout_user()

# @app.route('/')
# def home():
#     return 'Welcome to the Library Management System!'


@app.route('/')
def index():
    return render_template('index.html')