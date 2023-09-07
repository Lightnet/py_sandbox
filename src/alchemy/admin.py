

import functools
from flask import (
  Blueprint, Response, flash, g, jsonify, make_response, redirect, render_template, request, send_from_directory, session, url_for
)
import jwt
import os
from os import path
bp = Blueprint('admin', __name__)

@bp.route("/admin")
def index():
  
  return render_template('admin.html')