# import flask
from flask import *

# below we create a web server based application
app = Flask(__name__)



# below we create the home route
# routing:this is mapping diiferent resources to diff functions . We do this by the help of a decorater
@app.route("/api/home")
def home():
    return jsonify({"message": "Home Route accessed"})



# below is the products route
@app.route("/api/products")
def product():
    return jsonify({"message" : "Welcome to the products route"})





# below is route for addition.
@app.route("/api/calc", methods=["POST"])
def calculator():
    if request.method == "POST":
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        sum = int(number1) + int(number2)

        return jsonify({"The sum is ": sum})
    



@app.route("/api/calculator", methods=["POST"])
def simpleinterest():
    if request.method == "POST":
        principal = request.form["principal"]
        rate= request.form["rate"]
        time = request.form["time"]
        simple_interest = int(principal) * int(rate) * int(time)/100
        

        return jsonify({"The simple interest is ": simple_interest})
    


























# below we run the application
app.run(debug=True)

