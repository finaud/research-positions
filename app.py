from flask import Flask, render_template
from views.main.controllers import main
from views.auth.controllers import auth
from views.student.controllers import student
from views.prof.controllers import prof

import config


app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(student, url_prefix='/student')
app.register_blueprint(prof, url_prefix='/prof')


@app.errorhandler(404)
def page_not_found(error):
    # return render_template('page_not_found.html'), 404
    return "missing page", 404
