""" Flask API Model """
from flask import Flask, jsonify
from flask_restful import Resource, Api, request
from sqlalchemy import create_engine
# from to_do_app.input_validation import get_valid_input
from to_do_app import task
__author__ = "Both"

task_collection = task.TaskCollection()

class Task(Resource):
    """Task Resource for Flask API"""

    def get(self):
        """Defines Task GET view"""
        query = task_collection.sort_query('task_id', 'ASC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)

    def post(self):
        """Executes Task POST"""
        # Get data passed by CURL
        data = request.get_json()
        # Add data to database
        # Add task
        task_collection.add_task(
            name=data['name'],
            description=data['description'],
            priority=data['priority'],
        )
        # Set dates
        task_id = task_collection.get_max_task_id()-1
        if 'start_date' in data:
            task_collection.set_date(
                task_id=task_id,
                start_date=data['start_date'],
            )
        if 'due_date' in data:
            task_collection.set_date(
                task_id=task_id,
                due_date=data['due_date'],
            )
        if 'closed_date' in data:
            task_collection.set_date(
                task_id=task_id,
                closed_date=data['closed_date'],
            )
        task_collection.update(
            task_id=task_id,
            status=data['status'],
        )
        return data


class Priority(Resource):
    """Priority Resource for Flask API"""

    def get(self):
        """Defines Priority GET view"""
        query = task_collection.sort_query('priority', 'DESC')
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


class DueDate(Resource):
    """DueDate Resource for Flask API"""

    def get(self):
        """Defines DueDate GET view"""
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
    """Overdue Resource for Flask API"""

    def get(self):
        """Defines Overdue GET view"""
        query = task_collection.filter_overdue_query()
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)


def setup_app(path="sqlite:///task.db"):
    """Sets up and launches Flask app"""
    flask_database = create_engine(path)
    flask_app = Flask(__name__)
    api = Api(flask_app)
    api.add_resource(Task, '/tasks')
    api.add_resource(Priority, '/priority')
    api.add_resource(DueDate, '/due_date')
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
    # api.add_resource(Between, f'/between{dates["start_date"]}' \
    #                           f'&{dates["due_date"]}')
    api.add_resource(Overdue, '/overdue')
    return flask_app, flask_database

def close_app(app_db):
    """Close app and dispose of database connection"""
    app_db.dispose()



if __name__ == "__main__":
    app, database = setup_app()
    app.run(port="5002")
    close_app(database)
