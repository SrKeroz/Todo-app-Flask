from flask import render_template, session, redirect, flash, url_for
from flask_login import login_required, login_user, current_user, logout_user
from app.models import UserData
from . import auth
from app.forms import LoginForm
from flask import render_template
from app.firestore_service import get_user_id, user_put
from app.models import UserModel, UserData
from werkzeug.security import generate_password_hash, check_password_hash

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

            # valida la password cuando esta hasheada
            if check_password_hash or password (user_doc.to_dict()['password'], password):
                user_data = UserData(username,password)
                user = UserModel(user_data)

            # validados el password
            #if password == password_from_db:
             #   user_data = UserData(username, password)
             #   user = UserModel(user_data)

                login_user(user)

                flash("bienvenido de nuevo")

                redirect(url_for("hello"))
            else:
                flash("la informacion proporcionada no coincide")
        else:
            flash("el usuario no existe")
    

        return redirect("/")

    return render_template("login.html", **context)


@auth.route("logout")
@login_required
def logout():
    logout_user()
    flash("regresa pronto")

    return redirect(url_for("auth.login"))


@auth.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user_id(username)

        # verificamos si el usuario ya esta en la base de datos
        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)

            login_user(user)

            flash('Bienvenido!')

            return redirect(url_for('hello'))

        else:
            flash('El usario existe!')

    return render_template('signup.html', **context)