from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def main():     
     return render_template("box.html")

@app.route("/authenticate/", methods = ['GET'])
def auth():
        #request.form
        #request.form['user']
        return render_template("base.html", q = "Harambe")

if __name__ =="__main__":
    app.debug=True
    app.run()



