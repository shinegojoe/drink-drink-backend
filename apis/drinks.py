from sqllite_helper import SqlLiteHelper
from flask import jsonify, make_response, request
from flask_restful import Resource


class Drinks(Resource):
    def __init__(self):
        self.tabName = 'DRINKS'
        self.drinkTitle = 'DRINKTITLES'
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

        cmd = 'SELECT * FROM {} WHERE shopId = {}'.format(self.drinkTitle, shopId)
        # cmd = 'SELECT * FROM {}'.format(self.tabName)
        drinkTitleRes = self.sqlHelper.execute(cmd)
        resObj = {}
        for drinkTitle in drinkTitleRes.fetchall():
          print(drinkTitle)
          # print(drinkTitle[2])
          cmd = 'SELECT * FROM {} WHERE drinkTitleId = {}'.format(self.tabName, drinkTitle[0])
          drinkRes = self.sqlHelper.execute(cmd)

          drinkList = []
          for drink in drinkRes.fetchall():
            print('dd', drink)
            data = {
              'id': drink[0],
              'name': drink[1],
              'info': drink[2],
              'price': drink[4]
            }
            drinkList.append(data)
          resObj[drinkTitle[1]] = drinkList




        # res =  self.sqlHelper.execute(cmd)
        # resList = []
        # for row in res.fetchall():
        #     data = {
        #     'id': row[0],
        #     'name': row[1],
        #     'shipId': row[2],
        #     'price': row[3],
        #     'sizeId': row[4]
        #     }
        #     resList.append(data)
        resp = make_response(jsonify({'code': 200,'data': resObj}))
  
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