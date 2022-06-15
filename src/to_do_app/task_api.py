from flask import Flask, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from to_do_app.input_validation import get_valid_input
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
        query = task_collection.sort_query('priority', 'DESC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


class DueDate(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.sort_query('due_date', 'ASC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


class Between(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.filter_closed_between_query(
            start=dates['start_date'], end=dates['due_date'])
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


class Overdue(Resource):
    def get(self):
        task_collection = task.TaskCollection()
        query = task_collection.filter_overdue_query()
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


if __name__ == "__main__":
    db_connect = create_engine("sqlite:///task.db")
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Task, '/tasks')  # task 1-sorted by task id
    api.add_resource(Priority, '/priority')  # task 2-sorted by priority
    api.add_resource(DueDate, '/due_date')  # task 3-sorted by due date
    dates = get_valid_input(
        'start_date',
        'REQUEST: What date would you like to start from (YYYY-MM-DD)?\nDATE: ',
    )
    # Get end
    dates = get_valid_input(
        'due_date',
        'REQUEST: What date would you like to end at (YYYY-MM-DD)?\nDATE: ',
        dates,
    )
    api.add_resource(Between, f'/between{dates["start_date"]}&{dates["due_date"]}')  # task 4-between two dates
    api.add_resource(Overdue, '/overdue')  # task 5-overdue
    app.run(port="5002")
    db_connect.dispose()
