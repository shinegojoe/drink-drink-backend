from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request
from flask_restful import Resource


class Orders(Resource):
    def __init__(self):
        self.tabName = 'orders'
        self.sqlHelper = SqlLiteHelper()

    def options(self):
        return {'Allow': '*'}, 200, \
               {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*'}

    
    def get(self): 
        try:
            cmd = 'SELECT * FROM {}'.format(self.tabName)
            res =  self.sqlHelper.execute(cmd)
            resList = []
            for row in res.fetchall():
                data = {
                'id': row[0],
                'shopId': row[1],
                'orderNo': row[2]
                }
                resList.append(data)
            resp = make_response(jsonify({'code': 200,'data': resList}))
    
        except Exception as e:
                print('error', e)
                resp = make_response(jsonify({'code': 500, 'data': {}}))

        return resp

    def post(self):
        try:
            data = request.get_json(force=True)
            print(data)
            cmd = '''INSERT INTO {}(OrderNo, SHOPID) VALUES ('{}', '{}')'''.format(self.tabName, data['orderNo'], data['shopId'])
            res =  self.sqlHelper.execute(cmd)
            self.sqlHelper.commit()
            resp = make_response(jsonify({'code': 200,'data': 'sucess'}))
        except Exception as e:
            resp = make_response(jsonify({'code': 500, 'data': {}}))

        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        return resp

class Order(Resource):
    def __init__(self):
        self.tabName = 'orders'
        self.sqlHelper = SqlLiteHelper()

    def options(self):
        return {'Allow': '*'}, 200, \
               {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*'}

    
    def get(self, orderNo): 
        try:
            cmd = 'SELECT * FROM {} WHERE orderNo={}'.format(self.tabName, orderNo)
            res =  self.sqlHelper.execute(cmd)
            resList = []
            for row in res.fetchall():
                data = {
                'id': row[0],
                'shopId': row[1],
                'orderNo': row[2]
                }
                resList = data
            resp = make_response(jsonify({'code': 200,'data': resList}))
    
        except Exception as e:
                print('error', e)
                resp = make_response(jsonify({'code': 500, 'data': {}}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'

        return resp