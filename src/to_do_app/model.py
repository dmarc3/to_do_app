from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Date, Column


Base = declarative_base()


class Task(Base):
    __tablename__ = 'task_detail'
    task_id = Column(Integer, primary_key=True)
    task = Column(String(50))
    task_description = Column(String(100))
    start_date = Column(Date)
    due_date = Column(Date)
    status = Column(String(50))