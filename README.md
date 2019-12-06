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

  - hangman-shell.py -- prototype shell program to flesh out the logic of the game
  - .gitignore

# To install:
  - Clone the repository:
  - Install Python

# Credits:
  - Hangman SVG and functions cribbed from vlopezferrando's implementation
  - Authentication blueprints inspired by tholsapp's implementation, itself
    a modification from Michel Grinberg's Mega-Flask Tutorial
  - Application infrastructure inspired by Cookiecutter Flask application     blueprints
