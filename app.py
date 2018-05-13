#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Pista!"

if __name__ == '__main__':
    app.run(debug=True, port=3000)
