import logging
from datetime import datetime, timedelta
from sqlalchemy import create_engine, text, exc
# import to_do_app.validation as validation

__author__ = 'Kathleen Wong'
_logger = logging.getLogger(__name__)

class TaskCollection:
    """ Class to interact with SQL database """

    def __init__(self):
        """ Initialize TaskCollection """
        self.engine = create_engine('sqlite:///task.db', future=True)
        self.db = self.engine.connect()
        _logger.debug('Connection to sqlite:///task.db established.')
        try:
            self.db.execute(text('SELECT * FROM tasks'))
        except exc.OperationalError:
            _logger.debug('Database empty. Initializing database.')
            self.db.execute(text(
                """CREATE TABLE tasks(
                   task_id INTEGER NOT NULL,
                   name VARCHAR,
                   description VARCHAR,
                   start_date date,
                   due_date date,
                   status VARCHAR,
                   priority VARCHAR,
                   PRIMARY KEY (task_id))"""))

    def add_task(self, name, description, priority):
        try:
            max_query = self.db.execute(text("""SELECT
                                            task_id
                                            FROM tasks
                                            ORDER BY task_id DESC
                                            LIMIT 1"""))
            max_result = max_query.fetchone()
            max_id = max_result[0] + 1
        except TypeError:
            max_id = 1
        finally:
            self.db.execute(text(f"""INSERT INTO tasks(task_id, name,
                                  description, start_date, due_date, status,
                                  priority) VALUES({max_id}, "{name}",
                                  "{description}",
                                  '{datetime.today().strftime('%Y-%m-%d')}',
                                  '{(datetime.today()+timedelta(weeks=1)).strftime('%Y-%m-%d')}',
                                   'ACTIVE', '{priority}')"""))
            self.db.commit()

    def print_tasks(self, column_name):
        if column_name == 'completed':
            date_type = input('Which date do you want to search by? ')
            first_date = validation.date_response(date_type)
            second_date = validation.date_response(date_type)
            query = self.db.execute(text(f"""SELECT*
                                             FROM tasks t
                                             WHERE t.status=1
                                             AND t.{date_type} BETWEEN '{first_date}' AND '{second_date}'"""))
        elif column_name == 'overdue':
            query = self.db.execute(text("""SELECT*
                                            FROM tasks t
                                            WHERE t.status=0
                                            AND t.due_date<DATE()"""))
        else:
            query = self.db.execute(text(f"""SELECT*
                                            FROM tasks t
                                            ORDER BY t.{column_name}"""))
        query_results = query.fetchall()
        print('The following tasks are in the database:')
        try:
            for query_row in query_results:
                print('task_id:', query_row.task_id, 'task:', query_row.task, 'task description:',
                      query_row.description, 'start date:', query_row.start_date, 'due date:',
                      query_row.due_date, 'status:', query_row.status, 'priority:', query_row.priority)
        except TypeError:
            print('None')

    def set_date(self, task_id, start_date=None, due_date=None):
        if start_date:
            self.db.execute(text(f"""UPDATE tasks
                                     SET start_date='{start_date}'
                                     WHERE task_id={task_id}"""))
            self.db.commit()
        if due_date:
            self.db.execute(text(f"""UPDATE tasks
                                     SET due_date='{due_date}'
                                     WHERE task_id={task_id}"""))
            self.db.commit()

    def update(self, task_id, name=None, description=None, status=None):
        if name:
            self.db.execute(text(f"""UPDATE tasks
                                     SET name='{name}'
                                     WHERE task_id={task_id}"""))
            self.db.commit()
        if description:
            self.db.execute(text(f"""UPDATE tasks
                                     SET description='{description}'
                                     WHERE task_id={task_id}"""))
            self.db.commit()
        if status:
            self.db.execute(text(f"""UPDATE tasks
                                     SET status='{status}'
                                     WHERE task_id={task_id}"""))
            self.db.commit()

