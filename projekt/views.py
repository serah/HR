import pymongo
from pymongo import Connection
from bson.objectid import ObjectId, InvalidId
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.bcrypt import Bcrypt, generate_password_hash, \
	check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from projekt import app


@app.route('/')
def hello():
	"""
	Function handler for /
	"""
	return render_template('index.html')