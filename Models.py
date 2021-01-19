from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse, fields, Api
from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
import os

app = Flask(__name__)
api= Api(app)
databaseName="database.db"
wasDB= False
db= SQLAlchemy(app)
if os.path.exists(databaseName):
    wasDB=True

fullDB="sqlite:///"+databaseName
app.config["SQLALCHEMY_DATABASE_URI"]=fullDB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class RoomModel(db.Model):
    __tablename__= "Gallery"

    room_id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)
    debt = db.Column(db.Integer)

class ShopModel(db.Model):
    __tablename__ = "Shop"

    shop_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    industry = db.Column(db.String())
    room_id= db.Column(db.Integer, ForeignKey('Gallery.room_id'), nullable=False)


shop_fields={
    'shop_id': fields.Integer,
    'name' : fields.String,
    'industry' : fields.String,
    'room_id' : fields.Integer
}

room_fields={
    'room_id': fields.Integer,
    'rent' : fields.Integer,
    'debt' : fields.Integer
}

complex_fields={
'shop_id': fields.Integer,
    'name' : fields.String,
    'industry' : fields.String,
    'room_id' : fields.Integer,
    'room_id': fields.Integer,
    'rent' : fields.Integer,
    'debt' : fields.Integer
}

Room_Parser = reqparse.RequestParser()
Room_Parser.add_argument("room_id",type=int, help="Room id", required=True)
Room_Parser.add_argument("rent", type=int, help="Rent name", required=True)
Room_Parser.add_argument("debt",type=int, help="Room debt", required=True)


