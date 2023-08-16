# simple basic url access
import functools
from flask import (
  Blueprint, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for
)
import jwt

bp = Blueprint('entity', __name__)

@bp.route("/entity")
def index():
  return render_template('entity.html')