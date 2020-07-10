
from flask_restful import Resource
from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request

class Shops(Resource):
    def __init__(self):
      self.tabName = 'SHOPS'
      self.sqlHelper = SqlLiteHelper()
    
    def get(self): 
      try:
          cmd = 'SELECT * FROM {}'.format(self.tabName)
          res =  self.sqlHelper.execute(cmd)
          resList = []
          for row in res.fetchall():
              data = {
              'id': row[0],
              'name': row[1]
              }
              resList.append(data)
          resp = make_response(jsonify({'code': 200,'data': resList}))
  
      except Exception as e:
              print('error', e)
              resp = make_response(jsonify({'code': 500, 'data': {}}))
      
      return resp
    