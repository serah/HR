#imports
#import pymongo
#from pymongo import Connection
#from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.wtf import Form, TextField, TextAreaField, \
    PasswordField, SubmitField, Required, ValidationError
from flask.ext.bcrypt import Bcrypt, generate_password_hash, \
	check_password_hash
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

#define app
app = Flask(__name__)

#define bcrypt
bcrypt = Bcrypt(app)

#define the configuration
app.config.from_pyfile('config.cfg')

#imports forms models and views
import HR.forms
import HR.views
import HR.models

