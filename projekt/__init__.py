#imports
import pymongo
from pymongo import Connection
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flaskext.wtf import Form, TextField, TextAreaField, \
    PasswordField, SubmitField, Required, ValidationError
from flaskext.bcrypt import Bcrypt, generate_password_hash, \
	check_password_hash
	

#define app
app = Flask(__name__)

#define bcrypt
bcrypt = Bcrypt(app)

#define the configuration
app.config.from_pyfile('config.cfg')

#imports forms models and views
import projekt.forms
import projekt.views
import projekt.models