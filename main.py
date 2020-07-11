from flask import Flask, make_response, request, jsonify
from flask import send_file, send_from_directory
from flask_restful import Api
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_socketio import join_room, leave_room



from apis.shops import Shops, Shop
from apis.orders import Orders, Order
from apis.drinks import Drinks
from apis.orderInfo import OrderInfo
from apis.addShop import AddShop

from sqllite_helper import SqlLiteHelper

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins="*")


api.add_resource(Shops,'/shops')
api.add_resource(Shop,'/shops/<id>')

api.add_resource(Orders,'/orders')
api.add_resource(Order,'/order/<orderNo>')

api.add_resource(Drinks,'/drinks')
api.add_resource(OrderInfo,'/orderInfo')
api.add_resource(AddShop,'/addShop')


@socketio.on('orderUpdate')
def handle_my_custom_event(data):
  print('xxx', data)
  room = data['room']
  emit('orderUpdate', data, room=room)


@socketio.on('join')
def on_join(data):
  print('join', data)
  username = data['username']
  room = data['room']
  join_room(room)
  emit('join', username + ' has entered the room.', room=room)

@app.route("/images/<filename>", methods=['GET'])
def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    directory = 'images'
    return send_from_directory(directory, filename, as_attachment=True)






def main():
  sqlHelper = SqlLiteHelper()
  # cmd = '''CREATE TABLE test2 (
  #   ID INTEGER PRIMARY KEY AUTOINCREMENT,
  #   NAME TEXT NOT NULL
  # )'''

  # projectsTab = '''CREATE TABLE Projects (
  #     ID INTEGER PRIMARY KEY AUTOINCREMENT,
  #     NAME TEXT NOT NULL
  #   )'''

  shopTab = '''CREATE TABLE SHOPS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    imgUrl TEXT NOT NULL
  )'''

  drinkTitleTab = '''CREATE TABLE DRINKTITLES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    shopId INTEGER NOT NULL

  )'''

  drinkTab = '''CREATE TABLE DRINKS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    info TEXT NOT NULL,
    drinkTitleId INTEGER NOT NULL,
    price INTEGER NOT NULL
  )'''

  orderTab = '''CREATE TABLE ORDERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    SHOPID INTEGER NOT NULL,
    OrderNO INTEGER NOT NULL
  )'''


  orderInfoTab = '''CREATE TABLE orderInfo (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT NOT NULL,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    iceId INTEGER NOT NULL,
    orderId INTEGER NOT NULL

  )'''

  # cmd2 = '''INSERT INTO test2(NAME) VALUES ('xxx'
  #     )'''
  # sqlHelper.execute(shopTab)

  # sqlHelper.execute(drinkTitleTab)
  # sqlHelper.execute(drinkTab)

  # sqlHelper.execute(orderTab)
  # sqlHelper.execute(orderInfoTab)

  # sqlHelper.execute(cmd2)
  # sqlHelper.commit()
  # sqlHelper.test()

  # app.run(host='0.0.0.0')
  socketio.run(app)




if __name__ == "__main__":
  main()