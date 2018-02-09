from flask import render_template,redirect,url_for,flash
from . import auth
from ..models import Admin
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required

@auth.route('/adminlogin',methods = ["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = Admin.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.admin'))
        flash('Invalid username or Password')

    title = "blog admin login"
    return render_template('auth/admin_login.html',login_form=login_form,title=title)

@auth.route('/adminregister',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Admin(email = form.email.data,username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.adminlogin'))
        title = "New Account"
    return render_template('auth/admin_register.html',registration_form = form)
@auth.route('/adminlogout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth/adminlogin.html"))