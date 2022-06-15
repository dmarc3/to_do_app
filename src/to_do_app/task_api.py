from flask import Flask, jsonify
from flask_restful import Resource, Api
import main
import task


class Task(Resource):
    def get(self):
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query]}
        return jsonify(result)

    # def post(self):
    #     main.add_task(task_collection, [new_task, new_description, new_priority])


if __name__ == "__main__":
    task_collection = task.TaskCollection()
    app = Flask(__name__)
    api = Api(app)
    query = task_collection.sort_query('task_id', 'ASC')
    api.add_resource(Task, '/tasks')
    app.run(port="5002")
    task_collection.dispose()
        # elif option == 'b':
        #     new_task = input('What new task do you want to add? ')
        #     new_description = input('Describe the new task ')
        #     new_priority = input('How do you want to prioritize this task? ')
        #     # query = main.list_tasks(task_collection)
        #     api.add_resource(Task, '/tasks')
        #     query = main.list_tasks(task_collection)



# main.add_task(task_collection, ['testing new entry', 'python 320', '8'])
# main.delete_task(task_collection, '1')