""" Unittests for input validation """
from unittest.mock import Mock, patch
from to_do_app.input_validation import validate_input, get_valid_input
__author__ = "Marcus Bakke"


def test_validate_task_id():
    """task_id validation tests"""
    # Test valid task_id
    assert validate_input(dict(task_id=1))
    assert validate_input(dict(task_id=0))
    assert validate_input(dict(task_id=10000))
    assert validate_input(dict(task_id='2'))
    # Test invalid task_id
    assert not validate_input(dict(task_id='some non-numeric string'))
    assert not validate_input(dict(task_id=[1]))


def test_validate_name():
    """name validation tests"""
    # Test valid name
    assert validate_input(dict(name='t'*3))
    assert validate_input(dict(name='t'*50))
    assert validate_input(dict(name='t'*100))
    # Test invalid name
    assert not validate_input(dict(name='t'*2))
    assert not validate_input(dict(name='t'*101))


def test_validate_description():
    """description validation tests"""
    # Test valid description
    assert validate_input(dict(description='t'*10))
    assert validate_input(dict(description='t'*100))
    assert validate_input(dict(description='t'*500))
    # Test invalid description
    assert not validate_input(dict(description='t'*9))
    assert not validate_input(dict(description='t'*501))


def test_validate_date():
    """start_date/due_date/closed_date validation tests"""
    # Test valid start_date/due_date/closed_date
    dates = ['2022-06-06', '2022-6-6', '1001-01-01', '9999-09-09']
    for date in dates:
        assert validate_input(dict(start_date=date))
        assert validate_input(dict(due_date=date))
        assert validate_input(dict(closed_date=date))
    # closed_date is assigned today's date
    assert validate_input(dict(closed_date=[]))
    # Test invalid start_date/due_date
    dates = ['06-06-2022', 'June 6, 2022', '2022/06/06',
             '06/06/2022', '06-06-2022']
    for date in dates:
        assert not validate_input(dict(start_date=date))
        assert not validate_input(dict(due_date=date))
        assert not validate_input(dict(closed_date=date))


def test_validate_status():
    """status validation tests"""
    # Test valid status
    assert validate_input(dict(status='ACTIVE'))
    assert validate_input(dict(status='COMPLETED'))
    assert validate_input(dict(status='DELETED'))
    # Test invalid status
    assert not validate_input(dict(status='any'))
    assert not validate_input(dict(status='thing'))
    assert not validate_input(dict(status='else'))


def test_validate_priority():
    """priority validation tests"""
    # Test valid priority
    for priority in range(1, 11):
        assert validate_input(dict(priority=priority))
    # Test invalid priority
    assert not validate_input(dict(priority='0'))
    assert not validate_input(dict(priority='11'))
    assert not validate_input(dict(priority='any'))
    assert not validate_input(dict(priority='thing'))
    assert not validate_input(dict(priority='else'))


def test_get_valid_input():
    """test get_valid_input"""
    input_mock = Mock()
    input_mock.side_effect = ['INVALID', 'ACTIVE']
    with patch('builtins.input', input_mock) as mock_input:
        out = get_valid_input('status', 'PROMPT')
        assert out == dict(status='ACTIVE')
        mock_input.assert_called()

    input_mock = Mock()
    input_mock.side_effect = ['INVALID', 'ACTIVE']
    with patch('builtins.input', input_mock) as mock_input:
        out = get_valid_input('status', 'PROMPT', inputs=dict(task_id=1))
        assert out == dict(status='ACTIVE', task_id=1)
        mock_input.assert_called()
