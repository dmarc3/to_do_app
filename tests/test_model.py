""" Unittests for API model """
from unittest.mock import Mock, patch
import pytest
from flask import Flask
from flask_restful import Resource, Api
from to_do_app.task import TaskCollection
from to_do_app.task_api import run_app, close_app, Task, Priority


@pytest.fixture()
def client():
    """Initialize test app"""
    collection_mock = Mock()
    collection_mock.return_value = TaskCollection(path='sqlite://')
    with patch('to_do_app.task_api.task.TaskCollection', collection_mock):
        app, db = run_app(path='sqlite://')
    yield app.test_client()
    close_app(db)

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

def api_get(client, url: str):
    """Method to call get function with appropriate URL"""
    return client.get(url)

class TestModelGet:
    """Unittest class for model GET resources"""

    def test_task(self, tasks, client):
        """test add_task method"""
        response = api_get(client, '/tasks')
        import pdb; pdb.set_trace()
        assert response.status_code == 200

    # def test_priority(self, tasks, client):
    #     """test add_task method"""
    #     response = api_get(client, '/priority')
    #     import pdb; pdb.set_trace()
    #     assert response.status_code == 200
