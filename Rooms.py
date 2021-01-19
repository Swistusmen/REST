from Models import ShopModel, db, fullDB, shop_fields, RoomModel, room_fields, Room_Parser, complex_fields
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort,fields, marshal_with


class Rooms(Resource):
    @marshal_with(complex_fields)
    def get(self):
        shops=ShopModel.query.all()
        shop_list=[]
        taken=[]
        for i in shops:
            room=RoomModel.query.filter_by(room_id=i.room_id).first()
            shop_list.append({"shop_id":i.shop_id,"name":i.name,"industry":i.industry ,"room_id":i.room_id,"rent":room.rent,"debt":room.debt})
            taken.append(i.room_id)
        print(shop_list)
        AllRooms=RoomModel.query.all()
        for i in AllRooms:
            if i.room_id not in taken:
                shop_list.append({"shop_id":-1,"name":"empty","industry":"empty" ,"room_id":i.room_id,"rent":i.rent,"debt":i.debt})
        print(shop_list)
        return shop_list, 200