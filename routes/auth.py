from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from models.user import User
from extensions import db

auth = Blueprint("auth", __name__)


# ==========================
# Register
# ==========================
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        # Check Username
        user = User.query.filter_by(username=username).first()

        if user:
            flash("Username already exists!", "danger")
            return redirect(url_for("auth.register"))

        # Check Email
        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists!", "danger")
            return redirect(url_for("auth.register"))

        # Create User
        new_user = User(
            username=username,
            email=email
        )

        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful. Please Login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


# ==========================
# Login
# ==========================
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip()
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):

            session["user_id"] = user.id
            session["username"] = user.username

            flash("Login Successful!", "success")

            return redirect("/dashboard")

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")


# ==========================
# Logout
# ==========================
@auth.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully", "success")

    return redirect("/")