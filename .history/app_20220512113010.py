from crypt import methods
import requests
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return '<p>Hello</p>'


if __name__ == "__main__":
    app.run(debug=True)
