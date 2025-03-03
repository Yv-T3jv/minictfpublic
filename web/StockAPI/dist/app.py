from flask import *
import base64
import requests

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

api_key = "DAR3J9OGTF5NDNR6"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/scrape")
def scrape():

  url = base64.b64decode(request.args.get("url")).decode()
  
  blacklist = ["localhost", "127.0.0.1", "0.0.0.0"]
  for word in blacklist:
    if word in url:
      return "Nope!"

  url = "http://www.alphavantage.co" + url + f"&interval=5min&apikey={api_key}&function=TIME_SERIES_INTRADAY"
  print(url)
  r = requests.get(url)
  return r.text

@app.route("/admin")
def admin():
  if request.remote_addr == "127.0.0.1":
    return "Welcome admin! The flag is: IRS{sample_flag}"
  else:
    return "You are not the admin, so I cannot show you the flag."

if __name__ == "__main__":
  app.run("0.0.0.0", 6633)