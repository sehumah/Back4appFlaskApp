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


some Docker commands:

1. Build a Docker image: "docker build -t docker-image-name:1.0 ."
2. List Docker images: "docker images"
3. Run a new Docker container: "docker run -it -p 5000:5000 docker-image-name:1.0"
"""
