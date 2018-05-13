#!flask/bin/python
from flask import Flask

app = Flask(__name__)

# Priseless comment

@app.route('/')
def index():
    return "Hello, Gyuri and Pista!"
# Causeless comment

if __name__ == '__main__':
	# Useless comment
    app.run(debug=True, port=3000)
