#import pymongo
#from pymongo import Connection
#from bson.objectid import ObjectId, InvalidId
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.bcrypt import Bcrypt, generate_password_hash, \
	check_password_hash
#from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from HR import app


@app.route('/')
def hello():
	"""
	Function handler for /
	"""
	return render_template('index.html')

@app.route('/vacancy')
def vacancy():
  return render_template('vacancy.html')

@app.route('/application')
def application():
  year = datetime.now().year
  return render_template('application.html', currentyear=year)

@app.route('/applicants')
def applicants():
  return render_template('applicants.html')

@app.route('/applicant/<unique_id>')
def applicant(unique_id):
  foo = "This is your unique id " + unique_id
  return render_template('applicant.html', foo2=foo)

