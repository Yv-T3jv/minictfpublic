from flask import *
import random

app = Flask(__name__)
app.secret_key = str(random.randint(0, 10000000))

@app.route("/")
def index():
  if not "clicks" in session:
    session["clicks"] = 0
  flag = "Get 420 billion clicks to win!"
  if session["clicks"] >= 420000000000:
    flag = "IRS{sample_flag}"
  return render_template("index.html", flag=flag, clicks=session["clicks"])

@app.route("/click")
def click():
  session["clicks"] += 1
  return "ok!"

if __name__ == "__main__":
  app.run("0.0.0.0", 7060)