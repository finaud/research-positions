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


@auth.route('/register', methods=['GET'])
def register():
    pass


@auth.route('/register_student', methods=['POST'])
def register_student():
    pass


@auth.route('/register_prof', methods=['POST'])
def register_prof():
    pass


@auth.route('/login', methods=['GET'])
def login():
    pass


@auth.route('/login_student', methods=['POST'])
def login_student():
    pass


@auth.route('/login_prof', methods=['POST'])
def login_prof():
    pass
