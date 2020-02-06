from flask import Flask
from . import timezone

app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'The time is !'


if __name__ == "__main__":
    app.run(debug=True)
