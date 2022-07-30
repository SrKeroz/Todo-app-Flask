from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user, current_user
from app.models import UserData
from . import auth
from app.forms import LoginForm
from flask import render_template
from app.firestore_service import get_user_id
from app.models import UserModel, UserData

@auth.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    context = {
        "login_form": LoginForm()
    }
    # si el usuario ya esta autenticado lo redireciona al home
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # valida los datos enviados a travez del formulario
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user_id(username)

        # verificamos si el usuario existe
        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()["password"]

            # validados el password
            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                flash("bienvenido de nuevo")

                redirect(url_for("hello"))
            else:
                flash("la informacion proporcionada no coincide")
        else:
            flash("el usuario no existe")
    

        return redirect("/")

    return render_template("login.html", **context)