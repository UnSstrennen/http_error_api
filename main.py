from flask import Flask, abort, render_template, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:code>')
def error(code):
    if code == 302:
        return redirect('/')
    if code == 200:
        return 'success'
    return abort(code)


if __name__ == '__main__':
    app.run()
