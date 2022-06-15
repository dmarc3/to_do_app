""" Unittests for API model """
import pytest
from flask import Flask, jsonify
from to_do_app.task import TaskCollection


@pytest.fixture()
def app():
    """Initialize test app"""
    test_app = Flask(__name__)
    yield test_app.test_client()

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

    def test_task(self, app, tasks):
        """test add_task method"""
        import pdb; pdb.set_trace()
        print(app)
        print(tasks)