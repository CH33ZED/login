from flask import Flask, render_template, request
from utils import register

app = Flask(__name__)

@app.route("/")
def main():     
     return render_template("box.html")

@app.route("/authenticate/", methods = ['POST'])
def auth():
        return render_template("base.html", q = register.login(request.form["user"],request.form["password"]))

@app.route("/reg/", methods = ['POST'])
def rag():
        return render_template("base.html", q = register.regi(request.form["user"],request.form["password"]))

if __name__ =="__main__":
    app.debug=True
    app.run()



