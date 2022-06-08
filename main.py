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

    with model.engine.connect() as conn:
        if option == 'a':
            new_task = input('What task would you like to add? ')
            task_description = input('Provide a brief description to the task: ')
            task_collection.add_task(new_task,
                                     task_description)

        elif option == 'b':
            task.TaskCollection.print_task(task_collection)


