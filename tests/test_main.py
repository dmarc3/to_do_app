""" Unittests for main functions """
from datetime import datetime
from unittest.mock import Mock, patch
from to_do_app import main
from to_do_app import task
__author__ = "Marcus Bakke"


def mock_with_args(inp, task_func, func, expected):
    """Mock function with arguments"""
    tasks = task.TaskCollection()
    func_mock = Mock()
    with patch(task_func, func_mock):
        result = func(tasks, inp)
        assert result
        assert func_mock.call_args.kwargs == expected


def mock_no_args(inp, task_func, func, expected):
    """Mock function with no arguments"""
    tasks = task.TaskCollection()
    func_mock = Mock()
    with patch(task_func, func_mock):
        input_mock = Mock()
        input_mock.side_effect = inp
        with patch('builtins.input', input_mock):
            result = func(tasks, [])
            assert result
            assert func_mock.call_args.kwargs == expected


def mock_query_funcs(inp, task_func, func, expected):
    """Mock query functions"""
    tasks = task.TaskCollection()
    print_mock = Mock()
    with patch('to_do_app.task.TaskCollection.print_query', print_mock):
        func_mock = Mock()
        with patch(task_func, func_mock):
            input_mock = Mock()
            input_mock.side_effect = inp
            with patch('builtins.input', input_mock):
                result = func(tasks, [])
                assert result
                assert func_mock.call_args.kwargs == expected


def test_add_task_with_args():
    """test add_task with arguments supplied"""
    inp = ['Task 1', 'Task 1 description', 2]
    task_func = 'to_do_app.task.TaskCollection.add_task'
    func = main.add_task
    expected = dict(name=inp[0], description=inp[1], priority=inp[2])
    mock_with_args(inp, task_func, func, expected)


def test_add_task_no_args():
    """test add_task with no arguments supplied"""
    inp = ['Task 1', 'Task 1 description', 2]
    task_func = 'to_do_app.task.TaskCollection.add_task'
    func = main.add_task
    expected = dict(name=inp[0], description=inp[1], priority=inp[2])
    mock_no_args(inp, task_func, func, expected)


def test_list_tasks_1():
    """test list_tasks option 1 method"""
    inp = ['0', '1']
    task_func = 'to_do_app.task.TaskCollection.sort_query'
    func = main.list_tasks
    expected = dict(sort_by='task_id')
    mock_query_funcs(inp, task_func, func, expected)


def test_list_tasks_2():
    """test list_tasks option 2 method"""
    inp = '2'
    task_func = 'to_do_app.task.TaskCollection.sort_query'
    func = main.list_tasks
    expected = dict(sort_by='priority', direction='DESC')
    mock_query_funcs(inp, task_func, func, expected)


def test_list_tasks_3():
    """test list_tasks option 3 method"""
    inp = '3'
    task_func = 'to_do_app.task.TaskCollection.sort_open_query'
    func = main.list_tasks
    expected = dict(sort_by='due_date')
    mock_query_funcs(inp, task_func, func, expected)


def test_list_tasks_4():
    """test list_tasks option 4 method"""
    inp = ['4', '2022-06-10', '2022-06-19']
    task_func = 'to_do_app.task.TaskCollection.filter_closed_between_query'
    func = main.list_tasks
    expected = dict(start=inp[1], end=inp[2])
    mock_query_funcs(inp, task_func, func, expected)


def test_list_tasks_5():
    """test list_tasks option 5 method"""
    inp = '5'
    task_func = 'to_do_app.task.TaskCollection.filter_overdue_query'
    func = main.list_tasks
    expected = {}
    mock_query_funcs(inp, task_func, func, expected)


def test_set_start_date_with_args():
    """test set_start_date with args supplied"""
    inp = [1, '2022-06-13']
    task_func = 'to_do_app.task.TaskCollection.set_date'
    func = main.set_start_date
    expected = dict(task_id=inp[0], start_date=inp[1])
    mock_with_args(inp, task_func, func, expected)


