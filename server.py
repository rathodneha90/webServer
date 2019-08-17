from flask import Flask, render_template
app = Flask(__name__)
import os


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html",
                           message="following are my contacts",
                           contacts=[i for i in range(10)])


if __name__ == '__main__':
    app.run(debug=True)
