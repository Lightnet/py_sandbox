import functools
from flask import (
  Blueprint, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for
)
import jwt
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import exc
from .models import User, engine

bp = Blueprint('auth', __name__)
#================================================
# SIGN IN
#================================================
@bp.route("/signin")
def page_signin():
  return render_template('signin.html')

@bp.route("/api/auth/signin",methods=['POST'])
def auth_signin():
  user = request.get_json()
  print("user: ", user)
  #check for empty field
  if not user['alias'] or not user['passphrase']:
    #print("EMPTY?")
    return jsonify({"api":"EMPTY"})
  try:
    with Session(engine) as session:
      result = session.execute(select(User).where(User.alias == user['alias'])).scalar()# if nothing return None
      if result: #check if not exist
        if result.passphrase == user['passphrase']:
          print("PASSWORD PASS!")
          token = jwt.encode({"alias": user['alias'], 'date':"NOne"}, "secret", algorithm="HS256")
          #set content
          resp = make_response(jsonify({"api":"GRANTED","token":{"alias":user['alias'],"role":"member"},}))
          #set cookie
          resp.set_cookie('token', token)
          #return to header data to browser
          return resp
        else:
          return jsonify({"api":"FAIL"})
      else:# if does not exist return false
        return jsonify({"api":"NONEXIST"})

  except exc.SQLAlchemyError as e:
    print("USER SIGN IN ERROR!", e)
    #session.rollback()
    #pass

  return jsonify({"api":"ERROR"})
#================================================
# SIGN UP
#================================================
@bp.route("/signup")
def page_signup():
  return render_template('signup.html')

@bp.route("/api/auth/signup",methods=['POST'])
def auth_signup():

  user = request.get_json()
  if not user['alias'] or not user['passphrase']:
    #print("EMPTY?")
    return jsonify({"api":"EMPTY"})
  print("POST USER: ",user)
  try:
    with Session(engine) as session:
      result = session.execute(select(User).where(User.alias == user['alias'])).scalar()# if nothing return None
      print("RESULT: ", result)
      if result:
        print("FOUND")
        print("USER:", result)
        print("USER:", result.id)
        return {"api":"EXIST"}
      else:
        newUser = User(
          alias = user['alias'],
          passphrase = user['passphrase']
        )
        session.add_all([newUser])
        session.commit()
        return {"api":"PASS"}
  except exc.SQLAlchemyError as e:
    print("USER SIGN UP ERROR!", e)
    #session.rollback()
  return jsonify({"api":"ERROR"})
#================================================
# SIGN OUT
#================================================
@bp.route("/signout")
def page_signout():
  return render_template('signout.html')

@bp.route("/api/auth/signout",methods=['POST'])
def auth_signout():
  token = request.cookies.get('token')
  if token: #check if token exist
    resp = make_response(jsonify({"api":"LOGOUT"}))
    #set cookie
    resp.set_cookie('token', '', expires=0)#clear token data
    return resp
  
  return jsonify({"api":"ERROR"})
#================================================
# USER
#================================================
# for render get if already login
@bp.route("/api/auth/user")
def auth_user():
  token = request.cookies.get('token')
  if token: #check if token exist
    userData = jwt.decode(token, "secret", algorithms=["HS256"])
    if userData:
      with Session(engine) as session:
        result = session.execute(select(User).where(User.alias == userData['alias'])).scalar()# if nothing return None
        if result:
          print("USER DATA:", result)
          resp = make_response(jsonify({"api":"USER","token":{"alias":result.alias,"role":"member"}}))
          #set cookie
          #resp.set_cookie('token', '', expires=0)#clear token data
          return resp
  else:
    return jsonify({"api":"NOTLOGIN"})  
  return jsonify({"api":"ERROR"})

#================================================
# RECOVERY
#================================================

#================================================
# EMAIL ???
#================================================



