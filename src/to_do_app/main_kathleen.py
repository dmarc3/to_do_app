import task

while True:
    print(
        """
        A: Add task
        B: Print tasks ordered by task_id
        C: Print tasks ordered by due_date
        D: Print tasks ordered by priority
        E: Print completed tasks between specified dates
        F: List all overdue tasks
        G: Set a start date to a task
        H: Set a due date to a task
        I: Mark task as completed
        J: Delete status
        K: Change task name
        L: Change task description
        M: Set priority to task
        """
    )
    option = input('Select one of the above options: ')
    option = option.lower().strip()
    task_collection = task.TaskCollection()

    if option == 'a':
        new_task = input('What task would you like to add? ')
        task_description = input('Provide a brief description to the task: ')
        task_collection.add_task(new_task, task_description)

    elif option == 'b':
        task.TaskCollection.print_tasks(task_collection, 'task_id')

    elif option == 'c':
        task.TaskCollection.print_tasks(task_collection, 'due_date')

    elif option == 'd':
        task.TaskCollection.print_tasks(task_collection, 'priority')

    elif option == 'e':
        task.TaskCollection.print_tasks(task_collection, 'completed')

    elif option == 'f':
        task.TaskCollection.print_tasks(task_collection, 'overdue')

    elif option == 'g':
        task.TaskCollection.print_tasks(task_collection, 'task_id')
        task.TaskCollection.set_date(task_collection, 'start_date')

    elif option == 'h':
        task.TaskCollection.set_date(task_collection, 'due_date')

    elif option == 'i':
        task.TaskCollection.update_status(task_collection)

    elif option == 'j':
        task.TaskCollection.print_tasks(task_collection, 'task_id')
        task.TaskCollection.delete_status(task_collection)

    elif option == 'k':
        task.TaskCollection.print_tasks(task_collection, 'task_id')
        task.TaskCollection.update_data(task_collection, 'task')

    elif option == 'l':
        task.TaskCollection.print_tasks(task_collection, 'task_id')
        task.TaskCollection.update_data(task_collection, 'task_description')

    elif option == 'm':
        task.TaskCollection.print_tasks(task_collection, 'task_id')
        task.TaskCollection.update_data(task_collection, 'priority')
