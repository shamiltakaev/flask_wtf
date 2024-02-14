from flask import Flask, render_template, redirect
from login_form import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/success")

    return render_template("login.html", title="Аварийный доступ", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