def test_set_start_date_no_args():
    """test set_start_date with no args supplied"""
    inp = [1, '2022-06-13']
    task_func = 'to_do_app.task.TaskCollection.set_date'
    func = main.set_start_date
    expected = dict(task_id=inp[0], start_date=inp[1])
    mock_no_args(inp, task_func, func, expected)


def test_set_due_date_with_args():
    """test set_due_date with args supplied"""
    inp = [1, '2022-06-13']
    task_func = 'to_do_app.task.TaskCollection.set_date'
    func = main.set_due_date
    expected = dict(task_id=inp[0], due_date=inp[1])
    mock_with_args(inp, task_func, func, expected)


def test_set_due_date_no_args():
    """test set_due_date with no args supplied"""
    inp = [1, '2022-06-13']
    task_func = 'to_do_app.task.TaskCollection.set_date'
    func = main.set_due_date
    expected = dict(task_id=inp[0], due_date=inp[1])
    mock_no_args(inp, task_func, func, expected)


def test_mark_complete_with_args():
    """test mark_complete with args supplied"""
    inp = [[1], [1, '2022-06-13']]
    task_func = 'to_do_app.task.TaskCollection.update'
    func = main.mark_complete
    expected = [dict(task_id=1, status='COMPLETED'),
                dict(task_id=1, closed_date='2022-06-13', status='COMPLETED')]
    mock_with_args(inp[0], task_func, func, expected[0])
    mock_with_args(inp[1], task_func, func, expected[1])


def test_mark_complete_no_args():
    """test mark_complete with no args"""
    inp = [[1, ''], [1, '2022-06-13']]
    task_func = 'to_do_app.task.TaskCollection.update'
    expected = [dict(task_id=1,
                     closed_date=datetime.today().strftime('%Y-%m-%d'),
                     status='COMPLETED'),
                dict(task_id=1,
                     closed_date='2022-06-13',
                     status='COMPLETED')]
    func = main.mark_complete
    mock_no_args(inp[0], task_func, func, expected[0])
    mock_no_args(inp[1], task_func, func, expected[1])


def test_delete_task_with_args():
    """test delete_task with args supplied"""
    inp = [1]
    task_func = 'to_do_app.task.TaskCollection.update'
    func = main.delete_task
    expected = dict(task_id=inp[0], status='DELETED')
    mock_with_args(inp, task_func, func, expected)


def test_delete_task_no_args():
    """test delete_task with no args supplied"""
    inp = [1]
    task_func = 'to_do_app.task.TaskCollection.update'
    func = main.delete_task
    expected = dict(task_id=inp[0], status='DELETED')
    mock_no_args(inp, task_func, func, expected)


def test_change_task_name_with_args():
    """test change_task_name with args supplied"""
    inp = [1, 'Task Name']
    task_func = 'to_do_app.task.TaskCollection.update'
    func = main.change_task_name
    expected = dict(task_id=inp[0], name=inp[1])
    mock_with_args(inp, task_func, func, expected)


def test_change_task_name_no_args():
    """test change_task_name with no args supplied"""
    inp = [1, 'Task Name']
    task_func = 'to_do_app.task.TaskCollection.update'
    func = main.change_task_name
    expected = dict(task_id=inp[0], name=inp[1])
    mock_no_args(inp, task_func, func, expected)


def test_change_task_description_with_args():
    """test change_task_description with args supplied"""
    inp = [1, 'Task Description']
    task_func = 'to_do_app.task.TaskCollection.update'
    func = main.change_task_description
    expected = dict(task_id=inp[0], description=inp[1])
    mock_with_args(inp, task_func, func, expected)


def test_change_task_description_no_args():
    """test change_task_description with no args supplied"""
    inp = [1, 'Task Description']
    task_func = 'to_do_app.task.TaskCollection.update'
    func = main.change_task_description
    expected = dict(task_id=inp[0], description=inp[1])
    mock_no_args(inp, task_func, func, expected)
