""" Unittests for main functions """
import pytest
from sqlalchemy import text
from to_do_app.task import TaskCollection

@pytest.fixture()
def tasks():
    """Initialize in-memory TaskCollection"""
    yield TaskCollection(path='sqlite://')

class TestTaskCollection:
    """Unittest class for TaskCollection"""

    def test_add_task(self, tasks):
        """test add_task method"""
        tasks.add_task(
            name='Test Task 1',
            description='Test description 1...',
            priority='4',
        )
        tasks.add_task(
            name='Test Task 2',
            description='Test description 2...',
            priority='10',
        )
        out = tasks.sort_query(sort_by='task_id')


    # def test_list_tasks():
    #     """test list_tasks method"""
    #     pass


    # def test_set_start_date():
    #     """test set_Start_date method"""
    #     pass


    # def test_set_due_date():
    #     """test set_due_date method"""
    #     pass


    # def test_mark_complete():
    #     """test mark_complete method"""
    #     pass


    # def test_delete_task():
    #     """test delete_task method"""
    #     pass


    # def test_change_task_name():
    #     """test change_task_name method"""
    #     pass


    # def test_change_task_description():
    #     """test change_task_description method"""
    #     pass
