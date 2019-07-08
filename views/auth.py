from flask import Blueprint, render_template, session, request

import firebase_functions as firebase

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return "auth view"


@auth.route('/register', methods=['GET'])
def register():
    return render_template('auth/register.html')


@auth.route('/register_student', methods=['POST'])
def register_student():
    pass


@auth.route('/register_prof', methods=['POST'])
def register_prof():
    pass


@auth.route('/login', methods=['GET'])
def login():
    if request.method == 'POST':
        email, password, user_type = request.form['email'], request.form['password'], request.form['user_type']
        response = firebase.verify_credentials(email, password)
        if response['status'] == 'success':
            if user_type == 'student':
                session['user_type'], session['token'] = 'student', response['token']
                # retrieve student info
                return render_template('student/home.html')  # pass in data
            elif user_type == 'prof':
                session['user_type'], session['token'] = 'prof', response['token']
                # retrieve prof info
                return render_template('prof/home.html')  # pass in data
    return render_template('auth/login.html')


@auth.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return render_template('index.html')
