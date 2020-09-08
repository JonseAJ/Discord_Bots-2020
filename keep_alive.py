This is the code Jonse found on youtube to make his bots be online even after the tabs that are containing and running the codes are closed
Also Jonse found a way to make his bots now online 24/7!
This was done after using this keep_alive code's web link in https://uptimerobot.com

from flask import Flask
from threading import Thread


app = Flask("")

@app.route('/')
def main():
  return "Ultimate bot is online!"

def run():
   app.run(host="0.0.0.0", port=8080
   )

def keep_alive():
    server = Thread(target=run)
    server.start()
 
