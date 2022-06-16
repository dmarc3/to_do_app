from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from to_do_app.input_validation import get_valid_input
from to_do_app import task


# Define parser and request args
parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('description', type=str)
parser.add_argument('start_date', type=str)
parser.add_argument('due_date', type=str)
parser.add_argument('priority', type=str)

class Task(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.sort_query('task_id', 'ASC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


class Priority(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.sort_query('priority', 'DESC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


class DueDate(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.sort_query('due_date', 'ASC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


# class Between(Resource):
#     def get(self):
#         task_collection = task.TaskCollection()
#         query = task_collection.filter_closed_between_query(
#             start=dates['start_date'], end=dates['due_date'])
#         result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
#         return jsonify(result)


class Overdue(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.filter_overdue_query()
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)

class AddTask(Resource):
    def post(self):
        args = parser.parse_args()
        return jsonify(**args)

def run_app(path="sqlite:///task.db"):
    db = create_engine(path)
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Task, '/tasks')  # task 1-sorted by task id
    api.add_resource(Priority, '/priority')  # task 2-sorted by priority
    api.add_resource(DueDate, '/due_date')  # task 3-sorted by due date
    # dates = get_valid_input(
    #     'start_date',
    #     'REQUEST: What date would you like to start from (YYYY-MM-DD)?\nDATE: ',
    # )
    # # Get end
    # dates = get_valid_input(
    #     'due_date',
    #     'REQUEST: What date would you like to end at (YYYY-MM-DD)?\nDATE: ',
    #     dates,
    # )
    # api.add_resource(Between, f'/between{dates["start_date"]}&{dates["due_date"]}')  # task 4-between two dates
    api.add_resource(Overdue, '/overdue')  # task 5-overdue
    api.add_resource(AddTask, )
    return app, db

def close_app(db):
    """Close app and dispose of database connection"""
    db.dispose()



if __name__ == "__main__":
    app, db = run_app()
    app.run(port="5002")
    close_app(db)
