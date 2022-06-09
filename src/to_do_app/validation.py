from datetime import date

today_year = date.today().year


def month_response(date_type):
    month = input(f'What month would you like to {date_type} on this task?'
                  f' Please provide the month in numeric form ')
    while True:
        try:
            month = month.strip().lower()
            month = int(month)
            if 1 <= month <= 12:
                return month
            else:
                month = input('This is not a legitimate month! Please provide a new one: ')
        except ValueError:
            month = input('Please provide the month in numeric form! Please provide again ')


def day_response(date_type):
    day = input(f'What day would you like to {date_type} on this task?'
                  f' Please provide the month in numeric form ')
    while True:
        try:
            day = day.strip().lower()
            day = int(day)
            if 1 <= day <= 31:
                return day
            else:
                day = input('This is not a legitimate day! Please provide a new one: ')
        except ValueError:
            day = input('Please provide the day in numeric form! Please provide again ')


def year_response(date_type):
    year = input(f'What year would you like to {date_type} on this task?'
                  f' Please provide the year in numeric form ')
    while True:
        try:
            year = year.strip().lower()
            year = int(year)
            if year >= today_year:
                return year
            else:
                year = input('The year has passed! Try again ')
        except ValueError:
            year = input('Please provide the year in numeric form! Please provide again ')


def task_id_response(column_name):
    task_id = input(f'Which task would you want to update the {column_name} for?')
    while True:
        try:
            task_id = task_id.strip().lower()
            task_id = int(task_id)
            return task_id
        except ValueError:
            task_id = input('Please provide the task id in numeric form! Please provide again ')


def priority_response(task):
    priority = input(f'How would you like to set the priority for task_id {task}? Please choose between 1-10: ')
    while True:
        try:
            priority = priority.strip().lower()
            priority = int(priority)
            1 <= priority <= 10
            return priority
        except ValueError:
            priority = input('Please provide the priority in numeric form! Please provide again ')