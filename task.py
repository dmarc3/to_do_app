from sqlalchemy.orm import Session
from sqlalchemy import func
import model


class TaskCollection:
    def __init__(self, engine):
        self.engine = engine

    def add_task(self, task, task_description):
        session = Session(self.engine)
        max_id = session.query(func.max(model.Task.task_id))
        session.close()
