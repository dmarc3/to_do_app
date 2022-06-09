from sqlalchemy.orm import Session
from sqlalchemy import func, insert, update, select
from datetime import datetime
import model
import validation


class TaskCollection:
    def __init__(self, engine):
        self.engine = engine

    def add_task(self, task, task_description):
        session = Session(self.engine)
        max_id = session.query(func.max(model.Task.task_id))
        max_id = session.execute(max_id)
        try:
            max_id = max_id.fetchone + 1
        except TypeError:
            max_id = 1
        ins = insert(model.Task).values(task_id=max_id,
                                        task=task,
                                        task_description=task_description,
                                        start_date=None,
                                        due_date=None,
                                        status='Work in Progress')
        session.execute(ins)
        session.commit()
        session.close()

    def print_tasks(self):
        session = Session(self.engine)
        search_tasks = session.query(model.Task).all()
        print('The following tasks are included:')
        if len(search_tasks) > 0:
            for x in search_tasks:
                print('task_id:', x.task_id,
                      'task:', x.task,
                      'task_description:', x.task_description,
                      'start_date:', x.start_date,
                      'due_date:', x.due_date,
                      'status:', x.status)
        else:
            print('None')
        session.close()

    def set_date(self, column_name):
        session = Session(self.engine)
        TaskCollection.print_tasks(self)
        task_id = validation.task_id_response(column_name)
        while True:
            select_query = session.query(model.Task).filter_by(task_id=task_id)
            select_results = session.execute(select_query)
            select_result = select_results.first()[0]
            task_id = select_result.task_id
            if task_id is None:
                print(f'task id {task_id} does not exist! Try again.')
                task_id = validation.task_id_response(column_name)
            else:
                break
        month_date = validation.month_response(column_name)
        date_date = validation.day_response(column_name)
        year_date = validation.year_response(column_name)
        session.query(model.Task).filter(model.Task.task_id == task_id).update({column_name:
                                                                        datetime(year_date, month_date, date_date)})
        session.commit()
        session.close()

    def update_status(self):
        session = Session(self.engine)
        TaskCollection.print_tasks(self)
        task_id = validation.task_id_response('status')
        while True:
            select_query = session.query(model.Task).filter_by(task_id=task_id)
            select_results = session.execute(select_query)
            select_result = select_results.first()[0]
            task_id = select_result.task_id
            if task_id is None:
                print(f'task id {task_id} does not exist! Try again.')
                task_id = validation.task_id_response('status')
            else:
                break
        session.query(model.Task).filter(model.Task.task_id == task_id).update({'status': 'Completed'})
        session.commit()
        session.close()