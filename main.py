import model
import task
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import session
from datetime import datetime
from sqlalchemy import select

# while True:
#     print(
#         'A: Add task'
#     )



task_collection = task.TaskCollection()

try:
    max_id = select(max([task_collection.database.c.task_id]) + 1)
except:
    max_id = 1

ins = task_collection.database.insert().values(max_id=1,
                           task='Complete Homework',
                           task_description='for Python class',
                           start_date=datetime(2023,1,1),
                           due_date=datetime(2023,6,1))

for task in session.query(task_collection.database):
    print(task)
# # session.query(func.max(task_collection.task_id))
# # new_task = input('What task do you want to add? ')
# # task_description = input('Provide a brief description to the task ')
# # start_date = input('When do you want to start on this task? ')
# # due_date = input('When do you want to finish this task? ')
# #
# # task_collection.add_task(new_task, task_description, start_date, due_date)
# s = task_collection.select()
# result = model.conn.execute(s)
# row = result.fetchone()
# for x in row:
#    print(x)