from flask import Flask
from flask_restful import Resource, Api
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from preference import preference

sys.path.append(preference.db_path)
from mySqlService import mySqlService


app = Flask(__name__)
api = Api(app)


class Bobae(Resource):
    def get(self):
        sql = mySqlService()
        link = sql.selectLink()
        return {'status': 'success', 'link': link}

api.add_resource(Bobae, '/link')    

if __name__ == '__main__':
    app.run(debug=True)
    

    
