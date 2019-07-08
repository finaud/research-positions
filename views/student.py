from flask import Blueprint, render_template, session, redirect, url_for
import functools

import firebase_functions as firebase

student = Blueprint('student', __name__)


def student_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'token' not in session or not firebase.verify_token(session['token']) or session['user_type'] != 'student':
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@student.route('/')
@student_required
def index():
    return "student view"


@student.route('/home', methods=['GET'])
@student_required
def home():
    data = {}  # retrieve info
    return render_template('student/home.html', data=data)
