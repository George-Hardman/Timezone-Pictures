from flask import Flask, render_template
import timezone

app = Flask(__name__)

time = timezone.time_finder()

@app.route('/')
def index():
    return render_template("index.html", time=time)


if __name__ == "__main__":
    app.run(debug=True)
