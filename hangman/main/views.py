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

from hangman.extensions import db
from hangman.model import *

blueprint = Blueprint("main", __name__)

@blueprint.route('/')
def index():
    return render_template('main/index.html')

@blueprint.route('/dashboard/<username>')
@login_required
def dashboard(username):
    user = User.query.filter_by(username=username).first_or_404()
    games = Game.query.filter_by(player_id=user.id).all()
    print(user)
    print(games)
    return render_template('main/dashboard.html', games=games, user=user)

@blueprint.route('/play')
def new_game():
    if current_user.is_authenticated:
        user_id = current_user.id
    else:
        user_id = None
    game = Game(player_id=user_id)
    db.session.add(game)
    db.session.commit()
    return redirect(url_for('main.play', game_id=game.pk))

@blueprint.route('/play/<game_id>', methods=['GET', 'POST'])
def play(game_id):
    game = Game.query.get_or_404(game_id)

    if request.method == 'POST':
        letter = request.form['letter'].lower()
        if len(letter) == 1 and letter.isalpha():
            game.try_letter(letter)

    if request.is_xhr:
        return jsonify(current=game.current,
                             errors=game.errors,
                             finished=game.finished)
    else:
        return render_template('main/play.html', game=game)
