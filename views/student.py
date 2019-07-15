from flask import Blueprint, render_template, session, redirect, url_for, request
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
    data = fb_student.get_info(uid)
    return render_template('student/profile.html', data=data)


@student.route('/edit_profile', methods=['GET'])
@student_required
def edit_profile():
    uid = fb_auth.decode_token(session['token'])['uid']
    data = fb_student.get_info(uid)
    return render_template('student/edit_profile.html', data=data)


@student.route('/education', methods=['POST'])
@student_required
def education():
    uid = fb_auth.decode_token(session['token'])['uid']
    if request.method == 'POST':
        education_data = {
            'name': request.form['name'],
            'date': request.form['date'],
            'degree': request.form['degree']
        }
        fb_student.add_education(uid, education_data)
    return redirect(url_for('.edit_profile'))


@student.route('/experience', methods=['POST'])
@student_required
def experience():
    uid = fb_auth.decode_token(session['token'])['uid']
    if request.method == 'POST':
        experience_data = {
            'name': request.form['name'],
            'date': request.form['date'],
            'position': request.form['position'],
            'detail': request.form['detail']
        }
        fb_student.add_experience(uid, experience_data)
    return redirect(url_for('.edit_profile'))


@student.route('/coursework', methods=['POST'])
@student_required
def coursework():
    uid = fb_auth.decode_token(session['token'])['uid']
    if request.method == 'POST':
        coursework_data = {
            'code': request.form['code'],
            'name': request.form['name']
        }
        fb_student.add_coursework(uid, coursework_data)
    return redirect(url_for('.edit_profile'))
