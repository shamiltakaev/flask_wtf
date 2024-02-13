from flask import Flask, render_template


app = Flask(__name__)

@app.route("/list_prof/<lst>")
def index(lst):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template("index.html", lst=lst, professions=professions)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)