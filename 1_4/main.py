from flask import Flask, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def index():
    params = {
        "title": "Анкета",
        "surname": "Wathy",
        "name": "Mark",
        "education": "Высшее",
        "profession": "штурман марсохода",
        "gender": "male",
        "motivation": "Всегда мечтал застрять тут",
        "ready": "True"
    }
    return render_template("auto_answer.html", **params)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)