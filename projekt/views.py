import pymongo
from pymongo import Connection
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flaskext.bcrypt import Bcrypt, generate_password_hash, \
	check_password_hash
