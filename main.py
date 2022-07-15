from data import *
from flask import *

app = Flask(__name__)

@app.route("/get")
def home():
    user = request.args.get('user')
    key = request.args.get('key')
    return get_data(user, key)

@app.route("/put", methods = ['GET', 'POST', 'DELETE'])
def username():
    user = request.args.get('user')
    key = request.args.get('key')
    add = add_data(user, request.form, key)
    return add

@app.route("/tes", methods = ['POST'])
def home1():
    return request.form

app.run(debug=True)
