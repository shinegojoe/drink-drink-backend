from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request
from flask_restful import Resource


class Drinks(Resource):
    def __init__(self):
        self.tabName = 'drinks'
        self.sqlHelper = SqlLiteHelper()

    def options(self):
        return {'Allow': '*'}, 200, \
               {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*'}

    
    def get(self): 
      try:
        args = request.args
        # shopId = args['shopId']
        print('shopId', request)
        args = request.args
        print(args)
        shopId = args['shopId']
        print(shopId)

        cmd = 'SELECT * FROM {} WHERE shopId = {}'.format(self.tabName, shopId)
        # cmd = 'SELECT * FROM {}'.format(self.tabName)

        res =  self.sqlHelper.execute(cmd)
        resList = []
        for row in res.fetchall():
            data = {
            'id': row[0],
            'name': row[1],
            'shipId': row[2],
            'price': row[3],
            'sizeId': row[4]
            }
            resList.append(data)
        resp = make_response(jsonify({'code': 200,'data': resList}))
  
      except Exception as e:
              print('error', e)
              resp = make_response(jsonify({'code': 500, 'data': {}}))

      resp.headers['Access-Control-Allow-Origin'] = '*'
      resp.headers['Access-Control-Allow-Headers'] = '*'
      resp.headers['Access-Control-Allow-Methods'] = '*'
      return resp

    # def post(self):
    #     try:
    #         data = request.get_json(force=True)
    #         print(data)
    #         cmd = '''INSERT INTO {}(OrderNo, SHOPID) VALUES ('{}', '{}')'''.format(self.tabName, data['orderNo'], data['shopId'])
    #         res =  self.sqlHelper.execute(cmd)
    #         self.sqlHelper.commit()
    #         resp = make_response(jsonify({'code': 200,'data': 'sucess'}))
    #     except Exception as e:
    #         resp = make_response(jsonify({'code': 500, 'data': {}}))

    #     resp.headers['Access-Control-Allow-Origin'] = '*'
    #     resp.headers['Access-Control-Allow-Headers'] = '*'
    #     resp.headers['Access-Control-Allow-Methods'] = '*'
    #     return resp