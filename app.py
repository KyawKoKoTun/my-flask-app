from flask import *


app = Flask(__name__)


@app.route('/')
def main():
    return 'hello world 2'


if __name__ == '__main__':
    app.run(debug=True)