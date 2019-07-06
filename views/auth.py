from flask import Blueprint, render_template, session

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return "auth view"


@auth.route('/register', methods=['GET'])
def register():
    return render_template('auth/register.html')


@auth.route('/register_student', methods=['POST'])
def register_student():
    pass


@auth.route('/register_prof', methods=['POST'])
def register_prof():
    pass


@auth.route('/login', methods=['GET'])
def login():
    session.permanent = True
    return render_template('auth/login.html')


@auth.route('/login_student', methods=['POST'])
def login_student():
    pass


@auth.route('/login_prof', methods=['POST'])
def login_prof():
    pass


@auth.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return render_template('index.html')
