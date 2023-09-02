from .app_main import app
import alchemy.route as route
import alchemy.auth as auth
import alchemy.config as config
import alchemy.entity as entity
import alchemy.todotask as todotask

def create_app():
  #app.config['DEBUG'] = True
  #print("config PORT:", config.PORT)

  #blueprint
  app.register_blueprint(route.bp)
  app.register_blueprint(auth.bp)
  app.register_blueprint(entity.bp)
  app.register_blueprint(todotask.bp)

  #app.run()
  #app.run(debug=True, port=3000)
  return app