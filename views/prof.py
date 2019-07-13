from flask import Blueprint, render_template, session, redirect, url_for
import functools

from functions import firebase_auth as firebase

prof = Blueprint('prof', __name__)


def prof_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'token' not in session or not firebase.verify_token(session['token']) or session['user_type'] != 'prof':
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


@prof.route('/')
@prof_required
def index():
    return "prof view"


@prof.route('/home', methods=['GET'])
@prof_required
def home():
    data = {}  # retrieve info
    return render_template('prof/home.html', data=data)

