#-----------Flask Hello World---------#
#import flask
from flask import Flask

#create app
app = Flask(__name__)

#Error Handling --DEBUG MODE--
app.config["DEBUG"]=True

#use decorators
@app.route("/")
@app.route("/hello")
#define function
def hello_world():
    return "Hello, World!?!?!?!?!?!?!?!"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "bancroft":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404

#start dev server
if __name__ == "__main__":
    app.run(debug=True) ##--Activate Debug Mode--

