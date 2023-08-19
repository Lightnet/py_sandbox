
import functools
from flask import (
  Blueprint, Response, jsonify, make_response, redirect, render_template, request, send_from_directory, session, url_for
)
import jwt
import os
from os import path
bp = Blueprint('admin', __name__)

@bp.route("/admin")
def index():
  token = request.cookies.get('token')
  if token:
    return render_template('admin.html')
  else:
    return render_template('index.html')