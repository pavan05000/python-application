#Import Flask, if not then install and import.
import os
try:
  from flask import *
except:
  os.system("pip3 install flask")
  from flask import *
app = Flask(__name__)
@app.route("/")
def index():
  return "<h1>github changes</h1>"
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=False)
