from flask import Flask, jsonify
from flask_restful import Resource, Api
import main
import task


class Task(Resource):
    def get(self):
        query = main.list_tasks(db_connect)
        result = {'task': [i[1] for i in query]}
        return jsonify(result)

    def post(self):



if __name__ == "__main__":
    while True:
        print("""
        A. Review current data.
        B. Add data.
        """)
        option = input('Which option would you like to select from above? ')
        option = option.strip().lower()
        db_connect = task.TaskCollection()
        if option == 'a':
            app = Flask(__name__)
            api = Api(app)
            api.add_resource(Task, "/tasks") # Route_1
            app.run(port="5002")
            db_connect.dispose()
