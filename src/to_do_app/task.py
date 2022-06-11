from sqlalchemy import create_engine, text, exc
import validation


class TaskCollection:
    def __init__(self):
        self.engine = create_engine('sqlite:///task.db', future=True)
        self.db = self.engine.connect()
        try:
            self.db.execute(text('SELECT * FROM tasks'))
        except exc.OperationalError:
            self.db.execute(text(
                """CREATE TABLE tasks(
                   task_id INTEGER NOT NULL,
                   task VARCHAR,
                   task_description VARCHAR,
                   start_date date,
                   due_date date,
                   status VARCHAR,
                   priority VARCHAR,
                   PRIMARY KEY (task_id))"""))

    def add_task(self, task, task_description):
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
            self.db.execute(text(f"""INSERT INTO tasks(task_id, task, task_description) VALUES({max_id}, '{task}', 
            '{task_description}')"""))
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
            query = self.db.execute(text(f"""SELECT*
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
                      query_row.task_description, 'start date:', query_row.start_date, 'due date:',
                      query_row.due_date, 'status:', query_row.status, 'priority:', query_row.priority)
        except TypeError:
            print('None')

    def set_date(self, column_name):
        update_id = validation.task_id_response('set', column_name)
        while True:
            query = self.db.execute(text(f"""SELECT* FROM tasks t WHERE t.task_id={update_id}"""))
            query_results = query.fetchone()
            try:
                if len(query_results) > 0:
                    new_date = validation.date_response(column_name)
                    self.db.execute(text(f"""UPDATE tasks
                                             SET {column_name}='{new_date}'
                                             WHERE task_id={update_id}"""))
                    self.db.commit()
                    break
            except TypeError:
                print('This is not a legitimate task id! Try again.')
                update_id = validation.task_id_response(column_name)

    def update_status(self, new_status):
        update_id = validation.task_id_response('update', 'status')
        while True:
            query = self.db.execute(text(f"""SELECT* FROM tasks t WHERE t.task_id={update_id}"""))
            query_results = query.fetchone()
            try:
                if len(query_results) > 0:
                    self.db.execute(text(f"""UPDATE tasks
                                             SET status='{new_status}'
                                             WHERE task_id={update_id}"""))
                    self.db.commit()
                    break
            except TypeError:
                print('This is not a legitimate task id! Try again.')
                update_id = validation.task_id_response('status')

    def update_data(self, column_name):
        update_id = validation.task_id_response('set', column_name)
        while True:
            query = self.db.execute(text(f"""SELECT* FROM tasks t WHERE t.task_id={update_id}"""))
            query_results = query.fetchone()
            try:
                if len(query_results) > 0:
                    if column_name == 'priority':
                        new_answer = validation.priority_response(update_id)
                        self.db.execute(text(f"""UPDATE tasks
                                                 SET {column_name}='{new_answer}'
                                                 WHERE task_id={update_id}"""))
                        self.db.commit()
                        break
                    else:
                        new_answer = input(f'What would you like to update the {column_name} to?')
                        self.db.execute(text(f"""UPDATE tasks
                                                 SET {column_name}='{new_answer}'
                                                 WHERE task_id={update_id}"""))
                        self.db.commit()
                        break
            except TypeError:
                print('This is not a legitimate task id! Try again.')
                update_id = validation.task_id_response(column_name)
