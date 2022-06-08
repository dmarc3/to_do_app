# todo

Final assignment for University of Washington Python 320. Homework instructions can be found [here](INSTRUCTIONS.md).

## Authors

- Marcus Bakke
    - List contributions by Marcus...
    - `pyscaffold` and command line interface setup
    - Input validation
- Kathleen Wong
    - List contributions by Kathleen...
    - `SQLAlchemy` database model

## Usage

`to_do_app` is setup using `pyscaffold` and a command line interface. To use the application, use the following commands:

```
usage: todo [-h] [--version] [-v] [-vv] [-a] [-l] [-ssd] [-sdd] [-m] [-d] [-cn] [-cd]

Application to track todo tasks.

optional arguments:
  -h, --help                      show this help message and exit
  --version                       show program's version number and exit
  -v, --verbose                   set loglevel to INFO
  -vv, --very-verbose             set loglevel to DEBUG
  -a, --add_task                  adds a new task to database
  -l, --list_tasks                lists tasks from database
  -ssd, --set_start_date          sets start date for new task
  -sdd, --set_due_date            sets due date for new task
  -m, --mark_complete             marks a task as completed
  -d, --delete_task               deletes a task
  -cn, --change_task_name         changes a tasks name
  -cd, --change_task_description  changes a tasks description
```

Note that more than one command can be executed with one `todo` call. Each command is executed sequentially in the order of appearance in the help output.

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.1.4. For details and usage
information on PyScaffold see https://pyscaffold.org/.
