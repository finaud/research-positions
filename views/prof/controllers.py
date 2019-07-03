from flask import Blueprint, render_template

prof = Blueprint('prof', __name__)


@prof.route("/")
def index():
    return "prof view"
