from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Date, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
engine = create_engine('sqlite:///task.db')
Base = declarative_base()
meta.create_all(engine)
conn = engine.connect()

task = Table(
   'tasks', meta,
   Column('task_id', Integer, primary_key=True),
   Column('task', String),
   Column('task_description', String),
   Column('start_date', Date),
   Column('due_date', Date)
)

meta.create_all(engine)

conn = engine.connect()
# ins = task.insert().values(task_id=1,
#                            task='Complete Homework',
#                            task_description='for Python class',
#                            start_date=datetime(2023,1,1),
#                            due_date=datetime(2023,6,1))
# result = conn.execute(ins)
# s = task.select()
# result = conn.execute(s)
# row = result.fetchone()
# for x in row:
#    print(x)