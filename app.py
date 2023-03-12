from flask import *


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world! \n My brother is an idiot!'


if __name__ == '__main__':
    app.run()
