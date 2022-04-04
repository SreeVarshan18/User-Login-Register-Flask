from flask import Flask, render_template

App = Flask(__name__)


@App.route("/")
def home():
    return render_template("login.html")

@App.route("/register")
def search():
    return render_template("register.html")



if __name__ == "__main__":
    App.run()