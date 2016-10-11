from flask import Flask, render_template, request, session, redirect, url_for
from utils import register
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)
@app.route("/")
def main():
     if "user" in session:
         return redirect(url_for('page'))
     return render_template("box.html")

@app.route("/authenticate/", methods = ['POST'])
def auth():
        s = register.login(request.form["user"],request.form["password"])
        if s == "Welcome":
            session["user"] = request.form["user"]
        return render_template("base.html", q = s)

@app.route("/reg/", methods = ['POST'])
def rag():
        s = register.regi(request.form["user"],request.form["password"])
        if s == "Added":
            session["user"] = request.form["user"]
        return render_template("base.html", q = s)
                         
@app.route("/welcome/", methods = ['GET'])
def page():
     return render_template("base.html", q = "So you have already logged in")

@app.route("/bye/", methods = ['POST'])
def bye():
     if "user" in session:
        session.pop("user")
     return render_template("box.html")

  
if __name__ =="__main__":
    app.debug=True
    app.run()



