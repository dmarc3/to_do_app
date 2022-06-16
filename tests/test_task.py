""" Unittests for main functions """
import pytest
from sqlalchemy import text
from to_do_app.task import TaskCollection
__author__ = "Kathleen Wong"

@pytest.fixture(name="tasks")
def fixture_tasks():
    """Initialize in-memory TaskCollection"""
    yield TaskCollection(path='sqlite://')


class TestTaskCollection:
    """Unittest class for TaskCollection"""

    def test_add_task(self, tasks):
        """test add_task method"""
        tasks.add_task(
            name='Test Task 1',
            description='Test description 1...',
            priority='4', )
        assert type(tasks), TaskCollection
        expected = tasks.db.execute((text("""SELECT t.name FROM tasks t
                                             WHERE t.task_id=1""")))
        expected_result = expected.fetchone()
        assert expected_result, 'Test Task 1'
        tasks.add_task(
            name='Test Task 2',
            description='Test description 2...',
            priority='10',
        )
        expected_2 = tasks.db.execute((text("""SELECT t.name FROM tasks t
                                             WHERE t.task_id=2""")))
        expected_result_2 = expected_2.fetchone()
        assert expected_result_2, 'Test Task 2'
        first_task = tasks.sort_query('task_id').fetchone().name
        expected_first = tasks.db.execute((text("""SELECT t.name FROM tasks t
                                                   ORDER BY t.task_id ASC
                                                   LIMIT 1""")))
        expected_result_first = expected_first.fetchone().name
        assert expected_result_first, first_task
        second_task = tasks.sort_query('task_id').fetchone().name
        expected_second = tasks.db.execute((text("""SELECT t.name FROM tasks t
                                                   ORDER BY t.task_id DESC
                                                   LIMIT 1""")))
        expected_result_second = expected_second.fetchone().name
        assert expected_result_second, second_task

    def test_set_start_date(self, tasks):
        """test set_due_date method"""
        tasks.add_task(name='Test Task 1', description='Test description 1...', priority='4', )
        tasks.set_date(1, start_date='2022-05-01', due_date='2022-05-10', closed_date='2022-05-08')
        expected = tasks.db.execute((text("""SELECT t.start_date FROM tasks t
                                                     WHERE t.task_id=1""")))
        expected_result = expected.fetchone().start_date
        assert expected_result, '2022-05-01'

    def test_set_due_date(self, tasks):
        """test set_Start_date method"""
        tasks.add_task(name='Test Task 1', description='Test description 1...', priority='4', )
        tasks.add_task(name='Test Task 2', description='Test description 2...', priority='8', )
        tasks.set_date(1, start_date='2022-05-28', due_date='2022-06-01', closed_date='2022-06-03')
        tasks.set_date(1, due_date='2022-04-01')
        expected = tasks.db.execute((text("""SELECT t.due_date FROM tasks t
                                             WHERE t.task_id=1""")))
        expected_result = expected.fetchone().due_date
        assert expected_result, '2022-06-01'
        overdue_result = tasks.filter_overdue_query('due_date').fetchall()
        expected_overdue = tasks.db.execute((text("""SELECT t.name FROM tasks t
                                                    WHERE t.task_id=1
                                                    AND t.status = 'ACTIVE'
                                                    AND t.start_date<DATE()"""))).fetchone().name
        assert len(expected_overdue), len(overdue_result)
        open_task = tasks.sort_open_query('task_id', 'ASC').fetchone().name
        expected_open = tasks.db.execute((text("""SELECT t.name FROM tasks t
                                                   ORDER BY t.task_id DESC
                                                   LIMIT 1""")))
        expected_result_open = expected_open.fetchone().name
        assert expected_result_open, open_task

    def test_mark_complete(self, tasks):
        """test mark_complete method"""
        tasks.add_task(name='Test Task 1', description='Test description 1...', priority='4', )
        tasks.add_task(name='Test Task 2', description='Test description 2...', priority='8', )
        tasks.add_task(name='Test Task 3', description='Test description 3...', priority='9', )
        tasks.set_date(1, due_date='2022-06-01')
        tasks.set_date(2, due_date='2022-04-01')
        tasks.set_date(3, start_date='2022-06-01')
        tasks.set_date(3, due_date='2022-06-03')
        tasks.update(1, name='Testing Update', description='testing', status='COMPLETED')
        tasks.update(2, closed_date='2022-04-06', status='COMPLETED')
        tasks.update(3, status='COMPLETED')
        closed_check = tasks.filter_closed_between_query('2022-04-05', '2022-04-07').fetchone().name
        expected_closed = tasks.db.execute((text("""SELECT t.name FROM tasks t
                                                   WHERE t.closed_date BETWEEN '2022-04-05' AND '2022-04-06'
                                                   LIMIT 1"""))).fetchone().name
        assert expected_closed, 'Testing Update'
        assert closed_check, 'Testing Update'
        assert closed_check, expected_closed
        print_test = tasks.print_query(tasks.sort_query('task_id'))
        assert print_test, True
