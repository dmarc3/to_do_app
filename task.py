from datetime import datetime, date
from sqlalchemy import insert, select
from sqlalchemy import MetaData
import model

today = date.today()
conn = model.engine.connect()


class TaskCollection:
    def __init__(self):
        self.database = model.task_detail

    def add_task(self, new_task, task_description, start_date, due_date):
        select_max = select(max([self.database.c.task_id]) + 1)
        new_id = conn.execute(select_max)
        ins = insert(self.database).values(task_id=new_id,
                                     task=new_task,
                                     task_description=task_description,
                                     start_date=start_date,
                                     due_date=due_date)
        conn.execute(ins)

    def print_task(self):
        s = select(self.database.c.task_id)
        select_result = conn.execute(s)
        row = select_result.fetchone()
        for x in row:
            print(x)
