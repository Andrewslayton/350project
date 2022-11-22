from re import A
from flask import Flask, render_template, request, redirect, url_for, flash

#Flask is the web service used
app = Flask(__name__)

#The template displayed when website is opened
@app.route("/")
def index(): 
    return render_template("model.html")


#when website/1 is called returns the template of product description1
@app.route("/1")

def prod1():
        return render_template("projectD1.html")
#when website/2 is called returns the template of product description2
@app.route("/2")
def prod2():
        return render_template("projectd2.html")
#when website/2 is called returns the template of product description2
@app.route("/3")
def prod3():
        return render_template("projectd3.html")

    



@app.route("/<usr>")
def user(usr):
    
        return f"<h1>{usr}<h1>"





if __name__ == "__main__":
    app.run(debug=True)