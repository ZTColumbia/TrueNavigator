from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('homepage'))

@app.route('/homepage')
def homepage():  # put application's code here
    return render_template('homepage.html')

@app.route('/options')
def options():  # put application's code here
    return render_template('Options.html')


if __name__ == '__main__':
    app.run(debug=True)

