import model
import task
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import session
from datetime import datetime
from sqlalchemy import select

import validation

while True:
    print(
        """
        A: Add task
        B: Print tasks
        """
    )
    option = input('Select one of the above options: ')
    option = option.lower().strip()
    task_collection = task.TaskCollection()

    if option == 'a':
        new_task = input('What task would you like to add? ')
        task_description = input('Provide a brief description to the task: ')
        start_month = validation.month_response('start')
        start_date = validation.day_response('start')
        start_year = validation.year_response('start')
        due_month = validation.month_response('finish')
        due_date = validation.day_response('finish')
        due_year = validation.year_response('finish')
        task_collection.add_task(new_task,
                                 task_description,
                                 datetime(start_year, start_month, start_date),
                                 datetime(due_year, due_month, due_date))

    elif option == 'b':
        task.TaskCollection.print_task(task_collection)


# task_collection = task.TaskCollection()
#
# try:
#     max_id = select(max([task_collection.database.c.task_id]) + 1)
# except:
#     max_id = 1
#
# task_collection.add_task(1, 'complete homework', 'for python class',datetime(2023,1,1), datetime(2023,6,1))

# ins = task_collection.database.insert().values(task_id=1,
#                            task='Complete Homework',
#                            task_description='for Python class',
#                            start_date=datetime(2023,1,1),
#                            due_date=datetime(2023,6,1))


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