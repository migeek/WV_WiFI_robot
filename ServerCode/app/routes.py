from flask import render_template, url_for, request, flash, redirect
from app import app_instance
from flask_login import current_user, login_user, login_required, logout_user
from app.forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse
from app import db


import pdb


@app_instance.route('/')
def home():
    return render_template('home.html', title='home')

@app_instance.route('/login',methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template("login.html", title='Login',form=form)

@app_instance.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app_instance.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user")
        return redirect(url_for('login'))
    return render_template('register.html',title='Register', form=form)


@app_instance.route("/robot", methods=["POST", "GET"])
def client():
    user =User.query.get(current_user.get_id())
    return render_template("client.html", username=user.username, password_hash=user.password_hash)


