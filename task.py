from datetime import datetime, date
from sqlalchemy import insert
from sqlalchemy import MetaData
import model

today = date.today()


class TaskCollection:
    def __init__(self):
        self.database = model.task_detail

    def add_task(self, new_id, new_task, task_description, start_date, due_date):
        insert(self.database).values(task_id=new_id,
                                     task=new_task,
                                     task_description=task_description,
                                     start_date=start_date,
                                     due_date=due_date)
