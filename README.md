# todo

Final assignment for University of Washington Python 320. Homework instructions can be found [here](INSTRUCTIONS.md).

## Authors

- Marcus Bakke
    - `pyscaffold`, command line interface, and logging setup (`command_line_interface.py` and `logging.py`)
    - Input validation (`input_validation.py`)
    - Main function and integration (`main.py`)
    - Unittests for `command_line_interface.py`, `main.py`,  `input_validation.py` and `model.py`
- Kathleen Wong
    - `SQLAlchemy` database model and interactions (`task.py`)
    - API design and setup (`model.py`)
    - Unittests for `task.py`

## Usage

`to_do_app` is setup using `pyscaffold` and a command line interface. To use the application, use the following commands:

```
usage: todo [-h] [--version] [-s] [-v] [-a [NAME DESCRIPTION PRIORITY ...]] [-ssd [TASK_ID START_DATE ...]] [-sdd [TASK_ID DUE_DATE ...]] [-m [TASK_ID CLOSED_DATE ...]]
            [-d [TASK_ID CLOSED_DATE ...]] [-cn [TASK_ID NAME ...]] [-cd [TASK_ID DESCRIPTION ...]] [-l]

Application to track todo tasks.

optional arguments:
  -h, --help                                                                          show this help message and exit
  --version                                                                           show program's version number and exit
  -s, --silent                                                                        set loglevel to CRITICAL
  -v, --verbose                                                                       set loglevel to DEBUG
  -a [NAME DESCRIPTION PRIORITY ...], --add_task [NAME DESCRIPTION PRIORITY ...]      adds a new task to database
  -ssd [TASK_ID START_DATE ...], --set_start_date [TASK_ID START_DATE ...]            sets start date for new task
  -sdd [TASK_ID DUE_DATE ...], --set_due_date [TASK_ID DUE_DATE ...]                  sets due date for new task
  -m [TASK_ID CLOSED_DATE ...], --mark_complete [TASK_ID CLOSED_DATE ...]             marks a task as completed
  -d [TASK_ID CLOSED_DATE ...], --delete_task [TASK_ID CLOSED_DATE ...]               deletes a task
  -cn [TASK_ID NAME ...], --change_task_name [TASK_ID NAME ...]                       changes a tasks name
  -cd [TASK_ID DESCRIPTION ...], --change_task_description [TASK_ID DESCRIPTION ...]  changes a tasks description
  -l, --list_tasks                                                                    lists tasks from database
```

Note that more than one command can be executed with one `todo` call. Each command is executed sequentially in the order of appearance in the help output. You will need to know the next `task_id` in order to do this as most functions require it as an input. It is helpful to run a `todo -l` (option 1) before doing this.

## Populate the Database
The `populate_database.bat` may be executed to sequentially run a number of `todo` commands to quickly populate the database.

For a windows `CMD` terminal, simply call the `bat` file explicitly:
```shell
populate_database.bat
```
For a linux shell, execute the `bat` file as a script:
```shell
source populate_database.bat
```

## Curl Interface
Once the API is running via executing `model.py`, the user may interact with the API using standard `curl` commands. Below are few examples:

```
curl http://127.0.0.1:5002/tasks
curl http://127.0.0.1:5002/priority
curl http://127.0.0.1:5002/due_date
curl http://127.0.0.1:5002/overdue
curl http://127.0.0.1:5002/tasks -H "Content-Type: application/json" -d '{"name": "Task 1", "description": "Task Description 1", "start_date": "2022-06-15", "due_date": "2022-07-01", "priority": "5", "status": "ACTIVE"}'
```
These will:
1. Execute a `GET` request on the raw database sorted by `task_id`
1. Execute a `GET` request on the raw database sorted by `priority`
1. Execute a `GET` request on all open tasks sorted by `due_date`
1. Execute a `GET` request on all overdue tasks
1. Execute a `POST` request give the payload as a dictionary

Note that we did not finish the `BETWEEN` Flask API resource and therefore left that commented out.

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.1.4. For details and usage
information on PyScaffold see https://pyscaffold.org/.
