from flask import render_template, url_for, flash, redirect, session, request
from website import app, bcrypt, db, login_manager, access_levels
from website.models import User, Admin_users
from flask_login import UserMixin, login_user, login_required, logout_user, current_user
import website.form_validation as forms


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = forms.Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect password")
                return render_template('login.html', form=form)
        else:
            flash("User does not exists")
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = forms.Register()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(
            form.password.data)
        user = User(username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash("Sucessfully created account now please login with your credentials")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if Admin_users.query.filter_by(user_id=current_user.id).first() != None:
        return render_template('dashboard.html', Admin=True)
    return render_template('dashboard.html', Admin=False)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))
