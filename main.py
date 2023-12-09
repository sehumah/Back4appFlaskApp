"""

A simple RESTful API that is going to serve as a to-do list. (built with Flask and deployed to Back4App Containers)
Users can perform basic CRUD operations:
    - adding tasks
    - deleting tasks
    - marking them as done, and so on.

Tutorial URL: https://blog.back4app.com/how-to-build-and-deploy-a-python-application/



### simple flask boilerplate code ###

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {'detail': 'Hello World!'}


"""
