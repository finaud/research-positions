from flask import Blueprint, render_template, session, redirect, url_for
import functools

import functions.firebase_auth as fb_auth
import functions.firebase_student as fb_student

student = Blueprint('student', __name__)


def student_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'token' not in session or not fb_auth.verify_token(session['token']) or session['user_type'] != 'student':
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


@student.route('/profile', methods=['GET'])
@student_required
def profile():
    uid = fb_auth.decode_token(session['token'])['uid']
    data = {
        'info': fb_student.get_info(uid),
        'education': fb_student.get_education(uid),
        'experience': fb_student.get_experience(uid),
        'coursework': fb_student.get_coursework(uid)
    }

    return render_template('student/profile.html', data=data)
