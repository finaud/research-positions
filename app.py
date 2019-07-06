from flask import Flask
from views.main import main
from views.auth import auth
from views.student import student
from views.prof import prof

import config

from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=59)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(student, url_prefix='/student')
app.register_blueprint(prof, url_prefix='/prof')


@app.errorhandler(404)
def page_not_found(error):
    # return render_template('page_not_found.html'), 404
    return "missing page", 404
