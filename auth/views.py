from flask import render_template, session, redirect, flash, url_for
from . import auth
from app.forms import LoginForm
from flask import render_template

@auth.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    context = {
        "login_form": LoginForm()
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
    
        flash("nombre de usuario registrado con exito")

        return redirect("/")

    return render_template("login.html", **context)