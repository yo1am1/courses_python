import flask
import requests

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", name="Yegor")


@app.route("/name")
def name():
    return "Yegor"


@app.route("/rty")
def rty():
    r = requests.get('http://api.open-notify.org/astros.json')

    return


@app.errorhandler(404)
def page_not_found(error):
    return "Error! Not found (", 404


if __name__ == '__main__':
    app.run(debug=True)
