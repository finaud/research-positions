from flask import Blueprint, render_template, session
import functools

student = Blueprint('student', __name__)


def student_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'token' not in session or session['user_type'] != 'student':
            return "student login required"
            # return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@student.route('/')
@student_required
def index():
    return "student view"
