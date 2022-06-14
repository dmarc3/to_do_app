""" Main to_do_app functions. These are tied to CLI. """
import logging
from to_do_app.input_validation import get_valid_input

__author__ = 'Marcus Bakke'
_logger = logging.getLogger(__name__)

def add_task(tasks, arguments: list) -> bool:
    """adds a new task to database"""
    if not arguments:
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
    else:
        new_task = dict(
            name=arguments[0],
            description=arguments[1],
            priority=arguments[2],
        )
    # Execute command
    tasks.add_task(**new_task)
    return True


def list_tasks(tasks, *_) -> bool:
    """lists tasks from database"""
    while True:
        option = int(input("""
1. List all tasks sorted by task number
2. List all tasks sorted by priority
3. List all open tasks sorted by due date
4. List all closed tasks between specified dates
5. List all overdue tasks

Please enter your choice: """).strip())
        if option in [1, 2, 3, 4, 5]:
            break
        _logger.info('%s is an invalid option.', option)
    if option == 1:
        inputs = dict(sort_by='task_id')
        func = tasks.sort_query
    elif option == 2:
        inputs = dict(sort_by='priority', direction='DESC')
        func = tasks.sort_query
    elif option == 3:
        inputs = dict(sort_by='due_date')
        func = tasks.sort_open_query
    elif option == 4:
        # Get start
        dates = get_valid_input(
            'start_date',
            'REQUEST: What date would you like to start from (YYYY-MM-DD)?\nDATE: ',
            )
        # Get end
        dates = get_valid_input(
            'due_date',
            'REQUEST: What date would you like to end at (YYYY-MM-DD)?\nDATE: ',
            dates,
        )
        inputs = dict(start=dates['start_date'], end=dates['due_date'])
        func = tasks.filter_closed_between_query
    else:
        inputs = {}
        func = tasks.filter_overdue_query
    # Execute query and print
    print(func(**inputs))

    return True


def set_start_date(tasks, arguments: list) -> bool:
    """sets start date for new task"""
    if not arguments:
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
    else:
        task = dict(
            task_id=arguments[0],
            start_date=arguments[1],
        )
    # Execute command
    tasks.set_date(**task)
    return True


def set_due_date(tasks, arguments: list) -> bool:
    """sets due date for new task"""
    if not arguments:
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
    else:
        task = dict(
            task_id=arguments[0],
            due_date=arguments[1],
        )
    # Execute command
    tasks.set_date(**task)
    return True


def mark_complete(tasks, arguments: list) -> bool:
    """marks a task as completed"""
    if not arguments:
        task = get_valid_input(
            'task_id',
            'REQUEST: Provide task_id for task you would like ' \
            'to set mark complete:\nTASK ID: ',
        )
        task = get_valid_input(
            'closed_date',
            'REQUEST: Provide date the task was closed on (YYYY-MM-DD)'\
            '(Blank to use todays date):\nCLOSED DATE: ',
            task,
        )
        task['status'] = 'COMPLETED'
    else:
        task = dict(
            task_id=arguments[0],
            status='COMPLETED',
        )
        if len(arguments) == 2:
            task['closed_date'] = arguments[1]
    # Execute command
    tasks.update(**task)
    return True


def delete_task(tasks, arguments: list) -> bool:
    """deletes a task"""
    if not arguments:
        task = get_valid_input(
            'task_id',
            'REQUEST: Provide task_id for task you would like ' \
            'to delete:\nTASK ID: ',
        )
        task['status'] = 'DELETED'
    else:
        task = dict(
            task_id=arguments[0],
            status='DELETED',
        )
    # Execute command
    tasks.update(**task)
    return True


def change_task_name(tasks, arguments: list) -> bool:
    """changes a tasks name"""
    if not arguments:
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
    else:
        task = dict(
            task_id=arguments[0],
            name=arguments[1],
        )
    # Execute command
    tasks.update(**task)
    return True


def change_task_description(tasks, arguments: list) -> bool:
    """changes a tasks description"""
    if not arguments:
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
    else:
        task = dict(
            task_id=arguments[0],
            description=arguments[1],
        )
    # Execute command
    tasks.update(**task)
    return True
