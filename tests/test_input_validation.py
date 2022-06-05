""" Unittests for input validation """
from to_do_app.input_validation import validate_input
__author__ = "Marcus Bakke"


def test_validate_task_name():
    """task_name validation tests"""
    # Test valid task_name
    assert validate_input(dict(task_name='t'*3))
    assert validate_input(dict(task_name='t'*50))
    assert validate_input(dict(task_name='t'*100))
    # Test invalid task_name
    assert not validate_input(dict(task_name='t'*2))
    assert not validate_input(dict(task_name='t'*101))


def test_validate_task_description():
    """task_description validation tests"""
    # Test valid task_description
    assert validate_input(dict(task_description='t'*10))
    assert validate_input(dict(task_description='t'*100))
    assert validate_input(dict(task_description='t'*500))
    # Test invalid task_description
    assert not validate_input(dict(task_description='t'*9))
    assert not validate_input(dict(task_description='t'*501))


def test_validate_task_date():
    """task_start_date/task_due_date validation tests"""
    # Test valid task_start_date/task_due_date
    dates = ['2022-06-06', '2022-6-6', '1001-01-01', '9999-09-09']
    for date in dates:
        assert validate_input(dict(task_start_date=date))
        assert validate_input(dict(task_due_date=date))
    # Test invalid task_start_date/task_due_date
    dates = ['06-06-2022', 'June 6, 2022', '2022/06/06',
             '06/06/2022', '06-06-2022']
    for date in dates:
        assert not validate_input(dict(task_start_date=date))
        assert not validate_input(dict(task_due_date=date))


def test_validate_task_status():
    """task_status validation tests"""
    # Test valid task_status
    assert validate_input(dict(task_status='ACTIVE'))
    assert validate_input(dict(task_status='NOT STARTED'))
    assert validate_input(dict(task_status='COMPLETED'))
    assert validate_input(dict(task_status='DELETED'))
    # Test invalid task_status
    assert not validate_input(dict(task_status='any'))
    assert not validate_input(dict(task_status='thing'))
    assert not validate_input(dict(task_status='else'))


def test_validate_task_priority():
    """task_priority validation tests"""
    # Test valid task_priority
    for priority in range(1, 11):
        assert validate_input(dict(task_priority=str(priority)))
    # Test invalid task_priority
    assert not validate_input(dict(task_priority='0'))
    assert not validate_input(dict(task_priority='11'))
    assert not validate_input(dict(task_priority='any'))
    assert not validate_input(dict(task_priority='thing'))
    assert not validate_input(dict(task_priority='else'))
