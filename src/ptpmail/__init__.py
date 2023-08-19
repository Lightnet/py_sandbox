from .main_mail import amain
from .main_flask import app

import ptpmail.route as route
import ptpmail.auth as auth
import ptpmail.admin as admin
import ptpmail.email as email

import ptpmail.config as config

def create_app():
  #app.config['DEBUG'] = True

  
  #blueprint
  app.register_blueprint(route.bp)
  app.register_blueprint(admin.bp)
  app.register_blueprint(auth.bp)
  app.register_blueprint(email.bp)

  #app.run()
  #app.run(debug=True, port=3000)
  return app    