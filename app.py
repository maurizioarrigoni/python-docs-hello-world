# from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
# def hello():
#     return "Hello world!"
# https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
def index():
    return render_template('test_app_services.html')