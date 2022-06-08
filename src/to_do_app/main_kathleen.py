from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import validation
import model
import task

engine = create_engine('sqlite:///task.db', echo=True, future=True)
model.task_detail.metadata.bind = engine
model.task_detail.metadata.create_all()

task_collection = task.TaskCollection()
task_collection.add_task('test', 'for python 320')

# while True:
#     print(
#         """
#         A: Add task
#         B: Print tasks
#         C: Update tasks
#         """
#     )
#     option = input('Select one of the above options: ')
#     option = option.lower().strip()
#     task_collection = task.TaskCollection(engine)
#
#     with Session(engine) as session:
#         if option == 'a':
#             task = input('What task would you like to add? ')
#             task_description = input('Provide a brief description to the task: ')
#             task_collection.add_task(task,
#                                      task_description)
#
#         elif option == 'b':
#             task.TaskCollection.print_task(task_collection)


