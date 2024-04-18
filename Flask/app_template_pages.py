from flask import Flask, render_template

app = Flask(__name__) # is __name__ special variable name?

@app.route("/")  #base page
def index():
    return render_template("index.html") 

@app.route("/about") #about page
def about():
    return "THIS IS MY ABOUT PAGE"

@app.route("/data") # data page. Note that the structure of all pages is same
def data():
    return "THIS IS MY DATA PAGE"

if __name__=="__main__": # what this code do?
    app.run(debug=True)