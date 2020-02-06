from flask import Flask
import timezone

app = Flask(__name__)


@app.route('/')
def hello_world():
    return timezone.time_finder()


if __name__ == "__main__":
    app.run(debug=True)
