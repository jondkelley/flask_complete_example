# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2019 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import os
import sys

import click
from flask import Flask
from flask import redirect, url_for, abort, render_template, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from webroutes import web
from models import *
from forms import *
import config
app = Flask(__name__)

# setup the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config.from_object('config.Development')

@login_manager.user_loader
def load_user(user_id):
    return None


#db = SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(web)

# handlers
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Note=Note, Author=Author, Article=Article, Writer=Writer, Book=Book,
                Singer=Singer, Song=Song, Citizen=Citizen, City=City, Capital=Capital,
                Country=Country, Teacher=Teacher, Student=Student, Post=Post, Comment=Comment, Draft=Draft, User=User)


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


# same with:
# @db.event.listens_for(Draft.body, 'set', named=True)
# def increment_edit_time(**kwargs):
#     if kwargs['target'].edit_time is not None:
#         kwargs['target'].edit_time += 1
