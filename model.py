from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert

meta = MetaData()
engine = create_engine('sqlite:///task.db')
Base = declarative_base()

task = Table(
   'tasks', meta,
   Column('task_id', Integer, primary_key=True),
   Column('task', String)
)

meta.create_all(engine)

conn = engine.connect()
ins = task.insert().values(task_id=1, task='Complete Homework')
result = conn.execute(ins)
s = task.select()
result = conn.execute(s)
row = result.fetchone()
for x in row:
   print(x)

# class Task(Base):
#
#     __tablename__ = 'task'
#
#     id = Column(Integer, primary_key=True)
#     task = Column(String)
#
#     def __init__(self, task_id, task):
#         self.task_id = task_id
#         self.task = task
#
#
# meta.create_all(engine)
# conn = engine.connect()
#
# db = Base.metadata.create_all(engine)
# newTask = Task(task_id=1, task='Complete homework')
#
# db.session.add(newTask)
# db.session.commit()