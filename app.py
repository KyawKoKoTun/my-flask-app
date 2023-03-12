from flask import *


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world! \n<h1>My brother is an idiot!</h1>'


if __name__ == '__main__':
    app.run()
