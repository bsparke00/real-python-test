#-----------Flask Hello World---------#
#import flask
from flask import Flask
#create app
app = Flask(__name__)
#use decorators
@app.route("/")
@app.route("/hello")
#define function
def hello_word():
    print "Hello, World!"
#start dev server
if __name__ == "__main__":
    app.run()
