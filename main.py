import model
# import sqlalchemy.orm.query
from sqlalchemy.orm import session
from sqlalchemy import insert

db = model.Base.metadata.create_all(model.engine)

new_task = model.Task(task_id = 1,
                      task = 'Complete homework')

db.session.add(new_task)
db.session.commit()

check = db.select([model.Task]).where(modTask.columns.task_id == 1)