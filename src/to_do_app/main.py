""" Main to_do_app functions. These are tied to CLI. """
import logging
from to_do_app.input_validation import get_valid_input

__author__ = 'Marcus Bakke'
_logger = logging.getLogger(__name__)

def add_task(tasks) -> bool:
    """adds a new task to database"""
    # Get task name
    new_task = get_valid_input(
        'name',
        'REQUEST: What task would you like to add?\nNAME: ',
        )
    # Get task description
    new_task = get_valid_input(
        'description',
        'REQUEST: Provide a brief description to the task:\nDESCRIPTION: ',
        new_task,
    )
    # Get priority
    new_task = get_valid_input(
        'priority',
        'REQUEST: Provide a priority level (1-10):\nPRIORITY: ',
        new_task,
    )
    # Execute command
    tasks.add_task(**new_task)
    return True


def list_tasks(tasks) -> bool:
    """lists tasks from database"""
    _logger.info('list_task')
    return True


def set_start_date(tasks) -> bool:
    """sets start date for new task"""
    task = get_valid_input(
        'task_id',
        'REQUEST: Provide task_id for task you would like ' \
        'to set start date:\nTASK ID: ',
    )
    task = get_valid_input(
        'start_date',
        'REQUEST: Provide a start date (YYYY-MM-DD):\nSTART DATE: ',
        task,
    )
    # Execute command
    tasks.set_date(**task)
    return True


def set_due_date(tasks) -> bool:
    """sets due date for new task"""
    task = get_valid_input(
        'task_id',
        'REQUEST: Provide task_id for task you would like ' \
        'to set due date:\nTASK ID: ',
    )
    task = get_valid_input(
        'due_date',
        'REQUEST: Provide a due date (YYYY-MM-DD):\nDUE DATE: ',
        task,
    )
    # Execute command
    tasks.set_date(**task)
    return True


def mark_complete(tasks) -> bool:
    """marks a task as completed"""
    task = get_valid_input(
        'task_id',
        'REQUEST: Provide task_id for task you would like ' \
        'to set mark complete:\nTASK ID: ',
    )
    task['status'] = 'COMPLETED'
    # Execute command
    tasks.update(**task)
    return True


def delete_task(tasks) -> bool:
    """deletes a task"""
    task = get_valid_input(
        'task_id',
        'REQUEST: Provide task_id for task you would like ' \
        'to delete:\nTASK ID: ',
    )
    task['status'] = 'DELETED'
    # Execute command
    tasks.update(**task)
    return True


def change_task_name(tasks) -> bool:
    """changes a tasks name"""
    task = get_valid_input(
        'task_id',
        'REQUEST: Provide task_id for task you would like ' \
        'to change the name of:\nTASK ID: ',
    )
    task = get_valid_input(
        'name',
        'REQUEST: Provide a new task name:\nNAME: ',
        task,
    )
    # Execute command
    tasks.update(**task)
    return True


def change_task_description(tasks) -> bool:
    """changes a tasks description"""
    task = get_valid_input(
        'task_id',
        'REQUEST: Provide task_id for task you would like ' \
        'to change the description of:\nTASK ID: ',
    )
    task = get_valid_input(
        'description',
        'REQUEST: Provide a new task description:\nDESCRIPTION: ',
        task,
    )
    # Execute command
    tasks.update(**task)
    return True
