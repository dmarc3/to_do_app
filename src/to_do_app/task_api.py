from flask import Flask, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import task


class Task(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.sort_query('task_id', 'ASC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


class Priority(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.sort_query('priority', 'ASC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


if __name__ == "__main__":
    db_connect = create_engine("sqlite:///task.db")
    app = Flask(__name__)
    api = Api(app) # task 1
    api.add_resource(Task, '/tasks') # task 1-sorted by task id
    api.add_resource(Priority, '/priority') # task 2-sorted by priority
    app.run(port="5002")
    db_connect.dispose()
