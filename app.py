
from flask import Flask
# Flask constructor takes the name of 
# current module (__name__) as argument.

app = Flask(__name__)
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return "This is hello page"
@app.route("/test")
def testpage():
    return "This is test page"


# main driver function
if __name__ == '__main__':
    app.run(debug=True)
