from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('education.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')


if __name__ == '__main__':
    app.run(debug=True)
