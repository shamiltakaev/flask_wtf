from flask import Flask, render_template


app = Flask(__name__)

@app.route("/training/<prof>")
def index(prof):
    return render_template("training.html", prof=prof)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)