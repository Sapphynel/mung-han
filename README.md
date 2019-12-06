# Mung-Han
A simple Hangman game.

# Filetree:
  - hangman: The main application
    - auth: authentication blueprint, forms, and views
    - main: main foundation blueprints and views
    - static: held Bootstrap/JQuery/CSS/JS
    - templates: Jinja2 building blocks for HTML
    - init.py: application factory
    - extensions.py: setup module, designed to avoid circular imports
    - model.py: SQLAlchemy-based database schema
    - words.txt: words used for the game, taken from Webster's 2nd edition

  - migrations -- keeps migrations for possible database upgrades
  - hangman-shell.py -- prototype shell program to flesh out the logic of the game
  - .gitignore -- for files that should be ignored while creating and for your particular instance
  - requirements.txt -- holds all required packages

Not tracked:
  - Instance folders and database (specific to instance)
  - Bytefiles


# To install (Unix):
- Clone the repository:
```
git clone https://github.com/Sapphynel/mung-han.git
```

- Install Python
- Create a virtual environment in the newly cloned repo and start it:
```
python -m venv [name of virtual env]
source [name of virtual env]/bin/activate
```
- Install required packages:
```
pip install -r requirements.txt
```

- Configure variables (either through a file or through environment variables)
  - Needed configs: SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS=False
  - Example (in an instance folder in the root repo):
```
  import os

  SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'please-dont-use-this'

  SQLALCHEMY_DATABASE_URI = 'sqlite:///hangman.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
```

- In the application directory (hangman), initialize the environmental variables and database:
```
python
export FLASK_APP=hangman
from hangman import db 
db.create_all()
```

# Run (locally):
```
flask run OR waitress-serve --call 'hangman:create_app'
```
While running, you can view this application at localhost:5000.

# Credits:
  - Hangman SVG and functions cribbed from vlopezferrando's implementation
  - Authentication blueprints inspired by tholsapp's implementation, itself
    a modification from Michel Grinberg's Mega-Flask Tutorial
  - Application infrastructure inspired by Cookiecutter Flask application blueprints
