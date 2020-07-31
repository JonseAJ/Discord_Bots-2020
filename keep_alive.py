from flask import Flask
from threading import Thread


app = Flask("")

@app.route('/')
def main():
  return "Ultimate bot is online!"

def run():
   app.run(host="0.0.0.0", port=8080
   )
   #app.run(host="0.0.0.0", port=3333, debug=False)
   #app.run(host="0.0.0.0", port=8080, debug=True)
   #@Werkzeug debugger

def keep_alive():
    server = Thread(target=run)
    server.start()
 
