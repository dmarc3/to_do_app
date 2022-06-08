""" Main to_do_app functions. These are tied to CLI. """
import logging

_logger = logging.getLogger(__name__)

def add_task() -> bool:
    """adds a new task to database"""
    _logger.info('add_task')
    return True


def list_tasks() -> bool:
    """lists tasks from database"""
    _logger.info('list_task')
    return True


def set_start_date() -> bool:
    """sets start date for new task"""
    _logger.info('set_start_date')
    return True


def set_due_date() -> bool:
    """sets due date for new task"""
    _logger.info('set_due_date')
    return True


def mark_complete() -> bool:
    """marks a task as completed"""
    _logger.info('mark_complete')
    return True


def delete_task() -> bool:
    """deletes a task"""
    _logger.info('delete_task')
    return True


def change_task_name() -> bool:
    """changes a tasks name"""
    _logger.info('change_task_name')
    return True


def change_task_description() -> bool:
    """changes a tasks description"""
    _logger.info('change_task_description')
    return True
