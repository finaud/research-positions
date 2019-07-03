from flask import Blueprint, render_template, session
import functools

auth = Blueprint('auth', __name__)


def student_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'token' not in session or session['user_type'] != 'student':
            return "student login required"
            # return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


def prof_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'token' not in session or session['user_type'] != 'prof':
            return "prof login required"
            # return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@auth.route('/')
def index():
    return "auth view"
