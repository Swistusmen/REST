from Models import ShopModel, db, shop_fields, RoomModel
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort,fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

Shop_Parser = reqparse.RequestParser()
Shop_Parser.add_argument("shop_id",type=int, help="Shop id", required=True)
Shop_Parser.add_argument("name", type=str, help="Shop name", required=True)
Shop_Parser.add_argument("industry",type=str, help="industry", required=True)
Shop_Parser.add_argument("room_id",type=int, help="industry", required=True)

Shop_Updater=reqparse.RequestParser()
Shop_Updater.add_argument("shop_id",type=int, help="Shop id")
Shop_Updater.add_argument("name", type=str, help="Shop name")
Shop_Updater.add_argument("industry",type=str, help="industry")


class Shop(Resource):
    @marshal_with(shop_fields)
    def get(self, shop_id):
        result= ShopModel.query.filter_by(shop_id=shop_id).first()
        if not result:
            abort (404, message= "Shop is not in the data base")
        return result, 200

    @marshal_with(shop_fields)
    def put(self, shop_id):
        result = ShopModel.query.filter_by(shop_id=shop_id).first()
        if result:
            abort (406, message="Shop is already in database")
        args=Shop_Parser.parse_args()
        result=ShopModel(shop_id=shop_id, name=args['name'], industry=args['industry'], room_id=args['room_id'])
        room=RoomModel.query.filter_by(room_id=args['room_id']).first()
        if not room or room.debt!=0:
            abort( 406, message="This room is unavailable")
        updatedRoom = RoomModel(room_id=room.room_id, rent=room.rent, debt=0)
        RoomModel.query.filter_by(room_id=updatedRoom.room_id).delete()
        db.session.commit()
        db.session.add(updatedRoom)
        db.session.commit()
        db.session.add(result)
        db.session.commit()
        return args, 201

    @marshal_with(shop_fields)
    def post(self, shop_id):
        result = ShopModel.query.filter_by(shop_id=shop_id).first()
        args = Shop_Parser.parse_args()
        if result:
            result.name=args['name']
            result.industry=args['industry']
        else:
            room = RoomModel.query.filter_by(room_id=args['room_id']).first()
            if not room or room.debt != 0:
                abort(406, message="This room is unavailable")
            updatedRoom = RoomModel(room_id=room.room_id, rent=room.rent, debt=0)
            RoomModel.query.filter_by(room_id=updatedRoom.room_id).delete()
            db.session.commit()
            db.session.add(updatedRoom)
            db.session.commit()
            result = ShopModel(shop_id=shop_id, name=args['name'], industry=args['industry'],room_id=args['room_id'])
        db.session.add(result)
        db.session.commit()
        return args, 201

    @marshal_with(shop_fields)
    def delete(self, shop_id):
        ShopModel.query.filter_by(shop_id=shop_id).delete()
        db.session.commit()
        return 200





