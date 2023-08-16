# 
# https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
# https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
# https://www.tutorialspoint.com/sqlalchemy/index.htm
"""
  Note there couple different way to handle function calls.

"""
import os
from flask import (
  Flask, 
  jsonify, 
  render_template, 
  request, 
  url_for, 
  redirect, 
  make_response
)
#import jwt
#import sqlalchemy
#print("sqlalchemy.__version__  :", sqlalchemy.__version__  )
#import sqlalchemy as db
#init flask
app = Flask(__name__,static_folder='../dist')
#init sql
#engine = db.create_engine("sqlite:///database.sqlite")
#conn = engine.connect()
#metadata = db.MetaData() #extracting the metadata
#division= db.Table('divisions', metadata, autoload=True, autoload_with=engine) #Table object
#print(repr(metadata.tables['divisions']))

#def create_app():
  #app.config['DEBUG'] = True
  #app.run()

#create_app()
