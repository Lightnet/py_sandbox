
# https://pythonbasics.org/flask-http-methods/
import functools
from flask import (
  Blueprint, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for
)
#from sqlalchemy import JSON
from sqlalchemy import exc
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Task, engine

bp = Blueprint('todotask', __name__)
# https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html#selecting-orm-entities-and-attributes
@bp.route("/api/task")
def page_task():
  #list
  try:
    with Session(engine) as session:
      #results = session.execute(select(Task).order_by(Task.id)).scalars()
      #results = session.execute(select(Task).order_by(Task.id)).all()
      results = session.scalars(select(Task).order_by(Task.id)).all()
      print("results: ",results)
      #print("results: ",results[0][0])
      #print("results: ",jsonify(results))
      mytasks = []
      for result in results:
        print(result)
        print(result.id)
        #print("results: ",jsonify(result))
        mytasks.append(result.to_json())
      print(mytasks)
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
        except exc.SQLAlchemyError as e:
          session.rollback()
        

  return jsonify({"api":"ERROR"})

@bp.route("/task", methods=['PUT'])
def task_put():
  data = request.json()
  if data:

    pass
  
  return jsonify({"api":"ERROR"})

@bp.route("/task/<id>", methods=['DELETE'])
def task_delete(id):
  print("ID: ", id)

  #guide = Guide.query.get(id)
  #db.session.delete(guide)
  #db.session.commit()
  
  return jsonify({"api":"ERROR"})







