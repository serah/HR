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
from HR.models import users,vacancy

#@app.teardown_request
#def shutdown_session(exception=None):
#    db_session.remove()

@app.route('/')
def hello():
	"""
	Function handler for /
	"""
	return render_template('index.html', hello=True)

@app.route('/vacancy')
def vacancy():
  return render_template('vacancy.html')

@app.route('/application')
def application():
  year = datetime.now().year
  return render_template('application.html', currentyear=year)


@app.route('/applicants')
def applicants():
  namelist = []
  for name in User.query.filter(User.name):
    namelist.append(name)
  print namelist
  return render_template('applicants.html',names=namelist)

@app.route('/applicant/<unique_id>')
def applicant(unique_id):
  foo = "This is your unique id " + unique_id
  return render_template('applicant.html', foo2=foo)

@app.route('/panel')
def panel():
  return render_template('panel.html')

@app.route('/about')
def about():
  return render_template('index.html', about=True)

@app.route('/contact')
def contact():
  return render_template('index.html', contact=True)

@app.route('/login', methods=["POST", "GET"])
def login(self):
  if request.method == "POST":
    email = request.method['email']
    password = request.method['password']
    #hashed will come from the db
    #if check_password_hash(hashed, password):
      #login true
    #else:
      #return an error on the same page
    #insert into db
  return "foo"

@app.route('/position',methods=["POST","GET"])
def position():
  return render_template('position.html')

@app.route('/add_position')
def add_position():
  return render_template('add_position.html')

@app.route('/logout')
def logout():
  pass

