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

@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')

@app.route('/lesson2')
def lesson2():
    return render_template('lesson2.html')

@app.route('/lesson3')
def lesson3():
    return render_template('lesson3.html')


if __name__ == '__main__':
    app.run(debug=True)
