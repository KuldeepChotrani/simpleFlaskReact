# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask_restful import Resource, Api
from resources.helloWorld import HelloWorld
from flask_cors import CORS
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
app.secret_key = "kuldeep"
api = Api(app)
cors = CORS()
cors.init_app(app)
api.add_resource(HelloWorld, '/hello')
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()