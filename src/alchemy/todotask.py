
# https://pythonbasics.org/flask-http-methods/
import functools
from flask import (
  Blueprint, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for
)
#from sqlalchemy import JSON
from sqlalchemy import exc
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.orm import Session
from .models import Task, engine

bp = Blueprint('todotask', __name__)
# https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#selecting-orm-entities-and-attributes
@bp.route("/api/task")
def page_task():
  #list
  try:
    with Session(engine) as session:
      results = session.scalars(select(Task).order_by(Task.id)).all()
      #print("results: ",results)
      mytasks = []
      for result in results:
        #print(result)
        #print(result.id)
        mytasks.append(result.to_json())
      #print(mytasks)
      return jsonify(mytasks)
  except exc.SQLAlchemyError as e:
    print("ERROR: ", e)
    pass

  return jsonify({"api":"ERROR"})

@bp.route("/api/task", methods=['POST'])
def task_post():
  data = request.get_json()
  print(data)
  if data:
    content = data['content']
    if content != "":
      print("DATA:",data)
      with Session(engine) as session:
        newTask = Task(
          content=data['content']
        )
        session.add_all([newTask])
        try:
          session.commit()
          return jsonify({"api":"CREATED","id":newTask.id})
        except exc.SQLAlchemyError as e:
          session.rollback()
        

  return jsonify({"api":"ERROR"})

@bp.route("/api/task/<id>", methods=['PUT'])
def task_put(id):
  data = request.get_json()
  print("update data: ",data)
  if data:
    if data['id']:
      with Session(engine) as session:
        print(data['content'])
        print("session update")
        #session.execute(update(Task).where(Task.id == id).values(Task.content==data['content'])).scalar()# if nothing return None
        session.execute(update(Task).where(Task.id == id).values(content = data['content']))
        session.commit()
        return jsonify({"api":"UPDATE"})
    
  
  return jsonify({"api":"ERROR"})

@bp.route("/api/task/<id>", methods=['DELETE'])
def task_delete(id):
  print("ID: ", id)
  if id:
    with Session(engine) as session:
      print("session delete")
      result = session.execute(select(Task).where(Task.id == id)).scalar()# if nothing return None
      print("result: ", result)
      if result:
        try:
          session.delete(result)
          session.commit()
          return jsonify({"api":"DELETE"})
        except:
          session.rollback()
  return jsonify({"api":"ERROR"})







