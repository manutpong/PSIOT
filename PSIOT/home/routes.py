from flask import Blueprint, jsonify

home = Blueprint('home', __name__)


@home.route("/")
@home.route("/home")
def index():
    return "<h1>Home Page test main </h1>"


@home.route("/about")
def about():
    a = {
        'code': '1234',
        'name': '33333',
        'list': [{'course': '111111'},
                 {'course': '222222'}
                 ]
    }
    return jsonify(a)
