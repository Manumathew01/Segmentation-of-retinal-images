import requests
from flask import Flask, render_template, url_for, redirect


UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



@app.route('/')
def main():
    return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
