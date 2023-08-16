# https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy
# 

from alchemy import create_app

if __name__ == "__main__":
  #print("Hello World")
  app=create_app()
  app.run(
    debug=True,
    port=3000,
    #static_url_path='',
    #static_folder='../dist'
  )