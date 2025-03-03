from flask import *
from teacher import visit_page
import threading

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/visit", methods=["POST"])
def visit():
  threading.Thread(target=visit_page, args=(request.form.get("html"),)).start()
  return "The teacher is reviewing your HTML!"

if __name__ == "__main__":
  app.run("0.0.0.0", 7050)