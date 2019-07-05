from flask import Blueprint, render_template, session
import functools

prof = Blueprint('prof', __name__)


def prof_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'token' not in session or session['user_type'] != 'prof':
            return "prof login required"
            # return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@prof.route('/')
@prof_required
def index():
    return "prof view"
