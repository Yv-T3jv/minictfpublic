from flask import *
import random
import string
import os

# the art of confusion
_open = open
code = """
from shutil import *
from sqlite3 import *
from subprocess import Popen
from multiprocessing import *
from pickle import *
from tkinter import *
from sysconfig import * 
from pstats import * 
from xdrlib import * 
from cmd import * 
from linecache import * 
from distutils.spawn import * 
from dbm import * 
from audioop import * 
from mailbox import * 
from imaplib import * 
from mailcap import * 
from glob import * 
from optparse import * 
from shelve import * 
from pipes import * 
from mmap import * 
from contextlib import * 
from uuid import * 
from zlib import * 
from cgi import *
""".split("\n")
random.shuffle(code)
for line in code:
  exec(line)

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# nope!
app.jinja_env.globals.clear()

def bot_review_code(dump_id):
  content = Popen(["curl", f"http://localhost:4242/view_dump/{dump_id}"], stdout=-1).communicate()[0]
  if len(content) % 2 == 0:
    return "Good code!"
  return "Bad code!"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/add_code", methods=["POST"])
def add_code():

  code = request.form.get("code")

  # save code
  dump_id = "".join(random.choice(string.ascii_letters) for _ in range(16))
  with _open(f"templates/{dump_id}.html", "w") as w:
    w.write(code)

  # return
  return f"Your dump id is: {dump_id}"

@app.route("/review_code", methods=["POST"])
def review_code():

  dump_id = request.form.get("dump_id")
  if not f"{dump_id}.html" in os.listdir("templates"):
    return "Invalid dump id!"
  
  result = bot_review_code(dump_id)
  os.remove(f"templates/{dump_id}.html")

  return f"Your code has been reviewed: {result}"

@app.route("/view_dump/<dump_id>")
def view_dump(dump_id):
  if request.remote_addr == "127.0.0.1": # only admin!
    return render_template(f"{dump_id}.html")
  else:
    return "Not authorized!"

if __name__ == "__main__":
  app.run("0.0.0.0", 7000)