from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request
from flask_restful import Resource
from helper.pondaCrawler import PondaCralwer


class AddShop(Resource):
    def __init__(self):
        self.tabName = ''
        self.sqlHelper = SqlLiteHelper()
        self.crawler = PondaCralwer()

    def options(self):
        return {'Allow': '*'}, 200, \
               {'Access-Control-Allow-Origin': '*', \
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*'}


    def post(self):
        try:
            data = request.get_json(force=True)
            print(data)
            self.crawler.run(data['imgUrl'])
            # cmd = '''INSERT INTO {}(OrderNo, SHOPID) VALUES ('{}', '{}')'''.format(self.tabName, data['orderNo'], data['shopId'])
            # res =  self.sqlHelper.execute(cmd)
            # self.sqlHelper.commit()
            resp = make_response(jsonify({'code': 200,'data': 'sucess'}))
        except Exception as e:
          print('error', e)
          resp = make_response(jsonify({'code': 500, 'data': e }))

        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Headers'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = '*'
        return resp