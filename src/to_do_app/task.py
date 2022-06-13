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
                   priority INTEGER,
                   closed_date date,
                   PRIMARY KEY (task_id))"""))

    def add_task(self, name: str, description: str, priority: str):
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

    def sort_query(self, sort_by, direction='ASC'):
        query = self.db.execute(text(f"""SELECT*
                                         FROM tasks t
                                         ORDER BY t.{sort_by} {direction}
                                     """))
        return self.print_query(query)

    def sort_open_query(self, sort_by: str, direction='ASC'):
        query = self.db.execute(text(f"""SELECT*
                                         FROM tasks t
                                         WHERE t.status='ACTIVE'
                                         ORDER BY t.{sort_by} {direction}"""))
        return self.print_query(query)

    def filter_closed_between_query(self, start, end):
        query = self.db.execute(text(f"""SELECT*
                                         FROM tasks t
                                         WHERE (t.status='COMPLETED' OR t.status='DELETED')
                                         AND t.closed_date BETWEEN '{start}' AND '{end}'"""))
        return self.print_query(query)

    def filter_overdue_query(self, filter_by='due_date'):
        query = self.db.execute(text(f"""SELECT*
                                         FROM tasks t
                                         WHERE t.{filter_by}<DATE()"""))
        return self.print_query(query)

    def print_query(self, query: list):
        # Build header
        header = list(query.keys())
        header = [head.replace('_', ' ').upper() for head in header]
        widths = [len(head)+2 for head in header]
        # Calculate maximum column widths
        query = query.all()
        for row in query:
            for ind, value in enumerate(row):
                value = str(value)
                if len(value)+2 > widths[ind]:
                    widths[ind] = len(value)+2
        # Print results
        out = '\n'
        for ind, head in enumerate(header):
            out += head.ljust(widths[ind])
        out += '\n'
        out += '-'*(len(out)-2)+'\n'
        for row in query:
            for ind, value in enumerate(row):
                value = str(value)
                out += value.ljust(widths[ind])
            out += '\n'
        out += '\n'
        print(out)

    def set_date(self, task_id: int, start_date=None, due_date=None, closed_date=None):
        dates = dict(
            start_date=start_date,
            due_date=due_date,
            closed_date=closed_date,
        )
        for key, value in dates.items():
            if value:
                self.db.execute(text(f"""UPDATE tasks
                                     SET {key}='{value}'
                                     WHERE task_id={task_id}"""))
            self.db.commit()
            break

    def update(self, task_id: int, name=None, description=None, status=None, closed_date=None):
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
            if status in ['COMPLETED', 'DELETED']:
                if not closed_date:
                    closed_date = datetime.today().strftime('%Y-%m-%d')
                self.db.execute(text(f"""UPDATE tasks
                                        SET closed_date='{closed_date}'
                                        WHERE task_id={task_id}"""))
            self.db.commit()

