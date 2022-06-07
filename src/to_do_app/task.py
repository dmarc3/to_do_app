from datetime import datetime, date
from sqlalchemy import insert, select
from sqlalchemy import MetaData
import sqlite3
import model

today = date.today()
conn = model.engine.connect()


class TaskCollection:
    def __init__(self):
        self.database = model.task_detail

    def add_task(self, new_task, task_description):#, start_date, due_date):
        select_max = conn.execute(select(max([self.database.c.task_id])))
        id_results = select_max.fetchone()
        try:
            new_id = id_results.task_id + 1
        except AttributeError:
            new_id = 1
        # try:
        #     new_id = id_results.task_id + 1
        # except TypeError:
        #     new_id = 1
        ins = insert(self.database).values(task_id=new_id,
                                           task=new_task,
                                           task_description=task_description,
                                           start_date=None,
                                           due_date=None
                                             # start_date=start_date,
                                             # due_date=due_date
                                                   )
        conn.execute(ins)
        conn.commit()

    def print_task(self):
        s = select(self.database.c.task_id, self.database.c.task)
        select_result = conn.execute(s)
        row = select_result.fetchall()
        print('The following tasks have been added:')
        if len(row)>0:
            for x in row:
                print(x.task_id, x.task)
        else:
            print('None')