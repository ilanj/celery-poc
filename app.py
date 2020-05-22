'''
23May - @ilanchezhian
'''
from flask import Flask
from flask_restful import Api, Resource
import time

from task import task

app = Flask(__name__)
api = Api(app)


class Main(Resource):

    def get(self):
        task.delay()
        time_now = time.strftime("%X")
        return "task queued and accepted "+time_now

api.add_resource(Main, '/')

if __name__ == "__main__":
    app.run(debug=True)

