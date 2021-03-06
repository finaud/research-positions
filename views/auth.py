from flask import Blueprint, render_template, session, request, redirect, url_for, flash

from functions import firebase_auth as fb_auth

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return "auth view"


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if 'token' in session and fb_auth.verify_token(session['token']):
        if session['user_type'] == 'student':
            return redirect(url_for('student.home'))
        elif session['user_type'] == 'prof':
            return redirect(url_for('prof.home'))
    elif request.method == 'POST':
        user_type = request.form['user_type']
        if request.form['password'] != request.form['passwordConfirm']:
            flash('PASSWORDS_DO_NOT_MATCH', 'red')
            return render_template('auth/register.html')
        else:
            email, password = request.form['email'], request.form['password']
            response = fb_auth.create_user(email, password)
            if response['status'] == 'success':
                response2 = fb_auth.verify_credentials(email, password)
                if user_type == 'student':
                    session['user_type'], session['token'] = 'student', response2['token']
                    # retrieve student info
                    return redirect(url_for('student.home'))
                elif user_type == 'prof':
                    session['user_type'], session['token'] = 'prof', response2['token']
                    # retrieve prof info
                    return redirect(url_for('prof.home'))
            else:
                flash(response['msg'], 'red')

    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if 'token' in session and fb_auth.verify_token(session['token']):
        if session['user_type'] == 'student':
            return redirect(url_for('student.home'))
        elif session['user_type'] == 'prof':
            return redirect(url_for('prof.home'))
    elif request.method == 'POST':
        email, password, user_type = request.form['email'], request.form['password'], request.form['user_type']
        response = fb_auth.verify_credentials(email, password)
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
    return render_template('main/index.html')
