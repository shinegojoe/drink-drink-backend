from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request
from flask_restful import Resource


class OrderInfo(Resource):
    def __init__(self):
        self.tabName = 'orderInfo'
        self.sqlHelper = SqlLiteHelper()

    def options(self):
        return {'Allow': '*'}, 200, \
               {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*'}

    
    def get(self): 
        try:
            args = request.args
            args = request.args
            orderId = args['orderId']
            print(orderId)
            cmd = 'SELECT * FROM {} WHERE orderId = {}'.format(self.tabName, orderId)
            res =  self.sqlHelper.execute(cmd)
            resList = []
            for row in res.fetchall():
                data = {
                'id': row[0],
                'userName': row[1],
                'name': row[2],
                'price': row[3],
                'iceId': row[4],
                'orderId': row[5],
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

    def post(self):
        try:
            data = request.get_json(force=True)
            print(data)
            cmd = '''INSERT INTO {}(username, name, price, iceId, orderId) VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(
              self.tabName, data['username'], data['name'], data['price'], data['iceId'], data['orderId'])
            res =  self.sqlHelper.execute(cmd)
            self.sqlHelper.commit()
            resp = make_response(jsonify({'code': 200,'data': 'sucess'}))
        except Exception as e:
          print('error', e)
          resp = make_response(jsonify({'code': 500, 'data': {}}))

        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        return resp