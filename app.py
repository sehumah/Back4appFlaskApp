from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///default.db'
db.init_app(app=app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=False)

    is_done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=True)
    updated_at = db.Column(db.DateTime, default=None, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f'<Task {self.title}>'


@app.route('/')
def index():
    return {
        'name': 'Back4app Flask Todo App',
        'description': 'a simple todo app written in flask',
        'version': 1,
    }


@app.route('/api/')
def tasks():
    json = [task.as_dict() for task in Task.query.all()]
    return jsonify(json)


@app.route('/api/<int:task_id>', methods=['GET', 'DELETE'])
def task_detail(task_id):
    task = db.get_or_404(Task, task_id)

    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()

        return {
            'detail': 'Task has been deleted successfully.'
        }
    else:
        return task.as_dict()


@app.route('/api/create/', methods=['POST'])
def create_task():
    name = request.form.get('name')
    description = request.form.get('description')

    if name is None or description is None:
        return {
            'detail': 'Please provide the name and the description.'
        }, 400

    task = Task(name=name, description=description)
    db.session.add(task)
    db.session.commit()

    return task.as_dict()


@app.route('/api/toggle/<int:task_id>/')
def toggle(task_id):
    task = db.get_or_404(Task, task_id)

    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True

    task.updated_at = datetime.now()
    db.session.commit()

    return task.as_dict()
