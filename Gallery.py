from Models import ShopModel, db, fullDB, shop_fields, RoomModel, room_fields, Room_Parser, complex_fields
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort,fields, marshal_with

from flask_sqlalchemy import SQLAlchemy


class Gallery(Resource):
    @marshal_with(complex_fields)
    def get(self, room_id):
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

    @marshal_with(room_fields)
    def put(self, room_id):
        result = RoomModel.query.filter_by(room_id=room_id).first()
        if result:
            abort(406, message="Shop is already in database")
        args = Room_Parser.parse_args()
        result = RoomModel(room_id=room_id, rent=args['rent'], debt=args['debt'])

        db.session.add(result)
        db.session.commit()
        return args, 201

    @marshal_with(room_fields)
    def post(self,room_id):
        result = RoomModel.query.filter_by(room_id=room_id).first()
        args= Room_Parser.parse_args()
        if result:
            result.debt=args['debt']
            result.rent=args['rent']
        else:
            result=RoomModel(room_id=room_id, rent=args['rent'], debt=args['debt'])
        db.session.add(result)
        db.session.commit()
        return args, 201

