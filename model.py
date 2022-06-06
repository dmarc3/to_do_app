from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Integer, String, Date, Column, Table


metadata_object = MetaData()

task_detail = Table(
   'task_table',
   metadata_object,
   Column('task_id', Integer, primary_key=True),
   Column('task', String(50)),
   Column('task_description', String(150)),
   Column('start_date', Date),
   Column('due_date', Date)
)

# creating an engine object
engine = create_engine('sqlite:///task.db', echo=True, future=True)

# emitting DDL
metadata_object.create_all(engine)
