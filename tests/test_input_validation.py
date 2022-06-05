import pytest

from to_do_app.input_validation import validate_input
__author__ = "Marcus Bakke"


def test_validate_task_name():
    """task_name validation tests"""
    # Test valid task_names
    assert validate_input(dict(task_name='Test task'))

