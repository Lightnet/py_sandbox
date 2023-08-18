from ptpmail import create_app

if __name__ == "__main__":
  #print("Hello World")
  app=create_app()
  app.run(
    debug=True,
    port=3000
  )