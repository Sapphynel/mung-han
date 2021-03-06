from flask import (
    Blueprint,
    render_template,
    current_app,
    jsonify,
    flash,
    redirect,
    request,
    url_for,
)

from flask_login import login_user, logout_user, current_user, login_required

from hangman.extensions import db, login_manager
from hangman.model import *
from .forms import LoginForm, RegistrationForm


blueprint = Blueprint("auth", __name__)

@blueprint.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard', username=current_user.username))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
          flash('Invalid username or password')
          return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
          next_page = url_for('main.dashboard', username=form.username.data)
          return redirect(next_page)
    return render_template('auth/login.html', form=form)


@blueprint.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))
