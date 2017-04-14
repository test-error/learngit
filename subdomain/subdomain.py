#coding: utf8
from flask import Flask
import flask

from blueprints import cms

app = Flask(__name__)

app.config.update({
    'SERVER_NAME': 'jd.com:5000'
})

app.register_blueprint(cms.bp)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
