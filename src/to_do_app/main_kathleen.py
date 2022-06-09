from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import validation
import model
import task

engine = create_engine('sqlite:///task.db', echo=True, future=True)
model.Task.metadata.bind = engine
model.Task.metadata.create_all()


while True:
    print(
        """
        A: Add task
        B: Print tasks
        C: Set a start date to a task
        D: Set a due date to a task
        E: Mark task as completed
        """
    )
    option = input('Select one of the above options: ')
    option = option.lower().strip()
    task_collection = task.TaskCollection(engine)

    with Session(engine) as session:
        if option == 'a':
            task = input('What task would you like to add? ')
            task_description = input('Provide a brief description to the task: ')
            task_collection.add_task(task,
                                     task_description)

        elif option == 'b':
            task.TaskCollection.print_tasks(task_collection)

        elif option == 'c':
            task.TaskCollection.set_date(task_collection, 'start_date')

        elif option == 'd':
            task.TaskCollection.set_date(task_collection, 'due_date')

        elif option == 'e':
            task.TaskCollection.update_status(task_collection)