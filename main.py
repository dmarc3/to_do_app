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
        C: Update tasks
        """
    )
    option = input('Select one of the above options: ')
    option = option.lower().strip()
    task_collection = task.TaskCollection()

    if option == 'a':
        new_task = input('What task would you like to add? ')
        task_description = input('Provide a brief description to the task: ')
        # start_month = validation.month_response('start')
        # start_date = validation.day_response('start')
        # start_year = validation.year_response('start')
        # due_month = validation.month_response('finish')
        # due_date = validation.day_response('finish')
        # due_year = validation.year_response('finish')
        task_collection.add_task(new_task,
                                 task_description,
                                 # datetime(start_year, start_month, start_date),
                                 # datetime(due_year, due_month, due_date)
        )

    elif option == 'b':
        task.TaskCollection.print_task(task_collection)

    elif option == 'c':

