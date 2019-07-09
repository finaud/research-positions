from flask import Blueprint, render_template, session, request, redirect, url_for, flash

import firebase_functions as firebase

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return "auth view"


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if 'token' in session and firebase.verify_token(session['token']):
        pass  # redirect to appropriate home page
    elif request.method == 'POST':
        user_type = request.form['user_type']
        if user_type == 'student':
            pass  # create student
        elif user_type == 'prof':
            pass  # create prof

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if 'token' in session and firebase.verify_token(session['token']):
        pass  # redirect to appropriate home page
    elif request.method == 'POST':
        email, password, user_type = request.form['email'], request.form['password'], request.form['user_type']
        response = firebase.verify_credentials(email, password)
        if response['status'] == 'success':
            if user_type == 'student':
                session['user_type'], session['token'] = 'student', response['token']
                # retrieve student info
                return redirect(url_for('student.home'))
            elif user_type == 'prof':
                session['user_type'], session['token'] = 'prof', response['token']
                # retrieve prof info
                return redirect(url_for('prof.home'))
        else:
            flash(response['msg'], 'red')

    return render_template('auth/login.html')


@auth.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return render_template('index.html')
