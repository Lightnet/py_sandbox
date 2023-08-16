import functools
from flask import (
  Blueprint, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for
)
import jwt
from .models import db, conn
from .models import User

bp = Blueprint('auth', __name__)

@bp.route("/signin")
def page_signin():
  return render_template('signin.html')

@bp.route("/api/auth/signin",methods=['POST'])
def auth_signin():
  user = request.get_json()
  print("POST USER: ",user)
  #check for empty field
  if not user['alias'] or not user['passphrase']:
    #print("EMPTY?")
    return jsonify({"api":"EMPTY"})
  #query user alias id
  query = User.select().where(User.columns.alias == user['alias'])
  output = conn.execute(query)
  result = output.fetchone()
  #print("RESULT: ",result)
  if result: #check if not exist
    #print("result: ",result)#go by colums
    #print("result1: ",result[1])#alias
    #print("result2: ",result[2])#passphrase
    #print("result3: ",result[3])
    if result[2] == user['passphrase']:
      #return jsonify({"api":"PASS"})
      #set up token for cookie browser access
      token = jwt.encode({"alias": user['alias'], 'date':"NOne"}, "secret", algorithm="HS256")
      #set content
      resp = make_response(jsonify({"api":"GRANTED","token":{"alias":user['alias'],"role":"member"},}))
      #set cookie
      resp.set_cookie('token', token)
      #return to header data to browser
      return resp
    else:
      return jsonify({"api":"FAIL"})
    
  else:# if exist return true
    return jsonify({"api":"NONEXIST"})
  
  return jsonify({"api":"ERROR"})

@bp.route("/signup")
def page_signup():
  return render_template('signup.html')

@bp.route("/api/auth/signup",methods=['POST'])
def auth_signup():

  user = request.get_json()
  print("POST USER: ",user)

  query = User.select().where(User.columns.alias == user['alias'])
  output = conn.execute(query)
  print("RESULT: ",output.fetchone())
  if output.fetchone() == None: #check if not exist
    #print("user['alias']: ",user['alias'])
    #print("user['passphrase']: ",user['passphrase'])

    query = db.insert(User).values(alias=user['alias'], passphrase=user['passphrase'])
    Result = conn.execute(query)
    print("INSERT!")
    print("Result: ", Result)
    conn.commit()
    return jsonify({"api":"CREATED"})
  else:# if exist return true
    return jsonify({"api":"EXIST"})
  return jsonify({"api":"ERROR"})

@bp.route("/signout")
def page_signout():
  return render_template('signout.html')

@bp.route("/api/auth/signout")
def auth_signout():
  token = request.cookies.get('token')
  if token:
    

    resp = make_response(jsonify({"api":"LOGOUT"}))
    #set cookie
    resp.set_cookie('token', '', expires=0)
    return resp
  else:
    return jsonify({"api":"ERROR"})