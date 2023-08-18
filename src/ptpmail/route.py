# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
# simple basic url access
import functools
from flask import (
  Blueprint, Response, flash, g, jsonify, make_response, redirect, render_template, request, send_from_directory, session, url_for
)
import jwt
import os
from os import path
bp = Blueprint('route', __name__)

#@bp.route("/<path:path>")
#def send_report(path):
  #return send_from_directory('../dist', path)

#@bp.route("/")
#def index():
  #return render_template('index.html')

def root_dir():  # pragma: no cover
  return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
  try:
    src = os.path.join(root_dir(), filename)
    # Figure out how flask returns static files
    # Tried:
    # - render_template
    # - send_file
    # This should not be so non-obvious
    return open(src).read()
  except IOError as exc:
    return str(exc)

@bp.route("/")
def index():
  content = get_file('../../dist/index.html')
  return Response(content, mimetype="text/html")
  #return render_template('index.html')
  
# https://stackoverflow.com/questions/17295086/python-joining-current-directory-and-parent-directory-with-os-path-join
@bp.route("/assets/<path:path>")
def assets(path):
  mimetypes = {
    ".css": "text/css",
    ".html": "text/html",
    ".js": "application/javascript",
  }
  print("root_dir(): ", root_dir())
  #complete_path = os.path.join(root_dir(), "..\..\dist")
  #complete_path = os.path.join(complete_path, f"..\\..\\dist\\{path}" )
  complete_path = os.path.join(root_dir(), "..\\..\\dist\\assets\\", path )
  complete_path = os.path.normpath(complete_path)
  print("complete_path: ", complete_path)
  #print(os.path.normpath(complete_path))

  ext = os.path.splitext(path)[1]
  mimetype = mimetypes.get(ext, "text/html")
  content = get_file(complete_path)
  return Response(content, mimetype=mimetype)