""" Unittests for API model """
import pytest
from flask import Flask, jsonify
from flask_restful import Resource, Api
from to_do_app.task import TaskCollection
from to_do_app.task_api import Task


@pytest.fixture()
def client():
    """Initialize test app"""
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Task, '/tasks')  # task 1-sorted by task id
    yield app.test_client()

@pytest.fixture()
def tasks():
    """Initialize in-memory TaskCollection"""
    tasks = TaskCollection(path='sqlite://')
    for ind in range(0, 4):
        inputs = dict(
            name='Task '+str(ind),
            description='Task Description '+str(ind),
            priority=str(ind),
        )
        tasks.add_task(**inputs)
    yield tasks


class TestModelGet:
    """Unittest class for model GET resources"""

    def test_task(self, tasks, client):
        """test add_task method"""
        import pdb; pdb.set_trace()
        print(client)
        print(tasks)