from datetime import datetime, date
from sqlalchemy import insert
from sqlalchemy import MetaData
import model

today = date.today()


class TaskCollection:
    def __init__(self):
        self.database = model.conn.connect()

    def add_task(self, new_task, task_description, start_date, due_date):
        ins = self.database.insert().values(1,
                                            new_task,
                                            task_description,
                                            start_date,
                                            due_date)
        model.conn.execute(ins)