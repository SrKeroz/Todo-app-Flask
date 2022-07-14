from flask import render_template, request, make_response, redirect, session, flash

import unittest


from app import create_app
from app.forms import LoginForm

app = create_app()

todo = ["todo1", "todo2", "todo3"]




@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template("500.html", error=error)



@app.route("/")
def index():
    user_ip = request.remote_addr

    response = make_response(redirect("/hello")) # hacer una redireccion
    # response.set_cookie("user_ip", user_ip) #setear cookies y guardar la ip
    session["user_ip"] = user_ip # guarda la ip en un session

    return response



@app.route("/hello", methods=["GET", "POST"])
def hello():
    # user_ip = request.cookies.get("user_ip") # obtener la ip desde la cookie
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    username = session.get("username")

    context = {
        "user_ip": user_ip,
        "todo": todo,
        "login_form": login_form,
        "username": username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username

        flash("nombre de usuario registrado con exito")

        return redirect("/")

    return render_template("hello.html", **context) # renderizaar templates



if __name__ == "__main__":
    app.run(None, 3000, True)