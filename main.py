from flask import Flask, make_response, request, jsonify
from flask_restful import Api
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_socketio import join_room, leave_room



from apis.shops import Shops
from apis.orders import Orders, Order
from apis.drinks import Drinks
from apis.orderInfo import OrderInfo

from sqllite_helper import SqlLiteHelper

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins="*")


api.add_resource(Shops,'/shops')
api.add_resource(Orders,'/orders')
api.add_resource(Order,'/order/<orderNo>')

api.add_resource(Drinks,'/drinks')
api.add_resource(OrderInfo,'/orderInfo')


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
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL
  )'''

  drinkTab = '''CREATE TABLE DRINKS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    ShopID INTEGER NOT NULL,
    Price INTEGER NOT NULL,
    SizeID INTEGER NOT NULL
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